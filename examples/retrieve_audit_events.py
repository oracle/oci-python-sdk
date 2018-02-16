#!/usr/bin/env python
#  coding: utf-8
#  Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

#  This script retrieves all audit logs across an OCI Tenancy.
#  for a timespan defined by start_time and end_time.
#  This sample script retrieves Audit events for last 5 days.
#  This script will work at a tenancy level only.


import oci
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta


def get_regions(identity):
    '''
    To retrieve the list of all available regions.
    '''
    list_of_regions = []
    list_regions_response = identity.list_regions()
    for r in list_regions_response.data:
        list_of_regions.append(r.name)
    return list_of_regions


def get_compartments(identity, tenancy_id):
    '''
    Retrieve the list of compartments under the tenancy.
    '''
    compartment_ocids = []
    #  Store tenancy id as the first compartment
    compartment_ocids.append(tenancy_id)
    list_compartments_response = oci.pagination.list_call_get_all_results(
        identity.list_compartments,
        compartment_id=tenancy_id).data
    for c in list_compartments_response:
        compartment_ocids.append(c.id)
    return compartment_ocids


def get_audit_events(audit, compartment_ocids, start_time, end_time):
    '''
    Get events iteratively for each compartment defined in 'compartments' array
    for the region defined in "config['region']".
    '''
    list_of_audit_events = []
    for c in compartment_ocids:
        #  To separate results by compartments use print here.
        list_events_response = oci.pagination.list_call_get_all_results(
            audit.list_events,
            compartment_id=c,
            start_time=start_time,
            end_time=end_time).data

        #  Results for a compartment 'c' for a region defined
        #  in 'audit' object.
        #  Events can be filtered here based on some constraints.
        #  For example, to filter write events make use of
        #  the following condition
        #  list_events_response.data.request_action != 'GET'
        list_of_audit_events.append(list_events_response)
        return list_of_audit_events


'''Here's the code that retrives audits across the tenancy'''
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
regions = get_regions(identity)

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
        print audit_events
