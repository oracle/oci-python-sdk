# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeNumaNodesPerSocketPlatformOptions(object):
    """
    Configuration options for NUMA nodes per socket.
    """

    #: A constant which can be used with the service_allowed_values property of a ShapeNumaNodesPerSocketPlatformOptions.
    #: This constant has a value of "NPS0"
    SERVICE_ALLOWED_VALUES_NPS0 = "NPS0"

    #: A constant which can be used with the service_allowed_values property of a ShapeNumaNodesPerSocketPlatformOptions.
    #: This constant has a value of "NPS1"
    SERVICE_ALLOWED_VALUES_NPS1 = "NPS1"

    #: A constant which can be used with the service_allowed_values property of a ShapeNumaNodesPerSocketPlatformOptions.
    #: This constant has a value of "NPS2"
    SERVICE_ALLOWED_VALUES_NPS2 = "NPS2"

    #: A constant which can be used with the service_allowed_values property of a ShapeNumaNodesPerSocketPlatformOptions.
    #: This constant has a value of "NPS4"
    SERVICE_ALLOWED_VALUES_NPS4 = "NPS4"

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeNumaNodesPerSocketPlatformOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param service_allowed_values:
            The value to assign to the service_allowed_values property of this ShapeNumaNodesPerSocketPlatformOptions.
            Allowed values for items in this list are: "NPS0", "NPS1", "NPS2", "NPS4", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type service_allowed_values: list[str]

        :param default_value:
            The value to assign to the default_value property of this ShapeNumaNodesPerSocketPlatformOptions.
        :type default_value: str

        """
        self.swagger_types = {
            'service_allowed_values': 'list[str]',
            'default_value': 'str'
        }

        self.attribute_map = {
            'service_allowed_values': 'allowedValues',
            'default_value': 'defaultValue'
        }

        self._service_allowed_values = None
        self._default_value = None

    @property
    def service_allowed_values(self):
        """
        Gets the service_allowed_values of this ShapeNumaNodesPerSocketPlatformOptions.
        The supported values for this platform configuration property.

        Allowed values for items in this list are: "NPS0", "NPS1", "NPS2", "NPS4", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The service_allowed_values of this ShapeNumaNodesPerSocketPlatformOptions.
        :rtype: list[str]
        """
        return self._service_allowed_values

    @service_allowed_values.setter
    def service_allowed_values(self, service_allowed_values):
        """
        Sets the service_allowed_values of this ShapeNumaNodesPerSocketPlatformOptions.
        The supported values for this platform configuration property.


        :param service_allowed_values: The service_allowed_values of this ShapeNumaNodesPerSocketPlatformOptions.
        :type: list[str]
        """
        allowed_values = ["NPS0", "NPS1", "NPS2", "NPS4"]
        if service_allowed_values:
            service_allowed_values[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in service_allowed_values]
        self._service_allowed_values = service_allowed_values

    @property
    def default_value(self):
        """
        Gets the default_value of this ShapeNumaNodesPerSocketPlatformOptions.
        The default NUMA nodes per socket configuration.


        :return: The default_value of this ShapeNumaNodesPerSocketPlatformOptions.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ShapeNumaNodesPerSocketPlatformOptions.
        The default NUMA nodes per socket configuration.


        :param default_value: The default_value of this ShapeNumaNodesPerSocketPlatformOptions.
        :type: str
        """
        self._default_value = default_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
