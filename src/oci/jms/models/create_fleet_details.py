# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFleetDetails(object):
    """
    Attributes to create a Fleet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFleetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateFleetDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateFleetDetails.
        :type compartment_id: str

        :param description:
            The value to assign to the description property of this CreateFleetDetails.
        :type description: str

        :param inventory_log:
            The value to assign to the inventory_log property of this CreateFleetDetails.
        :type inventory_log: oci.jms.models.CustomLog

        :param operation_log:
            The value to assign to the operation_log property of this CreateFleetDetails.
        :type operation_log: oci.jms.models.CustomLog

        :param is_advanced_features_enabled:
            The value to assign to the is_advanced_features_enabled property of this CreateFleetDetails.
        :type is_advanced_features_enabled: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFleetDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFleetDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'description': 'str',
            'inventory_log': 'CustomLog',
            'operation_log': 'CustomLog',
            'is_advanced_features_enabled': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'description': 'description',
            'inventory_log': 'inventoryLog',
            'operation_log': 'operationLog',
            'is_advanced_features_enabled': 'isAdvancedFeaturesEnabled',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._description = None
        self._inventory_log = None
        self._operation_log = None
        self._is_advanced_features_enabled = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateFleetDetails.
        The name of the Fleet. The displayName must be unique for Fleets in the same compartment.


        :return: The display_name of this CreateFleetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateFleetDetails.
        The name of the Fleet. The displayName must be unique for Fleets in the same compartment.


        :param display_name: The display_name of this CreateFleetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateFleetDetails.
        The `OCID`__ of the compartment of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateFleetDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateFleetDetails.
        The `OCID`__ of the compartment of the Fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateFleetDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def description(self):
        """
        Gets the description of this CreateFleetDetails.
        The Fleet's description. If nothing is provided, the Fleet description will be null.


        :return: The description of this CreateFleetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateFleetDetails.
        The Fleet's description. If nothing is provided, the Fleet description will be null.


        :param description: The description of this CreateFleetDetails.
        :type: str
        """
        self._description = description

    @property
    def inventory_log(self):
        """
        **[Required]** Gets the inventory_log of this CreateFleetDetails.

        :return: The inventory_log of this CreateFleetDetails.
        :rtype: oci.jms.models.CustomLog
        """
        return self._inventory_log

    @inventory_log.setter
    def inventory_log(self, inventory_log):
        """
        Sets the inventory_log of this CreateFleetDetails.

        :param inventory_log: The inventory_log of this CreateFleetDetails.
        :type: oci.jms.models.CustomLog
        """
        self._inventory_log = inventory_log

    @property
    def operation_log(self):
        """
        Gets the operation_log of this CreateFleetDetails.

        :return: The operation_log of this CreateFleetDetails.
        :rtype: oci.jms.models.CustomLog
        """
        return self._operation_log

    @operation_log.setter
    def operation_log(self, operation_log):
        """
        Sets the operation_log of this CreateFleetDetails.

        :param operation_log: The operation_log of this CreateFleetDetails.
        :type: oci.jms.models.CustomLog
        """
        self._operation_log = operation_log

    @property
    def is_advanced_features_enabled(self):
        """
        Gets the is_advanced_features_enabled of this CreateFleetDetails.
        Whether or not advanced features are enabled in this fleet.
        Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` api instead.


        :return: The is_advanced_features_enabled of this CreateFleetDetails.
        :rtype: bool
        """
        return self._is_advanced_features_enabled

    @is_advanced_features_enabled.setter
    def is_advanced_features_enabled(self, is_advanced_features_enabled):
        """
        Sets the is_advanced_features_enabled of this CreateFleetDetails.
        Whether or not advanced features are enabled in this fleet.
        Deprecated, use `/fleets/{fleetId}/advanceFeatureConfiguration` api instead.


        :param is_advanced_features_enabled: The is_advanced_features_enabled of this CreateFleetDetails.
        :type: bool
        """
        self._is_advanced_features_enabled = is_advanced_features_enabled

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateFleetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this CreateFleetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateFleetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this CreateFleetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateFleetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this CreateFleetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateFleetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this CreateFleetDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
