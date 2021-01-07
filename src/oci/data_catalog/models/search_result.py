# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchResult(object):
    """
    The search result object is the definition of an element that is returned as part of search. It contains basic
    information about the object such as key, name and description. The search result also contains the list of tags
    for each object along with other contextual information like the data asset root, folder, or entity parents.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this SearchResult.
        :type key: str

        :param name:
            The value to assign to the name property of this SearchResult.
        :type name: str

        :param description:
            The value to assign to the description property of this SearchResult.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this SearchResult.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SearchResult.
        :type time_updated: datetime

        :param tag_summary:
            The value to assign to the tag_summary property of this SearchResult.
        :type tag_summary: list[oci.data_catalog.models.SearchTagSummary]

        :param term_summary:
            The value to assign to the term_summary property of this SearchResult.
        :type term_summary: list[oci.data_catalog.models.SearchTermSummary]

        :param type_name:
            The value to assign to the type_name property of this SearchResult.
        :type type_name: str

        :param external_type_name:
            The value to assign to the external_type_name property of this SearchResult.
        :type external_type_name: str

        :param external_data_type:
            The value to assign to the external_data_type property of this SearchResult.
        :type external_data_type: str

        :param data_asset_key:
            The value to assign to the data_asset_key property of this SearchResult.
        :type data_asset_key: str

        :param data_asset_type:
            The value to assign to the data_asset_type property of this SearchResult.
        :type data_asset_type: str

        :param data_asset_name:
            The value to assign to the data_asset_name property of this SearchResult.
        :type data_asset_name: str

        :param folder_key:
            The value to assign to the folder_key property of this SearchResult.
        :type folder_key: str

        :param folder_type:
            The value to assign to the folder_type property of this SearchResult.
        :type folder_type: str

        :param folder_name:
            The value to assign to the folder_name property of this SearchResult.
        :type folder_name: str

        :param entitykey:
            The value to assign to the entitykey property of this SearchResult.
        :type entitykey: str

        :param entity_type:
            The value to assign to the entity_type property of this SearchResult.
        :type entity_type: str

        :param entity_name:
            The value to assign to the entity_name property of this SearchResult.
        :type entity_name: str

        :param glossary_key:
            The value to assign to the glossary_key property of this SearchResult.
        :type glossary_key: str

        :param glossary_name:
            The value to assign to the glossary_name property of this SearchResult.
        :type glossary_name: str

        :param parent_term_key:
            The value to assign to the parent_term_key property of this SearchResult.
        :type parent_term_key: str

        :param parent_term_name:
            The value to assign to the parent_term_name property of this SearchResult.
        :type parent_term_name: str

        :param created_by_id:
            The value to assign to the created_by_id property of this SearchResult.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this SearchResult.
        :type updated_by_id: str

        :param path:
            The value to assign to the path property of this SearchResult.
        :type path: str

        :param expression:
            The value to assign to the expression property of this SearchResult.
        :type expression: str

        :param custom_properties:
            The value to assign to the custom_properties property of this SearchResult.
        :type custom_properties: list[oci.data_catalog.models.FacetedSearchCustomProperty]

        """
        self.swagger_types = {
            'key': 'str',
            'name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'tag_summary': 'list[SearchTagSummary]',
            'term_summary': 'list[SearchTermSummary]',
            'type_name': 'str',
            'external_type_name': 'str',
            'external_data_type': 'str',
            'data_asset_key': 'str',
            'data_asset_type': 'str',
            'data_asset_name': 'str',
            'folder_key': 'str',
            'folder_type': 'str',
            'folder_name': 'str',
            'entitykey': 'str',
            'entity_type': 'str',
            'entity_name': 'str',
            'glossary_key': 'str',
            'glossary_name': 'str',
            'parent_term_key': 'str',
            'parent_term_name': 'str',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'path': 'str',
            'expression': 'str',
            'custom_properties': 'list[FacetedSearchCustomProperty]'
        }

        self.attribute_map = {
            'key': 'key',
            'name': 'name',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'tag_summary': 'tagSummary',
            'term_summary': 'termSummary',
            'type_name': 'typeName',
            'external_type_name': 'externalTypeName',
            'external_data_type': 'externalDataType',
            'data_asset_key': 'dataAssetKey',
            'data_asset_type': 'dataAssetType',
            'data_asset_name': 'dataAssetName',
            'folder_key': 'folderKey',
            'folder_type': 'folderType',
            'folder_name': 'folderName',
            'entitykey': 'entitykey',
            'entity_type': 'entityType',
            'entity_name': 'entityName',
            'glossary_key': 'glossaryKey',
            'glossary_name': 'glossaryName',
            'parent_term_key': 'parentTermKey',
            'parent_term_name': 'parentTermName',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'path': 'path',
            'expression': 'expression',
            'custom_properties': 'customProperties'
        }

        self._key = None
        self._name = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._tag_summary = None
        self._term_summary = None
        self._type_name = None
        self._external_type_name = None
        self._external_data_type = None
        self._data_asset_key = None
        self._data_asset_type = None
        self._data_asset_name = None
        self._folder_key = None
        self._folder_type = None
        self._folder_name = None
        self._entitykey = None
        self._entity_type = None
        self._entity_name = None
        self._glossary_key = None
        self._glossary_name = None
        self._parent_term_key = None
        self._parent_term_name = None
        self._created_by_id = None
        self._updated_by_id = None
        self._path = None
        self._expression = None
        self._custom_properties = None

    @property
    def key(self):
        """
        Gets the key of this SearchResult.
        Unique key of the object returned as part of the search result.


        :return: The key of this SearchResult.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SearchResult.
        Unique key of the object returned as part of the search result.


        :param key: The key of this SearchResult.
        :type: str
        """
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this SearchResult.
        Name of the object.


        :return: The name of this SearchResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SearchResult.
        Name of the object.


        :param name: The name of this SearchResult.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SearchResult.
        Detailed description of the object.


        :return: The description of this SearchResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SearchResult.
        Detailed description of the object.


        :param description: The description of this SearchResult.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this SearchResult.
        The date and time the result object was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SearchResult.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SearchResult.
        The date and time the result object was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SearchResult.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SearchResult.
        The date and time the result object was updated, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this SearchResult.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SearchResult.
        The date and time the result object was updated, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this SearchResult.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def tag_summary(self):
        """
        Gets the tag_summary of this SearchResult.
        Array of the tags associated with this object.


        :return: The tag_summary of this SearchResult.
        :rtype: list[oci.data_catalog.models.SearchTagSummary]
        """
        return self._tag_summary

    @tag_summary.setter
    def tag_summary(self, tag_summary):
        """
        Sets the tag_summary of this SearchResult.
        Array of the tags associated with this object.


        :param tag_summary: The tag_summary of this SearchResult.
        :type: list[oci.data_catalog.models.SearchTagSummary]
        """
        self._tag_summary = tag_summary

    @property
    def term_summary(self):
        """
        Gets the term_summary of this SearchResult.
        Array of the terms associated with this object.


        :return: The term_summary of this SearchResult.
        :rtype: list[oci.data_catalog.models.SearchTermSummary]
        """
        return self._term_summary

    @term_summary.setter
    def term_summary(self, term_summary):
        """
        Sets the term_summary of this SearchResult.
        Array of the terms associated with this object.


        :param term_summary: The term_summary of this SearchResult.
        :type: list[oci.data_catalog.models.SearchTermSummary]
        """
        self._term_summary = term_summary

    @property
    def type_name(self):
        """
        Gets the type_name of this SearchResult.
        Name of the object type.


        :return: The type_name of this SearchResult.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this SearchResult.
        Name of the object type.


        :param type_name: The type_name of this SearchResult.
        :type: str
        """
        self._type_name = type_name

    @property
    def external_type_name(self):
        """
        Gets the external_type_name of this SearchResult.
        Name of the external object type in the host data asset. For example, column, field, table, view, or file.


        :return: The external_type_name of this SearchResult.
        :rtype: str
        """
        return self._external_type_name

    @external_type_name.setter
    def external_type_name(self, external_type_name):
        """
        Sets the external_type_name of this SearchResult.
        Name of the external object type in the host data asset. For example, column, field, table, view, or file.


        :param external_type_name: The external_type_name of this SearchResult.
        :type: str
        """
        self._external_type_name = external_type_name

    @property
    def external_data_type(self):
        """
        Gets the external_data_type of this SearchResult.
        Data type of the object if the object is an attribute. Null otherwise.


        :return: The external_data_type of this SearchResult.
        :rtype: str
        """
        return self._external_data_type

    @external_data_type.setter
    def external_data_type(self, external_data_type):
        """
        Sets the external_data_type of this SearchResult.
        Data type of the object if the object is an attribute. Null otherwise.


        :param external_data_type: The external_data_type of this SearchResult.
        :type: str
        """
        self._external_data_type = external_data_type

    @property
    def data_asset_key(self):
        """
        Gets the data_asset_key of this SearchResult.
        Unique key of the data asset that is the root parent of this object.


        :return: The data_asset_key of this SearchResult.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this SearchResult.
        Unique key of the data asset that is the root parent of this object.


        :param data_asset_key: The data_asset_key of this SearchResult.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def data_asset_type(self):
        """
        Gets the data_asset_type of this SearchResult.
        Type name of the data asset. For example, Oracle, MySQL or Oracle Object Storage.


        :return: The data_asset_type of this SearchResult.
        :rtype: str
        """
        return self._data_asset_type

    @data_asset_type.setter
    def data_asset_type(self, data_asset_type):
        """
        Sets the data_asset_type of this SearchResult.
        Type name of the data asset. For example, Oracle, MySQL or Oracle Object Storage.


        :param data_asset_type: The data_asset_type of this SearchResult.
        :type: str
        """
        self._data_asset_type = data_asset_type

    @property
    def data_asset_name(self):
        """
        Gets the data_asset_name of this SearchResult.
        Name of the data asset that is the root parent of this object.


        :return: The data_asset_name of this SearchResult.
        :rtype: str
        """
        return self._data_asset_name

    @data_asset_name.setter
    def data_asset_name(self, data_asset_name):
        """
        Sets the data_asset_name of this SearchResult.
        Name of the data asset that is the root parent of this object.


        :param data_asset_name: The data_asset_name of this SearchResult.
        :type: str
        """
        self._data_asset_name = data_asset_name

    @property
    def folder_key(self):
        """
        Gets the folder_key of this SearchResult.
        Unique key of the folder object if this object is a sub folder, entity, or attribute.


        :return: The folder_key of this SearchResult.
        :rtype: str
        """
        return self._folder_key

    @folder_key.setter
    def folder_key(self, folder_key):
        """
        Sets the folder_key of this SearchResult.
        Unique key of the folder object if this object is a sub folder, entity, or attribute.


        :param folder_key: The folder_key of this SearchResult.
        :type: str
        """
        self._folder_key = folder_key

    @property
    def folder_type(self):
        """
        Gets the folder_type of this SearchResult.
        Type name of the folder. For example, schema, directory, or topic.


        :return: The folder_type of this SearchResult.
        :rtype: str
        """
        return self._folder_type

    @folder_type.setter
    def folder_type(self, folder_type):
        """
        Sets the folder_type of this SearchResult.
        Type name of the folder. For example, schema, directory, or topic.


        :param folder_type: The folder_type of this SearchResult.
        :type: str
        """
        self._folder_type = folder_type

    @property
    def folder_name(self):
        """
        Gets the folder_name of this SearchResult.
        Name of the parent folder object if this object is a sub folder, entity, or attribute.


        :return: The folder_name of this SearchResult.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """
        Sets the folder_name of this SearchResult.
        Name of the parent folder object if this object is a sub folder, entity, or attribute.


        :param folder_name: The folder_name of this SearchResult.
        :type: str
        """
        self._folder_name = folder_name

    @property
    def entitykey(self):
        """
        Gets the entitykey of this SearchResult.
        Unique key of the entity object if this object is an attribute.


        :return: The entitykey of this SearchResult.
        :rtype: str
        """
        return self._entitykey

    @entitykey.setter
    def entitykey(self, entitykey):
        """
        Sets the entitykey of this SearchResult.
        Unique key of the entity object if this object is an attribute.


        :param entitykey: The entitykey of this SearchResult.
        :type: str
        """
        self._entitykey = entitykey

    @property
    def entity_type(self):
        """
        Gets the entity_type of this SearchResult.
        Type name of the entity. For example, table, view, external table, file, or object.


        :return: The entity_type of this SearchResult.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this SearchResult.
        Type name of the entity. For example, table, view, external table, file, or object.


        :param entity_type: The entity_type of this SearchResult.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def entity_name(self):
        """
        Gets the entity_name of this SearchResult.
        Name of the parent entity object if this object is an attribute.


        :return: The entity_name of this SearchResult.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this SearchResult.
        Name of the parent entity object if this object is an attribute.


        :param entity_name: The entity_name of this SearchResult.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def glossary_key(self):
        """
        Gets the glossary_key of this SearchResult.
        Unique id of the parent glossary.


        :return: The glossary_key of this SearchResult.
        :rtype: str
        """
        return self._glossary_key

    @glossary_key.setter
    def glossary_key(self, glossary_key):
        """
        Sets the glossary_key of this SearchResult.
        Unique id of the parent glossary.


        :param glossary_key: The glossary_key of this SearchResult.
        :type: str
        """
        self._glossary_key = glossary_key

    @property
    def glossary_name(self):
        """
        Gets the glossary_name of this SearchResult.
        Name of the parent glossary if this object is a term.


        :return: The glossary_name of this SearchResult.
        :rtype: str
        """
        return self._glossary_name

    @glossary_name.setter
    def glossary_name(self, glossary_name):
        """
        Sets the glossary_name of this SearchResult.
        Name of the parent glossary if this object is a term.


        :param glossary_name: The glossary_name of this SearchResult.
        :type: str
        """
        self._glossary_name = glossary_name

    @property
    def parent_term_key(self):
        """
        Gets the parent_term_key of this SearchResult.
        This terms parent term key. Will be null if the term has no parent term.


        :return: The parent_term_key of this SearchResult.
        :rtype: str
        """
        return self._parent_term_key

    @parent_term_key.setter
    def parent_term_key(self, parent_term_key):
        """
        Sets the parent_term_key of this SearchResult.
        This terms parent term key. Will be null if the term has no parent term.


        :param parent_term_key: The parent_term_key of this SearchResult.
        :type: str
        """
        self._parent_term_key = parent_term_key

    @property
    def parent_term_name(self):
        """
        Gets the parent_term_name of this SearchResult.
        Name of the parent term. Will be null if the term has no parent term.


        :return: The parent_term_name of this SearchResult.
        :rtype: str
        """
        return self._parent_term_name

    @parent_term_name.setter
    def parent_term_name(self, parent_term_name):
        """
        Sets the parent_term_name of this SearchResult.
        Name of the parent term. Will be null if the term has no parent term.


        :param parent_term_name: The parent_term_name of this SearchResult.
        :type: str
        """
        self._parent_term_name = parent_term_name

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this SearchResult.
        OCID of the user who created the resource.


        :return: The created_by_id of this SearchResult.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this SearchResult.
        OCID of the user who created the resource.


        :param created_by_id: The created_by_id of this SearchResult.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this SearchResult.
        OCID of the user who updated the resource.


        :return: The updated_by_id of this SearchResult.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this SearchResult.
        OCID of the user who updated the resource.


        :param updated_by_id: The updated_by_id of this SearchResult.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def path(self):
        """
        Gets the path of this SearchResult.
        Absolute path of this resource, which could be a term, folder, entity etc, usually resolvable to this resource through a namespace hierarchy.


        :return: The path of this SearchResult.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this SearchResult.
        Absolute path of this resource, which could be a term, folder, entity etc, usually resolvable to this resource through a namespace hierarchy.


        :param path: The path of this SearchResult.
        :type: str
        """
        self._path = path

    @property
    def expression(self):
        """
        Gets the expression of this SearchResult.
        Expression for logical entities against which names of dataObjects will be matched.


        :return: The expression of this SearchResult.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this SearchResult.
        Expression for logical entities against which names of dataObjects will be matched.


        :param expression: The expression of this SearchResult.
        :type: str
        """
        self._expression = expression

    @property
    def custom_properties(self):
        """
        Gets the custom_properties of this SearchResult.
        Custom properties defined by users.


        :return: The custom_properties of this SearchResult.
        :rtype: list[oci.data_catalog.models.FacetedSearchCustomProperty]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """
        Sets the custom_properties of this SearchResult.
        Custom properties defined by users.


        :param custom_properties: The custom_properties of this SearchResult.
        :type: list[oci.data_catalog.models.FacetedSearchCustomProperty]
        """
        self._custom_properties = custom_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
