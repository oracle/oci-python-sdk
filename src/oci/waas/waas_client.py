# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from oci._vendor import requests  # noqa: F401
from oci._vendor import six

from oci import retry  # noqa: F401
from oci.base_client import BaseClient
from oci.config import get_config_value_or_default, validate_config
from oci.signer import Signer
from oci.util import Sentinel, get_signer_from_authentication_type, AUTHENTICATION_TYPE_FIELD_NAME
from .models import waas_type_mapping
missing = Sentinel("Missing")


class WaasClient(object):
    """
    OCI Web Application Acceleration and Security Services
    """

    def __init__(self, config, **kwargs):
        """
        Creates a new service client

        :param dict config:
            Configuration keys and values as per `SDK and Tool Configuration <https://docs.cloud.oracle.com/Content/API/Concepts/sdkconfig.htm>`__.
            The :py:meth:`~oci.config.from_file` method can be used to load configuration from a file. Alternatively, a ``dict`` can be passed. You can validate_config
            the dict using :py:meth:`~oci.config.validate_config`

        :param str service_endpoint: (optional)
            The endpoint of the service to call using this client. For example ``https://iaas.us-ashburn-1.oraclecloud.com``. If this keyword argument is
            not provided then it will be derived using the region in the config parameter. You should only provide this keyword argument if you have an explicit
            need to specify a service endpoint.

        :param timeout: (optional)
            The connection and read timeouts for the client. The default values are connection timeout 10 seconds and read timeout 60 seconds. This keyword argument can be provided
            as a single float, in which case the value provided is used for both the read and connection timeouts, or as a tuple of two floats. If
            a tuple is provided then the first value is used as the connection timeout and the second value as the read timeout.
        :type timeout: float or tuple(float, float)

        :param signer: (optional)
            The signer to use when signing requests made by the service client. The default is to use a :py:class:`~oci.signer.Signer` based on the values
            provided in the config parameter.

            One use case for this parameter is for `Instance Principals authentication <https://docs.cloud.oracle.com/Content/Identity/Tasks/callingservicesfrominstances.htm>`__
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

        elif AUTHENTICATION_TYPE_FIELD_NAME in config:
            signer = get_signer_from_authentication_type(config)

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
            'base_path': '/20181116',
            'service_endpoint_template': 'https://waas.{region}.{secondLevelDomain}',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("waas", config, signer, waas_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def accept_recommendations(self, waas_policy_id, protection_rule_keys, **kwargs):
        """
        Accepts a list of recommended Web Application Firewall protection rules. Web Application Firewall protection rule recommendations are sets of rules generated by observed traffic patterns through the Web Application Firewall and are meant to optimize the Web Application Firewall's security profile. Only the rules specified in the request body will be updated; all other rules will remain unchanged.

        Use the `GET /waasPolicies/{waasPolicyId}/wafConfig/recommendations` method to view a list of recommended Web Application Firewall protection rules. For more information, see `WAF Protection Rules`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param list[str] protection_rule_keys: (required)

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "accept_recommendations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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
                header_params=header_params,
                body=protection_rule_keys)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=protection_rule_keys)

    def cancel_work_request(self, work_request_id, **kwargs):
        """
        Cancels a specified work request.


        :param str work_request_id: (required)
            The `OCID`__ of the work request. This number is generated when work request is created.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "cancel_work_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
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

    def change_address_list_compartment(self, address_list_id, change_address_list_compartment_details, **kwargs):
        """
        Moves address list into a different compartment. When provided, If-Match
        is checked against ETag values of the address list. For information about moving
        resources between compartments, see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str address_list_id: (required)
            The `OCID`__ of the address list. This number is generated when the address list is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.ChangeAddressListCompartmentDetails change_address_list_compartment_details: (required)

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/addressLists/{addressListId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_address_list_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "addressListId": address_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_address_list_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_address_list_compartment_details)

    def change_certificate_compartment(self, certificate_id, change_certificate_compartment_details, **kwargs):
        """
        Moves certificate into a different compartment. When provided, If-Match is checked against ETag values of the certificate.
        For information about moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str certificate_id: (required)
            The `OCID`__ of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.ChangeCertificateCompartmentDetails change_certificate_compartment_details: (required)

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/certificates/{certificateId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_certificate_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_certificate_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_certificate_compartment_details)

    def change_custom_protection_rule_compartment(self, custom_protection_rule_id, change_custom_protection_rule_compartment_details, **kwargs):
        """
        Moves a custom protection rule into a different compartment within the same tenancy. When provided, If-Match is checked against ETag values of the custom protection rule. For information about moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str custom_protection_rule_id: (required)
            The `OCID`__ of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.ChangeCustomProtectionRuleCompartmentDetails change_custom_protection_rule_compartment_details: (required)

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/customProtectionRules/{customProtectionRuleId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_custom_protection_rule_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "customProtectionRuleId": custom_protection_rule_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_custom_protection_rule_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_custom_protection_rule_compartment_details)

    def change_waas_policy_compartment(self, waas_policy_id, change_waas_policy_compartment_details, **kwargs):
        """
        Moves WAAS policy into a different compartment. When provided, If-Match is checked against ETag values of the WAAS policy.
        For information about moving resources between compartments, see `Moving Resources to a Different Compartment`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.ChangeWaasPolicyCompartmentDetails change_waas_policy_compartment_details: (required)

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/actions/changeCompartment"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "change_waas_policy_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing),
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_waas_policy_compartment_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=change_waas_policy_compartment_details)

    def create_address_list(self, create_address_list_details, **kwargs):
        """
        Creates an address list in a set compartment and allows it to be used in a WAAS policy and referenced by access rules. Addresses can be IP addresses and CIDR notations.


        :param oci.waas.models.CreateAddressListDetails create_address_list_details: (required)
            The details of the address list resource to create.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.AddressList`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/addressLists"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_address_list got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_address_list_details,
                response_type="AddressList")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_address_list_details,
                response_type="AddressList")

    def create_certificate(self, create_certificate_details, **kwargs):
        """
        Allows an SSL certificate to be added to a WAAS policy. The Web Application Firewall terminates SSL connections to inspect requests in runtime, and then re-encrypts requests before sending them to the origin for fulfillment.

        For more information, see `WAF Settings`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafsettings.htm


        :param oci.waas.models.CreateCertificateDetails create_certificate_details: (required)
            The details of the SSL certificate resource to create.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.Certificate`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/certificates"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_certificate_details,
                response_type="Certificate")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_certificate_details,
                response_type="Certificate")

    def create_custom_protection_rule(self, create_custom_protection_rule_details, **kwargs):
        """
        Creates a new custom protection rule in the specified compartment.

        Custom protection rules allow you to create rules in addition to the rulesets provided by the Web Application Firewall service, including rules from `ModSecurity`__. The syntax for custom rules is based on the ModSecurity syntax. For more information about custom protection rules, see `Custom Protection Rules`__.

        __ https://modsecurity.org/
        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/customprotectionrules.htm


        :param oci.waas.models.CreateCustomProtectionRuleDetails create_custom_protection_rule_details: (required)
            The details of the custom protection rule.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.CustomProtectionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/customProtectionRules"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_custom_protection_rule got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_custom_protection_rule_details,
                response_type="CustomProtectionRule")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_custom_protection_rule_details,
                response_type="CustomProtectionRule")

    def create_waas_policy(self, create_waas_policy_details, **kwargs):
        """
        Creates a new Web Application Acceleration and Security (WAAS) policy in the specified compartment. A WAAS policy must be established before creating Web Application Firewall (WAF) rules. To use WAF rules, your web application's origin servers must defined in the `WaasPolicy` schema.

        A domain name must be specified when creating a WAAS policy. The domain name should be different from the origins specified in your `WaasPolicy`. Once domain name is entered and stored, it is unchangeable.

        Use the record data returned in the `cname` field of the `WaasPolicy` object to create a CNAME record in your DNS configuration that will direct your domain's traffic through the WAF.

        For the purposes of access control, you must provide the OCID of the compartment where you want the service to reside. For information about access control and compartments, see `Overview of the IAM Service`__.

        You must specify a display name and domain for the WAAS policy. The display name does not have to be unique and can be changed. The domain name should be different from every origin specified in `WaasPolicy`.

        All Oracle Cloud Infrastructure resources, including WAAS policies, receive a unique, Oracle-assigned ID called an Oracle Cloud Identifier (OCID). When a resource is created, you can find its OCID in the response. You can also retrieve a resource's OCID by using a list API operation for that resource type, or by viewing the resource in the Console. Fore more information, see `Resource Identifiers`__.

        **Note:** After sending the POST request, the new object's state will temporarily be `CREATING`. Ensure that the resource's state has changed to `ACTIVE` before use.

        __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param oci.waas.models.CreateWaasPolicyDetails create_waas_policy_details: (required)
            The details of the WAAS policy.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_waas_policy got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_waas_policy_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_waas_policy_details)

    def delete_address_list(self, address_list_id, **kwargs):
        """
        Deletes the address list from the compartment if it is not used.


        :param str address_list_id: (required)
            The `OCID`__ of the address list. This number is generated when the address list is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/addressLists/{addressListId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_address_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "addressListId": address_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
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

    def delete_certificate(self, certificate_id, **kwargs):
        """
        Deletes an SSL certificate from the WAAS service.


        :param str certificate_id: (required)
            The `OCID`__ of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/certificates/{certificateId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
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

    def delete_custom_protection_rule(self, custom_protection_rule_id, **kwargs):
        """
        Deletes a Custom Protection rule.


        :param str custom_protection_rule_id: (required)
            The `OCID`__ of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/customProtectionRules/{customProtectionRuleId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_custom_protection_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "customProtectionRuleId": custom_protection_rule_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
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

    def delete_waas_policy(self, waas_policy_id, **kwargs):
        """
        Deletes a policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_waas_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
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

    def get_address_list(self, address_list_id, **kwargs):
        """
        Gets the details of an address list.


        :param str address_list_id: (required)
            The `OCID`__ of the address list. This number is generated when the address list is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.AddressList`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/addressLists/{addressListId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_address_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "addressListId": address_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="AddressList")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AddressList")

    def get_certificate(self, certificate_id, **kwargs):
        """
        Gets the details of an SSL certificate.


        :param str certificate_id: (required)
            The `OCID`__ of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.Certificate`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/certificates/{certificateId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="Certificate")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Certificate")

    def get_custom_protection_rule(self, custom_protection_rule_id, **kwargs):
        """
        Gets the details of a custom protection rule.


        :param str custom_protection_rule_id: (required)
            The `OCID`__ of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.CustomProtectionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/customProtectionRules/{customProtectionRuleId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_custom_protection_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "customProtectionRuleId": custom_protection_rule_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="CustomProtectionRule")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="CustomProtectionRule")

    def get_device_fingerprint_challenge(self, waas_policy_id, **kwargs):
        """
        Gets the device fingerprint challenge settings in the Web Application Firewall configuration for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.DeviceFingerprintChallenge`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/deviceFingerprintChallenge"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_device_fingerprint_challenge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="DeviceFingerprintChallenge")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DeviceFingerprintChallenge")

    def get_human_interaction_challenge(self, waas_policy_id, **kwargs):
        """
        Gets the human interaction challenge settings in the Web Application Firewall configuration for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.HumanInteractionChallenge`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/humanInteractionChallenge"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_human_interaction_challenge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="HumanInteractionChallenge")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="HumanInteractionChallenge")

    def get_js_challenge(self, waas_policy_id, **kwargs):
        """
        Gets the JavaScript challenge settings in the Web Application Firewall configuration for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.JsChallenge`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/jsChallenge"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_js_challenge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="JsChallenge")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="JsChallenge")

    def get_policy_config(self, waas_policy_id, **kwargs):
        """
        Gets the configuration of a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.PolicyConfig`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/policyConfig"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_policy_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="PolicyConfig")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="PolicyConfig")

    def get_protection_rule(self, waas_policy_id, protection_rule_key, **kwargs):
        """
        Gets the details of a protection rule in the Web Application Firewall configuration for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str protection_rule_key: (required)
            The protection rule key.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.ProtectionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/protectionRules/{protectionRuleKey}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_protection_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id,
            "protectionRuleKey": protection_rule_key
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="ProtectionRule")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ProtectionRule")

    def get_protection_settings(self, waas_policy_id, **kwargs):
        """
        Gets the protection settings in the Web Application Firewall configuration for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.ProtectionSettings`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/protectionSettings"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_protection_settings got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="ProtectionSettings")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="ProtectionSettings")

    def get_waas_policy(self, waas_policy_id, **kwargs):
        """
        Gets the details of a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.WaasPolicy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_waas_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="WaasPolicy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WaasPolicy")

    def get_waf_address_rate_limiting(self, waas_policy_id, **kwargs):
        """
        Gets the address rate limiting settings of the Web Application Firewall configuration for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.AddressRateLimiting`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/addressRateLimiting"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_waf_address_rate_limiting got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="AddressRateLimiting")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="AddressRateLimiting")

    def get_waf_config(self, waas_policy_id, **kwargs):
        """
        Gets the Web Application Firewall configuration details for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.WafConfig`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_waf_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="WafConfig")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WafConfig")

    def get_work_request(self, work_request_id, **kwargs):
        """
        Gets the details of a specified work request.


        :param str work_request_id: (required)
            The `OCID`__ of the work request. This number is generated when work request is created.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_work_request got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "workRequestId": work_request_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                header_params=header_params,
                response_type="WorkRequest")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest")

    def list_access_rules(self, waas_policy_id, **kwargs):
        """
        Gets the currently configured access rules for the Web Application Firewall configuration of a specified WAAS policy.
        The order of the access rules is important. The rules will be checked in the order they are specified and the first matching rule will be used.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.AccessRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/accessRules"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_access_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[AccessRule]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AccessRule]")

    def list_address_lists(self, compartment_id, **kwargs):
        """
        Gets a list of address lists that can be used in a WAAS policy.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment. This number is generated when the compartment is created.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param str sort_by: (optional)
            The value by which address lists are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.

            Allowed values are: "id", "name", "timeCreated"

        :param str sort_order: (optional)
            The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

            Allowed values are: "ASC", "DESC"

        :param list[str] id: (optional)
            Filter address lists using a list of address lists OCIDs.

        :param list[str] name: (optional)
            Filter address lists using a list of names.

        :param list[str] lifecycle_state: (optional)
            Filter address lists using a list of lifecycle states.

            Allowed values are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"

        :param datetime time_created_greater_than_or_equal_to: (optional)
            A filter that matches address lists created on or after the specified date-time.

        :param datetime time_created_less_than: (optional)
            A filter that matches address lists created before the specified date-time.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.AddressListSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/addressLists"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "id",
            "name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_address_lists got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "name", "timeCreated"]
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
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentId": compartment_id,
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "name": self.base_client.generate_collection_format_param(kwargs.get("name", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[AddressListSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AddressListSummary]")

    def list_caching_rules(self, waas_policy_id, **kwargs):
        """
        Gets the currently configured caching rules for the Web Application Firewall configuration of a specified WAAS policy.
        The rules are processed in the order they are specified in and the first matching rule will be used when processing a request.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.CachingRuleSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/cachingRules"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_caching_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[CachingRuleSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CachingRuleSummary]")

    def list_captchas(self, waas_policy_id, **kwargs):
        """
        Gets the list of currently configured CAPTCHA challenges in the Web
        Application Firewall configuration of a WAAS policy.

        The order of the CAPTCHA challenges is important. The URL for each
        CAPTCHA will be checked in the order they are created.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.Captcha`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/captchas"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_captchas got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[Captcha]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Captcha]")

    def list_certificates(self, compartment_id, **kwargs):
        """
        Gets a list of SSL certificates that can be used in a WAAS policy.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment. This number is generated when the compartment is created.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param str sort_by: (optional)
            The value by which certificate summaries are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.

            Allowed values are: "id", "compartmentId", "displayName", "notValidAfter", "timeCreated"

        :param str sort_order: (optional)
            The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

            Allowed values are: "ASC", "DESC"

        :param list[str] id: (optional)
            Filter certificates using a list of certificates OCIDs.

        :param list[str] display_name: (optional)
            Filter certificates using a list of display names.

        :param list[str] lifecycle_state: (optional)
            Filter certificates using a list of lifecycle states.

            Allowed values are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"

        :param datetime time_created_greater_than_or_equal_to: (optional)
            A filter that matches certificates created on or after the specified date-time.

        :param datetime time_created_less_than: (optional)
            A filter that matches certificates created before the specified date-time.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.CertificateSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/certificates"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "id",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_certificates got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "compartmentId", "displayName", "notValidAfter", "timeCreated"]
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
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "compartmentId": compartment_id,
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "displayName": self.base_client.generate_collection_format_param(kwargs.get("display_name", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[CertificateSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CertificateSummary]")

    def list_custom_protection_rules(self, compartment_id, **kwargs):
        """
        Gets a list of custom protection rules for the specified Web Application Firewall.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment. This number is generated when the compartment is created.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param str sort_by: (optional)
            The value by which custom protection rules are sorted in a paginated 'List' call. If unspecified, defaults to `timeCreated`.

            Allowed values are: "id", "compartmentId", "displayName", "modSecurityRuleId", "timeCreated"

        :param str sort_order: (optional)
            The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

            Allowed values are: "ASC", "DESC"

        :param list[str] id: (optional)
            Filter custom protection rules using a list of custom protection rule OCIDs.

        :param list[str] display_name: (optional)
            Filter custom protection rules using a list of display names.

        :param list[str] lifecycle_state: (optional)
            Filter Custom Protection rules using a list of lifecycle states.

            Allowed values are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"

        :param datetime time_created_greater_than_or_equal_to: (optional)
            A filter that matches Custom Protection rules created on or after the specified date-time.

        :param datetime time_created_less_than: (optional)
            A filter that matches custom protection rules created before the specified date-time.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.CustomProtectionRuleSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/customProtectionRules"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "id",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_custom_protection_rules got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "compartmentId", "displayName", "modSecurityRuleId", "timeCreated"]
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
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "displayName": self.base_client.generate_collection_format_param(kwargs.get("display_name", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[CustomProtectionRuleSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[CustomProtectionRuleSummary]")

    def list_edge_subnets(self, **kwargs):
        """
        Return the list of the tenant's edge node subnets. Use these CIDR blocks to restrict incoming traffic to your origin. These subnets are owned by OCI and forward traffic to customer origins. They are not associated with specific regions or compartments.


        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param str sort_by: (optional)
            The value by which edge node subnets are sorted in a paginated 'List' call. If unspecified, defaults to `timeModified`.

            Allowed values are: "cidr", "region", "timeModified"

        :param str sort_order: (optional)
            The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.EdgeSubnet`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/edgeSubnets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_edge_subnets got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["cidr", "region", "timeModified"]
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
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[EdgeSubnet]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[EdgeSubnet]")

    def list_good_bots(self, waas_policy_id, **kwargs):
        """
        Gets the list of good bots defined in the Web Application Firewall configuration for a WAAS policy.

        The list is sorted by `key`, in ascending order.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.GoodBot`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/goodBots"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_good_bots got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[GoodBot]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[GoodBot]")

    def list_protection_rules(self, waas_policy_id, **kwargs):
        """
        Gets the list of available protection rules for a WAAS policy. Use the `GetWafConfig` operation to view a list of currently configured protection rules for the Web Application Firewall, or use the `ListRecommendations` operation to get a list of recommended protection rules for the Web Application Firewall.
        The list is sorted by `key`, in ascending order.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param list[str] mod_security_rule_id: (optional)
            Filter rules using a list of ModSecurity rule IDs.

        :param list[str] action: (optional)
            Filter rules using a list of actions.

            Allowed values are: "OFF", "DETECT", "BLOCK"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.ProtectionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/protectionRules"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "mod_security_rule_id",
            "action"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_protection_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'action' in kwargs:
            action_allowed_values = ["OFF", "DETECT", "BLOCK"]
            for action_item in kwargs['action']:
                if action_item not in action_allowed_values:
                    raise ValueError(
                        "Invalid value for `action`, must be one of {0}".format(action_allowed_values)
                    )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "modSecurityRuleId": self.base_client.generate_collection_format_param(kwargs.get("mod_security_rule_id", missing), 'multi'),
            "action": self.base_client.generate_collection_format_param(kwargs.get("action", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[ProtectionRule]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ProtectionRule]")

    def list_recommendations(self, waas_policy_id, **kwargs):
        """
        Gets the list of recommended Web Application Firewall protection rules.

        Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended Web Application Firewall protection rules. For more information, see `WAF Protection Rules`__.
        The list is sorted by `key`, in ascending order.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str recommended_action: (optional)
            A filter that matches recommended protection rules based on the selected action. If unspecified, rules with any action type are returned.

            Allowed values are: "DETECT", "BLOCK"

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.Recommendation`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/recommendations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "recommended_action",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_recommendations got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'recommended_action' in kwargs:
            recommended_action_allowed_values = ["DETECT", "BLOCK"]
            if kwargs['recommended_action'] not in recommended_action_allowed_values:
                raise ValueError(
                    "Invalid value for `recommended_action`, must be one of {0}".format(recommended_action_allowed_values)
                )

        query_params = {
            "recommendedAction": kwargs.get("recommended_action", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[Recommendation]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Recommendation]")

    def list_threat_feeds(self, waas_policy_id, **kwargs):
        """
        Gets the list of available web application threat intelligence feeds
        and the actions set for each feed. The list is sorted by `key`,
        in ascending order.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.ThreatFeed`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/threatFeeds"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_threat_feeds got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[ThreatFeed]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[ThreatFeed]")

    def list_waas_policies(self, compartment_id, **kwargs):
        """
        Gets a list of WAAS policies.


        :param str compartment_id: (required)
            The `OCID`__ of the compartment. This number is generated when the compartment is created.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param str sort_by: (optional)
            The value by which policies are sorted in a paginated 'List' call.  If unspecified, defaults to `timeCreated`.

            Allowed values are: "id", "displayName", "timeCreated"

        :param str sort_order: (optional)
            The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

            Allowed values are: "ASC", "DESC"

        :param list[str] id: (optional)
            Filter policies using a list of policy OCIDs.

        :param list[str] display_name: (optional)
            Filter policies using a list of display names.

        :param list[str] lifecycle_state: (optional)
            Filter policies using a list of lifecycle states.

            Allowed values are: "CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"

        :param datetime time_created_greater_than_or_equal_to: (optional)
            A filter that matches policies created on or after the specified date and time.

        :param datetime time_created_less_than: (optional)
            A filter that matches policies created before the specified date-time.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.WaasPolicySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order",
            "id",
            "display_name",
            "lifecycle_state",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_waas_policies got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "displayName", "timeCreated"]
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
            lifecycle_state_allowed_values = ["CREATING", "ACTIVE", "FAILED", "UPDATING", "DELETING", "DELETED"]
            for lifecycle_state_item in kwargs['lifecycle_state']:
                if lifecycle_state_item not in lifecycle_state_allowed_values:
                    raise ValueError(
                        "Invalid value for `lifecycle_state`, must be one of {0}".format(lifecycle_state_allowed_values)
                    )

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing),
            "id": self.base_client.generate_collection_format_param(kwargs.get("id", missing), 'multi'),
            "displayName": self.base_client.generate_collection_format_param(kwargs.get("display_name", missing), 'multi'),
            "lifecycleState": self.base_client.generate_collection_format_param(kwargs.get("lifecycle_state", missing), 'multi'),
            "timeCreatedGreaterThanOrEqualTo": kwargs.get("time_created_greater_than_or_equal_to", missing),
            "timeCreatedLessThan": kwargs.get("time_created_less_than", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[WaasPolicySummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WaasPolicySummary]")

    def list_waas_policy_custom_protection_rules(self, waas_policy_id, **kwargs):
        """
        Gets the list of currently configured custom protection rules for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param list[str] mod_security_rule_id: (optional)
            Filter rules using a list of ModSecurity rule IDs.

        :param list[str] action: (optional)
            Filter rules using a list of actions.

            Allowed values are: "DETECT", "BLOCK"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.WaasPolicyCustomProtectionRuleSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/customProtectionRules"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "mod_security_rule_id",
            "action"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_waas_policy_custom_protection_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'action' in kwargs:
            action_allowed_values = ["DETECT", "BLOCK"]
            for action_item in kwargs['action']:
                if action_item not in action_allowed_values:
                    raise ValueError(
                        "Invalid value for `action`, must be one of {0}".format(action_allowed_values)
                    )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "modSecurityRuleId": self.base_client.generate_collection_format_param(kwargs.get("mod_security_rule_id", missing), 'multi'),
            "action": self.base_client.generate_collection_format_param(kwargs.get("action", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[WaasPolicyCustomProtectionRuleSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WaasPolicyCustomProtectionRuleSummary]")

    def list_waf_blocked_requests(self, waas_policy_id, **kwargs):
        """
        Gets the number of blocked requests by a Web Application Firewall feature in five minute blocks, sorted by `timeObserved` in ascending order (starting from oldest data).


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param datetime time_observed_greater_than_or_equal_to: (optional)
            A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.

        :param datetime time_observed_less_than: (optional)
            A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param list[str] waf_feature: (optional)
            Filter stats by the Web Application Firewall feature that triggered the block action. If unspecified, data for all WAF features will be returned.

            Allowed values are: "PROTECTION_RULES", "JS_CHALLENGE", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "CAPTCHA", "ADDRESS_RATE_LIMITING"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.WafBlockedRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/reports/waf/blocked"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "time_observed_greater_than_or_equal_to",
            "time_observed_less_than",
            "limit",
            "page",
            "waf_feature"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_waf_blocked_requests got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'waf_feature' in kwargs:
            waf_feature_allowed_values = ["PROTECTION_RULES", "JS_CHALLENGE", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "CAPTCHA", "ADDRESS_RATE_LIMITING"]
            for waf_feature_item in kwargs['waf_feature']:
                if waf_feature_item not in waf_feature_allowed_values:
                    raise ValueError(
                        "Invalid value for `waf_feature`, must be one of {0}".format(waf_feature_allowed_values)
                    )

        query_params = {
            "timeObservedGreaterThanOrEqualTo": kwargs.get("time_observed_greater_than_or_equal_to", missing),
            "timeObservedLessThan": kwargs.get("time_observed_less_than", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "wafFeature": self.base_client.generate_collection_format_param(kwargs.get("waf_feature", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[WafBlockedRequest]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WafBlockedRequest]")

    def list_waf_logs(self, waas_policy_id, **kwargs):
        """
        Gets structured Web Application Firewall event logs for a WAAS
        policy. Sorted by the `timeObserved` in ascending order (starting from the
        oldest recorded event).


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `20`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param datetime time_observed_greater_than_or_equal_to: (optional)
            A filter that matches log entries where the observed event occurred on or after a date and time specified in RFC 3339 format. If unspecified, defaults to two hours before receipt of the request.

        :param datetime time_observed_less_than: (optional)
            A filter that matches log entries where the observed event occurred before a date and time, specified in RFC 3339 format.

        :param str text_contains: (optional)
            A full text search for logs.

        :param list[str] access_rule_key: (optional)
            Filters logs by access rule key.

        :param list[str] action: (optional)
            Filters logs by Web Application Firewall action.

            Allowed values are: "BLOCK", "DETECT", "BYPASS", "LOG", "REDIRECTED"

        :param list[str] client_address: (optional)
            Filters logs by client IP address.

        :param list[str] country_code: (optional)
            Filters logs by country code. Country codes are in ISO 3166-1 alpha-2 format. For a list of codes, see `ISO's website`__.

            __ https://www.iso.org/obp/ui/#search/code/

        :param list[str] country_name: (optional)
            Filter logs by country name.

        :param list[str] fingerprint: (optional)
            Filter logs by device fingerprint.

        :param list[str] http_method: (optional)
            Filter logs by HTTP method.

            Allowed values are: "OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"

        :param list[str] incident_key: (optional)
            Filter logs by incident key.

        :param list[str] log_type: (optional)
            Filter by log type. For more information about WAF logs, see `Logs`__.

            __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/logs.htm

            Allowed values are: "ACCESS", "PROTECTION_RULES", "JS_CHALLENGE", "CAPTCHA", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "ADDRESS_RATE_LIMITING"

        :param list[str] origin_address: (optional)
            Filter by origin IP address.

        :param list[str] referrer: (optional)
            Filter by referrer.

        :param list[str] request_url: (optional)
            Filter by request URL.

        :param list[int] response_code: (optional)
            Filter by response code.

        :param list[str] threat_feed_key: (optional)
            Filter by threat feed key.

        :param list[str] user_agent: (optional)
            Filter by user agent.

        :param list[str] protection_rule_key: (optional)
            Filter by protection rule key.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.WafLog`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafLogs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "time_observed_greater_than_or_equal_to",
            "time_observed_less_than",
            "text_contains",
            "access_rule_key",
            "action",
            "client_address",
            "country_code",
            "country_name",
            "fingerprint",
            "http_method",
            "incident_key",
            "log_type",
            "origin_address",
            "referrer",
            "request_url",
            "response_code",
            "threat_feed_key",
            "user_agent",
            "protection_rule_key"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_waf_logs got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        if 'action' in kwargs:
            action_allowed_values = ["BLOCK", "DETECT", "BYPASS", "LOG", "REDIRECTED"]
            for action_item in kwargs['action']:
                if action_item not in action_allowed_values:
                    raise ValueError(
                        "Invalid value for `action`, must be one of {0}".format(action_allowed_values)
                    )

        if 'http_method' in kwargs:
            http_method_allowed_values = ["OPTIONS", "GET", "HEAD", "POST", "PUT", "DELETE", "TRACE", "CONNECT"]
            for http_method_item in kwargs['http_method']:
                if http_method_item not in http_method_allowed_values:
                    raise ValueError(
                        "Invalid value for `http_method`, must be one of {0}".format(http_method_allowed_values)
                    )

        if 'log_type' in kwargs:
            log_type_allowed_values = ["ACCESS", "PROTECTION_RULES", "JS_CHALLENGE", "CAPTCHA", "ACCESS_RULES", "THREAT_FEEDS", "HUMAN_INTERACTION_CHALLENGE", "DEVICE_FINGERPRINT_CHALLENGE", "ADDRESS_RATE_LIMITING"]
            for log_type_item in kwargs['log_type']:
                if log_type_item not in log_type_allowed_values:
                    raise ValueError(
                        "Invalid value for `log_type`, must be one of {0}".format(log_type_allowed_values)
                    )

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "timeObservedGreaterThanOrEqualTo": kwargs.get("time_observed_greater_than_or_equal_to", missing),
            "timeObservedLessThan": kwargs.get("time_observed_less_than", missing),
            "textContains": kwargs.get("text_contains", missing),
            "accessRuleKey": self.base_client.generate_collection_format_param(kwargs.get("access_rule_key", missing), 'multi'),
            "action": self.base_client.generate_collection_format_param(kwargs.get("action", missing), 'multi'),
            "clientAddress": self.base_client.generate_collection_format_param(kwargs.get("client_address", missing), 'multi'),
            "countryCode": self.base_client.generate_collection_format_param(kwargs.get("country_code", missing), 'multi'),
            "countryName": self.base_client.generate_collection_format_param(kwargs.get("country_name", missing), 'multi'),
            "fingerprint": self.base_client.generate_collection_format_param(kwargs.get("fingerprint", missing), 'multi'),
            "httpMethod": self.base_client.generate_collection_format_param(kwargs.get("http_method", missing), 'multi'),
            "incidentKey": self.base_client.generate_collection_format_param(kwargs.get("incident_key", missing), 'multi'),
            "logType": self.base_client.generate_collection_format_param(kwargs.get("log_type", missing), 'multi'),
            "originAddress": self.base_client.generate_collection_format_param(kwargs.get("origin_address", missing), 'multi'),
            "referrer": self.base_client.generate_collection_format_param(kwargs.get("referrer", missing), 'multi'),
            "requestUrl": self.base_client.generate_collection_format_param(kwargs.get("request_url", missing), 'multi'),
            "responseCode": self.base_client.generate_collection_format_param(kwargs.get("response_code", missing), 'multi'),
            "threatFeedKey": self.base_client.generate_collection_format_param(kwargs.get("threat_feed_key", missing), 'multi'),
            "userAgent": self.base_client.generate_collection_format_param(kwargs.get("user_agent", missing), 'multi'),
            "protectionRuleKey": self.base_client.generate_collection_format_param(kwargs.get("protection_rule_key", missing), 'multi')
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[WafLog]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WafLog]")

    def list_waf_requests(self, waas_policy_id, **kwargs):
        """
        Gets the number of requests managed by a Web Application Firewall
        over a specified period of time, including blocked requests. Sorted
        by `timeObserved` in ascending order (starting from oldest requests).


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param datetime time_observed_greater_than_or_equal_to: (optional)
            A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.

        :param datetime time_observed_less_than: (optional)
            A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.WafRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/reports/waf/requests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "time_observed_greater_than_or_equal_to",
            "time_observed_less_than",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_waf_requests got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "timeObservedGreaterThanOrEqualTo": kwargs.get("time_observed_greater_than_or_equal_to", missing),
            "timeObservedLessThan": kwargs.get("time_observed_less_than", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[WafRequest]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WafRequest]")

    def list_waf_traffic(self, waas_policy_id, **kwargs):
        """
        Gets the Web Application Firewall traffic data for a WAAS policy.
        Sorted by `timeObserved` in ascending order (starting from oldest data).


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param datetime time_observed_greater_than_or_equal_to: (optional)
            A filter that limits returned events to those occurring on or after a date and time, specified in RFC 3339 format. If unspecified, defaults to 30 minutes before receipt of the request.

        :param datetime time_observed_less_than: (optional)
            A filter that limits returned events to those occurring before a date and time, specified in RFC 3339 format.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.WafTrafficDatum`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/reports/waf/traffic"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "time_observed_greater_than_or_equal_to",
            "time_observed_less_than",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_waf_traffic got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "timeObservedGreaterThanOrEqualTo": kwargs.get("time_observed_greater_than_or_equal_to", missing),
            "timeObservedLessThan": kwargs.get("time_observed_less_than", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[WafTrafficDatum]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WafTrafficDatum]")

    def list_whitelists(self, waas_policy_id, **kwargs):
        """
        Gets the list of whitelists defined in the Web Application Firewall configuration for a WAAS policy.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.Whitelist`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/whitelists"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_whitelists got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                response_type="list[Whitelist]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Whitelist]")

    def list_work_requests(self, waas_policy_id, compartment_id, **kwargs):
        """
        Gets a list of subnets (CIDR notation) from which the WAAS EDGE may make requests. The subnets are owned by OCI and forward traffic to your origins. Allow traffic from these subnets to your origins. They are not associated with specific regions or compartments.


        :param str waas_policy_id: (required)
            The `OCID`__ of the policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str compartment_id: (required)
            The `OCID`__ of the compartment. This number is generated when the compartment is created.

            __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param int limit: (optional)
            The maximum number of items to return in a paginated call. If unspecified, defaults to `10`.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous paginated call.

        :param str sort_by: (optional)
            The value by which work requests are sorted in a paginated 'List' call. If unspecified, defaults to `timeAccepted`.

            Allowed values are: "id", "status", "timeAccepted", "timeStarted", "timeFinished", "operationType"

        :param str sort_order: (optional)
            The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.

            Allowed values are: "ASC", "DESC"

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.waas.models.WorkRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "limit",
            "page",
            "sort_by",
            "sort_order"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        if 'sort_by' in kwargs:
            sort_by_allowed_values = ["id", "status", "timeAccepted", "timeStarted", "timeFinished", "operationType"]
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
            "waasPolicyId": waas_policy_id,
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "sortBy": kwargs.get("sort_by", missing),
            "sortOrder": kwargs.get("sort_order", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing and v is not None}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing)
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
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]")

    def purge_cache(self, waas_policy_id, **kwargs):
        """
        Performs a purge of the cache for each specified resource. If no resources are passed, the cache for the entire Web Application Firewall will be purged.
        For more information, see `Caching Rules`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/cachingrules.htm#purge


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param PurgeCache purge_cache: (optional)

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/actions/purgeCache"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match",
            "purge_cache"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "purge_cache got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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
                header_params=header_params,
                body=kwargs.get('purge_cache'))
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('purge_cache'))

    def update_access_rules(self, waas_policy_id, access_rules, **kwargs):
        """
        Updates the list of access rules in the Web Application Firewall configuration for a specified WAAS policy. Access rules allow explicit actions to be defined and executed for requests that meet various conditions. A rule action can be set to allow, detect, or block requests. The detect setting allows the request to pass through the Web Application Firewall and is tagged with a `DETECT` flag in the Web Application Firewall's log.

        This operation can create, delete, update, and/or reorder access rules depending on the structure of the request body.

        Access rules can be updated by changing the properties of the access rule object with the rule's key specified in the key field. Access rules can be reordered by changing the order of the access rules in the list when updating.

        Access rules can be created by adding a new access rule object to the list without a `key` property specified. A `key` will be generated for the new access rule upon update.

        Any existing access rules that are not specified with a `key` in the list of access rules will be deleted upon update.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[AccessRule] access_rules: (required)

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/accessRules"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_access_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=access_rules)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=access_rules)

    def update_address_list(self, address_list_id, **kwargs):
        """
        Updates the details of an address list. Only the fields specified in the request body will be updated; all other properties will remain unchanged.


        :param str address_list_id: (required)
            The `OCID`__ of the address list. This number is generated when the address list is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param UpdateAddressListDetails update_address_list_details: (optional)
            The details of the address list to update.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.AddressList`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/addressLists/{addressListId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match",
            "update_address_list_details"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_address_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "addressListId": address_list_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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
                header_params=header_params,
                body=kwargs.get('update_address_list_details'),
                response_type="AddressList")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('update_address_list_details'),
                response_type="AddressList")

    def update_caching_rules(self, waas_policy_id, caching_rules_details, **kwargs):
        """
        Updates the configuration for each specified caching rule.

        Caching rules WAF policies allow you to selectively cache content on Oracle Cloud Infrastructure's edge servers, such as webpages or certain file types. For more information about caching rules, see `Caching Rules`__.

        This operation can create, delete, update, and/or reorder caching rules depending on the structure of the request body. Caching rules can be updated by changing the properties of the caching rule object with the rule's key specified in the key field. Any existing caching rules that are not specified with a key in the list of access rules will be deleted upon update.

        The order the caching rules are specified in is important. The rules are processed in the order they are specified and the first matching rule will be used when processing a request. Use `ListCachingRules` to view a list of all available caching rules in a compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/cachingrules.htm


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[CachingRule] caching_rules_details: (required)

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/cachingRules"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_caching_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=caching_rules_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=caching_rules_details)

    def update_captchas(self, waas_policy_id, captchas, **kwargs):
        """
        Updates the list of CAPTCHA challenges in the Web Application Firewall configuration for a WAAS policy.
        This operation can create, update, or delete CAPTCHAs depending on the structure of the request body.
        CAPTCHA challenges can be updated by changing the properties of the CAPTCHA object with the rule's key specified in the key field. CAPTCHA challenges can be reordered by changing the order of the CAPTCHA challenges in the list when updating.

        CAPTCHA challenges can be created by adding a new access rule object to the list without a `key` property specified. A `key` will be generated for the new CAPTCHA challenges upon update.

        Any existing CAPTCHA challenges that are not specified with a `key` in the list of CAPTCHA challenges will be deleted upon update.

        Query parameters are allowed in CAPTCHA URL.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[Captcha] captchas: (required)
            A list of CAPTCHA details.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/captchas"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_captchas got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=captchas)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=captchas)

    def update_certificate(self, certificate_id, **kwargs):
        """
        It is not possible to update a certificate, only create and delete. Therefore, this operation can only update the display name, freeform tags, and defined tags of a certificate.


        :param str certificate_id: (required)
            The `OCID`__ of the SSL certificate used in the WAAS policy. This number is generated when the certificate is added to the policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param UpdateCertificateDetails update_certificate_details: (optional)
            The new display name, freeform tags, and defined tags to apply to a certificate.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.Certificate`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/certificates/{certificateId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match",
            "update_certificate_details"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_certificate got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "certificateId": certificate_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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
                header_params=header_params,
                body=kwargs.get('update_certificate_details'),
                response_type="Certificate")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=kwargs.get('update_certificate_details'),
                response_type="Certificate")

    def update_custom_protection_rule(self, custom_protection_rule_id, update_custom_protection_rule_details, **kwargs):
        """
        Updates the configuration of a custom protection rule. Only the fields specified in the request body will be updated; all other properties will remain unchanged.


        :param str custom_protection_rule_id: (required)
            The `OCID`__ of the custom protection rule. This number is generated when the custom protection rule is added to the compartment.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.UpdateCustomProtectionRuleDetails update_custom_protection_rule_details: (required)
            The details of the custom protection rule to update.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.waas.models.CustomProtectionRule`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/customProtectionRules/{customProtectionRuleId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_custom_protection_rule got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "customProtectionRuleId": custom_protection_rule_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_custom_protection_rule_details,
                response_type="CustomProtectionRule")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_custom_protection_rule_details,
                response_type="CustomProtectionRule")

    def update_device_fingerprint_challenge(self, waas_policy_id, update_device_fingerprint_challenge_details, **kwargs):
        """
        Updates the Device Fingerprint Challenge (DFC) settings in the Web Application Firewall configuration for a policy. The DFC generates a hashed signature of both virtual and real browsers based on 50+ attributes. These proprietary signatures are then leveraged for real-time correlation to identify and block malicious bots.

        The signature is based on a library of attributes detected via JavaScript listeners; the attributes include OS, screen resolution, fonts, UserAgent, IP address, etc. We are constantly making improvements and considering new libraries to include in our DFC build. We can also exclude attributes from the signature as needed.

        DFC collects attributes to generate a hashed signature about a client - if a fingerprint is not possible, then it will result in a block or alert action. Actions can be enforced across multiple devices if they share they have the same fingerprint.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.DeviceFingerprintChallenge update_device_fingerprint_challenge_details: (required)
            The device fingerprint challenge settings to be updated.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/deviceFingerprintChallenge"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_device_fingerprint_challenge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_device_fingerprint_challenge_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_device_fingerprint_challenge_details)

    def update_good_bots(self, waas_policy_id, good_bots, **kwargs):
        """
        Updates the list of good bots in the Web Application Firewall configuration for a policy. Only the fields specified in the request body will be updated, all other configuration properties will remain unchanged.

        Good bots allows you to manage access for bots from known providers, such as Google or Baidu. For more information about good bots, see `Bot Management`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/botmanagement.htm


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[GoodBot] good_bots: (required)

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/goodBots"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_good_bots got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=good_bots)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=good_bots)

    def update_human_interaction_challenge(self, waas_policy_id, update_human_interaction_challenge_details, **kwargs):
        """
        Updates the Human Interaction Challenge (HIC) settings in the Web Application Firewall configuration for a WAAS policy. HIC is a countermeasure that allows the proxy to check the user's browser for various behaviors that distinguish a human presence from a bot.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.HumanInteractionChallenge update_human_interaction_challenge_details: (required)
            The human interaction challenge settings.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/humanInteractionChallenge"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_human_interaction_challenge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_human_interaction_challenge_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_human_interaction_challenge_details)

    def update_js_challenge(self, waas_policy_id, update_js_challenge_details, **kwargs):
        """
        Updates the JavaScript challenge settings in the Web Application Firewall configuration for a WAAS policy. JavaScript Challenge validates that the client can accept JavaScript with a binary decision. For more information, see `Bot Management`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/botmanagement.htm


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.JsChallenge update_js_challenge_details: (required)
            The JavaScript challenge settings to be updated.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/jsChallenge"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_js_challenge got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_js_challenge_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_js_challenge_details)

    def update_policy_config(self, waas_policy_id, update_policy_config_details, **kwargs):
        """
        Updates the configuration for a WAAS policy. Only the fields specified in the request body will be updated; all other properties will remain unchanged.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.PolicyConfig update_policy_config_details: (required)
            The new configuration to apply to a WAAS policy.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/policyConfig"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_policy_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_policy_config_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_policy_config_details)

    def update_protection_rules(self, waas_policy_id, protection_rules, **kwargs):
        """
        Updates the action for each specified protection rule. Requests can either be allowed, blocked, or trigger an alert if they meet the parameters of an applied rule. For more information on protection rules, see `WAF Protection Rules`__.
        This operation can update or disable protection rules depending on the structure of the request body.
        Protection rules can be updated by changing the properties of the protection rule object with the rule's key specified in the key field.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[ProtectionRuleAction] protection_rules: (required)

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/protectionRules"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_protection_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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
                header_params=header_params,
                body=protection_rules)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=protection_rules)

    def update_protection_settings(self, waas_policy_id, update_protection_settings_details, **kwargs):
        """
        Updates the protection settings in the Web Application Firewall configuration for a WAAS policy. Protection settings allow you define what action is taken when a request is blocked by the Web Application Firewall, such as returning a response code or block page. Only the fields specified in the request body will be updated; all other fields will remain unchanged.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.ProtectionSettings update_protection_settings_details: (required)
            The details of the protection settings to be updated.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/protectionSettings"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_protection_settings got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_protection_settings_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_protection_settings_details)

    def update_threat_feeds(self, waas_policy_id, threat_feeds, **kwargs):
        """
        Updates the action to take when a request's IP address matches an address in the specified threat intelligence feed. Threat intelligence feeds are compiled lists of IP addresses with malicious reputations based on internet intelligence. Only the threat feeds specified in the request body will be updated; all other threat feeds will remain unchanged.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[ThreatFeedAction] threat_feeds: (required)
            A list of threat feeds for which to update the actions.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/threatFeeds"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_threat_feeds got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "if-match": kwargs.get("if_match", missing)
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
                header_params=header_params,
                body=threat_feeds)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=threat_feeds)

    def update_waas_policy(self, waas_policy_id, update_waas_policy_details, **kwargs):
        """
        Updates the details of a WAAS policy, including origins and tags. Only the fields specified in the request body will be updated; all other properties will remain unchanged.
        To update platform provided resources such as `GoodBots`, `ProtectionRules`, and `ThreatFeeds`, first retrieve the list of available resources with the related list operation such as `GetThreatFeeds` or `GetProtectionRules`.
        The returned list will contain objects with `key` properties that can be used to update the resource during the `UpdateWaasPolicy` request.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.UpdateWaasPolicyDetails update_waas_policy_details: (required)
            The details of the WAAS policy to update.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_waas_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_waas_policy_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_waas_policy_details)

    def update_waas_policy_custom_protection_rules(self, waas_policy_id, update_custom_protection_rules_details, **kwargs):
        """
        Updates the action for each specified custom protection rule. Only the `DETECT` and `BLOCK` actions can be set. Disabled rules should not be included in the list. For more information on protection rules, see `WAF Protection Rules`__.

        __ https://docs.cloud.oracle.com/iaas/Content/WAF/Tasks/wafprotectionrules.htm


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[CustomProtectionRuleSetting] update_custom_protection_rules_details: (required)

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/customProtectionRules"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_waas_policy_custom_protection_rules got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_custom_protection_rules_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_custom_protection_rules_details)

    def update_waf_address_rate_limiting(self, waas_policy_id, update_waf_address_rate_limiting_details, **kwargs):
        """
        Updates the address rate limiting settings in the Web Application Firewall configuration for a policy. Rate limiting allows you to configure a threshold for the number of requests from a unique IP address for the given period. You can also define the response code for the requests from the same address that exceed the threshold.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.AddressRateLimiting update_waf_address_rate_limiting_details: (required)
            The address rate limiting settings.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/addressRateLimiting"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_waf_address_rate_limiting got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_waf_address_rate_limiting_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_waf_address_rate_limiting_details)

    def update_waf_config(self, waas_policy_id, update_waf_config_details, **kwargs):
        """
        Updates the Web Application Firewall configuration for a specified WAAS policy.

        To update platform provided resources such as `GoodBots`, `ProtectionRules`, and `ThreatFeeds`,
        first retrieve the list of available resources with the related list operation, such as
        `GetThreatFeeds` or `GetProtectionRules`.

        The returned list will contain objects with `key` properties that can be used to update the
        resource during the `UpdateWafConfig` request.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.WafConfig update_waf_config_details: (required)
            The new Web Application Firewall configuration to apply to a WAAS policy.

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_waf_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_waf_config_details)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_waf_config_details)

    def update_whitelists(self, waas_policy_id, whitelists, **kwargs):
        """
        Updates the list of IP addresses that bypass the Web Application Firewall for a WAAS policy. Supports single IP addresses, subnet masks (CIDR notation) and Address Lists.

        This operation can create, delete, update, and/or reorder whitelists depending on the structure of the request body.

        Whitelists can be updated by changing the properties of the whitelist object with the rule's key specified in the `key` field. Whitelists can be reordered by changing the order of the whitelists in the list of objects when updating.

        Whitelists can be created by adding a new whitelist object to the list without a `key` property specified. A `key` will be generated for the new whitelist upon update.

        Whitelists can be deleted by removing the existing whitelist object from the list. Any existing whitelists that are not specified with a `key` in the list of access rules will be deleted upon update.


        :param str waas_policy_id: (required)
            The `OCID`__ of the WAAS policy.

            __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm

        :param oci.waas.models.list[Whitelist] whitelists: (required)

        :param str opc_request_id: (optional)
            The unique Oracle-assigned identifier for the request. If you need to contact Oracle about a particular request, please provide the request ID.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or server error without risk of executing that same action again. Retry tokens expire after 24 hours, but can be invalidated before then due to conflicting operations
            *Example:* If a resource has been deleted and purged from the system, then a retry of the original delete request may be rejected.

        :param str if_match: (optional)
            For optimistic concurrency control. In the `PUT` or `DELETE` call for a resource, set the `if-match` parameter to the value of the etag from a previous `GET` or `POST` response for that resource. The resource will be updated or deleted only if the etag provided matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/waasPolicies/{waasPolicyId}/wafConfig/whitelists"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_request_id",
            "opc_retry_token",
            "if_match"
        ]
        extra_kwargs = [_key for _key in six.iterkeys(kwargs) if _key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_whitelists got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "waasPolicyId": waas_policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-request-id": kwargs.get("opc_request_id", missing),
            "opc-retry-token": kwargs.get("opc_retry_token", missing),
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing and v is not None}

        retry_strategy = self.retry_strategy
        if kwargs.get('retry_strategy'):
            retry_strategy = kwargs.get('retry_strategy')

        if retry_strategy:
            if not isinstance(retry_strategy, retry.NoneRetryStrategy):
                self.base_client.add_opc_retry_token_if_needed(header_params)
            return retry_strategy.make_retrying_call(
                self.base_client.call_api,
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=whitelists)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=whitelists)
