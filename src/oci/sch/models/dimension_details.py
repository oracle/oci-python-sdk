# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DimensionDetails(object):
    """
    A dimension name and value.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DimensionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DimensionDetails.
        :type name: str

        :param dimension_value:
            The value to assign to the dimension_value property of this DimensionDetails.
        :type dimension_value: oci.sch.models.DimensionValueDetails

        """
        self.swagger_types = {
            'name': 'str',
            'dimension_value': 'DimensionValueDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'dimension_value': 'dimensionValue'
        }

        self._name = None
        self._dimension_value = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DimensionDetails.
        Dimension key. A valid dimension key includes only printable ASCII, excluding periods (.) and spaces.
        Custom dimension keys are acceptable. Avoid entering confidential information.
        Due to use by Service Connector Hub, the following dimension names are reserved: `connectorId`, `connectorName`, `connectorSourceType`.
        For information on valid dimension keys and values, see :func:`metric_data_details`.
        Example: `type`


        :return: The name of this DimensionDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DimensionDetails.
        Dimension key. A valid dimension key includes only printable ASCII, excluding periods (.) and spaces.
        Custom dimension keys are acceptable. Avoid entering confidential information.
        Due to use by Service Connector Hub, the following dimension names are reserved: `connectorId`, `connectorName`, `connectorSourceType`.
        For information on valid dimension keys and values, see :func:`metric_data_details`.
        Example: `type`


        :param name: The name of this DimensionDetails.
        :type: str
        """
        self._name = name

    @property
    def dimension_value(self):
        """
        **[Required]** Gets the dimension_value of this DimensionDetails.

        :return: The dimension_value of this DimensionDetails.
        :rtype: oci.sch.models.DimensionValueDetails
        """
        return self._dimension_value

    @dimension_value.setter
    def dimension_value(self, dimension_value):
        """
        Sets the dimension_value of this DimensionDetails.

        :param dimension_value: The dimension_value of this DimensionDetails.
        :type: oci.sch.models.DimensionValueDetails
        """
        self._dimension_value = dimension_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
