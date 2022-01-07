# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .field_map import FieldMap
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleBasedFieldMap(FieldMap):
    """
    A map of rule patterns.
    """

    #: A constant which can be used with the map_type property of a RuleBasedFieldMap.
    #: This constant has a value of "MAPBYNAME"
    MAP_TYPE_MAPBYNAME = "MAPBYNAME"

    #: A constant which can be used with the map_type property of a RuleBasedFieldMap.
    #: This constant has a value of "MAPBYPOSITION"
    MAP_TYPE_MAPBYPOSITION = "MAPBYPOSITION"

    #: A constant which can be used with the map_type property of a RuleBasedFieldMap.
    #: This constant has a value of "MAPBYPATTERN"
    MAP_TYPE_MAPBYPATTERN = "MAPBYPATTERN"

    def __init__(self, **kwargs):
        """
        Initializes a new RuleBasedFieldMap object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.RuleBasedFieldMap.model_type` attribute
        of this class is ``RULE_BASED_FIELD_MAP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this RuleBasedFieldMap.
            Allowed values for this property are: "DIRECT_NAMED_FIELD_MAP", "COMPOSITE_FIELD_MAP", "DIRECT_FIELD_MAP", "RULE_BASED_FIELD_MAP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param description:
            The value to assign to the description property of this RuleBasedFieldMap.
        :type description: str

        :param key:
            The value to assign to the key property of this RuleBasedFieldMap.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this RuleBasedFieldMap.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this RuleBasedFieldMap.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this RuleBasedFieldMap.
        :type config_values: oci.data_integration.models.ConfigValues

        :param map_type:
            The value to assign to the map_type property of this RuleBasedFieldMap.
            Allowed values for this property are: "MAPBYNAME", "MAPBYPOSITION", "MAPBYPATTERN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type map_type: str

        :param from_pattern:
            The value to assign to the from_pattern property of this RuleBasedFieldMap.
        :type from_pattern: str

        :param to_pattern:
            The value to assign to the to_pattern property of this RuleBasedFieldMap.
        :type to_pattern: str

        :param is_java_regex_syntax:
            The value to assign to the is_java_regex_syntax property of this RuleBasedFieldMap.
        :type is_java_regex_syntax: bool

        :param object_status:
            The value to assign to the object_status property of this RuleBasedFieldMap.
        :type object_status: int

        :param from_rule_config:
            The value to assign to the from_rule_config property of this RuleBasedFieldMap.
        :type from_rule_config: oci.data_integration.models.RuleTypeConfig

        :param to_rule_config:
            The value to assign to the to_rule_config property of this RuleBasedFieldMap.
        :type to_rule_config: oci.data_integration.models.RuleTypeConfig

        """
        self.swagger_types = {
            'model_type': 'str',
            'description': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'map_type': 'str',
            'from_pattern': 'str',
            'to_pattern': 'str',
            'is_java_regex_syntax': 'bool',
            'object_status': 'int',
            'from_rule_config': 'RuleTypeConfig',
            'to_rule_config': 'RuleTypeConfig'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'description': 'description',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'map_type': 'mapType',
            'from_pattern': 'fromPattern',
            'to_pattern': 'toPattern',
            'is_java_regex_syntax': 'isJavaRegexSyntax',
            'object_status': 'objectStatus',
            'from_rule_config': 'fromRuleConfig',
            'to_rule_config': 'toRuleConfig'
        }

        self._model_type = None
        self._description = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._map_type = None
        self._from_pattern = None
        self._to_pattern = None
        self._is_java_regex_syntax = None
        self._object_status = None
        self._from_rule_config = None
        self._to_rule_config = None
        self._model_type = 'RULE_BASED_FIELD_MAP'

    @property
    def key(self):
        """
        Gets the key of this RuleBasedFieldMap.
        The object key.


        :return: The key of this RuleBasedFieldMap.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this RuleBasedFieldMap.
        The object key.


        :param key: The key of this RuleBasedFieldMap.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this RuleBasedFieldMap.
        The object's model version.


        :return: The model_version of this RuleBasedFieldMap.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this RuleBasedFieldMap.
        The object's model version.


        :param model_version: The model_version of this RuleBasedFieldMap.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this RuleBasedFieldMap.

        :return: The parent_ref of this RuleBasedFieldMap.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this RuleBasedFieldMap.

        :param parent_ref: The parent_ref of this RuleBasedFieldMap.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def config_values(self):
        """
        Gets the config_values of this RuleBasedFieldMap.

        :return: The config_values of this RuleBasedFieldMap.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this RuleBasedFieldMap.

        :param config_values: The config_values of this RuleBasedFieldMap.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def map_type(self):
        """
        Gets the map_type of this RuleBasedFieldMap.
        mapType

        Allowed values for this property are: "MAPBYNAME", "MAPBYPOSITION", "MAPBYPATTERN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The map_type of this RuleBasedFieldMap.
        :rtype: str
        """
        return self._map_type

    @map_type.setter
    def map_type(self, map_type):
        """
        Sets the map_type of this RuleBasedFieldMap.
        mapType


        :param map_type: The map_type of this RuleBasedFieldMap.
        :type: str
        """
        allowed_values = ["MAPBYNAME", "MAPBYPOSITION", "MAPBYPATTERN"]
        if not value_allowed_none_or_none_sentinel(map_type, allowed_values):
            map_type = 'UNKNOWN_ENUM_VALUE'
        self._map_type = map_type

    @property
    def from_pattern(self):
        """
        Gets the from_pattern of this RuleBasedFieldMap.
        The pattern to map from.


        :return: The from_pattern of this RuleBasedFieldMap.
        :rtype: str
        """
        return self._from_pattern

    @from_pattern.setter
    def from_pattern(self, from_pattern):
        """
        Sets the from_pattern of this RuleBasedFieldMap.
        The pattern to map from.


        :param from_pattern: The from_pattern of this RuleBasedFieldMap.
        :type: str
        """
        self._from_pattern = from_pattern

    @property
    def to_pattern(self):
        """
        Gets the to_pattern of this RuleBasedFieldMap.
        The pattern to map to.


        :return: The to_pattern of this RuleBasedFieldMap.
        :rtype: str
        """
        return self._to_pattern

    @to_pattern.setter
    def to_pattern(self, to_pattern):
        """
        Sets the to_pattern of this RuleBasedFieldMap.
        The pattern to map to.


        :param to_pattern: The to_pattern of this RuleBasedFieldMap.
        :type: str
        """
        self._to_pattern = to_pattern

    @property
    def is_java_regex_syntax(self):
        """
        Gets the is_java_regex_syntax of this RuleBasedFieldMap.
        Specifies whether the rule uses a java regex syntax.


        :return: The is_java_regex_syntax of this RuleBasedFieldMap.
        :rtype: bool
        """
        return self._is_java_regex_syntax

    @is_java_regex_syntax.setter
    def is_java_regex_syntax(self, is_java_regex_syntax):
        """
        Sets the is_java_regex_syntax of this RuleBasedFieldMap.
        Specifies whether the rule uses a java regex syntax.


        :param is_java_regex_syntax: The is_java_regex_syntax of this RuleBasedFieldMap.
        :type: bool
        """
        self._is_java_regex_syntax = is_java_regex_syntax

    @property
    def object_status(self):
        """
        Gets the object_status of this RuleBasedFieldMap.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this RuleBasedFieldMap.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this RuleBasedFieldMap.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this RuleBasedFieldMap.
        :type: int
        """
        self._object_status = object_status

    @property
    def from_rule_config(self):
        """
        Gets the from_rule_config of this RuleBasedFieldMap.

        :return: The from_rule_config of this RuleBasedFieldMap.
        :rtype: oci.data_integration.models.RuleTypeConfig
        """
        return self._from_rule_config

    @from_rule_config.setter
    def from_rule_config(self, from_rule_config):
        """
        Sets the from_rule_config of this RuleBasedFieldMap.

        :param from_rule_config: The from_rule_config of this RuleBasedFieldMap.
        :type: oci.data_integration.models.RuleTypeConfig
        """
        self._from_rule_config = from_rule_config

    @property
    def to_rule_config(self):
        """
        Gets the to_rule_config of this RuleBasedFieldMap.

        :return: The to_rule_config of this RuleBasedFieldMap.
        :rtype: oci.data_integration.models.RuleTypeConfig
        """
        return self._to_rule_config

    @to_rule_config.setter
    def to_rule_config(self, to_rule_config):
        """
        Sets the to_rule_config of this RuleBasedFieldMap.

        :param to_rule_config: The to_rule_config of this RuleBasedFieldMap.
        :type: oci.data_integration.models.RuleTypeConfig
        """
        self._to_rule_config = to_rule_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
