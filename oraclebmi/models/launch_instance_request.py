# coding: utf-8

"""
This is a modified version of the same template from swagger-codegen.
The original can be found at https://github.com/swagger-api/swagger-codegen.
The original license is below.

    Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems

class LaunchInstanceRequest(object):

    def __init__(self):
        """
        LaunchInstanceRequest - a model defined in Swagger
        """

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'image': 'str',
            'metadata': 'dict(str, str)',
            'shape': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'image': 'image',
            'metadata': 'metadata',
            'shape': 'shape',
            'subnet_id': 'subnetId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._image = None
        self._metadata = None
        self._shape = None
        self._subnet_id = None


    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this LaunchInstanceRequest.
        The Availability Domain of an instance.

        :return: The availability_domain of this LaunchInstanceRequest.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this LaunchInstanceRequest.
        The Availability Domain of an instance.

        :param availability_domain: The availability_domain of this LaunchInstanceRequest.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this LaunchInstanceRequest.
        The OCID of the compartment.

        :return: The compartment_id of this LaunchInstanceRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LaunchInstanceRequest.
        The OCID of the compartment.

        :param compartment_id: The compartment_id of this LaunchInstanceRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this LaunchInstanceRequest.
        The non-unique, changeable name of an instance.

        :return: The display_name of this LaunchInstanceRequest.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LaunchInstanceRequest.
        The non-unique, changeable name of an instance.

        :param display_name: The display_name of this LaunchInstanceRequest.
        :type: str
        """
        self._display_name = display_name

    @property
    def image(self):
        """
        Gets the image of this LaunchInstanceRequest.
        The image used to boot the instance.

        :return: The image of this LaunchInstanceRequest.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this LaunchInstanceRequest.
        The image used to boot the instance.

        :param image: The image of this LaunchInstanceRequest.
        :type: str
        """
        self._image = image

    @property
    def metadata(self):
        """
        Gets the metadata of this LaunchInstanceRequest.
        Custom metadata key/value pairs that you provide, such as the SSH public key\nrequired to connect to the instance.\n\nA metadata service runs on every launched instance. The service is an HTTP\nendpoint listening on 169.254.169.254. You can use the service to:\n\n* Provide information to [Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)\n  to be used for various system initialization tasks.\n\n* Get information about the instance, including the custom metadata that you\n  provide when you launch the instance.\n\n __Providing Cloud-Init Metadata__\n\n You can use the following metadata key names to provide information to\n Cloud-Init:\n\n __\"ssh_authorized_keys\"__ - Provide one or more public SSH keys to be\n included in the `~/.ssh/authorized_keys` file for the default user on the\n instance. Use a newline character to separate multiple keys. The SSH\n keys must be in the format necessary for the `authorized_keys` file, as shown\n in the example below.\n\n __\"user_data\"__ - Provide your own base64-encoded data to be used by\n Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For\n information about how to take advantage of user data, see the\n [Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html).\n\n __Note:__ Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/` path. When the instance\n launches and either of these keys are provided, the key values are formatted as\n OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:\n\n `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob\n contains, among other things, the SSH keys that you provided for\n  __\"ssh_authorized_keys\"__.\n\n `http://169.254.169.254/openstack/latest/user_data` - Contains the\n base64-decoded data that you provided for __\"user_data\"__.\n\n __Metadata Example__\n\n      \"metadata\" : {\n         \"quake_bot_level\" : \"Severe\",\n         \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com\n         ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",\n         \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"\n      }\n __Getting Metadata on the Instance__\n\n To get information about your instance, connect to the instance using SSH and issue any of the\n following GET requests:\n\n     curl http://169.254.169.254/opc/v1/instance/\n     curl http://169.254.169.254/opc/v1/instance/metadata/\n     curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>\n\n You'll get back a response that includes all the instance information; only the metadata information; or the metadata information for the specified key name, respectively.\n

        :return: The metadata of this LaunchInstanceRequest.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this LaunchInstanceRequest.
        Custom metadata key/value pairs that you provide, such as the SSH public key\nrequired to connect to the instance.\n\nA metadata service runs on every launched instance. The service is an HTTP\nendpoint listening on 169.254.169.254. You can use the service to:\n\n* Provide information to [Cloud-Init](https://cloudinit.readthedocs.org/en/latest/)\n  to be used for various system initialization tasks.\n\n* Get information about the instance, including the custom metadata that you\n  provide when you launch the instance.\n\n __Providing Cloud-Init Metadata__\n\n You can use the following metadata key names to provide information to\n Cloud-Init:\n\n __\"ssh_authorized_keys\"__ - Provide one or more public SSH keys to be\n included in the `~/.ssh/authorized_keys` file for the default user on the\n instance. Use a newline character to separate multiple keys. The SSH\n keys must be in the format necessary for the `authorized_keys` file, as shown\n in the example below.\n\n __\"user_data\"__ - Provide your own base64-encoded data to be used by\n Cloud-Init to run custom scripts or provide custom Cloud-Init configuration. For\n information about how to take advantage of user data, see the\n [Cloud-Init Documentation](http://cloudinit.readthedocs.org/en/latest/topics/format.html).\n\n __Note:__ Cloud-Init does not pull this data from the `http://169.254.169.254/opc/v1/instance/metadata/` path. When the instance\n launches and either of these keys are provided, the key values are formatted as\n OpenStack metadata and copied to the following locations, which are recognized by Cloud-Init:\n\n `http://169.254.169.254/openstack/latest/meta_data.json` - This JSON blob\n contains, among other things, the SSH keys that you provided for\n  __\"ssh_authorized_keys\"__.\n\n `http://169.254.169.254/openstack/latest/user_data` - Contains the\n base64-decoded data that you provided for __\"user_data\"__.\n\n __Metadata Example__\n\n      \"metadata\" : {\n         \"quake_bot_level\" : \"Severe\",\n         \"ssh_authorized_keys\" : \"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCZ06fccNTQfq+xubFlJ5ZR3kt+uzspdH9tXL+lAejSM1NXM+CFZev7MIxfEjas06y80ZBZ7DUTQO0GxJPeD8NCOb1VorF8M4xuLwrmzRtkoZzU16umt4y1W0Q4ifdp3IiiU0U8/WxczSXcUVZOLqkz5dc6oMHdMVpkimietWzGZ4LBBsH/LjEVY7E0V+a0sNchlVDIZcm7ErReBLcdTGDq0uLBiuChyl6RUkX1PNhusquTGwK7zc8OBXkRuubn5UKXhI3Ul9Nyk4XESkVWIGNKmw8mSpoJSjR8P9ZjRmcZVo8S+x4KVPMZKQEor== ryan.smith@company.com\n         ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAzJSAtwEPoB3Jmr58IXrDGzLuDYkWAYg8AsLYlo6JZvKpjY1xednIcfEVQJm4T2DhVmdWhRrwQ8DmayVZvBkLt+zs2LdoAJEVimKwXcJFD/7wtH8Lnk17HiglbbbNXsemjDY0hea4JUE5CfvkIdZBITuMrfqSmA4n3VNoorXYdvtTMoGG8fxMub46RPtuxtqi9bG9Zqenordkg5FJt2mVNfQRqf83CWojcOkklUWq4CjyxaeLf5i9gv1fRoBo4QhiA8I6NCSppO8GnoV/6Ox6TNoh9BiifqGKC9VGYuC89RvUajRBTZSK2TK4DPfaT+2R+slPsFrwiT/oPEhhEK1S5Q== rsa-key-20160227\",\n         \"user_data\" : \"SWYgeW91IGNhbiBzZWUgdGhpcywgdGhlbiBpdCB3b3JrZWQgbWF5YmUuCg==\"\n      }\n __Getting Metadata on the Instance__\n\n To get information about your instance, connect to the instance using SSH and issue any of the\n following GET requests:\n\n     curl http://169.254.169.254/opc/v1/instance/\n     curl http://169.254.169.254/opc/v1/instance/metadata/\n     curl http://169.254.169.254/opc/v1/instance/metadata/<any-key-name>\n\n You'll get back a response that includes all the instance information; only the metadata information; or the metadata information for the specified key name, respectively.\n

        :param metadata: The metadata of this LaunchInstanceRequest.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def shape(self):
        """
        Gets the shape of this LaunchInstanceRequest.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,\nand other resources allocated to the instance. Specify one of the following shapes:\n\n__x5-2.36.256__ Creates a bare metal general purpose compute instance on an\nOracle Server X5-2 with 36 cores and 256 GB RAM. You can add network-attached block\nstorage as needed by using the Cloud Block Storage service. This option offers a balance\nof compute power, memory capacity, and network resources for your general purpose computing needs.\n\n__x5-2.36.512.nvme-6.4__ Creates a bare metal compute instance with NVMe drives. This option adds\nfour locally-attached 1.6 TB NVMe drives (6.4 TB total) to the general purpose compute\nOracle Server X5-2. This option provides hundreds of thousands of IOPS and multiple\nGBs of throughput per second. Use this option for I/O-intensive workloads such as\nrunning large databases, Hadoop, and Apache Spark.\n\nYou may enumerate all available shapes by calling [ListShapes] (#listShapes).\n

        :return: The shape of this LaunchInstanceRequest.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this LaunchInstanceRequest.
        The shape of an instance. The shape determines the number of CPUs, amount of memory,\nand other resources allocated to the instance. Specify one of the following shapes:\n\n__x5-2.36.256__ Creates a bare metal general purpose compute instance on an\nOracle Server X5-2 with 36 cores and 256 GB RAM. You can add network-attached block\nstorage as needed by using the Cloud Block Storage service. This option offers a balance\nof compute power, memory capacity, and network resources for your general purpose computing needs.\n\n__x5-2.36.512.nvme-6.4__ Creates a bare metal compute instance with NVMe drives. This option adds\nfour locally-attached 1.6 TB NVMe drives (6.4 TB total) to the general purpose compute\nOracle Server X5-2. This option provides hundreds of thousands of IOPS and multiple\nGBs of throughput per second. Use this option for I/O-intensive workloads such as\nrunning large databases, Hadoop, and Apache Spark.\n\nYou may enumerate all available shapes by calling [ListShapes] (#listShapes).\n

        :param shape: The shape of this LaunchInstanceRequest.
        :type: str
        """
        self._shape = shape

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this LaunchInstanceRequest.
        The OCID of the subnet.

        :return: The subnet_id of this LaunchInstanceRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this LaunchInstanceRequest.
        The OCID of the subnet.

        :param subnet_id: The subnet_id of this LaunchInstanceRequest.
        :type: str
        """
        self._subnet_id = subnet_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if objects are equal
        """
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

