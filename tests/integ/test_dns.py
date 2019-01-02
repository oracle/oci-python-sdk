# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from . import util
from .. import test_config_container
import oci


# DNS operations for getting records (at the zone, domain or RRSet level) are GETs but they have the
# characteristics of a pagination operation in that they accept page tokens and have a limit parameter.
#
# However, they are unlike pagination operations as they wrap results in a RecordCollection (which currently
# has a single .items attribute) rather than returning the results inline.
def test_record_collection_pagination(dns_client):
    zone_name = '{}.com'.format(util.random_name('python-sdk-testing-', insert_underscore=False))

    with test_config_container.create_vcr().use_cassette('test_dns_record_collection_pagination.yml'):
        try:
            create_zone_details = oci.dns.models.CreateZoneDetails(
                name=zone_name,
                zone_type='PRIMARY',
                compartment_id=util.COMPARTMENT_ID
            )
            dns_client.create_zone(create_zone_details)

            # At the zone level, there are multiple NS records and an SOA record so we can paginate through
            # those as a sanity test that iterating over a RecordCollection works
            all_zone_records = oci.pagination.list_call_get_all_results(
                dns_client.get_zone_records,
                zone_name,
                limit=1  # 1 record at a time
            )
            assert len(all_zone_records.data.items) > 0

            zone_records_to_limit = oci.pagination.list_call_get_up_to_limit(
                dns_client.get_zone_records,
                4,
                1,
                zone_name
            )
            assert len(zone_records_to_limit.data.items) == 4

            # Try the generator variants where we yield individual records. The list_call_get_all_results
            # and list_call_get_up_to_limit leverage the generator variants where we yield responses, so we
            # have already tested them via inference
            all_records_generator = oci.pagination.list_call_get_all_results_generator(
                dns_client.get_zone_records,
                'record',
                zone_name,
                limit=1
            )
            num_records = 0
            for record in all_records_generator:
                num_records += 1
                assert isinstance(record, oci.dns.models.Record)
            assert num_records > 0

            records_to_limit_generator = oci.pagination.list_call_get_up_to_limit_generator(
                dns_client.get_zone_records,
                4,
                1,
                'record',
                zone_name
            )
            num_records = 0
            for record in records_to_limit_generator:
                num_records += 1
                assert isinstance(record, oci.dns.models.Record)
            assert num_records == 4
        finally:
            zones = get_zones(dns_client, name=zone_name)
            for z in zones.data:
                delete_zone(dns_client, z.name)
                break


# We want to paginate on RRSets, but these use a different type than GetZoneRecords and GetDomainRecords, so have a
# different test case for that
def test_rrset_pagination(dns_client):
    zone_name = '{}.com'.format(util.random_name('python-sdk-testing-', insert_underscore=False))

    with test_config_container.create_vcr().use_cassette('test_dns_rrset_pagination.yml'):
        try:
            create_zone_details = oci.dns.models.CreateZoneDetails(
                name=zone_name,
                zone_type='PRIMARY',
                compartment_id=util.COMPARTMENT_ID
            )
            dns_client.create_zone(create_zone_details)

            # At the zone level, there are multiple NS records so we can paginate through
            # those as a sanity test that iterating over a RecordCollection works
            all_rrset_records = oci.pagination.list_call_get_all_results(
                dns_client.get_rr_set,
                zone_name,  # zone
                zone_name,  # domain
                'NS',
                limit=1  # 1 record at a time
            )
            assert len(all_rrset_records.data.items) > 0

            rrset_records_to_limit = oci.pagination.list_call_get_up_to_limit(
                dns_client.get_rr_set,
                2,
                1,
                zone_name,
                zone_name,
                'NS'
            )
            assert len(rrset_records_to_limit.data.items) == 2

            # Try the generator variants where we yield individual records. The list_call_get_all_results
            # and list_call_get_up_to_limit leverage the generator variants where we yield responses, so we
            # have already tested them via inference
            all_records_generator = oci.pagination.list_call_get_all_results_generator(
                dns_client.get_rr_set,
                'record',
                zone_name,
                zone_name,
                'NS',
                limit=1
            )
            num_records = 0
            for record in all_records_generator:
                num_records += 1
                assert isinstance(record, oci.dns.models.Record)
            assert num_records > 0

            records_to_limit_generator = oci.pagination.list_call_get_up_to_limit_generator(
                dns_client.get_rr_set,
                2,
                1,
                'record',
                zone_name,
                zone_name,
                'NS'
            )
            num_records = 0
            for record in records_to_limit_generator:
                num_records += 1
                assert isinstance(record, oci.dns.models.Record)
            assert num_records == 2
        finally:
            zones = get_zones(dns_client, name=zone_name)
            for z in zones.data:
                delete_zone(dns_client, z.name)
                break


def test_crud_zone(dns_client):
    zone_name = '{}.com'.format(util.random_name('python-sdk-testing-', insert_underscore=False))

    with test_config_container.create_vcr().use_cassette('test_dns.yml'):
        try:
            create_zone_details = oci.dns.models.CreateZoneDetails(
                name=zone_name,
                zone_type='PRIMARY',
                compartment_id=util.COMPARTMENT_ID
            )
            create_response = dns_client.create_zone(create_zone_details)
            assert create_response.request_id
            assert create_response.headers.get('ETag')
            assert create_response.data
            assert create_response.data.id
            assert 'PRIMARY' == create_response.data.zone_type
            assert zone_name == create_response.data.name
            assert create_response.data.time_created
            assert len(create_response.data.external_masters) == 0
            assert create_response.data.version is not None
            assert create_response.data.serial is not None
            assert create_response.data.self_uri
            assert util.COMPARTMENT_ID == create_response.data.compartment_id

            zone_id = create_response.data.id
            zones = get_zones(dns_client, name=zone_name)
            assert len(zones.data) == 1
            assert zones.data[0].id == zone_id

            zone_by_name = dns_client.get_zone(zone_name)
            assert zone_by_name.request_id
            assert zone_by_name.headers.get('ETag')
            assert 'PRIMARY' == zone_by_name.data.zone_type
            assert len(zone_by_name.data.external_masters) == 0
            assert zone_id == zone_by_name.data.id
            assert util.COMPARTMENT_ID == create_response.data.compartment_id
            assert zone_by_name.data.version is not None
            assert zone_by_name.data.serial is not None
            assert zone_by_name.data.self_uri is not None

            zone_by_id = dns_client.get_zone(zone_id)
            assert zone_by_id.request_id
            assert zone_by_name.headers.get('ETag') == zone_by_id.headers.get('ETag')
            assert zone_by_name.data == zone_by_id.data

            update_zone_details = oci.dns.models.UpdateZoneDetails(
                external_masters=[]
            )
            update_response = dns_client.update_zone(zone_name, update_zone_details)
            assert update_response.request_id
            assert update_response.headers.get('ETag')
            assert len(update_response.data.external_masters) == 0

            # Update and patch operations can take either the zone name or the zone OCID, so test
            # using both

            update_zone_records(dns_client, zone_name, zone_name)
            update_zone_records(dns_client, zone_id, zone_name)

            patch_zone_records(dns_client, zone_name, zone_name)
            patch_zone_records(dns_client, zone_id, zone_name)

            update_domain_records(dns_client, zone_name, zone_name, "testsubdomain")
            update_domain_records(dns_client, zone_id, zone_name, "testsubdomain")

            patch_domain_records(dns_client, zone_name, zone_name, "testsubdomain")
            patch_domain_records(dns_client, zone_id, zone_name, "testsubdomain")

            update_rr_set_records(dns_client, zone_name, zone_name, "testsubdomain")
            update_rr_set_records(dns_client, zone_id, zone_name, "testsubdomain")

            patch_rr_set_records(dns_client, zone_name, zone_name, "testsubdomain")
            patch_rr_set_records(dns_client, zone_id, zone_name, "testsubdomain")
        finally:
            zones = get_zones(dns_client, name=zone_name)
            for z in zones.data:
                delete_zone(dns_client, z.name)
                break


# zone_name_or_id is to pass as the identifier to service operations
# zone_name is to use for forming domain/subdomain names
def update_zone_records(dns_client, zone_name_or_id, zone_name):
    zone_version = get_zone(dns_client, zone_name_or_id).version

    get_zone_records_kwargs = {
        'zone_version': zone_version,
        'domain': zone_name,
        'compartment_id': util.COMPARTMENT_ID,
    }

    get_zone_records_kwargs['rtype'] = 'NS'
    ns_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    original_ns_records = []
    for response in ns_records_generator:
        original_ns_records.extend(response.data.items)
    assert len(original_ns_records) > 0

    get_zone_records_kwargs['rtype'] = 'TXT'
    txt_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    original_txt_records = []
    for response in txt_records_generator:
        original_txt_records.extend(response.data.items)
    assert len(original_txt_records) == 0

    # We need to add the NS records here so that an UpdateZoneRecords call doesn't blow them away
    update_zone_record_items = []
    for ns_record in original_ns_records:
        assert 'NS' == ns_record.rtype
        assert zone_name == ns_record.domain
        assert ns_record.record_hash
        assert ns_record.rdata
        assert ns_record.ttl
        assert ns_record.rrset_version

        update_zone_record_items.append(
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

    update_zone_record_items.append(
        oci.dns.models.RecordDetails(
            domain=zone_name,
            ttl=30,
            rtype='TXT',
            rdata='Some textual data'
        )
    )

    update_response = dns_client.update_zone_records(
        zone_name_or_id,
        oci.dns.models.UpdateZoneRecordsDetails(items=update_zone_record_items)
    )
    assert update_response.request_id
    assert update_response.headers.get('ETag')
    assert int(update_response.headers.get('opc-total-items')) > 0
    assert len(update_response.data.items) == int(update_response.headers.get('opc-total-items'))

    zone_version = get_zone(dns_client, zone_name_or_id).version

    get_zone_records_kwargs['rtype'] = 'NS'
    get_zone_records_kwargs['zone_version'] = zone_version
    ns_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    updated_ns_records = []
    for response in ns_records_generator:
        updated_ns_records.extend(response.data.items)
    assert len(updated_ns_records) == len(original_ns_records)
    for original in original_ns_records:
        assert original in updated_ns_records

    get_zone_records_kwargs['rtype'] = 'TXT'
    txt_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    updated_txt_records = []
    for response in txt_records_generator:
        updated_txt_records.extend(response.data.items)
    assert len(updated_txt_records) == 1
    assert 'TXT' == updated_txt_records[0].rtype
    assert zone_name == updated_txt_records[0].domain
    assert updated_txt_records[0].record_hash
    assert '"Some" "textual" "data"' == updated_txt_records[0].rdata
    assert 30 == updated_txt_records[0].ttl
    assert updated_txt_records[0].rrset_version

    get_zone_records_kwargs.pop('rtype')
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    num_ns_records = 0
    num_txt_records = 0
    num_soa_records = 0
    total_records = 0
    for response in all_records_generator:
        for item in response.data.items:
            total_records += 1
            if item.rtype == 'NS':
                num_ns_records += 1
            elif item.rtype == 'TXT':
                num_txt_records += 1
            elif item.rtype == 'SOA':
                num_soa_records += 1
    assert len(updated_ns_records) == num_ns_records
    assert len(updated_txt_records) == num_txt_records
    assert 1 == num_soa_records
    assert num_ns_records + num_txt_records + num_soa_records == total_records

    delete_rr_set_records(dns_client, zone_name_or_id, zone_name, 'TXT')
    zone_version = get_zone(dns_client, zone_name_or_id).version

    get_zone_records_kwargs['zone_version'] = zone_version
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    num_ns_records = 0
    num_txt_records = 0
    num_soa_records = 0
    total_records = 0
    for response in all_records_generator:
        for item in response.data.items:
            total_records += 1
            if item.rtype == 'NS':
                num_ns_records += 1
            elif item.rtype == 'TXT':
                num_txt_records += 1
            elif item.rtype == 'SOA':
                num_soa_records += 1
    assert 0 == num_txt_records
    assert 1 == num_soa_records
    assert len(updated_ns_records) == num_ns_records
    assert num_ns_records + num_soa_records == total_records


def patch_zone_records(dns_client, zone_name_or_id, zone_name):
    # The zone already has NS and SOA records, so patch add/remove records and make sure that the NS
    # and SOA records are not impacted

    failing_patch_zone_records = [
        # This should fail because of a bad version
        oci.dns.models.RecordOperation(
            domain=zone_name,
            rrset_version='99',
            rtype='TXT',
            operation='REQUIRE'
        ),

        # This is a "good" operation that would otherwise succeed
        oci.dns.models.RecordOperation(
            domain=zone_name,
            ttl=45,
            rtype='TXT',
            rdata='Patched text data',
            operation='ADD'
        )
    ]

    try:
        dns_client.patch_zone_records(
            zone_name_or_id,
            oci.dns.models.PatchZoneRecordsDetails(items=failing_patch_zone_records)
        )
    except oci.exceptions.ServiceError as e:
        assert e.status == 409

    successful_patch_zone_records = [
        # This should succeed as the version does not exist
        oci.dns.models.RecordOperation(
            domain=zone_name,
            rrset_version='99',
            rtype='TXT',
            operation='PROHIBIT'
        ),
        oci.dns.models.RecordOperation(
            domain=zone_name,
            ttl=45,
            rtype='TXT',
            rdata='Patched text data',
            operation='ADD'
        ),
        oci.dns.models.RecordOperation(
            domain='testsubdomain.{}'.format(zone_name),
            rtype='A',
            ttl=3600,
            rdata='127.0.0.1',
            operation='ADD'
        )
    ]

    patch_response = dns_client.patch_zone_records(
        zone_name_or_id,
        oci.dns.models.PatchZoneRecordsDetails(items=successful_patch_zone_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert len(patch_response.data.items) > 0
    assert int(patch_response.headers.get('opc-total-items')) == len(patch_response.data.items)

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_zone_records_kwargs = {
        'zone_version': zone_version,
        'compartment_id': util.COMPARTMENT_ID,
    }
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    all_records = []
    for response in all_records_generator:
        all_records.extend(response.data.items)

    txt_records = []
    a_records = []
    num_ns_records = 0
    num_soa_records = 0
    for record in all_records:
        if record.rtype == 'TXT':
            txt_records.append(record)
        elif record.rtype == 'A':
            a_records.append(record)
        elif record.rtype == 'NS':
            num_ns_records += 1
        elif record.rtype == 'SOA':
            num_soa_records += 1
    assert len(txt_records) == 1
    assert len(a_records) == 1
    assert 1 == num_soa_records
    assert num_ns_records > 0

    assert zone_name == txt_records[0].domain
    assert txt_records[0].record_hash
    assert '"Patched" "text" "data"' == txt_records[0].rdata
    assert 45 == txt_records[0].ttl
    assert txt_records[0].rrset_version

    assert 'testsubdomain.{}'.format(zone_name) == a_records[0].domain
    assert a_records[0].record_hash
    assert '127.0.0.1' == a_records[0].rdata
    assert 3600 == a_records[0].ttl
    assert a_records[0].rrset_version

    # Remove TXT with a condition
    remove_patch_zone_records = [
        oci.dns.models.RecordOperation(
            domain=zone_name,
            rrset_version=txt_records[0].rrset_version,
            operation='REQUIRE',
            rtype='TXT'
        ),
        oci.dns.models.RecordOperation(
            domain=zone_name,
            record_hash=txt_records[0].record_hash,
            rdata=txt_records[0].rdata,
            rtype='TXT',
            operation='REMOVE'
        ),
    ]
    patch_response = dns_client.patch_zone_records(
        zone_name_or_id,
        oci.dns.models.PatchZoneRecordsDetails(items=remove_patch_zone_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert len(patch_response.data.items) > 0
    assert int(patch_response.headers.get('opc-total-items')) == len(patch_response.data.items)

    # Remove without condition
    remove_patch_zone_records = [
        oci.dns.models.RecordOperation(
            domain='testsubdomain.{}'.format(zone_name),
            record_hash=a_records[0].record_hash,
            rdata=a_records[0].rdata,
            rtype='A',
            operation='REMOVE'
        ),
    ]
    patch_response = dns_client.patch_zone_records(
        zone_name_or_id,
        oci.dns.models.PatchZoneRecordsDetails(items=remove_patch_zone_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert len(patch_response.data.items) > 0
    assert int(patch_response.headers.get('opc-total-items')) == len(patch_response.data.items)

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_zone_records_kwargs['zone_version'] = zone_version
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_zone_records,
        'response',
        zone_name_or_id,
        **get_zone_records_kwargs
    )
    for response in all_records_generator:
        # We should have deleted the A and TXT records, but not touched the NS or SOA records
        for item in response.data.items:
            assert item.rtype != 'A' and item.rtype != 'TXT'
            assert item.rtype == 'NS' or item.rtype == 'SOA'


def update_domain_records(dns_client, zone_name_or_id, zone_name, subdomain_base):
    domain = '{}.{}'.format(subdomain_base, zone_name)

    update_domain_record_items = [
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=31,
            rtype='TXT',
            rdata='domain data'
        )
    ]

    update_response = dns_client.update_domain_records(
        zone_name_or_id,
        domain,
        oci.dns.models.UpdateDomainRecordsDetails(items=update_domain_record_items)
    )
    assert update_response.request_id
    assert update_response.headers.get('ETag')
    assert int(update_response.headers.get('opc-total-items')) == 1
    assert len(update_response.data.items) == 1

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_domain_records_kwargs = {
        'zone_version': zone_version,
        'rtype': 'TXT'
    }

    txt_domain_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    txt_records = []
    for response in txt_domain_records_generator:
        txt_records.extend(response.data.items)
    assert len(txt_records) == 1
    assert 'TXT' == txt_records[0].rtype
    assert domain == txt_records[0].domain
    assert txt_records[0].record_hash
    assert '"domain" "data"' == txt_records[0].rdata
    assert 31 == txt_records[0].ttl
    assert txt_records[0].rrset_version

    # This should blow away the TXT record
    update_domain_record_items = [
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=1800,
            rtype='A',
            rdata='127.0.0.1'
        )
    ]
    update_response = dns_client.update_domain_records(
        zone_name_or_id,
        domain,
        oci.dns.models.UpdateDomainRecordsDetails(items=update_domain_record_items)
    )
    assert update_response.request_id
    assert update_response.headers.get('ETag')
    assert int(update_response.headers.get('opc-total-items')) == 1
    assert len(update_response.data.items) == 1

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_domain_records_kwargs = {'zone_version': zone_version}
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    all_records = []
    for response in all_records_generator:
        all_records.extend(response.data.items)
    assert len(all_records) == 1

    assert 'A' == all_records[0].rtype
    assert domain == all_records[0].domain
    assert all_records[0].record_hash
    assert '127.0.0.1' == all_records[0].rdata
    assert 1800 == all_records[0].ttl
    assert all_records[0].rrset_version

    delete_domain_records(dns_client, zone_name_or_id, domain)

    zone_version = get_zone(dns_client, zone_name_or_id).version
    assert len(dns_client.get_domain_records(zone_name_or_id, domain, zone_version=zone_version).data.items) == 0


def patch_domain_records(dns_client, zone_name_or_id, zone_name, subdomain_base):
    # Our subdomain (should) start out without any records, so add some in and do patch operations and
    # check those existing records are not impacted
    domain = '{}.{}'.format(subdomain_base, zone_name)
    update_domain_record_items = [
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=60,
            rtype='TXT',
            rdata='rec'
        ),
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=60,
            rtype='TXT',
            rdata='rec2'
        )
    ]
    dns_client.update_domain_records(
        zone_name_or_id,
        domain,
        oci.dns.models.UpdateDomainRecordsDetails(items=update_domain_record_items)
    )

    # Sanity test that we have 2 records with a TTL of 60
    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_domain_records_kwargs = {'zone_version': zone_version, 'rtype': 'TXT'}
    txt_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    txt_records = []
    for response in txt_records_generator:
        txt_records.extend(response.data.items)
    assert len(txt_records) == 2
    for t in txt_records:
        assert 60 == t.ttl

    patch_ttl_add_txt_records = [
        oci.dns.models.RecordOperation(
            domain=domain,
            ttl=45,
            rtype='TXT',
            rdata='"rec2"',
            operation='ADD'
        )
    ]
    patch_response = dns_client.patch_domain_records(
        zone_name_or_id,
        domain,
        oci.dns.models.PatchDomainRecordsDetails(items=patch_ttl_add_txt_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert int(patch_response.headers.get('opc-total-items')) == 2
    assert len(patch_response.data.items) == 2

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_domain_records_kwargs['zone_version'] = zone_version
    txt_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    num_records = 0
    rec_one_found = False
    rec_one = None  # Grab this so we can do a patch with preconditions later
    rec_two_found = False
    for response in txt_records_generator:
        for item in response.data.items:
            num_records += 1
            assert 45 == item.ttl
            assert 'TXT' == item.rtype
            assert item.record_hash
            assert item.rrset_version

            if item.rdata == '"rec"':
                rec_one_found = True
                rec_one = item
            elif item.rdata == '"rec2"':
                rec_two_found = True
    assert rec_one_found
    assert rec_two_found
    assert num_records == 2

    failing_patch_domain_records = [
        oci.dns.models.RecordOperation(
            domain=domain,
            rrset_version='99',
            rtype='TXT',
            operation='REQUIRE'
        ),
        oci.dns.models.RecordOperation(
            domain=domain,
            ttl=45,
            rtype='TXT',
            rdata='Add patch record',
            operation='ADD'
        )
    ]
    try:
        dns_client.patch_domain_records(
            zone_name_or_id,
            domain,
            oci.dns.models.PatchDomainRecordsDetails(items=failing_patch_domain_records)
        )
    except oci.exceptions.ServiceError as e:
        assert e.status == 409

    successful_patch_add_a_records = [
        oci.dns.models.RecordOperation(
            domain=domain,
            rrset_version=rec_one.rrset_version,
            rtype='TXT',
            operation='REQUIRE'
        ),
        oci.dns.models.RecordOperation(
            domain=domain,
            rtype='A',
            ttl=1900,
            rdata='127.0.0.1',
            operation='ADD'
        ),
        oci.dns.models.RecordOperation(
            domain=domain,
            rtype='A',
            ttl=1900,
            rdata='127.0.0.2',
            operation='ADD'
        )
    ]

    patch_response = dns_client.patch_domain_records(
        zone_name_or_id,
        domain,
        oci.dns.models.PatchDomainRecordsDetails(items=successful_patch_add_a_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert int(patch_response.headers.get('opc-total-items')) == 4
    assert len(patch_response.data.items) == 4
    num_txt_records = 0
    num_a_records = 0
    for item in patch_response.data.items:
        if item.rtype == 'TXT':
            num_txt_records += 1
        elif item.rtype == 'A':
            num_a_records += 1
    assert num_txt_records == 2
    assert num_a_records == 2

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_domain_records_kwargs = {'zone_version': zone_version, 'rtype': 'A'}
    a_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    num_a_records = 0
    found_a_record_one = False
    found_a_record_two = False
    for response in a_records_generator:
        for item in response.data.items:
            num_a_records += 1
            assert item.ttl == 1900
            assert item.rtype == 'A'
            assert item.record_hash
            assert item.rrset_version

            if item.rdata == '127.0.0.1':
                found_a_record_one = True
            elif item.rdata == '127.0.0.2':
                found_a_record_two = True
    assert num_a_records == 2
    assert found_a_record_one
    assert found_a_record_two

    patch_ttl_all_a_records = [
        oci.dns.models.RecordOperation(
            domain=domain,
            ttl=3600,
            rtype='A',
            rdata='127.0.0.1',  # We need to provide rdata otherwise the call results in a 400
            operation='ADD'
        )
    ]
    patch_response = dns_client.patch_domain_records(
        zone_name_or_id,
        domain,
        oci.dns.models.PatchDomainRecordsDetails(items=patch_ttl_all_a_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert int(patch_response.headers.get('opc-total-items')) == 4
    assert len(patch_response.data.items) == 4

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_domain_records_kwargs = {'zone_version': zone_version, 'rtype': 'A'}
    a_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    a_records = []
    for response in a_records_generator:
        for item in response.data.items:
            a_records.append(item)
            assert item.ttl == 3600
    assert len(a_records) == 2

    get_domain_records_kwargs['rtype'] = 'TXT'
    txt_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    txt_records = []
    for response in txt_records_generator:
        txt_records.extend(response.data.items)
    assert len(txt_records) == 2

    remove_one_txt_one_a_record = [
        oci.dns.models.RecordOperation(
            domain=domain,
            record_hash=txt_records[0].record_hash,
            rdata=txt_records[0].rdata,
            rtype='TXT',
            operation='REMOVE'
        ),
        oci.dns.models.RecordOperation(
            domain=domain,
            record_hash=a_records[1].record_hash,
            rdata=a_records[1].rdata,
            rtype='A',
            operation='REMOVE'
        )
    ]

    patch_response = dns_client.patch_domain_records(
        zone_name_or_id,
        domain,
        oci.dns.models.PatchDomainRecordsDetails(items=remove_one_txt_one_a_record)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')

    zone_version = get_zone(dns_client, zone_name_or_id).version
    get_domain_records_kwargs = {'zone_version': zone_version}
    all_records_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_domain_records,
        'response',
        zone_name_or_id,
        domain,
        **get_domain_records_kwargs
    )
    all_records = []
    for response in all_records_generator:
        all_records.extend(response.data.items)
    assert len(all_records) == 2

    found_txt_record = False
    found_a_record = False
    for record in all_records:
        if record.rtype == 'TXT':
            found_txt_record = True
            assert txt_records[1].record_hash == record.record_hash
            assert txt_records[1].rdata == record.rdata
        elif record.rtype == 'A':
            found_a_record = True
            assert a_records[0].record_hash == record.record_hash
            assert a_records[0].rdata == record.rdata
    assert found_txt_record
    assert found_a_record

    delete_domain_records(dns_client, zone_name_or_id, domain)
    zone_version = get_zone(dns_client, zone_name_or_id).version
    assert len(dns_client.get_domain_records(zone_name_or_id, domain, zone_version=zone_version).data.items) == 0


def update_rr_set_records(dns_client, zone_name_or_id, zone_name, subdomain_base):
    domain = '{}.{}'.format(subdomain_base, zone_name)

    update_rr_set_items = [
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=3500,
            rtype='A',
            rdata='127.0.0.1'
        ),
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=3500,
            rtype='A',
            rdata='127.0.0.2'
        )
    ]

    update_response = dns_client.update_rr_set(
        zone_name_or_id,
        domain,
        'A',
        oci.dns.models.UpdateRRSetDetails(items=update_rr_set_items)
    )
    assert update_response.request_id
    assert update_response.headers.get('ETag')
    assert int(update_response.headers.get('opc-total-items')) == 2
    assert len(update_response.data.items) == 2

    zone_version = get_zone(dns_client, zone_name_or_id).version
    rr_set_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_rr_set,
        'response',
        zone_name_or_id,
        domain,
        'A',
        zone_version=zone_version
    )
    a_records = []
    for response in rr_set_generator:
        a_records.extend(response.data.items)
    assert len(a_records) == 2

    found_record_one = False
    found_record_two = False
    for record in a_records:
        assert record.rtype == 'A'
        assert record.ttl == 3500
        assert record.record_hash
        assert record.rrset_version

        if record.rdata == '127.0.0.1':
            found_record_one = True
        elif record.rdata == '127.0.0.2':
            found_record_two = True
    assert found_record_one
    assert found_record_two

    delete_rr_set_records(dns_client, zone_name_or_id, domain, 'A')
    assert len(dns_client.get_rr_set(zone_name_or_id, domain, 'A').data.items) == 0


def patch_rr_set_records(dns_client, zone_name_or_id, zone_name, subdomain_base):
    domain = '{}.{}'.format(subdomain_base, zone_name)

    # Our RR Set (should) start out without any records, so add some in and do patch operations and
    # check those existing records are not impacted

    update_rr_set_items = [
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=3500,
            rtype='A',
            rdata='127.0.0.1'
        ),
        oci.dns.models.RecordDetails(
            domain=domain,
            ttl=3500,
            rtype='A',
            rdata='127.0.0.2'
        )
    ]

    dns_client.update_rr_set(
        zone_name_or_id,
        domain,
        'A',
        oci.dns.models.UpdateRRSetDetails(items=update_rr_set_items)
    )

    patch_ttl_all_a_records = [
        oci.dns.models.RecordOperation(
            domain=domain,
            ttl=2000,
            rtype='A',
            rdata='127.0.0.1',
            operation='ADD'
        )
    ]

    patch_response = dns_client.patch_rr_set(
        zone_name_or_id,
        domain,
        'A',
        oci.dns.models.PatchRRSetDetails(items=patch_ttl_all_a_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert int(patch_response.headers.get('opc-total-items')) == 2
    assert len(patch_response.data.items) == 2

    zone_version = get_zone(dns_client, zone_name_or_id).version
    rr_set_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_rr_set,
        'response',
        zone_name_or_id,
        domain,
        'A',
        zone_version=zone_version
    )
    a_records = []
    for response in rr_set_generator:
        a_records.extend(response.data.items)
    assert len(a_records) == 2
    for record in a_records:
        assert record.ttl == 2000

    failing_patch_rr_set_records = [
        oci.dns.models.RecordOperation(  # This fails because the RRSet does not exist
            domain=domain,
            rrset_version='77',
            rtype='A',
            operation='REQUIRE'
        ),
        oci.dns.models.RecordOperation(
            domain=domain,
            rtype='A',
            rdata='127.0.0.3'
        )
    ]

    try:
        dns_client.patch_rr_set(
            zone_name_or_id,
            domain,
            'A',
            oci.dns.models.PatchRRSetDetails(items=failing_patch_rr_set_records)
        )
    except oci.exceptions.ServiceError as e:
        assert e.status == 409

    successful_patch_rr_set_records = [
        oci.dns.models.RecordOperation(
            domain=domain,
            rtype='A',
            rdata='127.0.0.3',
            ttl=2000
        )
    ]
    patch_response = dns_client.patch_rr_set(
        zone_name_or_id,
        domain,
        'A',
        oci.dns.models.PatchRRSetDetails(items=successful_patch_rr_set_records)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')
    assert int(patch_response.headers.get('opc-total-items')) == 3
    assert len(patch_response.data.items) == 3

    zone_version = get_zone(dns_client, zone_name_or_id).version
    rr_set_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_rr_set,
        'response',
        zone_name_or_id,
        domain,
        'A',
        zone_version=zone_version
    )
    a_records = []
    for response in rr_set_generator:
        a_records.extend(response.data.items)
    assert len(a_records) == 3
    found_record_one = False
    found_record_two = False
    found_record_three = False
    for record in a_records:
        assert record.rtype == 'A'
        assert record.ttl == 2000
        assert record.record_hash
        assert record.rrset_version

        if record.rdata == '127.0.0.1':
            found_record_one = True
        elif record.rdata == '127.0.0.2':
            found_record_two = True
        elif record.rdata == '127.0.0.3':
            found_record_three = True
    assert found_record_one
    assert found_record_two
    assert found_record_three

    remove_one_a_record = [
        oci.dns.models.RecordOperation(
            domain=domain,
            rtype='A',
            rrset_version=a_records[0].rrset_version,
            operation='REQUIRE'
        ),
        oci.dns.models.RecordOperation(
            domain=domain,
            rtype='A',
            record_hash=a_records[1].record_hash,
            rdata=a_records[1].rdata,
            operation='REMOVE'
        )
    ]

    patch_response = dns_client.patch_rr_set(
        zone_name_or_id,
        domain,
        'A',
        oci.dns.models.PatchRRSetDetails(items=remove_one_a_record)
    )
    assert patch_response.request_id
    assert patch_response.headers.get('ETag')

    zone_version = get_zone(dns_client, zone_name_or_id).version
    rr_set_generator = oci.pagination.list_call_get_all_results_generator(
        dns_client.get_rr_set,
        'response',
        zone_name_or_id,
        domain,
        'A',
        zone_version=zone_version
    )
    a_records_after_removal = []
    for response in rr_set_generator:
        a_records_after_removal.extend(response.data.items)
    assert len(a_records_after_removal) == 2
    found_record_one = False
    found_record_three = False
    for record in a_records:
        assert record.rtype == 'A'
        assert record.ttl == 2000
        assert record.record_hash
        assert record.rrset_version

        if record.rdata == a_records[0].rdata:
            found_record_one = True
        elif record.rdata == a_records[2].rdata:
            found_record_three = True
    assert found_record_one
    assert found_record_three

    delete_rr_set_records(dns_client, zone_name_or_id, domain, 'A')
    zone_version = get_zone(dns_client, zone_name_or_id).version
    assert len(dns_client.get_rr_set(zone_name_or_id, domain, 'A', zone_version=zone_version).data.items) == 0


def delete_domain_records(dns_client, zone_name_or_id, domain):
    delete_response = dns_client.delete_domain_records(
        zone_name_or_id,
        domain
    )
    assert delete_response.request_id


def delete_rr_set_records(dns_client, zone_name_or_id, domain, rtype):
    delete_response = dns_client.delete_rr_set(
        zone_name_or_id,
        domain,
        rtype
    )
    assert delete_response.request_id


def get_zone(dns_client, zone_name_or_id):
    return dns_client.get_zone(zone_name_or_id).data


def delete_zone(dns_client, zone_name):
    response = dns_client.delete_zone(zone_name)
    assert response.request_id


def get_zones(dns_client, **kwargs):
    return oci.pagination.list_call_get_all_results(dns_client.list_zones, util.COMPARTMENT_ID, **kwargs)
