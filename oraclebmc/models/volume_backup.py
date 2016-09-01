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

class VolumeBackup(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'size_in_m_bs': 'int',
            'time_created': 'datetime',
            'time_request_received': 'datetime',
            'unique_size_in_mbs': 'int',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'size_in_m_bs': 'sizeInMBs',
            'time_created': 'timeCreated',
            'time_request_received': 'timeRequestReceived',
            'unique_size_in_mbs': 'uniqueSizeInMbs',
            'volume_id': 'volumeId'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._size_in_m_bs = None
        self._time_created = None
        self._time_request_received = None
        self._unique_size_in_mbs = None
        self._volume_id = None


    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VolumeBackup.
        The OCID of the compartment that contains the volumeBackup.

        :return: The compartment_id of this VolumeBackup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeBackup.
        The OCID of the compartment that contains the volumeBackup.

        :param compartment_id: The compartment_id of this VolumeBackup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VolumeBackup.
        A user-friendly name for the volumeBackup. Does not have to be unique and it's changeable.

        :return: The display_name of this VolumeBackup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeBackup.
        A user-friendly name for the volumeBackup. Does not have to be unique and it's changeable.

        :param display_name: The display_name of this VolumeBackup.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this VolumeBackup.
        The Oracle Cloud ID (OCID) that uniquely identifies the volumeBackup.

        :return: The id of this VolumeBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeBackup.
        The Oracle Cloud ID (OCID) that uniquely identifies the volumeBackup.

        :param id: The id of this VolumeBackup.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VolumeBackup.
        The current state of a volumeBackup.

        :return: The lifecycle_state of this VolumeBackup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VolumeBackup.
        The current state of a volumeBackup.

        :param lifecycle_state: The lifecycle_state of this VolumeBackup.
        :type: str
        """
        allowed_values = ["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_m_bs(self):
        """
        Gets the size_in_m_bs of this VolumeBackup.
        The size of the volumeBackup in MBs.

        :return: The size_in_m_bs of this VolumeBackup.
        :rtype: int
        """
        return self._size_in_m_bs

    @size_in_m_bs.setter
    def size_in_m_bs(self, size_in_m_bs):
        """
        Sets the size_in_m_bs of this VolumeBackup.
        The size of the volumeBackup in MBs.

        :param size_in_m_bs: The size_in_m_bs of this VolumeBackup.
        :type: int
        """
        self._size_in_m_bs = size_in_m_bs

    @property
    def time_created(self):
        """
        Gets the time_created of this VolumeBackup.
        The date and time the volumeBackup was created. This is the time actual snapshot of the volume\ndata was taken. Format defined by RFC3339.\n

        :return: The time_created of this VolumeBackup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeBackup.
        The date and time the volumeBackup was created. This is the time actual snapshot of the volume\ndata was taken. Format defined by RFC3339.\n

        :param time_created: The time_created of this VolumeBackup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_request_received(self):
        """
        Gets the time_request_received of this VolumeBackup.
        The date and time the request for creating volumeBackup was received. Format defined by RFC3339.

        :return: The time_request_received of this VolumeBackup.
        :rtype: datetime
        """
        return self._time_request_received

    @time_request_received.setter
    def time_request_received(self, time_request_received):
        """
        Sets the time_request_received of this VolumeBackup.
        The date and time the request for creating volumeBackup was received. Format defined by RFC3339.

        :param time_request_received: The time_request_received of this VolumeBackup.
        :type: datetime
        """
        self._time_request_received = time_request_received

    @property
    def unique_size_in_mbs(self):
        """
        Gets the unique_size_in_mbs of this VolumeBackup.
        The size of the volumeBackup volume in MBs.

        :return: The unique_size_in_mbs of this VolumeBackup.
        :rtype: int
        """
        return self._unique_size_in_mbs

    @unique_size_in_mbs.setter
    def unique_size_in_mbs(self, unique_size_in_mbs):
        """
        Sets the unique_size_in_mbs of this VolumeBackup.
        The size of the volumeBackup volume in MBs.

        :param unique_size_in_mbs: The unique_size_in_mbs of this VolumeBackup.
        :type: int
        """
        self._unique_size_in_mbs = unique_size_in_mbs

    @property
    def volume_id(self):
        """
        Gets the volume_id of this VolumeBackup.
        A OCID that uniquely identifies the volume.

        :return: The volume_id of this VolumeBackup.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this VolumeBackup.
        A OCID that uniquely identifies the volume.

        :param volume_id: The volume_id of this VolumeBackup.
        :type: str
        """
        self._volume_id = volume_id

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

