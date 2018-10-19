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
from .models import identity_type_mapping
missing = Sentinel("Missing")


class IdentityClient(object):
    """
    APIs for managing users, groups, compartments, and policies.
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
            'base_path': '/20160918',
            'skip_deserialization': kwargs.get('skip_deserialization', False)
        }
        self.base_client = BaseClient("identity", config, signer, identity_type_mapping, **base_client_init_kwargs)
        self.retry_strategy = kwargs.get('retry_strategy')

    def add_user_to_group(self, add_user_to_group_details, **kwargs):
        """
        AddUserToGroup
        Adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.

        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.


        :param AddUserToGroupDetails add_user_to_group_details: (required)
            Request object for adding a user to a group.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.UserGroupMembership`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/userGroupMemberships/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "add_user_to_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=add_user_to_group_details,
                response_type="UserGroupMembership")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=add_user_to_group_details,
                response_type="UserGroupMembership")

    def create_auth_token(self, create_auth_token_details, user_id, **kwargs):
        """
        CreateAuthToken
        Creates a new auth token for the specified user. For information about what auth tokens are for, see
        `Managing User Credentials`__.

        You must specify a *description* for the auth token (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with
        :func:`update_auth_token`.

        Every user has permission to create an auth token for *their own user ID*. An administrator in your organization
        does not need to write a policy to give users this ability. To compare, administrators who have permission to the
        tenancy can use this operation to create an auth token for any user, including themselves.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingcredentials.htm


        :param CreateAuthTokenDetails create_auth_token_details: (required)
            Request object for creating a new auth token.

        :param str user_id: (required)
            The OCID of the user.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.AuthToken`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/authTokens/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_auth_token got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_auth_token_details,
                response_type="AuthToken")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_auth_token_details,
                response_type="AuthToken")

    def create_compartment(self, create_compartment_details, **kwargs):
        """
        CreateCompartment
        Creates a new compartment in the specified compartment.

        **Important:** Compartments cannot be deleted.

        Specify the parent compartment's OCID as the compartment ID in the request object. Remember that the tenancy
        is simply the root compartment. For information about OCIDs, see
        `Resource Identifiers`__.

        You must also specify a *name* for the compartment, which must be unique across all compartments in
        your tenancy. You can use this name or the OCID when writing policies that apply
        to the compartment. For more information about policies, see
        `How Policies Work`__.

        You must also specify a *description* for the compartment (although it can be an empty string). It does
        not have to be unique, and you can change it anytime with
        :func:`update_compartment`.

        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm


        :param CreateCompartmentDetails create_compartment_details: (required)
            Request object for creating a new compartment.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Compartment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/compartments/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_compartment_details,
                response_type="Compartment")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_compartment_details,
                response_type="Compartment")

    def create_customer_secret_key(self, create_customer_secret_key_details, user_id, **kwargs):
        """
        CreateCustomerSecretKey
        Creates a new secret key for the specified user. Secret keys are used for authentication with the Object Storage Service's Amazon S3
        compatible API. For information, see
        `Managing User Credentials`__.

        You must specify a *description* for the secret key (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with
        :func:`update_customer_secret_key`.

        Every user has permission to create a secret key for *their own user ID*. An administrator in your organization
        does not need to write a policy to give users this ability. To compare, administrators who have permission to the
        tenancy can use this operation to create a secret key for any user, including themselves.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingcredentials.htm


        :param CreateCustomerSecretKeyDetails create_customer_secret_key_details: (required)
            Request object for creating a new secret key.

        :param str user_id: (required)
            The OCID of the user.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.CustomerSecretKey`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/customerSecretKeys/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_customer_secret_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_customer_secret_key_details,
                response_type="CustomerSecretKey")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_customer_secret_key_details,
                response_type="CustomerSecretKey")

    def create_dynamic_group(self, create_dynamic_group_details, **kwargs):
        """
        CreateDynamicGroup
        Creates a new dynamic group in your tenancy.

        You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy
        is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies)
        reside within the tenancy itself, unlike cloud resources such as compute instances, which typically
        reside within compartments inside the tenancy. For information about OCIDs, see
        `Resource Identifiers`__.

        You must also specify a *name* for the dynamic group, which must be unique across all dynamic groups in your
        tenancy, and cannot be changed. Note that this name has to be also unique accross all groups in your tenancy.
        You can use this name or the OCID when writing policies that apply to the dynamic group. For more information
        about policies, see `How Policies Work`__.

        You must also specify a *description* for the dynamic group (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with :func:`update_dynamic_group`.

        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm


        :param CreateDynamicGroupDetails create_dynamic_group_details: (required)
            Request object for creating a new dynamic group.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.DynamicGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dynamicGroups/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_dynamic_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_dynamic_group_details,
                response_type="DynamicGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_dynamic_group_details,
                response_type="DynamicGroup")

    def create_group(self, create_group_details, **kwargs):
        """
        CreateGroup
        Creates a new group in your tenancy.

        You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy
        is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies)
        reside within the tenancy itself, unlike cloud resources such as compute instances, which typically
        reside within compartments inside the tenancy. For information about OCIDs, see
        `Resource Identifiers`__.

        You must also specify a *name* for the group, which must be unique across all groups in your tenancy and
        cannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more
        information about policies, see `How Policies Work`__.

        You must also specify a *description* for the group (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with :func:`update_group`.

        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.

        After creating the group, you need to put users in it and write policies for it.
        See :func:`add_user_to_group` and
        :func:`create_policy`.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm


        :param CreateGroupDetails create_group_details: (required)
            Request object for creating a new group.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Group`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/groups/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_group_details,
                response_type="Group")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_group_details,
                response_type="Group")

    def create_identity_provider(self, create_identity_provider_details, **kwargs):
        """
        CreateIdentityProvider
        Creates a new identity provider in your tenancy. For more information, see
        `Identity Providers and Federation`__.

        You must specify your tenancy's OCID as the compartment ID in the request object.
        Remember that the tenancy is simply the root compartment. For information about
        OCIDs, see `Resource Identifiers`__.

        You must also specify a *name* for the `IdentityProvider`, which must be unique
        across all `IdentityProvider` objects in your tenancy and cannot be changed.

        You must also specify a *description* for the `IdentityProvider` (although
        it can be an empty string). It does not have to be unique, and you can change
        it anytime with
        :func:`update_identity_provider`.

        After you send your request, the new object's `lifecycleState` will temporarily
        be CREATING. Before using the object, first make sure its `lifecycleState` has
        changed to ACTIVE.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/federation.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateIdentityProviderDetails create_identity_provider_details: (required)
            Request object for creating a new SAML2 identity provider.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.IdentityProvider`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_identity_provider got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_identity_provider_details,
                response_type="IdentityProvider")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_identity_provider_details,
                response_type="IdentityProvider")

    def create_idp_group_mapping(self, create_idp_group_mapping_details, identity_provider_id, **kwargs):
        """
        CreateIdpGroupMapping
        Creates a single mapping between an IdP group and an IAM Service
        :class:`Group`.


        :param CreateIdpGroupMappingDetails create_idp_group_mapping_details: (required)
            Add a mapping from an SAML2.0 identity provider group to a BMC group.

        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.IdpGroupMapping`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}/groupMappings/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_idp_group_mapping got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_idp_group_mapping_details,
                response_type="IdpGroupMapping")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_idp_group_mapping_details,
                response_type="IdpGroupMapping")

    def create_or_reset_ui_password(self, user_id, **kwargs):
        """
        CreateOrResetUIPassword
        Creates a new Console one-time password for the specified user. For more information about user
        credentials, see `User Credentials`__.

        Use this operation after creating a new user, or if a user forgets their password. The new one-time
        password is returned to you in the response, and you must securely deliver it to the user. They'll
        be prompted to change this password the next time they sign in to the Console. If they don't change
        it within 7 days, the password will expire and you'll need to create a new one-time password for the
        user.

        **Note:** The user's Console login is the unique name you specified when you created the user
        (see :func:`create_user`).

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/usercredentials.htm


        :param str user_id: (required)
            The OCID of the user.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.UIPassword`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/uiPassword"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_or_reset_ui_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                response_type="UIPassword")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="UIPassword")

    def create_policy(self, create_policy_details, **kwargs):
        """
        CreatePolicy
        Creates a new policy in the specified compartment (either the tenancy or another of your compartments).
        If you're new to policies, see `Getting Started with Policies`__.

        You must specify a *name* for the policy, which must be unique across all policies in your tenancy
        and cannot be changed.

        You must also specify a *description* for the policy (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with :func:`update_policy`.

        You must specify one or more policy statements in the statements array. For information about writing
        policies, see `How Policies Work`__ and
        `Common Policies`__.

        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
        object, first make sure its `lifecycleState` has changed to ACTIVE.

        New policies take effect typically within 10 seconds.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policies.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/commonpolicies.htm


        :param CreatePolicyDetails create_policy_details: (required)
            Request object for creating a new policy.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Policy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/policies/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_policy got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_policy_details,
                response_type="Policy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_policy_details,
                response_type="Policy")

    def create_region_subscription(self, create_region_subscription_details, tenancy_id, **kwargs):
        """
        CreateRegionSubscription
        Creates a subscription to a region for a tenancy.


        :param CreateRegionSubscriptionDetails create_region_subscription_details: (required)
            Request object for activate a new region.

        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.RegionSubscription`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tenancies/{tenancyId}/regionSubscriptions"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_region_subscription got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tenancyId": tenancy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_region_subscription_details,
                response_type="RegionSubscription")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_region_subscription_details,
                response_type="RegionSubscription")

    def create_smtp_credential(self, create_smtp_credential_details, user_id, **kwargs):
        """
        CreateSmtpCredential
        Creates a new SMTP credential for the specified user. An SMTP credential has an SMTP user name and an SMTP password.
        You must specify a *description* for the SMTP credential (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with
        :func:`update_smtp_credential`.


        :param CreateSmtpCredentialDetails create_smtp_credential_details: (required)
            Request object for creating a new SMTP credential with the user.

        :param str user_id: (required)
            The OCID of the user.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.SmtpCredential`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/smtpCredentials/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_smtp_credential got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_smtp_credential_details,
                response_type="SmtpCredential")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_smtp_credential_details,
                response_type="SmtpCredential")

    def create_swift_password(self, create_swift_password_details, user_id, **kwargs):
        """
        CreateSwiftPassword
        **Deprecated. Use :func:`create_auth_token` instead.**

        Creates a new Swift password for the specified user. For information about what Swift passwords are for, see
        `Managing User Credentials`__.

        You must specify a *description* for the Swift password (although it can be an empty string). It does not
        have to be unique, and you can change it anytime with
        :func:`update_swift_password`.

        Every user has permission to create a Swift password for *their own user ID*. An administrator in your organization
        does not need to write a policy to give users this ability. To compare, administrators who have permission to the
        tenancy can use this operation to create a Swift password for any user, including themselves.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingcredentials.htm


        :param CreateSwiftPasswordDetails create_swift_password_details: (required)
            Request object for creating a new swift password.

        :param str user_id: (required)
            The OCID of the user.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.SwiftPassword`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/swiftPasswords/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_swift_password_details,
                response_type="SwiftPassword")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_swift_password_details,
                response_type="SwiftPassword")

    def create_tag(self, tag_namespace_id, create_tag_details, **kwargs):
        """
        CreateTag
        Creates a new tag in the specified tag namespace.

        You must specify either the OCID or the name of the tag namespace that will contain this tag definition.

        You must also specify a *name* for the tag, which must be unique across all tags in the tag namespace
        and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters.
        Names are case insensitive. That means, for example, \"myTag\" and \"mytag\" are not allowed in the same namespace.
        If you specify a name that's already in use in the tag namespace, a 409 error is returned.

        You must also specify a *description* for the tag.
        It does not have to be unique, and you can change it with
        :func:`update_tag`.


        :param str tag_namespace_id: (required)
            The OCID of the tag namespace.

        :param CreateTagDetails create_tag_details: (required)
            Request object for creating a new tag in the specified tag namespace.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Tag`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces/{tagNamespaceId}/tags"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_tag got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tagNamespaceId": tag_namespace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_tag_details,
                response_type="Tag")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_tag_details,
                response_type="Tag")

    def create_tag_namespace(self, create_tag_namespace_details, **kwargs):
        """
        CreateTagNamespace
        Creates a new tag namespace in the specified compartment.

        You must specify the compartment ID in the request object (remember that the tenancy is simply the root
        compartment).

        You must also specify a *name* for the namespace, which must be unique across all namespaces in your tenancy
        and cannot be changed. The name can contain any ASCII character except the space (_) or period (.).
        Names are case insensitive. That means, for example, \"myNamespace\" and \"mynamespace\" are not allowed
        in the same tenancy. Once you created a namespace, you cannot change the name.
        If you specify a name that's already in use in the tenancy, a 409 error is returned.

        You must also specify a *description* for the namespace.
        It does not have to be unique, and you can change it with
        :func:`update_tag_namespace`.

        Tag namespaces cannot be deleted, but they can be retired.
        See `Retiring Key Definitions and Namespace Definitions`__ for more information.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :param CreateTagNamespaceDetails create_tag_namespace_details: (required)
            Request object for creating a new tag namespace.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.TagNamespace`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_tag_namespace got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_tag_namespace_details,
                response_type="TagNamespace")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_tag_namespace_details,
                response_type="TagNamespace")

    def create_user(self, create_user_details, **kwargs):
        """
        CreateUser
        Creates a new user in your tenancy. For conceptual information about users, your tenancy, and other
        IAM Service components, see `Overview of the IAM Service`__.

        You must specify your tenancy's OCID as the compartment ID in the request object (remember that the
        tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and
        some policies) reside within the tenancy itself, unlike cloud resources such as compute instances,
        which typically reside within compartments inside the tenancy. For information about OCIDs, see
        `Resource Identifiers`__.

        You must also specify a *name* for the user, which must be unique across all users in your tenancy
        and cannot be changed. Allowed characters: No spaces. Only letters, numerals, hyphens, periods,
        underscores, +, and @. If you specify a name that's already in use, you'll get a 409 error.
        This name will be the user's login to the Console. You might want to pick a
        name that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses.
        If you delete a user and then create a new user with the same name, they'll be considered different
        users because they have different OCIDs.

        You must also specify a *description* for the user (although it can be an empty string).
        It does not have to be unique, and you can change it anytime with
        :func:`update_user`. You can use the field to provide the user's
        full name, a description, a nickname, or other information to generally identify the user.

        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before
        using the object, first make sure its `lifecycleState` has changed to ACTIVE.

        A new user has no permissions until you place the user in one or more groups (see
        :func:`add_user_to_group`). If the user needs to
        access the Console, you need to provide the user a password (see
        :func:`create_or_reset_ui_password`).
        If the user needs to access the Oracle Cloud Infrastructure REST API, you need to upload a
        public API signing key for that user (see
        `Required Keys and OCIDs`__ and also
        :func:`upload_api_key`).

        **Important:** Make sure to inform the new user which compartment(s) they have access to.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm


        :param CreateUserDetails create_user_details: (required)
            Request object for creating a new user.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.User`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_user got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_user_details,
                response_type="User")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                body=create_user_details,
                response_type="User")

    def delete_api_key(self, user_id, fingerprint, **kwargs):
        """
        DeleteApiKey
        Deletes the specified API signing key for the specified user.

        Every user has permission to use this operation to delete a key for *their own user ID*. An
        administrator in your organization does not need to write a policy to give users this ability.
        To compare, administrators who have permission to the tenancy can use this operation to delete
        a key for any user, including themselves.


        :param str user_id: (required)
            The OCID of the user.

        :param str fingerprint: (required)
            The key's fingerprint.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/apiKeys/{fingerprint}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_api_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "fingerprint": fingerprint
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_auth_token(self, user_id, auth_token_id, **kwargs):
        """
        DeleteAuthToken
        Deletes the specified auth token for the specified user.


        :param str user_id: (required)
            The OCID of the user.

        :param str auth_token_id: (required)
            The OCID of the auth token.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/authTokens/{authTokenId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_auth_token got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "authTokenId": auth_token_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_compartment(self, compartment_id, **kwargs):
        """
        DeleteCompartment
        Deletes the specified compartment. The compartment must be empty.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/compartments/{compartmentId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "compartmentId": compartment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_customer_secret_key(self, user_id, customer_secret_key_id, **kwargs):
        """
        DeleteCustomerSecretKey
        Deletes the specified secret key for the specified user.


        :param str user_id: (required)
            The OCID of the user.

        :param str customer_secret_key_id: (required)
            The OCID of the secret key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/customerSecretKeys/{customerSecretKeyId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_customer_secret_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "customerSecretKeyId": customer_secret_key_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_dynamic_group(self, dynamic_group_id, **kwargs):
        """
        DeleteDynamicGroup
        Deletes the specified dynamic group.


        :param str dynamic_group_id: (required)
            The OCID of the dynamic group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dynamicGroups/{dynamicGroupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_dynamic_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dynamicGroupId": dynamic_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_group(self, group_id, **kwargs):
        """
        DeleteGroup
        Deletes the specified group. The group must be empty.


        :param str group_id: (required)
            The OCID of the group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/groups/{groupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_identity_provider(self, identity_provider_id, **kwargs):
        """
        DeleteIdentityProvider
        Deletes the specified identity provider. The identity provider must not have
        any group mappings (see :class:`IdpGroupMapping`).


        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_identity_provider got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_idp_group_mapping(self, identity_provider_id, mapping_id, **kwargs):
        """
        DeleteIdpGroupMapping
        Deletes the specified group mapping.


        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param str mapping_id: (required)
            The OCID of the group mapping.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}/groupMappings/{mappingId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_idp_group_mapping got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id,
            "mappingId": mapping_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_policy(self, policy_id, **kwargs):
        """
        DeletePolicy
        Deletes the specified policy. The deletion takes effect typically within 10 seconds.


        :param str policy_id: (required)
            The OCID of the policy.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/policies/{policyId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_smtp_credential(self, user_id, smtp_credential_id, **kwargs):
        """
        DeleteSmtpCredential
        Deletes the specified SMTP credential for the specified user.


        :param str user_id: (required)
            The OCID of the user.

        :param str smtp_credential_id: (required)
            The OCID of the SMTP credential.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/smtpCredentials/{smtpCredentialId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_smtp_credential got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "smtpCredentialId": smtp_credential_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_swift_password(self, user_id, swift_password_id, **kwargs):
        """
        DeleteSwiftPassword
        **Deprecated. Use :func:`delete_auth_token` instead.**

        Deletes the specified Swift password for the specified user.


        :param str user_id: (required)
            The OCID of the user.

        :param str swift_password_id: (required)
            The OCID of the Swift password.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/swiftPasswords/{swiftPasswordId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "swiftPasswordId": swift_password_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def delete_user(self, user_id, **kwargs):
        """
        DeleteUser
        Deletes the specified user. The user must not be in any groups.


        :param str user_id: (required)
            The OCID of the user.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def get_compartment(self, compartment_id, **kwargs):
        """
        GetCompartment
        Gets the specified compartment's information.

        This operation does not return a list of all the resources inside the compartment. There is no single
        API operation that does that. Compartments can contain multiple types of resources (instances, block
        storage volumes, etc.). To find out what's in a compartment, you must call the \"List\" operation for
        each resource type and specify the compartment's OCID as a query parameter in the request. For example,
        call the :func:`list_instances` operation in the Cloud Compute
        Service or the :func:`list_volumes` operation in Cloud Block Storage.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Compartment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/compartments/{compartmentId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "compartmentId": compartment_id
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
                response_type="Compartment")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Compartment")

    def get_dynamic_group(self, dynamic_group_id, **kwargs):
        """
        GetDynamicGroup
        Gets the specified dynamic group's information.


        :param str dynamic_group_id: (required)
            The OCID of the dynamic group.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.DynamicGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dynamicGroups/{dynamicGroupId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_dynamic_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dynamicGroupId": dynamic_group_id
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
                response_type="DynamicGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="DynamicGroup")

    def get_group(self, group_id, **kwargs):
        """
        GetGroup
        Gets the specified group's information.

        This operation does not return a list of all the users in the group. To do that, use
        :func:`list_user_group_memberships` and
        provide the group's OCID as a query parameter in the request.


        :param str group_id: (required)
            The OCID of the group.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Group`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/groups/{groupId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
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
                response_type="Group")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Group")

    def get_identity_provider(self, identity_provider_id, **kwargs):
        """
        GetIdentityProvider
        Gets the specified identity provider's information.


        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.IdentityProvider`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_identity_provider got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id
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
                response_type="IdentityProvider")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IdentityProvider")

    def get_idp_group_mapping(self, identity_provider_id, mapping_id, **kwargs):
        """
        GetIdpGroupMapping
        Gets the specified group mapping.


        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param str mapping_id: (required)
            The OCID of the group mapping.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.IdpGroupMapping`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}/groupMappings/{mappingId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_idp_group_mapping got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id,
            "mappingId": mapping_id
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
                response_type="IdpGroupMapping")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="IdpGroupMapping")

    def get_policy(self, policy_id, **kwargs):
        """
        GetPolicy
        Gets the specified policy's information.


        :param str policy_id: (required)
            The OCID of the policy.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Policy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/policies/{policyId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
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
                response_type="Policy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Policy")

    def get_tag(self, tag_namespace_id, tag_name, **kwargs):
        """
        GetTag
        Gets the specified tag's information.


        :param str tag_namespace_id: (required)
            The OCID of the tag namespace.

        :param str tag_name: (required)
            The name of the tag.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Tag`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces/{tagNamespaceId}/tags/{tagName}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_tag got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tagNamespaceId": tag_namespace_id,
            "tagName": tag_name
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
                response_type="Tag")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Tag")

    def get_tag_namespace(self, tag_namespace_id, **kwargs):
        """
        GetTagNamespace
        Gets the specified tag namespace's information.


        :param str tag_namespace_id: (required)
            The OCID of the tag namespace.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.TagNamespace`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces/{tagNamespaceId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_tag_namespace got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tagNamespaceId": tag_namespace_id
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
                response_type="TagNamespace")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="TagNamespace")

    def get_tenancy(self, tenancy_id, **kwargs):
        """
        GetTenancy
        Get the specified tenancy's information.


        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Tenancy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tenancies/{tenancyId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_tenancy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tenancyId": tenancy_id
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
                response_type="Tenancy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="Tenancy")

    def get_user(self, user_id, **kwargs):
        """
        GetUser
        Gets the specified user's information.


        :param str user_id: (required)
            The OCID of the user.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.User`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
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
                response_type="User")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="User")

    def get_user_group_membership(self, user_group_membership_id, **kwargs):
        """
        GetUserGroupMembership
        Gets the specified UserGroupMembership's information.


        :param str user_group_membership_id: (required)
            The OCID of the userGroupMembership.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.UserGroupMembership`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/userGroupMemberships/{userGroupMembershipId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "get_user_group_membership got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userGroupMembershipId": user_group_membership_id
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
                response_type="UserGroupMembership")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="UserGroupMembership")

    def get_work_request(self, work_request_id, **kwargs):
        """
        GetWorkRequest
        Gets details on a specified work request. The workRequestID is returned in the opc-workrequest-id header
        for any asynchronous operation in the Identity and Access Management service.


        :param str work_request_id: (required)
            The OCID of the work request.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.WorkRequest`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/{workRequestId}"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
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
                response_type="WorkRequest")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="WorkRequest")

    def list_api_keys(self, user_id, **kwargs):
        """
        ListApiKeys
        Lists the API signing keys for the specified user. A user can have a maximum of three keys.

        Every user has permission to use this API call for *their own user ID*.  An administrator in your
        organization does not need to write a policy to give users this ability.


        :param str user_id: (required)
            The OCID of the user.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.ApiKey`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/apiKeys/"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_api_keys got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
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
                response_type="list[ApiKey]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="list[ApiKey]")

    def list_auth_tokens(self, user_id, **kwargs):
        """
        ListAuthTokens
        Lists the auth tokens for the specified user. The returned object contains the token's OCID, but not
        the token itself. The actual token is returned only upon creation.


        :param str user_id: (required)
            The OCID of the user.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.AuthToken`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/authTokens/"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_auth_tokens got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
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
                response_type="list[AuthToken]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="list[AuthToken]")

    def list_availability_domains(self, compartment_id, **kwargs):
        """
        ListAvailabilityDomains
        Lists the availability domains in your tenancy. Specify the OCID of either the tenancy or another
        of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment).
        See `Where to Get the Tenancy's OCID and User's OCID`__.
        Note that the order of the results returned can change if availability domains are added or removed; therefore, do not
        create a dependency on the list order.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.AvailabilityDomain`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/availabilityDomains/"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_availability_domains got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id
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
                response_type="list[AvailabilityDomain]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[AvailabilityDomain]")

    def list_compartments(self, compartment_id, **kwargs):
        """
        ListCompartments
        Lists the compartments in a specified compartment. The members of the list
        returned depends on the values set for several parameters.

        With the exception of the tenancy (root compartment), the ListCompartments operation
        returns only the first-level child compartments in the parent compartment specified in
        `compartmentId`. The list does not include any subcompartments of the child
        compartments (grandchildren).

        The parameter `accessLevel` specifies whether to return only those compartments for which the
        requestor has INSPECT permissions on at least one resource directly
        or indirectly (the resource can be in a subcompartment).

        The parameter `compartmentIdInSubtree` applies only when you perform ListCompartments on the
        tenancy (root compartment). When set to true, the entire hierarchy of compartments can be returned.
        To get a full list of all compartments and subcompartments in the tenancy (root compartment),
        set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ANY.

        See `Where to Get the Tenancy's OCID and User's OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str access_level: (optional)
            Valid values are `ANY` and `ACCESSIBLE`. Default is `ANY`.
            Setting this to `ACCESSIBLE` returns only those compartments for which the
            user has INSPECT permissions directly or indirectly (permissions can be on a
            resource in a subcompartment). For the compartments on which the user indirectly has
            INSPECT permissions, a restricted set of fields is returned.

            When set to `ANY` permissions are not checked.

            Allowed values are: "ANY", "ACCESSIBLE"

        :param bool compartment_id_in_subtree: (optional)
            Default is false. Can only be set to true when performing
            ListCompartments on the tenancy (root compartment).
            When set to true, the hierarchy of compartments is traversed
            and all compartments and subcompartments in the tenancy are
            returned depending on the the setting of `accessLevel`.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.Compartment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/compartments/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit",
            "access_level",
            "compartment_id_in_subtree"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_compartments got unknown kwargs: {!r}".format(extra_kwargs))

        if 'access_level' in kwargs:
            access_level_allowed_values = ["ANY", "ACCESSIBLE"]
            if kwargs['access_level'] not in access_level_allowed_values:
                raise ValueError(
                    "Invalid value for `access_level`, must be one of {0}".format(access_level_allowed_values)
                )

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "accessLevel": kwargs.get("access_level", missing),
            "compartmentIdInSubtree": kwargs.get("compartment_id_in_subtree", missing)
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
                response_type="list[Compartment]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Compartment]")

    def list_cost_tracking_tags(self, compartment_id, **kwargs):
        """
        ListCostTrackingTags
        Lists all the tags enabled for cost-tracking in the specified tenancy. For information about
        cost-tracking tags, see `Using Cost-tracking Tags`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#costs


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.Tag`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces/actions/listCostTrackingTags"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cost_tracking_tags got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="list[Tag]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Tag]")

    def list_customer_secret_keys(self, user_id, **kwargs):
        """
        ListCustomerSecretKeys
        Lists the secret keys for the specified user. The returned object contains the secret key's OCID, but not
        the secret key itself. The actual secret key is returned only upon creation.


        :param str user_id: (required)
            The OCID of the user.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.CustomerSecretKeySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/customerSecretKeys/"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_customer_secret_keys got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
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
                response_type="list[CustomerSecretKeySummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="list[CustomerSecretKeySummary]")

    def list_dynamic_groups(self, compartment_id, **kwargs):
        """
        ListDynamicGroups
        Lists the dynamic groups in your tenancy. You must specify your tenancy's OCID as the value for
        the compartment ID (remember that the tenancy is simply the root compartment).
        See `Where to Get the Tenancy's OCID and User's OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.DynamicGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dynamicGroups/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_dynamic_groups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="list[DynamicGroup]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[DynamicGroup]")

    def list_fault_domains(self, compartment_id, availability_domain, **kwargs):
        """
        ListFaultDomains
        Lists the Fault Domains in your tenancy. Specify the OCID of either the tenancy or another
        of your compartments as the value for the compartment ID (remember that the tenancy is simply the root compartment).
        See `Where to Get the Tenancy's OCID and User's OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str availability_domain: (required)
            The name of the availibilityDomain.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.FaultDomain`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/faultDomains/"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_fault_domains got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "availabilityDomain": availability_domain
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
                response_type="list[FaultDomain]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[FaultDomain]")

    def list_groups(self, compartment_id, **kwargs):
        """
        ListGroups
        Lists the groups in your tenancy. You must specify your tenancy's OCID as the value for
        the compartment ID (remember that the tenancy is simply the root compartment).
        See `Where to Get the Tenancy's OCID and User's OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.Group`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/groups/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_groups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="list[Group]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Group]")

    def list_identity_providers(self, protocol, compartment_id, **kwargs):
        """
        ListIdentityProviders
        Lists all the identity providers in your tenancy. You must specify the identity provider type (e.g., `SAML2` for
        identity providers using the SAML2.0 protocol). You must specify your tenancy's OCID as the value for the
        compartment ID (remember that the tenancy is simply the root compartment).
        See `Where to Get the Tenancy's OCID and User's OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str protocol: (required)
            The protocol used for federation.

            Allowed values are: "SAML2"

        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.IdentityProvider`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_identity_providers got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "protocol": protocol,
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="list[IdentityProvider]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[IdentityProvider]")

    def list_idp_group_mappings(self, identity_provider_id, **kwargs):
        """
        ListIdpGroupMappings
        Lists the group mappings for the specified identity provider.


        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.IdpGroupMapping`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}/groupMappings/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_idp_group_mappings got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[IdpGroupMapping]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[IdpGroupMapping]")

    def list_policies(self, compartment_id, **kwargs):
        """
        ListPolicies
        Lists the policies in the specified compartment (either the tenancy or another of your compartments).
        See `Where to Get the Tenancy's OCID and User's OCID`__.

        To determine which policies apply to a particular group or compartment, you must view the individual
        statements inside all your policies. There isn't a way to automatically obtain that information via the API.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.Policy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/policies/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_policies got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="list[Policy]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[Policy]")

    def list_region_subscriptions(self, tenancy_id, **kwargs):
        """
        ListRegionSubscriptions
        Lists the region subscriptions for the specified tenancy.


        :param str tenancy_id: (required)
            The OCID of the tenancy.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.RegionSubscription`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tenancies/{tenancyId}/regionSubscriptions"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_region_subscriptions got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tenancyId": tenancy_id
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
                response_type="list[RegionSubscription]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="list[RegionSubscription]")

    def list_regions(self, **kwargs):
        """
        ListRegions
        Lists all the regions offered by Oracle Cloud Infrastructure.


        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.Region`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/regions"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_regions got unknown kwargs: {!r}".format(extra_kwargs))

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
                response_type="list[Region]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                header_params=header_params,
                response_type="list[Region]")

    def list_smtp_credentials(self, user_id, **kwargs):
        """
        ListSmtpCredentials
        Lists the SMTP credentials for the specified user. The returned object contains the credential's OCID,
        the SMTP user name but not the SMTP password. The SMTP password is returned only upon creation.


        :param str user_id: (required)
            The OCID of the user.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.SmtpCredentialSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/smtpCredentials/"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_smtp_credentials got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
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
                response_type="list[SmtpCredentialSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="list[SmtpCredentialSummary]")

    def list_swift_passwords(self, user_id, **kwargs):
        """
        ListSwiftPasswords
        **Deprecated. Use :func:`list_auth_tokens` instead.**

        Lists the Swift passwords for the specified user. The returned object contains the password's OCID, but not
        the password itself. The actual password is returned only upon creation.


        :param str user_id: (required)
            The OCID of the user.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.SwiftPassword`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/swiftPasswords/"
        method = "GET"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_swift_passwords got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
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
                response_type="list[SwiftPassword]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                response_type="list[SwiftPassword]")

    def list_tag_namespaces(self, compartment_id, **kwargs):
        """
        ListTagNamespaces
        Lists the tag namespaces in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param bool include_subcompartments: (optional)
            An optional boolean parameter indicating whether to retrieve all tag namespaces in subcompartments. If this
            parameter is not specified, only the tag namespaces defined in the specified compartment are retrieved.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.TagNamespaceSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit",
            "include_subcompartments"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_tag_namespaces got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "includeSubcompartments": kwargs.get("include_subcompartments", missing)
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
                response_type="list[TagNamespaceSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[TagNamespaceSummary]")

    def list_tags(self, tag_namespace_id, **kwargs):
        """
        ListTags
        Lists the tag definitions in the specified tag namespace.


        :param str tag_namespace_id: (required)
            The OCID of the tag namespace.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.TagSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces/{tagNamespaceId}/tags"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_tags got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tagNamespaceId": tag_namespace_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        query_params = {
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[TagSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                query_params=query_params,
                header_params=header_params,
                response_type="list[TagSummary]")

    def list_user_group_memberships(self, compartment_id, **kwargs):
        """
        ListUserGroupMemberships
        Lists the `UserGroupMembership` objects in your tenancy. You must specify your tenancy's OCID
        as the value for the compartment ID
        (see `Where to Get the Tenancy's OCID and User's OCID`__).
        You must also then filter the list in one of these ways:

        - You can limit the results to just the memberships for a given user by specifying a `userId`.
        - Similarly, you can limit the results to just the memberships for a given group by specifying a `groupId`.
        - You can set both the `userId` and `groupId` to determine if the specified user is in the specified group.
        If the answer is no, the response is an empty list.
        - Although`userId` and `groupId` are not indvidually required, you must set one of them.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str user_id: (optional)
            The OCID of the user.

        :param str group_id: (optional)
            The OCID of the group.

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.UserGroupMembership`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/userGroupMemberships/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "user_id",
            "group_id",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_user_group_memberships got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "userId": kwargs.get("user_id", missing),
            "groupId": kwargs.get("group_id", missing),
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="list[UserGroupMembership]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[UserGroupMembership]")

    def list_users(self, compartment_id, **kwargs):
        """
        ListUsers
        Lists the users in your tenancy. You must specify your tenancy's OCID as the value for the
        compartment ID (remember that the tenancy is simply the root compartment).
        See `Where to Get the Tenancy's OCID and User's OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm#five


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.User`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_users got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing)
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
                response_type="list[User]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[User]")

    def list_work_requests(self, compartment_id, **kwargs):
        """
        ListWorkRequests
        Lists the work requests in compartment.


        :param str compartment_id: (required)
            The OCID of the parent compartment (remember that the tenancy is simply the root compartment).

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

        :param str resource_identifier: (optional)
            The identifier of the resource the work request affects.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type list of :class:`~oci.identity.models.WorkRequestSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/workRequests/"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "page",
            "limit",
            "resource_identifier"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_work_requests got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "page": kwargs.get("page", missing),
            "limit": kwargs.get("limit", missing),
            "resourceIdentifier": kwargs.get("resource_identifier", missing)
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
                response_type="list[WorkRequestSummary]")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                query_params=query_params,
                header_params=header_params,
                response_type="list[WorkRequestSummary]")

    def remove_user_from_group(self, user_group_membership_id, **kwargs):
        """
        RemoveUserFromGroup
        Removes a user from a group by deleting the corresponding `UserGroupMembership`.


        :param str user_group_membership_id: (required)
            The OCID of the userGroupMembership.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type None
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/userGroupMemberships/{userGroupMembershipId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "remove_user_from_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userGroupMembershipId": user_group_membership_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                header_params=header_params)
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params)

    def update_auth_token(self, user_id, auth_token_id, update_auth_token_details, **kwargs):
        """
        UpdateAuthToken
        Updates the specified auth token's description.


        :param str user_id: (required)
            The OCID of the user.

        :param str auth_token_id: (required)
            The OCID of the auth token.

        :param UpdateAuthTokenDetails update_auth_token_details: (required)
            Request object for updating an auth token.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.AuthToken`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/authTokens/{authTokenId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_auth_token got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "authTokenId": auth_token_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_auth_token_details,
                response_type="AuthToken")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_auth_token_details,
                response_type="AuthToken")

    def update_compartment(self, compartment_id, update_compartment_details, **kwargs):
        """
        UpdateCompartment
        Updates the specified compartment's description or name. You can't update the root compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param UpdateCompartmentDetails update_compartment_details: (required)
            Request object for updating a compartment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Compartment`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/compartments/{compartmentId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_compartment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "compartmentId": compartment_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_compartment_details,
                response_type="Compartment")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_compartment_details,
                response_type="Compartment")

    def update_customer_secret_key(self, user_id, customer_secret_key_id, update_customer_secret_key_details, **kwargs):
        """
        UpdateCustomerSecretKey
        Updates the specified secret key's description.


        :param str user_id: (required)
            The OCID of the user.

        :param str customer_secret_key_id: (required)
            The OCID of the secret key.

        :param UpdateCustomerSecretKeyDetails update_customer_secret_key_details: (required)
            Request object for updating a secret key.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.CustomerSecretKeySummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/customerSecretKeys/{customerSecretKeyId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_customer_secret_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "customerSecretKeyId": customer_secret_key_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_customer_secret_key_details,
                response_type="CustomerSecretKeySummary")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_customer_secret_key_details,
                response_type="CustomerSecretKeySummary")

    def update_dynamic_group(self, dynamic_group_id, update_dynamic_group_details, **kwargs):
        """
        UpdateDynamicGroup
        Updates the specified dynamic group.


        :param str dynamic_group_id: (required)
            The OCID of the dynamic group.

        :param UpdateDynamicGroupDetails update_dynamic_group_details: (required)
            Request object for updating an dynamic group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.DynamicGroup`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/dynamicGroups/{dynamicGroupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_dynamic_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dynamicGroupId": dynamic_group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_dynamic_group_details,
                response_type="DynamicGroup")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_dynamic_group_details,
                response_type="DynamicGroup")

    def update_group(self, group_id, update_group_details, **kwargs):
        """
        UpdateGroup
        Updates the specified group.


        :param str group_id: (required)
            The OCID of the group.

        :param UpdateGroupDetails update_group_details: (required)
            Request object for updating a group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Group`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/groups/{groupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "groupId": group_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_group_details,
                response_type="Group")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_group_details,
                response_type="Group")

    def update_identity_provider(self, identity_provider_id, update_identity_provider_details, **kwargs):
        """
        UpdateIdentityProvider
        Updates the specified identity provider.


        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param UpdateIdentityProviderDetails update_identity_provider_details: (required)
            Request object for updating a identity provider.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.IdentityProvider`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_identity_provider got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_identity_provider_details,
                response_type="IdentityProvider")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_identity_provider_details,
                response_type="IdentityProvider")

    def update_idp_group_mapping(self, identity_provider_id, mapping_id, update_idp_group_mapping_details, **kwargs):
        """
        UpdateIdpGroupMapping
        Updates the specified group mapping.


        :param str identity_provider_id: (required)
            The OCID of the identity provider.

        :param str mapping_id: (required)
            The OCID of the group mapping.

        :param UpdateIdpGroupMappingDetails update_idp_group_mapping_details: (required)
            Request object for updating an identity provider group mapping

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.IdpGroupMapping`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/identityProviders/{identityProviderId}/groupMappings/{mappingId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_idp_group_mapping got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "identityProviderId": identity_provider_id,
            "mappingId": mapping_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_idp_group_mapping_details,
                response_type="IdpGroupMapping")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_idp_group_mapping_details,
                response_type="IdpGroupMapping")

    def update_policy(self, policy_id, update_policy_details, **kwargs):
        """
        UpdatePolicy
        Updates the specified policy. You can update the description or the policy statements themselves.

        Policy changes take effect typically within 10 seconds.


        :param str policy_id: (required)
            The OCID of the policy.

        :param UpdatePolicyDetails update_policy_details: (required)
            Request object for updating a policy.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Policy`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/policies/{policyId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_policy got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "policyId": policy_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_policy_details,
                response_type="Policy")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_policy_details,
                response_type="Policy")

    def update_smtp_credential(self, user_id, smtp_credential_id, update_smtp_credential_details, **kwargs):
        """
        UpdateSmtpCredential
        Updates the specified SMTP credential's description.


        :param str user_id: (required)
            The OCID of the user.

        :param str smtp_credential_id: (required)
            The OCID of the SMTP credential.

        :param UpdateSmtpCredentialDetails update_smtp_credential_details: (required)
            Request object for updating a SMTP credential.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.SmtpCredentialSummary`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/smtpCredentials/{smtpCredentialId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_smtp_credential got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "smtpCredentialId": smtp_credential_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_smtp_credential_details,
                response_type="SmtpCredentialSummary")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_smtp_credential_details,
                response_type="SmtpCredentialSummary")

    def update_swift_password(self, user_id, swift_password_id, update_swift_password_details, **kwargs):
        """
        UpdateSwiftPassword
        **Deprecated. Use :func:`update_auth_token` instead.**

        Updates the specified Swift password's description.


        :param str user_id: (required)
            The OCID of the user.

        :param str swift_password_id: (required)
            The OCID of the Swift password.

        :param UpdateSwiftPasswordDetails update_swift_password_details: (required)
            Request object for updating a Swift password.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.SwiftPassword`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/swiftPasswords/{swiftPasswordId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_swift_password got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id,
            "swiftPasswordId": swift_password_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_swift_password_details,
                response_type="SwiftPassword")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_swift_password_details,
                response_type="SwiftPassword")

    def update_tag(self, tag_namespace_id, tag_name, update_tag_details, **kwargs):
        """
        UpdateTag
        Updates the the specified tag definition. You can update `description`, and `isRetired`.


        :param str tag_namespace_id: (required)
            The OCID of the tag namespace.

        :param str tag_name: (required)
            The name of the tag.

        :param UpdateTagDetails update_tag_details: (required)
            Request object for updating a tag.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.Tag`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces/{tagNamespaceId}/tags/{tagName}"
        method = "PUT"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_tag got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tagNamespaceId": tag_namespace_id,
            "tagName": tag_name
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
                body=update_tag_details,
                response_type="Tag")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_tag_details,
                response_type="Tag")

    def update_tag_namespace(self, tag_namespace_id, update_tag_namespace_details, **kwargs):
        """
        UpdateTagNamespace
        Updates the the specified tag namespace. You can't update the namespace name.

        Updating `isRetired` to 'true' retires the namespace and all the tag definitions in the namespace. Reactivating a
        namespace (changing `isRetired` from 'true' to 'false') does not reactivate tag definitions.
        To reactivate the tag definitions, you must reactivate each one indvidually *after* you reactivate the namespace,
        using :func:`update_tag`. For more information about retiring tag namespaces, see
        `Retiring Key Definitions and Namespace Definitions`__.

        You can't add a namespace with the same name as a retired namespace in the same tenancy.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/taggingoverview.htm#Retiring


        :param str tag_namespace_id: (required)
            The OCID of the tag namespace.

        :param UpdateTagNamespaceDetails update_tag_namespace_details: (required)
            Request object for updating a namespace.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.TagNamespace`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/tagNamespaces/{tagNamespaceId}"
        method = "PUT"

        expected_kwargs = ["retry_strategy"]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_tag_namespace got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "tagNamespaceId": tag_namespace_id
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
                body=update_tag_namespace_details,
                response_type="TagNamespace")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_tag_namespace_details,
                response_type="TagNamespace")

    def update_user(self, user_id, update_user_details, **kwargs):
        """
        UpdateUser
        Updates the description of the specified user.


        :param str user_id: (required)
            The OCID of the user.

        :param UpdateUserDetails update_user_details: (required)
            Request object for updating a user.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.User`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_user got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_user_details,
                response_type="User")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_user_details,
                response_type="User")

    def update_user_state(self, user_id, update_state_details, **kwargs):
        """
        UpdateUserState
        Updates the state of the specified user.


        :param str user_id: (required)
            The OCID of the user.

        :param UpdateStateDetails update_state_details: (required)
            Request object for updating a user state.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.User`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/state/"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_user_state got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=update_state_details,
                response_type="User")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=update_state_details,
                response_type="User")

    def upload_api_key(self, user_id, create_api_key_details, **kwargs):
        """
        UploadApiKey
        Uploads an API signing key for the specified user.

        Every user has permission to use this operation to upload a key for *their own user ID*. An
        administrator in your organization does not need to write a policy to give users this ability.
        To compare, administrators who have permission to the tenancy can use this operation to upload a
        key for any user, including themselves.

        **Important:** Even though you have permission to upload an API key, you might not yet
        have permission to do much else. If you try calling an operation unrelated to your own credential
        management (e.g., `ListUsers`, `LaunchInstance`) and receive an \"unauthorized\" error,
        check with an administrator to confirm which IAM Service group(s) you're in and what access
        you have. Also confirm you're working in the correct compartment.

        After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using
        the object, first make sure its `lifecycleState` has changed to ACTIVE.


        :param str user_id: (required)
            The OCID of the user.

        :param CreateApiKeyDetails create_api_key_details: (required)
            Request object for uploading an API key for a user.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :param obj retry_strategy: (optional)
            A retry strategy to apply to this specific operation/call. This will override any retry strategy set at the client-level.

            This should be one of the strategies available in the :py:mod:`~oci.retry` module. A convenience :py:data:`~oci.retry.DEFAULT_RETRY_STRATEGY`
            is also available. The specifics of the default retry strategy are described `here <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/retries.html>`__.

            To have this operation explicitly not perform any retries, pass an instance of :py:class:`~oci.retry.NoneRetryStrategy`.

        :return: A :class:`~oci.response.Response` object with data of type :class:`~oci.identity.models.ApiKey`
        :rtype: :class:`~oci.response.Response`
        """
        resource_path = "/users/{userId}/apiKeys/"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "retry_strategy",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "upload_api_key got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "userId": user_id
        }

        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        for (k, v) in six.iteritems(path_params):
            if v is None or (isinstance(v, six.string_types) and len(v.strip()) == 0):
                raise ValueError('Parameter {} cannot be None, whitespace or empty string'.format(k))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
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
                body=create_api_key_details,
                response_type="ApiKey")
        else:
            return self.base_client.call_api(
                resource_path=resource_path,
                method=method,
                path_params=path_params,
                header_params=header_params,
                body=create_api_key_details,
                response_type="ApiKey")
