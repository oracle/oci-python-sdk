# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOperationsInsightsWarehouseDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOperationsInsightsWarehouseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateOperationsInsightsWarehouseDetails.
        :type display_name: str

        :param cpu_allocated:
            The value to assign to the cpu_allocated property of this UpdateOperationsInsightsWarehouseDetails.
        :type cpu_allocated: float

        :param storage_allocated_in_gbs:
            The value to assign to the storage_allocated_in_gbs property of this UpdateOperationsInsightsWarehouseDetails.
        :type storage_allocated_in_gbs: float

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOperationsInsightsWarehouseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOperationsInsightsWarehouseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'cpu_allocated': 'float',
            'storage_allocated_in_gbs': 'float',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'cpu_allocated': 'cpuAllocated',
            'storage_allocated_in_gbs': 'storageAllocatedInGBs',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._cpu_allocated = None
        self._storage_allocated_in_gbs = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateOperationsInsightsWarehouseDetails.
        User-friedly name of Operations Insights Warehouse that does not have to be unique.


        :return: The display_name of this UpdateOperationsInsightsWarehouseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateOperationsInsightsWarehouseDetails.
        User-friedly name of Operations Insights Warehouse that does not have to be unique.


        :param display_name: The display_name of this UpdateOperationsInsightsWarehouseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def cpu_allocated(self):
        """
        Gets the cpu_allocated of this UpdateOperationsInsightsWarehouseDetails.
        Number of OCPUs allocated to OPSI Warehouse ADW.


        :return: The cpu_allocated of this UpdateOperationsInsightsWarehouseDetails.
        :rtype: float
        """
        return self._cpu_allocated

    @cpu_allocated.setter
    def cpu_allocated(self, cpu_allocated):
        """
        Sets the cpu_allocated of this UpdateOperationsInsightsWarehouseDetails.
        Number of OCPUs allocated to OPSI Warehouse ADW.


        :param cpu_allocated: The cpu_allocated of this UpdateOperationsInsightsWarehouseDetails.
        :type: float
        """
        self._cpu_allocated = cpu_allocated

    @property
    def storage_allocated_in_gbs(self):
        """
        Gets the storage_allocated_in_gbs of this UpdateOperationsInsightsWarehouseDetails.
        Storage allocated to OPSI Warehouse ADW.


        :return: The storage_allocated_in_gbs of this UpdateOperationsInsightsWarehouseDetails.
        :rtype: float
        """
        return self._storage_allocated_in_gbs

    @storage_allocated_in_gbs.setter
    def storage_allocated_in_gbs(self, storage_allocated_in_gbs):
        """
        Sets the storage_allocated_in_gbs of this UpdateOperationsInsightsWarehouseDetails.
        Storage allocated to OPSI Warehouse ADW.


        :param storage_allocated_in_gbs: The storage_allocated_in_gbs of this UpdateOperationsInsightsWarehouseDetails.
        :type: float
        """
        self._storage_allocated_in_gbs = storage_allocated_in_gbs

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOperationsInsightsWarehouseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOperationsInsightsWarehouseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOperationsInsightsWarehouseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOperationsInsightsWarehouseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOperationsInsightsWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOperationsInsightsWarehouseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOperationsInsightsWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOperationsInsightsWarehouseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
