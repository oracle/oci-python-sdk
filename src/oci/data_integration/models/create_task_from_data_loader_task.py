# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_task_details import CreateTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTaskFromDataLoaderTask(CreateTaskDetails):
    """
    The information about a data flow task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTaskFromDataLoaderTask object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateTaskFromDataLoaderTask.model_type` attribute
        of this class is ``DATA_LOADER_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateTaskFromDataLoaderTask.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateTaskFromDataLoaderTask.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateTaskFromDataLoaderTask.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateTaskFromDataLoaderTask.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateTaskFromDataLoaderTask.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateTaskFromDataLoaderTask.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateTaskFromDataLoaderTask.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateTaskFromDataLoaderTask.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this CreateTaskFromDataLoaderTask.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this CreateTaskFromDataLoaderTask.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this CreateTaskFromDataLoaderTask.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this CreateTaskFromDataLoaderTask.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this CreateTaskFromDataLoaderTask.
        :type config_provider_delegate: oci.data_integration.models.CreateConfigProvider

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateTaskFromDataLoaderTask.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param data_flow:
            The value to assign to the data_flow property of this CreateTaskFromDataLoaderTask.
        :type data_flow: oci.data_integration.models.DataFlow

        :param conditional_composite_field_map:
            The value to assign to the conditional_composite_field_map property of this CreateTaskFromDataLoaderTask.
        :type conditional_composite_field_map: oci.data_integration.models.ConditionalCompositeFieldMap

        :param is_single_load:
            The value to assign to the is_single_load property of this CreateTaskFromDataLoaderTask.
        :type is_single_load: bool

        :param parallel_load_limit:
            The value to assign to the parallel_load_limit property of this CreateTaskFromDataLoaderTask.
        :type parallel_load_limit: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'config_provider_delegate': 'CreateConfigProvider',
            'registry_metadata': 'RegistryMetadata',
            'data_flow': 'DataFlow',
            'conditional_composite_field_map': 'ConditionalCompositeFieldMap',
            'is_single_load': 'bool',
            'parallel_load_limit': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'config_provider_delegate': 'configProviderDelegate',
            'registry_metadata': 'registryMetadata',
            'data_flow': 'dataFlow',
            'conditional_composite_field_map': 'conditionalCompositeFieldMap',
            'is_single_load': 'isSingleLoad',
            'parallel_load_limit': 'parallelLoadLimit'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._input_ports = None
        self._output_ports = None
        self._parameters = None
        self._op_config_values = None
        self._config_provider_delegate = None
        self._registry_metadata = None
        self._data_flow = None
        self._conditional_composite_field_map = None
        self._is_single_load = None
        self._parallel_load_limit = None
        self._model_type = 'DATA_LOADER_TASK'

    @property
    def data_flow(self):
        """
        Gets the data_flow of this CreateTaskFromDataLoaderTask.

        :return: The data_flow of this CreateTaskFromDataLoaderTask.
        :rtype: oci.data_integration.models.DataFlow
        """
        return self._data_flow

    @data_flow.setter
    def data_flow(self, data_flow):
        """
        Sets the data_flow of this CreateTaskFromDataLoaderTask.

        :param data_flow: The data_flow of this CreateTaskFromDataLoaderTask.
        :type: oci.data_integration.models.DataFlow
        """
        self._data_flow = data_flow

    @property
    def conditional_composite_field_map(self):
        """
        Gets the conditional_composite_field_map of this CreateTaskFromDataLoaderTask.

        :return: The conditional_composite_field_map of this CreateTaskFromDataLoaderTask.
        :rtype: oci.data_integration.models.ConditionalCompositeFieldMap
        """
        return self._conditional_composite_field_map

    @conditional_composite_field_map.setter
    def conditional_composite_field_map(self, conditional_composite_field_map):
        """
        Sets the conditional_composite_field_map of this CreateTaskFromDataLoaderTask.

        :param conditional_composite_field_map: The conditional_composite_field_map of this CreateTaskFromDataLoaderTask.
        :type: oci.data_integration.models.ConditionalCompositeFieldMap
        """
        self._conditional_composite_field_map = conditional_composite_field_map

    @property
    def is_single_load(self):
        """
        Gets the is_single_load of this CreateTaskFromDataLoaderTask.
        Defines whether Data Loader task is used for single load or multiple


        :return: The is_single_load of this CreateTaskFromDataLoaderTask.
        :rtype: bool
        """
        return self._is_single_load

    @is_single_load.setter
    def is_single_load(self, is_single_load):
        """
        Sets the is_single_load of this CreateTaskFromDataLoaderTask.
        Defines whether Data Loader task is used for single load or multiple


        :param is_single_load: The is_single_load of this CreateTaskFromDataLoaderTask.
        :type: bool
        """
        self._is_single_load = is_single_load

    @property
    def parallel_load_limit(self):
        """
        Gets the parallel_load_limit of this CreateTaskFromDataLoaderTask.
        Defines the number of entities being loaded in parallel at a time for a Data Loader task


        :return: The parallel_load_limit of this CreateTaskFromDataLoaderTask.
        :rtype: int
        """
        return self._parallel_load_limit

    @parallel_load_limit.setter
    def parallel_load_limit(self, parallel_load_limit):
        """
        Sets the parallel_load_limit of this CreateTaskFromDataLoaderTask.
        Defines the number of entities being loaded in parallel at a time for a Data Loader task


        :param parallel_load_limit: The parallel_load_limit of this CreateTaskFromDataLoaderTask.
        :type: int
        """
        self._parallel_load_limit = parallel_load_limit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
