# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MappedSecret(object):
    """
    Mapped secret used on the firewall policy rules.
    """

    #: A constant which can be used with the type property of a MappedSecret.
    #: This constant has a value of "SSL_INBOUND_INSPECTION"
    TYPE_SSL_INBOUND_INSPECTION = "SSL_INBOUND_INSPECTION"

    #: A constant which can be used with the type property of a MappedSecret.
    #: This constant has a value of "SSL_FORWARD_PROXY"
    TYPE_SSL_FORWARD_PROXY = "SSL_FORWARD_PROXY"

    def __init__(self, **kwargs):
        """
        Initializes a new MappedSecret object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.network_firewall.models.VaultMappedSecret`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source:
            The value to assign to the source property of this MappedSecret.
        :type source: str

        :param type:
            The value to assign to the type property of this MappedSecret.
            Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'source': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'source': 'source',
            'type': 'type'
        }

        self._source = None
        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'OCI_VAULT':
            return 'VaultMappedSecret'
        else:
            return 'MappedSecret'

    @property
    def source(self):
        """
        **[Required]** Gets the source of this MappedSecret.
        Source of the secrets, where the secrets are stored.


        :return: The source of this MappedSecret.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this MappedSecret.
        Source of the secrets, where the secrets are stored.


        :param source: The source of this MappedSecret.
        :type: str
        """
        self._source = source

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MappedSecret.
        Type of the secrets mapped based on the policy.

         * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic.
         * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.

        Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MappedSecret.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MappedSecret.
        Type of the secrets mapped based on the policy.

         * `SSL_INBOUND_INSPECTION`: For Inbound inspection of SSL traffic.
         * `SSL_FORWARD_PROXY`: For forward proxy certificates for SSL inspection.


        :param type: The type of this MappedSecret.
        :type: str
        """
        allowed_values = ["SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
