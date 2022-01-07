# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UnsupportedDatabaseObject(object):
    """
    Database objects to exclude from migration
    """

    #: A constant which can be used with the type property of a UnsupportedDatabaseObject.
    #: This constant has a value of "GOLDEN_GATE"
    TYPE_GOLDEN_GATE = "GOLDEN_GATE"

    def __init__(self, **kwargs):
        """
        Initializes a new UnsupportedDatabaseObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UnsupportedDatabaseObject.
            Allowed values for this property are: "GOLDEN_GATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param owner:
            The value to assign to the owner property of this UnsupportedDatabaseObject.
        :type owner: str

        :param object_name:
            The value to assign to the object_name property of this UnsupportedDatabaseObject.
        :type object_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'owner': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'owner': 'owner',
            'object_name': 'objectName'
        }

        self._type = None
        self._owner = None
        self._object_name = None

    @property
    def type(self):
        """
        Gets the type of this UnsupportedDatabaseObject.
        Type of unsupported object

        Allowed values for this property are: "GOLDEN_GATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this UnsupportedDatabaseObject.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UnsupportedDatabaseObject.
        Type of unsupported object


        :param type: The type of this UnsupportedDatabaseObject.
        :type: str
        """
        allowed_values = ["GOLDEN_GATE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this UnsupportedDatabaseObject.
        Owner of the object (regular expression is allowed)


        :return: The owner of this UnsupportedDatabaseObject.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this UnsupportedDatabaseObject.
        Owner of the object (regular expression is allowed)


        :param owner: The owner of this UnsupportedDatabaseObject.
        :type: str
        """
        self._owner = owner

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this UnsupportedDatabaseObject.
        Name of the object (regular expression is allowed)


        :return: The object_name of this UnsupportedDatabaseObject.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this UnsupportedDatabaseObject.
        Name of the object (regular expression is allowed)


        :param object_name: The object_name of this UnsupportedDatabaseObject.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
