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

class IPSecConnection(object):

    def __init__(self):
        """
        IPSecConnection - a model defined in Swagger
        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cpe_id': 'str',
            'display_name': 'str',
            'drg_id': 'str',
            'id': 'str',
            'state': 'str',
            'static_routes': 'list[str]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cpe_id': 'cpeId',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'id': 'id',
            'state': 'state',
            'static_routes': 'staticRoutes',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._cpe_id = None
        self._display_name = None
        self._drg_id = None
        self._id = None
        self._state = None
        self._static_routes = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this IPSecConnection.
        The OCID of the compartment containing the IPsec connection.

        :return: The compartment_id of this IPSecConnection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnection.
        The OCID of the compartment containing the IPsec connection.

        :param compartment_id: The compartment_id of this IPSecConnection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpe_id(self):
        """
        Gets the cpe_id of this IPSecConnection.
        The OCID of the CPE.

        :return: The cpe_id of this IPSecConnection.
        :rtype: str
        """
        return self._cpe_id

    @cpe_id.setter
    def cpe_id(self, cpe_id):
        """
        Sets the cpe_id of this IPSecConnection.
        The OCID of the CPE.

        :param cpe_id: The cpe_id of this IPSecConnection.
        :type: str
        """
        self._cpe_id = cpe_id

    @property
    def display_name(self):
        """
        Gets the display_name of this IPSecConnection.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :return: The display_name of this IPSecConnection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IPSecConnection.
        A user-friendly name. Does not have to be unique, and it's unchangeable.\n

        :param display_name: The display_name of this IPSecConnection.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        Gets the drg_id of this IPSecConnection.
        The OCID of the DRG.

        :return: The drg_id of this IPSecConnection.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this IPSecConnection.
        The OCID of the DRG.

        :param drg_id: The drg_id of this IPSecConnection.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def id(self):
        """
        Gets the id of this IPSecConnection.
        The IPsec connection's Oracle ID (OCID).

        :return: The id of this IPSecConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnection.
        The IPsec connection's Oracle ID (OCID).

        :param id: The id of this IPSecConnection.
        :type: str
        """
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this IPSecConnection.
        The IPsec connection's current state.

        :return: The state of this IPSecConnection.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this IPSecConnection.
        The IPsec connection's current state.

        :param state: The state of this IPSecConnection.
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
    def static_routes(self):
        """
        Gets the static_routes of this IPSecConnection.
        Static routes to the CPE.

        :return: The static_routes of this IPSecConnection.
        :rtype: list[str]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """
        Sets the static_routes of this IPSecConnection.
        Static routes to the CPE.

        :param static_routes: The static_routes of this IPSecConnection.
        :type: list[str]
        """
        self._static_routes = static_routes

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnection.
        Date and time the IPsec connection was created.

        :return: The time_created of this IPSecConnection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnection.
        Date and time the IPsec connection was created.

        :param time_created: The time_created of this IPSecConnection.
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

