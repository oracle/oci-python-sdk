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


class CreateCompartmentDetails(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description'
        }

        self._compartment_id = None
        self._name = None
        self._description = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateCompartmentDetails.
        The OCID of the tenancy containing the compartment.

        :return: The compartment_id of this CreateCompartmentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateCompartmentDetails.
        The OCID of the tenancy containing the compartment.

        :param compartment_id: The compartment_id of this CreateCompartmentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        Gets the name of this CreateCompartmentDetails.
        A unique, unchangeable name you assign to the compartment during creation. Must be unique across all
        compartments in the tenancy.

        :return: The name of this CreateCompartmentDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateCompartmentDetails.
        A unique, unchangeable name you assign to the compartment during creation. Must be unique across all
        compartments in the tenancy.

        :param name: The name of this CreateCompartmentDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateCompartmentDetails.
        The non-unique, changeable description you assign to the compartment during creation.

        :return: The description of this CreateCompartmentDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCompartmentDetails.
        The non-unique, changeable description you assign to the compartment during creation.

        :param description: The description of this CreateCompartmentDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
