# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInstancePoolDetails(object):
    """
    The data to update an instance pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInstancePoolDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateInstancePoolDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateInstancePoolDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateInstancePoolDetails.
        :type freeform_tags: dict(str, str)

        :param instance_configuration_id:
            The value to assign to the instance_configuration_id property of this UpdateInstancePoolDetails.
        :type instance_configuration_id: str

        :param placement_configurations:
            The value to assign to the placement_configurations property of this UpdateInstancePoolDetails.
        :type placement_configurations: list[oci.core.models.UpdateInstancePoolPlacementConfigurationDetails]

        :param size:
            The value to assign to the size property of this UpdateInstancePoolDetails.
        :type size: int

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'instance_configuration_id': 'str',
            'placement_configurations': 'list[UpdateInstancePoolPlacementConfigurationDetails]',
            'size': 'int'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'instance_configuration_id': 'instanceConfigurationId',
            'placement_configurations': 'placementConfigurations',
            'size': 'size'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._instance_configuration_id = None
        self._placement_configurations = None
        self._size = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateInstancePoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateInstancePoolDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateInstancePoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateInstancePoolDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateInstancePoolDetails.
        A user-friendly name for the instance pool. Does not have to be unique, and it's
        changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateInstancePoolDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateInstancePoolDetails.
        A user-friendly name for the instance pool. Does not have to be unique, and it's
        changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateInstancePoolDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateInstancePoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateInstancePoolDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateInstancePoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateInstancePoolDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def instance_configuration_id(self):
        """
        Gets the instance_configuration_id of this UpdateInstancePoolDetails.
        The `OCID`__ of the instance configuration associated with the
        instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The instance_configuration_id of this UpdateInstancePoolDetails.
        :rtype: str
        """
        return self._instance_configuration_id

    @instance_configuration_id.setter
    def instance_configuration_id(self, instance_configuration_id):
        """
        Sets the instance_configuration_id of this UpdateInstancePoolDetails.
        The `OCID`__ of the instance configuration associated with the
        instance pool.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param instance_configuration_id: The instance_configuration_id of this UpdateInstancePoolDetails.
        :type: str
        """
        self._instance_configuration_id = instance_configuration_id

    @property
    def placement_configurations(self):
        """
        Gets the placement_configurations of this UpdateInstancePoolDetails.
        The placement configurations for the instance pool. Provide one placement configuration for
        each availability domain.

        To use the instance pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :return: The placement_configurations of this UpdateInstancePoolDetails.
        :rtype: list[oci.core.models.UpdateInstancePoolPlacementConfigurationDetails]
        """
        return self._placement_configurations

    @placement_configurations.setter
    def placement_configurations(self, placement_configurations):
        """
        Sets the placement_configurations of this UpdateInstancePoolDetails.
        The placement configurations for the instance pool. Provide one placement configuration for
        each availability domain.

        To use the instance pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :param placement_configurations: The placement_configurations of this UpdateInstancePoolDetails.
        :type: list[oci.core.models.UpdateInstancePoolPlacementConfigurationDetails]
        """
        self._placement_configurations = placement_configurations

    @property
    def size(self):
        """
        Gets the size of this UpdateInstancePoolDetails.
        The number of instances that should be in the instance pool.


        :return: The size of this UpdateInstancePoolDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this UpdateInstancePoolDetails.
        The number of instances that should be in the instance pool.


        :param size: The size of this UpdateInstancePoolDetails.
        :type: int
        """
        self._size = size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
