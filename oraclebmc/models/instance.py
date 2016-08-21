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

class Instance(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'image': 'str',
            'metadata': 'dict(str, str)',
            'region': 'str',
            'shape': 'str',
            'state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'image': 'image',
            'metadata': 'metadata',
            'region': 'region',
            'shape': 'shape',
            'state': 'state',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._image = None
        self._metadata = None
        self._region = None
        self._shape = None
        self._state = None
        self._time_created = None


    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Instance.
        The Availability Domain the instance is running in.

        :return: The availability_domain of this Instance.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Instance.
        The Availability Domain the instance is running in.

        :param availability_domain: The availability_domain of this Instance.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Instance.
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
    def display_name(self):
        """
        Gets the display_name of this Instance.
        The non-unique, changeable name of the instance.

        :return: The display_name of this Instance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Instance.
        The non-unique, changeable name of the instance.

        :param display_name: The display_name of this Instance.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Instance.
        The OCID that uniquely identifies the instance.

        :return: The id of this Instance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Instance.
        The OCID that uniquely identifies the instance.

        :param id: The id of this Instance.
        :type: str
        """
        self._id = id

    @property
    def image(self):
        """
        Gets the image of this Instance.
        The image used to boot the instance. The available images are:\n\n  * __ol7.1-base-0.0.1__ - For Oracle Linux 7.1.\n\n  * __ol6.7-oracledbee_12.1.0.2/11.2.0.4-0.0.1__ - For Oracle Linux 6.7 with Oracle Database Enterprise Edition 11.2.0.4 or 12.1.0.2.\n\n  * __ol6.7-base-0.0.1__ - For Oracle Linux 6.7 with Unbreakable Enterprise Kernel (UEK) Release 3.\n

        :return: The image of this Instance.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Instance.
        The image used to boot the instance. The available images are:\n\n  * __ol7.1-base-0.0.1__ - For Oracle Linux 7.1.\n\n  * __ol6.7-oracledbee_12.1.0.2/11.2.0.4-0.0.1__ - For Oracle Linux 6.7 with Oracle Database Enterprise Edition 11.2.0.4 or 12.1.0.2.\n\n  * __ol6.7-base-0.0.1__ - For Oracle Linux 6.7 with Unbreakable Enterprise Kernel (UEK) Release 3.\n

        :param image: The image of this Instance.
        :type: str
        """
        self._image = image

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
        Gets the region of this Instance.
        The region that contains the Availability Domain the instance is running in.

        :return: The region of this Instance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Instance.
        The region that contains the Availability Domain the instance is running in.

        :param region: The region of this Instance.
        :type: str
        """
        self._region = region

    @property
    def shape(self):
        """
        Gets the shape of this Instance.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance.

        :return: The shape of this Instance.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this Instance.
        The shape of the instance. The shape determines the number of CPUs and the amount of memory allocated to the instance.

        :param shape: The shape of this Instance.
        :type: str
        """
        self._shape = shape

    @property
    def state(self):
        """
        Gets the state of this Instance.
        The current state of the instance.

        :return: The state of this Instance.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Instance.
        The current state of the instance.

        :param state: The state of this Instance.
        :type: str
        """
        allowed_values = ["PROVISIONING", "RUNNING", "STARTING", "STOPPING", "STOPPED", "TERMINATING", "TERMINATED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def time_created(self):
        """
        Gets the time_created of this Instance.
        The date and time the instance was created.

        :return: The time_created of this Instance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Instance.
        The date and time the instance was created.

        :param time_created: The time_created of this Instance.
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

