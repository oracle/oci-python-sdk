# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypeCustomPropertyDetails(object):
    """
    Array of custom property IDs for which we have to associate the custom property to the type
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TypeCustomPropertyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param custom_property_ids:
            The value to assign to the custom_property_ids property of this TypeCustomPropertyDetails.
        :type custom_property_ids: list[str]

        """
        self.swagger_types = {
            'custom_property_ids': 'list[str]'
        }

        self.attribute_map = {
            'custom_property_ids': 'customPropertyIds'
        }

        self._custom_property_ids = None

    @property
    def custom_property_ids(self):
        """
        Gets the custom_property_ids of this TypeCustomPropertyDetails.
        array of custom property Ids


        :return: The custom_property_ids of this TypeCustomPropertyDetails.
        :rtype: list[str]
        """
        return self._custom_property_ids

    @custom_property_ids.setter
    def custom_property_ids(self, custom_property_ids):
        """
        Sets the custom_property_ids of this TypeCustomPropertyDetails.
        array of custom property Ids


        :param custom_property_ids: The custom_property_ids of this TypeCustomPropertyDetails.
        :type: list[str]
        """
        self._custom_property_ids = custom_property_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
