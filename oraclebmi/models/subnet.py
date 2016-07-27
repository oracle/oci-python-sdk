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

class Subnet(object):

    def __init__(self):
        """
        Subnet - a model defined in Swagger
        """
        self.swagger_types = {
            'availability_domain': 'str',
            'cidr_block': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'route_table_id': 'str',
            'state': 'str',
            'time_created': 'datetime',
            'vcn_id': 'str',
            'virtual_router_ip': 'str',
            'virtual_router_mac': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'route_table_id': 'routeTableId',
            'state': 'state',
            'time_created': 'timeCreated',
            'vcn_id': 'vcnId',
            'virtual_router_ip': 'virtualRouterIp',
            'virtual_router_mac': 'virtualRouterMac'
        }

        self._availability_domain = None
        self._cidr_block = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._route_table_id = None
        self._state = None
        self._time_created = None
        self._vcn_id = None
        self._virtual_router_ip = None
        self._virtual_router_mac = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this Subnet.
        The subnet's Availability Domain.

        :return: The availability_domain of this Subnet.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this Subnet.
        The subnet's Availability Domain.

        :param availability_domain: The availability_domain of this Subnet.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this Subnet.
        The subnet's CIDR block.

        :return: The cidr_block of this Subnet.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Subnet.
        The subnet's CIDR block.

        :param cidr_block: The cidr_block of this Subnet.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Subnet.
        The OCID of the compartment containing the subnet.

        :return: The compartment_id of this Subnet.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Subnet.
        The OCID of the compartment containing the subnet.

        :param compartment_id: The compartment_id of this Subnet.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Subnet.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :return: The display_name of this Subnet.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Subnet.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :param display_name: The display_name of this Subnet.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Subnet.
        The subnet's Oracle ID (OCID).

        :return: The id of this Subnet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subnet.
        The subnet's Oracle ID (OCID).

        :param id: The id of this Subnet.
        :type: str
        """
        self._id = id

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this Subnet.
        The OCID of the route table the subnet is using.

        :return: The route_table_id of this Subnet.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this Subnet.
        The OCID of the route table the subnet is using.

        :param route_table_id: The route_table_id of this Subnet.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def state(self):
        """
        Gets the state of this Subnet.
        The subnet's current state.

        :return: The state of this Subnet.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Subnet.
        The subnet's current state.

        :param state: The state of this Subnet.
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
    def time_created(self):
        """
        Gets the time_created of this Subnet.
        Date and time the subnet was created.

        :return: The time_created of this Subnet.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Subnet.
        Date and time the subnet was created.

        :param time_created: The time_created of this Subnet.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this Subnet.
        The OCID of the VCN the subnet is in.

        :return: The vcn_id of this Subnet.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this Subnet.
        The OCID of the VCN the subnet is in.

        :param vcn_id: The vcn_id of this Subnet.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def virtual_router_ip(self):
        """
        Gets the virtual_router_ip of this Subnet.
        The IP address of the virtual router.

        :return: The virtual_router_ip of this Subnet.
        :rtype: str
        """
        return self._virtual_router_ip

    @virtual_router_ip.setter
    def virtual_router_ip(self, virtual_router_ip):
        """
        Sets the virtual_router_ip of this Subnet.
        The IP address of the virtual router.

        :param virtual_router_ip: The virtual_router_ip of this Subnet.
        :type: str
        """
        self._virtual_router_ip = virtual_router_ip

    @property
    def virtual_router_mac(self):
        """
        Gets the virtual_router_mac of this Subnet.
        The MAC address of the virtual router.

        :return: The virtual_router_mac of this Subnet.
        :rtype: str
        """
        return self._virtual_router_mac

    @virtual_router_mac.setter
    def virtual_router_mac(self, virtual_router_mac):
        """
        Sets the virtual_router_mac of this Subnet.
        The MAC address of the virtual router.

        :param virtual_router_mac: The virtual_router_mac of this Subnet.
        :type: str
        """
        self._virtual_router_mac = virtual_router_mac

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

