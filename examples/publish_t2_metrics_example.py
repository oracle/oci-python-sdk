# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This script gives an example on passing in a request model for an API to the pagination call.

# !!! THIS EXAMPLE HAS INFORMATION ABOUT R1 AND IS INTENDED FOR INTERNAL CUSTOMERS. MASK DETAILS FOR PUBLIC VERSION !!!

from datetime import datetime, timedelta, timezone

from oci.auth.signers import InstancePrincipalsSecurityTokenSigner, OauthExchangeTokenSigner
from oci.monitoring import MonitoringClient, models

metrics_endpoint = "https://telemetry-ingestion.us-ashburn-1.oraclecloud.com"

target_compartment = ""
root_cert_path = ""

instance_principal_signer = InstancePrincipalsSecurityTokenSigner(
    federation_endpoint='https://auth.us-ashburn-1.oraclecloud.com/v1/x509')

oauth_exchange_signer = OauthExchangeTokenSigner(instance_principal_signer,
                                                 scope=f"monitoring_write_urn-{target_compartment}:instance",
                                                 cert_bundle_verify=root_cert_path,
                                                 target_compartment=target_compartment,
                                                 oauth_token_endpoint="https://auth.region.oraclecloud.com}/v1/oauth2/scoped")

monitoring = MonitoringClient({}, service_endpoint=metrics_endpoint, signer=oauth_exchange_signer)

metric_data = [models.MetricDataDetails(
    namespace="",
    resource_group="",
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
print("Posting metric data....")

post_metric_data_details = models.PostMetricDataDetails(
    metric_data=metric_data,
    batch_atomicity=models.PostMetricDataDetails.BATCH_ATOMICITY_ATOMIC
)
post_metric_result = monitoring.post_metric_data(post_metric_data_details)

print("post metrics response status: ", post_metric_result.status)
print("post metrics response data: ", post_metric_result.data)
