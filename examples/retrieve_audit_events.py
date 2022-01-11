# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

#  This script retrieves all audit logs across an Oracle Cloud Infrastructure Tenancy.
#  for a timespan defined by start_time and end_time.
#  This sample script retrieves Audit events for last 5 days.
#  This script will work at a tenancy level only.

import datetime
import oci


def get_subscription_regions(identity, tenancy_id):
    '''
    To retrieve the list of all available regions.
    '''
    list_of_regions = []
    list_regions_response = identity.list_region_subscriptions(tenancy_id)
    for r in list_regions_response.data:
        list_of_regions.append(r.region_name)
    return list_of_regions


def get_compartments(identity, tenancy_id):
    '''
    Retrieve the list of compartments under the tenancy.
    '''
    list_compartments_response = oci.pagination.list_call_get_all_results(
        identity.list_compartments,
        compartment_id=tenancy_id).data

    compartment_ocids = [c.id for c in filter(lambda c: c.lifecycle_state == 'ACTIVE', list_compartments_response)]

    return compartment_ocids


def get_audit_events(audit, compartment_ocids, start_time, end_time):
    '''
    Get events iteratively for each compartment defined in 'compartments_ocids'
    for the region defined in 'audit'.
    This method eagerly loads all audit records in the time range and it does
    have performance implications of lot of audit records.
    Ideally, the generator method in oci.pagination should be used to lazily
    load results.
    '''
    list_of_audit_events = []
    for c in compartment_ocids:
        list_events_response = oci.pagination.list_call_get_all_results(
            audit.list_events,
            compartment_id=c,
            start_time=start_time,
            end_time=end_time).data

        #  Results for a compartment 'c' for a region defined
        #  in 'audit' object.
        list_of_audit_events.extend(list_events_response)
        return list_of_audit_events


#  Setting configuration
#  Default path for configuration file is "~/.oci/config"
config = oci.config.from_file()
tenancy_id = config["tenancy"]

#  Initiate the client with the locally available config.
identity = oci.identity.IdentityClient(config)

#  Timespan defined by variables start_time and end_time(today).
#  ListEvents expects timestamps into RFC3339 format.
#  For the purposes of sample script, logs of last 5 days.
end_time = datetime.datetime.utcnow()
start_time = end_time + datetime.timedelta(days=-5)

# This array will be used to store the list of available regions.
regions = get_subscription_regions(identity, tenancy_id)

# This array will be used to store the list of compartments in the tenancy.
compartments = get_compartments(identity, tenancy_id)

audit = oci.audit.audit_client.AuditClient(config)

#  For each region get the logs for each compartment.
for r in regions:
    #  Intialize with a region value.
    audit.base_client.set_region(r)
    #  To separate results by region use print here.
    audit_events = get_audit_events(
        audit,
        compartments,
        start_time,
        end_time)

    #  Results for a region 'r' for each compartment.
    if audit_events:
        print(audit_events)
