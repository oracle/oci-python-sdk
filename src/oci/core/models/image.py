# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Image(object):
    """
    A boot disk image for launching an instance. For more information, see
    `Overview of the Compute Service`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the launch_mode property of a Image.
    #: This constant has a value of "NATIVE"
    LAUNCH_MODE_NATIVE = "NATIVE"

    #: A constant which can be used with the launch_mode property of a Image.
    #: This constant has a value of "EMULATED"
    LAUNCH_MODE_EMULATED = "EMULATED"

    #: A constant which can be used with the launch_mode property of a Image.
    #: This constant has a value of "PARAVIRTUALIZED"
    LAUNCH_MODE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    #: A constant which can be used with the launch_mode property of a Image.
    #: This constant has a value of "CUSTOM"
    LAUNCH_MODE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the lifecycle_state property of a Image.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Image.
    #: This constant has a value of "IMPORTING"
    LIFECYCLE_STATE_IMPORTING = "IMPORTING"

    #: A constant which can be used with the lifecycle_state property of a Image.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Image.
    #: This constant has a value of "EXPORTING"
    LIFECYCLE_STATE_EXPORTING = "EXPORTING"

    #: A constant which can be used with the lifecycle_state property of a Image.
    #: This constant has a value of "DISABLED"
    LIFECYCLE_STATE_DISABLED = "DISABLED"

    #: A constant which can be used with the lifecycle_state property of a Image.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Image object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param base_image_id:
            The value to assign to the base_image_id property of this Image.
        :type base_image_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Image.
        :type compartment_id: str

        :param create_image_allowed:
            The value to assign to the create_image_allowed property of this Image.
        :type create_image_allowed: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this Image.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Image.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Image.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Image.
        :type id: str

        :param launch_mode:
            The value to assign to the launch_mode property of this Image.
            Allowed values for this property are: "NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type launch_mode: str

        :param launch_options:
            The value to assign to the launch_options property of this Image.
        :type launch_options: LaunchOptions

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Image.
            Allowed values for this property are: "PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param operating_system:
            The value to assign to the operating_system property of this Image.
        :type operating_system: str

        :param operating_system_version:
            The value to assign to the operating_system_version property of this Image.
        :type operating_system_version: str

        :param agent_features:
            The value to assign to the agent_features property of this Image.
        :type agent_features: InstanceAgentFeatures

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this Image.
        :type size_in_mbs: int

        :param time_created:
            The value to assign to the time_created property of this Image.
        :type time_created: datetime

        """
        self.swagger_types = {
            'base_image_id': 'str',
            'compartment_id': 'str',
            'create_image_allowed': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'launch_mode': 'str',
            'launch_options': 'LaunchOptions',
            'lifecycle_state': 'str',
            'operating_system': 'str',
            'operating_system_version': 'str',
            'agent_features': 'InstanceAgentFeatures',
            'size_in_mbs': 'int',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'base_image_id': 'baseImageId',
            'compartment_id': 'compartmentId',
            'create_image_allowed': 'createImageAllowed',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'launch_mode': 'launchMode',
            'launch_options': 'launchOptions',
            'lifecycle_state': 'lifecycleState',
            'operating_system': 'operatingSystem',
            'operating_system_version': 'operatingSystemVersion',
            'agent_features': 'agentFeatures',
            'size_in_mbs': 'sizeInMBs',
            'time_created': 'timeCreated'
        }

        self._base_image_id = None
        self._compartment_id = None
        self._create_image_allowed = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._launch_mode = None
        self._launch_options = None
        self._lifecycle_state = None
        self._operating_system = None
        self._operating_system_version = None
        self._agent_features = None
        self._size_in_mbs = None
        self._time_created = None

    @property
    def base_image_id(self):
        """
        Gets the base_image_id of this Image.
        The OCID of the image originally used to launch the instance.


        :return: The base_image_id of this Image.
        :rtype: str
        """
        return self._base_image_id

    @base_image_id.setter
    def base_image_id(self, base_image_id):
        """
        Sets the base_image_id of this Image.
        The OCID of the image originally used to launch the instance.


        :param base_image_id: The base_image_id of this Image.
        :type: str
        """
        self._base_image_id = base_image_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Image.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :return: The compartment_id of this Image.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Image.
        The OCID of the compartment containing the instance you want to use as the basis for the image.


        :param compartment_id: The compartment_id of this Image.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def create_image_allowed(self):
        """
        **[Required]** Gets the create_image_allowed of this Image.
        Whether instances launched with this image can be used to create new images.
        For example, you cannot create an image of an Oracle Database instance.

        Example: `true`


        :return: The create_image_allowed of this Image.
        :rtype: bool
        """
        return self._create_image_allowed

    @create_image_allowed.setter
    def create_image_allowed(self, create_image_allowed):
        """
        Sets the create_image_allowed of this Image.
        Whether instances launched with this image can be used to create new images.
        For example, you cannot create an image of an Oracle Database instance.

        Example: `true`


        :param create_image_allowed: The create_image_allowed of this Image.
        :type: bool
        """
        self._create_image_allowed = create_image_allowed

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Image.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Image.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Image.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Image.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Image.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My custom Oracle Linux image`


        :return: The display_name of this Image.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Image.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        You cannot use an Oracle-provided image name as a custom image name.

        Example: `My custom Oracle Linux image`


        :param display_name: The display_name of this Image.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Image.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Image.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Image.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Image.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Image.
        The OCID of the image.


        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Image.
        The OCID of the image.


        :param id: The id of this Image.
        :type: str
        """
        self._id = id

    @property
    def launch_mode(self):
        """
        Gets the launch_mode of this Image.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

        Allowed values for this property are: "NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The launch_mode of this Image.
        :rtype: str
        """
        return self._launch_mode

    @launch_mode.setter
    def launch_mode(self, launch_mode):
        """
        Sets the launch_mode of this Image.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.


        :param launch_mode: The launch_mode of this Image.
        :type: str
        """
        allowed_values = ["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(launch_mode, allowed_values):
            launch_mode = 'UNKNOWN_ENUM_VALUE'
        self._launch_mode = launch_mode

    @property
    def launch_options(self):
        """
        Gets the launch_options of this Image.

        :return: The launch_options of this Image.
        :rtype: LaunchOptions
        """
        return self._launch_options

    @launch_options.setter
    def launch_options(self, launch_options):
        """
        Sets the launch_options of this Image.

        :param launch_options: The launch_options of this Image.
        :type: LaunchOptions
        """
        self._launch_options = launch_options

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Image.
        Allowed values for this property are: "PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Image.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Image.

        :param lifecycle_state: The lifecycle_state of this Image.
        :type: str
        """
        allowed_values = ["PROVISIONING", "IMPORTING", "AVAILABLE", "EXPORTING", "DISABLED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def operating_system(self):
        """
        **[Required]** Gets the operating_system of this Image.
        The image's operating system.

        Example: `Oracle Linux`


        :return: The operating_system of this Image.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this Image.
        The image's operating system.

        Example: `Oracle Linux`


        :param operating_system: The operating_system of this Image.
        :type: str
        """
        self._operating_system = operating_system

    @property
    def operating_system_version(self):
        """
        **[Required]** Gets the operating_system_version of this Image.
        The image's operating system version.

        Example: `7.2`


        :return: The operating_system_version of this Image.
        :rtype: str
        """
        return self._operating_system_version

    @operating_system_version.setter
    def operating_system_version(self, operating_system_version):
        """
        Sets the operating_system_version of this Image.
        The image's operating system version.

        Example: `7.2`


        :param operating_system_version: The operating_system_version of this Image.
        :type: str
        """
        self._operating_system_version = operating_system_version

    @property
    def agent_features(self):
        """
        Gets the agent_features of this Image.

        :return: The agent_features of this Image.
        :rtype: InstanceAgentFeatures
        """
        return self._agent_features

    @agent_features.setter
    def agent_features(self, agent_features):
        """
        Sets the agent_features of this Image.

        :param agent_features: The agent_features of this Image.
        :type: InstanceAgentFeatures
        """
        self._agent_features = agent_features

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this Image.
        The boot volume size for an instance launched from this image, (1 MB = 1048576 bytes).
        Note this is not the same as the size of the image when it was exported or the actual size of the image.

        Example: `47694`


        :return: The size_in_mbs of this Image.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this Image.
        The boot volume size for an instance launched from this image, (1 MB = 1048576 bytes).
        Note this is not the same as the size of the image when it was exported or the actual size of the image.

        Example: `47694`


        :param size_in_mbs: The size_in_mbs of this Image.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Image.
        The date and time the image was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Image.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Image.
        The date and time the image was created, in the format defined by `RFC3339`__.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Image.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
