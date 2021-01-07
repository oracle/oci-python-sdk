# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StaticPublicKey(object):
    """
    A static public key which is used to verify the JWT signature.
    """

    #: A constant which can be used with the format property of a StaticPublicKey.
    #: This constant has a value of "JSON_WEB_KEY"
    FORMAT_JSON_WEB_KEY = "JSON_WEB_KEY"

    #: A constant which can be used with the format property of a StaticPublicKey.
    #: This constant has a value of "PEM"
    FORMAT_PEM = "PEM"

    def __init__(self, **kwargs):
        """
        Initializes a new StaticPublicKey object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.JsonWebKey`
        * :class:`~oci.apigateway.models.PemEncodedPublicKey`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kid:
            The value to assign to the kid property of this StaticPublicKey.
        :type kid: str

        :param format:
            The value to assign to the format property of this StaticPublicKey.
            Allowed values for this property are: "JSON_WEB_KEY", "PEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format: str

        """
        self.swagger_types = {
            'kid': 'str',
            'format': 'str'
        }

        self.attribute_map = {
            'kid': 'kid',
            'format': 'format'
        }

        self._kid = None
        self._format = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['format']

        if type == 'JSON_WEB_KEY':
            return 'JsonWebKey'

        if type == 'PEM':
            return 'PemEncodedPublicKey'
        else:
            return 'StaticPublicKey'

    @property
    def kid(self):
        """
        **[Required]** Gets the kid of this StaticPublicKey.
        A unique key ID. This key will be used to verify the signature of a
        JWT with matching \"kid\".


        :return: The kid of this StaticPublicKey.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """
        Sets the kid of this StaticPublicKey.
        A unique key ID. This key will be used to verify the signature of a
        JWT with matching \"kid\".


        :param kid: The kid of this StaticPublicKey.
        :type: str
        """
        self._kid = kid

    @property
    def format(self):
        """
        **[Required]** Gets the format of this StaticPublicKey.
        The format of the public key.

        Allowed values for this property are: "JSON_WEB_KEY", "PEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format of this StaticPublicKey.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this StaticPublicKey.
        The format of the public key.


        :param format: The format of this StaticPublicKey.
        :type: str
        """
        allowed_values = ["JSON_WEB_KEY", "PEM"]
        if not value_allowed_none_or_none_sentinel(format, allowed_values):
            format = 'UNKNOWN_ENUM_VALUE'
        self._format = format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
