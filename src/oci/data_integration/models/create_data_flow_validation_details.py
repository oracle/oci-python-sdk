# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataFlowValidationDetails(object):
    """
    The information about integration dataflow validation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataFlowValidationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateDataFlowValidationDetails.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this CreateDataFlowValidationDetails.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this CreateDataFlowValidationDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateDataFlowValidationDetails.
        :type parent_ref: ParentReference

        :param name:
            The value to assign to the name property of this CreateDataFlowValidationDetails.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this CreateDataFlowValidationDetails.
        :type identifier: str

        :param object_version:
            The value to assign to the object_version property of this CreateDataFlowValidationDetails.
        :type object_version: int

        :param nodes:
            The value to assign to the nodes property of this CreateDataFlowValidationDetails.
        :type nodes: list[FlowNode]

        :param parameters:
            The value to assign to the parameters property of this CreateDataFlowValidationDetails.
        :type parameters: list[Parameter]

        :param description:
            The value to assign to the description property of this CreateDataFlowValidationDetails.
        :type description: str

        :param flow_config_values:
            The value to assign to the flow_config_values property of this CreateDataFlowValidationDetails.
        :type flow_config_values: ConfigValues

        :param object_status:
            The value to assign to the object_status property of this CreateDataFlowValidationDetails.
        :type object_status: int

        :param metadata:
            The value to assign to the metadata property of this CreateDataFlowValidationDetails.
        :type metadata: ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this CreateDataFlowValidationDetails.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'identifier': 'str',
            'object_version': 'int',
            'nodes': 'list[FlowNode]',
            'parameters': 'list[Parameter]',
            'description': 'str',
            'flow_config_values': 'ConfigValues',
            'object_status': 'int',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'identifier': 'identifier',
            'object_version': 'objectVersion',
            'nodes': 'nodes',
            'parameters': 'parameters',
            'description': 'description',
            'flow_config_values': 'flowConfigValues',
            'object_status': 'objectStatus',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._identifier = None
        self._object_version = None
        self._nodes = None
        self._parameters = None
        self._description = None
        self._flow_config_values = None
        self._object_status = None
        self._metadata = None
        self._key_map = None

    @property
    def key(self):
        """
        Gets the key of this CreateDataFlowValidationDetails.
        Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.


        :return: The key of this CreateDataFlowValidationDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateDataFlowValidationDetails.
        Generated key that can be used in API calls to identify data flow. On scenarios where reference to the data flow is needed, a value can be passed in create.


        :param key: The key of this CreateDataFlowValidationDetails.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateDataFlowValidationDetails.
        The type of the object.


        :return: The model_type of this CreateDataFlowValidationDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateDataFlowValidationDetails.
        The type of the object.


        :param model_type: The model_type of this CreateDataFlowValidationDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateDataFlowValidationDetails.
        The model version of an object.


        :return: The model_version of this CreateDataFlowValidationDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateDataFlowValidationDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateDataFlowValidationDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CreateDataFlowValidationDetails.

        :return: The parent_ref of this CreateDataFlowValidationDetails.
        :rtype: ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CreateDataFlowValidationDetails.

        :param parent_ref: The parent_ref of this CreateDataFlowValidationDetails.
        :type: ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this CreateDataFlowValidationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :return: The name of this CreateDataFlowValidationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateDataFlowValidationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :param name: The name of this CreateDataFlowValidationDetails.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this CreateDataFlowValidationDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :return: The identifier of this CreateDataFlowValidationDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateDataFlowValidationDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :param identifier: The identifier of this CreateDataFlowValidationDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def object_version(self):
        """
        Gets the object_version of this CreateDataFlowValidationDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this CreateDataFlowValidationDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CreateDataFlowValidationDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this CreateDataFlowValidationDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def nodes(self):
        """
        Gets the nodes of this CreateDataFlowValidationDetails.
        An array of nodes.


        :return: The nodes of this CreateDataFlowValidationDetails.
        :rtype: list[FlowNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this CreateDataFlowValidationDetails.
        An array of nodes.


        :param nodes: The nodes of this CreateDataFlowValidationDetails.
        :type: list[FlowNode]
        """
        self._nodes = nodes

    @property
    def parameters(self):
        """
        Gets the parameters of this CreateDataFlowValidationDetails.
        An array of parameters.


        :return: The parameters of this CreateDataFlowValidationDetails.
        :rtype: list[Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateDataFlowValidationDetails.
        An array of parameters.


        :param parameters: The parameters of this CreateDataFlowValidationDetails.
        :type: list[Parameter]
        """
        self._parameters = parameters

    @property
    def description(self):
        """
        Gets the description of this CreateDataFlowValidationDetails.
        Detailed description for the object.


        :return: The description of this CreateDataFlowValidationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDataFlowValidationDetails.
        Detailed description for the object.


        :param description: The description of this CreateDataFlowValidationDetails.
        :type: str
        """
        self._description = description

    @property
    def flow_config_values(self):
        """
        Gets the flow_config_values of this CreateDataFlowValidationDetails.

        :return: The flow_config_values of this CreateDataFlowValidationDetails.
        :rtype: ConfigValues
        """
        return self._flow_config_values

    @flow_config_values.setter
    def flow_config_values(self, flow_config_values):
        """
        Sets the flow_config_values of this CreateDataFlowValidationDetails.

        :param flow_config_values: The flow_config_values of this CreateDataFlowValidationDetails.
        :type: ConfigValues
        """
        self._flow_config_values = flow_config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateDataFlowValidationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateDataFlowValidationDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateDataFlowValidationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateDataFlowValidationDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateDataFlowValidationDetails.

        :return: The metadata of this CreateDataFlowValidationDetails.
        :rtype: ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateDataFlowValidationDetails.

        :param metadata: The metadata of this CreateDataFlowValidationDetails.
        :type: ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this CreateDataFlowValidationDetails.
        A map, if provided key is replaced with generated key, this structure provides mapping between user provided key and generated key


        :return: The key_map of this CreateDataFlowValidationDetails.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this CreateDataFlowValidationDetails.
        A map, if provided key is replaced with generated key, this structure provides mapping between user provided key and generated key


        :param key_map: The key_map of this CreateDataFlowValidationDetails.
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
