# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script provides a basic example of how to use the Health Checks service.
# Please review the documentation for more information about
# how Health Checks works, including permissions needed.
#
# https://docs.cloud.oracle.com/iaas/Content/HealthChecks/Concepts/healthchecks.htm


import oci
from datetime import datetime


# Helper to format dates
def format_time(timestamp):
    # Will be ticks, not seconds from epoch
    return datetime.utcfromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')


# Default config file and profile
config = oci.config.from_file()
healthchecks_client = oci.healthchecks.HealthChecksClient(config)

# This is the root compartment.  You can use another compartment in your tenancy.
compartment_id = config["tenancy"]

# List of available vantage points
vantage_points = healthchecks_client.list_health_checks_vantage_points().data


# HttpMonitors examples
# Creating a new HttpMonitor:
http_monitor = healthchecks_client.create_http_monitor(
    oci.healthchecks.models.CreateHttpMonitorDetails(
        compartment_id=compartment_id,
        display_name="Monitor Name",
        targets=["example.com"],
        protocol="HTTPS",
        vantage_point_names=[vantage_points[0].name],  # If not specified we will auto assign 3 vantage points
        port=443,
        path="/",
        is_enabled=False,
        interval_in_seconds=30,
        timeout_in_seconds=30
    )
).data

# Updating an existing monitor:
#   Note: You only need to specify any properties you wish to change.
#   It returns the updated monitor.

http_monitor = healthchecks_client.update_http_monitor(
    monitor_id=http_monitor.id,
    update_http_monitor_details=oci.healthchecks.models.UpdateHttpMonitorDetails(
        targets=["example.com", "other.example.com"],
        is_enabled=True
    )
).data

print('Display Name: {}, isEnabled: {}'.format(http_monitor.display_name, http_monitor.is_enabled))

# Retrieving monitor results:
# There's a pagination helper to get all the pages for you.
http_monitor_results = oci.pagination.list_call_get_all_results(healthchecks_client.list_http_probe_results, http_monitor.id)

for monitor_result in http_monitor_results.data:
    print('Result: {}, Start Time: {}, isHealthy: {}'.format(monitor_result.target, format_time(monitor_result.start_time), monitor_result.is_healthy))

# To change the compartment:
healthchecks_client.change_http_monitor_compartment(
    monitor_id=http_monitor.id,
    change_http_monitor_compartment_details=oci.healthchecks.models.ChangeHttpMonitorCompartmentDetails(
        compartment_id="NEW_COMPARTMENT_ID"
    )
)

# The delete will have no return if successful
healthchecks_client.delete_http_monitor(monitor_id=http_monitor.id)

# PingMonitors examples

# Creating a new PingMonitor:
ping_monitor = healthchecks_client.create_ping_monitor(
    oci.healthchecks.models.CreatePingMonitorDetails(
        compartment_id=compartment_id,
        display_name="Monitor Name",
        targets=["example.com"],
        protocol="ICMP",
        vantage_point_names=[vantage_points[0].name],  # If not specified we will auto assign 3 vantage points
        is_enabled=False,
        interval_in_seconds=30,
        timeout_in_seconds=30
    )
).data

# Updating an existing monitor:
# Note: You only need to specify any properties you wish to change.
# It returns the updated monitor.
ping_monitor = healthchecks_client.update_ping_monitor(
    monitor_id=ping_monitor.id,
    update_ping_monitor_details=oci.healthchecks.models.UpdatePingMonitorDetails(
        targets=["example.com", "other.example.com"],
        is_enabled=True
    )
).data

print('Display Name: {}, isEnabled: {}'.format(ping_monitor.display_name, ping_monitor.is_enabled))

# Retrieving monitor results:
# There's a pagination helper to get all the pages for you.
ping_monitor_results = oci.pagination.list_call_get_all_results(healthchecks_client.list_ping_probe_results, ping_monitor.id)

for monitor_result in ping_monitor_results.data:
    print('Result: {}, Start Time: {}, isHealthy: {}'.format(monitor_result.target, format_time(monitor_result.start_time), monitor_result.is_healthy))

# To change the compartment:
healthchecks_client.change_ping_monitor_compartment(
    monitor_id=ping_monitor.id,
    change_ping_monitor_compartment_details=oci.healthchecks.models.ChangePingMonitorCompartmentDetails(
        compartment_id="NEW_COMPARTMENT_ID"
    )
)

# The delete will have no return if successful
healthchecks_client.delete_ping_monitor(monitor_id=ping_monitor.id)
