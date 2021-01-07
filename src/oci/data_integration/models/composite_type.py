# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompositeType(BaseType):
    """
    A `CompositeType` represents a type that is composed of a list of sub-types, for example an `Address` type.   The sub-types can be simple `DataType` or other `CompositeType` objects. Typically, a `CompositeType` may represent an arbitrarily deep hierarchy of types.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompositeType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CompositeType.model_type` attribute
        of this class is ``COMPOSITE_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CompositeType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CompositeType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CompositeType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CompositeType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CompositeType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this CompositeType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this CompositeType.
        :type description: str

        :param parent_type:
            The value to assign to the parent_type property of this CompositeType.
        :type parent_type: oci.data_integration.models.CompositeType

        :param elements:
            The value to assign to the elements property of this CompositeType.
        :type elements: list[oci.data_integration.models.TypedObject]

        :param config_definition:
            The value to assign to the config_definition property of this CompositeType.
        :type config_definition: oci.data_integration.models.ConfigDefinition

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_status': 'int',
            'description': 'str',
            'parent_type': 'CompositeType',
            'elements': 'list[TypedObject]',
            'config_definition': 'ConfigDefinition'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_status': 'objectStatus',
            'description': 'description',
            'parent_type': 'parentType',
            'elements': 'elements',
            'config_definition': 'configDefinition'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._parent_type = None
        self._elements = None
        self._config_definition = None
        self._model_type = 'COMPOSITE_TYPE'

    @property
    def parent_type(self):
        """
        Gets the parent_type of this CompositeType.

        :return: The parent_type of this CompositeType.
        :rtype: oci.data_integration.models.CompositeType
        """
        return self._parent_type

    @parent_type.setter
    def parent_type(self, parent_type):
        """
        Sets the parent_type of this CompositeType.

        :param parent_type: The parent_type of this CompositeType.
        :type: oci.data_integration.models.CompositeType
        """
        self._parent_type = parent_type

    @property
    def elements(self):
        """
        Gets the elements of this CompositeType.
        An array of elements.


        :return: The elements of this CompositeType.
        :rtype: list[oci.data_integration.models.TypedObject]
        """
        return self._elements

    @elements.setter
    def elements(self, elements):
        """
        Sets the elements of this CompositeType.
        An array of elements.


        :param elements: The elements of this CompositeType.
        :type: list[oci.data_integration.models.TypedObject]
        """
        self._elements = elements

    @property
    def config_definition(self):
        """
        Gets the config_definition of this CompositeType.

        :return: The config_definition of this CompositeType.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._config_definition

    @config_definition.setter
    def config_definition(self, config_definition):
        """
        Sets the config_definition of this CompositeType.

        :param config_definition: The config_definition of this CompositeType.
        :type: oci.data_integration.models.ConfigDefinition
        """
        self._config_definition = config_definition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
