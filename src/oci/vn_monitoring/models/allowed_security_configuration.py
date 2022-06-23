# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedSecurityConfiguration(object):
    """
    Defines the allowed security configuration for the traffic.
    """

    #: A constant which can be used with the type property of a AllowedSecurityConfiguration.
    #: This constant has a value of "NSG"
    TYPE_NSG = "NSG"

    #: A constant which can be used with the type property of a AllowedSecurityConfiguration.
    #: This constant has a value of "STATEFUL_NSG"
    TYPE_STATEFUL_NSG = "STATEFUL_NSG"

    #: A constant which can be used with the type property of a AllowedSecurityConfiguration.
    #: This constant has a value of "INGRESS_SECURITY_LIST"
    TYPE_INGRESS_SECURITY_LIST = "INGRESS_SECURITY_LIST"

    #: A constant which can be used with the type property of a AllowedSecurityConfiguration.
    #: This constant has a value of "STATEFUL_INGRESS_SECURITY_LIST"
    TYPE_STATEFUL_INGRESS_SECURITY_LIST = "STATEFUL_INGRESS_SECURITY_LIST"

    #: A constant which can be used with the type property of a AllowedSecurityConfiguration.
    #: This constant has a value of "EGRESS_SECURITY_LIST"
    TYPE_EGRESS_SECURITY_LIST = "EGRESS_SECURITY_LIST"

    #: A constant which can be used with the type property of a AllowedSecurityConfiguration.
    #: This constant has a value of "STATEFUL_EGRESS_SECURITY_LIST"
    TYPE_STATEFUL_EGRESS_SECURITY_LIST = "STATEFUL_EGRESS_SECURITY_LIST"

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedSecurityConfiguration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.StatefulEgressSecurityListConfiguration`
        * :class:`~oci.vn_monitoring.models.NsgConfiguration`
        * :class:`~oci.vn_monitoring.models.IngressSecurityListConfiguration`
        * :class:`~oci.vn_monitoring.models.StatefulIngressSecurityListConfiguration`
        * :class:`~oci.vn_monitoring.models.EgressSecurityListConfiguration`
        * :class:`~oci.vn_monitoring.models.StatefulNsgConfiguration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AllowedSecurityConfiguration.
            Allowed values for this property are: "NSG", "STATEFUL_NSG", "INGRESS_SECURITY_LIST", "STATEFUL_INGRESS_SECURITY_LIST", "EGRESS_SECURITY_LIST", "STATEFUL_EGRESS_SECURITY_LIST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'STATEFUL_EGRESS_SECURITY_LIST':
            return 'StatefulEgressSecurityListConfiguration'

        if type == 'NSG':
            return 'NsgConfiguration'

        if type == 'INGRESS_SECURITY_LIST':
            return 'IngressSecurityListConfiguration'

        if type == 'STATEFUL_INGRESS_SECURITY_LIST':
            return 'StatefulIngressSecurityListConfiguration'

        if type == 'EGRESS_SECURITY_LIST':
            return 'EgressSecurityListConfiguration'

        if type == 'STATEFUL_NSG':
            return 'StatefulNsgConfiguration'
        else:
            return 'AllowedSecurityConfiguration'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AllowedSecurityConfiguration.
        The type of the allowed security configuration.

        Allowed values for this property are: "NSG", "STATEFUL_NSG", "INGRESS_SECURITY_LIST", "STATEFUL_INGRESS_SECURITY_LIST", "EGRESS_SECURITY_LIST", "STATEFUL_EGRESS_SECURITY_LIST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AllowedSecurityConfiguration.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AllowedSecurityConfiguration.
        The type of the allowed security configuration.


        :param type: The type of this AllowedSecurityConfiguration.
        :type: str
        """
        allowed_values = ["NSG", "STATEFUL_NSG", "INGRESS_SECURITY_LIST", "STATEFUL_INGRESS_SECURITY_LIST", "EGRESS_SECURITY_LIST", "STATEFUL_EGRESS_SECURITY_LIST"]
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
