# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInstanceDetails(object):
    """
    UpdateInstanceDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this UpdateInstanceDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param agent_config:
            The value to assign to the agent_config property of this UpdateInstanceDetails.
        :type agent_config: UpdateInstanceAgentConfigDetails

        :param metadata:
            The value to assign to the metadata property of this UpdateInstanceDetails.
        :type metadata: dict(str, str)

        :param extended_metadata:
            The value to assign to the extended_metadata property of this UpdateInstanceDetails.
        :type extended_metadata: dict(str, object)

        :param shape:
            The value to assign to the shape property of this UpdateInstanceDetails.
        :type shape: str

        :param shape_config:
            The value to assign to the shape_config property of this UpdateInstanceDetails.
        :type shape_config: UpdateInstanceShapeConfigDetails

        :param instance_options:
            The value to assign to the instance_options property of this UpdateInstanceDetails.
        :type instance_options: InstanceOptions

        :param fault_domain:
            The value to assign to the fault_domain property of this UpdateInstanceDetails.
        :type fault_domain: str

        :param launch_options:
            The value to assign to the launch_options property of this UpdateInstanceDetails.
        :type launch_options: UpdateLaunchOptions

        :param availability_config:
            The value to assign to the availability_config property of this UpdateInstanceDetails.
        :type availability_config: UpdateInstanceAvailabilityConfigDetails

        """
        self.swagger_types = {
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'agent_config': 'UpdateInstanceAgentConfigDetails',
            'metadata': 'dict(str, str)',
            'extended_metadata': 'dict(str, object)',
            'shape': 'str',
            'shape_config': 'UpdateInstanceShapeConfigDetails',
            'instance_options': 'InstanceOptions',
            'fault_domain': 'str',
            'launch_options': 'UpdateLaunchOptions',
            'availability_config': 'UpdateInstanceAvailabilityConfigDetails'
        }

        self.attribute_map = {
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'agent_config': 'agentConfig',
            'metadata': 'metadata',
            'extended_metadata': 'extendedMetadata',
            'shape': 'shape',
            'shape_config': 'shapeConfig',
            'instance_options': 'instanceOptions',
            'fault_domain': 'faultDomain',
            'launch_options': 'launchOptions',
            'availability_config': 'availabilityConfig'
        }

        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._agent_config = None
        self._metadata = None
        self._extended_metadata = None
        self._shape = None
        self._shape_config = None
        self._instance_options = None
        self._fault_domain = None
        self._launch_options = None
        self._availability_config = None

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :return: The display_name of this UpdateInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :param display_name: The display_name of this UpdateInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def agent_config(self):
        """
        Gets the agent_config of this UpdateInstanceDetails.
        Instance agent configuration options to choose for updating the instance


        :return: The agent_config of this UpdateInstanceDetails.
        :rtype: UpdateInstanceAgentConfigDetails
        """
        return self._agent_config

    @agent_config.setter
    def agent_config(self, agent_config):
        """
        Sets the agent_config of this UpdateInstanceDetails.
        Instance agent configuration options to choose for updating the instance


        :param agent_config: The agent_config of this UpdateInstanceDetails.
        :type: UpdateInstanceAgentConfigDetails
        """
        self._agent_config = agent_config

    @property
    def metadata(self):
        """
        Gets the metadata of this UpdateInstanceDetails.
        Custom metadata key/value string pairs that you provide. Any set of key/value pairs
        provided here will completely replace the current set of key/value pairs in the `metadata`
        field on the instance.

        The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance
        has launched. Any request that updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that
        already exist on the instance.

        The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
        32,000 bytes.


        :return: The metadata of this UpdateInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UpdateInstanceDetails.
        Custom metadata key/value string pairs that you provide. Any set of key/value pairs
        provided here will completely replace the current set of key/value pairs in the `metadata`
        field on the instance.

        The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance
        has launched. Any request that updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that
        already exist on the instance.

        The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
        32,000 bytes.


        :param metadata: The metadata of this UpdateInstanceDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this UpdateInstanceDetails.
        Additional metadata key/value pairs that you provide. They serve the same purpose and
        functionality as fields in the `metadata` object.

        They are distinguished from `metadata` fields in that these can be nested JSON objects
        (whereas `metadata` fields are string/string maps only).

        The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance
        has launched. Any request that updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that
        already exist on the instance.

        The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
        32,000 bytes.


        :return: The extended_metadata of this UpdateInstanceDetails.
        :rtype: dict(str, object)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this UpdateInstanceDetails.
        Additional metadata key/value pairs that you provide. They serve the same purpose and
        functionality as fields in the `metadata` object.

        They are distinguished from `metadata` fields in that these can be nested JSON objects
        (whereas `metadata` fields are string/string maps only).

        The \"user_data\" field and the \"ssh_authorized_keys\" field cannot be changed after an instance
        has launched. Any request that updates, removes, or adds either of these fields will be
        rejected. You must provide the same values for \"user_data\" and \"ssh_authorized_keys\" that
        already exist on the instance.

        The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
        32,000 bytes.


        :param extended_metadata: The extended_metadata of this UpdateInstanceDetails.
        :type: dict(str, object)
        """
        self._extended_metadata = extended_metadata

    @property
    def shape(self):
        """
        Gets the shape of this UpdateInstanceDetails.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory
        allocated to the instance. For more information about how to change shapes, and a list of
        shapes that are supported, see
        `Editing an Instance`__.

        For details about the CPUs, memory, and other properties of each shape, see
        `Compute Shapes`__.

        The new shape must be compatible with the image that was used to launch the instance. You
        can enumerate all available shapes and determine image compatibility by calling
        :func:`list_shapes`.

        If the instance is running when you change the shape, the instance is rebooted.

        Example: `VM.Standard2.1`

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Compute/References/computeshapes.htm


        :return: The shape of this UpdateInstanceDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this UpdateInstanceDetails.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory
        allocated to the instance. For more information about how to change shapes, and a list of
        shapes that are supported, see
        `Editing an Instance`__.

        For details about the CPUs, memory, and other properties of each shape, see
        `Compute Shapes`__.

        The new shape must be compatible with the image that was used to launch the instance. You
        can enumerate all available shapes and determine image compatibility by calling
        :func:`list_shapes`.

        If the instance is running when you change the shape, the instance is rebooted.

        Example: `VM.Standard2.1`

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/Tasks/resizinginstances.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Compute/References/computeshapes.htm


        :param shape: The shape of this UpdateInstanceDetails.
        :type: str
        """
        self._shape = shape

    @property
    def shape_config(self):
        """
        Gets the shape_config of this UpdateInstanceDetails.

        :return: The shape_config of this UpdateInstanceDetails.
        :rtype: UpdateInstanceShapeConfigDetails
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this UpdateInstanceDetails.

        :param shape_config: The shape_config of this UpdateInstanceDetails.
        :type: UpdateInstanceShapeConfigDetails
        """
        self._shape_config = shape_config

    @property
    def instance_options(self):
        """
        Gets the instance_options of this UpdateInstanceDetails.

        :return: The instance_options of this UpdateInstanceDetails.
        :rtype: InstanceOptions
        """
        return self._instance_options

    @instance_options.setter
    def instance_options(self, instance_options):
        """
        Sets the instance_options of this UpdateInstanceDetails.

        :param instance_options: The instance_options of this UpdateInstanceDetails.
        :type: InstanceOptions
        """
        self._instance_options = instance_options

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this UpdateInstanceDetails.
        A fault domain is a grouping of hardware and infrastructure within an availability domain.
        Each availability domain contains three fault domains. Fault domains let you distribute your
        instances so that they are not on the same physical hardware within a single availability domain.
        A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
        instances in other fault domains.

        To get a list of fault domains, use the
        :func:`list_fault_domains` operation in the
        Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :return: The fault_domain of this UpdateInstanceDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this UpdateInstanceDetails.
        A fault domain is a grouping of hardware and infrastructure within an availability domain.
        Each availability domain contains three fault domains. Fault domains let you distribute your
        instances so that they are not on the same physical hardware within a single availability domain.
        A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
        instances in other fault domains.

        To get a list of fault domains, use the
        :func:`list_fault_domains` operation in the
        Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :param fault_domain: The fault_domain of this UpdateInstanceDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def launch_options(self):
        """
        Gets the launch_options of this UpdateInstanceDetails.
        Options for tuning the compatibility and performance of VM shapes.


        :return: The launch_options of this UpdateInstanceDetails.
        :rtype: UpdateLaunchOptions
        """
        return self._launch_options

    @launch_options.setter
    def launch_options(self, launch_options):
        """
        Sets the launch_options of this UpdateInstanceDetails.
        Options for tuning the compatibility and performance of VM shapes.


        :param launch_options: The launch_options of this UpdateInstanceDetails.
        :type: UpdateLaunchOptions
        """
        self._launch_options = launch_options

    @property
    def availability_config(self):
        """
        Gets the availability_config of this UpdateInstanceDetails.
        Options for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware.


        :return: The availability_config of this UpdateInstanceDetails.
        :rtype: UpdateInstanceAvailabilityConfigDetails
        """
        return self._availability_config

    @availability_config.setter
    def availability_config(self, availability_config):
        """
        Sets the availability_config of this UpdateInstanceDetails.
        Options for defining the availability of a VM instance after a maintenance event that impacts the underlying hardware.


        :param availability_config: The availability_config of this UpdateInstanceDetails.
        :type: UpdateInstanceAvailabilityConfigDetails
        """
        self._availability_config = availability_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
