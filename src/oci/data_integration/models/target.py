# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operator import Operator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Target(Operator):
    """
    The information about the target operator. The target operator lets you specify the data entity to store the transformed data.
    """

    #: A constant which can be used with the data_property property of a Target.
    #: This constant has a value of "TRUNCATE"
    DATA_PROPERTY_TRUNCATE = "TRUNCATE"

    #: A constant which can be used with the data_property property of a Target.
    #: This constant has a value of "MERGE"
    DATA_PROPERTY_MERGE = "MERGE"

    #: A constant which can be used with the data_property property of a Target.
    #: This constant has a value of "BACKUP"
    DATA_PROPERTY_BACKUP = "BACKUP"

    #: A constant which can be used with the data_property property of a Target.
    #: This constant has a value of "OVERWRITE"
    DATA_PROPERTY_OVERWRITE = "OVERWRITE"

    #: A constant which can be used with the data_property property of a Target.
    #: This constant has a value of "APPEND"
    DATA_PROPERTY_APPEND = "APPEND"

    #: A constant which can be used with the data_property property of a Target.
    #: This constant has a value of "IGNORE"
    DATA_PROPERTY_IGNORE = "IGNORE"

    def __init__(self, **kwargs):
        """
        Initializes a new Target object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Target.model_type` attribute
        of this class is ``TARGET_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Target.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "REST_OPERATOR", "TASK_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Target.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Target.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Target.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Target.
        :type name: str

        :param description:
            The value to assign to the description property of this Target.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Target.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this Target.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this Target.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param object_status:
            The value to assign to the object_status property of this Target.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Target.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this Target.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this Target.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param entity:
            The value to assign to the entity property of this Target.
        :type entity: oci.data_integration.models.DataEntity

        :param is_read_access:
            The value to assign to the is_read_access property of this Target.
        :type is_read_access: bool

        :param is_copy_fields:
            The value to assign to the is_copy_fields property of this Target.
        :type is_copy_fields: bool

        :param is_predefined_shape:
            The value to assign to the is_predefined_shape property of this Target.
        :type is_predefined_shape: bool

        :param data_property:
            The value to assign to the data_property property of this Target.
            Allowed values for this property are: "TRUNCATE", "MERGE", "BACKUP", "OVERWRITE", "APPEND", "IGNORE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_property: str

        :param schema_drift_config:
            The value to assign to the schema_drift_config property of this Target.
        :type schema_drift_config: oci.data_integration.models.SchemaDriftConfig

        :param fixed_data_shape:
            The value to assign to the fixed_data_shape property of this Target.
        :type fixed_data_shape: oci.data_integration.models.Shape

        :param write_operation_config:
            The value to assign to the write_operation_config property of this Target.
        :type write_operation_config: oci.data_integration.models.WriteOperationConfig

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'object_status': 'int',
            'identifier': 'str',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'entity': 'DataEntity',
            'is_read_access': 'bool',
            'is_copy_fields': 'bool',
            'is_predefined_shape': 'bool',
            'data_property': 'str',
            'schema_drift_config': 'SchemaDriftConfig',
            'fixed_data_shape': 'Shape',
            'write_operation_config': 'WriteOperationConfig'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'entity': 'entity',
            'is_read_access': 'isReadAccess',
            'is_copy_fields': 'isCopyFields',
            'is_predefined_shape': 'isPredefinedShape',
            'data_property': 'dataProperty',
            'schema_drift_config': 'schemaDriftConfig',
            'fixed_data_shape': 'fixedDataShape',
            'write_operation_config': 'writeOperationConfig'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._input_ports = None
        self._output_ports = None
        self._object_status = None
        self._identifier = None
        self._parameters = None
        self._op_config_values = None
        self._entity = None
        self._is_read_access = None
        self._is_copy_fields = None
        self._is_predefined_shape = None
        self._data_property = None
        self._schema_drift_config = None
        self._fixed_data_shape = None
        self._write_operation_config = None
        self._model_type = 'TARGET_OPERATOR'

    @property
    def entity(self):
        """
        Gets the entity of this Target.

        :return: The entity of this Target.
        :rtype: oci.data_integration.models.DataEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this Target.

        :param entity: The entity of this Target.
        :type: oci.data_integration.models.DataEntity
        """
        self._entity = entity

    @property
    def is_read_access(self):
        """
        Gets the is_read_access of this Target.
        Specifies the read access.


        :return: The is_read_access of this Target.
        :rtype: bool
        """
        return self._is_read_access

    @is_read_access.setter
    def is_read_access(self, is_read_access):
        """
        Sets the is_read_access of this Target.
        Specifies the read access.


        :param is_read_access: The is_read_access of this Target.
        :type: bool
        """
        self._is_read_access = is_read_access

    @property
    def is_copy_fields(self):
        """
        Gets the is_copy_fields of this Target.
        Specifies the copy fields.


        :return: The is_copy_fields of this Target.
        :rtype: bool
        """
        return self._is_copy_fields

    @is_copy_fields.setter
    def is_copy_fields(self, is_copy_fields):
        """
        Sets the is_copy_fields of this Target.
        Specifies the copy fields.


        :param is_copy_fields: The is_copy_fields of this Target.
        :type: bool
        """
        self._is_copy_fields = is_copy_fields

    @property
    def is_predefined_shape(self):
        """
        Gets the is_predefined_shape of this Target.
        Specifies if this uses a predefined shape.


        :return: The is_predefined_shape of this Target.
        :rtype: bool
        """
        return self._is_predefined_shape

    @is_predefined_shape.setter
    def is_predefined_shape(self, is_predefined_shape):
        """
        Sets the is_predefined_shape of this Target.
        Specifies if this uses a predefined shape.


        :param is_predefined_shape: The is_predefined_shape of this Target.
        :type: bool
        """
        self._is_predefined_shape = is_predefined_shape

    @property
    def data_property(self):
        """
        Gets the data_property of this Target.
        Specifies the data property.

        Allowed values for this property are: "TRUNCATE", "MERGE", "BACKUP", "OVERWRITE", "APPEND", "IGNORE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_property of this Target.
        :rtype: str
        """
        return self._data_property

    @data_property.setter
    def data_property(self, data_property):
        """
        Sets the data_property of this Target.
        Specifies the data property.


        :param data_property: The data_property of this Target.
        :type: str
        """
        allowed_values = ["TRUNCATE", "MERGE", "BACKUP", "OVERWRITE", "APPEND", "IGNORE"]
        if not value_allowed_none_or_none_sentinel(data_property, allowed_values):
            data_property = 'UNKNOWN_ENUM_VALUE'
        self._data_property = data_property

    @property
    def schema_drift_config(self):
        """
        Gets the schema_drift_config of this Target.

        :return: The schema_drift_config of this Target.
        :rtype: oci.data_integration.models.SchemaDriftConfig
        """
        return self._schema_drift_config

    @schema_drift_config.setter
    def schema_drift_config(self, schema_drift_config):
        """
        Sets the schema_drift_config of this Target.

        :param schema_drift_config: The schema_drift_config of this Target.
        :type: oci.data_integration.models.SchemaDriftConfig
        """
        self._schema_drift_config = schema_drift_config

    @property
    def fixed_data_shape(self):
        """
        Gets the fixed_data_shape of this Target.

        :return: The fixed_data_shape of this Target.
        :rtype: oci.data_integration.models.Shape
        """
        return self._fixed_data_shape

    @fixed_data_shape.setter
    def fixed_data_shape(self, fixed_data_shape):
        """
        Sets the fixed_data_shape of this Target.

        :param fixed_data_shape: The fixed_data_shape of this Target.
        :type: oci.data_integration.models.Shape
        """
        self._fixed_data_shape = fixed_data_shape

    @property
    def write_operation_config(self):
        """
        Gets the write_operation_config of this Target.

        :return: The write_operation_config of this Target.
        :rtype: oci.data_integration.models.WriteOperationConfig
        """
        return self._write_operation_config

    @write_operation_config.setter
    def write_operation_config(self, write_operation_config):
        """
        Sets the write_operation_config of this Target.

        :param write_operation_config: The write_operation_config of this Target.
        :type: oci.data_integration.models.WriteOperationConfig
        """
        self._write_operation_config = write_operation_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
