# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TokenAuthenticationValidationPolicy(object):
    """
    Authentication Policies for the Token Authentication types.
    """

    #: A constant which can be used with the type property of a TokenAuthenticationValidationPolicy.
    #: This constant has a value of "STATIC_KEYS"
    TYPE_STATIC_KEYS = "STATIC_KEYS"

    #: A constant which can be used with the type property of a TokenAuthenticationValidationPolicy.
    #: This constant has a value of "REMOTE_JWKS"
    TYPE_REMOTE_JWKS = "REMOTE_JWKS"

    #: A constant which can be used with the type property of a TokenAuthenticationValidationPolicy.
    #: This constant has a value of "REMOTE_DISCOVERY"
    TYPE_REMOTE_DISCOVERY = "REMOTE_DISCOVERY"

    def __init__(self, **kwargs):
        """
        Initializes a new TokenAuthenticationValidationPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.TokenAuthenticationRemoteJWKSValidationPolicy`
        * :class:`~oci.apigateway.models.TokenAuthenticationRemoteDiscoveryValidationPolicy`
        * :class:`~oci.apigateway.models.TokenAuthenticationStaticKeysValidationPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TokenAuthenticationValidationPolicy.
            Allowed values for this property are: "STATIC_KEYS", "REMOTE_JWKS", "REMOTE_DISCOVERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param additional_validation_policy:
            The value to assign to the additional_validation_policy property of this TokenAuthenticationValidationPolicy.
        :type additional_validation_policy: oci.apigateway.models.AdditionalValidationPolicy

        """
        self.swagger_types = {
            'type': 'str',
            'additional_validation_policy': 'AdditionalValidationPolicy'
        }

        self.attribute_map = {
            'type': 'type',
            'additional_validation_policy': 'additionalValidationPolicy'
        }

        self._type = None
        self._additional_validation_policy = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'REMOTE_JWKS':
            return 'TokenAuthenticationRemoteJWKSValidationPolicy'

        if type == 'REMOTE_DISCOVERY':
            return 'TokenAuthenticationRemoteDiscoveryValidationPolicy'

        if type == 'STATIC_KEYS':
            return 'TokenAuthenticationStaticKeysValidationPolicy'
        else:
            return 'TokenAuthenticationValidationPolicy'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this TokenAuthenticationValidationPolicy.
        Type of the token validation policy.

        Allowed values for this property are: "STATIC_KEYS", "REMOTE_JWKS", "REMOTE_DISCOVERY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this TokenAuthenticationValidationPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TokenAuthenticationValidationPolicy.
        Type of the token validation policy.


        :param type: The type of this TokenAuthenticationValidationPolicy.
        :type: str
        """
        allowed_values = ["STATIC_KEYS", "REMOTE_JWKS", "REMOTE_DISCOVERY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def additional_validation_policy(self):
        """
        Gets the additional_validation_policy of this TokenAuthenticationValidationPolicy.

        :return: The additional_validation_policy of this TokenAuthenticationValidationPolicy.
        :rtype: oci.apigateway.models.AdditionalValidationPolicy
        """
        return self._additional_validation_policy

    @additional_validation_policy.setter
    def additional_validation_policy(self, additional_validation_policy):
        """
        Sets the additional_validation_policy of this TokenAuthenticationValidationPolicy.

        :param additional_validation_policy: The additional_validation_policy of this TokenAuthenticationValidationPolicy.
        :type: oci.apigateway.models.AdditionalValidationPolicy
        """
        self._additional_validation_policy = additional_validation_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
