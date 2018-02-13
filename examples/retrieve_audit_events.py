#!/usr/bin/env python
#  coding: utf-8
#  Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

#  This script retrieves all audit logs across an OCI Tenancy.
#  for a timespan defined by start_time and end_time.
#  This script will work at a tenancy level only.


import oci
from datetime import date
from dateutil.relativedelta import relativedelta


def get_regions(identity):
    '''To retrieve the list of all available regions.
    '''
    list_of_regions = []
    list_regions_response = identity.list_regions()
    for r in list_regions_response.data:
        list_of_regions.append(r.name)
    return list_of_regions


def get_compartments(identity):
    ''' Retrieve the list of compartments under the tenancy.
    '''
    compartment_ocids = []
    list_compartments_response = oci.pagination.list_call_get_all_results(
        identity.list_compartments,
        compartment_id=config['tenancy']).data
    for c in list_compartments_response:
        compartment_ocids.append(c.id)
    return compartment_ocids


def get_audit_events(audit, compartment_ocids, start_time, end_time, r):
    '''Get events iteratively for each compartment defined in 'compartments' array
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
#  These are global variables and used across all the functions.
audit = oci.audit.audit_client.AuditClient(config)
identity = oci.identity.IdentityClient(config)


#  Timespan defined by variables start_time and end_time(today).
today = date.today() + relativedelta(months=0)
today_minus_one_month = date.today() + relativedelta(months=-1)

#  ListEvents expects timestamps into RFC3339 format.
#  Converting dates into RFC3339 e.g. 2018-01-15T00:00:00Z
end_time = str(today.year) + '-' + str(today.month).zfill(2) \
    + '-' + str(today.day) + 'T00:00:00Z'
start_time = str(today_minus_one_month.year) + '-' \
    + str(today_minus_one_month.month).zfill(2) + '-' \
    + str(today_minus_one_month.day) + 'T00:00:00Z'

regions = []  # This array will be used to store the list of available regions.
regions = get_regions(identity)

# This array will be used to store the list of compartments in the tenancy.
compartments = []
compartments.append(tenancy_id)  # Tenancy is the first compartment.
compartments = get_compartments(identity)

audit = oci.audit.audit_client.AuditClient(config)
audit_events = []

#  For each region get the logs for each compartment.
for r in regions:
    #  Intialize with a region value.
    audit.base_client.set_region(r)
    #  To separate results by region use print here.
    audit_events = get_audit_events(
        audit,
        compartments,
        start_time,
        end_time, r)

    #  Results for a region 'r' for each compartment.
    if audit_events:
        print audit_events
