# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypedObject(object):
    """
    The `TypedObject` class is a base class for any model object that has a type.
    """

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "SHAPE"
    MODEL_TYPE_SHAPE = "SHAPE"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "INPUT_PORT"
    MODEL_TYPE_INPUT_PORT = "INPUT_PORT"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "SHAPE_FIELD"
    MODEL_TYPE_SHAPE_FIELD = "SHAPE_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "INPUT_FIELD"
    MODEL_TYPE_INPUT_FIELD = "INPUT_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "DERIVED_FIELD"
    MODEL_TYPE_DERIVED_FIELD = "DERIVED_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "MACRO_FIELD"
    MODEL_TYPE_MACRO_FIELD = "MACRO_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "OUTPUT_FIELD"
    MODEL_TYPE_OUTPUT_FIELD = "OUTPUT_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "DYNAMIC_PROXY_FIELD"
    MODEL_TYPE_DYNAMIC_PROXY_FIELD = "DYNAMIC_PROXY_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "OUTPUT_PORT"
    MODEL_TYPE_OUTPUT_PORT = "OUTPUT_PORT"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "DYNAMIC_INPUT_FIELD"
    MODEL_TYPE_DYNAMIC_INPUT_FIELD = "DYNAMIC_INPUT_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "PROXY_FIELD"
    MODEL_TYPE_PROXY_FIELD = "PROXY_FIELD"

    #: A constant which can be used with the model_type property of a TypedObject.
    #: This constant has a value of "PARAMETER"
    MODEL_TYPE_PARAMETER = "PARAMETER"

    def __init__(self, **kwargs):
        """
        Initializes a new TypedObject object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.OutputPort`
        * :class:`~oci.data_integration.models.DynamicInputField`
        * :class:`~oci.data_integration.models.AbstractField`
        * :class:`~oci.data_integration.models.InputField`
        * :class:`~oci.data_integration.models.Shape`
        * :class:`~oci.data_integration.models.InputPort`
        * :class:`~oci.data_integration.models.ProxyField`
        * :class:`~oci.data_integration.models.DynamicProxyField`
        * :class:`~oci.data_integration.models.ShapeField`
        * :class:`~oci.data_integration.models.Parameter`
        * :class:`~oci.data_integration.models.OutputField`
        * :class:`~oci.data_integration.models.MacroField`
        * :class:`~oci.data_integration.models.DerivedField`
        * :class:`~oci.data_integration.models.FlowPort`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TypedObject.
            Allowed values for this property are: "SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "MACRO_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this TypedObject.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TypedObject.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TypedObject.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this TypedObject.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this TypedObject.
        :type object_status: int

        :param name:
            The value to assign to the name property of this TypedObject.
        :type name: str

        :param description:
            The value to assign to the description property of this TypedObject.
        :type description: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'name': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'name': 'name',
            'description': 'description'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._name = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'OUTPUT_PORT':
            return 'OutputPort'

        if type == 'DYNAMIC_INPUT_FIELD':
            return 'DynamicInputField'

        if type == 'FIELD':
            return 'AbstractField'

        if type == 'INPUT_FIELD':
            return 'InputField'

        if type == 'SHAPE':
            return 'Shape'

        if type == 'INPUT_PORT':
            return 'InputPort'

        if type == 'PROXY_FIELD':
            return 'ProxyField'

        if type == 'DYNAMIC_PROXY_FIELD':
            return 'DynamicProxyField'

        if type == 'SHAPE_FIELD':
            return 'ShapeField'

        if type == 'PARAMETER':
            return 'Parameter'

        if type == 'OUTPUT_FIELD':
            return 'OutputField'

        if type == 'MACRO_FIELD':
            return 'MacroField'

        if type == 'DERIVED_FIELD':
            return 'DerivedField'

        if type == 'FLOW_PORT':
            return 'FlowPort'
        else:
            return 'TypedObject'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this TypedObject.
        The type of the types object.

        Allowed values for this property are: "SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "MACRO_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this TypedObject.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this TypedObject.
        The type of the types object.


        :param model_type: The model_type of this TypedObject.
        :type: str
        """
        allowed_values = ["SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "MACRO_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this TypedObject.
        The key of the object.


        :return: The key of this TypedObject.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TypedObject.
        The key of the object.


        :param key: The key of this TypedObject.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this TypedObject.
        The model version of an object.


        :return: The model_version of this TypedObject.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this TypedObject.
        The model version of an object.


        :param model_version: The model_version of this TypedObject.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this TypedObject.

        :return: The parent_ref of this TypedObject.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this TypedObject.

        :param parent_ref: The parent_ref of this TypedObject.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def config_values(self):
        """
        Gets the config_values of this TypedObject.

        :return: The config_values of this TypedObject.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this TypedObject.

        :param config_values: The config_values of this TypedObject.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this TypedObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this TypedObject.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this TypedObject.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this TypedObject.
        :type: int
        """
        self._object_status = object_status

    @property
    def name(self):
        """
        Gets the name of this TypedObject.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this TypedObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TypedObject.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this TypedObject.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TypedObject.
        Detailed description for the object.


        :return: The description of this TypedObject.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TypedObject.
        Detailed description for the object.


        :param description: The description of this TypedObject.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
