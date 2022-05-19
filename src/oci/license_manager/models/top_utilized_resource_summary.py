# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopUtilizedResourceSummary(object):
    """
    A summary of a top utlized resource.
    """

    #: A constant which can be used with the unit_type property of a TopUtilizedResourceSummary.
    #: This constant has a value of "OCPU"
    UNIT_TYPE_OCPU = "OCPU"

    def __init__(self, **kwargs):
        """
        Initializes a new TopUtilizedResourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this TopUtilizedResourceSummary.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this TopUtilizedResourceSummary.
        :type resource_name: str

        :param resource_compartment_id:
            The value to assign to the resource_compartment_id property of this TopUtilizedResourceSummary.
        :type resource_compartment_id: str

        :param resource_compartment_name:
            The value to assign to the resource_compartment_name property of this TopUtilizedResourceSummary.
        :type resource_compartment_name: str

        :param total_units:
            The value to assign to the total_units property of this TopUtilizedResourceSummary.
        :type total_units: float

        :param unit_type:
            The value to assign to the unit_type property of this TopUtilizedResourceSummary.
            Allowed values for this property are: "OCPU", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit_type: str

        """
        self.swagger_types = {
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_compartment_id': 'str',
            'resource_compartment_name': 'str',
            'total_units': 'float',
            'unit_type': 'str'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_compartment_id': 'resourceCompartmentId',
            'resource_compartment_name': 'resourceCompartmentName',
            'total_units': 'totalUnits',
            'unit_type': 'unitType'
        }

        self._resource_id = None
        self._resource_name = None
        self._resource_compartment_id = None
        self._resource_compartment_name = None
        self._total_units = None
        self._unit_type = None

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this TopUtilizedResourceSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this TopUtilizedResourceSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this TopUtilizedResourceSummary.
        The `OCID`__ of the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this TopUtilizedResourceSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this TopUtilizedResourceSummary.
        Resource canonical name.


        :return: The resource_name of this TopUtilizedResourceSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this TopUtilizedResourceSummary.
        Resource canonical name.


        :param resource_name: The resource_name of this TopUtilizedResourceSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_compartment_id(self):
        """
        **[Required]** Gets the resource_compartment_id of this TopUtilizedResourceSummary.
        The compartment `OCID`__ that contains the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The resource_compartment_id of this TopUtilizedResourceSummary.
        :rtype: str
        """
        return self._resource_compartment_id

    @resource_compartment_id.setter
    def resource_compartment_id(self, resource_compartment_id):
        """
        Sets the resource_compartment_id of this TopUtilizedResourceSummary.
        The compartment `OCID`__ that contains the resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param resource_compartment_id: The resource_compartment_id of this TopUtilizedResourceSummary.
        :type: str
        """
        self._resource_compartment_id = resource_compartment_id

    @property
    def resource_compartment_name(self):
        """
        **[Required]** Gets the resource_compartment_name of this TopUtilizedResourceSummary.
        The display name of the compartment that contains the resource.


        :return: The resource_compartment_name of this TopUtilizedResourceSummary.
        :rtype: str
        """
        return self._resource_compartment_name

    @resource_compartment_name.setter
    def resource_compartment_name(self, resource_compartment_name):
        """
        Sets the resource_compartment_name of this TopUtilizedResourceSummary.
        The display name of the compartment that contains the resource.


        :param resource_compartment_name: The resource_compartment_name of this TopUtilizedResourceSummary.
        :type: str
        """
        self._resource_compartment_name = resource_compartment_name

    @property
    def total_units(self):
        """
        **[Required]** Gets the total_units of this TopUtilizedResourceSummary.
        Number of license units consumed by the resource.


        :return: The total_units of this TopUtilizedResourceSummary.
        :rtype: float
        """
        return self._total_units

    @total_units.setter
    def total_units(self, total_units):
        """
        Sets the total_units of this TopUtilizedResourceSummary.
        Number of license units consumed by the resource.


        :param total_units: The total_units of this TopUtilizedResourceSummary.
        :type: float
        """
        self._total_units = total_units

    @property
    def unit_type(self):
        """
        **[Required]** Gets the unit_type of this TopUtilizedResourceSummary.
        The resource unit.

        Allowed values for this property are: "OCPU", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit_type of this TopUtilizedResourceSummary.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """
        Sets the unit_type of this TopUtilizedResourceSummary.
        The resource unit.


        :param unit_type: The unit_type of this TopUtilizedResourceSummary.
        :type: str
        """
        allowed_values = ["OCPU"]
        if not value_allowed_none_or_none_sentinel(unit_type, allowed_values):
            unit_type = 'UNKNOWN_ENUM_VALUE'
        self._unit_type = unit_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
