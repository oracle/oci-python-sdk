# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import oci.pagination
import os


PAGE_SIZE = 10


def test_manual_paging(identity, config):
    request_number = 0
    previous_first_ocid = None
    next_page = None

    while True:
        if request_number == 0:
            response = identity.list_users(config["tenancy"], limit=PAGE_SIZE)
        else:
            response = identity.list_users(config["tenancy"], limit=PAGE_SIZE, page=next_page)

        if not response.has_next_page:
            break

        next_page = response.next_page
        request_number += 1
        assert response.status == 200
        assert previous_first_ocid != response.data[0].id

        previous_first_ocid = response.data[0].id

    # Make sure we've at least looked at a couple pages.
    assert request_number > 1


def test_pagination_get_all_results(identity, config):
    all_users_response = oci.pagination.list_call_get_all_results(identity.list_users, config["tenancy"])
    assert not all_users_response.has_next_page
    assert len(all_users_response.data) > 0

    found_test_user = False
    for user in all_users_response.data:
        if user.id == config["user"]:
            found_test_user = True
            break
    assert found_test_user


def test_pagination_get_all_results_second_style(search_client):
    all_results_response = oci.pagination.list_call_get_all_results(search_client.search_resources,
                                                                    oci.resource_search.models.FreeTextSearchDetails(text="test"))

    assert not all_results_response.has_next_page
    assert len(all_results_response.data) > 0


def test_pagination_get_up_to_limit(identity, config):
    # There may not be 70 users, so only check that we get no more than what we ask for
    list_users_response = oci.pagination.list_call_get_up_to_limit(identity.list_users, 70, 10, config["tenancy"])
    assert len(list_users_response.data) <= 70

    # There should always be at least one user, so asking for one should get us exactly one
    list_users_response = oci.pagination.list_call_get_up_to_limit(identity.list_users, 1, 1, config["tenancy"])
    assert list_users_response.has_next_page
    assert len(list_users_response.data) == 1


def test_pagination_get_up_to_limit_second_style(search_client):
    all_results_response = oci.pagination.list_call_get_up_to_limit(search_client.search_resources, 200, 10,
                                                                    oci.resource_search.models.FreeTextSearchDetails(
                                                                        text="test"))
    assert all_results_response.has_next_page
    assert len(all_results_response.data) > 0


def test_pagination_get_up_to_limit_none_limit(identity, config):
    list_users_response = oci.pagination.list_call_get_up_to_limit(identity.list_users, None, 10, config["tenancy"])
    assert list_users_response.has_next_page
    assert len(list_users_response.data) <= 10


def test_pagination_get_all_yields(identity, config):
    all_users = []
    found_test_user = True
    for user in oci.pagination.list_call_get_all_results_generator(identity.list_users, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        all_users.append(user)
        if config["user"] == user.id:
            found_test_user = True

    assert len(all_users) > 1
    assert found_test_user

    all_users_response = oci.pagination.list_call_get_all_results(identity.list_users, config["tenancy"])

    # Some jitter in case other tests are adding/removing users, but they should be close to each other
    assert abs(len(all_users_response.data) - len(all_users)) < 5


def test_pagination_get_up_to_limit_yields_none_limit(identity, config):
    num_iterations = 0
    call_result = None
    for response in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, None, 10, 'response', config["tenancy"]):
        call_result = response
        num_iterations += 1

    assert num_iterations == 1  # Since we had a none limit, yield a single page
    assert len(call_result.data) > 1
    assert len(call_result.data) <= 10

    users = []
    num_iterations = 0
    for user in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, None, 10, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        num_iterations += 1
        users.append(user)
    assert num_iterations == len(users)
    # Some jitter in case other tests are adding/removing users, but they should be close to each other
    assert abs(len(call_result.data) - len(users)) < 5


def test_pagination_get_up_to_limit_yields(identity, config):
    num_iterations = 0
    users_from_response_gen = []
    for response in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 70, 10, 'response', config["tenancy"]):
        num_iterations += 1
        users_from_response_gen.extend(response.data)
    assert num_iterations > 1
    # The identity service appears to respond with a next page as long as the current request
    # returned any results.
    # If last page of results is not full then the number of iterations is less than or equal to the ceiling of
    # total items / number in page + 1 for the page with no results.
    # This means that if there are 64 users and we want to get 70 with 10 users per page.  The number of iterations
    # is ceiling(64 / 10) == 7 + 1 more request because the request which returned the last 4 results has the
    # next_page set.
    assert num_iterations <= 8
    assert len(users_from_response_gen) <= 70

    users = []
    num_iterations = 0
    for user in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 70, 10, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        num_iterations += 1
        users.append(user)
    assert num_iterations > 1
    assert num_iterations <= 70
    assert len(users_from_response_gen) == len(users)

    users = []
    num_iterations = 0
    for user in oci.pagination.list_call_get_up_to_limit_generator(identity.list_users, 1, 1, 'record', config["tenancy"]):
        assert user.id is not None
        assert user.name is not None
        num_iterations += 1
        users.append(user)
    assert len(users) == 1
    assert num_iterations == 1


def test_pagination_when_no_data_exists(compute):
    all_records_eager = oci.pagination.list_call_get_all_results(compute.list_images, os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os')
    limit_records_eager = oci.pagination.list_call_get_up_to_limit(compute.list_images, 20, 5, os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os')

    assert len(all_records_eager.data) == 0
    assert len(limit_records_eager.data) == 0

    num_iterations = 0
    call_result = None
    for response in oci.pagination.list_call_get_all_results_generator(compute.list_images, 'response', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        call_result = response
    assert num_iterations == 1
    assert len(call_result.data) == 0

    num_iterations = 0
    call_result = None
    for response in oci.pagination.list_call_get_up_to_limit_generator(compute.list_images, 20, 5, 'response', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        call_result = response
    assert num_iterations == 1
    assert len(call_result.data) == 0

    num_iterations = 0
    records = []
    for image in oci.pagination.list_call_get_all_results_generator(compute.list_images, 'record', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        records.append(image)
    assert num_iterations == 0
    assert len(records) == 0

    num_iterations = 0
    records = []
    for image in oci.pagination.list_call_get_up_to_limit_generator(compute.list_images, 20, 5, 'record', os.environ.get("OCI_PYSDK_COMPARTMENT_ID"), operating_system='superman fake os'):
        num_iterations += 1
        records.append(image)
    assert num_iterations == 0
    assert len(records) == 0
