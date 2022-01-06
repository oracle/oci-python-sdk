# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthorizationRequest(object):
    """
    AuthorizationRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthorizationRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param request_id:
            The value to assign to the request_id property of this AuthorizationRequest.
        :type request_id: str

        :param user_principal:
            The value to assign to the user_principal property of this AuthorizationRequest.
        :type user_principal: oci.identity_data_plane.models.Principal

        :param svc_principal:
            The value to assign to the svc_principal property of this AuthorizationRequest.
        :type svc_principal: oci.identity_data_plane.models.Principal

        :param service_name:
            The value to assign to the service_name property of this AuthorizationRequest.
        :type service_name: str

        :param context:
            The value to assign to the context property of this AuthorizationRequest.
        :type context: list[oci.identity_data_plane.models.PermissionContext]

        :param policy_hash:
            The value to assign to the policy_hash property of this AuthorizationRequest.
        :type policy_hash: str

        """
        self.swagger_types = {
            'request_id': 'str',
            'user_principal': 'Principal',
            'svc_principal': 'Principal',
            'service_name': 'str',
            'context': 'list[PermissionContext]',
            'policy_hash': 'str'
        }

        self.attribute_map = {
            'request_id': 'requestId',
            'user_principal': 'userPrincipal',
            'svc_principal': 'svcPrincipal',
            'service_name': 'serviceName',
            'context': 'context',
            'policy_hash': 'policyHash'
        }

        self._request_id = None
        self._user_principal = None
        self._svc_principal = None
        self._service_name = None
        self._context = None
        self._policy_hash = None

    @property
    def request_id(self):
        """
        **[Required]** Gets the request_id of this AuthorizationRequest.
        The id of this request. It is a GUID.


        :return: The request_id of this AuthorizationRequest.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this AuthorizationRequest.
        The id of this request. It is a GUID.


        :param request_id: The request_id of this AuthorizationRequest.
        :type: str
        """
        self._request_id = request_id

    @property
    def user_principal(self):
        """
        **[Required]** Gets the user_principal of this AuthorizationRequest.
        The user principal object


        :return: The user_principal of this AuthorizationRequest.
        :rtype: oci.identity_data_plane.models.Principal
        """
        return self._user_principal

    @user_principal.setter
    def user_principal(self, user_principal):
        """
        Sets the user_principal of this AuthorizationRequest.
        The user principal object


        :param user_principal: The user_principal of this AuthorizationRequest.
        :type: oci.identity_data_plane.models.Principal
        """
        self._user_principal = user_principal

    @property
    def svc_principal(self):
        """
        **[Required]** Gets the svc_principal of this AuthorizationRequest.
        The service principal object for service to service calls.


        :return: The svc_principal of this AuthorizationRequest.
        :rtype: oci.identity_data_plane.models.Principal
        """
        return self._svc_principal

    @svc_principal.setter
    def svc_principal(self, svc_principal):
        """
        Sets the svc_principal of this AuthorizationRequest.
        The service principal object for service to service calls.


        :param svc_principal: The svc_principal of this AuthorizationRequest.
        :type: oci.identity_data_plane.models.Principal
        """
        self._svc_principal = svc_principal

    @property
    def service_name(self):
        """
        **[Required]** Gets the service_name of this AuthorizationRequest.
        The name of the service that is making this authorization request


        :return: The service_name of this AuthorizationRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this AuthorizationRequest.
        The name of the service that is making this authorization request


        :param service_name: The service_name of this AuthorizationRequest.
        :type: str
        """
        self._service_name = service_name

    @property
    def context(self):
        """
        **[Required]** Gets the context of this AuthorizationRequest.
        A set of permission contexts


        :return: The context of this AuthorizationRequest.
        :rtype: list[oci.identity_data_plane.models.PermissionContext]
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this AuthorizationRequest.
        A set of permission contexts


        :param context: The context of this AuthorizationRequest.
        :type: list[oci.identity_data_plane.models.PermissionContext]
        """
        self._context = context

    @property
    def policy_hash(self):
        """
        **[Required]** Gets the policy_hash of this AuthorizationRequest.
        The hash of cached policy on the caller service side. If this is different than what Identity has, it will
        send the most recent policy statements.


        :return: The policy_hash of this AuthorizationRequest.
        :rtype: str
        """
        return self._policy_hash

    @policy_hash.setter
    def policy_hash(self, policy_hash):
        """
        Sets the policy_hash of this AuthorizationRequest.
        The hash of cached policy on the caller service side. If this is different than what Identity has, it will
        send the most recent policy statements.


        :param policy_hash: The policy_hash of this AuthorizationRequest.
        :type: str
        """
        self._policy_hash = policy_hash

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
