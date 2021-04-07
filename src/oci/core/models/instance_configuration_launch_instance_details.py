# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationLaunchInstanceDetails(object):
    """
    Instance launch details for creating an instance from an instance configuration. Use the `sourceDetails`
    parameter to specify whether a boot volume or an image should be used to launch a new instance.

    See :class:`LaunchInstanceDetails` for more information.
    """

    #: A constant which can be used with the launch_mode property of a InstanceConfigurationLaunchInstanceDetails.
    #: This constant has a value of "NATIVE"
    LAUNCH_MODE_NATIVE = "NATIVE"

    #: A constant which can be used with the launch_mode property of a InstanceConfigurationLaunchInstanceDetails.
    #: This constant has a value of "EMULATED"
    LAUNCH_MODE_EMULATED = "EMULATED"

    #: A constant which can be used with the launch_mode property of a InstanceConfigurationLaunchInstanceDetails.
    #: This constant has a value of "PARAVIRTUALIZED"
    LAUNCH_MODE_PARAVIRTUALIZED = "PARAVIRTUALIZED"

    #: A constant which can be used with the launch_mode property of a InstanceConfigurationLaunchInstanceDetails.
    #: This constant has a value of "CUSTOM"
    LAUNCH_MODE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the preferred_maintenance_action property of a InstanceConfigurationLaunchInstanceDetails.
    #: This constant has a value of "LIVE_MIGRATE"
    PREFERRED_MAINTENANCE_ACTION_LIVE_MIGRATE = "LIVE_MIGRATE"

    #: A constant which can be used with the preferred_maintenance_action property of a InstanceConfigurationLaunchInstanceDetails.
    #: This constant has a value of "REBOOT"
    PREFERRED_MAINTENANCE_ACTION_REBOOT = "REBOOT"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationLaunchInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this InstanceConfigurationLaunchInstanceDetails.
        :type availability_domain: str

        :param capacity_reservation_id:
            The value to assign to the capacity_reservation_id property of this InstanceConfigurationLaunchInstanceDetails.
        :type capacity_reservation_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConfigurationLaunchInstanceDetails.
        :type compartment_id: str

        :param create_vnic_details:
            The value to assign to the create_vnic_details property of this InstanceConfigurationLaunchInstanceDetails.
        :type create_vnic_details: oci.core.models.InstanceConfigurationCreateVnicDetails

        :param defined_tags:
            The value to assign to the defined_tags property of this InstanceConfigurationLaunchInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this InstanceConfigurationLaunchInstanceDetails.
        :type display_name: str

        :param extended_metadata:
            The value to assign to the extended_metadata property of this InstanceConfigurationLaunchInstanceDetails.
        :type extended_metadata: dict(str, object)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this InstanceConfigurationLaunchInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param ipxe_script:
            The value to assign to the ipxe_script property of this InstanceConfigurationLaunchInstanceDetails.
        :type ipxe_script: str

        :param metadata:
            The value to assign to the metadata property of this InstanceConfigurationLaunchInstanceDetails.
        :type metadata: dict(str, str)

        :param shape:
            The value to assign to the shape property of this InstanceConfigurationLaunchInstanceDetails.
        :type shape: str

        :param shape_config:
            The value to assign to the shape_config property of this InstanceConfigurationLaunchInstanceDetails.
        :type shape_config: oci.core.models.InstanceConfigurationLaunchInstanceShapeConfigDetails

        :param platform_config:
            The value to assign to the platform_config property of this InstanceConfigurationLaunchInstanceDetails.
        :type platform_config: oci.core.models.InstanceConfigurationLaunchInstancePlatformConfig

        :param source_details:
            The value to assign to the source_details property of this InstanceConfigurationLaunchInstanceDetails.
        :type source_details: oci.core.models.InstanceConfigurationInstanceSourceDetails

        :param fault_domain:
            The value to assign to the fault_domain property of this InstanceConfigurationLaunchInstanceDetails.
        :type fault_domain: str

        :param dedicated_vm_host_id:
            The value to assign to the dedicated_vm_host_id property of this InstanceConfigurationLaunchInstanceDetails.
        :type dedicated_vm_host_id: str

        :param launch_mode:
            The value to assign to the launch_mode property of this InstanceConfigurationLaunchInstanceDetails.
            Allowed values for this property are: "NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type launch_mode: str

        :param launch_options:
            The value to assign to the launch_options property of this InstanceConfigurationLaunchInstanceDetails.
        :type launch_options: oci.core.models.InstanceConfigurationLaunchOptions

        :param agent_config:
            The value to assign to the agent_config property of this InstanceConfigurationLaunchInstanceDetails.
        :type agent_config: oci.core.models.InstanceConfigurationLaunchInstanceAgentConfigDetails

        :param is_pv_encryption_in_transit_enabled:
            The value to assign to the is_pv_encryption_in_transit_enabled property of this InstanceConfigurationLaunchInstanceDetails.
        :type is_pv_encryption_in_transit_enabled: bool

        :param preferred_maintenance_action:
            The value to assign to the preferred_maintenance_action property of this InstanceConfigurationLaunchInstanceDetails.
            Allowed values for this property are: "LIVE_MIGRATE", "REBOOT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type preferred_maintenance_action: str

        :param instance_options:
            The value to assign to the instance_options property of this InstanceConfigurationLaunchInstanceDetails.
        :type instance_options: oci.core.models.InstanceConfigurationInstanceOptions

        :param availability_config:
            The value to assign to the availability_config property of this InstanceConfigurationLaunchInstanceDetails.
        :type availability_config: oci.core.models.InstanceConfigurationAvailabilityConfig

        :param preemptible_instance_config:
            The value to assign to the preemptible_instance_config property of this InstanceConfigurationLaunchInstanceDetails.
        :type preemptible_instance_config: oci.core.models.PreemptibleInstanceConfigDetails

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'capacity_reservation_id': 'str',
            'compartment_id': 'str',
            'create_vnic_details': 'InstanceConfigurationCreateVnicDetails',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'extended_metadata': 'dict(str, object)',
            'freeform_tags': 'dict(str, str)',
            'ipxe_script': 'str',
            'metadata': 'dict(str, str)',
            'shape': 'str',
            'shape_config': 'InstanceConfigurationLaunchInstanceShapeConfigDetails',
            'platform_config': 'InstanceConfigurationLaunchInstancePlatformConfig',
            'source_details': 'InstanceConfigurationInstanceSourceDetails',
            'fault_domain': 'str',
            'dedicated_vm_host_id': 'str',
            'launch_mode': 'str',
            'launch_options': 'InstanceConfigurationLaunchOptions',
            'agent_config': 'InstanceConfigurationLaunchInstanceAgentConfigDetails',
            'is_pv_encryption_in_transit_enabled': 'bool',
            'preferred_maintenance_action': 'str',
            'instance_options': 'InstanceConfigurationInstanceOptions',
            'availability_config': 'InstanceConfigurationAvailabilityConfig',
            'preemptible_instance_config': 'PreemptibleInstanceConfigDetails'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'capacity_reservation_id': 'capacityReservationId',
            'compartment_id': 'compartmentId',
            'create_vnic_details': 'createVnicDetails',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'extended_metadata': 'extendedMetadata',
            'freeform_tags': 'freeformTags',
            'ipxe_script': 'ipxeScript',
            'metadata': 'metadata',
            'shape': 'shape',
            'shape_config': 'shapeConfig',
            'platform_config': 'platformConfig',
            'source_details': 'sourceDetails',
            'fault_domain': 'faultDomain',
            'dedicated_vm_host_id': 'dedicatedVmHostId',
            'launch_mode': 'launchMode',
            'launch_options': 'launchOptions',
            'agent_config': 'agentConfig',
            'is_pv_encryption_in_transit_enabled': 'isPvEncryptionInTransitEnabled',
            'preferred_maintenance_action': 'preferredMaintenanceAction',
            'instance_options': 'instanceOptions',
            'availability_config': 'availabilityConfig',
            'preemptible_instance_config': 'preemptibleInstanceConfig'
        }

        self._availability_domain = None
        self._capacity_reservation_id = None
        self._compartment_id = None
        self._create_vnic_details = None
        self._defined_tags = None
        self._display_name = None
        self._extended_metadata = None
        self._freeform_tags = None
        self._ipxe_script = None
        self._metadata = None
        self._shape = None
        self._shape_config = None
        self._platform_config = None
        self._source_details = None
        self._fault_domain = None
        self._dedicated_vm_host_id = None
        self._launch_mode = None
        self._launch_options = None
        self._agent_config = None
        self._is_pv_encryption_in_transit_enabled = None
        self._preferred_maintenance_action = None
        self._instance_options = None
        self._availability_config = None
        self._preemptible_instance_config = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this InstanceConfigurationLaunchInstanceDetails.
        The availability domain of the instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this InstanceConfigurationLaunchInstanceDetails.
        The availability domain of the instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def capacity_reservation_id(self):
        """
        Gets the capacity_reservation_id of this InstanceConfigurationLaunchInstanceDetails.
        The OCID of the compute capacity reservation this instance is launched under.


        :return: The capacity_reservation_id of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._capacity_reservation_id

    @capacity_reservation_id.setter
    def capacity_reservation_id(self, capacity_reservation_id):
        """
        Sets the capacity_reservation_id of this InstanceConfigurationLaunchInstanceDetails.
        The OCID of the compute capacity reservation this instance is launched under.


        :param capacity_reservation_id: The capacity_reservation_id of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._capacity_reservation_id = capacity_reservation_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this InstanceConfigurationLaunchInstanceDetails.
        The OCID of the compartment.


        :return: The compartment_id of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this InstanceConfigurationLaunchInstanceDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def create_vnic_details(self):
        """
        Gets the create_vnic_details of this InstanceConfigurationLaunchInstanceDetails.

        :return: The create_vnic_details of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationCreateVnicDetails
        """
        return self._create_vnic_details

    @create_vnic_details.setter
    def create_vnic_details(self, create_vnic_details):
        """
        Sets the create_vnic_details of this InstanceConfigurationLaunchInstanceDetails.

        :param create_vnic_details: The create_vnic_details of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationCreateVnicDetails
        """
        self._create_vnic_details = create_vnic_details

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstanceConfigurationLaunchInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstanceConfigurationLaunchInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this InstanceConfigurationLaunchInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this InstanceConfigurationLaunchInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :return: The display_name of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstanceConfigurationLaunchInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.

        Example: `My bare metal instance`


        :param display_name: The display_name of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def extended_metadata(self):
        """
        Gets the extended_metadata of this InstanceConfigurationLaunchInstanceDetails.
        Additional metadata key/value pairs that you provide. They serve the same purpose and
        functionality as fields in the `metadata` object.

        They are distinguished from `metadata` fields in that these can be nested JSON objects
        (whereas `metadata` fields are string/string maps only).

        The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
        32,000 bytes.


        :return: The extended_metadata of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: dict(str, object)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this InstanceConfigurationLaunchInstanceDetails.
        Additional metadata key/value pairs that you provide. They serve the same purpose and
        functionality as fields in the `metadata` object.

        They are distinguished from `metadata` fields in that these can be nested JSON objects
        (whereas `metadata` fields are string/string maps only).

        The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of
        32,000 bytes.


        :param extended_metadata: The extended_metadata of this InstanceConfigurationLaunchInstanceDetails.
        :type: dict(str, object)
        """
        self._extended_metadata = extended_metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstanceConfigurationLaunchInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstanceConfigurationLaunchInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this InstanceConfigurationLaunchInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def ipxe_script(self):
        """
        Gets the ipxe_script of this InstanceConfigurationLaunchInstanceDetails.
        This is an advanced option.

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

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm


        :return: The ipxe_script of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._ipxe_script

    @ipxe_script.setter
    def ipxe_script(self, ipxe_script):
        """
        Sets the ipxe_script of this InstanceConfigurationLaunchInstanceDetails.
        This is an advanced option.

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

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/References/bringyourownimage.htm


        :param ipxe_script: The ipxe_script of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._ipxe_script = ipxe_script

    @property
    def metadata(self):
        """
        Gets the metadata of this InstanceConfigurationLaunchInstanceDetails.
        Custom metadata key/value pairs that you provide, such as the SSH public key
        required to connect to the instance.

        A metadata service runs on every launched instance. The service is an HTTP
        endpoint listening on 169.254.169.254. You can use the service to:

        * Provide information to `Cloud-Init`__
          to be used for various system initialization tasks.

        * Get information about the instance, including the custom metadata that you
          provide when you launch the instance.

         **Providing Cloud-Init Metadata**

         You can use the following metadata key names to provide information to
         Cloud-Init:

         **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be
         included in the `~/.ssh/authorized_keys` file for the default user on the
         instance. Use a newline character to separate multiple keys. The SSH
         keys must be in the format necessary for the `authorized_keys` file, as shown
         in the example below.

         **\"user_data\"** - Provide your own base64-encoded data to be used by
         Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
         information about how to take advantage of user data, see the
         `Cloud-Init Documentation`__.

         **Metadata Example**

              \"metadata\" : {
                 \"quake_bot_level\" : \"Severe\",
                 \"ssh_authorized_keys\" : \"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\",
                 \"user_data\" : \"<your_public_SSH_key>==\"
              }
         **Getting Metadata on the Instance**

         To get information about your instance, connect to the instance using SSH and issue any of the
         following GET requests:

             curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/
             curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/
             curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>

         You'll get back a response that includes all the instance information; only the metadata information; or
         the metadata information for the specified key name, respectively.

         The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

        __ https://cloudinit.readthedocs.org/en/latest/
        __ http://cloudinit.readthedocs.org/en/latest/topics/format.html


        :return: The metadata of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this InstanceConfigurationLaunchInstanceDetails.
        Custom metadata key/value pairs that you provide, such as the SSH public key
        required to connect to the instance.

        A metadata service runs on every launched instance. The service is an HTTP
        endpoint listening on 169.254.169.254. You can use the service to:

        * Provide information to `Cloud-Init`__
          to be used for various system initialization tasks.

        * Get information about the instance, including the custom metadata that you
          provide when you launch the instance.

         **Providing Cloud-Init Metadata**

         You can use the following metadata key names to provide information to
         Cloud-Init:

         **\"ssh_authorized_keys\"** - Provide one or more public SSH keys to be
         included in the `~/.ssh/authorized_keys` file for the default user on the
         instance. Use a newline character to separate multiple keys. The SSH
         keys must be in the format necessary for the `authorized_keys` file, as shown
         in the example below.

         **\"user_data\"** - Provide your own base64-encoded data to be used by
         Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
         information about how to take advantage of user data, see the
         `Cloud-Init Documentation`__.

         **Metadata Example**

              \"metadata\" : {
                 \"quake_bot_level\" : \"Severe\",
                 \"ssh_authorized_keys\" : \"ssh-rsa <your_public_SSH_key>== rsa-key-20160227\",
                 \"user_data\" : \"<your_public_SSH_key>==\"
              }
         **Getting Metadata on the Instance**

         To get information about your instance, connect to the instance using SSH and issue any of the
         following GET requests:

             curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/
             curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/
             curl -H \"Authorization: Bearer Oracle\" http://169.254.169.254/opc/v2/instance/metadata/<any-key-name>

         You'll get back a response that includes all the instance information; only the metadata information; or
         the metadata information for the specified key name, respectively.

         The combined size of the `metadata` and `extendedMetadata` objects can be a maximum of 32,000 bytes.

        __ https://cloudinit.readthedocs.org/en/latest/
        __ http://cloudinit.readthedocs.org/en/latest/topics/format.html


        :param metadata: The metadata of this InstanceConfigurationLaunchInstanceDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def shape(self):
        """
        Gets the shape of this InstanceConfigurationLaunchInstanceDetails.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.

        You can enumerate all available shapes by calling :func:`list_shapes`.


        :return: The shape of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this InstanceConfigurationLaunchInstanceDetails.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.

        You can enumerate all available shapes by calling :func:`list_shapes`.


        :param shape: The shape of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._shape = shape

    @property
    def shape_config(self):
        """
        Gets the shape_config of this InstanceConfigurationLaunchInstanceDetails.

        :return: The shape_config of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationLaunchInstanceShapeConfigDetails
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this InstanceConfigurationLaunchInstanceDetails.

        :param shape_config: The shape_config of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationLaunchInstanceShapeConfigDetails
        """
        self._shape_config = shape_config

    @property
    def platform_config(self):
        """
        Gets the platform_config of this InstanceConfigurationLaunchInstanceDetails.

        :return: The platform_config of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationLaunchInstancePlatformConfig
        """
        return self._platform_config

    @platform_config.setter
    def platform_config(self, platform_config):
        """
        Sets the platform_config of this InstanceConfigurationLaunchInstanceDetails.

        :param platform_config: The platform_config of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationLaunchInstancePlatformConfig
        """
        self._platform_config = platform_config

    @property
    def source_details(self):
        """
        Gets the source_details of this InstanceConfigurationLaunchInstanceDetails.

        :return: The source_details of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationInstanceSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this InstanceConfigurationLaunchInstanceDetails.

        :param source_details: The source_details of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationInstanceSourceDetails
        """
        self._source_details = source_details

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this InstanceConfigurationLaunchInstanceDetails.
        A fault domain is a grouping of hardware and infrastructure within an availability domain.
        Each availability domain contains three fault domains. Fault domains let you distribute your
        instances so that they are not on the same physical hardware within a single availability domain.
        A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
        instances in other fault domains.

        If you do not specify the fault domain, the system selects one for you.


        To get a list of fault domains, use the
        :func:`list_fault_domains` operation in the
        Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :return: The fault_domain of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this InstanceConfigurationLaunchInstanceDetails.
        A fault domain is a grouping of hardware and infrastructure within an availability domain.
        Each availability domain contains three fault domains. Fault domains let you distribute your
        instances so that they are not on the same physical hardware within a single availability domain.
        A hardware failure or Compute hardware maintenance that affects one fault domain does not affect
        instances in other fault domains.

        If you do not specify the fault domain, the system selects one for you.


        To get a list of fault domains, use the
        :func:`list_fault_domains` operation in the
        Identity and Access Management Service API.

        Example: `FAULT-DOMAIN-1`


        :param fault_domain: The fault_domain of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def dedicated_vm_host_id(self):
        """
        Gets the dedicated_vm_host_id of this InstanceConfigurationLaunchInstanceDetails.
        The OCID of dedicated VM host.

        Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
        cannot be used to launch instance pools.


        :return: The dedicated_vm_host_id of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._dedicated_vm_host_id

    @dedicated_vm_host_id.setter
    def dedicated_vm_host_id(self, dedicated_vm_host_id):
        """
        Sets the dedicated_vm_host_id of this InstanceConfigurationLaunchInstanceDetails.
        The OCID of dedicated VM host.

        Dedicated VM hosts can be used when launching individual instances from an instance configuration. They
        cannot be used to launch instance pools.


        :param dedicated_vm_host_id: The dedicated_vm_host_id of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        self._dedicated_vm_host_id = dedicated_vm_host_id

    @property
    def launch_mode(self):
        """
        Gets the launch_mode of this InstanceConfigurationLaunchInstanceDetails.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.

        Allowed values for this property are: "NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The launch_mode of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._launch_mode

    @launch_mode.setter
    def launch_mode(self, launch_mode):
        """
        Sets the launch_mode of this InstanceConfigurationLaunchInstanceDetails.
        Specifies the configuration mode for launching virtual machine (VM) instances. The configuration modes are:
        * `NATIVE` - VM instances launch with iSCSI boot and VFIO devices. The default value for platform images.
        * `EMULATED` - VM instances launch with emulated devices, such as the E1000 network driver and emulated SCSI disk controller.
        * `PARAVIRTUALIZED` - VM instances launch with paravirtualized devices using VirtIO drivers.
        * `CUSTOM` - VM instances launch with custom configuration settings specified in the `LaunchOptions` parameter.


        :param launch_mode: The launch_mode of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        allowed_values = ["NATIVE", "EMULATED", "PARAVIRTUALIZED", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(launch_mode, allowed_values):
            launch_mode = 'UNKNOWN_ENUM_VALUE'
        self._launch_mode = launch_mode

    @property
    def launch_options(self):
        """
        Gets the launch_options of this InstanceConfigurationLaunchInstanceDetails.

        :return: The launch_options of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationLaunchOptions
        """
        return self._launch_options

    @launch_options.setter
    def launch_options(self, launch_options):
        """
        Sets the launch_options of this InstanceConfigurationLaunchInstanceDetails.

        :param launch_options: The launch_options of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationLaunchOptions
        """
        self._launch_options = launch_options

    @property
    def agent_config(self):
        """
        Gets the agent_config of this InstanceConfigurationLaunchInstanceDetails.

        :return: The agent_config of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationLaunchInstanceAgentConfigDetails
        """
        return self._agent_config

    @agent_config.setter
    def agent_config(self, agent_config):
        """
        Sets the agent_config of this InstanceConfigurationLaunchInstanceDetails.

        :param agent_config: The agent_config of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationLaunchInstanceAgentConfigDetails
        """
        self._agent_config = agent_config

    @property
    def is_pv_encryption_in_transit_enabled(self):
        """
        Gets the is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchInstanceDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.


        :return: The is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: bool
        """
        return self._is_pv_encryption_in_transit_enabled

    @is_pv_encryption_in_transit_enabled.setter
    def is_pv_encryption_in_transit_enabled(self, is_pv_encryption_in_transit_enabled):
        """
        Sets the is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchInstanceDetails.
        Whether to enable in-transit encryption for the data volume's paravirtualized attachment. The default value is false.


        :param is_pv_encryption_in_transit_enabled: The is_pv_encryption_in_transit_enabled of this InstanceConfigurationLaunchInstanceDetails.
        :type: bool
        """
        self._is_pv_encryption_in_transit_enabled = is_pv_encryption_in_transit_enabled

    @property
    def preferred_maintenance_action(self):
        """
        Gets the preferred_maintenance_action of this InstanceConfigurationLaunchInstanceDetails.
        The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported.
        * `LIVE_MIGRATE` - Run maintenance using a live migration.
        * `REBOOT` - Run maintenance using a reboot.

        Allowed values for this property are: "LIVE_MIGRATE", "REBOOT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The preferred_maintenance_action of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: str
        """
        return self._preferred_maintenance_action

    @preferred_maintenance_action.setter
    def preferred_maintenance_action(self, preferred_maintenance_action):
        """
        Sets the preferred_maintenance_action of this InstanceConfigurationLaunchInstanceDetails.
        The preferred maintenance action for an instance. The default is LIVE_MIGRATE, if live migration is supported.
        * `LIVE_MIGRATE` - Run maintenance using a live migration.
        * `REBOOT` - Run maintenance using a reboot.


        :param preferred_maintenance_action: The preferred_maintenance_action of this InstanceConfigurationLaunchInstanceDetails.
        :type: str
        """
        allowed_values = ["LIVE_MIGRATE", "REBOOT"]
        if not value_allowed_none_or_none_sentinel(preferred_maintenance_action, allowed_values):
            preferred_maintenance_action = 'UNKNOWN_ENUM_VALUE'
        self._preferred_maintenance_action = preferred_maintenance_action

    @property
    def instance_options(self):
        """
        Gets the instance_options of this InstanceConfigurationLaunchInstanceDetails.

        :return: The instance_options of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationInstanceOptions
        """
        return self._instance_options

    @instance_options.setter
    def instance_options(self, instance_options):
        """
        Sets the instance_options of this InstanceConfigurationLaunchInstanceDetails.

        :param instance_options: The instance_options of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationInstanceOptions
        """
        self._instance_options = instance_options

    @property
    def availability_config(self):
        """
        Gets the availability_config of this InstanceConfigurationLaunchInstanceDetails.

        :return: The availability_config of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.InstanceConfigurationAvailabilityConfig
        """
        return self._availability_config

    @availability_config.setter
    def availability_config(self, availability_config):
        """
        Sets the availability_config of this InstanceConfigurationLaunchInstanceDetails.

        :param availability_config: The availability_config of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.InstanceConfigurationAvailabilityConfig
        """
        self._availability_config = availability_config

    @property
    def preemptible_instance_config(self):
        """
        Gets the preemptible_instance_config of this InstanceConfigurationLaunchInstanceDetails.

        :return: The preemptible_instance_config of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: oci.core.models.PreemptibleInstanceConfigDetails
        """
        return self._preemptible_instance_config

    @preemptible_instance_config.setter
    def preemptible_instance_config(self, preemptible_instance_config):
        """
        Sets the preemptible_instance_config of this InstanceConfigurationLaunchInstanceDetails.

        :param preemptible_instance_config: The preemptible_instance_config of this InstanceConfigurationLaunchInstanceDetails.
        :type: oci.core.models.PreemptibleInstanceConfigDetails
        """
        self._preemptible_instance_config = preemptible_instance_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
