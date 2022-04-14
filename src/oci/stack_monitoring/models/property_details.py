# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PropertyDetails(object):
    """
    Property Details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PropertyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param properties_map:
            The value to assign to the properties_map property of this PropertyDetails.
        :type properties_map: dict(str, str)

        """
        self.swagger_types = {
            'properties_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'properties_map': 'propertiesMap'
        }

        self._properties_map = None

    @property
    def properties_map(self):
        """
        Gets the properties_map of this PropertyDetails.
        Key/Value pair of Property


        :return: The properties_map of this PropertyDetails.
        :rtype: dict(str, str)
        """
        return self._properties_map

    @properties_map.setter
    def properties_map(self, properties_map):
        """
        Sets the properties_map of this PropertyDetails.
        Key/Value pair of Property


        :param properties_map: The properties_map of this PropertyDetails.
        :type: dict(str, str)
        """
        self._properties_map = properties_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
