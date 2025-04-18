# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemConnectionInfo(object):
    """
    The connection details required to connect to an external DB system component.
    """

    #: A constant which can be used with the component_type property of a ExternalDbSystemConnectionInfo.
    #: This constant has a value of "DATABASE"
    COMPONENT_TYPE_DATABASE = "DATABASE"

    #: A constant which can be used with the component_type property of a ExternalDbSystemConnectionInfo.
    #: This constant has a value of "ASM"
    COMPONENT_TYPE_ASM = "ASM"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemConnectionInfo object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.ExternalAsmConnectionInfo`
        * :class:`~oci.database_management.models.ExternalDatabaseConnectionInfo`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_type:
            The value to assign to the component_type property of this ExternalDbSystemConnectionInfo.
            Allowed values for this property are: "DATABASE", "ASM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type component_type: str

        """
        self.swagger_types = {
            'component_type': 'str'
        }
        self.attribute_map = {
            'component_type': 'componentType'
        }
        self._component_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['componentType']

        if type == 'ASM':
            return 'ExternalAsmConnectionInfo'

        if type == 'DATABASE':
            return 'ExternalDatabaseConnectionInfo'
        else:
            return 'ExternalDbSystemConnectionInfo'

    @property
    def component_type(self):
        """
        **[Required]** Gets the component_type of this ExternalDbSystemConnectionInfo.
        The component type.

        Allowed values for this property are: "DATABASE", "ASM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The component_type of this ExternalDbSystemConnectionInfo.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """
        Sets the component_type of this ExternalDbSystemConnectionInfo.
        The component type.


        :param component_type: The component_type of this ExternalDbSystemConnectionInfo.
        :type: str
        """
        allowed_values = ["DATABASE", "ASM"]
        if not value_allowed_none_or_none_sentinel(component_type, allowed_values):
            component_type = 'UNKNOWN_ENUM_VALUE'
        self._component_type = component_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
