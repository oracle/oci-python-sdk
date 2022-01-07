# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsUserPassword(object):
    """
    The user password.
    """

    #: A constant which can be used with the value_type property of a DatabaseToolsUserPassword.
    #: This constant has a value of "SECRETID"
    VALUE_TYPE_SECRETID = "SECRETID"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsUserPassword object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_tools.models.DatabaseToolsUserPasswordSecretId`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value_type:
            The value to assign to the value_type property of this DatabaseToolsUserPassword.
            Allowed values for this property are: "SECRETID", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_type: str

        """
        self.swagger_types = {
            'value_type': 'str'
        }

        self.attribute_map = {
            'value_type': 'valueType'
        }

        self._value_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['valueType']

        if type == 'SECRETID':
            return 'DatabaseToolsUserPasswordSecretId'
        else:
            return 'DatabaseToolsUserPassword'

    @property
    def value_type(self):
        """
        **[Required]** Gets the value_type of this DatabaseToolsUserPassword.
        The value type of the user password.

        Allowed values for this property are: "SECRETID", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The value_type of this DatabaseToolsUserPassword.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this DatabaseToolsUserPassword.
        The value type of the user password.


        :param value_type: The value_type of this DatabaseToolsUserPassword.
        :type: str
        """
        allowed_values = ["SECRETID"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            value_type = 'UNKNOWN_ENUM_VALUE'
        self._value_type = value_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
