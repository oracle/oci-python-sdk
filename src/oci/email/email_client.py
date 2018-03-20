# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import requests  # noqa: F401
import six

from .. import retry  # noqa: F401
from ..base_client import BaseClient
from ..config import get_config_value_or_default, validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import email_type_mapping
missing = Sentinel("Missing")


class EmailClient(object):

    def __init__(self, config, **kwargs):
        validate_config(config, signer=kwargs.get('signer'))
        if 'signer' in kwargs:
            signer = kwargs['signer']
        else:
            signer = Signer(
                tenancy=config["tenancy"],
                user=config["user"],
                fingerprint=config["fingerprint"],
                private_key_file_location=config.get("key_file"),
                pass_phrase=get_config_value_or_default(config, "pass_phrase"),
                private_key_content=config.get("key_content")
            )
        self.base_client = BaseClient("email", config, signer, email_type_mapping)
        self.retry_strategy = kwargs.get('retry_strategy')

    def create_sender(self, create_sender_details, **kwargs):
        """
        Creates a sender for a tenancy in a given compartment.
        Creates a sender for a tenancy in a given compartment.


        :param CreateSenderDetails create_sender_details: (required)
            Create a sender.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.email.models.Sender`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/senders"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_sender got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_sender_details,
                response_type="Sender")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_sender_details,
                response_type="Sender")

    def create_suppression(self, create_suppression_details, **kwargs):
        """
        Creates an email suppression for a tenancy.
        Adds recipient email addresses to the suppression list for a tenancy.


        :param CreateSuppressionDetails create_suppression_details: (required)
            Adds a single email address to the suppression list for a compartment's tenancy.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.email.models.Suppression`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/suppressions"
        method = "POST"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_suppression got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_suppression_details,
                response_type="Suppression")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_suppression_details,
                response_type="Suppression")

    def delete_sender(self, sender_id, **kwargs):
        """
        Deletes a sender for a tenancy in a given compartment.
        Deletes an approved sender for a tenancy in a given compartment for a
        provided `senderId`.


        :param str sender_id: (required)
            The unique OCID of the sender.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/senders/{senderId}"
        method = "DELETE"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_sender got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "senderId": sender_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_suppression(self, suppression_id, **kwargs):
        """
        Deletes a suppressed email address.
        Removes a suppressed recipient email address from the suppression list
        for a tenancy in a given compartment for a provided `suppressionId`.


        :param str suppression_id: (required)
            The unique OCID of the suppression.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/suppressions/{suppressionId}"
        method = "DELETE"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_suppression got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "suppressionId": suppression_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def get_sender(self, sender_id, **kwargs):
        """
        Gets an approved sender.
        Gets an approved sender for a given `senderId`.


        :param str sender_id: (required)
            The unique OCID of the sender.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.email.models.Sender`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/senders/{senderId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_sender got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "senderId": sender_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Sender")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Sender")

    def get_suppression(self, suppression_id, **kwargs):
        """
        Get a suppressed email address.
        Gets the details of a suppressed recipient email address for a given
        `suppressionId`. Each suppression is given a unique OCID.


        :param str suppression_id: (required)
            The unique OCID of the suppression.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.email.models.Suppression`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/suppressions/{suppressionId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_suppression got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "suppressionId": suppression_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Suppression")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Suppression")

    def list_senders(self, compartment_id, **kwargs):
        """
        Get a list of approved sender summaries.
        Gets a collection of approved sender email addresses and sender IDs.


        :param str compartment_id: (required)
            The OCID for the compartment.

        :param str lifecycle_state: (optional)
            The current state of a sender.

            Allowed values are: "CREATING", "ACTIVE", "DELETING", "DELETED"

        :param str email_address: (optional)
            The email address of the approved sender.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous
            GET request.

        :param int limit: (optional)
            The maximum number of items to return in a paginated GET request.

        :param str sort_by: (optional)
            The field to sort by. The `TIMECREATED` value returns the list in in
            descending order by default. The `EMAILADDRESS` value returns the list in
            ascending order by default. Use the `SortOrderQueryParam` to change the
            direction of the returned list of items.

            Allowed values are: "TIMECREATED", "EMAILADDRESS"

        :param str sort_order: (optional)
            The sort order to use, either ascending or descending order.

            Allowed values are: "ASC", "DESC"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.email.models.SenderSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/senders"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "lifecycle_state",
            "email_address",
            "page",
            "limit",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_senders got unknown kwargs: {!r}".format(extra_kwargs))

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "EMAILADDRESS"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "lifecycleState": kwargs.get("lifecycle_state", missing),
            "emailAddress": kwargs.get("email_address", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SenderSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SenderSummary]")

    def list_suppressions(self, compartment_id, **kwargs):
        """
        Get a summary of suppressed email addresses.
        Gets a list of suppressed recipient email addresses for a user. The
        `compartmentId` for suppressions must be a tenancy OCID. The returned list
        is sorted by creation time in descending order.


        :param str compartment_id: (required)
            The OCID for the compartment.

        :param str email_address: (optional)
            The email address of the suppression.

        :param datetime time_created_greater_than_or_equal_to: (optional)
            Search for suppressions that were created within a specific date range,
            using this parameter to specify the earliest creation date for the
            returned list (inclusive). Specifying this parameter without the
            corresponding `timeCreatedLessThan` parameter will retrieve suppressions created from the
            given `timeCreatedGreaterThanOrEqualTo` to the current time, in \"YYYY-MM-ddThh:mmZ\" format with a
            Z offset, as defined by RFC 3339.

            **Example:** 2016-12-19T16:39:57.600Z

        :param datetime time_created_less_than: (optional)
            Search for suppressions that were created within a specific date range,
            using this parameter to specify the latest creation date for the returned
            list (exclusive). Specifying this parameter without the corresponding
            `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all suppressions created before the
            specified end date, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as
            defined by RFC 3339.

            **Example:** 2016-12-19T16:39:57.600Z

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous
            GET request.

        :param int limit: (optional)
            The maximum number of items to return in a paginated GET request.

        :param str sort_by: (optional)
            The field to sort by. The `TIMECREATED` value returns the list in in
            descending order by default. The `EMAILADDRESS` value returns the list in
            ascending order by default. Use the `SortOrderQueryParam` to change the
            direction of the returned list of items.

            Allowed values are: "TIMECREATED", "EMAILADDRESS"

        :param str sort_order: (optional)
            The sort order to use, either ascending or descending order.

            Allowed values are: "ASC", "DESC"

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.email.models.SuppressionSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/suppressions"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "email_address",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "page",
            "limit",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_suppressions got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["TIMECREATED", "EMAILADDRESS"]
            if kwargs['sort_by'] not in sort_by_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_by`, must be one of {0}".format(sort_by_allowed_values)
                )

        if 'sort_order' in kwargs:
            sort_order_allowed_values = ["ASC", "DESC"]
            if kwargs['sort_order'] not in sort_order_allowed_values:
                raise ValueError(
                    "Invalid value for `sort_order`, must be one of {0}".format(sort_order_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "emailAddress": kwargs.get("email_address", missing),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SuppressionSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[SuppressionSummary]")
