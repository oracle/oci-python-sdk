# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from . import util
from .. import test_config_container
import datetime
import oci

SENDER_EMAIL_ADDRESS = 'integ@pythonsdktesting.com'
SUPPRESSION_EMAIL_ADDRESS = 'suppress@pythonsdktesting.com'


def test_crud_sender(email_client):
    with test_config_container.create_vcr().use_cassette('test_email_crud_sender.yml'):
        created_senders = []

        try:
            created_senders = create_senders(email_client, [SENDER_EMAIL_ADDRESS], wait_for_active=False)
            sender = created_senders[0]

            current_senders = oci.pagination.list_call_get_all_results(
                email_client.list_senders,
                util.COMPARTMENT_ID
            ).data
            assert len(current_senders) > 0

            found_sender_summary = None
            for cs in current_senders:
                if cs.id == sender.id:
                    found_sender_summary = cs
                    assert cs.email_address == sender.email_address
                    assert cs.time_created == sender.time_created
                    assert cs.lifecycle_state
                    break
            assert found_sender_summary

            current_senders = oci.pagination.list_call_get_all_results(
                email_client.list_senders,
                util.COMPARTMENT_ID,
                email_address=sender.email_address
            ).data
            assert len(current_senders) == 1
            assert found_sender_summary == current_senders[0]
        finally:
            if created_senders:
                for cs in created_senders:
                    delete_sender(email_client, cs)


def test_crud_suppression(email_client, config):
    with test_config_container.create_vcr().use_cassette('test_email_crud_suppression.yml'):
        created_suppressions = []

        try:
            created_suppressions = create_suppressions(email_client, [SUPPRESSION_EMAIL_ADDRESS], config)
            suppression = created_suppressions[0]

            current_suppressions = oci.pagination.list_call_get_all_results(
                email_client.list_suppressions,
                config['tenancy']
            ).data
            assert len(current_suppressions) > 0

            found_suppression_summary = None
            for cs in current_suppressions:
                if cs.id == suppression.id:
                    found_suppression_summary = cs
                    assert cs.email_address == suppression.email_address
                    assert cs.time_created == suppression.time_created
                    assert cs.reason == suppression.reason
                    break
            assert found_suppression_summary

            current_suppressions = oci.pagination.list_call_get_all_results(
                email_client.list_suppressions,
                config['tenancy'],
                email_address=suppression.email_address
            ).data
            assert len(current_suppressions) == 1
            assert found_suppression_summary == current_suppressions[0]
        finally:
            if created_suppressions:
                for cs in created_suppressions:
                    delete_suppression(email_client, cs, config)


def test_list_senders_with_sort_and_filter(email_client):
    with test_config_container.create_vcr().use_cassette('test_email_list_senders.yml'):
        sender_email_addresses = [
            '1-{}'.format(SENDER_EMAIL_ADDRESS),
            '2-{}'.format(SENDER_EMAIL_ADDRESS),
            '3-{}'.format(SENDER_EMAIL_ADDRESS)
        ]
        created_senders = create_senders(email_client, sender_email_addresses, wait_for_active=False)

        try:
            list_senders_with_sorting(email_client, created_senders, 'EMAILADDRESS', 'ASC', lambda s: s.email_address)
            list_senders_with_sorting(email_client, created_senders, 'EMAILADDRESS', 'DESC', lambda s: s.email_address)
            list_senders_with_sorting(email_client, created_senders, 'TIMECREATED', 'ASC', lambda s: s.time_created)
            list_senders_with_sorting(email_client, created_senders, 'TIMECREATED', 'DESC', lambda s: s.time_created)

            # Email address filtering is done in test_crud_sender, so we just exercise lifecycle state here
            list_senders_with_lifecycle_state_filtering(email_client, created_senders)
        finally:
            for cs in created_senders:
                delete_sender(email_client, cs)


def test_list_suppressions_with_sort_and_filter(email_client, config):
    with test_config_container.create_vcr().use_cassette('test_email_list_suppressions.yml'):
        suppression_email_addresses = [
            '1-{}'.format(SUPPRESSION_EMAIL_ADDRESS),
            '2-{}'.format(SUPPRESSION_EMAIL_ADDRESS),
            '3-{}'.format(SUPPRESSION_EMAIL_ADDRESS)
        ]
        created_suppressions = create_suppressions(email_client, suppression_email_addresses, config)

        try:
            list_suppressions_with_sorting(email_client, created_suppressions, config, 'EMAILADDRESS', 'ASC', lambda s: s.email_address)
            list_suppressions_with_sorting(email_client, created_suppressions, config, 'EMAILADDRESS', 'DESC', lambda s: s.email_address)
            list_suppressions_with_sorting(email_client, created_suppressions, config, 'TIMECREATED', 'ASC', lambda s: s.time_created)
            list_suppressions_with_sorting(email_client, created_suppressions, config, 'TIMECREATED', 'DESC', lambda s: s.time_created)

            list_suppressions_no_results_with_created_less_than(email_client, created_suppressions, config)
            list_suppressions_results_with_created_less_than(email_client, created_suppressions, config)

            list_suppressions_no_results_with_greater_than_or_equal_to(email_client, created_suppressions, config)
            list_suppressions_results_with_greater_than_or_equal_to(email_client, created_suppressions, config)

            list_suppressions_no_results_with_date_range(email_client, created_suppressions, config)
            list_suppressions_results_with_date_range(email_client, created_suppressions, config)
        finally:
            for cs in created_suppressions:
                delete_suppression(email_client, cs, config)


def list_senders_with_sorting(email_client, created_senders, sort_by, sort_order, sort_key_lambda):
    senders = oci.pagination.list_call_get_all_results(
        email_client.list_senders,
        util.COMPARTMENT_ID,
        sort_by=sort_by,
        sort_order=sort_order
    ).data
    assert len(senders) >= len(created_senders)

    sorted_senders = sorted(senders, key=sort_key_lambda, reverse=(sort_order == 'DESC'))
    for idx, val in enumerate(sorted_senders):
        assert val.id
        assert val.lifecycle_state
        assert val.time_created
        assert val.email_address
        assert val == senders[idx]


def list_senders_with_lifecycle_state_filtering(email_client, created_senders):
    senders = oci.pagination.list_call_get_all_results(
        email_client.list_senders,
        util.COMPARTMENT_ID,
        lifecycle_state=created_senders[0].lifecycle_state
    ).data
    assert len(senders) > 0

    found_sender = False
    for s in senders:
        assert s.lifecycle_state == created_senders[0].lifecycle_state
        if s.id == created_senders[0].id:
            found_sender = True
            assert s.email_address == created_senders[0].email_address
            assert s.time_created == created_senders[0].time_created
    assert found_sender

    senders = oci.pagination.list_call_get_all_results(
        email_client.list_senders,
        util.COMPARTMENT_ID,
        lifecycle_state='DELETED'
    ).data
    for s in senders:
        for cs in created_senders:
            assert s.id != cs.id


def list_suppressions_with_sorting(email_client, created_suppressions, config, sort_by, sort_order, sort_key_lambda):
    suppressions = oci.pagination.list_call_get_all_results(
        email_client.list_suppressions,
        config['tenancy'],
        sort_by=sort_by,
        sort_order=sort_order
    ).data
    assert len(suppressions) >= len(created_suppressions)

    # The sort order employeed by the server puts '_' after '3' when in accending
    # order and before it when in descending order.  This is the opposite of
    # the Python algorithm.  Therefore email addresses with leading '_' characters
    # are causing the test to fail.  There is no guarentees that other tests
    # won't have email addresses that will cause this behavior, so remove all
    # email addresses which were not created for this test.
    if len(suppressions) > len(created_suppressions):
        suppressions = [x for x in suppressions if x in created_suppressions]

    sorted_suppressions = sorted(suppressions, key=sort_key_lambda, reverse=(sort_order == 'DESC'))
    for idx, val in enumerate(sorted_suppressions):
        assert val.id
        assert val.reason
        assert val.time_created
        assert val.email_address
        assert val == suppressions[idx]


def list_suppressions_no_results_with_created_less_than(email_client, created_suppressions, config):
    created_less_than = datetime.datetime(2001, 1, 1)

    suppressions = oci.pagination.list_call_get_all_results(
        email_client.list_suppressions,
        config['tenancy'],
        time_created_less_than=created_less_than
    ).data
    assert len(suppressions) == 0


def list_suppressions_no_results_with_greater_than_or_equal_to(email_client, created_suppressions, config):
    greater_than_or_equal = datetime.datetime.max

    suppressions = oci.pagination.list_call_get_all_results(
        email_client.list_suppressions,
        config['tenancy'],
        time_created_greater_than_or_equal_to=greater_than_or_equal
    ).data
    assert len(suppressions) == 0


def list_suppressions_no_results_with_date_range(email_client, created_suppressions, config):
    inclusive_lower_bound = datetime.datetime(2001, 1, 1)
    exclusive_upper_bound = datetime.datetime(2001, 1, 2)

    suppressions = oci.pagination.list_call_get_all_results(
        email_client.list_suppressions,
        config['tenancy'],
        time_created_less_than=exclusive_upper_bound,
        time_created_greater_than_or_equal_to=inclusive_lower_bound
    ).data
    assert len(suppressions) == 0


def list_suppressions_results_with_created_less_than(email_client, created_suppressions, config):
    created_less_than = created_suppressions[-1].time_created

    suppressions = oci.pagination.list_call_get_all_results(
        email_client.list_suppressions,
        config['tenancy'],
        time_created_less_than=created_less_than
    ).data
    assert len(suppressions) > 0

    # We should not have the last record because the bound is exclusive
    for s in suppressions:
        assert s.id != created_suppressions[-1].id

    for cs in created_suppressions:
        if cs.id == created_suppressions[-1].id:
            continue

        found_suppression = False
        for s in suppressions:
            if s.id == cs.id:
                found_suppression = True
                assert s.email_address == cs.email_address
                assert s.time_created < created_less_than
                assert s.time_created == cs.time_created
                assert s.reason == cs.reason
                break
        assert found_suppression


def list_suppressions_results_with_greater_than_or_equal_to(email_client, created_suppressions, config):
    greater_than_or_equal = created_suppressions[0].time_created

    suppressions = oci.pagination.list_call_get_all_results(
        email_client.list_suppressions,
        config['tenancy'],
        time_created_greater_than_or_equal_to=greater_than_or_equal
    ).data
    assert len(suppressions) >= len(created_suppressions)

    for cs in created_suppressions:
        found_suppression = False
        for s in suppressions:
            if s.id == cs.id:
                found_suppression = True
                assert s.email_address == cs.email_address
                assert s.reason == cs.reason
                assert s.time_created >= greater_than_or_equal
                assert s.time_created == cs.time_created
                break
        assert found_suppression


def list_suppressions_results_with_date_range(email_client, created_suppressions, config):
    inclusive_lower_bound = created_suppressions[0].time_created
    exclusive_upper_bound = created_suppressions[-1].time_created + datetime.timedelta(minutes=15)

    suppressions = oci.pagination.list_call_get_all_results(
        email_client.list_suppressions,
        config['tenancy'],
        time_created_less_than=exclusive_upper_bound,
        time_created_greater_than_or_equal_to=inclusive_lower_bound
    ).data
    assert len(suppressions) >= len(created_suppressions)

    for cs in created_suppressions:
        found_suppression = False
        for s in suppressions:
            if s.id == cs.id:
                found_suppression = True
                assert s.email_address == cs.email_address
                assert s.reason == cs.reason
                assert s.time_created >= inclusive_lower_bound
                assert s.time_created < exclusive_upper_bound
                assert s.time_created == cs.time_created
                break
        assert found_suppression


def create_senders(email_client, sender_addresses, wait_for_active=True):
    created_senders = []

    for sender in sender_addresses:
        create_response = email_client.create_sender(
            oci.email.models.CreateSenderDetails(
                compartment_id=util.COMPARTMENT_ID,
                email_address=sender
            )
        )
        assert create_response.request_id
        assert create_response.data.id
        assert create_response.data.email_address == sender
        assert create_response.data.time_created
        assert create_response.data.lifecycle_state

        get_sender_response = email_client.get_sender(create_response.data.id)
        assert get_sender_response.request_id
        if wait_for_active:
            get_sender_response = oci.wait_until(email_client, get_sender_response, 'lifecycle_state', 'ACTIVE')
            assert get_sender_response.request_id

        assert get_sender_response.data.email_address == sender
        assert get_sender_response.data.time_created == create_response.data.time_created
        if wait_for_active:
            assert get_sender_response.data.lifecycle_state == 'ACTIVE'
        else:
            assert get_sender_response.data.lifecycle_state

        created_senders.append(get_sender_response.data)

    return created_senders


def create_suppressions(email_client, suppression_addresses, config):
    created_suppressions = []

    for suppression in suppression_addresses:
        create_response = email_client.create_suppression(
            oci.email.models.CreateSuppressionDetails(
                compartment_id=config['tenancy'],
                email_address=suppression
            )
        )
        assert create_response.request_id
        assert create_response.data.id
        assert create_response.data.reason
        assert create_response.data.email_address == suppression
        assert create_response.data.time_created

        get_suppression_response = email_client.get_suppression(create_response.data.id)
        assert get_suppression_response.request_id
        assert get_suppression_response.data.reason == create_response.data.reason
        assert get_suppression_response.data.email_address == suppression
        assert get_suppression_response.data.time_created == create_response.data.time_created

        created_suppressions.append(get_suppression_response.data)

    return created_suppressions


def delete_sender(email_client, sender):
    get_sender_response = email_client.get_sender(sender.id)
    delete_response = email_client.delete_sender(sender.id)
    assert delete_response.request_id

    oci.wait_until(email_client, get_sender_response, 'lifecycle_state', 'DELETED', succeed_on_not_found=True)

    list_response = email_client.list_senders(util.COMPARTMENT_ID, email_address=sender.email_address)
    assert len(list_response.data) == 0


def delete_suppression(email_client, suppression, config):
    delete_response = email_client.delete_suppression(suppression.id)
    assert delete_response.request_id

    list_response = email_client.list_suppressions(config['tenancy'], email_address=suppression.email_address)
    assert len(list_response.data) == 0
