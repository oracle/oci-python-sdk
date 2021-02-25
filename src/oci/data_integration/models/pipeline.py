# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Pipeline(object):
    """
    A pipeline is a logical grouping of tasks that together perform a higher level operation. For example, a pipeline could contain a set of tasks that load and clean data, then execute a dataflow to analyze the data. The pipeline allows you to manage the activities as a unit instead of individually. Users can also schedule the pipeline instead of the tasks independently.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Pipeline object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Pipeline.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Pipeline.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Pipeline.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Pipeline.
        :type name: str

        :param description:
            The value to assign to the description property of this Pipeline.
        :type description: str

        :param model_type:
            The value to assign to the model_type property of this Pipeline.
        :type model_type: str

        :param object_version:
            The value to assign to the object_version property of this Pipeline.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this Pipeline.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Pipeline.
        :type identifier: str

        :param nodes:
            The value to assign to the nodes property of this Pipeline.
        :type nodes: list[oci.data_integration.models.FlowNode]

        :param parameters:
            The value to assign to the parameters property of this Pipeline.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param flow_config_values:
            The value to assign to the flow_config_values property of this Pipeline.
        :type flow_config_values: oci.data_integration.models.ConfigValues

        :param variables:
            The value to assign to the variables property of this Pipeline.
        :type variables: list[oci.data_integration.models.Variable]

        :param metadata:
            The value to assign to the metadata property of this Pipeline.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'model_type': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'nodes': 'list[FlowNode]',
            'parameters': 'list[Parameter]',
            'flow_config_values': 'ConfigValues',
            'variables': 'list[Variable]',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'model_type': 'modelType',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'nodes': 'nodes',
            'parameters': 'parameters',
            'flow_config_values': 'flowConfigValues',
            'variables': 'variables',
            'metadata': 'metadata'
        }

        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._model_type = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._nodes = None
        self._parameters = None
        self._flow_config_values = None
        self._variables = None
        self._metadata = None

    @property
    def key(self):
        """
        Gets the key of this Pipeline.
        Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.


        :return: The key of this Pipeline.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Pipeline.
        Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.


        :param key: The key of this Pipeline.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this Pipeline.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :return: The model_version of this Pipeline.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Pipeline.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :param model_version: The model_version of this Pipeline.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this Pipeline.

        :return: The parent_ref of this Pipeline.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this Pipeline.

        :param parent_ref: The parent_ref of this Pipeline.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this Pipeline.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this Pipeline.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Pipeline.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this Pipeline.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Pipeline.
        Detailed description for the object.


        :return: The description of this Pipeline.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Pipeline.
        Detailed description for the object.


        :param description: The description of this Pipeline.
        :type: str
        """
        self._description = description

    @property
    def model_type(self):
        """
        Gets the model_type of this Pipeline.
        The type of the object.


        :return: The model_type of this Pipeline.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Pipeline.
        The type of the object.


        :param model_type: The model_type of this Pipeline.
        :type: str
        """
        self._model_type = model_type

    @property
    def object_version(self):
        """
        Gets the object_version of this Pipeline.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :return: The object_version of this Pipeline.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this Pipeline.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :param object_version: The object_version of this Pipeline.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this Pipeline.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this Pipeline.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this Pipeline.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this Pipeline.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this Pipeline.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this Pipeline.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Pipeline.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this Pipeline.
        :type: str
        """
        self._identifier = identifier

    @property
    def nodes(self):
        """
        Gets the nodes of this Pipeline.
        A list of nodes attached to the pipeline.


        :return: The nodes of this Pipeline.
        :rtype: list[oci.data_integration.models.FlowNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this Pipeline.
        A list of nodes attached to the pipeline.


        :param nodes: The nodes of this Pipeline.
        :type: list[oci.data_integration.models.FlowNode]
        """
        self._nodes = nodes

    @property
    def parameters(self):
        """
        Gets the parameters of this Pipeline.
        A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.


        :return: The parameters of this Pipeline.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Pipeline.
        A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.


        :param parameters: The parameters of this Pipeline.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def flow_config_values(self):
        """
        Gets the flow_config_values of this Pipeline.

        :return: The flow_config_values of this Pipeline.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._flow_config_values

    @flow_config_values.setter
    def flow_config_values(self, flow_config_values):
        """
        Sets the flow_config_values of this Pipeline.

        :param flow_config_values: The flow_config_values of this Pipeline.
        :type: oci.data_integration.models.ConfigValues
        """
        self._flow_config_values = flow_config_values

    @property
    def variables(self):
        """
        Gets the variables of this Pipeline.
        The list of variables required in pipeline, variables can be used to store values that can be used as inputs to tasks in the pipeline.


        :return: The variables of this Pipeline.
        :rtype: list[oci.data_integration.models.Variable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this Pipeline.
        The list of variables required in pipeline, variables can be used to store values that can be used as inputs to tasks in the pipeline.


        :param variables: The variables of this Pipeline.
        :type: list[oci.data_integration.models.Variable]
        """
        self._variables = variables

    @property
    def metadata(self):
        """
        Gets the metadata of this Pipeline.

        :return: The metadata of this Pipeline.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Pipeline.

        :param metadata: The metadata of this Pipeline.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
