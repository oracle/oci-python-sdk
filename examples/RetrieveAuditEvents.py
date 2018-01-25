#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.
'''
This script retrieves all audit logs across an OCI Tenancy
for a defined timespan.

This script relies on OCI config as per the format defined at
https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm

This script will work at a tenancy level only.

The config file should have the following contents
User OCID
RSA private key in PEM format
Fingerprint
Tenancy OCID
'''

import oci

__author__ = "saurabh.bangad@oracle.com"

configfile = "~/.oci/config"

config = oci.config.from_file(configfile)  # Path to relevant config file
tenancy_id = config["tenancy"]
# This array will be used to store the list of compartments in the tenancy
compartments = []
compartments.append(tenancy_id)  # Tenancy is the first compartment
regions = []  # This array will be used to store the list of available regions
auditevents = []


#  Initiate the client with the locally available config
#  These are global variables and used across all the functions
audit = oci.audit.audit_client.AuditClient(config)
identity = oci.identity.IdentityClient(config)


# Timespan defined by variables start_time and end_time
start_time = '2018-01-15T00:00:00Z'
end_time = '2018-01-17T00:00:00Z'


def get_regions():
    '''To retrieve the list of all available regions
    '''
    listofregions = []
    rawsoutput = []
    rawoutput = identity.list_regions()
    for i in range(len(rawoutput.data)):
        listofregions.append(str(rawoutput.data[i].name))
    return listofregions


def paginate(operation, *args, **kwargs):
    '''Function to paginate API calls.

    Refer to
    https://github.com/oracle/oci-python-sdk/blob/master/docs/quickstart.rst

    For better exception handling refer to
    https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/index.html#oci.exceptions.ServiceError
    '''
    while True:
        try:
            response = operation(*args, **kwargs)
            for value in response.data:
                yield value
            kwargs["page"] = response.next_page
            if not response.has_next_page:
                break
        except oci.exceptions.ServiceError as e:
            if e.code == 'NotAuthorizedOrNotFound':
                print 'Error: Please check if you have sufficient \
                permissions to execute the operation' + str(operation.im_func)
            elif e.status == '500':
                print 'InternalServerError: Please retry after sometime.'
            else:
                print 'Something went wrong.'
                print 'Here is the info about the exception:'
                print str(e)
            quit()


def get_compartments():
    ''' Retrieve the list of compartments under the tenancy
    '''
    listofcompartments = []
    for list_compartments_json in paginate(
            identity.list_compartments,
            compartment_id=tenancy_id):
            listofcompartments.append(str(list_compartments_json.id))
    return listofcompartments


def get_audit_events(start_time, end_time):
    '''Get events iteratively for each compartment defined in 'compartments' array
    for the region defined in "config['region']".
    '''
    listofauditevents = []
    for i in range(len(compartments)):
        for events in paginate(
                audit.list_events,
                compartment_id=compartments[i],
                start_time=start_time,
                end_time=end_time):
            '''The following condition eliminates all the read API calls.
              Uncomment this if write events need to be filtered.
              '''
            # if events.request_action != 'GET':
            listofauditevents.append(events)
    return listofauditevents


'''Here's the main code that retrives audits across the tenancy'''

#  Retrieve the list of all the OCI regions.
#  This gracefully handles addition of new regions.
regions = get_regions()

#  Retrieve all the compartments.
#  This gracefully handles compartment changes on a tenancy.
compartments = get_compartments()

#  For a region defined by config['region'] get the logs for each compartment
for i in range(len(regions)):
    config['region'] = regions[i]

    #  Reintialize with a different region value
    audit = oci.audit.audit_client.AuditClient(config)
    identity = oci.identity.IdentityClient(config)

    #  To separate results by region use print here
    auditevents = get_audit_events(
        start_time, end_time)
    if auditevents:
        print auditevents
