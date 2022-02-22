# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectivityValidationDetails(object):
    """
    Input to perform connector validation. If defines some data integration semantics in a data flow. It may be reading/writing data or transforming the data.
    """

    #: A constant which can be used with the model_type property of a CreateConnectivityValidationDetails.
    #: This constant has a value of "SOURCE_OPERATOR"
    MODEL_TYPE_SOURCE_OPERATOR = "SOURCE_OPERATOR"

    #: A constant which can be used with the model_type property of a CreateConnectivityValidationDetails.
    #: This constant has a value of "TARGET_OPERATOR"
    MODEL_TYPE_TARGET_OPERATOR = "TARGET_OPERATOR"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectivityValidationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.Target`
        * :class:`~oci.data_connectivity.models.Source`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateConnectivityValidationDetails.
            Allowed values for this property are: "SOURCE_OPERATOR", "TARGET_OPERATOR"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateConnectivityValidationDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateConnectivityValidationDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateConnectivityValidationDetails.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateConnectivityValidationDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateConnectivityValidationDetails.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this CreateConnectivityValidationDetails.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this CreateConnectivityValidationDetails.
        :type input_ports: list[oci.data_connectivity.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this CreateConnectivityValidationDetails.
        :type output_ports: list[oci.data_connectivity.models.OutputPort]

        :param object_status:
            The value to assign to the object_status property of this CreateConnectivityValidationDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateConnectivityValidationDetails.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this CreateConnectivityValidationDetails.
        :type parameters: list[oci.data_connectivity.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this CreateConnectivityValidationDetails.
        :type op_config_values: oci.data_connectivity.models.ConfigValues

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
            'op_config_values': 'ConfigValues'
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
            'op_config_values': 'opConfigValues'
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'TARGET_OPERATOR':
            return 'Target'

        if type == 'SOURCE_OPERATOR':
            return 'Source'
        else:
            return 'CreateConnectivityValidationDetails'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this CreateConnectivityValidationDetails.
        The model type of the operator.

        Allowed values for this property are: "SOURCE_OPERATOR", "TARGET_OPERATOR"


        :return: The model_type of this CreateConnectivityValidationDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateConnectivityValidationDetails.
        The model type of the operator.


        :param model_type: The model_type of this CreateConnectivityValidationDetails.
        :type: str
        """
        allowed_values = ["SOURCE_OPERATOR", "TARGET_OPERATOR"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this CreateConnectivityValidationDetails.
        The key of the object.


        :return: The key of this CreateConnectivityValidationDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateConnectivityValidationDetails.
        The key of the object.


        :param key: The key of this CreateConnectivityValidationDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateConnectivityValidationDetails.
        The model version of an object.


        :return: The model_version of this CreateConnectivityValidationDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateConnectivityValidationDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateConnectivityValidationDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CreateConnectivityValidationDetails.

        :return: The parent_ref of this CreateConnectivityValidationDetails.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CreateConnectivityValidationDetails.

        :param parent_ref: The parent_ref of this CreateConnectivityValidationDetails.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this CreateConnectivityValidationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateConnectivityValidationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateConnectivityValidationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateConnectivityValidationDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateConnectivityValidationDetails.
        Details about the operator.


        :return: The description of this CreateConnectivityValidationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateConnectivityValidationDetails.
        Details about the operator.


        :param description: The description of this CreateConnectivityValidationDetails.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this CreateConnectivityValidationDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this CreateConnectivityValidationDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CreateConnectivityValidationDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this CreateConnectivityValidationDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def input_ports(self):
        """
        Gets the input_ports of this CreateConnectivityValidationDetails.
        An array of input ports.


        :return: The input_ports of this CreateConnectivityValidationDetails.
        :rtype: list[oci.data_connectivity.models.InputPort]
        """
        return self._input_ports

    @input_ports.setter
    def input_ports(self, input_ports):
        """
        Sets the input_ports of this CreateConnectivityValidationDetails.
        An array of input ports.


        :param input_ports: The input_ports of this CreateConnectivityValidationDetails.
        :type: list[oci.data_connectivity.models.InputPort]
        """
        self._input_ports = input_ports

    @property
    def output_ports(self):
        """
        Gets the output_ports of this CreateConnectivityValidationDetails.
        An array of output ports.


        :return: The output_ports of this CreateConnectivityValidationDetails.
        :rtype: list[oci.data_connectivity.models.OutputPort]
        """
        return self._output_ports

    @output_ports.setter
    def output_ports(self, output_ports):
        """
        Sets the output_ports of this CreateConnectivityValidationDetails.
        An array of output ports.


        :param output_ports: The output_ports of this CreateConnectivityValidationDetails.
        :type: list[oci.data_connectivity.models.OutputPort]
        """
        self._output_ports = output_ports

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateConnectivityValidationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateConnectivityValidationDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateConnectivityValidationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateConnectivityValidationDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this CreateConnectivityValidationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateConnectivityValidationDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateConnectivityValidationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateConnectivityValidationDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def parameters(self):
        """
        Gets the parameters of this CreateConnectivityValidationDetails.
        An array of parameters used in the data flow.


        :return: The parameters of this CreateConnectivityValidationDetails.
        :rtype: list[oci.data_connectivity.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateConnectivityValidationDetails.
        An array of parameters used in the data flow.


        :param parameters: The parameters of this CreateConnectivityValidationDetails.
        :type: list[oci.data_connectivity.models.Parameter]
        """
        self._parameters = parameters

    @property
    def op_config_values(self):
        """
        Gets the op_config_values of this CreateConnectivityValidationDetails.

        :return: The op_config_values of this CreateConnectivityValidationDetails.
        :rtype: oci.data_connectivity.models.ConfigValues
        """
        return self._op_config_values

    @op_config_values.setter
    def op_config_values(self, op_config_values):
        """
        Sets the op_config_values of this CreateConnectivityValidationDetails.

        :param op_config_values: The op_config_values of this CreateConnectivityValidationDetails.
        :type: oci.data_connectivity.models.ConfigValues
        """
        self._op_config_values = op_config_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
