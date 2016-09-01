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

class VolumeAttachment(object):

    def __init__(self):

        self.swagger_types = {
            'attachment_type': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'attachment_type': 'attachmentType',
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'volume_id': 'volumeId'
        }

        self._attachment_type = None
        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._volume_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['attachmentType']

        if type == 'iscsi':
               return 'IScsiVolumeAttachment'

        raise ValueError('Could not resolve subtype type based on the object dictionary.')

    @property
    def attachment_type(self):
        """
        Gets the attachment_type of this VolumeAttachment.
        The type of volume attachment.

        :return: The attachment_type of this VolumeAttachment.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """
        Sets the attachment_type of this VolumeAttachment.
        The type of volume attachment.

        :param attachment_type: The attachment_type of this VolumeAttachment.
        :type: str
        """
        self._attachment_type = attachment_type

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this VolumeAttachment.
        The Availability Domain of the instance.

        :return: The availability_domain of this VolumeAttachment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VolumeAttachment.
        The Availability Domain of the instance.

        :param availability_domain: The availability_domain of this VolumeAttachment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VolumeAttachment.
        The OCID of the compartment.

        :return: The compartment_id of this VolumeAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeAttachment.
        The OCID of the compartment.

        :param compartment_id: The compartment_id of this VolumeAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VolumeAttachment.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :return: The display_name of this VolumeAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeAttachment.
        A user-friendly name. Does not have to be unique, and it's not changeable.\n

        :param display_name: The display_name of this VolumeAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this VolumeAttachment.
        The OCID of the volume attachment.

        :return: The id of this VolumeAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeAttachment.
        The OCID of the volume attachment.

        :param id: The id of this VolumeAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this VolumeAttachment.
        The OCID of the instance the volume is attached to.

        :return: The instance_id of this VolumeAttachment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this VolumeAttachment.
        The OCID of the instance the volume is attached to.

        :param instance_id: The instance_id of this VolumeAttachment.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VolumeAttachment.
        The current state of the volume attachment.

        :return: The lifecycle_state of this VolumeAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VolumeAttachment.
        The current state of the volume attachment.

        :param lifecycle_state: The lifecycle_state of this VolumeAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this VolumeAttachment.
        The date and time the volume was created, in the format defined by RFC3339.\n\nExample: `2016-03-24T17:43:01.389+0000`\n

        :return: The time_created of this VolumeAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeAttachment.
        The date and time the volume was created, in the format defined by RFC3339.\n\nExample: `2016-03-24T17:43:01.389+0000`\n

        :param time_created: The time_created of this VolumeAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def volume_id(self):
        """
        Gets the volume_id of this VolumeAttachment.
        The OCID of the volume.

        :return: The volume_id of this VolumeAttachment.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this VolumeAttachment.
        The OCID of the volume.

        :param volume_id: The volume_id of this VolumeAttachment.
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

