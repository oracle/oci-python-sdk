# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEmWarehouseDetails(object):
    """
    The information about new EmWarehouse.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEmWarehouseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateEmWarehouseDetails.
        :type display_name: str

        :param em_bridge_id:
            The value to assign to the em_bridge_id property of this CreateEmWarehouseDetails.
        :type em_bridge_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEmWarehouseDetails.
        :type compartment_id: str

        :param operations_insights_warehouse_id:
            The value to assign to the operations_insights_warehouse_id property of this CreateEmWarehouseDetails.
        :type operations_insights_warehouse_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEmWarehouseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEmWarehouseDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'em_bridge_id': 'str',
            'compartment_id': 'str',
            'operations_insights_warehouse_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'em_bridge_id': 'emBridgeId',
            'compartment_id': 'compartmentId',
            'operations_insights_warehouse_id': 'operationsInsightsWarehouseId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._em_bridge_id = None
        self._compartment_id = None
        self._operations_insights_warehouse_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateEmWarehouseDetails.
        EmWarehouse Identifier


        :return: The display_name of this CreateEmWarehouseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateEmWarehouseDetails.
        EmWarehouse Identifier


        :param display_name: The display_name of this CreateEmWarehouseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def em_bridge_id(self):
        """
        **[Required]** Gets the em_bridge_id of this CreateEmWarehouseDetails.
        EMBridge Identifier


        :return: The em_bridge_id of this CreateEmWarehouseDetails.
        :rtype: str
        """
        return self._em_bridge_id

    @em_bridge_id.setter
    def em_bridge_id(self, em_bridge_id):
        """
        Sets the em_bridge_id of this CreateEmWarehouseDetails.
        EMBridge Identifier


        :param em_bridge_id: The em_bridge_id of this CreateEmWarehouseDetails.
        :type: str
        """
        self._em_bridge_id = em_bridge_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateEmWarehouseDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateEmWarehouseDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateEmWarehouseDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateEmWarehouseDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def operations_insights_warehouse_id(self):
        """
        **[Required]** Gets the operations_insights_warehouse_id of this CreateEmWarehouseDetails.
        operations Insights Warehouse Identifier


        :return: The operations_insights_warehouse_id of this CreateEmWarehouseDetails.
        :rtype: str
        """
        return self._operations_insights_warehouse_id

    @operations_insights_warehouse_id.setter
    def operations_insights_warehouse_id(self, operations_insights_warehouse_id):
        """
        Sets the operations_insights_warehouse_id of this CreateEmWarehouseDetails.
        operations Insights Warehouse Identifier


        :param operations_insights_warehouse_id: The operations_insights_warehouse_id of this CreateEmWarehouseDetails.
        :type: str
        """
        self._operations_insights_warehouse_id = operations_insights_warehouse_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateEmWarehouseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateEmWarehouseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateEmWarehouseDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateEmWarehouseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateEmWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateEmWarehouseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateEmWarehouseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateEmWarehouseDetails.
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
