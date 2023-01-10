# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script gives an example on passing in a request model for an API to the pagination call.

import oci

config = oci.config.from_file()
compartment_id = config["tenancy"]
monitoring = oci.monitoring.MonitoringClient(config)

paginated_response = oci.pagination.list_call_get_all_results(
    monitoring.list_metrics,
    compartment_id,
    oci.monitoring.models.ListMetricsDetails()  # Request model passed in as specified from monitoring.ListMetricsDetail API
).data

print("paginated response: ", paginated_response)
