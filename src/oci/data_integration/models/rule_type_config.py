# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dynamic_type_handler import DynamicTypeHandler
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleTypeConfig(DynamicTypeHandler):
    """
    The rule type config.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RuleTypeConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.RuleTypeConfig.model_type` attribute
        of this class is ``RULE_TYPE_CONFIGS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this RuleTypeConfig.
            Allowed values for this property are: "RULE_TYPE_CONFIGS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this RuleTypeConfig.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this RuleTypeConfig.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this RuleTypeConfig.
        :type parent_ref: ParentReference

        :param scope:
            The value to assign to the scope property of this RuleTypeConfig.
        :type scope: object

        :param is_order_by_rule:
            The value to assign to the is_order_by_rule property of this RuleTypeConfig.
        :type is_order_by_rule: bool

        :param projection_rules:
            The value to assign to the projection_rules property of this RuleTypeConfig.
        :type projection_rules: list[ProjectionRule]

        :param config_values:
            The value to assign to the config_values property of this RuleTypeConfig.
        :type config_values: ConfigValues

        :param object_status:
            The value to assign to the object_status property of this RuleTypeConfig.
        :type object_status: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'scope': 'object',
            'is_order_by_rule': 'bool',
            'projection_rules': 'list[ProjectionRule]',
            'config_values': 'ConfigValues',
            'object_status': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'scope': 'scope',
            'is_order_by_rule': 'isOrderByRule',
            'projection_rules': 'projectionRules',
            'config_values': 'configValues',
            'object_status': 'objectStatus'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._scope = None
        self._is_order_by_rule = None
        self._projection_rules = None
        self._config_values = None
        self._object_status = None
        self._model_type = 'RULE_TYPE_CONFIGS'

    @property
    def key(self):
        """
        Gets the key of this RuleTypeConfig.
        The key of the object.


        :return: The key of this RuleTypeConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this RuleTypeConfig.
        The key of the object.


        :param key: The key of this RuleTypeConfig.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this RuleTypeConfig.
        The model version of an object.


        :return: The model_version of this RuleTypeConfig.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this RuleTypeConfig.
        The model version of an object.


        :param model_version: The model_version of this RuleTypeConfig.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this RuleTypeConfig.

        :return: The parent_ref of this RuleTypeConfig.
        :rtype: ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this RuleTypeConfig.

        :param parent_ref: The parent_ref of this RuleTypeConfig.
        :type: ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def scope(self):
        """
        Gets the scope of this RuleTypeConfig.
        Reference to a typed object, this can be either a key value to an object within the document, a shall referenced to a `TypedObject` or a full `TypedObject` definition.


        :return: The scope of this RuleTypeConfig.
        :rtype: object
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this RuleTypeConfig.
        Reference to a typed object, this can be either a key value to an object within the document, a shall referenced to a `TypedObject` or a full `TypedObject` definition.


        :param scope: The scope of this RuleTypeConfig.
        :type: object
        """
        self._scope = scope

    @property
    def is_order_by_rule(self):
        """
        Gets the is_order_by_rule of this RuleTypeConfig.
        Specifies whether it is ordered by rule.


        :return: The is_order_by_rule of this RuleTypeConfig.
        :rtype: bool
        """
        return self._is_order_by_rule

    @is_order_by_rule.setter
    def is_order_by_rule(self, is_order_by_rule):
        """
        Sets the is_order_by_rule of this RuleTypeConfig.
        Specifies whether it is ordered by rule.


        :param is_order_by_rule: The is_order_by_rule of this RuleTypeConfig.
        :type: bool
        """
        self._is_order_by_rule = is_order_by_rule

    @property
    def projection_rules(self):
        """
        Gets the projection_rules of this RuleTypeConfig.
        The projection rules.


        :return: The projection_rules of this RuleTypeConfig.
        :rtype: list[ProjectionRule]
        """
        return self._projection_rules

    @projection_rules.setter
    def projection_rules(self, projection_rules):
        """
        Sets the projection_rules of this RuleTypeConfig.
        The projection rules.


        :param projection_rules: The projection_rules of this RuleTypeConfig.
        :type: list[ProjectionRule]
        """
        self._projection_rules = projection_rules

    @property
    def config_values(self):
        """
        Gets the config_values of this RuleTypeConfig.

        :return: The config_values of this RuleTypeConfig.
        :rtype: ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this RuleTypeConfig.

        :param config_values: The config_values of this RuleTypeConfig.
        :type: ConfigValues
        """
        self._config_values = config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this RuleTypeConfig.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this RuleTypeConfig.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this RuleTypeConfig.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this RuleTypeConfig.
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
