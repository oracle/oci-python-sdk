# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connectivity_validation_details import CreateConnectivityValidationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Source(CreateConnectivityValidationDetails):
    """
    The information about the source object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Source object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.Source.model_type` attribute
        of this class is ``SOURCE_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Source.
            Allowed values for this property are: "SOURCE_OPERATOR", "TARGET_OPERATOR"
        :type model_type: str

        :param key:
            The value to assign to the key property of this Source.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Source.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Source.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this Source.
        :type name: str

        :param description:
            The value to assign to the description property of this Source.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Source.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this Source.
        :type input_ports: list[oci.data_connectivity.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this Source.
        :type output_ports: list[oci.data_connectivity.models.OutputPort]

        :param object_status:
            The value to assign to the object_status property of this Source.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Source.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this Source.
        :type parameters: list[oci.data_connectivity.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this Source.
        :type op_config_values: oci.data_connectivity.models.ConfigValues

        :param entity:
            The value to assign to the entity property of this Source.
        :type entity: oci.data_connectivity.models.DataEntity

        :param is_read_access:
            The value to assign to the is_read_access property of this Source.
        :type is_read_access: bool

        :param is_copy_fields:
            The value to assign to the is_copy_fields property of this Source.
        :type is_copy_fields: bool

        :param is_predefined_shape:
            The value to assign to the is_predefined_shape property of this Source.
        :type is_predefined_shape: bool

        :param schema_drift_config:
            The value to assign to the schema_drift_config property of this Source.
        :type schema_drift_config: oci.data_connectivity.models.SchemaDriftConfig

        :param fixed_data_shape:
            The value to assign to the fixed_data_shape property of this Source.
        :type fixed_data_shape: oci.data_connectivity.models.Shape

        :param read_operation_config:
            The value to assign to the read_operation_config property of this Source.
        :type read_operation_config: oci.data_connectivity.models.ReadOperationConfig

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
            'schema_drift_config': 'SchemaDriftConfig',
            'fixed_data_shape': 'Shape',
            'read_operation_config': 'ReadOperationConfig'
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
            'schema_drift_config': 'schemaDriftConfig',
            'fixed_data_shape': 'fixedDataShape',
            'read_operation_config': 'readOperationConfig'
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
        self._schema_drift_config = None
        self._fixed_data_shape = None
        self._read_operation_config = None
        self._model_type = 'SOURCE_OPERATOR'

    @property
    def entity(self):
        """
        **[Required]** Gets the entity of this Source.

        :return: The entity of this Source.
        :rtype: oci.data_connectivity.models.DataEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this Source.

        :param entity: The entity of this Source.
        :type: oci.data_connectivity.models.DataEntity
        """
        self._entity = entity

    @property
    def is_read_access(self):
        """
        Gets the is_read_access of this Source.
        Specifies the read access.


        :return: The is_read_access of this Source.
        :rtype: bool
        """
        return self._is_read_access

    @is_read_access.setter
    def is_read_access(self, is_read_access):
        """
        Sets the is_read_access of this Source.
        Specifies the read access.


        :param is_read_access: The is_read_access of this Source.
        :type: bool
        """
        self._is_read_access = is_read_access

    @property
    def is_copy_fields(self):
        """
        Gets the is_copy_fields of this Source.
        Specifies the copy fields.


        :return: The is_copy_fields of this Source.
        :rtype: bool
        """
        return self._is_copy_fields

    @is_copy_fields.setter
    def is_copy_fields(self, is_copy_fields):
        """
        Sets the is_copy_fields of this Source.
        Specifies the copy fields.


        :param is_copy_fields: The is_copy_fields of this Source.
        :type: bool
        """
        self._is_copy_fields = is_copy_fields

    @property
    def is_predefined_shape(self):
        """
        Gets the is_predefined_shape of this Source.
        Specifies if this uses a predefined shape.


        :return: The is_predefined_shape of this Source.
        :rtype: bool
        """
        return self._is_predefined_shape

    @is_predefined_shape.setter
    def is_predefined_shape(self, is_predefined_shape):
        """
        Sets the is_predefined_shape of this Source.
        Specifies if this uses a predefined shape.


        :param is_predefined_shape: The is_predefined_shape of this Source.
        :type: bool
        """
        self._is_predefined_shape = is_predefined_shape

    @property
    def schema_drift_config(self):
        """
        Gets the schema_drift_config of this Source.

        :return: The schema_drift_config of this Source.
        :rtype: oci.data_connectivity.models.SchemaDriftConfig
        """
        return self._schema_drift_config

    @schema_drift_config.setter
    def schema_drift_config(self, schema_drift_config):
        """
        Sets the schema_drift_config of this Source.

        :param schema_drift_config: The schema_drift_config of this Source.
        :type: oci.data_connectivity.models.SchemaDriftConfig
        """
        self._schema_drift_config = schema_drift_config

    @property
    def fixed_data_shape(self):
        """
        Gets the fixed_data_shape of this Source.

        :return: The fixed_data_shape of this Source.
        :rtype: oci.data_connectivity.models.Shape
        """
        return self._fixed_data_shape

    @fixed_data_shape.setter
    def fixed_data_shape(self, fixed_data_shape):
        """
        Sets the fixed_data_shape of this Source.

        :param fixed_data_shape: The fixed_data_shape of this Source.
        :type: oci.data_connectivity.models.Shape
        """
        self._fixed_data_shape = fixed_data_shape

    @property
    def read_operation_config(self):
        """
        Gets the read_operation_config of this Source.

        :return: The read_operation_config of this Source.
        :rtype: oci.data_connectivity.models.ReadOperationConfig
        """
        return self._read_operation_config

    @read_operation_config.setter
    def read_operation_config(self, read_operation_config):
        """
        Sets the read_operation_config of this Source.

        :param read_operation_config: The read_operation_config of this Source.
        :type: oci.data_connectivity.models.ReadOperationConfig
        """
        self._read_operation_config = read_operation_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
