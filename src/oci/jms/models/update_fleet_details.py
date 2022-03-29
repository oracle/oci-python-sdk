# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFleetDetails(object):
    """
    Attributes to update a Fleet.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFleetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateFleetDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateFleetDetails.
        :type description: str

        :param inventory_log:
            The value to assign to the inventory_log property of this UpdateFleetDetails.
        :type inventory_log: oci.jms.models.CustomLog

        :param operation_log:
            The value to assign to the operation_log property of this UpdateFleetDetails.
        :type operation_log: oci.jms.models.CustomLog

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateFleetDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateFleetDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'inventory_log': 'CustomLog',
            'operation_log': 'CustomLog',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'inventory_log': 'inventoryLog',
            'operation_log': 'operationLog',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._display_name = None
        self._description = None
        self._inventory_log = None
        self._operation_log = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateFleetDetails.
        The name of the Fleet. The displayName must be unique for Fleets in the same compartment.


        :return: The display_name of this UpdateFleetDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateFleetDetails.
        The name of the Fleet. The displayName must be unique for Fleets in the same compartment.


        :param display_name: The display_name of this UpdateFleetDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateFleetDetails.
        The Fleet's description.


        :return: The description of this UpdateFleetDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateFleetDetails.
        The Fleet's description.


        :param description: The description of this UpdateFleetDetails.
        :type: str
        """
        self._description = description

    @property
    def inventory_log(self):
        """
        Gets the inventory_log of this UpdateFleetDetails.

        :return: The inventory_log of this UpdateFleetDetails.
        :rtype: oci.jms.models.CustomLog
        """
        return self._inventory_log

    @inventory_log.setter
    def inventory_log(self, inventory_log):
        """
        Sets the inventory_log of this UpdateFleetDetails.

        :param inventory_log: The inventory_log of this UpdateFleetDetails.
        :type: oci.jms.models.CustomLog
        """
        self._inventory_log = inventory_log

    @property
    def operation_log(self):
        """
        Gets the operation_log of this UpdateFleetDetails.

        :return: The operation_log of this UpdateFleetDetails.
        :rtype: oci.jms.models.CustomLog
        """
        return self._operation_log

    @operation_log.setter
    def operation_log(self, operation_log):
        """
        Sets the operation_log of this UpdateFleetDetails.

        :param operation_log: The operation_log of this UpdateFleetDetails.
        :type: oci.jms.models.CustomLog
        """
        self._operation_log = operation_log

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateFleetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this UpdateFleetDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateFleetDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this UpdateFleetDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateFleetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this UpdateFleetDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateFleetDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this UpdateFleetDetails.
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
