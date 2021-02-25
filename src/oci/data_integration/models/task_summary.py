# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskSummary(object):
    """
    The task summary object type contains the audit summary information and the definition of the task summary object.
    """

    #: A constant which can be used with the model_type property of a TaskSummary.
    #: This constant has a value of "INTEGRATION_TASK"
    MODEL_TYPE_INTEGRATION_TASK = "INTEGRATION_TASK"

    #: A constant which can be used with the model_type property of a TaskSummary.
    #: This constant has a value of "DATA_LOADER_TASK"
    MODEL_TYPE_DATA_LOADER_TASK = "DATA_LOADER_TASK"

    #: A constant which can be used with the model_type property of a TaskSummary.
    #: This constant has a value of "PIPELINE_TASK"
    MODEL_TYPE_PIPELINE_TASK = "PIPELINE_TASK"

    def __init__(self, **kwargs):
        """
        Initializes a new TaskSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.TaskSummaryFromIntegrationTask`
        * :class:`~oci.data_integration.models.TaskSummaryFromPipelineTask`
        * :class:`~oci.data_integration.models.TaskSummaryFromDataLoaderTask`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TaskSummary.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this TaskSummary.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TaskSummary.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TaskSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskSummary.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskSummary.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this TaskSummary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this TaskSummary.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this TaskSummary.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this TaskSummary.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this TaskSummary.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this TaskSummary.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this TaskSummary.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param metadata:
            The value to assign to the metadata property of this TaskSummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this TaskSummary.
        :type key_map: dict(str, str)

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
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
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
            'metadata': 'metadata',
            'key_map': 'keyMap'
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
        self._metadata = None
        self._key_map = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'INTEGRATION_TASK':
            return 'TaskSummaryFromIntegrationTask'

        if type == 'PIPELINE_TASK':
            return 'TaskSummaryFromPipelineTask'

        if type == 'DATA_LOADER_TASK':
            return 'TaskSummaryFromDataLoaderTask'
        else:
            return 'TaskSummary'

    @property
    def model_type(self):
        """
        Gets the model_type of this TaskSummary.
        The type of task.

        Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this TaskSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this TaskSummary.
        The type of task.


        :param model_type: The model_type of this TaskSummary.
        :type: str
        """
        allowed_values = ["INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this TaskSummary.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :return: The key of this TaskSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TaskSummary.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :param key: The key of this TaskSummary.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this TaskSummary.
        The object's model version.


        :return: The model_version of this TaskSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this TaskSummary.
        The object's model version.


        :param model_version: The model_version of this TaskSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this TaskSummary.

        :return: The parent_ref of this TaskSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this TaskSummary.

        :param parent_ref: The parent_ref of this TaskSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this TaskSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this TaskSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaskSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this TaskSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TaskSummary.
        Detailed description for the object.


        :return: The description of this TaskSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TaskSummary.
        Detailed description for the object.


        :param description: The description of this TaskSummary.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this TaskSummary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this TaskSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this TaskSummary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this TaskSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this TaskSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this TaskSummary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this TaskSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this TaskSummary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this TaskSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this TaskSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this TaskSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this TaskSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def input_ports(self):
        """
        Gets the input_ports of this TaskSummary.
        An array of input ports.


        :return: The input_ports of this TaskSummary.
        :rtype: list[oci.data_integration.models.InputPort]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """
        Sets the input_ports of this TaskSummary.
        An array of input ports.


        :param input_ports: The input_ports of this TaskSummary.
        :type: list[oci.data_integration.models.InputPort]
        """
        self._input_ports = input_ports

    @property
    def output_ports(self):
        """
        Gets the output_ports of this TaskSummary.
        An array of output ports.


        :return: The output_ports of this TaskSummary.
        :rtype: list[oci.data_integration.models.OutputPort]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """
        Sets the output_ports of this TaskSummary.
        An array of output ports.


        :param output_ports: The output_ports of this TaskSummary.
        :type: list[oci.data_integration.models.OutputPort]
        """
        self._output_ports = output_ports

    @property
    def parameters(self):
        """
        Gets the parameters of this TaskSummary.
        An array of parameters.


        :return: The parameters of this TaskSummary.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this TaskSummary.
        An array of parameters.


        :param parameters: The parameters of this TaskSummary.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def op_config_values(self):
        """
        Gets the op_config_values of this TaskSummary.

        :return: The op_config_values of this TaskSummary.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._op_config_values

    @op_config_values.setter
    def op_config_values(self, op_config_values):
        """
        Sets the op_config_values of this TaskSummary.

        :param op_config_values: The op_config_values of this TaskSummary.
        :type: oci.data_integration.models.ConfigValues
        """
        self._op_config_values = op_config_values

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this TaskSummary.

        :return: The config_provider_delegate of this TaskSummary.
        :rtype: oci.data_integration.models.ConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this TaskSummary.

        :param config_provider_delegate: The config_provider_delegate of this TaskSummary.
        :type: oci.data_integration.models.ConfigProvider
        """
        self._config_provider_delegate = config_provider_delegate

    @property
    def metadata(self):
        """
        Gets the metadata of this TaskSummary.

        :return: The metadata of this TaskSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TaskSummary.

        :param metadata: The metadata of this TaskSummary.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this TaskSummary.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this TaskSummary.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this TaskSummary.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this TaskSummary.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
