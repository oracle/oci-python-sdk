# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import datetime
import pytest
from . import util
import oci
import pytz


class TestAudit:

    def test_list_events(self, audit_client):
        end_time = datetime.datetime.utcnow()
        start_time = end_time + datetime.timedelta(days=-90)
        response = audit_client.list_events(
            util.COMPARTMENT_ID, start_time, end_time)
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
        assert event.request_parameters is not None  # may be empty though
        assert event.response_headers is not None
        assert event.response_status is not None
        assert event.response_time is not None
        assert event.tenant_id is not None
        # verify event time in the range
        event_time = event.event_time
        assert event_time >= pytz.utc.localize(start_time) and event_time <= pytz.utc.localize(end_time)
