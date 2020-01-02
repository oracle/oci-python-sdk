# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import pytest
from .. import test_config_container  # noqa: F401
from .. import util
import oci
import oci.exceptions as oci_exception
import os


def session_agnostic_query_matcher(r1, r2):
    r1_query = [x for x in r1.query if x[0] != 'sessionId']
    r2_query = [x for x in r2.query if x[0] != 'sessionId']
    return r1_query == r2_query


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'waas_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_accept_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'AcceptRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'AcceptRecommendations')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='AcceptRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.accept_recommendations(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                protection_rule_keys=request.pop(util.camelize('protection_rule_keys')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'AcceptRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accept_recommendations',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_change_address_list_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ChangeAddressListCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ChangeAddressListCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ChangeAddressListCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.change_address_list_compartment(
                address_list_id=request.pop(util.camelize('address_list_id')),
                change_address_list_compartment_details=request.pop(util.camelize('change_address_list_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ChangeAddressListCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_address_list_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_change_certificate_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ChangeCertificateCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ChangeCertificateCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ChangeCertificateCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.change_certificate_compartment(
                certificate_id=request.pop(util.camelize('certificate_id')),
                change_certificate_compartment_details=request.pop(util.camelize('change_certificate_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ChangeCertificateCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_certificate_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_change_custom_protection_rule_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ChangeCustomProtectionRuleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ChangeCustomProtectionRuleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ChangeCustomProtectionRuleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.change_custom_protection_rule_compartment(
                custom_protection_rule_id=request.pop(util.camelize('custom_protection_rule_id')),
                change_custom_protection_rule_compartment_details=request.pop(util.camelize('change_custom_protection_rule_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ChangeCustomProtectionRuleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_custom_protection_rule_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_change_waas_policy_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ChangeWaasPolicyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ChangeWaasPolicyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ChangeWaasPolicyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.change_waas_policy_compartment(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                change_waas_policy_compartment_details=request.pop(util.camelize('change_waas_policy_compartment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ChangeWaasPolicyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_waas_policy_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_create_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'CreateAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'CreateAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='CreateAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.create_address_list(
                create_address_list_details=request.pop(util.camelize('create_address_list_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'CreateAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addressList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_create_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'CreateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'CreateCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='CreateCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.create_certificate(
                create_certificate_details=request.pop(util.camelize('create_certificate_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'CreateCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_create_custom_protection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'CreateCustomProtectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'CreateCustomProtectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='CreateCustomProtectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.create_custom_protection_rule(
                create_custom_protection_rule_details=request.pop(util.camelize('create_custom_protection_rule_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'CreateCustomProtectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customProtectionRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_create_waas_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'CreateWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'CreateWaasPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='CreateWaasPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.create_waas_policy(
                create_waas_policy_details=request.pop(util.camelize('create_waas_policy_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'CreateWaasPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_waas_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_delete_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'DeleteAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'DeleteAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='DeleteAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.delete_address_list(
                address_list_id=request.pop(util.camelize('address_list_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'DeleteAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_address_list',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_delete_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'DeleteCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'DeleteCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='DeleteCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.delete_certificate(
                certificate_id=request.pop(util.camelize('certificate_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'DeleteCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_certificate',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_delete_custom_protection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'DeleteCustomProtectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'DeleteCustomProtectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='DeleteCustomProtectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.delete_custom_protection_rule(
                custom_protection_rule_id=request.pop(util.camelize('custom_protection_rule_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'DeleteCustomProtectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_custom_protection_rule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_delete_waas_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'DeleteWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'DeleteWaasPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='DeleteWaasPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.delete_waas_policy(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'DeleteWaasPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_waas_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_address_list(
                address_list_id=request.pop(util.camelize('address_list_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addressList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate(
                certificate_id=request.pop(util.camelize('certificate_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_custom_protection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetCustomProtectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetCustomProtectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetCustomProtectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_custom_protection_rule(
                custom_protection_rule_id=request.pop(util.camelize('custom_protection_rule_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetCustomProtectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customProtectionRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_device_fingerprint_challenge(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetDeviceFingerprintChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetDeviceFingerprintChallenge')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetDeviceFingerprintChallenge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_device_fingerprint_challenge(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetDeviceFingerprintChallenge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deviceFingerprintChallenge',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_human_interaction_challenge(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetHumanInteractionChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetHumanInteractionChallenge')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetHumanInteractionChallenge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_human_interaction_challenge(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetHumanInteractionChallenge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'humanInteractionChallenge',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_js_challenge(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetJsChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetJsChallenge')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetJsChallenge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_js_challenge(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetJsChallenge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jsChallenge',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_policy_config(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetPolicyConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetPolicyConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetPolicyConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_policy_config(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetPolicyConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'policyConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_protection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetProtectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetProtectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetProtectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_protection_rule(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                protection_rule_key=request.pop(util.camelize('protection_rule_key')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetProtectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_protection_settings(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetProtectionSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetProtectionSettings')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetProtectionSettings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_protection_settings(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetProtectionSettings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionSettings',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_waas_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetWaasPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetWaasPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_waas_policy(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetWaasPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'waasPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_waf_address_rate_limiting(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetWafAddressRateLimiting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetWafAddressRateLimiting')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetWafAddressRateLimiting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_waf_address_rate_limiting(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetWafAddressRateLimiting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addressRateLimiting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_waf_config(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetWafConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetWafConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetWafConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_waf_config(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetWafConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'wafConfig',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_access_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListAccessRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListAccessRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListAccessRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_access_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_access_rules(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_access_rules(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListAccessRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'accessRule',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_address_lists(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListAddressLists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListAddressLists')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListAddressLists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_address_lists(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_address_lists(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_address_lists(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListAddressLists',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addressListSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_caching_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListCachingRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListCachingRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListCachingRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_caching_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_caching_rules(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_caching_rules(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListCachingRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cachingRuleSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_captchas(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListCaptchas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListCaptchas')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListCaptchas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_captchas(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_captchas(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_captchas(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListCaptchas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'captcha',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_certificates(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListCertificates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListCertificates')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListCertificates')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_certificates(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_certificates(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_certificates(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListCertificates',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_custom_protection_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListCustomProtectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListCustomProtectionRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListCustomProtectionRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_custom_protection_rules(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_custom_protection_rules(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_custom_protection_rules(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListCustomProtectionRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customProtectionRuleSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_edge_subnets(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListEdgeSubnets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListEdgeSubnets')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListEdgeSubnets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_edge_subnets(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_edge_subnets(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_edge_subnets(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListEdgeSubnets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'edgeSubnet',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_good_bots(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListGoodBots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListGoodBots')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListGoodBots')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_good_bots(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_good_bots(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_good_bots(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListGoodBots',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'goodBot',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_protection_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListProtectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListProtectionRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListProtectionRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_protection_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_protection_rules(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_protection_rules(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListProtectionRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'protectionRule',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListRecommendations')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_recommendations(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_recommendations(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_recommendations(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recommendation',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_threat_feeds(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListThreatFeeds'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListThreatFeeds')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListThreatFeeds')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_threat_feeds(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_threat_feeds(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_threat_feeds(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListThreatFeeds',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'threatFeed',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_waas_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWaasPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWaasPolicies')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWaasPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_waas_policies(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_waas_policies(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_waas_policies(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWaasPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'waasPolicySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_waas_policy_custom_protection_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWaasPolicyCustomProtectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWaasPolicyCustomProtectionRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWaasPolicyCustomProtectionRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_waas_policy_custom_protection_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_waas_policy_custom_protection_rules(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_waas_policy_custom_protection_rules(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWaasPolicyCustomProtectionRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'waasPolicyCustomProtectionRuleSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_waf_blocked_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWafBlockedRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWafBlockedRequests')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWafBlockedRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_waf_blocked_requests(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_waf_blocked_requests(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_waf_blocked_requests(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWafBlockedRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'wafBlockedRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_waf_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWafLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWafLogs')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWafLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_waf_logs(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_waf_logs(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_waf_logs(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWafLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'wafLog',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_waf_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWafRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWafRequests')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWafRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_waf_requests(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_waf_requests(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_waf_requests(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWafRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'wafRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_waf_traffic(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWafTraffic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWafTraffic')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWafTraffic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_waf_traffic(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_waf_traffic(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_waf_traffic(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWafTraffic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'wafTrafficDatum',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_whitelists(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWhitelists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWhitelists')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWhitelists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_whitelists(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_whitelists(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_whitelists(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWhitelists',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'whitelist',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'ListWorkRequests')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_purge_cache(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'PurgeCache'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'PurgeCache')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='PurgeCache')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.purge_cache(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'PurgeCache',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'purge_cache',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_access_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateAccessRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateAccessRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateAccessRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_access_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                access_rules=request.pop(util.camelize('access_rules')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateAccessRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_access_rules',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_address_list(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateAddressList'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateAddressList')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateAddressList')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_address_list(
                address_list_id=request.pop(util.camelize('address_list_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateAddressList',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addressList',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_caching_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateCachingRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateCachingRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateCachingRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_caching_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                caching_rules_details=request.pop(util.camelize('caching_rules_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateCachingRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_caching_rules',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_captchas(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateCaptchas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateCaptchas')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateCaptchas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_captchas(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                captchas=request.pop(util.camelize('captchas')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateCaptchas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_captchas',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_certificate(
                certificate_id=request.pop(util.camelize('certificate_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_custom_protection_rule(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateCustomProtectionRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateCustomProtectionRule')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateCustomProtectionRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_custom_protection_rule(
                custom_protection_rule_id=request.pop(util.camelize('custom_protection_rule_id')),
                update_custom_protection_rule_details=request.pop(util.camelize('update_custom_protection_rule_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateCustomProtectionRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customProtectionRule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_device_fingerprint_challenge(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateDeviceFingerprintChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateDeviceFingerprintChallenge')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateDeviceFingerprintChallenge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_device_fingerprint_challenge(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_device_fingerprint_challenge_details=request.pop(util.camelize('update_device_fingerprint_challenge_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateDeviceFingerprintChallenge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_device_fingerprint_challenge',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_good_bots(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateGoodBots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateGoodBots')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateGoodBots')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_good_bots(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                good_bots=request.pop(util.camelize('good_bots')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateGoodBots',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_good_bots',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_human_interaction_challenge(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateHumanInteractionChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateHumanInteractionChallenge')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateHumanInteractionChallenge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_human_interaction_challenge(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_human_interaction_challenge_details=request.pop(util.camelize('update_human_interaction_challenge_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateHumanInteractionChallenge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_human_interaction_challenge',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_js_challenge(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateJsChallenge'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateJsChallenge')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateJsChallenge')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_js_challenge(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_js_challenge_details=request.pop(util.camelize('update_js_challenge_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateJsChallenge',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_js_challenge',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_policy_config(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdatePolicyConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdatePolicyConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdatePolicyConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_policy_config(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_policy_config_details=request.pop(util.camelize('update_policy_config_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdatePolicyConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_policy_config',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_protection_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateProtectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateProtectionRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateProtectionRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_protection_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                protection_rules=request.pop(util.camelize('protection_rules')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateProtectionRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_protection_rules',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_protection_settings(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateProtectionSettings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateProtectionSettings')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateProtectionSettings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_protection_settings(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_protection_settings_details=request.pop(util.camelize('update_protection_settings_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateProtectionSettings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_protection_settings',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_threat_feeds(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateThreatFeeds'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateThreatFeeds')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateThreatFeeds')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_threat_feeds(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                threat_feeds=request.pop(util.camelize('threat_feeds')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateThreatFeeds',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_threat_feeds',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_waas_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateWaasPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateWaasPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateWaasPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_waas_policy(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_waas_policy_details=request.pop(util.camelize('update_waas_policy_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateWaasPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_waas_policy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_waas_policy_custom_protection_rules(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateWaasPolicyCustomProtectionRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateWaasPolicyCustomProtectionRules')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateWaasPolicyCustomProtectionRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_waas_policy_custom_protection_rules(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_custom_protection_rules_details=request.pop(util.camelize('update_custom_protection_rules_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateWaasPolicyCustomProtectionRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_waas_policy_custom_protection_rules',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_waf_address_rate_limiting(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateWafAddressRateLimiting'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateWafAddressRateLimiting')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateWafAddressRateLimiting')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_waf_address_rate_limiting(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_waf_address_rate_limiting_details=request.pop(util.camelize('update_waf_address_rate_limiting_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateWafAddressRateLimiting',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_waf_address_rate_limiting',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_waf_config(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateWafConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateWafConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateWafConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_waf_config(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                update_waf_config_details=request.pop(util.camelize('update_waf_config_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateWafConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_waf_config',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_whitelists(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateWhitelists'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('waas'), 'UpdateWhitelists')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateWhitelists')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.waas.WaasClient(config, service_endpoint=service_endpoint)
            response = client.update_whitelists(
                waas_policy_id=request.pop(util.camelize('waas_policy_id')),
                whitelists=request.pop(util.camelize('whitelists')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateWhitelists',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_whitelists',
            False,
            False
        )
