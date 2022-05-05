# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .field_map import FieldMap
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConditionalCompositeFieldMap(FieldMap):
    """
    A conditional composite field map.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConditionalCompositeFieldMap object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ConditionalCompositeFieldMap.model_type` attribute
        of this class is ``CONDITIONAL_COMPOSITE_FIELD_MAP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ConditionalCompositeFieldMap.
            Allowed values for this property are: "DIRECT_NAMED_FIELD_MAP", "COMPOSITE_FIELD_MAP", "DIRECT_FIELD_MAP", "RULE_BASED_FIELD_MAP", "CONDITIONAL_COMPOSITE_FIELD_MAP", "NAMED_ENTITY_MAP", "RULE_BASED_ENTITY_MAP"
        :type model_type: str

        :param description:
            The value to assign to the description property of this ConditionalCompositeFieldMap.
        :type description: str

        :param field_map_scope:
            The value to assign to the field_map_scope property of this ConditionalCompositeFieldMap.
        :type field_map_scope: list[oci.data_integration.models.ProjectionRule]

        :param key:
            The value to assign to the key property of this ConditionalCompositeFieldMap.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ConditionalCompositeFieldMap.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ConditionalCompositeFieldMap.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this ConditionalCompositeFieldMap.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this ConditionalCompositeFieldMap.
        :type object_status: int

        :param field_maps:
            The value to assign to the field_maps property of this ConditionalCompositeFieldMap.
        :type field_maps: list[oci.data_integration.models.FieldMap]

        """
        self.swagger_types = {
            'model_type': 'str',
            'description': 'str',
            'field_map_scope': 'list[ProjectionRule]',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'field_maps': 'list[FieldMap]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'description': 'description',
            'field_map_scope': 'fieldMapScope',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'field_maps': 'fieldMaps'
        }

        self._model_type = None
        self._description = None
        self._field_map_scope = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._field_maps = None
        self._model_type = 'CONDITIONAL_COMPOSITE_FIELD_MAP'

    @property
    def field_map_scope(self):
        """
        Gets the field_map_scope of this ConditionalCompositeFieldMap.
        An array of projection rules.


        :return: The field_map_scope of this ConditionalCompositeFieldMap.
        :rtype: list[oci.data_integration.models.ProjectionRule]
        """
        return self._field_map_scope

    @field_map_scope.setter
    def field_map_scope(self, field_map_scope):
        """
        Sets the field_map_scope of this ConditionalCompositeFieldMap.
        An array of projection rules.


        :param field_map_scope: The field_map_scope of this ConditionalCompositeFieldMap.
        :type: list[oci.data_integration.models.ProjectionRule]
        """
        self._field_map_scope = field_map_scope

    @property
    def key(self):
        """
        Gets the key of this ConditionalCompositeFieldMap.
        The object key.


        :return: The key of this ConditionalCompositeFieldMap.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ConditionalCompositeFieldMap.
        The object key.


        :param key: The key of this ConditionalCompositeFieldMap.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this ConditionalCompositeFieldMap.
        The object's model version.


        :return: The model_version of this ConditionalCompositeFieldMap.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ConditionalCompositeFieldMap.
        The object's model version.


        :param model_version: The model_version of this ConditionalCompositeFieldMap.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ConditionalCompositeFieldMap.

        :return: The parent_ref of this ConditionalCompositeFieldMap.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ConditionalCompositeFieldMap.

        :param parent_ref: The parent_ref of this ConditionalCompositeFieldMap.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def config_values(self):
        """
        Gets the config_values of this ConditionalCompositeFieldMap.

        :return: The config_values of this ConditionalCompositeFieldMap.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this ConditionalCompositeFieldMap.

        :param config_values: The config_values of this ConditionalCompositeFieldMap.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def object_status(self):
        """
        Gets the object_status of this ConditionalCompositeFieldMap.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this ConditionalCompositeFieldMap.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ConditionalCompositeFieldMap.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this ConditionalCompositeFieldMap.
        :type: int
        """
        self._object_status = object_status

    @property
    def field_maps(self):
        """
        Gets the field_maps of this ConditionalCompositeFieldMap.
        An array of field maps.


        :return: The field_maps of this ConditionalCompositeFieldMap.
        :rtype: list[oci.data_integration.models.FieldMap]
        """
        return self._field_maps

    @field_maps.setter
    def field_maps(self, field_maps):
        """
        Sets the field_maps of this ConditionalCompositeFieldMap.
        An array of field maps.


        :param field_maps: The field_maps of this ConditionalCompositeFieldMap.
        :type: list[oci.data_integration.models.FieldMap]
        """
        self._field_maps = field_maps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
