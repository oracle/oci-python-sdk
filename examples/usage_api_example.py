# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to you can use usage api.
# It then shows how to perform updates, reads, and deletes. It will:
#   * Create a usage api client
#   * get possible parameters for querying usage/cost
#   * get cost
#   * get cost with filter
#   * get cost with group by compartmentPath
# see more api detail at https://docs.cloud.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm#cost_analysis_using_the_api

import oci.usage_api.models
from oci.usage_api.models import RequestSummarizedUsagesDetails, Filter, Dimension
from datetime import datetime

# Default config file and profile
config = oci.config.from_file()
usage_api_client = oci.usage_api.UsageapiClient(config)

tenant_id = config['tenancy']

# get possible parameters for getting cost
config_response = usage_api_client.request_summarized_configurations(tenant_id)
print("get possible parameters for getting usage")
print(config_response.__dict__)

# query cost with group by service
usage_request = RequestSummarizedUsagesDetails(tenant_id=tenant_id,
                                               time_usage_started=datetime(2020, 9, 1, 0, 0, 0, 0),
                                               time_usage_ended=datetime(2020, 9, 10, 0, 0, 0, 0),
                                               granularity='DAILY',
                                               query_type='COST',
                                               group_by=['service'])

usage_response = usage_api_client.request_summarized_usages(usage_request)
print("query cost with group by service")
print(usage_response.__dict__)

# find possible service name from request_summarized_configurations
service_dem1 = Dimension(key='service', value='COMPUTE')
service_dem2 = Dimension(key='service', value='BLOCK_STORAGE')

simple_filter = Filter(operator='OR', dimensions=[service_dem1, service_dem2])

service_filter1 = Filter(operator='AND', dimensions=[service_dem1])
service_filter2 = Filter(operator='AND', dimensions=[service_dem2])
nested_filter = Filter(operator='OR', dimensions=[], filters=[service_filter1, service_filter2])

# get cost with service == COMPUTE or service == BLOCK_STORAGE in simple filter
usage_request.filter = simple_filter
usage_response = usage_api_client.request_summarized_usages(usage_request)
print("get cost with service == COMPUTE or service == BLOCK_STORAGE in simple filter")
print(usage_response.__dict__)

# get cost with service == COMPUTE or service == BLOCK_STORAGE in nested filter
usage_request.filter = nested_filter
usage_response = usage_api_client.request_summarized_usages(usage_request)
print("get cost with service == COMPUTE or service == BLOCK_STORAGE in nested filter")
print(usage_response.__dict__)

# group by compartmentPath
usage_request = RequestSummarizedUsagesDetails(tenant_id=tenant_id,
                                               time_usage_started=datetime(2020, 9, 1, 0, 0, 0, 0),
                                               time_usage_ended=datetime(2020, 9, 10, 0, 0, 0, 0),
                                               granularity='DAILY',
                                               query_type='COST',
                                               compartment_depth=3,
                                               group_by=['compartmentPath'])
usage_response = usage_api_client.request_summarized_usages(usage_request)
print("group by compartmentPath")
print(usage_response.__dict__)
