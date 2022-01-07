# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use work requests using Python SDK.
# This script will:
#
#    * Read in user OCI config
#    * Retrieve a list of all Work Requests for the compartment
#    * Get Work Request details
#    * List errors related to a Work Request
#    * List logs related to a Work Request
#
# This script takes no arguments
#
#
# Usage :
#    python work_request.py
#
#

import oci
from oci.work_requests import WorkRequestClient


def perform_work_request_example():
    global work_request_client

    # read oci config
    config = oci.config.from_file()

    # create WorkRequestClient() with configuration
    work_request_client = WorkRequestClient(config)

    # This is the root compartment.  You can use another compartment in your tenancy.
    compartment_id = config["tenancy"]
    print("Using compartment_id: {}".format(compartment_id))

    work_requests = list_work_requests(compartment_id)
    print("{} Work Requests found.".format(len(work_requests)))

    for work_request in work_requests:

        get_print_details(work_request.id)

        list_print_errors(work_request.id)

        list_print_logs(work_request.id)


def list_work_requests(compartment_id):
    # Only return a maxium of 5 work requests for this example
    resp = work_request_client.list_work_requests(compartment_id, limit=5)
    work_requests = resp.data
    return work_requests


def get_print_details(workrequest_id):
    resp = work_request_client.get_work_request(workrequest_id)
    wrDetails = resp.data

    print()
    print()
    print('=' * 90)
    print('Work Request Details: {}'.format(workrequest_id))
    print('=' * 90)
    print("{}".format(wrDetails))
    print()


def list_print_errors(workrequest_id):
    resp = work_request_client.list_work_request_errors(workrequest_id)
    work_request_errors = resp.data

    print('Work Request Errors')
    print('=' * 30)
    for work_request_error in work_request_errors:
        print("{}".format(work_request_error))
    print()


def list_print_logs(workrequest_id):
    print('Work Request Logs')
    print('=' * 30)

    # example showing how to use the pagination feature. Other work request calls can also be paginated but aren't for simplicity.
    log_limit = 20
    page_size = 5
    resp = oci.pagination.list_call_get_up_to_limit(work_request_client.list_work_request_logs, log_limit, page_size, workrequest_id)
    for work_request_log in resp.data:
        print('{}'.format(work_request_log))


if __name__ == "__main__":
    perform_work_request_example()
