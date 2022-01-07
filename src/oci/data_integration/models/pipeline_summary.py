# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineSummary(object):
    """
    The pipeline summary type contains the audit summary information and the definition of the pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this PipelineSummary.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this PipelineSummary.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this PipelineSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this PipelineSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this PipelineSummary.
        :type description: str

        :param model_type:
            The value to assign to the model_type property of this PipelineSummary.
        :type model_type: str

        :param object_version:
            The value to assign to the object_version property of this PipelineSummary.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this PipelineSummary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this PipelineSummary.
        :type identifier: str

        :param nodes:
            The value to assign to the nodes property of this PipelineSummary.
        :type nodes: list[oci.data_integration.models.FlowNode]

        :param parameters:
            The value to assign to the parameters property of this PipelineSummary.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param flow_config_values:
            The value to assign to the flow_config_values property of this PipelineSummary.
        :type flow_config_values: oci.data_integration.models.ConfigValues

        :param variables:
            The value to assign to the variables property of this PipelineSummary.
        :type variables: list[oci.data_integration.models.Variable]

        :param metadata:
            The value to assign to the metadata property of this PipelineSummary.
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
        Gets the key of this PipelineSummary.
        Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.


        :return: The key of this PipelineSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PipelineSummary.
        Generated key that can be used in API calls to identify pipeline. On scenarios where reference to the pipeline is needed, a value can be passed in create.


        :param key: The key of this PipelineSummary.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this PipelineSummary.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :return: The model_version of this PipelineSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this PipelineSummary.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :param model_version: The model_version of this PipelineSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this PipelineSummary.

        :return: The parent_ref of this PipelineSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this PipelineSummary.

        :param parent_ref: The parent_ref of this PipelineSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this PipelineSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this PipelineSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PipelineSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this PipelineSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this PipelineSummary.
        Detailed description for the object.


        :return: The description of this PipelineSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PipelineSummary.
        Detailed description for the object.


        :param description: The description of this PipelineSummary.
        :type: str
        """
        self._description = description

    @property
    def model_type(self):
        """
        Gets the model_type of this PipelineSummary.
        The type of the object.


        :return: The model_type of this PipelineSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this PipelineSummary.
        The type of the object.


        :param model_type: The model_type of this PipelineSummary.
        :type: str
        """
        self._model_type = model_type

    @property
    def object_version(self):
        """
        Gets the object_version of this PipelineSummary.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :return: The object_version of this PipelineSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this PipelineSummary.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :param object_version: The object_version of this PipelineSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this PipelineSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this PipelineSummary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this PipelineSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this PipelineSummary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this PipelineSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this PipelineSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this PipelineSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this PipelineSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def nodes(self):
        """
        Gets the nodes of this PipelineSummary.
        A list of nodes attached to the pipeline.


        :return: The nodes of this PipelineSummary.
        :rtype: list[oci.data_integration.models.FlowNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this PipelineSummary.
        A list of nodes attached to the pipeline.


        :param nodes: The nodes of this PipelineSummary.
        :type: list[oci.data_integration.models.FlowNode]
        """
        self._nodes = nodes

    @property
    def parameters(self):
        """
        Gets the parameters of this PipelineSummary.
        A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.


        :return: The parameters of this PipelineSummary.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this PipelineSummary.
        A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.


        :param parameters: The parameters of this PipelineSummary.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def flow_config_values(self):
        """
        Gets the flow_config_values of this PipelineSummary.

        :return: The flow_config_values of this PipelineSummary.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._flow_config_values

    @flow_config_values.setter
    def flow_config_values(self, flow_config_values):
        """
        Sets the flow_config_values of this PipelineSummary.

        :param flow_config_values: The flow_config_values of this PipelineSummary.
        :type: oci.data_integration.models.ConfigValues
        """
        self._flow_config_values = flow_config_values

    @property
    def variables(self):
        """
        Gets the variables of this PipelineSummary.
        The list of variables required in pipeline, variables can be used to store values that can be used as inputs to tasks in the pipeline.


        :return: The variables of this PipelineSummary.
        :rtype: list[oci.data_integration.models.Variable]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this PipelineSummary.
        The list of variables required in pipeline, variables can be used to store values that can be used as inputs to tasks in the pipeline.


        :param variables: The variables of this PipelineSummary.
        :type: list[oci.data_integration.models.Variable]
        """
        self._variables = variables

    @property
    def metadata(self):
        """
        Gets the metadata of this PipelineSummary.

        :return: The metadata of this PipelineSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this PipelineSummary.

        :param metadata: The metadata of this PipelineSummary.
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
