# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the DNS service in the Python SDK. This script accepts two
# arguments:
#
#   * The first argument is the OCID of the compartment where we'll create a DNS zone
#   * The second is the name of the DNS zone to create (e.g. my-example-zone.com)

import oci
import sys


def get_all_zone_records(dns_client, zone_name, zone_version):
    all_records = []
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',  # Iterate through the raw responses
        zone_name,
        zone_version=zone_version
    )
    for response in all_records_generator:
        # Each response contains a header which has the total number of records. This can
        # be accessed via:
        #   response.headers.get('opc-total-items')
        all_records.extend(response.data.items)

    return all_records


def get_all_domain_records(dns_client, zone_name, domain, zone_version):
    all_records = []
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',  # Iterate through the raw responses
        zone_name,
        domain,
        zone_version=zone_version
    )
    for response in all_records_generator:
        all_records.extend(response.data.items)

    return all_records


def get_all_rr_set_records(dns_client, zone_name, domain, zone_version, rtype):
    all_records = []
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_rr_set,
        'response',  # Iterate through the raw responses
        zone_name,
        domain,
        rtype,
        zone_version=zone_version
    )
    for response in all_records_generator:
        all_records.extend(response.data.items)

    return all_records


def get_zone(dns_client, zone_name):
    return dns_client.get_zone(zone_name).data


# Default config file and profile
config = oci.config.from_file()
dns_client = oci.dns.DnsClient(config)

if len(sys.argv) != 4:
    raise RuntimeError('This script expects an argument of a compartment OCID where the zone will be created,  the name of the zone, and a target compartment OCID to which the zone will be moved.')

# The first argument is the name of the script, so start the index at 1
compartment_id = sys.argv[1]
zone_name = sys.argv[2]
target_compartment_id = sys.argv[3]

create_response = dns_client.create_zone(
    oci.dns.models.CreateZoneDetails(
        name=zone_name,
        zone_type='PRIMARY',
        compartment_id=compartment_id
    )
)

print('Created zone:\n{}'.format(create_response.data))
print('\n=========================\n')

# This will just get all the zones
all_zones = oci.pagination.list_call_get_all_results(dns_client.list_zones, compartment_id)
print('All zones:\n{}'.format(all_zones.data))

# We can also provide filter conditions and sort order to the list_zones operation. Here we filter based
# on an exact name match and filter by the time the zone was created descending
zones_matching_name = oci.pagination.list_call_get_all_results(
    dns_client.list_zones,
    compartment_id,
    name=zone_name,
    sort_by='timeCreated',
    sort_order='DESC'
)
print('All zones with sort and filter:\n{}'.format(zones_matching_name.data))
print('\n=========================\n')

# We can update records in the zone. This will overwrite any existing records so if there are items
# we wish to keep (e.g. the NS records in the zone) we need to read those out first and make
# sure they are included in the update.
#
# Note, also, that when updating zone records we can add records with different rtypes and also
# for different domains in the zone

# get_zone_records is a paginated operation, so we can use operations in the oci.pagination module
# to handle getting pages of data for us, rather than handling page tokens ourselves. We're also
# supplying some additional filter criteria to get_zone_records to narrow down what gets returned
original_zone_ns_records_generator = oci.pagination.list_call_get_all_results_generator(
    dns_client.get_zone_records,
    'response',
    zone_name,
    zone_version=zones_matching_name.data[0].version,  # Make sure we use the correct version when getting records
    domain=zone_name,
    compartment_id=compartment_id,
    rtype='NS'
)
original_ns_records = []
for response in original_zone_ns_records_generator:
    original_ns_records.extend(response.data.items)

print('Original NS records:\n{}'.format(original_ns_records))

# Here we prepare our update - this will include the NS records, plus a TXT record for the top level
# domain and an A record for a subdomain
update_zone_records = []
for ns_record in original_ns_records:
    update_zone_records.append(
        oci.dns.models.RecordDetails(
            domain=ns_record.domain,
            ttl=ns_record.ttl,
            rtype='NS',
            record_hash=ns_record.record_hash,
            rdata=ns_record.rdata,
            rrset_version=ns_record.rrset_version,
            is_protected=True
        )
    )
update_zone_records.extend([
    oci.dns.models.RecordDetails(
        domain=zone_name,
        ttl=30,
        rtype='TXT',
        rdata='Some textual data'
    ),
    oci.dns.models.RecordDetails(
        domain='testsubdomain1.{}'.format(zone_name),
        ttl=1800,
        rtype='A',
        rdata='127.0.0.1'
    )
])

dns_client.update_zone_records(
    zone_name,
    oci.dns.models.UpdateZoneRecordsDetails(items=update_zone_records)
)

# When retrieving records, we can optionally specify what version of the zone we want records for. In this case,
# we explicitly want the latest version, which we can get by retrieving the zone and then interrogating its
# version. Specifying different versions is also possible
records_after_update = get_all_zone_records(
    dns_client,
    zone_name,
    get_zone(dns_client, zone_name).version
)
print('Updated zone records:\n{}'.format(records_after_update))
print('\n=========================\n')

# In addition to updates, we can use the patch operation to add and remove records from the zone without
# having to send through the complete list of records each time. In this example, we'll remove the existing
# TXT record and add a new one in

txt_record = None
for record in records_after_update:
    if record.rtype == 'TXT':
        txt_record = record
        break

patch_add_remove_txt_record = [
    oci.dns.models.RecordOperation(
        domain=zone_name,
        record_hash=txt_record.record_hash,
        rtype='TXT',
        rdata=txt_record.rdata,
        operation='REMOVE'
    ),
    oci.dns.models.RecordOperation(
        domain=zone_name,
        rtype='TXT',
        ttl=45,
        rdata='Patch new text data',
        operation='ADD'
    )
]
dns_client.patch_zone_records(
    zone_name,
    oci.dns.models.PatchZoneRecordsDetails(items=patch_add_remove_txt_record)
)

records_after_patch = get_all_zone_records(
    dns_client,
    zone_name,
    get_zone(dns_client, zone_name).version
)
print('Zone records after patch:\n{}'.format(records_after_patch))
print('\n=========================\n')

# As part of patch operations, we can also specify preconditions (REQUIRE - data must be present, and
# PROHIBIT - data must not be present) which must be met for the operation to succeed.
#
# As of the time of writing (6 February 2018), these preconditions cannot contain rdata or record_hash
# fields

a_record = None
for record in records_after_update:
    if record.rtype == 'A':
        a_record = record
        break

failing_patch_operation = [
    oci.dns.models.RecordOperation(  # This will fail as nothing matches this criteria
        domain='testsubdomain1.{}'.format(zone_name),
        rtype='A',
        rrset_version='1234567',
        operation='REQUIRE'
    ),
    oci.dns.models.RecordOperation(
        domain='testsubdomain1.{}'.format(zone_name),
        rtype='A',
        ttl=1800,
        rdata='127.0.0.2',
        operation='ADD'
    )
]

try:
    dns_client.patch_zone_records(
        zone_name,
        oci.dns.models.PatchZoneRecordsDetails(items=failing_patch_operation)
    )
except oci.exceptions.ServiceError as e:
    print('Patch with bad precondition failed with status: {}'.format(e.status))

# This operation will succeed since we're asking that something matching the criteria doesn't exist (PROHIBIT). Note
# also that the TTL will be applied to all other A records in the domain (i.e. our existing A record will have its
# TTL changed to 2100)
successful_patch_operation = [
    oci.dns.models.RecordOperation(
        domain='testsubdomain1.{}'.format(zone_name),
        rtype='A',
        rrset_version='1234567',
        operation='PROHIBIT'
    ),
    oci.dns.models.RecordOperation(
        domain='testsubdomain1.{}'.format(zone_name),
        rtype='A',
        ttl=2100,
        rdata='127.0.0.2',
        operation='ADD'
    )
]

dns_client.patch_zone_records(
    zone_name,
    oci.dns.models.PatchZoneRecordsDetails(items=successful_patch_operation)
)

records_after_patch = get_all_zone_records(
    dns_client,
    zone_name,
    get_zone(dns_client, zone_name).version
)
print('Zone records after patch with preconditions:\n{}'.format(records_after_patch))
print('\n=========================\n')

# We can also do update and patch operations at the domain level. This can handle records with different rtypes
# but they must all be in the same domain

subdomain = "testsubdomain2.{}".format(zone_name)
all_domain_records = get_all_domain_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version)

# Initially the domain should not have any records
print('Current domain records: {}'.format(all_domain_records))

update_domain_records = [
    oci.dns.models.RecordDetails(
        domain=subdomain,
        ttl=30,
        rtype='TXT',
        rdata='Subdomain text'
    ),
    oci.dns.models.RecordDetails(
        domain=subdomain,
        ttl=900,
        rtype='A',
        rdata='127.0.0.7'
    )
]

dns_client.update_domain_records(
    zone_name,
    subdomain,
    oci.dns.models.UpdateDomainRecordsDetails(items=update_domain_records)
)

all_domain_records = get_all_domain_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version)
print('Domain records after update:\n{}'.format(all_domain_records))

a_record = None
txt_record = None
for record in all_domain_records:
    if record.rtype == 'A':
        a_record = record
    elif record.rtype == 'TXT':
        txt_record = record

# Patch operations at the domain level function similarly to patch operations at the zone level, in that we can send through
# partial updates (additions and removals) and also specify preconditions
#
# Here we specify two preconditions (which should succeed):
#   * TXT records match the given RRSet version
#   * A records have the given TTL
#
# And if that is successful we'll update the TTL of the existing A record
domain_patch_operations = [
    oci.dns.models.RecordOperation(
        domain=subdomain,
        rtype='TXT',
        rrset_version=txt_record.rrset_version,
        operation='REQUIRE'
    ),
    oci.dns.models.RecordOperation(
        domain=subdomain,
        rtype='A',
        ttl=a_record.ttl,
        operation='REQUIRE'
    ),
    oci.dns.models.RecordOperation(
        domain=subdomain,
        ttl=1000,
        rtype='A',
        rdata='127.0.0.7',
        operation='ADD'
    )
]

dns_client.patch_domain_records(
    zone_name,
    subdomain,
    oci.dns.models.PatchDomainRecordsDetails(items=domain_patch_operations)
)

all_domain_records = get_all_domain_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version)
print('Domain records after patch:\n{}'.format(all_domain_records))
print('\n=========================\n')

# We can also delete records from the domain
dns_client.delete_domain_records(zone_name, subdomain)

all_domain_records = get_all_domain_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version)
print('Domain records after delete:\n{}'.format(all_domain_records))
print('\n=========================\n')

# We can also do update and patch operations at the RRSet level. This is scoped to a particular domain and rtype.

subdomain = 'testsubdomain3.{}'.format(zone_name)

all_rr_set_records = get_all_rr_set_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version, 'TXT')

# Initially the RRSet should not have any records as we're using a "fresh" subdomain
print('Current RRSet records: {}'.format(all_rr_set_records))

update_rr_set = [
    oci.dns.models.RecordDetails(
        domain=subdomain,
        rtype='TXT',
        ttl=100,  # TTL should be consistent on each RecordDetails
        rdata='rec1'
    ),
    oci.dns.models.RecordDetails(
        domain=subdomain,
        rtype='TXT',
        ttl=100,
        rdata='rec2'
    )
]

dns_client.update_rr_set(
    zone_name,
    subdomain,
    'TXT',
    oci.dns.models.UpdateRRSetDetails(items=update_rr_set)
)

all_rr_set_records = get_all_rr_set_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version, 'TXT')
print('RRSet records after update: {}'.format(all_rr_set_records))

# Patch operations on RRSets function similar to elsewhere in that we can send through
# partial updates (additions and removals) and also specify preconditions.
#
# Here we specify a precondition on the TTL, and also remove one record and add another. Note that the new TTL specified
# will apply to all records

patch_rr_set_operations = [
    oci.dns.models.RecordOperation(
        domain=subdomain,
        rtype='TXT',
        ttl=101,
        operation='PROHIBIT'
    ),
    oci.dns.models.RecordOperation(
        domain=subdomain,
        rtype='TXT',
        record_hash=all_rr_set_records[1].record_hash,
        # Currently (as of 6 Feb 2018) for a TXT record, if you want to send in rdata for an EXISTING record then it should be quoted. For example:
        #   - '"Hello" "World"' instead of 'Hello World'
        #   - '"rec3"' instead of 'rec3'
        rdata=all_rr_set_records[1].rdata,
        operation='REMOVE'
    ),
    oci.dns.models.RecordOperation(
        domain=subdomain,
        rtype='TXT',
        ttl=101,
        rdata='rec3',  # For new TXT records, we don't need to quote it
        operation='ADD'
    )
]

dns_client.patch_rr_set(
    zone_name,
    subdomain,
    'TXT',
    oci.dns.models.PatchRRSetDetails(items=patch_rr_set_operations)
)

all_rr_set_records = get_all_rr_set_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version, 'TXT')
print('RRSet records after patch: {}'.format(all_rr_set_records))

# We can also delete records from the RRSet
dns_client.delete_rr_set(zone_name, subdomain, 'TXT')

all_rr_set_records = get_all_rr_set_records(dns_client, zone_name, subdomain, get_zone(dns_client, zone_name).version, 'TXT')
print('RRSet records after delete: {}'.format(all_rr_set_records))
print('\n=========================\n')

# We can also move the the zone to a new compartment
dns_client.change_zone_compartment(get_zone(dns_client, zone_name).zone_id, target_compartment_id)

dns_client.delete_zone(zone_name)
print('Deleted zone')
