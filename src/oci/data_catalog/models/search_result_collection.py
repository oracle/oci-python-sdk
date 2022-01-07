# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchResultCollection(object):
    """
    The list of search result items matching the criteria returned from the search operation. Search errors and
    messages, if any , will be part of the standard error response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchResultCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param count:
            The value to assign to the count property of this SearchResultCollection.
        :type count: int

        :param items:
            The value to assign to the items property of this SearchResultCollection.
        :type items: list[oci.data_catalog.models.SearchResult]

        :param query:
            The value to assign to the query property of this SearchResultCollection.
        :type query: str

        :param faceted_search_aggregation:
            The value to assign to the faceted_search_aggregation property of this SearchResultCollection.
        :type faceted_search_aggregation: list[oci.data_catalog.models.FacetedSearchAggregation]

        :param sortable_fields:
            The value to assign to the sortable_fields property of this SearchResultCollection.
        :type sortable_fields: list[str]

        """
        self.swagger_types = {
            'count': 'int',
            'items': 'list[SearchResult]',
            'query': 'str',
            'faceted_search_aggregation': 'list[FacetedSearchAggregation]',
            'sortable_fields': 'list[str]'
        }

        self.attribute_map = {
            'count': 'count',
            'items': 'items',
            'query': 'query',
            'faceted_search_aggregation': 'facetedSearchAggregation',
            'sortable_fields': 'sortableFields'
        }

        self._count = None
        self._items = None
        self._query = None
        self._faceted_search_aggregation = None
        self._sortable_fields = None

    @property
    def count(self):
        """
        Gets the count of this SearchResultCollection.
        Total number of items returned.


        :return: The count of this SearchResultCollection.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SearchResultCollection.
        Total number of items returned.


        :param count: The count of this SearchResultCollection.
        :type: int
        """
        self._count = count

    @property
    def items(self):
        """
        Gets the items of this SearchResultCollection.
        Search result set.


        :return: The items of this SearchResultCollection.
        :rtype: list[oci.data_catalog.models.SearchResult]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SearchResultCollection.
        Search result set.


        :param items: The items of this SearchResultCollection.
        :type: list[oci.data_catalog.models.SearchResult]
        """
        self._items = items

    @property
    def query(self):
        """
        Gets the query of this SearchResultCollection.
        String that data objects are to be searched with.


        :return: The query of this SearchResultCollection.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchResultCollection.
        String that data objects are to be searched with.


        :param query: The query of this SearchResultCollection.
        :type: str
        """
        self._query = query

    @property
    def faceted_search_aggregation(self):
        """
        Gets the faceted_search_aggregation of this SearchResultCollection.
        Aggregations/facets on properties of data objects.


        :return: The faceted_search_aggregation of this SearchResultCollection.
        :rtype: list[oci.data_catalog.models.FacetedSearchAggregation]
        """
        return self._faceted_search_aggregation

    @faceted_search_aggregation.setter
    def faceted_search_aggregation(self, faceted_search_aggregation):
        """
        Sets the faceted_search_aggregation of this SearchResultCollection.
        Aggregations/facets on properties of data objects.


        :param faceted_search_aggregation: The faceted_search_aggregation of this SearchResultCollection.
        :type: list[oci.data_catalog.models.FacetedSearchAggregation]
        """
        self._faceted_search_aggregation = faceted_search_aggregation

    @property
    def sortable_fields(self):
        """
        Gets the sortable_fields of this SearchResultCollection.
        A list of fields or properties used in the sorting of a search result.


        :return: The sortable_fields of this SearchResultCollection.
        :rtype: list[str]
        """
        return self._sortable_fields

    @sortable_fields.setter
    def sortable_fields(self, sortable_fields):
        """
        Sets the sortable_fields of this SearchResultCollection.
        A list of fields or properties used in the sorting of a search result.


        :param sortable_fields: The sortable_fields of this SearchResultCollection.
        :type: list[str]
        """
        self._sortable_fields = sortable_fields

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
