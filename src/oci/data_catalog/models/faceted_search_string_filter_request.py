# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190325


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FacetedSearchStringFilterRequest(object):
    """
    Object with string filter criteria
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FacetedSearchStringFilterRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field:
            The value to assign to the field property of this FacetedSearchStringFilterRequest.
        :type field: str

        :param values:
            The value to assign to the values property of this FacetedSearchStringFilterRequest.
        :type values: list[str]

        """
        self.swagger_types = {
            'field': 'str',
            'values': 'list[str]'
        }
        self.attribute_map = {
            'field': 'field',
            'values': 'values'
        }
        self._field = None
        self._values = None

    @property
    def field(self):
        """
        Gets the field of this FacetedSearchStringFilterRequest.
        String/boolean/numerical field name that needs to be filtered by.
        Acceptable field names: CatalogType, AttributeType, FolderType, DataAssetType, CreatedBy, UpdatedBy, Term, Tag, DataAssetName, LifeCycleState.


        :return: The field of this FacetedSearchStringFilterRequest.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this FacetedSearchStringFilterRequest.
        String/boolean/numerical field name that needs to be filtered by.
        Acceptable field names: CatalogType, AttributeType, FolderType, DataAssetType, CreatedBy, UpdatedBy, Term, Tag, DataAssetName, LifeCycleState.


        :param field: The field of this FacetedSearchStringFilterRequest.
        :type: str
        """
        self._field = field

    @property
    def values(self):
        """
        Gets the values of this FacetedSearchStringFilterRequest.
        Array of values that the search results needs to be filtered by.
        Acceptable values for field 'CatalogType': DataAsset, Folder, DataEntity, Attribute, Term, Category, Glossary, Pattern, Job, Schedule, CustomProperty.
        For other fields, acceptable values can be derived by inspecting the data object.


        :return: The values of this FacetedSearchStringFilterRequest.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this FacetedSearchStringFilterRequest.
        Array of values that the search results needs to be filtered by.
        Acceptable values for field 'CatalogType': DataAsset, Folder, DataEntity, Attribute, Term, Category, Glossary, Pattern, Job, Schedule, CustomProperty.
        For other fields, acceptable values can be derived by inspecting the data object.


        :param values: The values of this FacetedSearchStringFilterRequest.
        :type: list[str]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
