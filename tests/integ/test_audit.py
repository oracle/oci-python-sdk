# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import datetime
import pytest
from . import util
from .. import test_config_container
import oci
import pytz


class TestAudit:
    def test_list_events(self, audit_client):
        pytest.skip('TODO: Fix this on both master and preview.')
        # Don't match on the query string because that includes the date range for the query (and that will change between runs)
        with test_config_container.create_vcr(match_on=['method', 'scheme', 'host', 'port', 'path']).use_cassette('test_audit_list_events.yml'):
            utc_now = datetime.datetime.utcnow()
            end_time = datetime.datetime(year=utc_now.year, month=utc_now.month, day=utc_now.day, hour=utc_now.hour, minute=0, second=0, microsecond=0, tzinfo=pytz.utc)
            start_time = end_time + datetime.timedelta(days=-90)
            response = audit_client.list_events(util.COMPARTMENT_ID, start_time, end_time)
            events = response.data
            assert 200 == response.status
            assert response.request_id is not None
            assert len(events) >= 0

            event_ids = set()
            for event in events:
                self.validate_event(event, util.COMPARTMENT_ID, start_time, end_time)
                event_ids.add(event.event_id)

            # verify next page list when it's available
            if response.next_page is not None:
                response = audit_client.list_events(
                    util.COMPARTMENT_ID, start_time, end_time, page=response.next_page)
                assert 200 == response.status
                assert len(response.data) >= 0

                # verify no dupe event in next page
                for event in response.data:
                    self.validate_event(event, util.COMPARTMENT_ID, start_time, end_time)
                    assert event.event_id not in event_ids

    def test_retention_config(self, audit_client, tenant_id):
        pytest.skip('TODO: Fix this on both master and preview.')
        with test_config_container.create_vcr().use_cassette('test_audit_retention_config.yml'):
            response = audit_client.get_configuration(tenant_id)
            assert 200 == response.status

            old_retention_period = response.data.retention_period_days

            request = oci.audit.models.UpdateConfigurationDetails()
            request.retention_period_days = 5

            # set retention periods to invalid range
            with pytest.raises(oci.exceptions.ServiceError) as excinfo:
                audit_client.update_configuration(tenant_id, request)
                assert 400 == excinfo.status

            # set to valid range 90-365
            request.retention_period_days = 100
            response = audit_client.update_configuration(tenant_id, request)
            assert 202 == response.status

            # restore to old value
            request.retention_period_days = old_retention_period
            response = audit_client.update_configuration(tenant_id, request)
            assert 202 == response.status

    def validate_event(self, event, compartment_id, start_time, end_time):
        assert compartment_id == event.compartment_id
        assert event.credential_id is not None
        assert event.event_id is not None
        assert event.event_source is not None
        assert event.event_time is not None
        assert event.event_type is not None
        assert event.principal_id is not None
        assert event.request_action is not None
        assert event.request_agent is not None
        assert event.request_headers is not None
        assert event.response_headers is not None
        assert event.response_status is not None
        assert event.response_time is not None
        assert event.tenant_id is not None

        # verify event time in the range if we're not mocking
        if not test_config_container.using_vcr_with_mock_responses():
            event_time = event.event_time
            # assert event_time.astimezone(pytz.utc) >= start_time and event_time.astimezone(pytz.utc) <= end_time
            assert event_time
