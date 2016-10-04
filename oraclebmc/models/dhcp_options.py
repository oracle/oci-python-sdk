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


from ..util import formatted_flat_dict


class DhcpOptions(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'options': 'list[DhcpOption]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'options': 'options',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._options = None
        self._time_created = None


    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DhcpOptions.
        The OCID of the compartment containing the set of DHCP options.

        :return: The compartment_id of this DhcpOptions.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DhcpOptions.
        The OCID of the compartment containing the set of DHCP options.

        :param compartment_id: The compartment_id of this DhcpOptions.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this DhcpOptions.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :return: The display_name of this DhcpOptions.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DhcpOptions.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :param display_name: The display_name of this DhcpOptions.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this DhcpOptions.
        Oracle ID (OCID) for the set of DHCP options.

        :return: The id of this DhcpOptions.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DhcpOptions.
        Oracle ID (OCID) for the set of DHCP options.

        :param id: The id of this DhcpOptions.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DhcpOptions.
        The current state of the set of DHCP options.

        :return: The lifecycle_state of this DhcpOptions.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DhcpOptions.
        The current state of the set of DHCP options.

        :param lifecycle_state: The lifecycle_state of this DhcpOptions.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if lifecycle_state not in allowed_values:
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def options(self):
        """
        Gets the options of this DhcpOptions.
        The collection of individual DHCP options.

        :return: The options of this DhcpOptions.
        :rtype: list[DhcpOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this DhcpOptions.
        The collection of individual DHCP options.

        :param options: The options of this DhcpOptions.
        :type: list[DhcpOption]
        """
        self._options = options

    @property
    def time_created(self):
        """
        Gets the time_created of this DhcpOptions.
        Date and time the set of DHCP options was created.

        :return: The time_created of this DhcpOptions.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DhcpOptions.
        Date and time the set of DHCP options was created.

        :param time_created: The time_created of this DhcpOptions.
        :type: datetime
        """
        self._time_created = time_created


    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

