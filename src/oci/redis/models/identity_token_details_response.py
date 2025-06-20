# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220315


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IdentityTokenDetailsResponse(object):
    """
    Response an Identity token generated for Redis cluster
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IdentityTokenDetailsResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param identity_token:
            The value to assign to the identity_token property of this IdentityTokenDetailsResponse.
        :type identity_token: str

        :param redis_user:
            The value to assign to the redis_user property of this IdentityTokenDetailsResponse.
        :type redis_user: str

        """
        self.swagger_types = {
            'identity_token': 'str',
            'redis_user': 'str'
        }
        self.attribute_map = {
            'identity_token': 'identityToken',
            'redis_user': 'redisUser'
        }
        self._identity_token = None
        self._redis_user = None

    @property
    def identity_token(self):
        """
        **[Required]** Gets the identity_token of this IdentityTokenDetailsResponse.
        Generated Identity token


        :return: The identity_token of this IdentityTokenDetailsResponse.
        :rtype: str
        """
        return self._identity_token

    @identity_token.setter
    def identity_token(self, identity_token):
        """
        Sets the identity_token of this IdentityTokenDetailsResponse.
        Generated Identity token


        :param identity_token: The identity_token of this IdentityTokenDetailsResponse.
        :type: str
        """
        self._identity_token = identity_token

    @property
    def redis_user(self):
        """
        **[Required]** Gets the redis_user of this IdentityTokenDetailsResponse.
        Redis user for the newly created identity token


        :return: The redis_user of this IdentityTokenDetailsResponse.
        :rtype: str
        """
        return self._redis_user

    @redis_user.setter
    def redis_user(self, redis_user):
        """
        Sets the redis_user of this IdentityTokenDetailsResponse.
        Redis user for the newly created identity token


        :param redis_user: The redis_user of this IdentityTokenDetailsResponse.
        :type: str
        """
        self._redis_user = redis_user

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
