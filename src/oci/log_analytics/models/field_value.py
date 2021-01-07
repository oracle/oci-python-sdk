# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FieldValue(object):
    """
    Field value representing and entry in a list-of-values field.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FieldValue object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_value:
            The value to assign to the display_value property of this FieldValue.
        :type display_value: str

        :param internal_value:
            The value to assign to the internal_value property of this FieldValue.
        :type internal_value: object

        :param is_deleted:
            The value to assign to the is_deleted property of this FieldValue.
        :type is_deleted: bool

        """
        self.swagger_types = {
            'display_value': 'str',
            'internal_value': 'object',
            'is_deleted': 'bool'
        }

        self.attribute_map = {
            'display_value': 'displayValue',
            'internal_value': 'internalValue',
            'is_deleted': 'isDeleted'
        }

        self._display_value = None
        self._internal_value = None
        self._is_deleted = None

    @property
    def display_value(self):
        """
        Gets the display_value of this FieldValue.
        Display representation of the field value.


        :return: The display_value of this FieldValue.
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """
        Sets the display_value of this FieldValue.
        Display representation of the field value.


        :param display_value: The display_value of this FieldValue.
        :type: str
        """
        self._display_value = display_value

    @property
    def internal_value(self):
        """
        Gets the internal_value of this FieldValue.
        Internal representation of the field value.


        :return: The internal_value of this FieldValue.
        :rtype: object
        """
        return self._internal_value

    @internal_value.setter
    def internal_value(self, internal_value):
        """
        Sets the internal_value of this FieldValue.
        Internal representation of the field value.


        :param internal_value: The internal_value of this FieldValue.
        :type: object
        """
        self._internal_value = internal_value

    @property
    def is_deleted(self):
        """
        Gets the is_deleted of this FieldValue.
        Denotes if this list-of-values value has been marked as deleted.


        :return: The is_deleted of this FieldValue.
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """
        Sets the is_deleted of this FieldValue.
        Denotes if this list-of-values value has been marked as deleted.


        :param is_deleted: The is_deleted of this FieldValue.
        :type: bool
        """
        self._is_deleted = is_deleted

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
