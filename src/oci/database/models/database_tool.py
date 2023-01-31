# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseTool(object):
    """
    Summary of database tools of autonomous database.
    """

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "APEX"
    NAME_APEX = "APEX"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "DATABASE_ACTIONS"
    NAME_DATABASE_ACTIONS = "DATABASE_ACTIONS"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "GRAPH_STUDIO"
    NAME_GRAPH_STUDIO = "GRAPH_STUDIO"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "OML"
    NAME_OML = "OML"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "DATA_TRANSFORMS"
    NAME_DATA_TRANSFORMS = "DATA_TRANSFORMS"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "ORDS"
    NAME_ORDS = "ORDS"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "MONGODB_API"
    NAME_MONGODB_API = "MONGODB_API"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseTool object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DatabaseTool.
            Allowed values for this property are: "APEX", "DATABASE_ACTIONS", "GRAPH_STUDIO", "OML", "DATA_TRANSFORMS", "ORDS", "MONGODB_API", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this DatabaseTool.
        :type is_enabled: bool

        """
        self.swagger_types = {
            'name': 'str',
            'is_enabled': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'is_enabled': 'isEnabled'
        }

        self._name = None
        self._is_enabled = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DatabaseTool.
        Name of database tool.

        Allowed values for this property are: "APEX", "DATABASE_ACTIONS", "GRAPH_STUDIO", "OML", "DATA_TRANSFORMS", "ORDS", "MONGODB_API", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this DatabaseTool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatabaseTool.
        Name of database tool.


        :param name: The name of this DatabaseTool.
        :type: str
        """
        allowed_values = ["APEX", "DATABASE_ACTIONS", "GRAPH_STUDIO", "OML", "DATA_TRANSFORMS", "ORDS", "MONGODB_API"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this DatabaseTool.
        Indicates whether tool is enabled.


        :return: The is_enabled of this DatabaseTool.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DatabaseTool.
        Indicates whether tool is enabled.


        :param is_enabled: The is_enabled of this DatabaseTool.
        :type: bool
        """
        self._is_enabled = is_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
