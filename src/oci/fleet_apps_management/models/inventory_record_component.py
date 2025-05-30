# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250228


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InventoryRecordComponent(object):
    """
    Details about a target component
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InventoryRecordComponent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param component_name:
            The value to assign to the component_name property of this InventoryRecordComponent.
        :type component_name: str

        :param component_version:
            The value to assign to the component_version property of this InventoryRecordComponent.
        :type component_version: str

        :param component_path:
            The value to assign to the component_path property of this InventoryRecordComponent.
        :type component_path: str

        :param properties:
            The value to assign to the properties property of this InventoryRecordComponent.
        :type properties: list[oci.fleet_apps_management.models.InventoryRecordProperty]

        """
        self.swagger_types = {
            'component_name': 'str',
            'component_version': 'str',
            'component_path': 'str',
            'properties': 'list[InventoryRecordProperty]'
        }
        self.attribute_map = {
            'component_name': 'componentName',
            'component_version': 'componentVersion',
            'component_path': 'componentPath',
            'properties': 'properties'
        }
        self._component_name = None
        self._component_version = None
        self._component_path = None
        self._properties = None

    @property
    def component_name(self):
        """
        **[Required]** Gets the component_name of this InventoryRecordComponent.
        Name of the target component


        :return: The component_name of this InventoryRecordComponent.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this InventoryRecordComponent.
        Name of the target component


        :param component_name: The component_name of this InventoryRecordComponent.
        :type: str
        """
        self._component_name = component_name

    @property
    def component_version(self):
        """
        **[Required]** Gets the component_version of this InventoryRecordComponent.
        Version of the target component


        :return: The component_version of this InventoryRecordComponent.
        :rtype: str
        """
        return self._component_version

    @component_version.setter
    def component_version(self, component_version):
        """
        Sets the component_version of this InventoryRecordComponent.
        Version of the target component


        :param component_version: The component_version of this InventoryRecordComponent.
        :type: str
        """
        self._component_version = component_version

    @property
    def component_path(self):
        """
        **[Required]** Gets the component_path of this InventoryRecordComponent.
        Path of the component


        :return: The component_path of this InventoryRecordComponent.
        :rtype: str
        """
        return self._component_path

    @component_path.setter
    def component_path(self, component_path):
        """
        Sets the component_path of this InventoryRecordComponent.
        Path of the component


        :param component_path: The component_path of this InventoryRecordComponent.
        :type: str
        """
        self._component_path = component_path

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this InventoryRecordComponent.
        List of component properties


        :return: The properties of this InventoryRecordComponent.
        :rtype: list[oci.fleet_apps_management.models.InventoryRecordProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this InventoryRecordComponent.
        List of component properties


        :param properties: The properties of this InventoryRecordComponent.
        :type: list[oci.fleet_apps_management.models.InventoryRecordProperty]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
