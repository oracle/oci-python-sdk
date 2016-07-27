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

class Vnic(object):

    def __init__(self):
        """
        Vnic - a model defined in Swagger
        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'overlay_ip': 'str',
            'public_ip': 'str',
            'state': 'str',
            'subnet_id': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'overlay_ip': 'overlayIp',
            'public_ip': 'publicIp',
            'state': 'state',
            'subnet_id': 'subnetId',
            'time_created': 'timeCreated'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._overlay_ip = None
        self._public_ip = None
        self._state = None
        self._subnet_id = None
        self._time_created = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Vnic.
        The VNIC's Availability Domain.

        :return: The availability_domain of this Vnic.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Vnic.
        The VNIC's Availability Domain.

        :param availability_domain: The availability_domain of this Vnic.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Vnic.
        The OCID of the compartment containing the VNIC.

        :return: The compartment_id of this Vnic.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vnic.
        The OCID of the compartment containing the VNIC.

        :param compartment_id: The compartment_id of this Vnic.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :return: The display_name of this Vnic.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vnic.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :param display_name: The display_name of this Vnic.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Vnic.
        The VNIC's Oracle ID (OCID).

        :return: The id of this Vnic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vnic.
        The VNIC's Oracle ID (OCID).

        :param id: The id of this Vnic.
        :type: str
        """
        self._id = id

    @property
    def overlay_ip(self):
        """
        Gets the overlay_ip of this Vnic.
        The private IP addresses of the VNIC, which is within the VNIC subnet\nand is accessible within the VCN.\n

        :return: The overlay_ip of this Vnic.
        :rtype: str
        """
        return self._overlay_ip

    @overlay_ip.setter
    def overlay_ip(self, overlay_ip):
        """
        Sets the overlay_ip of this Vnic.
        The private IP addresses of the VNIC, which is within the VNIC subnet\nand is accessible within the VCN.\n

        :param overlay_ip: The overlay_ip of this Vnic.
        :type: str
        """
        self._overlay_ip = overlay_ip

    @property
    def public_ip(self):
        """
        Gets the public_ip of this Vnic.
        The public IP address of the VNIC, which Oracle performs NAT for at the gateway.\n

        :return: The public_ip of this Vnic.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """
        Sets the public_ip of this Vnic.
        The public IP address of the VNIC, which Oracle performs NAT for at the gateway.\n

        :param public_ip: The public_ip of this Vnic.
        :type: str
        """
        self._public_ip = public_ip

    @property
    def state(self):
        """
        Gets the state of this Vnic.
        The current state of the VNIC

        :return: The state of this Vnic.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Vnic.
        The current state of the VNIC

        :param state: The state of this Vnic.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )
        self._state = state

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this Vnic.
        The OCID of the subnet the VNIC is in.

        :return: The subnet_id of this Vnic.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Vnic.
        The OCID of the subnet the VNIC is in.

        :param subnet_id: The subnet_id of this Vnic.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Vnic.
        Date and time the VNIC was created.

        :return: The time_created of this Vnic.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vnic.
        Date and time the VNIC was created.

        :param time_created: The time_created of this Vnic.
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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if objects are not equal
        """
        return not self == other

