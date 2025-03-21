# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Compartment(object):
    """
    Compartment model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Compartment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Compartment.
        :type id: str

        :param name:
            The value to assign to the name property of this Compartment.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this Compartment.
        :type display_name: str

        :param full_name:
            The value to assign to the full_name property of this Compartment.
        :type full_name: str

        :param parent_compartment_id:
            The value to assign to the parent_compartment_id property of this Compartment.
        :type parent_compartment_id: str

        :param status:
            The value to assign to the status property of this Compartment.
        :type status: oci.identity_data_plane.models.EntityStatus

        :param property_map:
            The value to assign to the property_map property of this Compartment.
        :type property_map: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'full_name': 'str',
            'parent_compartment_id': 'str',
            'status': 'EntityStatus',
            'property_map': 'dict(str, str)'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'full_name': 'fullName',
            'parent_compartment_id': 'parentCompartmentId',
            'status': 'status',
            'property_map': 'propertyMap'
        }
        self._id = None
        self._name = None
        self._display_name = None
        self._full_name = None
        self._parent_compartment_id = None
        self._status = None
        self._property_map = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Compartment.
        The id of the compartment.


        :return: The id of this Compartment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Compartment.
        The id of the compartment.


        :param id: The id of this Compartment.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Compartment.
        The name of the compartment.


        :return: The name of this Compartment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Compartment.
        The name of the compartment.


        :param name: The name of this Compartment.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Compartment.
        The display name of the compartment.


        :return: The display_name of this Compartment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Compartment.
        The display name of the compartment.


        :param display_name: The display_name of this Compartment.
        :type: str
        """
        self._display_name = display_name

    @property
    def full_name(self):
        """
        **[Required]** Gets the full_name of this Compartment.
        The full name of the compartment.


        :return: The full_name of this Compartment.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this Compartment.
        The full name of the compartment.


        :param full_name: The full_name of this Compartment.
        :type: str
        """
        self._full_name = full_name

    @property
    def parent_compartment_id(self):
        """
        **[Required]** Gets the parent_compartment_id of this Compartment.
        The id of the parent compartment.


        :return: The parent_compartment_id of this Compartment.
        :rtype: str
        """
        return self._parent_compartment_id

    @parent_compartment_id.setter
    def parent_compartment_id(self, parent_compartment_id):
        """
        Sets the parent_compartment_id of this Compartment.
        The id of the parent compartment.


        :param parent_compartment_id: The parent_compartment_id of this Compartment.
        :type: str
        """
        self._parent_compartment_id = parent_compartment_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this Compartment.
        The status of the compartment.


        :return: The status of this Compartment.
        :rtype: oci.identity_data_plane.models.EntityStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Compartment.
        The status of the compartment.


        :param status: The status of this Compartment.
        :type: oci.identity_data_plane.models.EntityStatus
        """
        self._status = status

    @property
    def property_map(self):
        """
        **[Required]** Gets the property_map of this Compartment.
        The extended properties.


        :return: The property_map of this Compartment.
        :rtype: dict(str, str)
        """
        return self._property_map

    @property_map.setter
    def property_map(self, property_map):
        """
        Sets the property_map of this Compartment.
        The extended properties.


        :param property_map: The property_map of this Compartment.
        :type: dict(str, str)
        """
        self._property_map = property_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
