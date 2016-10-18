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


class Cpe(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'ip_address': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'ip_address': 'ipAddress',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._ip_address = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Cpe.
        The OCID of the compartment containing the CPE.

        :return: The compartment_id of this Cpe.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Cpe.
        The OCID of the compartment containing the CPE.

        :param compartment_id: The compartment_id of this Cpe.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this Cpe.
        A user-friendly name. Does not have to be unique, and it's changeable.

        :return: The display_name of this Cpe.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Cpe.
        A user-friendly name. Does not have to be unique, and it's changeable.

        :param display_name: The display_name of this Cpe.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Cpe.
        The CPE's Oracle ID (OCID).

        :return: The id of this Cpe.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Cpe.
        The CPE's Oracle ID (OCID).

        :param id: The id of this Cpe.
        :type: str
        """
        self._id = id

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Cpe.
        The public IP address of the on-premise router.

        :return: The ip_address of this Cpe.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Cpe.
        The public IP address of the on-premise router.

        :param ip_address: The ip_address of this Cpe.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def time_created(self):
        """
        Gets the time_created of this Cpe.
        The date and time the CPE was created.

        :return: The time_created of this Cpe.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Cpe.
        The date and time the CPE was created.

        :param time_created: The time_created of this Cpe.
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
