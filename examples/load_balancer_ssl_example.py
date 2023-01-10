# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# This example creates a new loadbalancer with SSL cipher suites. After that it creates a new listener with the SSL configuration and updates the backend set with it. Finally it updates the loadbalancer cipher suites and deletes it in the end.

import oci
import argparse

# ---------- parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--compartment-id',
                    help='compartment ID in which to perform the operation',
                    required=True
                    )
parser.add_argument('--subnet-id',
                    help='subnet ID in which the load balancer will be created',
                    required=True
                    )
parser.add_argument('--display-name',
                    help='display name for the load balancer to be created',
                    required=False,
                    default='python-sdk-create-lb-example'
                    )
parser.add_argument('--shape-name',
                    help='shape name of the load balancer to be created',
                    required=False,
                    default='100Mbps'
                    )
args = parser.parse_args()

# ---------- certificate keys
cert_private_key = """-----BEGIN RSA PRIVATE KEY-----### the content of your private key ###-----END RSA PRIVATE KEY-----"""
cert_public_key = """-----BEGIN CERTIFICATE-----### the content of your certificate ###-----END CERTIFICATE-----"""
cert_password = "password of your certificate"

# ---------- assign provided arguments
compartment_id = args.compartment_id
subnet_id = args.subnet_id
display_name = args.display_name
shape_name = args.shape_name

# ---------- read config from file
config = oci.config.from_file()
load_balancer_client = oci.load_balancer.LoadBalancerClient(config)
load_balancer_client_composite_ops = oci.load_balancer.LoadBalancerClientCompositeOperations(load_balancer_client)

print('Create new Load Balancer')
print('\n================================\n')
# ---------- create load balancer
load_balancer = load_balancer_client_composite_ops.create_load_balancer_and_wait_for_state(
    oci.load_balancer.models.CreateLoadBalancerDetails(
        compartment_id=compartment_id,
        display_name=display_name,
        shape_name=shape_name,
        subnet_ids=[subnet_id],
        backend_sets={
            'backend1': oci.load_balancer.models.BackendSetDetails(
                policy='ROUND_ROBIN',
                health_checker=oci.load_balancer.models.HealthCheckerDetails(
                    protocol='HTTP',
                    url_path='/',
                    port=80,
                    retries=1,
                    timeout_in_millis=100,
                    interval_in_millis=1000
                ),
                session_persistence_configuration=oci.load_balancer.models.SessionPersistenceConfigurationDetails(
                    cookie_name='*',
                    disable_fallback=False
                )
            ),
            'backend2': oci.load_balancer.models.BackendSetDetails(
                policy='ROUND_ROBIN',
                health_checker=oci.load_balancer.models.HealthCheckerDetails(
                    protocol='HTTP',
                    url_path='/testurl2',
                    port=80,
                    retries=1,
                    timeout_in_millis=100,
                    interval_in_millis=1000
                )
            )
        },
        ssl_cipher_suites={
            'test-suite': oci.load_balancer.models.SSLCipherSuiteDetails(
                name='test-suite',
                ciphers=["ECDHE-RSA-AES256-GCM-SHA384", "ECDHE-ECDSA-AES256-GCM-SHA384", "ECDHE-RSA-AES128-GCM-SHA256"]
            )
        }

    ),
    [oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

load_balancer_ocid = load_balancer.data.id

print('Created Load Balancer %s' % (load_balancer_ocid))
print('\n================================\n')

print('Create new certificate')
print('\n================================\n')
load_balancer_client_composite_ops.create_certificate_and_wait_for_state(
    oci.load_balancer.models.CreateCertificateDetails(
        certificate_name='example-certificate',
        public_certificate=cert_public_key,
        passphrase=cert_password,
        private_key=cert_private_key,
        ca_certificate=cert_public_key
    ),
    load_balancer_ocid,
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

print('Create new listener with ssl configuration')
print('\n================================\n')
load_balancer_client_composite_ops.create_listener_and_wait_for_state(
    oci.load_balancer.models.CreateListenerDetails(
        name='listener1',
        default_backend_set_name='backend1',
        port=8080,
        protocol='HTTP',
        ssl_configuration=oci.load_balancer.models.SSLConfigurationDetails(
            certificate_name='example-certificate',
            cipher_suite_name='test-suite',
            protocols=["TLSv1.1", "TLSv1.2"],
            server_order_preference="ENABLED",
            verify_peer_certificate=True
        )
    ),
    load_balancer_ocid,
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

print('Update backend sets with sslconfig')
print('\n================================\n')
load_balancer_client_composite_ops.update_backend_set_and_wait_for_state(
    oci.load_balancer.models.UpdateBackendSetDetails(
        policy='ROUND_ROBIN',
        health_checker=oci.load_balancer.models.HealthCheckerDetails(
            protocol='HTTP',
            url_path='/testurl2',
            port=80,
            retries=1,
            timeout_in_millis=100,
            interval_in_millis=1000
        ),
        ssl_configuration=oci.load_balancer.models.SSLConfigurationDetails(
            certificate_name='example-certificate',
            cipher_suite_name='test-suite',
            protocols=["TLSv1.1"],
            verify_peer_certificate=False
        ),
        backends=[]
    ),
    load_balancer_ocid,
    'backend1',
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

print('Update ssl cipher suite')
print('\n================================\n')
load_balancer_client_composite_ops.update_ssl_cipher_suite_and_wait_for_state(
    oci.load_balancer.models.UpdateSSLCipherSuiteDetails(
        ciphers=["DHE-DSS-AES256-SHA256", "CAMELLIA256-SHA"]
    ),
    load_balancer_ocid,
    'test-suite',
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED]
)

print("Attempting to delete load balancer {}".format(load_balancer_ocid))
print('\n================================\n')
load_balancer_client_composite_ops.delete_load_balancer_and_wait_for_state(
    load_balancer_ocid,
    wait_for_states=[oci.load_balancer.models.WorkRequest.LIFECYCLE_STATE_SUCCEEDED])
print('Deleted Load Balancer')
