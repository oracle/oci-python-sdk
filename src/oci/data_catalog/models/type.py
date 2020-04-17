# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Type(object):
    """
    Full data catalog type definition. Fully defines a type of the data catalog. All types are statically defined
    in the system and are immutable. It isn't possible to create new types or update existing types via the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Type object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Type.
        :type key: str

        :param name:
            The value to assign to the name property of this Type.
        :type name: str

        :param description:
            The value to assign to the description property of this Type.
        :type description: str

        :param catalog_id:
            The value to assign to the catalog_id property of this Type.
        :type catalog_id: str

        :param properties:
            The value to assign to the properties property of this Type.
        :type properties: dict(str, list[PropertyDefinition])

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Type.
        :type lifecycle_state: str

        :param is_internal:
            The value to assign to the is_internal property of this Type.
        :type is_internal: bool

        :param is_tag:
            The value to assign to the is_tag property of this Type.
        :type is_tag: bool

        :param is_approved:
            The value to assign to the is_approved property of this Type.
        :type is_approved: bool

        :param type_category:
            The value to assign to the type_category property of this Type.
        :type type_category: str

        :param external_type_name:
            The value to assign to the external_type_name property of this Type.
        :type external_type_name: str

        :param uri:
            The value to assign to the uri property of this Type.
        :type uri: str

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'description': 'str',
            'catalog_id': 'str',
            'properties': 'dict(str, list[PropertyDefinition])',
            'lifecycle_state': 'str',
            'is_internal': 'bool',
            'is_tag': 'bool',
            'is_approved': 'bool',
            'type_category': 'str',
            'external_type_name': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'description': 'description',
            'catalog_id': 'catalogId',
            'properties': 'properties',
            'lifecycle_state': 'lifecycleState',
            'is_internal': 'isInternal',
            'is_tag': 'isTag',
            'is_approved': 'isApproved',
            'type_category': 'typeCategory',
            'external_type_name': 'externalTypeName',
            'uri': 'uri'
        }

        self._key = None
        self._name = None
        self._description = None
        self._catalog_id = None
        self._properties = None
        self._lifecycle_state = None
        self._is_internal = None
        self._is_tag = None
        self._is_approved = None
        self._type_category = None
        self._external_type_name = None
        self._uri = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Type.
        Unique type key that is immutable.


        :return: The key of this Type.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Type.
        Unique type key that is immutable.


        :param key: The key of this Type.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this Type.
        The immutable name of the type.


        :return: The name of this Type.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Type.
        The immutable name of the type.


        :param name: The name of this Type.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Type.
        Detailed description of the type.


        :return: The description of this Type.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Type.
        Detailed description of the type.


        :param description: The description of this Type.
        :type: str
        """
        self._description = description

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this Type.
        The data catalog's OCID.


        :return: The catalog_id of this Type.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this Type.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this Type.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def properties(self):
        """
        Gets the properties of this Type.
        A map of arrays which defines the type specific properties, both required and optional. The map keys are
        category names and the values are arrays contiaing all property details. Every property is contained inside
        of a category. Most types have required properties within the \"default\" category.
        Example:
        `{
           \"properties\": {
             \"default\": {
               \"attributes:\": [
                 {
                   \"name\": \"host\",
                   \"type\": \"string\",
                   \"isRequired\": true,
                   \"isUpdatable\": false
                 },
                 ...
               ]
             }
           }
         }`


        :return: The properties of this Type.
        :rtype: dict(str, list[PropertyDefinition])
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Type.
        A map of arrays which defines the type specific properties, both required and optional. The map keys are
        category names and the values are arrays contiaing all property details. Every property is contained inside
        of a category. Most types have required properties within the \"default\" category.
        Example:
        `{
           \"properties\": {
             \"default\": {
               \"attributes:\": [
                 {
                   \"name\": \"host\",
                   \"type\": \"string\",
                   \"isRequired\": true,
                   \"isUpdatable\": false
                 },
                 ...
               ]
             }
           }
         }`


        :param properties: The properties of this Type.
        :type: dict(str, list[PropertyDefinition])
        """
        self._properties = properties

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Type.
        The current state of the type.


        :return: The lifecycle_state of this Type.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Type.
        The current state of the type.


        :param lifecycle_state: The lifecycle_state of this Type.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def is_internal(self):
        """
        Gets the is_internal of this Type.
        Indicates whether the type is internal, making it unavailable for use by metadata elements.


        :return: The is_internal of this Type.
        :rtype: bool
        """
        return self._is_internal

    @is_internal.setter
    def is_internal(self, is_internal):
        """
        Sets the is_internal of this Type.
        Indicates whether the type is internal, making it unavailable for use by metadata elements.


        :param is_internal: The is_internal of this Type.
        :type: bool
        """
        self._is_internal = is_internal

    @property
    def is_tag(self):
        """
        Gets the is_tag of this Type.
        Indicates whether the type can be used for tagging metadata elements.


        :return: The is_tag of this Type.
        :rtype: bool
        """
        return self._is_tag

    @is_tag.setter
    def is_tag(self, is_tag):
        """
        Sets the is_tag of this Type.
        Indicates whether the type can be used for tagging metadata elements.


        :param is_tag: The is_tag of this Type.
        :type: bool
        """
        self._is_tag = is_tag

    @property
    def is_approved(self):
        """
        Gets the is_approved of this Type.
        Indicates whether the type is approved for use as a classifying object.


        :return: The is_approved of this Type.
        :rtype: bool
        """
        return self._is_approved

    @is_approved.setter
    def is_approved(self, is_approved):
        """
        Sets the is_approved of this Type.
        Indicates whether the type is approved for use as a classifying object.


        :param is_approved: The is_approved of this Type.
        :type: bool
        """
        self._is_approved = is_approved

    @property
    def type_category(self):
        """
        Gets the type_category of this Type.
        Indicates the category this type belongs to. For instance, data assets, connections.


        :return: The type_category of this Type.
        :rtype: str
        """
        return self._type_category

    @type_category.setter
    def type_category(self, type_category):
        """
        Sets the type_category of this Type.
        Indicates the category this type belongs to. For instance, data assets, connections.


        :param type_category: The type_category of this Type.
        :type: str
        """
        self._type_category = type_category

    @property
    def external_type_name(self):
        """
        Gets the external_type_name of this Type.
        Mapping type equivalence in the external system.


        :return: The external_type_name of this Type.
        :rtype: str
        """
        return self._external_type_name

    @external_type_name.setter
    def external_type_name(self, external_type_name):
        """
        Sets the external_type_name of this Type.
        Mapping type equivalence in the external system.


        :param external_type_name: The external_type_name of this Type.
        :type: str
        """
        self._external_type_name = external_type_name

    @property
    def uri(self):
        """
        Gets the uri of this Type.
        URI to the type instance in the API.


        :return: The uri of this Type.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Type.
        URI to the type instance in the API.


        :param uri: The uri of this Type.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
