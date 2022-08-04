# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchemaDefinition(object):
    """
    The schema object details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SchemaDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SchemaDefinition.
        :type name: str

        :param objects:
            The value to assign to the objects property of this SchemaDefinition.
        :type objects: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'objects': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'objects': 'objects'
        }

        self._name = None
        self._objects = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SchemaDefinition.
        The name of the schema.


        :return: The name of this SchemaDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SchemaDefinition.
        The name of the schema.


        :param name: The name of this SchemaDefinition.
        :type: str
        """
        self._name = name

    @property
    def objects(self):
        """
        Gets the objects of this SchemaDefinition.
        The names of schema objects.


        :return: The objects of this SchemaDefinition.
        :rtype: list[str]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """
        Sets the objects of this SchemaDefinition.
        The names of schema objects.


        :param objects: The objects of this SchemaDefinition.
        :type: list[str]
        """
        self._objects = objects

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
