# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_task_details import UpdateTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTaskFromDataLoaderTask(UpdateTaskDetails):
    """
    The information about the data loader task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTaskFromDataLoaderTask object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.UpdateTaskFromDataLoaderTask.model_type` attribute
        of this class is ``DATA_LOADER_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UpdateTaskFromDataLoaderTask.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this UpdateTaskFromDataLoaderTask.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UpdateTaskFromDataLoaderTask.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UpdateTaskFromDataLoaderTask.
        :type parent_ref: ParentReference

        :param name:
            The value to assign to the name property of this UpdateTaskFromDataLoaderTask.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateTaskFromDataLoaderTask.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateTaskFromDataLoaderTask.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this UpdateTaskFromDataLoaderTask.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this UpdateTaskFromDataLoaderTask.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this UpdateTaskFromDataLoaderTask.
        :type input_ports: list[InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this UpdateTaskFromDataLoaderTask.
        :type output_ports: list[OutputPort]

        :param parameters:
            The value to assign to the parameters property of this UpdateTaskFromDataLoaderTask.
        :type parameters: list[Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this UpdateTaskFromDataLoaderTask.
        :type op_config_values: ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this UpdateTaskFromDataLoaderTask.
        :type config_provider_delegate: ConfigProvider

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateTaskFromDataLoaderTask.
        :type registry_metadata: RegistryMetadata

        :param data_flow:
            The value to assign to the data_flow property of this UpdateTaskFromDataLoaderTask.
        :type data_flow: DataFlow

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
            'data_flow': 'DataFlow'
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
            'data_flow': 'dataFlow'
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
        self._data_flow = None
        self._model_type = 'DATA_LOADER_TASK'

    @property
    def data_flow(self):
        """
        Gets the data_flow of this UpdateTaskFromDataLoaderTask.

        :return: The data_flow of this UpdateTaskFromDataLoaderTask.
        :rtype: DataFlow
        """
        return self._data_flow

    @data_flow.setter
    def data_flow(self, data_flow):
        """
        Sets the data_flow of this UpdateTaskFromDataLoaderTask.

        :param data_flow: The data_flow of this UpdateTaskFromDataLoaderTask.
        :type: DataFlow
        """
        self._data_flow = data_flow

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
