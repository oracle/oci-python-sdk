# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
    if test_config_container.test_mode == 'mock':
        yield
    else:
        # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
        # instead of 'query' matcher (which ignores sessionId in the url)
        # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
        custom_vcr = test_config_container.create_vcr()
        custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

        cassette_location = os.path.join('generated', 'adm_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_change_knowledge_base_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ChangeKnowledgeBaseCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ChangeKnowledgeBaseCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ChangeKnowledgeBaseCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_knowledge_base_compartment(
                knowledge_base_id=request.pop(util.camelize('knowledgeBaseId')),
                change_knowledge_base_compartment_details=request.pop(util.camelize('ChangeKnowledgeBaseCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ChangeKnowledgeBaseCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_knowledge_base_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_change_vulnerability_audit_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ChangeVulnerabilityAuditCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ChangeVulnerabilityAuditCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ChangeVulnerabilityAuditCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_vulnerability_audit_compartment(
                vulnerability_audit_id=request.pop(util.camelize('vulnerabilityAuditId')),
                change_vulnerability_audit_compartment_details=request.pop(util.camelize('ChangeVulnerabilityAuditCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ChangeVulnerabilityAuditCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_vulnerability_audit_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_create_knowledge_base(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'CreateKnowledgeBase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'CreateKnowledgeBase')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='CreateKnowledgeBase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_knowledge_base(
                create_knowledge_base_details=request.pop(util.camelize('CreateKnowledgeBaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'CreateKnowledgeBase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_knowledge_base',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_create_vulnerability_audit(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'CreateVulnerabilityAudit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'CreateVulnerabilityAudit')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='CreateVulnerabilityAudit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_vulnerability_audit(
                create_vulnerability_audit_details=request.pop(util.camelize('CreateVulnerabilityAuditDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'CreateVulnerabilityAudit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vulnerabilityAudit',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_delete_knowledge_base(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'DeleteKnowledgeBase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'DeleteKnowledgeBase')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='DeleteKnowledgeBase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_knowledge_base(
                knowledge_base_id=request.pop(util.camelize('knowledgeBaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'DeleteKnowledgeBase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_knowledge_base',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_delete_vulnerability_audit(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'DeleteVulnerabilityAudit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'DeleteVulnerabilityAudit')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='DeleteVulnerabilityAudit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_vulnerability_audit(
                vulnerability_audit_id=request.pop(util.camelize('vulnerabilityAuditId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'DeleteVulnerabilityAudit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_vulnerability_audit',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_get_knowledge_base(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'GetKnowledgeBase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'GetKnowledgeBase')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='GetKnowledgeBase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_knowledge_base(
                knowledge_base_id=request.pop(util.camelize('knowledgeBaseId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'GetKnowledgeBase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'knowledgeBase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_get_vulnerability_audit(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'GetVulnerabilityAudit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'GetVulnerabilityAudit')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='GetVulnerabilityAudit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_vulnerability_audit(
                vulnerability_audit_id=request.pop(util.camelize('vulnerabilityAuditId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'GetVulnerabilityAudit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vulnerabilityAudit',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_list_application_dependency_vulnerabilities(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ListApplicationDependencyVulnerabilities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ListApplicationDependencyVulnerabilities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ListApplicationDependencyVulnerabilities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_application_dependency_vulnerabilities(
                vulnerability_audit_id=request.pop(util.camelize('vulnerabilityAuditId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_application_dependency_vulnerabilities(
                    vulnerability_audit_id=request.pop(util.camelize('vulnerabilityAuditId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_application_dependency_vulnerabilities(
                        vulnerability_audit_id=request.pop(util.camelize('vulnerabilityAuditId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ListApplicationDependencyVulnerabilities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationDependencyVulnerabilityCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_list_knowledge_bases(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ListKnowledgeBases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ListKnowledgeBases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ListKnowledgeBases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_knowledge_bases(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_knowledge_bases(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_knowledge_bases(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ListKnowledgeBases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'knowledgeBaseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_list_vulnerability_audits(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ListVulnerabilityAudits'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ListVulnerabilityAudits')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ListVulnerabilityAudits')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_vulnerability_audits(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vulnerability_audits(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vulnerability_audits(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ListVulnerabilityAudits',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vulnerabilityAuditCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_update_knowledge_base(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'UpdateKnowledgeBase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'UpdateKnowledgeBase')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='UpdateKnowledgeBase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_knowledge_base(
                knowledge_base_id=request.pop(util.camelize('knowledgeBaseId')),
                update_knowledge_base_details=request.pop(util.camelize('UpdateKnowledgeBaseDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'UpdateKnowledgeBase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_knowledge_base',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="amw-dev_ww_grp@oracle.com" jiraProject="AMW" opsJiraProject="AMW"
def test_update_vulnerability_audit(testing_service_client):
    if not testing_service_client.is_api_enabled('adm', 'UpdateVulnerabilityAudit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('adm', util.camelize('application_dependency_management'), 'UpdateVulnerabilityAudit')
    )

    request_containers = testing_service_client.get_requests(service_name='adm', api_name='UpdateVulnerabilityAudit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.adm.ApplicationDependencyManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_vulnerability_audit(
                vulnerability_audit_id=request.pop(util.camelize('vulnerabilityAuditId')),
                update_vulnerability_audit_details=request.pop(util.camelize('UpdateVulnerabilityAuditDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'adm',
            'UpdateVulnerabilityAudit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vulnerabilityAudit',
            False,
            False
        )
