# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProjectionRule(object):
    """
    Base type for how fields are projected. There are many different mechanisms for doing this such as by a name pattern, datatype and so on. See the `modelType` property for the types.
    """

    #: A constant which can be used with the model_type property of a ProjectionRule.
    #: This constant has a value of "NAME_PATTERN_RULE"
    MODEL_TYPE_NAME_PATTERN_RULE = "NAME_PATTERN_RULE"

    #: A constant which can be used with the model_type property of a ProjectionRule.
    #: This constant has a value of "TYPE_LIST_RULE"
    MODEL_TYPE_TYPE_LIST_RULE = "TYPE_LIST_RULE"

    #: A constant which can be used with the model_type property of a ProjectionRule.
    #: This constant has a value of "NAME_LIST_RULE"
    MODEL_TYPE_NAME_LIST_RULE = "NAME_LIST_RULE"

    #: A constant which can be used with the model_type property of a ProjectionRule.
    #: This constant has a value of "TYPED_NAME_PATTERN_RULE"
    MODEL_TYPE_TYPED_NAME_PATTERN_RULE = "TYPED_NAME_PATTERN_RULE"

    #: A constant which can be used with the model_type property of a ProjectionRule.
    #: This constant has a value of "RENAME_RULE"
    MODEL_TYPE_RENAME_RULE = "RENAME_RULE"

    def __init__(self, **kwargs):
        """
        Initializes a new ProjectionRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.RenameRule`
        * :class:`~oci.data_integration.models.TypeListRule`
        * :class:`~oci.data_integration.models.TypedNamePatternRule`
        * :class:`~oci.data_integration.models.NamePatternRule`
        * :class:`~oci.data_integration.models.NameListRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ProjectionRule.
            Allowed values for this property are: "NAME_PATTERN_RULE", "TYPE_LIST_RULE", "NAME_LIST_RULE", "TYPED_NAME_PATTERN_RULE", "RENAME_RULE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this ProjectionRule.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ProjectionRule.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ProjectionRule.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param is_java_regex_syntax:
            The value to assign to the is_java_regex_syntax property of this ProjectionRule.
        :type is_java_regex_syntax: bool

        :param config_values:
            The value to assign to the config_values property of this ProjectionRule.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this ProjectionRule.
        :type object_status: int

        :param description:
            The value to assign to the description property of this ProjectionRule.
        :type description: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'is_java_regex_syntax': 'bool',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'description': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'is_java_regex_syntax': 'isJavaRegexSyntax',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'description': 'description'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._is_java_regex_syntax = None
        self._config_values = None
        self._object_status = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'RENAME_RULE':
            return 'RenameRule'

        if type == 'TYPE_LIST_RULE':
            return 'TypeListRule'

        if type == 'TYPED_NAME_PATTERN_RULE':
            return 'TypedNamePatternRule'

        if type == 'NAME_PATTERN_RULE':
            return 'NamePatternRule'

        if type == 'NAME_LIST_RULE':
            return 'NameListRule'
        else:
            return 'ProjectionRule'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this ProjectionRule.
        The type of the project rule.

        Allowed values for this property are: "NAME_PATTERN_RULE", "TYPE_LIST_RULE", "NAME_LIST_RULE", "TYPED_NAME_PATTERN_RULE", "RENAME_RULE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this ProjectionRule.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ProjectionRule.
        The type of the project rule.


        :param model_type: The model_type of this ProjectionRule.
        :type: str
        """
        allowed_values = ["NAME_PATTERN_RULE", "TYPE_LIST_RULE", "NAME_LIST_RULE", "TYPED_NAME_PATTERN_RULE", "RENAME_RULE"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this ProjectionRule.
        The key of the object.


        :return: The key of this ProjectionRule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ProjectionRule.
        The key of the object.


        :param key: The key of this ProjectionRule.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this ProjectionRule.
        The model version of an object.


        :return: The model_version of this ProjectionRule.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ProjectionRule.
        The model version of an object.


        :param model_version: The model_version of this ProjectionRule.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ProjectionRule.

        :return: The parent_ref of this ProjectionRule.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ProjectionRule.

        :param parent_ref: The parent_ref of this ProjectionRule.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def is_java_regex_syntax(self):
        """
        Gets the is_java_regex_syntax of this ProjectionRule.
        Specifies whether the rule uses a java regex syntax.


        :return: The is_java_regex_syntax of this ProjectionRule.
        :rtype: bool
        """
        return self._is_java_regex_syntax

    @is_java_regex_syntax.setter
    def is_java_regex_syntax(self, is_java_regex_syntax):
        """
        Sets the is_java_regex_syntax of this ProjectionRule.
        Specifies whether the rule uses a java regex syntax.


        :param is_java_regex_syntax: The is_java_regex_syntax of this ProjectionRule.
        :type: bool
        """
        self._is_java_regex_syntax = is_java_regex_syntax

    @property
    def config_values(self):
        """
        Gets the config_values of this ProjectionRule.

        :return: The config_values of this ProjectionRule.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this ProjectionRule.

        :param config_values: The config_values of this ProjectionRule.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this ProjectionRule.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this ProjectionRule.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ProjectionRule.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this ProjectionRule.
        :type: int
        """
        self._object_status = object_status

    @property
    def description(self):
        """
        Gets the description of this ProjectionRule.
        A user defined description for the object.


        :return: The description of this ProjectionRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProjectionRule.
        A user defined description for the object.


        :param description: The description of this ProjectionRule.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
