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


class CreateIPSecConnectionDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'cpe_id': 'str',
            'display_name': 'str',
            'drg_id': 'str',
            'static_routes': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cpe_id': 'cpeId',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'static_routes': 'staticRoutes'
        }

        self._compartment_id = None
        self._cpe_id = None
        self._display_name = None
        self._drg_id = None
        self._static_routes = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateIPSecConnectionDetails.
        The OCID of the compartment to contain the IPSec connection.

        :return: The compartment_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIPSecConnectionDetails.
        The OCID of the compartment to contain the IPSec connection.

        :param compartment_id: The compartment_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpe_id(self):
        """
        Gets the cpe_id of this CreateIPSecConnectionDetails.
        The OCID of the CPE.

        :return: The cpe_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._cpe_id

    @cpe_id.setter
    def cpe_id(self, cpe_id):
        """
        Sets the cpe_id of this CreateIPSecConnectionDetails.
        The OCID of the CPE.

        :param cpe_id: The cpe_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._cpe_id = cpe_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateIPSecConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.

        :return: The display_name of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateIPSecConnectionDetails.
        A user-friendly name. Does not have to be unique, and it's not changeable.

        :param display_name: The display_name of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        Gets the drg_id of this CreateIPSecConnectionDetails.
        The OCID of the DRG.

        :return: The drg_id of this CreateIPSecConnectionDetails.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this CreateIPSecConnectionDetails.
        The OCID of the DRG.

        :param drg_id: The drg_id of this CreateIPSecConnectionDetails.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def static_routes(self):
        """
        Gets the static_routes of this CreateIPSecConnectionDetails.
        Static routes to the CPE.

        :return: The static_routes of this CreateIPSecConnectionDetails.
        :rtype: list[str]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """
        Sets the static_routes of this CreateIPSecConnectionDetails.
        Static routes to the CPE.

        :param static_routes: The static_routes of this CreateIPSecConnectionDetails.
        :type: list[str]
        """
        self._static_routes = static_routes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
