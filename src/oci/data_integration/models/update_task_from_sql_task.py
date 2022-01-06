# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_task_details import UpdateTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTaskFromSQLTask(UpdateTaskDetails):
    """
    The information about the SQL task.
    """

    #: A constant which can be used with the sql_script_type property of a UpdateTaskFromSQLTask.
    #: This constant has a value of "STORED_PROCEDURE"
    SQL_SCRIPT_TYPE_STORED_PROCEDURE = "STORED_PROCEDURE"

    #: A constant which can be used with the sql_script_type property of a UpdateTaskFromSQLTask.
    #: This constant has a value of "SQL_CODE"
    SQL_SCRIPT_TYPE_SQL_CODE = "SQL_CODE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTaskFromSQLTask object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.UpdateTaskFromSQLTask.model_type` attribute
        of this class is ``SQL_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateTaskFromSQLTask.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateTaskFromSQLTask.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateTaskFromSQLTask.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UpdateTaskFromSQLTask.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this UpdateTaskFromSQLTask.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateTaskFromSQLTask.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateTaskFromSQLTask.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateTaskFromSQLTask.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateTaskFromSQLTask.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this UpdateTaskFromSQLTask.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this UpdateTaskFromSQLTask.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this UpdateTaskFromSQLTask.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this UpdateTaskFromSQLTask.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this UpdateTaskFromSQLTask.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateTaskFromSQLTask.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param script:
            The value to assign to the script property of this UpdateTaskFromSQLTask.
        :type script: oci.data_integration.models.Script

        :param sql_script_type:
            The value to assign to the sql_script_type property of this UpdateTaskFromSQLTask.
            Allowed values for this property are: "STORED_PROCEDURE", "SQL_CODE"
        :type sql_script_type: str

        :param operation:
            The value to assign to the operation property of this UpdateTaskFromSQLTask.
        :type operation: object

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'config_provider_delegate': 'ConfigProvider',
            'registry_metadata': 'RegistryMetadata',
            'script': 'Script',
            'sql_script_type': 'str',
            'operation': 'object'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'config_provider_delegate': 'configProviderDelegate',
            'registry_metadata': 'registryMetadata',
            'script': 'script',
            'sql_script_type': 'sqlScriptType',
            'operation': 'operation'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._input_ports = None
        self._output_ports = None
        self._parameters = None
        self._op_config_values = None
        self._config_provider_delegate = None
        self._registry_metadata = None
        self._script = None
        self._sql_script_type = None
        self._operation = None
        self._model_type = 'SQL_TASK'

    @property
    def script(self):
        """
        Gets the script of this UpdateTaskFromSQLTask.

        :return: The script of this UpdateTaskFromSQLTask.
        :rtype: oci.data_integration.models.Script
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this UpdateTaskFromSQLTask.

        :param script: The script of this UpdateTaskFromSQLTask.
        :type: oci.data_integration.models.Script
        """
        self._script = script

    @property
    def sql_script_type(self):
        """
        Gets the sql_script_type of this UpdateTaskFromSQLTask.
        Indicates whether the task is invoking a custom SQL script or stored procedure.

        Allowed values for this property are: "STORED_PROCEDURE", "SQL_CODE"


        :return: The sql_script_type of this UpdateTaskFromSQLTask.
        :rtype: str
        """
        return self._sql_script_type

    @sql_script_type.setter
    def sql_script_type(self, sql_script_type):
        """
        Sets the sql_script_type of this UpdateTaskFromSQLTask.
        Indicates whether the task is invoking a custom SQL script or stored procedure.


        :param sql_script_type: The sql_script_type of this UpdateTaskFromSQLTask.
        :type: str
        """
        allowed_values = ["STORED_PROCEDURE", "SQL_CODE"]
        if not value_allowed_none_or_none_sentinel(sql_script_type, allowed_values):
            raise ValueError(
                "Invalid value for `sql_script_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._sql_script_type = sql_script_type

    @property
    def operation(self):
        """
        Gets the operation of this UpdateTaskFromSQLTask.
        Describes the shape of the execution result


        :return: The operation of this UpdateTaskFromSQLTask.
        :rtype: object
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this UpdateTaskFromSQLTask.
        Describes the shape of the execution result


        :param operation: The operation of this UpdateTaskFromSQLTask.
        :type: object
        """
        self._operation = operation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
