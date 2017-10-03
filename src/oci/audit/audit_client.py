# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import get_config_value_or_default, validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import audit_type_mapping
missing = Sentinel("Missing")


class AuditClient(object):

    def __init__(self, config):
        validate_config(config)
        signer = Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config.get("key_file"),
            pass_phrase=get_config_value_or_default(config, "pass_phrase"),
            private_key_content=config.get("key_content")
        )
        self.base_client = BaseClient("audit", config, signer, audit_type_mapping)

    def get_configuration(self, compartment_id, **kwargs):
        """
        GetConfiguration
        Get the configuration


        :param str compartment_id: (required)
            ID of the root compartment (tenancy)

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.audit.models.Configuration`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/configuration"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_configuration got unknown kwargs: {!r}".format(kwargs))

        query_params = {
            "compartmentId": compartment_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="Configuration")

    def list_events(self, compartment_id, start_time, end_time, **kwargs):
        """
        ListEvents
        Returns all audit events for the specified compartment that were processed within the specified time range.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param datetime start_time: (required)
            Returns events that were processed at or after this start date and time, expressed in `RFC 3339`__ timestamp format.
            For example, a start value of `2017-01-15T11:30:00Z` will retrieve a list of all events processed since 30 minutes after the 11th hour of January 15, 2017, in Coordinated Universal Time (UTC).
            You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`.

            __ https://tools.ietf.org/html/rfc3339

        :param datetime end_time: (required)
            Returns events that were processed before this end date and time, expressed in `RFC 3339`__ timestamp format. For example, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-01-02T00:00:00Z` will retrieve a list of all events processed on January 1, 2017.
            Similarly, a start value of `2017-01-01T00:00:00Z` and an end value of `2017-02-01T00:00:00Z` will result in a list of all events processed between January 1, 2017 and January 31, 2017.
            You can specify a value with granularity to the minute. Seconds (and milliseconds, if included) must be set to `0`.

            __ https://tools.ietf.org/html/rfc3339

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous list query.

        :param str opc_request_id: (optional)
            Unique Oracle-assigned identifier for the request.
            If you need to contact Oracle about a particular request, please provide the request ID.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.audit.models.AuditEvent`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/auditEvents"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "page",
            "opc_request_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_events got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "startTime": start_time,
            "endTime": end_time,
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[AuditEvent]")

    def update_configuration(self, compartment_id, update_configuration_details, **kwargs):
        """
        UpdateConfiguration
        Update the configuration


        :param str compartment_id: (required)
            ID of the root compartment (tenancy)

        :param UpdateConfigurationDetails update_configuration_details: (required)
            The configuration properties

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/configuration"
        method = "PUT"

        if kwargs:
            raise ValueError(
                "update_configuration got unknown kwargs: {!r}".format(kwargs))

        query_params = {
            "compartmentId": compartment_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            body=update_configuration_details)
