# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomPropertyTypeUsage(object):
    """
    Object which describes the indivial object stats for every custom property
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomPropertyTypeUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type_id:
            The value to assign to the type_id property of this CustomPropertyTypeUsage.
        :type type_id: str

        :param type_name:
            The value to assign to the type_name property of this CustomPropertyTypeUsage.
        :type type_name: str

        :param count:
            The value to assign to the count property of this CustomPropertyTypeUsage.
        :type count: int

        """
        self.swagger_types = {
            'type_id': 'str',
            'type_name': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'type_id': 'typeId',
            'type_name': 'typeName',
            'count': 'count'
        }

        self._type_id = None
        self._type_name = None
        self._count = None

    @property
    def type_id(self):
        """
        Gets the type_id of this CustomPropertyTypeUsage.
        Unique type key identifier


        :return: The type_id of this CustomPropertyTypeUsage.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this CustomPropertyTypeUsage.
        Unique type key identifier


        :param type_id: The type_id of this CustomPropertyTypeUsage.
        :type: str
        """
        self._type_id = type_id

    @property
    def type_name(self):
        """
        Gets the type_name of this CustomPropertyTypeUsage.
        Name of the type associated with


        :return: The type_name of this CustomPropertyTypeUsage.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this CustomPropertyTypeUsage.
        Name of the type associated with


        :param type_name: The type_name of this CustomPropertyTypeUsage.
        :type: str
        """
        self._type_name = type_name

    @property
    def count(self):
        """
        Gets the count of this CustomPropertyTypeUsage.
        Number of objects associated with this type


        :return: The count of this CustomPropertyTypeUsage.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this CustomPropertyTypeUsage.
        Number of objects associated with this type


        :param count: The count of this CustomPropertyTypeUsage.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
