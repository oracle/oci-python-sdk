# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.


from ..util import formatted_flat_dict


class LaunchInstanceDetails(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'image_id': 'str',
            'metadata': 'dict(str, str)',
            'opc_ipxe_script': 'str',
            'shape': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'image_id': 'imageId',
            'metadata': 'metadata',
            'opc_ipxe_script': 'opcIpxeScript',
            'shape': 'shape',
            'subnet_id': 'subnetId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._image_id = None
        self._metadata = None
        self._opc_ipxe_script = None
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
    def metadata(self):
        """
        Gets the metadata of this LaunchInstanceDetails.
        Custom metadata key/value pairs that you provide, such as the SSH public key
        required to connect to the instance.
        A metadata service runs on every launched instance. The service is an HTTP
        endpoint listening on 169.254.169.254. You can use the service to:
        * Provide information to [Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)
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
         [Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html).
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
        * Provide information to [Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)
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
         [Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html).
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

        :param metadata: The metadata of this LaunchInstanceDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def opc_ipxe_script(self):
        """
        Gets the opc_ipxe_script of this LaunchInstanceDetails.
        For Oracle internal use only.

        :return: The opc_ipxe_script of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._opc_ipxe_script

    @opc_ipxe_script.setter
    def opc_ipxe_script(self, opc_ipxe_script):
        """
        Sets the opc_ipxe_script of this LaunchInstanceDetails.
        For Oracle internal use only.

        :param opc_ipxe_script: The opc_ipxe_script of this LaunchInstanceDetails.
        :type: str
        """
        self._opc_ipxe_script = opc_ipxe_script

    @property
    def shape(self):
        """
        Gets the shape of this LaunchInstanceDetails.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.
        You can enumerate all available shapes by calling ListShapes.

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
        You can enumerate all available shapes by calling ListShapes.

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
