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

from pprint import pformat
from six import iteritems

class Image(object):

    def __init__(self):

        self.swagger_types = {
            'base_image_id': 'str',
            'compartment_id': 'str',
            'create_image_allowed': 'bool',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'operating_system': 'str',
            'operating_system_version': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'base_image_id': 'baseImageId',
            'compartment_id': 'compartmentId',
            'create_image_allowed': 'createImageAllowed',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'operating_system': 'operatingSystem',
            'operating_system_version': 'operatingSystemVersion',
            'time_created': 'timeCreated'
        }

        self._base_image_id = None
        self._compartment_id = None
        self._create_image_allowed = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._operating_system = None
        self._operating_system_version = None
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
        Gets the compartment_id of this Image.
        The OCID of the compartment containing the instance you want to use as the basis for the image.\n

        :return: The compartment_id of this Image.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Image.
        The OCID of the compartment containing the instance you want to use as the basis for the image.\n

        :param compartment_id: The compartment_id of this Image.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def create_image_allowed(self):
        """
        Gets the create_image_allowed of this Image.
        Whether instances launched with this image can be used to create new images. For example, you cannot create an image of an Oracle Database instance.\n\nExample: `true`\n

        :return: The create_image_allowed of this Image.
        :rtype: bool
        """
        return self._create_image_allowed

    @create_image_allowed.setter
    def create_image_allowed(self, create_image_allowed):
        """
        Sets the create_image_allowed of this Image.
        Whether instances launched with this image can be used to create new images. For example, you cannot create an image of an Oracle Database instance.\n\nExample: `true`\n

        :param create_image_allowed: The create_image_allowed of this Image.
        :type: bool
        """
        self._create_image_allowed = create_image_allowed

    @property
    def display_name(self):
        """
        Gets the display_name of this Image.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.\nYou cannot use an Oracle-provided image name as a custom image name.\n\nExample: `My custom Oracle Linux image`\n

        :return: The display_name of this Image.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Image.
        A user-friendly name for the image. It does not have to be unique, and it's changeable.\nYou cannot use an Oracle-provided image name as a custom image name.\n\nExample: `My custom Oracle Linux image`\n

        :param display_name: The display_name of this Image.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Image.
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
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Image.


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
        allowed_values = ["PROVISIONING", "AVAILABLE", "DISABLED", "DELETED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def operating_system(self):
        """
        Gets the operating_system of this Image.
        The image's operating system.\n\nExample: `Oracle Linux`\n

        :return: The operating_system of this Image.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this Image.
        The image's operating system.\n\nExample: `Oracle Linux`\n

        :param operating_system: The operating_system of this Image.
        :type: str
        """
        self._operating_system = operating_system

    @property
    def operating_system_version(self):
        """
        Gets the operating_system_version of this Image.
        The image's operating system version.\n\nExample: `7.2`\n

        :return: The operating_system_version of this Image.
        :rtype: str
        """
        return self._operating_system_version

    @operating_system_version.setter
    def operating_system_version(self, operating_system_version):
        """
        Sets the operating_system_version of this Image.
        The image's operating system version.\n\nExample: `7.2`\n

        :param operating_system_version: The operating_system_version of this Image.
        :type: str
        """
        self._operating_system_version = operating_system_version

    @property
    def time_created(self):
        """
        Gets the time_created of this Image.
        The date and time the image was created, in the format defined by RFC3339.\n\nExample: `2016-08-25T21:10:29.600Z`\n

        :return: The time_created of this Image.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Image.
        The date and time the image was created, in the format defined by RFC3339.\n\nExample: `2016-08-25T21:10:29.600Z`\n

        :param time_created: The time_created of this Image.
        :type: datetime
        """
        self._time_created = time_created

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

