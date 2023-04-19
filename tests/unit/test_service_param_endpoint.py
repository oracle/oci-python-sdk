# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci


# Test - should return endpoint with service param value if it exists in path or query and is a required param
def test_should_return_endpoint_with_service_param_values(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    template = 'https://{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com'
    client.endpoint = template
    correct_endpoint = 'https://fakenameSpace.objectstorage.us-phoenix-1.oraclecloud.com'
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {}
    required_arguments = ['namespaceName']
    endpoint = client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Test - should return endpoint with service param values as empty string if is not in path or query params.
def test_should_return_endpoint_with_no_service_param_values(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    template = 'https://{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com'
    client.endpoint = template
    correct_endpoint = 'https://objectstorage.us-phoenix-1.oraclecloud.com'
    path_params = {}
    query_params = {}
    required_arguments = []
    endpoint = client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Test - should return empty string for service params that is not a required argument
def test_should_return_endpoint_with_no_service_param_value_due_to_not_required_arg(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    template = 'https://objectstorage.us-phoenix-1.oraclecloud.com'
    client.endpoint = template
    correct_endpoint = 'https://objectstorage.us-phoenix-1.oraclecloud.com'
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {}
    required_arguments = []
    endpoint = client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Should handle multiple service params in endpoint.
def test_should_return_multiple_service_param_values(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    template = 'https://{bucketName+Dot}{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com'
    client.endpoint = template
    correct_endpoint = 'https://fakeBucket.fakenameSpace.objectstorage.us-phoenix-1.oraclecloud.com'
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {'bucketName': 'fakeBucket'}
    required_arguments = ['namespaceName', 'bucketName']
    endpoint = client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Should handle +Dot and . service params
def test_should_return_multiple_service_param_values_combinations(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    template = 'https://{bucketName}.{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com'
    client.endpoint = template
    correct_endpoint = 'https://fakeBucket.fakenameSpace.objectstorage.us-phoenix-1.oraclecloud.com'
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {'bucketName': 'fakeBucket'}
    required_arguments = ['namespaceName', 'bucketName']
    endpoint = client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Ignore service params that is not a required argument
def test_should_ignore_service_params_not_required_arg(identity, config):
    client = oci.BaseClient('identity', config, identity.base_client.signer, {})
    template = 'https://{bucketName}.{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com'
    client.endpoint = template
    correct_endpoint = 'https://fakeBucket.objectstorage.us-phoenix-1.oraclecloud.com'
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {'bucketName': 'fakeBucket'}
    required_arguments = ['bucketName']
    endpoint = client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Test with service client, should return endpoint with service param value if it exists in path or query and is a required param
def test_service_client_should_return_endpoint_with_service_param_values(identity, config):
    client = identity
    template = 'https://{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    client.base_client.endpoint = template
    correct_endpoint = 'https://fakenameSpace.objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {}
    required_arguments = ['namespaceName']
    endpoint = client.base_client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Test with service client, should return endpoint with service param values as empty string if is not in path or query params.
def test_service_client_should_return_endpoint_with_no_service_param_values(identity, config):
    client = identity
    template = 'https://{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    client.base_client.endpoint = template
    correct_endpoint = 'https://objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    path_params = {}
    query_params = {}
    required_arguments = []
    endpoint = client.base_client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Test with service client, Ignore service params that is not a required argument
def test_service_client_should_ignore_service_params_not_required_arg(identity, config):
    client = identity
    template = 'https://{bucketName}.{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    client.base_client.endpoint = template
    correct_endpoint = 'https://fakeBucket.objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {'bucketName': 'fakeBucket'}
    required_arguments = ['bucketName']
    endpoint = client.base_client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    assert endpoint == correct_endpoint


# Test with service client, endpoint should use realm specific endpoint when client.client_level_realm_specific_endpoint_template_enabled=True
def test_service_client_use_realm_specific_endpoint_template_when_enabled(identity, config):
    client = identity
    service_endpoint_template_per_realm = {'oc1': 'https://{bucketName}.{namespaceName+Dot}reference.{region}.oci.customer-oci.com', 'oc2': 'https://{uuidPath+Dot}reference.{region}.oci.{secondLevelDomain}'}
    template = 'https://{bucketName}.{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    client.base_client.endpoint = template
    client.base_client.service_endpoint_template_per_realm = service_endpoint_template_per_realm
    client.base_client.set_region('us-phoenix-1')
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {'bucketName': 'fakeBucket'}
    required_arguments = ['bucketName']
    client.base_client.client_level_realm_specific_endpoint_template_enabled = True
    endpoint = client.base_client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    correct_endpoint = 'https://fakeBucket.reference.us-phoenix-1.oci.customer-oci.com/20160918'
    assert endpoint == correct_endpoint


# Test with service client, endpoint should not use realm specific endpoint when client.client_level_realm_specific_endpoint_template_enabled=False
def test_service_client_should_notuse_realm_specific_endpoint_template_when_disabled(identity, config):
    client = identity
    service_endpoint_template_per_realm = {'oc1': 'https://{bucketName}.{namespaceName+Dot}reference.{region}.oci.customer-oci.com', 'oc2': 'https://{uuidPath+Dot}reference.{region}.oci.{secondLevelDomain}'}
    template = 'https://{bucketName}.{namespaceName+Dot}objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    client.base_client.service_endpoint_template = template
    client.base_client.service_endpoint_template_per_realm = service_endpoint_template_per_realm
    client.base_client.set_region('us-phoenix-1')
    path_params = {'namespaceName': 'fakenameSpace'}
    query_params = {'bucketName': 'fakeBucket'}
    required_arguments = ['bucketName']
    client.base_client.client_level_realm_specific_endpoint_template_enabled = False
    endpoint = client.base_client.handle_service_params_in_endpoint(path_params, query_params, required_arguments)
    correct_endpoint = 'https://fakeBucket.objectstorage.us-phoenix-1.oraclecloud.com/20160918'
    assert endpoint == correct_endpoint
