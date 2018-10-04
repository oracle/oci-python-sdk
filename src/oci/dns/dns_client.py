# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel
from .models import dns_type_mapping
missing = Sentinel("Missing")


class DnsClient(object):
    """
    API for managing DNS zones, records, and policies.
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default is that the client never times out. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
            by passing an instance of :py:class:`~oci.auth.signers.InstancePrincipalsSecurityTokenSigner` as the value for this keyword argument
        :type signer: :py:class:`~oci.signer.AbstractBaseSigner`

        :param obj retry_strategy: (optional)
            A retry strategy to apply to all calls made by this service client (i.e. at the client level). There is no retry strategy applied by default.
            Retry strategies can also be applied at the operation level by passing a ``retry_strategy`` keyword argument as part of calling the operation.
            Any value provided at the operation level will override whatever is specified at the client level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.
        """
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

        base_client_init_kwargs = {
            'regional_client': True,
            'service_endpoint': kwargs.get('service_endpoint'),
            'timeout': kwargs.get('timeout'),
            'base_path': '/20180115',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("dns", config, signer, dns_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def create_zone(self, create_zone_details, **kwargs):
        """
        Creates a new zone in the specified compartment. The `compartmentId`
        query parameter is required if the `Content-Type` header for the
        request is `text/dns`.


        :param CreateZoneDetails create_zone_details: (required)
            Details for creating a new zone.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Zone`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_zone got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

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
                body=create_zone_details,
                response_type="Zone")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                body=create_zone_details,
                response_type="Zone")

    def delete_domain_records(self, zone_name_or_id, domain, **kwargs):
        """
        Deletes all records at the specified zone and domain.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def delete_rr_set(self, zone_name_or_id, domain, rtype, **kwargs):
        """
        Deletes all records in the specified RRSet.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def delete_zone(self, zone_name_or_id, **kwargs):
        """
        Deletes the specified zone. A `204` response indicates that zone has been
        successfully deleted.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_zone got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params)

    def get_domain_records(self, zone_name_or_id, domain, **kwargs):
        """
        Gets a list of all records at the specified zone and domain.
        The results are sorted by `rtype` in alphabetical order by default. You
        can optionally filter and/or sort the results using the listed parameters.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str zone_version: (optional)
            The version of the zone for which data is requested.

        :param str rtype: (optional)
            Search by record type.
            Will match any record whose `type`__ (case-insensitive) equals the provided value.

            __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4

        :param str sort_by: (optional)
            The field by which to sort records.

            Allowed values are: "rtype", "ttl"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "limit",
            "page",
            "zone_version",
            "rtype",
            "sort_by",
            "sort_order",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["rtype", "ttl"]
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
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "zoneVersion": kwargs.get("zone_version", missing),
            "rtype": kwargs.get("rtype", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection")

    def get_rr_set(self, zone_name_or_id, domain, rtype, **kwargs):
        """
        Gets a list of all records in the specified RRSet. The results are
        sorted by `recordHash` by default.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str zone_version: (optional)
            The version of the zone for which data is requested.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RRSet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "limit",
            "page",
            "zone_version",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "zoneVersion": kwargs.get("zone_version", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RRSet")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RRSet")

    def get_zone(self, zone_name_or_id, **kwargs):
        """
        Gets information about the specified zone, including its creation date,
        zone type, and serial.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Zone`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_zone got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Zone")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="Zone")

    def get_zone_records(self, zone_name_or_id, **kwargs):
        """
        Gets all records in the specified zone. The results are
        sorted by `domain` in alphabetical order by default. For more
        information about records, please see `Resource Record (RR) TYPEs`__.

        __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str if_none_match: (optional)
            The `If-None-Match` header field makes the request method conditional on
            the absence of any current representation of the target resource, when
            the field-value is `*`, or having a selected representation with an
            entity-tag that does not match any of those listed in the field-value.

        :param str if_modified_since: (optional)
            The `If-Modified-Since` header field makes a GET or HEAD request method
            conditional on the selected representation's modification date being more
            recent than the date provided in the field-value.  Transfer of the
            selected representation's data is avoided if that data has not changed.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str zone_version: (optional)
            The version of the zone for which data is requested.

        :param str domain: (optional)
            Search by domain.
            Will match any record whose domain (case-insensitive) equals the provided value.

        :param str domain_contains: (optional)
            Search by domain.
            Will match any record whose domain (case-insensitive) contains the provided value.

        :param str rtype: (optional)
            Search by record type.
            Will match any record whose `type`__ (case-insensitive) equals the provided value.

            __ https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml#dns-parameters-4

        :param str sort_by: (optional)
            The field by which to sort records.

            Allowed values are: "domain", "rtype", "ttl"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_none_match",
            "if_modified_since",
            "limit",
            "page",
            "zone_version",
            "domain",
            "domain_contains",
            "rtype",
            "sort_by",
            "sort_order",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_zone_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["domain", "rtype", "ttl"]
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
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "zoneVersion": kwargs.get("zone_version", missing),
            "domain": kwargs.get("domain", missing),
            "domainContains": kwargs.get("domain_contains", missing),
            "rtype": kwargs.get("rtype", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-None-Match": kwargs.get("if_none_match", missing),
            "If-Modified-Since": kwargs.get("if_modified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="RecordCollection")

    def list_zones(self, compartment_id, **kwargs):
        """
        Gets a list of all zones in the specified compartment. The collection
        can be filtered by name, time created, and zone type.


        :param str compartment_id: (required)
            The OCID of the compartment the resource belongs to.

        :param int limit: (optional)
            The maximum number of items to return in a page of the collection.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param str name: (optional)
            A case-sensitive filter for zone names.
            Will match any zone with a name that equals the provided value.

        :param str name_contains: (optional)
            Search by zone name.
            Will match any zone whose name (case-insensitive) contains the provided value.

        :param str zone_type: (optional)
            Search by zone type, `PRIMARY` or `SECONDARY`.
            Will match any zone whose type equals the provided value.

            Allowed values are: "PRIMARY", "SECONDARY"

        :param datetime time_created_greater_than_or_equal_to: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created on or after the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param datetime time_created_less_than: (optional)
            An `RFC 3339`__ timestamp that states
            all returned resources were created before the indicated time.

            __ https://www.ietf.org/rfc/rfc3339.txt

        :param str sort_by: (optional)
            The field by which to sort zones.

            Allowed values are: "name", "zoneType", "timeCreated"

        :param str sort_order: (optional)
            The order to sort the resources.

            Allowed values are: "ASC", "DESC"

        :param str lifecycle_state: (optional)
            The state of a resource.

            Allowed values are: "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.dns.models.ZoneSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "limit",
            "page",
            "name",
            "name_contains",
            "zone_type",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "sort_by",
            "sort_order",
            "lifecycle_state"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_zones got unknown kwargs: {!r}".format(extra_kwargs))

        if 'zone_type' in kwargs:
            zone_type_allowed_values = ["PRIMARY", "SECONDARY"]
            if kwargs['zone_type'] not in zone_type_allowed_values:
                raise ValueError(
                    "Invalid value for `zone_type`, must be one of {0}".format(zone_type_allowed_values)
                )

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["name", "zoneType", "timeCreated"]
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

        if 'lifecycle_state' in kwargs:
            lifecycle_state_allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED"]
            if kwargs['lifecycle_state'] not in lifecycle_state_allowed_values:
                raise ValueError(
                    "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "compartmentId": compartment_id,
            "name": kwargs.get("name", missing),
            "nameContains": kwargs.get("name_contains", missing),
            "zoneType": kwargs.get("zone_type", missing),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "lifecycleState": kwargs.get("lifecycle_state", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

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
                response_type="list[ZoneSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ZoneSummary]")

    def patch_domain_records(self, zone_name_or_id, domain, patch_domain_records_details, **kwargs):
        """
        Replaces records in the specified zone at a domain. You can update one record or all records for the specified zone depending on the changes provided in the request body. You can also add or remove records using this function.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param PatchDomainRecordsDetails patch_domain_records_details: (required)
            Operations describing how to modify the collection of records.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "PATCH"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "patch_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_domain_records_details,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_domain_records_details,
                response_type="RecordCollection")

    def patch_rr_set(self, zone_name_or_id, domain, rtype, patch_rr_set_details, **kwargs):
        """
        Updates records in the specified RRSet.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param PatchRRSetDetails patch_rr_set_details: (required)
            Operations describing how to modify the collection of records.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "PATCH"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "patch_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_rr_set_details,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_rr_set_details,
                response_type="RecordCollection")

    def patch_zone_records(self, zone_name_or_id, patch_zone_records_details, **kwargs):
        """
        Updates a collection of records in the specified zone. You can update
        one record or all records for the specified zone depending on the
        changes provided in the request body. You can also add or remove records
        using this function.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param PatchZoneRecordsDetails patch_zone_records_details: (required)
            The operations describing how to modify the collection of records.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records"
        method = "PATCH"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "patch_zone_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_zone_records_details,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=patch_zone_records_details,
                response_type="RecordCollection")

    def update_domain_records(self, zone_name_or_id, domain, update_domain_records_details, **kwargs):
        """
        Replaces records in the specified zone at a domain with the records
        specified in the request body. If a specified record does not exist,
        it will be created. If the record exists, then it will be updated to
        represent the record in the body of the request. If a record in the zone
        does not exist in the request body, the record will be removed from the
        zone.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param UpdateDomainRecordsDetails update_domain_records_details: (required)
            A full list of records for the domain.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_domain_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_domain_records_details,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_domain_records_details,
                response_type="RecordCollection")

    def update_rr_set(self, zone_name_or_id, domain, rtype, update_rr_set_details, **kwargs):
        """
        Replaces records in the specified RRSet.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param str domain: (required)
            The target fully-qualified domain name (FQDN) within the target zone.

        :param str rtype: (required)
            The type of the target RRSet within the target zone.

        :param UpdateRRSetDetails update_rr_set_details: (required)
            A full list of records for the RRSet.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records/{domain}/{rtype}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_rr_set got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id,
            "domain": domain,
            "rtype": rtype
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_rr_set_details,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_rr_set_details,
                response_type="RecordCollection")

    def update_zone(self, zone_name_or_id, update_zone_details, **kwargs):
        """
        Updates the specified secondary zone with your new external master
        server information. For more information about secondary zone, see
        `Manage DNS Service Zone`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/DNS/Tasks/managingdnszones.htm


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param UpdateZoneDetails update_zone_details: (required)
            New data for the zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.Zone`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_zone got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_details,
                response_type="Zone")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_details,
                response_type="Zone")

    def update_zone_records(self, zone_name_or_id, update_zone_records_details, **kwargs):
        """
        Replaces records in the specified zone with the records specified in the
        request body. If a specified record does not exist, it will be created.
        If the record exists, then it will be updated to represent the record in
        the body of the request. If a record in the zone does not exist in the
        request body, the record will be removed from the zone.


        :param str zone_name_or_id: (required)
            The name or OCID of the target zone.

        :param UpdateZoneRecordsDetails update_zone_records_details: (required)
            A full list of records for the zone.

        :param str if_match: (optional)
            The `If-Match` header field makes the request method conditional on the
            existence of at least one current representation of the target resource,
            when the field-value is `*`, or having a current representation of the
            target resource that has an entity-tag matching a member of the list of
            entity-tags provided in the field-value.

        :param str if_unmodified_since: (optional)
            The `If-Unmodified-Since` header field makes the request method
            conditional on the selected representation's last modification date being
            earlier than or equal to the date provided in the field-value.  This
            field accomplishes the same purpose as If-Match for cases where the user
            agent does not have an entity-tag for the representation.

        :param str compartment_id: (optional)
            The OCID of the compartment the resource belongs to.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.dns.models.RecordCollection`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/zones/{zoneNameOrId}/records"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "if_unmodified_since",
            "compartment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_zone_records got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "zoneNameOrId": zone_name_or_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "compartmentId": kwargs.get("compartment_id", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "If-Match": kwargs.get("if_match", missing),
            "If-Unmodified-Since": kwargs.get("if_unmodified_since", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_records_details,
                response_type="RecordCollection")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                body=update_zone_records_details,
                response_type="RecordCollection")
