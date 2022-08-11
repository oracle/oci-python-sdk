# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EntityDetails(object):
    """
    Entities Details for a data source
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EntityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this EntityDetails.
        :type display_name: str

        :param value:
            The value to assign to the value property of this EntityDetails.
        :type value: str

        :param type:
            The value to assign to the type property of this EntityDetails.
        :type type: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'value': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'value': 'value',
            'type': 'type'
        }

        self._display_name = None
        self._value = None
        self._type = None

    @property
    def display_name(self):
        """
        Gets the display_name of this EntityDetails.
        The display name of entity


        :return: The display_name of this EntityDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EntityDetails.
        The display name of entity


        :param display_name: The display_name of this EntityDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def value(self):
        """
        Gets the value of this EntityDetails.
        The entity value


        :return: The value of this EntityDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this EntityDetails.
        The entity value


        :param value: The value of this EntityDetails.
        :type: str
        """
        self._value = value

    @property
    def type(self):
        """
        Gets the type of this EntityDetails.
        Type of entity


        :return: The type of this EntityDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EntityDetails.
        Type of entity


        :param type: The type of this EntityDetails.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
