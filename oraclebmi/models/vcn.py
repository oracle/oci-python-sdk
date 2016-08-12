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

class Vcn(object):

    def __init__(self):

        self.swagger_types = {
            'cidr_block': 'str',
            'compartment_id': 'str',
            'default_route_table_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'compartment_id': 'compartmentId',
            'default_route_table_id': 'defaultRouteTableId',
            'display_name': 'displayName',
            'id': 'id',
            'state': 'state',
            'time_created': 'timeCreated'
        }

        self._cidr_block = None
        self._compartment_id = None
        self._default_route_table_id = None
        self._display_name = None
        self._id = None
        self._state = None
        self._time_created = None


    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this Vcn.
        The CIDR IP address block of the VCN.

        :return: The cidr_block of this Vcn.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this Vcn.
        The CIDR IP address block of the VCN.

        :param cidr_block: The cidr_block of this Vcn.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Vcn.
        The OCID of the compartment containing the VCN.

        :return: The compartment_id of this Vcn.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Vcn.
        The OCID of the compartment containing the VCN.

        :param compartment_id: The compartment_id of this Vcn.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def default_route_table_id(self):
        """
        Gets the default_route_table_id of this Vcn.
        The OCID for the VCN's default route table.

        :return: The default_route_table_id of this Vcn.
        :rtype: str
        """
        return self._default_route_table_id

    @default_route_table_id.setter
    def default_route_table_id(self, default_route_table_id):
        """
        Sets the default_route_table_id of this Vcn.
        The OCID for the VCN's default route table.

        :param default_route_table_id: The default_route_table_id of this Vcn.
        :type: str
        """
        self._default_route_table_id = default_route_table_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Vcn.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :return: The display_name of this Vcn.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Vcn.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :param display_name: The display_name of this Vcn.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Vcn.
        The VCN's Oracle ID (OCID).

        :return: The id of this Vcn.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vcn.
        The VCN's Oracle ID (OCID).

        :param id: The id of this Vcn.
        :type: str
        """
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this Vcn.
        The VCN's current state.

        :return: The state of this Vcn.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Vcn.
        The VCN's current state.

        :param state: The state of this Vcn.
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
        Gets the time_created of this Vcn.
        Date and time the VCN was created.

        :return: The time_created of this Vcn.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Vcn.
        Date and time the VCN was created.

        :param time_created: The time_created of this Vcn.
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

