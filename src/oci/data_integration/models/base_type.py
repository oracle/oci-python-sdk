# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseType(object):
    """
    Base type for the type system.
    """

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "DYNAMIC_TYPE"
    MODEL_TYPE_DYNAMIC_TYPE = "DYNAMIC_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "STRUCTURED_TYPE"
    MODEL_TYPE_STRUCTURED_TYPE = "STRUCTURED_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "DATA_TYPE"
    MODEL_TYPE_DATA_TYPE = "DATA_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "JAVA_TYPE"
    MODEL_TYPE_JAVA_TYPE = "JAVA_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "CONFIGURED_TYPE"
    MODEL_TYPE_CONFIGURED_TYPE = "CONFIGURED_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "COMPOSITE_TYPE"
    MODEL_TYPE_COMPOSITE_TYPE = "COMPOSITE_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "DERIVED_TYPE"
    MODEL_TYPE_DERIVED_TYPE = "DERIVED_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "ARRAY_TYPE"
    MODEL_TYPE_ARRAY_TYPE = "ARRAY_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "MAP_TYPE"
    MODEL_TYPE_MAP_TYPE = "MAP_TYPE"

    #: A constant which can be used with the model_type property of a BaseType.
    #: This constant has a value of "MATERIALIZED_COMPOSITE_TYPE"
    MODEL_TYPE_MATERIALIZED_COMPOSITE_TYPE = "MATERIALIZED_COMPOSITE_TYPE"

    def __init__(self, **kwargs):
        """
        Initializes a new BaseType object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_integration.models.ArrayType`
        * :class:`~oci.data_integration.models.ConfiguredType`
        * :class:`~oci.data_integration.models.JavaType`
        * :class:`~oci.data_integration.models.DynamicType`
        * :class:`~oci.data_integration.models.DerivedType`
        * :class:`~oci.data_integration.models.DataType`
        * :class:`~oci.data_integration.models.MaterializedCompositeType`
        * :class:`~oci.data_integration.models.MapType`
        * :class:`~oci.data_integration.models.CompositeType`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this BaseType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", "ARRAY_TYPE", "MAP_TYPE", "MATERIALIZED_COMPOSITE_TYPE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this BaseType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this BaseType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this BaseType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this BaseType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this BaseType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this BaseType.
        :type description: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_status': 'int',
            'description': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_status': 'objectStatus',
            'description': 'description'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'ARRAY_TYPE':
            return 'ArrayType'

        if type == 'CONFIGURED_TYPE':
            return 'ConfiguredType'

        if type == 'JAVA_TYPE':
            return 'JavaType'

        if type == 'DYNAMIC_TYPE':
            return 'DynamicType'

        if type == 'DERIVED_TYPE':
            return 'DerivedType'

        if type == 'DATA_TYPE':
            return 'DataType'

        if type == 'MATERIALIZED_COMPOSITE_TYPE':
            return 'MaterializedCompositeType'

        if type == 'MAP_TYPE':
            return 'MapType'

        if type == 'COMPOSITE_TYPE':
            return 'CompositeType'
        else:
            return 'BaseType'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this BaseType.
        The property which disciminates the subtypes.

        Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", "ARRAY_TYPE", "MAP_TYPE", "MATERIALIZED_COMPOSITE_TYPE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this BaseType.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this BaseType.
        The property which disciminates the subtypes.


        :param model_type: The model_type of this BaseType.
        :type: str
        """
        allowed_values = ["DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", "ARRAY_TYPE", "MAP_TYPE", "MATERIALIZED_COMPOSITE_TYPE"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this BaseType.
        The key of the object.


        :return: The key of this BaseType.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this BaseType.
        The key of the object.


        :param key: The key of this BaseType.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this BaseType.
        The model version of an object.


        :return: The model_version of this BaseType.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this BaseType.
        The model version of an object.


        :param model_version: The model_version of this BaseType.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this BaseType.

        :return: The parent_ref of this BaseType.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this BaseType.

        :param parent_ref: The parent_ref of this BaseType.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this BaseType.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this BaseType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BaseType.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this BaseType.
        :type: str
        """
        self._name = name

    @property
    def object_status(self):
        """
        Gets the object_status of this BaseType.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this BaseType.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this BaseType.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this BaseType.
        :type: int
        """
        self._object_status = object_status

    @property
    def description(self):
        """
        Gets the description of this BaseType.
        A user defined description for the object.


        :return: The description of this BaseType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BaseType.
        A user defined description for the object.


        :param description: The description of this BaseType.
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
