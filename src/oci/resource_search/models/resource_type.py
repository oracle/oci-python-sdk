# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceType(object):
    """
    Defines a type of resource that you can find with a search or query.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ResourceType.
        :type name: str

        :param fields:
            The value to assign to the fields property of this ResourceType.
        :type fields: list[QueryableFieldDescription]

        """
        self.swagger_types = {
            'name': 'str',
            'fields': 'list[QueryableFieldDescription]'
        }

        self.attribute_map = {
            'name': 'name',
            'fields': 'fields'
        }

        self._name = None
        self._fields = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ResourceType.
        The unique name of the resource type, which matches the value returned as part of the ResourceSummary object.


        :return: The name of this ResourceType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResourceType.
        The unique name of the resource type, which matches the value returned as part of the ResourceSummary object.


        :param name: The name of this ResourceType.
        :type: str
        """
        self._name = name

    @property
    def fields(self):
        """
        **[Required]** Gets the fields of this ResourceType.
        List of all the fields and their value type that are indexed for querying.


        :return: The fields of this ResourceType.
        :rtype: list[QueryableFieldDescription]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this ResourceType.
        List of all the fields and their value type that are indexed for querying.


        :param fields: The fields of this ResourceType.
        :type: list[QueryableFieldDescription]
        """
        self._fields = fields

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
