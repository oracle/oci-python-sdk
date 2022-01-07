# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PatchObjectMetadata(object):
    """
    A summary type containing information about the object including its key, name and when/who created/updated it.
    """

    #: A constant which can be used with the type property of a PatchObjectMetadata.
    #: This constant has a value of "INTEGRATION_TASK"
    TYPE_INTEGRATION_TASK = "INTEGRATION_TASK"

    #: A constant which can be used with the type property of a PatchObjectMetadata.
    #: This constant has a value of "DATA_LOADER_TASK"
    TYPE_DATA_LOADER_TASK = "DATA_LOADER_TASK"

    #: A constant which can be used with the type property of a PatchObjectMetadata.
    #: This constant has a value of "PIPELINE_TASK"
    TYPE_PIPELINE_TASK = "PIPELINE_TASK"

    #: A constant which can be used with the type property of a PatchObjectMetadata.
    #: This constant has a value of "SQL_TASK"
    TYPE_SQL_TASK = "SQL_TASK"

    #: A constant which can be used with the type property of a PatchObjectMetadata.
    #: This constant has a value of "OCI_DATAFLOW_TASK"
    TYPE_OCI_DATAFLOW_TASK = "OCI_DATAFLOW_TASK"

    #: A constant which can be used with the type property of a PatchObjectMetadata.
    #: This constant has a value of "REST_TASK"
    TYPE_REST_TASK = "REST_TASK"

    #: A constant which can be used with the action property of a PatchObjectMetadata.
    #: This constant has a value of "CREATED"
    ACTION_CREATED = "CREATED"

    #: A constant which can be used with the action property of a PatchObjectMetadata.
    #: This constant has a value of "DELETED"
    ACTION_DELETED = "DELETED"

    #: A constant which can be used with the action property of a PatchObjectMetadata.
    #: This constant has a value of "UPDATED"
    ACTION_UPDATED = "UPDATED"

    def __init__(self, **kwargs):
        """
        Initializes a new PatchObjectMetadata object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this PatchObjectMetadata.
        :type key: str

        :param name:
            The value to assign to the name property of this PatchObjectMetadata.
        :type name: str

        :param name_path:
            The value to assign to the name_path property of this PatchObjectMetadata.
        :type name_path: str

        :param type:
            The value to assign to the type property of this PatchObjectMetadata.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param object_version:
            The value to assign to the object_version property of this PatchObjectMetadata.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this PatchObjectMetadata.
        :type identifier: str

        :param action:
            The value to assign to the action property of this PatchObjectMetadata.
            Allowed values for this property are: "CREATED", "DELETED", "UPDATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'name_path': 'str',
            'type': 'str',
            'object_version': 'int',
            'identifier': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'name_path': 'namePath',
            'type': 'type',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'action': 'action'
        }

        self._key = None
        self._name = None
        self._name_path = None
        self._type = None
        self._object_version = None
        self._identifier = None
        self._action = None

    @property
    def key(self):
        """
        Gets the key of this PatchObjectMetadata.
        The key of the object.


        :return: The key of this PatchObjectMetadata.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PatchObjectMetadata.
        The key of the object.


        :param key: The key of this PatchObjectMetadata.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this PatchObjectMetadata.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this PatchObjectMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PatchObjectMetadata.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this PatchObjectMetadata.
        :type: str
        """
        self._name = name

    @property
    def name_path(self):
        """
        Gets the name_path of this PatchObjectMetadata.
        The fully qualified path of the published object, which would include its project and folder.


        :return: The name_path of this PatchObjectMetadata.
        :rtype: str
        """
        return self._name_path

    @name_path.setter
    def name_path(self, name_path):
        """
        Sets the name_path of this PatchObjectMetadata.
        The fully qualified path of the published object, which would include its project and folder.


        :param name_path: The name_path of this PatchObjectMetadata.
        :type: str
        """
        self._name_path = name_path

    @property
    def type(self):
        """
        Gets the type of this PatchObjectMetadata.
        The type of the object in patch.

        Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this PatchObjectMetadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PatchObjectMetadata.
        The type of the object in patch.


        :param type: The type of this PatchObjectMetadata.
        :type: str
        """
        allowed_values = ["INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def object_version(self):
        """
        Gets the object_version of this PatchObjectMetadata.
        The object version.


        :return: The object_version of this PatchObjectMetadata.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this PatchObjectMetadata.
        The object version.


        :param object_version: The object_version of this PatchObjectMetadata.
        :type: int
        """
        self._object_version = object_version

    @property
    def identifier(self):
        """
        Gets the identifier of this PatchObjectMetadata.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this PatchObjectMetadata.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this PatchObjectMetadata.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this PatchObjectMetadata.
        :type: str
        """
        self._identifier = identifier

    @property
    def action(self):
        """
        Gets the action of this PatchObjectMetadata.
        The patch action indicating if object was created, updated, or deleted.

        Allowed values for this property are: "CREATED", "DELETED", "UPDATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this PatchObjectMetadata.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PatchObjectMetadata.
        The patch action indicating if object was created, updated, or deleted.


        :param action: The action of this PatchObjectMetadata.
        :type: str
        """
        allowed_values = ["CREATED", "DELETED", "UPDATED"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
