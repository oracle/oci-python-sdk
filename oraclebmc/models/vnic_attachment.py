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

class VnicAttachment(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'state': 'str',
            'subnet_id': 'str',
            'time_created': 'datetime',
            'vnic_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'state': 'state',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated',
            'vnic_id': 'vnicId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._state = None
        self._subnet_id = None
        self._time_created = None
        self._vnic_id = None


    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this VnicAttachment.
        The Availability Domain of an instance.

        :return: The availability_domain of this VnicAttachment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VnicAttachment.
        The Availability Domain of an instance.

        :param availability_domain: The availability_domain of this VnicAttachment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VnicAttachment.
        The OCID of the compartment.

        :return: The compartment_id of this VnicAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VnicAttachment.
        The OCID of the compartment.

        :param compartment_id: The compartment_id of this VnicAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VnicAttachment.
        The name of the VNIC attachment.

        :return: The display_name of this VnicAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VnicAttachment.
        The name of the VNIC attachment.

        :param display_name: The display_name of this VnicAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this VnicAttachment.
        The OCID of the VNIC attachment.

        :return: The id of this VnicAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VnicAttachment.
        The OCID of the VNIC attachment.

        :param id: The id of this VnicAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this VnicAttachment.
        The OCID of the instance.

        :return: The instance_id of this VnicAttachment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this VnicAttachment.
        The OCID of the instance.

        :param instance_id: The instance_id of this VnicAttachment.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def state(self):
        """
        Gets the state of this VnicAttachment.
        The current state of the VNIC attachment.

        :return: The state of this VnicAttachment.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this VnicAttachment.
        The current state of the VNIC attachment.

        :param state: The state of this VnicAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this VnicAttachment.
        The OCID of the subnet of the VNIC.

        :return: The subnet_id of this VnicAttachment.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this VnicAttachment.
        The OCID of the subnet of the VNIC.

        :param subnet_id: The subnet_id of this VnicAttachment.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this VnicAttachment.


        :return: The time_created of this VnicAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VnicAttachment.


        :param time_created: The time_created of this VnicAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vnic_id(self):
        """
        Gets the vnic_id of this VnicAttachment.
        The vnic identifier

        :return: The vnic_id of this VnicAttachment.
        :rtype: str
        """
        return self._vnic_id

    @vnic_id.setter
    def vnic_id(self, vnic_id):
        """
        Sets the vnic_id of this VnicAttachment.
        The vnic identifier

        :param vnic_id: The vnic_id of this VnicAttachment.
        :type: str
        """
        self._vnic_id = vnic_id

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

