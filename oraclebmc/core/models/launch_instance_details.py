# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class LaunchInstanceDetails(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'hostname_label': 'str',
            'image_id': 'str',
            'ipxe_script': 'str',
            'metadata': 'dict(str, str)',
            'shape': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'hostname_label': 'hostnameLabel',
            'image_id': 'imageId',
            'ipxe_script': 'ipxeScript',
            'metadata': 'metadata',
            'shape': 'shape',
            'subnet_id': 'subnetId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._hostname_label = None
        self._image_id = None
        self._ipxe_script = None
        self._metadata = None
        self._shape = None
        self._subnet_id = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this LaunchInstanceDetails.
        The Availability Domain of the instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this LaunchInstanceDetails.
        The Availability Domain of the instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this LaunchInstanceDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this LaunchInstanceDetails.
        The OCID of the compartment.


        :return: The compartment_id of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LaunchInstanceDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this LaunchInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this LaunchInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.

        Example: `My bare metal instance`


        :return: The display_name of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LaunchInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.

        Example: `My bare metal instance`


        :param display_name: The display_name of this LaunchInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this LaunchInstanceDetails.
        The hostname for the VNIC that is created during instance launch.
        Used for DNS. The value is the hostname portion of the instance's
        fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN
        `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value cannot be changed, and it can be retrieved from the
        :class:`Vnic`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance-1`

         __ https://tools.ietf.org/html/rfc952
         __ https://tools.ietf.org/html/rfc1123
        __ {{DOC_SERVER_URL}}/Content/Network/Concepts/dns.htm


        :return: The hostname_label of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this LaunchInstanceDetails.
        The hostname for the VNIC that is created during instance launch.
        Used for DNS. The value is the hostname portion of the instance's
        fully qualified domain name (FQDN) (e.g., `bminstance-1` in FQDN
        `bminstance-1.subnet123.vcn1.oraclevcn.com`).
        Must be unique across all VNICs in the subnet and comply with
        `RFC 952`__ and
        `RFC 1123`__.
        The value cannot be changed, and it can be retrieved from the
        :class:`Vnic`.

        For more information, see
        `DNS in Your Virtual Cloud Network`__.

        Example: `bminstance-1`

         __ https://tools.ietf.org/html/rfc952
         __ https://tools.ietf.org/html/rfc1123
        __ {{DOC_SERVER_URL}}/Content/Network/Concepts/dns.htm


        :param hostname_label: The hostname_label of this LaunchInstanceDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def image_id(self):
        """
        Gets the image_id of this LaunchInstanceDetails.
        The OCID of the image used to boot the instance.


        :return: The image_id of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this LaunchInstanceDetails.
        The OCID of the image used to boot the instance.


        :param image_id: The image_id of this LaunchInstanceDetails.
        :type: str
        """
        self._image_id = image_id

    @property
    def ipxe_script(self):
        """
        Gets the ipxe_script of this LaunchInstanceDetails.
        This is an advanced option.

        When an Oracle Bare Metal Cloud Services or virtual machine
        instance boots, the iPXE firmware that runs on the instance is
        configured to run an iPXE script to continue the boot process.

        If you want more control over the boot process, you can provide
        your own custom iPXE script that will run when the instance boots;
        however, you should be aware that the same iPXE script will run
        every time an instance boots; not only after the initial
        LaunchInstance call.

        The default iPXE script connects to the instance\u2019s local boot
        volume over iSCSI and performs a network boot. If you use a custom iPXE
        script and want to network-boot from the instance\u2019s local boot volume
        over iSCSI the same way as the default iPXE script, you should use the
        following iSCSI IP address: 169.254.0.2, and boot volume IQN:
        iqn.2015-02.oracle.boot.

        For more information about the Bring Your Own Image feature of
        Oracle Bare Metal Cloud Services, see
        `Bring Your Own Image`__.

        For more information about iPXE, see http://ipxe.org.

        __ {{DOC_SERVER_URL}}/Content/Compute/References/bringyourownimage.htm


        :return: The ipxe_script of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._ipxe_script

    @ipxe_script.setter
    def ipxe_script(self, ipxe_script):
        """
        Sets the ipxe_script of this LaunchInstanceDetails.
        This is an advanced option.

        When an Oracle Bare Metal Cloud Services or virtual machine
        instance boots, the iPXE firmware that runs on the instance is
        configured to run an iPXE script to continue the boot process.

        If you want more control over the boot process, you can provide
        your own custom iPXE script that will run when the instance boots;
        however, you should be aware that the same iPXE script will run
        every time an instance boots; not only after the initial
        LaunchInstance call.

        The default iPXE script connects to the instance\u2019s local boot
        volume over iSCSI and performs a network boot. If you use a custom iPXE
        script and want to network-boot from the instance\u2019s local boot volume
        over iSCSI the same way as the default iPXE script, you should use the
        following iSCSI IP address: 169.254.0.2, and boot volume IQN:
        iqn.2015-02.oracle.boot.

        For more information about the Bring Your Own Image feature of
        Oracle Bare Metal Cloud Services, see
        `Bring Your Own Image`__.

        For more information about iPXE, see http://ipxe.org.

        __ {{DOC_SERVER_URL}}/Content/Compute/References/bringyourownimage.htm


        :param ipxe_script: The ipxe_script of this LaunchInstanceDetails.
        :type: str
        """
        self._ipxe_script = ipxe_script

    @property
    def metadata(self):
        """
        Gets the metadata of this LaunchInstanceDetails.
        Custom metadata key/value pairs that you provide, such as the SSH public key
        required to connect to the instance.

        A metadata service runs on every launched instance. The service is an HTTP
        endpoint listening on 169.254.169.254. You can use the service to:

        * Provide information to `Cloud-Init`__
          to be used for various system initialization tasks.

        * Get information about the instance, including the custom metadata that you
          provide when you launch the instance.

         __Providing Cloud-Init Metadata__

         You can use the following metadata key names to provide information to
         Cloud-Init:

         __\"ssh_authorized_keys\"__ - Provide one or more public SSH keys to be
         included in the `~/.ssh/authorized_keys` file for the default user on the
         instance. Use a newline character to separate multiple keys. The SSH
         keys must be in the format necessary for the `authorized_keys` file, as shown
         in the example below.

         __\"user_data\"__ - Provide your own base64-encoded data to be used by
         Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
         information about how to take advantage of user data, see the
         `Cloud-Init Documentation`__.

         __Note:__ Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`
         path. When the instance launches and either of these keys are provided, the key values are formatted as
         OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:

         `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob
         contains, among other things, the SSH keys that you provided for
          __\"ssh_authorized_keys\"__.

         `http://169.254.169.254/openstack/latest/user_data` - Contains the
         base64-decoded data that you provided for __\"user_data\"__.

         __Metadata Example__

              \"metadata\" : {
                 \"quake_bot_level\" : \"Severe\",
                 \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com
                 ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",
                 \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"
              }
         __Getting Metadata on the Instance__

         To get information about your instance, connect to the instance using SSH and issue any of the
         following GET requests:

             curl http://169.254.169.254/opc/v1/instance/
             curl http://169.254.169.254/opc/v1/instance/metadata/
             curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>

         You'll get back a response that includes all the instance information; only the metadata information; or
         the metadata information for the specified key name, respectively.

         __ https://cloudinit.readthedocs.org/en/latest/
         __ http://cloudinit.readthedocs.org/en/latest/topics/format.html


        :return: The metadata of this LaunchInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this LaunchInstanceDetails.
        Custom metadata key/value pairs that you provide, such as the SSH public key
        required to connect to the instance.

        A metadata service runs on every launched instance. The service is an HTTP
        endpoint listening on 169.254.169.254. You can use the service to:

        * Provide information to `Cloud-Init`__
          to be used for various system initialization tasks.

        * Get information about the instance, including the custom metadata that you
          provide when you launch the instance.

         __Providing Cloud-Init Metadata__

         You can use the following metadata key names to provide information to
         Cloud-Init:

         __\"ssh_authorized_keys\"__ - Provide one or more public SSH keys to be
         included in the `~/.ssh/authorized_keys` file for the default user on the
         instance. Use a newline character to separate multiple keys. The SSH
         keys must be in the format necessary for the `authorized_keys` file, as shown
         in the example below.

         __\"user_data\"__ - Provide your own base64-encoded data to be used by
         Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For
         information about how to take advantage of user data, see the
         `Cloud-Init Documentation`__.

         __Note:__ Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`
         path. When the instance launches and either of these keys are provided, the key values are formatted as
         OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:

         `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob
         contains, among other things, the SSH keys that you provided for
          __\"ssh_authorized_keys\"__.

         `http://169.254.169.254/openstack/latest/user_data` - Contains the
         base64-decoded data that you provided for __\"user_data\"__.

         __Metadata Example__

              \"metadata\" : {
                 \"quake_bot_level\" : \"Severe\",
                 \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com
                 ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",
                 \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"
              }
         __Getting Metadata on the Instance__

         To get information about your instance, connect to the instance using SSH and issue any of the
         following GET requests:

             curl http://169.254.169.254/opc/v1/instance/
             curl http://169.254.169.254/opc/v1/instance/metadata/
             curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>

         You'll get back a response that includes all the instance information; only the metadata information; or
         the metadata information for the specified key name, respectively.

         __ https://cloudinit.readthedocs.org/en/latest/
         __ http://cloudinit.readthedocs.org/en/latest/topics/format.html


        :param metadata: The metadata of this LaunchInstanceDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def shape(self):
        """
        Gets the shape of this LaunchInstanceDetails.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.

        You can enumerate all available shapes by calling :func:`list_shapes`.


        :return: The shape of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this LaunchInstanceDetails.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.

        You can enumerate all available shapes by calling :func:`list_shapes`.


        :param shape: The shape of this LaunchInstanceDetails.
        :type: str
        """
        self._shape = shape

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this LaunchInstanceDetails.
        The OCID of the subnet.


        :return: The subnet_id of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this LaunchInstanceDetails.
        The OCID of the subnet.


        :param subnet_id: The subnet_id of this LaunchInstanceDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
