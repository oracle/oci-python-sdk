# coding: utf-8

# This is a modified version of the same template from swagger-codegen.
# The original can be found at https://github.com/swagger-api/swagger-codegen.
# The original license is below.
#
#     Copyright 2016 SmartBear Software
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Ref: https://github.com/swagger-api/swagger-codegen


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
        The Availability Domain of the instance.\n\nExample: `Uocm:PHX-AD-1`\n

        :return: The availability_domain of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this LaunchInstanceDetails.
        The Availability Domain of the instance.\n\nExample: `Uocm:PHX-AD-1`\n

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
        A user-friendly name. Does not have to be unique, and it's changeable.\n\nExample: `My bare metal instance`\n

        :return: The display_name of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LaunchInstanceDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.\n\nExample: `My bare metal instance`\n

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
        Custom metadata key/value pairs that you provide, such as the SSH public key\nrequired to connect to the instance.\n\nA metadata service runs on every launched instance. The service is an HTTP\nendpoint listening on 169.254.169.254. You can use the service to:\n\n* Provide information to [Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)\n  to be used for various system initialization tasks.\n\n* Get information about the instance, including the custom metadata that you\n  provide when you launch the instance.\n\n __Providing Cloud-Init Metadata__\n\n You can use the following metadata key names to provide information to\n Cloud-Init:\n\n __\"ssh_authorized_keys\"__ - Provide one or more public SSH keys to be\n included in the `~/.ssh/authorized_keys` file for the default user on the\n instance. Use a newline character to separate multiple keys. The SSH\n keys must be in the format necessary for the `authorized_keys` file, as shown\n in the example below.\n\n __\"user_data\"__ - Provide your own base64-encoded data to be used by\n Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For\n information about how to take advantage of user data, see the\n [Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html).\n\n __Note:__ Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`\n path. When the instance launches and either of these keys are provided, the key values are formatted as\n OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:\n\n `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob\n contains, among other things, the SSH keys that you provided for\n  __\"ssh_authorized_keys\"__.\n\n `http://169.254.169.254/openstack/latest/user_data` - Contains the\n base64-decoded data that you provided for __\"user_data\"__.\n\n __Metadata Example__\n\n      \"metadata\" : {\n         \"quake_bot_level\" : \"Severe\",\n         \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com\n         ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",\n         \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"\n      }\n __Getting Metadata on the Instance__\n\n To get information about your instance, connect to the instance using SSH and issue any of the\n following GET requests:\n\n     curl http://169.254.169.254/opc/v1/instance/\n     curl http://169.254.169.254/opc/v1/instance/metadata/\n     curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>\n\n You'll get back a response that includes all the instance information; only the metadata information; or\n the metadata information for the specified key name, respectively.\n

        :return: The metadata of this LaunchInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this LaunchInstanceDetails.
        Custom metadata key/value pairs that you provide, such as the SSH public key\nrequired to connect to the instance.\n\nA metadata service runs on every launched instance. The service is an HTTP\nendpoint listening on 169.254.169.254. You can use the service to:\n\n* Provide information to [Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)\n  to be used for various system initialization tasks.\n\n* Get information about the instance, including the custom metadata that you\n  provide when you launch the instance.\n\n __Providing Cloud-Init Metadata__\n\n You can use the following metadata key names to provide information to\n Cloud-Init:\n\n __\"ssh_authorized_keys\"__ - Provide one or more public SSH keys to be\n included in the `~/.ssh/authorized_keys` file for the default user on the\n instance. Use a newline character to separate multiple keys. The SSH\n keys must be in the format necessary for the `authorized_keys` file, as shown\n in the example below.\n\n __\"user_data\"__ - Provide your own base64-encoded data to be used by\n Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For\n information about how to take advantage of user data, see the\n [Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html).\n\n __Note:__ Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/`\n path. When the instance launches and either of these keys are provided, the key values are formatted as\n OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:\n\n `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob\n contains, among other things, the SSH keys that you provided for\n  __\"ssh_authorized_keys\"__.\n\n `http://169.254.169.254/openstack/latest/user_data` - Contains the\n base64-decoded data that you provided for __\"user_data\"__.\n\n __Metadata Example__\n\n      \"metadata\" : {\n         \"quake_bot_level\" : \"Severe\",\n         \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com\n         ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",\n         \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"\n      }\n __Getting Metadata on the Instance__\n\n To get information about your instance, connect to the instance using SSH and issue any of the\n following GET requests:\n\n     curl http://169.254.169.254/opc/v1/instance/\n     curl http://169.254.169.254/opc/v1/instance/metadata/\n     curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>\n\n You'll get back a response that includes all the instance information; only the metadata information; or\n the metadata information for the specified key name, respectively.\n

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
        The shape of an instance. The shape determines the number of CPUs, amount of memory,\nand other resources allocated to the instance.\n\nYou can enumerate all available shapes by calling [ListShapes](#/en/iaas/20160918/Shape/ListShapes).\n

        :return: The shape of this LaunchInstanceDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this LaunchInstanceDetails.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,\nand other resources allocated to the instance.\n\nYou can enumerate all available shapes by calling [ListShapes](#/en/iaas/20160918/Shape/ListShapes).\n

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

