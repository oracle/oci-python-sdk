# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Expression(object):
    """
    An expression node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Expression object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Expression.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this Expression.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this Expression.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Expression.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param expr_string:
            The value to assign to the expr_string property of this Expression.
        :type expr_string: str

        :param config_values:
            The value to assign to the config_values property of this Expression.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this Expression.
        :type object_status: int

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'expr_string': 'str',
            'config_values': 'ConfigValues',
            'object_status': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'expr_string': 'exprString',
            'config_values': 'configValues',
            'object_status': 'objectStatus'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._expr_string = None
        self._config_values = None
        self._object_status = None

    @property
    def key(self):
        """
        Gets the key of this Expression.
        The object key.


        :return: The key of this Expression.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Expression.
        The object key.


        :param key: The key of this Expression.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this Expression.
        The object type.


        :return: The model_type of this Expression.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Expression.
        The object type.


        :param model_type: The model_type of this Expression.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this Expression.
        The object's model version.


        :return: The model_version of this Expression.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Expression.
        The object's model version.


        :param model_version: The model_version of this Expression.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this Expression.

        :return: The parent_ref of this Expression.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this Expression.

        :param parent_ref: The parent_ref of this Expression.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def expr_string(self):
        """
        Gets the expr_string of this Expression.
        The expression string for the object.


        :return: The expr_string of this Expression.
        :rtype: str
        """
        return self._expr_string

    @expr_string.setter
    def expr_string(self, expr_string):
        """
        Sets the expr_string of this Expression.
        The expression string for the object.


        :param expr_string: The expr_string of this Expression.
        :type: str
        """
        self._expr_string = expr_string

    @property
    def config_values(self):
        """
        Gets the config_values of this Expression.

        :return: The config_values of this Expression.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this Expression.

        :param config_values: The config_values of this Expression.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this Expression.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this Expression.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this Expression.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this Expression.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
