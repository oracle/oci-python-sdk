# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateUserDefinedFunctionDetails(object):
    """
    Properties used in user defined function update operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateUserDefinedFunctionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parent_ref:
            The value to assign to the parent_ref property of this UpdateUserDefinedFunctionDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this UpdateUserDefinedFunctionDetails.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this UpdateUserDefinedFunctionDetails.
        :type identifier: str

        :param model_version:
            The value to assign to the model_version property of this UpdateUserDefinedFunctionDetails.
        :type model_version: str

        :param object_version:
            The value to assign to the object_version property of this UpdateUserDefinedFunctionDetails.
        :type object_version: int

        :param signatures:
            The value to assign to the signatures property of this UpdateUserDefinedFunctionDetails.
        :type signatures: list[oci.data_integration.models.FunctionSignature]

        :param expr:
            The value to assign to the expr property of this UpdateUserDefinedFunctionDetails.
        :type expr: oci.data_integration.models.Expression

        :param description:
            The value to assign to the description property of this UpdateUserDefinedFunctionDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UpdateUserDefinedFunctionDetails.
        :type object_status: int

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateUserDefinedFunctionDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'parent_ref': 'ParentReference',
            'name': 'str',
            'identifier': 'str',
            'model_version': 'str',
            'object_version': 'int',
            'signatures': 'list[FunctionSignature]',
            'expr': 'Expression',
            'description': 'str',
            'object_status': 'int',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'parent_ref': 'parentRef',
            'name': 'name',
            'identifier': 'identifier',
            'model_version': 'modelVersion',
            'object_version': 'objectVersion',
            'signatures': 'signatures',
            'expr': 'expr',
            'description': 'description',
            'object_status': 'objectStatus',
            'registry_metadata': 'registryMetadata'
        }

        self._parent_ref = None
        self._name = None
        self._identifier = None
        self._model_version = None
        self._object_version = None
        self._signatures = None
        self._expr = None
        self._description = None
        self._object_status = None
        self._registry_metadata = None

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this UpdateUserDefinedFunctionDetails.

        :return: The parent_ref of this UpdateUserDefinedFunctionDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this UpdateUserDefinedFunctionDetails.

        :param parent_ref: The parent_ref of this UpdateUserDefinedFunctionDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this UpdateUserDefinedFunctionDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this UpdateUserDefinedFunctionDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateUserDefinedFunctionDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this UpdateUserDefinedFunctionDetails.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this UpdateUserDefinedFunctionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this UpdateUserDefinedFunctionDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this UpdateUserDefinedFunctionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this UpdateUserDefinedFunctionDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def model_version(self):
        """
        Gets the model_version of this UpdateUserDefinedFunctionDetails.
        The model version of an object.


        :return: The model_version of this UpdateUserDefinedFunctionDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this UpdateUserDefinedFunctionDetails.
        The model version of an object.


        :param model_version: The model_version of this UpdateUserDefinedFunctionDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def object_version(self):
        """
        Gets the object_version of this UpdateUserDefinedFunctionDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this UpdateUserDefinedFunctionDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this UpdateUserDefinedFunctionDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this UpdateUserDefinedFunctionDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def signatures(self):
        """
        Gets the signatures of this UpdateUserDefinedFunctionDetails.
        An array of function signature.


        :return: The signatures of this UpdateUserDefinedFunctionDetails.
        :rtype: list[oci.data_integration.models.FunctionSignature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """
        Sets the signatures of this UpdateUserDefinedFunctionDetails.
        An array of function signature.


        :param signatures: The signatures of this UpdateUserDefinedFunctionDetails.
        :type: list[oci.data_integration.models.FunctionSignature]
        """
        self._signatures = signatures

    @property
    def expr(self):
        """
        Gets the expr of this UpdateUserDefinedFunctionDetails.

        :return: The expr of this UpdateUserDefinedFunctionDetails.
        :rtype: oci.data_integration.models.Expression
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """
        Sets the expr of this UpdateUserDefinedFunctionDetails.

        :param expr: The expr of this UpdateUserDefinedFunctionDetails.
        :type: oci.data_integration.models.Expression
        """
        self._expr = expr

    @property
    def description(self):
        """
        Gets the description of this UpdateUserDefinedFunctionDetails.
        Detailed description for the object.


        :return: The description of this UpdateUserDefinedFunctionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateUserDefinedFunctionDetails.
        Detailed description for the object.


        :param description: The description of this UpdateUserDefinedFunctionDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this UpdateUserDefinedFunctionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this UpdateUserDefinedFunctionDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this UpdateUserDefinedFunctionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this UpdateUserDefinedFunctionDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this UpdateUserDefinedFunctionDetails.

        :return: The registry_metadata of this UpdateUserDefinedFunctionDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this UpdateUserDefinedFunctionDetails.

        :param registry_metadata: The registry_metadata of this UpdateUserDefinedFunctionDetails.
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
