# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .published_object import PublishedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PublishedObjectFromDataLoaderTask(PublishedObject):
    """
    The data loader task published object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PublishedObjectFromDataLoaderTask object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.PublishedObjectFromDataLoaderTask.model_type` attribute
        of this class is ``DATA_LOADER_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this PublishedObjectFromDataLoaderTask.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this PublishedObjectFromDataLoaderTask.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this PublishedObjectFromDataLoaderTask.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this PublishedObjectFromDataLoaderTask.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this PublishedObjectFromDataLoaderTask.
        :type name: str

        :param description:
            The value to assign to the description property of this PublishedObjectFromDataLoaderTask.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this PublishedObjectFromDataLoaderTask.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this PublishedObjectFromDataLoaderTask.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this PublishedObjectFromDataLoaderTask.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this PublishedObjectFromDataLoaderTask.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this PublishedObjectFromDataLoaderTask.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this PublishedObjectFromDataLoaderTask.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this PublishedObjectFromDataLoaderTask.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this PublishedObjectFromDataLoaderTask.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param data_flow:
            The value to assign to the data_flow property of this PublishedObjectFromDataLoaderTask.
        :type data_flow: oci.data_integration.models.DataFlow

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'config_provider_delegate': 'ConfigProvider',
            'data_flow': 'DataFlow'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'config_provider_delegate': 'configProviderDelegate',
            'data_flow': 'dataFlow'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._input_ports = None
        self._output_ports = None
        self._parameters = None
        self._op_config_values = None
        self._config_provider_delegate = None
        self._data_flow = None
        self._model_type = 'DATA_LOADER_TASK'

    @property
    def input_ports(self):
        """
        Gets the input_ports of this PublishedObjectFromDataLoaderTask.
        An array of input ports.


        :return: The input_ports of this PublishedObjectFromDataLoaderTask.
        :rtype: list[oci.data_integration.models.InputPort]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """
        Sets the input_ports of this PublishedObjectFromDataLoaderTask.
        An array of input ports.


        :param input_ports: The input_ports of this PublishedObjectFromDataLoaderTask.
        :type: list[oci.data_integration.models.InputPort]
        """
        self._input_ports = input_ports

    @property
    def output_ports(self):
        """
        Gets the output_ports of this PublishedObjectFromDataLoaderTask.
        An array of output ports.


        :return: The output_ports of this PublishedObjectFromDataLoaderTask.
        :rtype: list[oci.data_integration.models.OutputPort]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """
        Sets the output_ports of this PublishedObjectFromDataLoaderTask.
        An array of output ports.


        :param output_ports: The output_ports of this PublishedObjectFromDataLoaderTask.
        :type: list[oci.data_integration.models.OutputPort]
        """
        self._output_ports = output_ports

    @property
    def parameters(self):
        """
        Gets the parameters of this PublishedObjectFromDataLoaderTask.
        An array of parameters.


        :return: The parameters of this PublishedObjectFromDataLoaderTask.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this PublishedObjectFromDataLoaderTask.
        An array of parameters.


        :param parameters: The parameters of this PublishedObjectFromDataLoaderTask.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def op_config_values(self):
        """
        Gets the op_config_values of this PublishedObjectFromDataLoaderTask.

        :return: The op_config_values of this PublishedObjectFromDataLoaderTask.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._op_config_values

    @op_config_values.setter
    def op_config_values(self, op_config_values):
        """
        Sets the op_config_values of this PublishedObjectFromDataLoaderTask.

        :param op_config_values: The op_config_values of this PublishedObjectFromDataLoaderTask.
        :type: oci.data_integration.models.ConfigValues
        """
        self._op_config_values = op_config_values

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this PublishedObjectFromDataLoaderTask.

        :return: The config_provider_delegate of this PublishedObjectFromDataLoaderTask.
        :rtype: oci.data_integration.models.ConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this PublishedObjectFromDataLoaderTask.

        :param config_provider_delegate: The config_provider_delegate of this PublishedObjectFromDataLoaderTask.
        :type: oci.data_integration.models.ConfigProvider
        """
        self._config_provider_delegate = config_provider_delegate

    @property
    def data_flow(self):
        """
        Gets the data_flow of this PublishedObjectFromDataLoaderTask.

        :return: The data_flow of this PublishedObjectFromDataLoaderTask.
        :rtype: oci.data_integration.models.DataFlow
        """
        return self._data_flow

    @data_flow.setter
    def data_flow(self, data_flow):
        """
        Sets the data_flow of this PublishedObjectFromDataLoaderTask.

        :param data_flow: The data_flow of this PublishedObjectFromDataLoaderTask.
        :type: oci.data_integration.models.DataFlow
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
