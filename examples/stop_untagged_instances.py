# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example demonstrates how to find, stop and report on instances that have
# been improperly tagged.
#
# I recommend that you run this every 30 minutes and set the audit hours to 1.
# Example usage 'stop_untagged_instances.py --hours_to_audit 2 --tag_string CostCenter'
# This searches for any instance without the CostCenter tag applied, stops them, finds who started it and logs
# the results.

import oci
import datetime
import argparse


# After determining all the events associated with th stopped instances, merge those event records (OCID and Email)
# with the existing list of instances_to_stop to add the email to the existing list, then write it to disk.
def join_lists(instance_list, events_list, filename):
    for item in instance_list:
        for item2 in events_list:
            # when you find a match between the event_list & instances to stop, add the email to the creator column
            if item['instance_ocid'] == item2['instance_ocid']:
                item['creator'] = item2['principal_name']

    # Write out this joined list to disk
    try:
        with open(filename, 'w') as f:
            for item in instance_list:
                f.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\n'
                        .format(item['stop_datetime'], item['region'], item['compartment_name'], item['instance_name'],
                                item['instance_shape'], item['time_created'], item['instance_ocid'],
                                item['compartment_ocid'], item['creator']))
    except Exception as e:
        print('An unexpected Error Occured writing the file: {0}' .format(e))


# This function stops the instance sent in as a parameter
def stop_resource(instance_id, region):
    base_compute = oci.core.compute_client.ComputeClient(config)
    base_compute.base_client.set_region(region)

    # Stop a running instance, but it is possible for it to fail so putting it in a try catch for common errors.
    try:
        if base_compute.get_instance(instance_id).data.lifecycle_state in 'RUNNING':
            try:
                print('\t\tStopping instance {0}.  Stop response code: {1}'
                      .format(instance_id, str(base_compute.instance_action(instance_id, 'STOP').status)))
            except oci.exceptions.ServiceError as e:
                print('\t\tStopping instance failed. {0}' .format(e))
        else:
            print('\t\tThe instance {} was in the incorrect state to stop' .format(instance_id))
    except oci.exceptions.ServiceError as e:
        print('\t\tStopping instance failed. {0}'.format(e))


# determines the list of subscribed regions for the tenancy
def list_of_regions(tenancy_id):
    identity = oci.identity.IdentityClient(config)
    list_of_regions = []
    list_regions_response = identity.list_region_subscriptions(tenancy_id)
    for r in list_regions_response.data:
        list_of_regions.append(r.region_name)
    return list_of_regions


# This function finds LaunchInstance audit events based on the instance OCID and compartment passed into it
# from the find_resources_wo_tags function.  The LaunchInstance events give it the principal (usually email) of the
# 'person' who started the resource and joins it to the exisitng instances_to_stop so it now contains the email of who
# started it.
def find_audit_events(instances_to_stop, instance_stop_list, compartment_id_stop_list, tenancy_id):
    end_time = datetime.datetime.utcnow()
    start_time = end_time + datetime.timedelta(hours=-int(audit_hours))
    list_of_audit_events = []
    events_list = [{'principal_name': '', 'instance_ocid': ''}]
    audit = oci.audit.audit_client.AuditClient(config)
    print('\nGetting list of audit events for the last {0} hour(s).' .format(audit_hours))

    # Finding all Resources in a region
    region_list = list_of_regions(tenancy_id)
    for region in region_list:
        audit.base_client.set_region(region)

        for c in compartment_id_stop_list:
            # clear out the audit events from a compartment
            del list_of_audit_events[:]
            list_events_response = oci.pagination.list_call_get_all_results(audit.list_events, compartment_id=c,
                                                                            start_time=start_time,
                                                                            end_time=end_time).data
            list_of_audit_events.extend(list_events_response)
            print('\t\tNumber of audit events in {0}\\{1}: {2}' .format(region, identity_client.get_compartment(c).data.name, len(list_of_audit_events)))

            for ae in list_of_audit_events:
                if ae.event_name == 'LaunchInstance':
                    if ae.response_payload['id'] in instance_stop_list:
                        if len(ae.user_name) == 0:
                            principal_name = ae.principal_id.rsplit('/', 1)[-1]
                        else:
                            principal_name = ae.user_name

                        events_line = {'principal_name': principal_name,
                                       'instance_ocid': ae.response_payload['id']}

                        events_list.append(events_line)
                        print('\t\t\tFound a launch instance: {0}'.format(ae.response_payload['id']))
    join_lists(instances_to_stop, events_list, 'stop_untagged_instances_result.csv')


# This function looks for all compute instances using the RQS (search) service, then it filters that list by looking
# For any resources that are in the correct state and that are either missing tags entirely or not tag correctly.
# It records those which are going to be stopped and calls stop_resource with a list of all compute instances to be
# stopped.
def find_resources_wo_tags(instances_to_stop_list, search_string, tenancy_id):
    instances_stop_list = []
    compartment_id_stop_list = []
    search_client = oci.resource_search.ResourceSearchClient(config)
    compute_client = oci.core.ComputeClient(config)

    # Finding all Resources in a region
    region_list = list_of_regions(tenancy_id)
    for region in region_list:
        print('Searching RQS to find mis-tagged resources in Region:{0}' .format(region))
        try:
            search_client.base_client.set_region(region)
            structured_search = oci.resource_search.models.StructuredSearchDetails(
                query="query instance resources",
                type='Structured',
                matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_NONE)
            results = search_client.search_resources(structured_search)
        except oci.exceptions.ServiceError as e:
            print('\t\tRQS Search failed with Service Error: {0}' .format(e))
        except oci.exceptions.RequestException as e:
            print('\t\tRQS Search failed w/ a Request exception. {0}' .format(e))

        # Filtering from everything to just those not tagged.
        # This method is needed to also find resources with no tags at all
        filter_key = search_string
        for result in results.data.items:
            if (filter_key not in str(result.defined_tags)) or len(result.defined_tags) == 0:
                if result.lifecycle_state in ('Provisioning', 'Starting', 'Running'):
                    compute_client.base_client.set_region(region)
                    try:
                        stopped_instances_line = {'stop_datetime': datetime.datetime.utcnow().replace(microsecond=0).isoformat(),
                                                  'region': region,
                                                  'compartment_name': identity_client.get_compartment(result.compartment_id).data.name,
                                                  'instance_name': result.display_name,
                                                  'instance_shape': compute_client.get_instance(result.identifier).data.shape,
                                                  'time_created': result.time_created.replace(microsecond=0).isoformat(),
                                                  'instance_ocid': result.identifier,
                                                  'compartment_ocid': result.compartment_id,
                                                  'creator': 'Not Found'}
                        instances_to_stop_list.append(stopped_instances_line)
                        instances_stop_list.append(result.identifier)
                        if result.compartment_id not in compartment_id_stop_list:
                            compartment_id_stop_list.append(result.compartment_id)
                        print('\t\t*Found an resource ({0}) without a tag.  Stopping it.*' .format(result.display_name))
                        stop_resource(result.identifier, region)

                    except oci.exceptions.ServiceError as e:
                        print('\t\tThe instance ({0}) could not be retrieved. It may be a ghost Search entry. {1}'
                              .format(result.display_name, e))

    # Only find audit events for  those compartments with a stopped instance
    if len(instances_to_stop_list) != 0:
        find_audit_events(instances_to_stop_list, instances_stop_list, compartment_id_stop_list, tenancy_id)


# A helper function that processes the two arguments for this program.  Tag_string is the string that is searched for.
# Hours to audit is the number of hours before now to search the audit log for.
def prep_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tag_string', default='', help='The string in all tags that will be searched for.')
    parser.add_argument('--hours_to_audit', default=1, help='The number of hours to search the audit logs for.')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # Starts a timer for the execution time.
    print('Stop the Untagged v0.61')
    start_time = datetime.datetime.now()
    print('Start Time: {0}'.format(start_time.replace(microsecond=0).isoformat()))

    config = oci.config.from_file()
    identity_client = oci.identity.IdentityClient(config)

    tenancy_id = config['tenancy']
    # Set the search_string and audit_hours from arguments
    args = prep_arguments()
    search_string = args.tag_string
    audit_hours = args.hours_to_audit

    # Create a list of dictionaries that represents the final csv file that records all stopped records.
    instances_to_stop = []
    instance_line = {'stop_datetime': 'stop_datetime', 'region': 'region', 'compartment_name': 'compartment_name',
                     'instance_name': 'instance_name', 'instance_shape': 'instance_shape',
                     'time_created': 'time_created', 'instance_ocid': 'instance_ocid ',
                     'compartment_ocid': 'compartment_ocid', 'creator': 'creator'}
    instances_to_stop.append(instance_line)

    # This is the main function that finds any instance that's not tagged with the search_string
    find_resources_wo_tags(instances_to_stop, search_string, tenancy_id)

    # Completes the program and shows the duration of the run
    end_time = datetime.datetime.now()
    print('\nEnd Time: {0}' .format(end_time.replace(microsecond=0).isoformat()))
    print('Duration: {0}' .format((end_time - start_time)))
