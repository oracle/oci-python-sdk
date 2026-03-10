# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script gives an example on passing in a request model for an API to the pagination call.

# !!! THIS EXAMPLE HAS INFORMATION ABOUT R1 AND IS INTENDED FOR INTERNAL CUSTOMERS. MASK DETAILS FOR PUBLIC VERSION !!!

import time
from datetime import datetime, timedelta, timezone

from oci.auth.signers import InstancePrincipalsSecurityTokenSigner, OauthExchangeTokenSigner
from oci.monitoring import MonitoringClient, models

metrics_endpoint = "https://telemetry-ingestion.us-ashburn-1.oraclecloud.com"

target_compartment = ""
root_cert_path = ""

# Duration to run the loop (in minutes)
DURATION_MINUTES = 60
# Interval between metric publications (in seconds)
PUBLISH_INTERVAL_SECONDS = 10

instance_principal_signer = InstancePrincipalsSecurityTokenSigner(
    federation_endpoint='https://auth.us-ashburn-1.oraclecloud.com/v1/x509')

oauth_exchange_signer = OauthExchangeTokenSigner(instance_principal_signer,
                                                 scope=f"monitoring_write_urn-{target_compartment}:instance",
                                                 cert_bundle_verify=root_cert_path,
                                                 target_compartment=target_compartment,
                                                 oauth_token_endpoint="https://auth.us-ashburn-1.oraclecloud.com/v1/oauth2/scoped")

monitoring = MonitoringClient({}, service_endpoint=metrics_endpoint, signer=oauth_exchange_signer)

start_time = time.time()
end_time = start_time + (DURATION_MINUTES * 60)

print(f"Starting metric publishing loop for {DURATION_MINUTES} minutes...")
print(f"Will publish metrics every {PUBLISH_INTERVAL_SECONDS} seconds")

iteration = 0
while time.time() < end_time:
    iteration += 1
    elapsed_minutes = (time.time() - start_time) / 60

    metric_data = [models.MetricDataDetails(
        namespace="identity",
        resource_group="identity-data-plane-test",
        compartment_id=target_compartment,
        name="SDKTestMetric",
        dimensions={
            "resourceId": "exampleDimensionResource"
        },
        metadata={
            "unit": "count",
        },
        datapoints=[
            {
                "timestamp": (
                    datetime.now(timezone.utc) - timedelta(minutes=5)
                ).strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                "value": 15,
                "count": 1
            }
        ]
    ) for i in range(4)]

    print(f"\n[Iteration {iteration}] [{elapsed_minutes:.1f} mins elapsed] Posting metric data at {datetime.now()}...")

    post_metric_data_details = models.PostMetricDataDetails(
        metric_data=metric_data,
        batch_atomicity=models.PostMetricDataDetails.BATCH_ATOMICITY_ATOMIC
    )

    try:
        post_metric_result = monitoring.post_metric_data(post_metric_data_details)
        print("post metrics response status: ", post_metric_result.status)
        print("post metrics response data: ", post_metric_result.data)
    except Exception as e:
        print(f"Error posting metrics: {e}")

    # Sleep until next interval (unless we're at the end of the duration)
    if time.time() < end_time:
        time.sleep(PUBLISH_INTERVAL_SECONDS)

print(f"\nCompleted metric publishing after {DURATION_MINUTES} minutes ({iteration} iterations)")
