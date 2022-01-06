# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbManagementPrivateEndpointDetails(object):
    """
    The details used to update a Database Management private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbManagementPrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateDbManagementPrivateEndpointDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateDbManagementPrivateEndpointDetails.
        :type description: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateDbManagementPrivateEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'nsg_ids': 'nsgIds'
        }

        self._name = None
        self._description = None
        self._nsg_ids = None

    @property
    def name(self):
        """
        Gets the name of this UpdateDbManagementPrivateEndpointDetails.
        The display name of the private endpoint.


        :return: The name of this UpdateDbManagementPrivateEndpointDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateDbManagementPrivateEndpointDetails.
        The display name of the private endpoint.


        :param name: The name of this UpdateDbManagementPrivateEndpointDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateDbManagementPrivateEndpointDetails.
        The description of the private endpoint.


        :return: The description of this UpdateDbManagementPrivateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDbManagementPrivateEndpointDetails.
        The description of the private endpoint.


        :param description: The description of this UpdateDbManagementPrivateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateDbManagementPrivateEndpointDetails.
        The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.


        :return: The nsg_ids of this UpdateDbManagementPrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateDbManagementPrivateEndpointDetails.
        The OCIDs of the Network Security Groups to which the Database Management private endpoint belongs.


        :param nsg_ids: The nsg_ids of this UpdateDbManagementPrivateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
