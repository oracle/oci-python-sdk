# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FacetedSearchAggregation(object):
    """
    Aggregation/facets on properties of data object.
    """

    #: A constant which can be used with the property_type property of a FacetedSearchAggregation.
    #: This constant has a value of "CUSTOM_PROPERTY"
    PROPERTY_TYPE_CUSTOM_PROPERTY = "CUSTOM_PROPERTY"

    #: A constant which can be used with the property_type property of a FacetedSearchAggregation.
    #: This constant has a value of "DEFAULT_PROPERTY"
    PROPERTY_TYPE_DEFAULT_PROPERTY = "DEFAULT_PROPERTY"

    def __init__(self, **kwargs):
        """
        Initializes a new FacetedSearchAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FacetedSearchAggregation.
        :type type: str

        :param aggregation:
            The value to assign to the aggregation property of this FacetedSearchAggregation.
        :type aggregation: dict(str, int)

        :param data_type:
            The value to assign to the data_type property of this FacetedSearchAggregation.
        :type data_type: str

        :param property_type:
            The value to assign to the property_type property of this FacetedSearchAggregation.
            Allowed values for this property are: "CUSTOM_PROPERTY", "DEFAULT_PROPERTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type property_type: str

        """
        self.swagger_types = {
            'type': 'str',
            'aggregation': 'dict(str, int)',
            'data_type': 'str',
            'property_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'aggregation': 'aggregation',
            'data_type': 'dataType',
            'property_type': 'propertyType'
        }

        self._type = None
        self._aggregation = None
        self._data_type = None
        self._property_type = None

    @property
    def type(self):
        """
        Gets the type of this FacetedSearchAggregation.
        Name of data object property


        :return: The type of this FacetedSearchAggregation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FacetedSearchAggregation.
        Name of data object property


        :param type: The type of this FacetedSearchAggregation.
        :type: str
        """
        self._type = type

    @property
    def aggregation(self):
        """
        Gets the aggregation of this FacetedSearchAggregation.
        Count of number of data objects having property.


        :return: The aggregation of this FacetedSearchAggregation.
        :rtype: dict(str, int)
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """
        Sets the aggregation of this FacetedSearchAggregation.
        Count of number of data objects having property.


        :param aggregation: The aggregation of this FacetedSearchAggregation.
        :type: dict(str, int)
        """
        self._aggregation = aggregation

    @property
    def data_type(self):
        """
        Gets the data_type of this FacetedSearchAggregation.
        Data type of object property.


        :return: The data_type of this FacetedSearchAggregation.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this FacetedSearchAggregation.
        Data type of object property.


        :param data_type: The data_type of this FacetedSearchAggregation.
        :type: str
        """
        self._data_type = data_type

    @property
    def property_type(self):
        """
        Gets the property_type of this FacetedSearchAggregation.
        Type of property that indicates if it was defined by the user or system.
        CUSTOM_PROPERTY is defined by the user on a data object.
        DEFAULT_PROPERTY is defined by the system on a data object.

        Allowed values for this property are: "CUSTOM_PROPERTY", "DEFAULT_PROPERTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The property_type of this FacetedSearchAggregation.
        :rtype: str
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type):
        """
        Sets the property_type of this FacetedSearchAggregation.
        Type of property that indicates if it was defined by the user or system.
        CUSTOM_PROPERTY is defined by the user on a data object.
        DEFAULT_PROPERTY is defined by the system on a data object.


        :param property_type: The property_type of this FacetedSearchAggregation.
        :type: str
        """
        allowed_values = ["CUSTOM_PROPERTY", "DEFAULT_PROPERTY"]
        if not value_allowed_none_or_none_sentinel(property_type, allowed_values):
            property_type = 'UNKNOWN_ENUM_VALUE'
        self._property_type = property_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
