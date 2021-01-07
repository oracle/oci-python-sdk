# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FlowNode(object):
    """
    The flow node can be connected to other nodes in a data flow with input and output links and is bound to an opertor which defines the semantics of the node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FlowNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this FlowNode.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this FlowNode.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this FlowNode.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this FlowNode.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this FlowNode.
        :type name: str

        :param description:
            The value to assign to the description property of this FlowNode.
        :type description: str

        :param input_links:
            The value to assign to the input_links property of this FlowNode.
        :type input_links: list[oci.data_integration.models.InputLink]

        :param output_links:
            The value to assign to the output_links property of this FlowNode.
        :type output_links: list[oci.data_integration.models.OutputLink]

        :param operator:
            The value to assign to the operator property of this FlowNode.
        :type operator: oci.data_integration.models.Operator

        :param ui_properties:
            The value to assign to the ui_properties property of this FlowNode.
        :type ui_properties: oci.data_integration.models.UIProperties

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this FlowNode.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param object_status:
            The value to assign to the object_status property of this FlowNode.
        :type object_status: int

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'input_links': 'list[InputLink]',
            'output_links': 'list[OutputLink]',
            'operator': 'Operator',
            'ui_properties': 'UIProperties',
            'config_provider_delegate': 'ConfigProvider',
            'object_status': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'input_links': 'inputLinks',
            'output_links': 'outputLinks',
            'operator': 'operator',
            'ui_properties': 'uiProperties',
            'config_provider_delegate': 'configProviderDelegate',
            'object_status': 'objectStatus'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._input_links = None
        self._output_links = None
        self._operator = None
        self._ui_properties = None
        self._config_provider_delegate = None
        self._object_status = None

    @property
    def key(self):
        """
        Gets the key of this FlowNode.
        The key of the object.


        :return: The key of this FlowNode.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FlowNode.
        The key of the object.


        :param key: The key of this FlowNode.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this FlowNode.
        The type of the object.


        :return: The model_type of this FlowNode.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this FlowNode.
        The type of the object.


        :param model_type: The model_type of this FlowNode.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this FlowNode.
        The model version of an object.


        :return: The model_version of this FlowNode.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this FlowNode.
        The model version of an object.


        :param model_version: The model_version of this FlowNode.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this FlowNode.

        :return: The parent_ref of this FlowNode.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this FlowNode.

        :param parent_ref: The parent_ref of this FlowNode.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this FlowNode.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this FlowNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FlowNode.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this FlowNode.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FlowNode.
        Detailed description for the object.


        :return: The description of this FlowNode.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FlowNode.
        Detailed description for the object.


        :param description: The description of this FlowNode.
        :type: str
        """
        self._description = description

    @property
    def input_links(self):
        """
        Gets the input_links of this FlowNode.
        An array of input links.


        :return: The input_links of this FlowNode.
        :rtype: list[oci.data_integration.models.InputLink]
        """
        return self._input_links

    @input_links.setter
    def input_links(self, input_links):
        """
        Sets the input_links of this FlowNode.
        An array of input links.


        :param input_links: The input_links of this FlowNode.
        :type: list[oci.data_integration.models.InputLink]
        """
        self._input_links = input_links

    @property
    def output_links(self):
        """
        Gets the output_links of this FlowNode.
        An array of output links.


        :return: The output_links of this FlowNode.
        :rtype: list[oci.data_integration.models.OutputLink]
        """
        return self._output_links

    @output_links.setter
    def output_links(self, output_links):
        """
        Sets the output_links of this FlowNode.
        An array of output links.


        :param output_links: The output_links of this FlowNode.
        :type: list[oci.data_integration.models.OutputLink]
        """
        self._output_links = output_links

    @property
    def operator(self):
        """
        Gets the operator of this FlowNode.

        :return: The operator of this FlowNode.
        :rtype: oci.data_integration.models.Operator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this FlowNode.

        :param operator: The operator of this FlowNode.
        :type: oci.data_integration.models.Operator
        """
        self._operator = operator

    @property
    def ui_properties(self):
        """
        Gets the ui_properties of this FlowNode.

        :return: The ui_properties of this FlowNode.
        :rtype: oci.data_integration.models.UIProperties
        """
        return self._ui_properties

    @ui_properties.setter
    def ui_properties(self, ui_properties):
        """
        Sets the ui_properties of this FlowNode.

        :param ui_properties: The ui_properties of this FlowNode.
        :type: oci.data_integration.models.UIProperties
        """
        self._ui_properties = ui_properties

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this FlowNode.

        :return: The config_provider_delegate of this FlowNode.
        :rtype: oci.data_integration.models.ConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this FlowNode.

        :param config_provider_delegate: The config_provider_delegate of this FlowNode.
        :type: oci.data_integration.models.ConfigProvider
        """
        self._config_provider_delegate = config_provider_delegate

    @property
    def object_status(self):
        """
        Gets the object_status of this FlowNode.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this FlowNode.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this FlowNode.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this FlowNode.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
