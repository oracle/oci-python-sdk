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

class Volume(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'size_in_m_bs': 'int',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'size_in_m_bs': 'sizeInMBs',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._size_in_m_bs = None
        self._time_created = None


    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Volume.
        The Availability Domain of the volume.

        :return: The availability_domain of this Volume.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Volume.
        The Availability Domain of the volume.

        :param availability_domain: The availability_domain of this Volume.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Volume.
        The OCID of the compartment that contains the volume.

        :return: The compartment_id of this Volume.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Volume.
        The OCID of the compartment that contains the volume.

        :param compartment_id: The compartment_id of this Volume.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Volume.
        A user-friendly name. Does not have to be unique, and it's changeable.\n

        :return: The display_name of this Volume.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Volume.
        A user-friendly name. Does not have to be unique, and it's changeable.\n

        :param display_name: The display_name of this Volume.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Volume.
        The Oracle Cloud ID (OCID) that uniquely identifies the volume.

        :return: The id of this Volume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Volume.
        The Oracle Cloud ID (OCID) that uniquely identifies the volume.

        :param id: The id of this Volume.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Volume.
        The current state of a volume.

        :return: The lifecycle_state of this Volume.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Volume.
        The current state of a volume.

        :param lifecycle_state: The lifecycle_state of this Volume.
        :type: str
        """
        allowed_values = ["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_m_bs(self):
        """
        Gets the size_in_m_bs of this Volume.
        The size of the volume in MBs.

        :return: The size_in_m_bs of this Volume.
        :rtype: int
        """
        return self._size_in_m_bs

    @size_in_m_bs.setter
    def size_in_m_bs(self, size_in_m_bs):
        """
        Sets the size_in_m_bs of this Volume.
        The size of the volume in MBs.

        :param size_in_m_bs: The size_in_m_bs of this Volume.
        :type: int
        """
        self._size_in_m_bs = size_in_m_bs

    @property
    def time_created(self):
        """
        Gets the time_created of this Volume.
        The date and time the volume was created. Format defined by RFC3339.

        :return: The time_created of this Volume.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Volume.
        The date and time the volume was created. Format defined by RFC3339.

        :param time_created: The time_created of this Volume.
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

