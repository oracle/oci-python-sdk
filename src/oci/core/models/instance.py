# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Instance(object):
    """
    A compute host. The image used to launch the instance determines its operating system and other
    software. The shape specified during the launch process determines the number of CPUs and memory
    allocated to the instance. For more information, see
    `Overview of the Compute Service`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/Concepts/computeoverview.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the launch_mode property of a Instance.
    #: This constant has a value of "NATIVE"
    LAUNCH_MODE_NATIVE = "NATIVE"

    #: A constant which can be used with the launch_mode property of a Instance.
    #: This constant has a value of "EMULATED"
    LAUNCH_MODE_EMULATED = "EMULATED"

    #: A constant which can be used with the launch_mode property of a Instance.
    #: This constant has a value of "CUSTOM"
    LAUNCH_MODE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_STATE_RUNNING = "RUNNING"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "CREATING_IMAGE"
    LIFECYCLE_STATE_CREATING_IMAGE = "CREATING_IMAGE"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Instance.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    def __init__(self, **kwargs):
        """
        Initializes a new Instance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this Instance.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Instance.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Instance.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this Instance.
        :type display_name: str

        :param extended_metadata:
            The value to assign to the extended_metadata property of this Instance.
        :type extended_metadata: dict(str, object)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Instance.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Instance.
        :type id: str

        :param image_id:
            The value to assign to the image_id property of this Instance.
        :type image_id: str

        :param ipxe_script:
            The value to assign to the ipxe_script property of this Instance.
        :type ipxe_script: str

        :param launch_mode:
            The value to assign to the launch_mode property of this Instance.
            Allowed values for this property are: "NATIVE", "EMULATED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type launch_mode: str

        :param launch_options:
            The value to assign to the launch_options property of this Instance.
        :type launch_options: LaunchOptions

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Instance.
            Allowed values for this property are: "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param metadata:
            The value to assign to the metadata property of this Instance.
        :type metadata: dict(str, str)

        :param region:
            The value to assign to the region property of this Instance.
        :type region: str

        :param shape:
            The value to assign to the shape property of this Instance.
        :type shape: str

        :param source_details:
            The value to assign to the source_details property of this Instance.
        :type source_details: InstanceSourceDetails

        :param time_created:
            The value to assign to the time_created property of this Instance.
        :type time_created: datetime

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'extended_metadata': 'dict(str, object)',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'image_id': 'str',
            'ipxe_script': 'str',
            'launch_mode': 'str',
            'launch_options': 'LaunchOptions',
            'lifecycle_state': 'str',
            'metadata': 'dict(str, str)',
            'region': 'str',
            'shape': 'str',
            'source_details': 'InstanceSourceDetails',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'extended_metadata': 'extendedMetadata',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'image_id': 'imageId',
            'ipxe_script': 'ipxeScript',
            'launch_mode': 'launchMode',
            'launch_options': 'launchOptions',
            'lifecycle_state': 'lifecycleState',
            'metadata': 'metadata',
            'region': 'region',
            'shape': 'shape',
            'source_details': 'sourceDetails',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._extended_metadata = None
        self._freeform_tags = None
        self._id = None
        self._image_id = None
        self._ipxe_script = None
        self._launch_mode = None
        self._launch_options = None
        self._lifecycle_state = None
        self._metadata = None
        self._region = None
        self._shape = None
        self._source_details = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this Instance.
        The Availability Domain the instance is running in.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this Instance.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Instance.
        The Availability Domain the instance is running in.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this Instance.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Instance.
        The OCID of the compartment that contains the instance.


        :return: The compartment_id of this Instance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Instance.
        The OCID of the compartment that contains the instance.


        :param compartment_id: The compartment_id of this Instance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Instance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Instance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Instance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Instance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this Instance.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :return: The display_name of this Instance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Instance.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :param display_name: The display_name of this Instance.
        :type: str
        """
        self._display_name = display_name

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this Instance.
        Additional metadata key/value pairs that you provide.  They serve a similar purpose and functionality from fields in the 'metadata' object.

        They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps only).

        If you don't need nested metadata values, it is strongly advised to avoid using this object and use the Metadata object instead.


        :return: The extended_metadata of this Instance.
        :rtype: dict(str, object)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this Instance.
        Additional metadata key/value pairs that you provide.  They serve a similar purpose and functionality from fields in the 'metadata' object.

        They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps only).

        If you don't need nested metadata values, it is strongly advised to avoid using this object and use the Metadata object instead.


        :param extended_metadata: The extended_metadata of this Instance.
        :type: dict(str, object)
        """
        self._extended_metadata = extended_metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Instance.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Instance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Instance.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Instance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Instance.
        The OCID of the instance.


        :return: The id of this Instance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Instance.
        The OCID of the instance.


        :param id: The id of this Instance.
        :type: str
        """
        self._id = id

    @property
    def image_id(self):
        """
        Gets the image_id of this Instance.
        Deprecated. Use `sourceDetails` instead.


        :return: The image_id of this Instance.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this Instance.
        Deprecated. Use `sourceDetails` instead.


        :param image_id: The image_id of this Instance.
        :type: str
        """
        self._image_id = image_id

    @property
    def ipxe_script(self):
        """
        Gets the ipxe_script of this Instance.
        When a bare metal or virtual machine
        instance boots, the iPXE firmware that runs on the instance is
        configured to run an iPXE script to continue the boot process.

        If you want more control over the boot process, you can provide
        your own custom iPXE script that will run when the instance boots;
        however, you should be aware that the same iPXE script will run
        every time an instance boots; not only after the initial
        LaunchInstance call.

        The default iPXE script connects to the instance's local boot
        volume over iSCSI and performs a network boot. If you use a custom iPXE
        script and want to network-boot from the instance's local boot volume
        over iSCSI the same way as the default iPXE script, you should use the
        following iSCSI IP address: 169.254.0.2, and boot volume IQN:
        iqn.2015-02.oracle.boot.

        For more information about the Bring Your Own Image feature of
        Oracle Cloud Infrastructure, see
        `Bring Your Own Image`__.

        For more information about iPXE, see http://ipxe.org.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/References/bringyourownimage.htm


        :return: The ipxe_script of this Instance.
        :rtype: str
        """
        return self._ipxe_script

    @ipxe_script.setter
    def ipxe_script(self, ipxe_script):
        """
        Sets the ipxe_script of this Instance.
        When a bare metal or virtual machine
        instance boots, the iPXE firmware that runs on the instance is
        configured to run an iPXE script to continue the boot process.

        If you want more control over the boot process, you can provide
        your own custom iPXE script that will run when the instance boots;
        however, you should be aware that the same iPXE script will run
        every time an instance boots; not only after the initial
        LaunchInstance call.

        The default iPXE script connects to the instance's local boot
        volume over iSCSI and performs a network boot. If you use a custom iPXE
        script and want to network-boot from the instance's local boot volume
        over iSCSI the same way as the default iPXE script, you should use the
        following iSCSI IP address: 169.254.0.2, and boot volume IQN:
        iqn.2015-02.oracle.boot.

        For more information about the Bring Your Own Image feature of
        Oracle Cloud Infrastructure, see
        `Bring Your Own Image`__.

        For more information about iPXE, see http://ipxe.org.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/References/bringyourownimage.htm


        :param ipxe_script: The ipxe_script of this Instance.
        :type: str
        """
        self._ipxe_script = ipxe_script

    @property
    def launch_mode(self):
        """
        Gets the launch_mode of this Instance.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

        Allowed values for this property are: "NATIVE", "EMULATED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The launch_mode of this Instance.
        :rtype: str
        """
        return self._launch_mode

    @launch_mode.setter
    def launch_mode(self, launch_mode):
        """
        Sets the launch_mode of this Instance.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for Oracle-provided images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.


        :param launch_mode: The launch_mode of this Instance.
        :type: str
        """
        allowed_values = ["NATIVE", "EMULATED", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(launch_mode, allowed_values):
            launch_mode = 'UNKNOWN_ENUM_VALUE'
        self._launch_mode = launch_mode

    @property
    def launch_options(self):
        """
        Gets the launch_options of this Instance.

        :return: The launch_options of this Instance.
        :rtype: LaunchOptions
        """
        return self._launch_options

    @launch_options.setter
    def launch_options(self, launch_options):
        """
        Sets the launch_options of this Instance.

        :param launch_options: The launch_options of this Instance.
        :type: LaunchOptions
        """
        self._launch_options = launch_options

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Instance.
        The current state of the instance.

        Allowed values for this property are: "PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Instance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Instance.
        The current state of the instance.


        :param lifecycle_state: The lifecycle_state of this Instance.
        :type: str
        """
        allowed_values = ["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "CREATING_IMAGE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def metadata(self):
        """
        Gets the metadata of this Instance.
        Custom metadata that you provide.


        :return: The metadata of this Instance.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Instance.
        Custom metadata that you provide.


        :param metadata: The metadata of this Instance.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def region(self):
        """
        **[Required]** Gets the region of this Instance.
        The region that contains the Availability Domain the instance is running in.

        Example: `phx`


        :return: The region of this Instance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Instance.
        The region that contains the Availability Domain the instance is running in.

        Example: `phx`


        :param region: The region of this Instance.
        :type: str
        """
        self._region = region

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this Instance.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory
        allocated to the instance. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :return: The shape of this Instance.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this Instance.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory
        allocated to the instance. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :param shape: The shape of this Instance.
        :type: str
        """
        self._shape = shape

    @property
    def source_details(self):
        """
        Gets the source_details of this Instance.
        Details for creating an instance


        :return: The source_details of this Instance.
        :rtype: InstanceSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this Instance.
        Details for creating an instance


        :param source_details: The source_details of this Instance.
        :type: InstanceSourceDetails
        """
        self._source_details = source_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Instance.
        The date and time the instance was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this Instance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Instance.
        The date and time the instance was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this Instance.
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
