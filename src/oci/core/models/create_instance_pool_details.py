# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateInstancePoolDetails(object):
    """
    The data to create an instance pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateInstancePoolDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateInstancePoolDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateInstancePoolDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateInstancePoolDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateInstancePoolDetails.
        :type freeform_tags: dict(str, str)

        :param instance_configuration_id:
            The value to assign to the instance_configuration_id property of this CreateInstancePoolDetails.
        :type instance_configuration_id: str

        :param placement_configurations:
            The value to assign to the placement_configurations property of this CreateInstancePoolDetails.
        :type placement_configurations: list[CreateInstancePoolPlacementConfigurationDetails]

        :param size:
            The value to assign to the size property of this CreateInstancePoolDetails.
        :type size: int

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'instance_configuration_id': 'str',
            'placement_configurations': 'list[CreateInstancePoolPlacementConfigurationDetails]',
            'size': 'int'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'instance_configuration_id': 'instanceConfigurationId',
            'placement_configurations': 'placementConfigurations',
            'size': 'size'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._instance_configuration_id = None
        self._placement_configurations = None
        self._size = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateInstancePoolDetails.
        The OCID of the compartment containing the instance pool


        :return: The compartment_id of this CreateInstancePoolDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateInstancePoolDetails.
        The OCID of the compartment containing the instance pool


        :param compartment_id: The compartment_id of this CreateInstancePoolDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateInstancePoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateInstancePoolDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateInstancePoolDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateInstancePoolDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateInstancePoolDetails.
        The user-friendly name.  Does not have to be unique.


        :return: The display_name of this CreateInstancePoolDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateInstancePoolDetails.
        The user-friendly name.  Does not have to be unique.


        :param display_name: The display_name of this CreateInstancePoolDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateInstancePoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateInstancePoolDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateInstancePoolDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateInstancePoolDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def instance_configuration_id(self):
        """
        **[Required]** Gets the instance_configuration_id of this CreateInstancePoolDetails.
        The OCID of the instance configuration associated to the instance pool.


        :return: The instance_configuration_id of this CreateInstancePoolDetails.
        :rtype: str
        """
        return self._instance_configuration_id

    @instance_configuration_id.setter
    def instance_configuration_id(self, instance_configuration_id):
        """
        Sets the instance_configuration_id of this CreateInstancePoolDetails.
        The OCID of the instance configuration associated to the instance pool.


        :param instance_configuration_id: The instance_configuration_id of this CreateInstancePoolDetails.
        :type: str
        """
        self._instance_configuration_id = instance_configuration_id

    @property
    def placement_configurations(self):
        """
        **[Required]** Gets the placement_configurations of this CreateInstancePoolDetails.
        The placement configurations for the instance pool.
        There should be 1 placement configuration for each desired AD.


        :return: The placement_configurations of this CreateInstancePoolDetails.
        :rtype: list[CreateInstancePoolPlacementConfigurationDetails]
        """
        return self._placement_configurations

    @placement_configurations.setter
    def placement_configurations(self, placement_configurations):
        """
        Sets the placement_configurations of this CreateInstancePoolDetails.
        The placement configurations for the instance pool.
        There should be 1 placement configuration for each desired AD.


        :param placement_configurations: The placement_configurations of this CreateInstancePoolDetails.
        :type: list[CreateInstancePoolPlacementConfigurationDetails]
        """
        self._placement_configurations = placement_configurations

    @property
    def size(self):
        """
        **[Required]** Gets the size of this CreateInstancePoolDetails.
        The number of instances that should be in the instance pool.


        :return: The size of this CreateInstancePoolDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this CreateInstancePoolDetails.
        The number of instances that should be in the instance pool.


        :param size: The size of this CreateInstancePoolDetails.
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
