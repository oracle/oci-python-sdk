# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTaskDetails(object):
    """
    Properties used in task create operations.
    """

    #: A constant which can be used with the model_type property of a CreateTaskDetails.
    #: This constant has a value of "INTEGRATION_TASK"
    MODEL_TYPE_INTEGRATION_TASK = "INTEGRATION_TASK"

    #: A constant which can be used with the model_type property of a CreateTaskDetails.
    #: This constant has a value of "DATA_LOADER_TASK"
    MODEL_TYPE_DATA_LOADER_TASK = "DATA_LOADER_TASK"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTaskDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.CreateTaskFromIntegrationTask`
        * :class:`~oci.data_integration.models.CreateTaskFromDataLoaderTask`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateTaskDetails.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateTaskDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateTaskDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateTaskDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateTaskDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateTaskDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateTaskDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateTaskDetails.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this CreateTaskDetails.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this CreateTaskDetails.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this CreateTaskDetails.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this CreateTaskDetails.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this CreateTaskDetails.
        :type config_provider_delegate: oci.data_integration.models.CreateConfigProvider

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateTaskDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

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
            'registry_metadata': 'RegistryMetadata'
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
            'registry_metadata': 'registryMetadata'
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'INTEGRATION_TASK':
            return 'CreateTaskFromIntegrationTask'

        if type == 'DATA_LOADER_TASK':
            return 'CreateTaskFromDataLoaderTask'
        else:
            return 'CreateTaskDetails'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this CreateTaskDetails.
        The type of the task.

        Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK"


        :return: The model_type of this CreateTaskDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateTaskDetails.
        The type of the task.


        :param model_type: The model_type of this CreateTaskDetails.
        :type: str
        """
        allowed_values = ["INTEGRATION_TASK", "DATA_LOADER_TASK"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this CreateTaskDetails.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :return: The key of this CreateTaskDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateTaskDetails.
        Generated key that can be used in API calls to identify task. On scenarios where reference to the task is needed, a value can be passed in create.


        :param key: The key of this CreateTaskDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateTaskDetails.
        The object's model version.


        :return: The model_version of this CreateTaskDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateTaskDetails.
        The object's model version.


        :param model_version: The model_version of this CreateTaskDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CreateTaskDetails.

        :return: The parent_ref of this CreateTaskDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CreateTaskDetails.

        :param parent_ref: The parent_ref of this CreateTaskDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateTaskDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateTaskDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateTaskDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateTaskDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateTaskDetails.
        Detailed description for the object.


        :return: The description of this CreateTaskDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTaskDetails.
        Detailed description for the object.


        :param description: The description of this CreateTaskDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateTaskDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateTaskDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateTaskDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateTaskDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateTaskDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateTaskDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateTaskDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateTaskDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def input_ports(self):
        """
        Gets the input_ports of this CreateTaskDetails.
        An array of input ports.


        :return: The input_ports of this CreateTaskDetails.
        :rtype: list[oci.data_integration.models.InputPort]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """
        Sets the input_ports of this CreateTaskDetails.
        An array of input ports.


        :param input_ports: The input_ports of this CreateTaskDetails.
        :type: list[oci.data_integration.models.InputPort]
        """
        self._input_ports = input_ports

    @property
    def output_ports(self):
        """
        Gets the output_ports of this CreateTaskDetails.
        An array of output ports.


        :return: The output_ports of this CreateTaskDetails.
        :rtype: list[oci.data_integration.models.OutputPort]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """
        Sets the output_ports of this CreateTaskDetails.
        An array of output ports.


        :param output_ports: The output_ports of this CreateTaskDetails.
        :type: list[oci.data_integration.models.OutputPort]
        """
        self._output_ports = output_ports

    @property
    def parameters(self):
        """
        Gets the parameters of this CreateTaskDetails.
        An array of parameters.


        :return: The parameters of this CreateTaskDetails.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateTaskDetails.
        An array of parameters.


        :param parameters: The parameters of this CreateTaskDetails.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def op_config_values(self):
        """
        Gets the op_config_values of this CreateTaskDetails.

        :return: The op_config_values of this CreateTaskDetails.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._op_config_values

    @op_config_values.setter
    def op_config_values(self, op_config_values):
        """
        Sets the op_config_values of this CreateTaskDetails.

        :param op_config_values: The op_config_values of this CreateTaskDetails.
        :type: oci.data_integration.models.ConfigValues
        """
        self._op_config_values = op_config_values

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this CreateTaskDetails.

        :return: The config_provider_delegate of this CreateTaskDetails.
        :rtype: oci.data_integration.models.CreateConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this CreateTaskDetails.

        :param config_provider_delegate: The config_provider_delegate of this CreateTaskDetails.
        :type: oci.data_integration.models.CreateConfigProvider
        """
        self._config_provider_delegate = config_provider_delegate

    @property
    def registry_metadata(self):
        """
        **[Required]** Gets the registry_metadata of this CreateTaskDetails.

        :return: The registry_metadata of this CreateTaskDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateTaskDetails.

        :param registry_metadata: The registry_metadata of this CreateTaskDetails.
        :type: oci.data_integration.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
