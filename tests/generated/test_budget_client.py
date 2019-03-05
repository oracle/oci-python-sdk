# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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

    cassette_location = os.path.join('generated', 'budget_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


def test_create_alert_rule(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'CreateAlertRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='CreateAlertRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.create_alert_rule(
                budget_id=request.pop(util.camelize('budget_id')),
                create_alert_rule_details=request.pop(util.camelize('create_alert_rule_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'CreateAlertRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertRule',
            False,
            False
        )


def test_create_budget(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'CreateBudget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='CreateBudget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.create_budget(
                create_budget_details=request.pop(util.camelize('create_budget_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'CreateBudget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'budget',
            False,
            False
        )


def test_delete_alert_rule(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'DeleteAlertRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='DeleteAlertRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.delete_alert_rule(
                budget_id=request.pop(util.camelize('budget_id')),
                alert_rule_id=request.pop(util.camelize('alert_rule_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'DeleteAlertRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_alert_rule',
            True,
            False
        )


def test_delete_budget(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'DeleteBudget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='DeleteBudget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.delete_budget(
                budget_id=request.pop(util.camelize('budget_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'DeleteBudget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_budget',
            True,
            False
        )


def test_get_alert_rule(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'GetAlertRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='GetAlertRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.get_alert_rule(
                budget_id=request.pop(util.camelize('budget_id')),
                alert_rule_id=request.pop(util.camelize('alert_rule_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'GetAlertRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertRule',
            False,
            False
        )


def test_get_budget(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'GetBudget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='GetBudget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.get_budget(
                budget_id=request.pop(util.camelize('budget_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'GetBudget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'budget',
            False,
            False
        )


def test_list_alert_rules(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'ListAlertRules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='ListAlertRules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.list_alert_rules(
                budget_id=request.pop(util.camelize('budget_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_alert_rules(
                    budget_id=request.pop(util.camelize('budget_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_alert_rules(
                        budget_id=request.pop(util.camelize('budget_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'ListAlertRules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertRuleSummary',
            False,
            True
        )


def test_list_budgets(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'ListBudgets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='ListBudgets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.list_budgets(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_budgets(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_budgets(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'ListBudgets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'budgetSummary',
            False,
            True
        )


def test_update_alert_rule(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'UpdateAlertRule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='UpdateAlertRule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.update_alert_rule(
                budget_id=request.pop(util.camelize('budget_id')),
                alert_rule_id=request.pop(util.camelize('alert_rule_id')),
                update_alert_rule_details=request.pop(util.camelize('update_alert_rule_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'UpdateAlertRule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'alertRule',
            False,
            False
        )


def test_update_budget(testing_service_client, config):
    if not testing_service_client.is_api_enabled('budget', 'UpdateBudget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='budget', api_name='UpdateBudget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.budget.BudgetClient(config)
            response = client.update_budget(
                budget_id=request.pop(util.camelize('budget_id')),
                update_budget_details=request.pop(util.camelize('update_budget_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'budget',
            'UpdateBudget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'budget',
            False,
            False
        )
