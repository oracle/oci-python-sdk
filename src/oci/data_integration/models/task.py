# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Task(object):
    """
    The task type contains the audit summary information and the definition of the task.
    """

    #: A constant which can be used with the model_type property of a Task.
    #: This constant has a value of "INTEGRATION_TASK"
    MODEL_TYPE_INTEGRATION_TASK = "INTEGRATION_TASK"

    #: A constant which can be used with the model_type property of a Task.
    #: This constant has a value of "DATA_LOADER_TASK"
    MODEL_TYPE_DATA_LOADER_TASK = "DATA_LOADER_TASK"

    def __init__(self, **kwargs):
        """
        Initializes a new Task object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.TaskFromIntegrationTaskDetails`
        * :class:`~oci.data_integration.models.TaskFromDataLoaderTaskDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Task.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Task.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Task.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Task.
        :type parent_ref: ParentReference

        :param name:
            The value to assign to the name property of this Task.
        :type name: str

        :param description:
            The value to assign to the description property of this Task.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Task.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this Task.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Task.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this Task.
        :type input_ports: list[InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this Task.
        :type output_ports: list[OutputPort]

        :param parameters:
            The value to assign to the parameters property of this Task.
        :type parameters: list[Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this Task.
        :type op_config_values: ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this Task.
        :type config_provider_delegate: ConfigProvider

        :param metadata:
            The value to assign to the metadata property of this Task.
        :type metadata: ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this Task.
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
            return 'TaskFromIntegrationTaskDetails'

        if type == 'DATA_LOADER_TASK':
            return 'TaskFromDataLoaderTaskDetails'
        else:
            return 'Task'

    @property
    def model_type(self):
        """
        Gets the model_type of this Task.
        The type of the task.

        Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this Task.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Task.
        The type of the task.


        :param model_type: The model_type of this Task.
        :type: str
        """
        allowed_values = ["INTEGRATION_TASK", "DATA_LOADER_TASK"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this Task.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :return: The key of this Task.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Task.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :param key: The key of this Task.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this Task.
        The model version of an object.


        :return: The model_version of this Task.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Task.
        The model version of an object.


        :param model_version: The model_version of this Task.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this Task.

        :return: The parent_ref of this Task.
        :rtype: ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this Task.

        :param parent_ref: The parent_ref of this Task.
        :type: ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this Task.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :return: The name of this Task.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Task.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :param name: The name of this Task.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Task.
        Detailed description for the object.


        :return: The description of this Task.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Task.
        Detailed description for the object.


        :param description: The description of this Task.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this Task.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this Task.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this Task.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this Task.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this Task.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this Task.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this Task.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this Task.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this Task.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :return: The identifier of this Task.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Task.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :param identifier: The identifier of this Task.
        :type: str
        """
        self._identifier = identifier

    @property
    def input_ports(self):
        """
        Gets the input_ports of this Task.
        An array of input ports.


        :return: The input_ports of this Task.
        :rtype: list[InputPort]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """
        Sets the input_ports of this Task.
        An array of input ports.


        :param input_ports: The input_ports of this Task.
        :type: list[InputPort]
        """
        self._input_ports = input_ports

    @property
    def output_ports(self):
        """
        Gets the output_ports of this Task.
        An array of output ports.


        :return: The output_ports of this Task.
        :rtype: list[OutputPort]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """
        Sets the output_ports of this Task.
        An array of output ports.


        :param output_ports: The output_ports of this Task.
        :type: list[OutputPort]
        """
        self._output_ports = output_ports

    @property
    def parameters(self):
        """
        Gets the parameters of this Task.
        An array of parameters.


        :return: The parameters of this Task.
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Task.
        An array of parameters.


        :param parameters: The parameters of this Task.
        :type: list[Parameter]
        """
        self._parameters = parameters

    @property
    def op_config_values(self):
        """
        Gets the op_config_values of this Task.

        :return: The op_config_values of this Task.
        :rtype: ConfigValues
        """
        return self._op_config_values

    @op_config_values.setter
    def op_config_values(self, op_config_values):
        """
        Sets the op_config_values of this Task.

        :param op_config_values: The op_config_values of this Task.
        :type: ConfigValues
        """
        self._op_config_values = op_config_values

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this Task.

        :return: The config_provider_delegate of this Task.
        :rtype: ConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this Task.

        :param config_provider_delegate: The config_provider_delegate of this Task.
        :type: ConfigProvider
        """
        self._config_provider_delegate = config_provider_delegate

    @property
    def metadata(self):
        """
        Gets the metadata of this Task.

        :return: The metadata of this Task.
        :rtype: ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Task.

        :param metadata: The metadata of this Task.
        :type: ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this Task.
        A map, if provided key is replaced with generated key, this structure provides mapping between user provided key and generated key


        :return: The key_map of this Task.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this Task.
        A map, if provided key is replaced with generated key, this structure provides mapping between user provided key and generated key


        :param key_map: The key_map of this Task.
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
