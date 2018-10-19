# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationLaunchInstanceDetails(object):
    """
    See Instance launch details - :class:`LaunchInstanceDetails`
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationLaunchInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this InstanceConfigurationLaunchInstanceDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this InstanceConfigurationLaunchInstanceDetails.
        :type compartment_id: str

        :param create_vnic_details:
            The value to assign to the create_vnic_details property of this InstanceConfigurationLaunchInstanceDetails.
        :type create_vnic_details: InstanceConfigurationCreateVnicDetails

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

        :param source_details:
            The value to assign to the source_details property of this InstanceConfigurationLaunchInstanceDetails.
        :type source_details: InstanceConfigurationInstanceSourceDetails

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'create_vnic_details': 'InstanceConfigurationCreateVnicDetails',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'extended_metadata': 'dict(str, object)',
            'freeform_tags': 'dict(str, str)',
            'ipxe_script': 'str',
            'metadata': 'dict(str, str)',
            'shape': 'str',
            'source_details': 'InstanceConfigurationInstanceSourceDetails'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'create_vnic_details': 'createVnicDetails',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'extended_metadata': 'extendedMetadata',
            'freeform_tags': 'freeformTags',
            'ipxe_script': 'ipxeScript',
            'metadata': 'metadata',
            'shape': 'shape',
            'source_details': 'sourceDetails'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._create_vnic_details = None
        self._defined_tags = None
        self._display_name = None
        self._extended_metadata = None
        self._freeform_tags = None
        self._ipxe_script = None
        self._metadata = None
        self._shape = None
        self._source_details = None

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
        Details for the primary VNIC, which is automatically created and attached when
        the instance is launched.


        :return: The create_vnic_details of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: InstanceConfigurationCreateVnicDetails
        """
        return self._create_vnic_details

    @create_vnic_details.setter
    def create_vnic_details(self, create_vnic_details):
        """
        Sets the create_vnic_details of this InstanceConfigurationLaunchInstanceDetails.
        Details for the primary VNIC, which is automatically created and attached when
        the instance is launched.


        :param create_vnic_details: The create_vnic_details of this InstanceConfigurationLaunchInstanceDetails.
        :type: InstanceConfigurationCreateVnicDetails
        """
        self._create_vnic_details = create_vnic_details

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this InstanceConfigurationLaunchInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this InstanceConfigurationLaunchInstanceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


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
        Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

        They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps only).


        :return: The extended_metadata of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: dict(str, object)
        """
        return self._extended_metadata

    @extended_metadata.setter
    def extended_metadata(self, extended_metadata):
        """
        Sets the extended_metadata of this InstanceConfigurationLaunchInstanceDetails.
        Additional metadata key/value pairs that you provide. They serve the same purpose and functionality as fields in the 'metadata' object.

        They are distinguished from 'metadata' fields in that these can be nested JSON objects (whereas 'metadata' fields are string/string maps only).


        :param extended_metadata: The extended_metadata of this InstanceConfigurationLaunchInstanceDetails.
        :type: dict(str, object)
        """
        self._extended_metadata = extended_metadata

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this InstanceConfigurationLaunchInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this InstanceConfigurationLaunchInstanceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/References/bringyourownimage.htm


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

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Compute/References/bringyourownimage.htm


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

         **Note:** Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`
         path. When the instance launches and either of these keys are provided, the key values are formatted as
         OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:

         `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob
         contains, among other things, the SSH keys that you provided for
          **\"ssh_authorized_keys\"**.

         `http://169.254.169.254/openstack/latest/user_data` - Contains the
         base64-decoded data that you provided for **\"user_data\"**.

         **Metadata Example**

              \"metadata\" : {
                 \"quake_bot_level\" : \"Severe\",
                 \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com
                 ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",
                 \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"
              }
         **Getting Metadata on the Instance**

         To get information about your instance, connect to the instance using SSH and issue any of the
         following GET requests:

             curl http://169.254.169.254/opc/v1/instance/
             curl http://169.254.169.254/opc/v1/instance/metadata/
             curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>

         You'll get back a response that includes all the instance information; only the metadata information; or
         the metadata information for the specified key name, respectively.

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

         **Note:** Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`
         path. When the instance launches and either of these keys are provided, the key values are formatted as
         OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:

         `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob
         contains, among other things, the SSH keys that you provided for
          **\"ssh_authorized_keys\"**.

         `http://169.254.169.254/openstack/latest/user_data` - Contains the
         base64-decoded data that you provided for **\"user_data\"**.

         **Metadata Example**

              \"metadata\" : {
                 \"quake_bot_level\" : \"Severe\",
                 \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com
                 ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",
                 \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"
              }
         **Getting Metadata on the Instance**

         To get information about your instance, connect to the instance using SSH and issue any of the
         following GET requests:

             curl http://169.254.169.254/opc/v1/instance/
             curl http://169.254.169.254/opc/v1/instance/metadata/
             curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>

         You'll get back a response that includes all the instance information; only the metadata information; or
         the metadata information for the specified key name, respectively.

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
    def source_details(self):
        """
        Gets the source_details of this InstanceConfigurationLaunchInstanceDetails.
        Details for creating an instance.
        Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.


        :return: The source_details of this InstanceConfigurationLaunchInstanceDetails.
        :rtype: InstanceConfigurationInstanceSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this InstanceConfigurationLaunchInstanceDetails.
        Details for creating an instance.
        Use this parameter to specify whether a boot volume or an image should be used to launch a new instance.


        :param source_details: The source_details of this InstanceConfigurationLaunchInstanceDetails.
        :type: InstanceConfigurationInstanceSourceDetails
        """
        self._source_details = source_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
