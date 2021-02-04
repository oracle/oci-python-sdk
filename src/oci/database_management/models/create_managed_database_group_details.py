# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagedDatabaseGroupDetails(object):
    """
    The details required to create a Managed Database Group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagedDatabaseGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateManagedDatabaseGroupDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateManagedDatabaseGroupDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagedDatabaseGroupDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId'
        }

        self._name = None
        self._description = None
        self._compartment_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateManagedDatabaseGroupDetails.
        The name of the Managed Database Group. Valid characters are uppercase or
        lowercase letters, numbers, and \"_\". The name of the Managed Database Group
        cannot be modified. It must be unique in the compartment and must begin with
        an alphabetic character.


        :return: The name of this CreateManagedDatabaseGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateManagedDatabaseGroupDetails.
        The name of the Managed Database Group. Valid characters are uppercase or
        lowercase letters, numbers, and \"_\". The name of the Managed Database Group
        cannot be modified. It must be unique in the compartment and must begin with
        an alphabetic character.


        :param name: The name of this CreateManagedDatabaseGroupDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateManagedDatabaseGroupDetails.
        The information specified by the user about the Managed Database Group.


        :return: The description of this CreateManagedDatabaseGroupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateManagedDatabaseGroupDetails.
        The information specified by the user about the Managed Database Group.


        :param description: The description of this CreateManagedDatabaseGroupDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagedDatabaseGroupDetails.
        The `OCID`__ of the compartment
        in which the Managed Database Group resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateManagedDatabaseGroupDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagedDatabaseGroupDetails.
        The `OCID`__ of the compartment
        in which the Managed Database Group resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateManagedDatabaseGroupDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
