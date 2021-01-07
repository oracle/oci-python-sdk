# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchCriteria(object):
    """
    Search Query object that allows complex search predicates that cannot be expressed through simple query params.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchCriteria object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param query:
            The value to assign to the query property of this SearchCriteria.
        :type query: str

        :param faceted_query:
            The value to assign to the faceted_query property of this SearchCriteria.
        :type faceted_query: str

        :param dimensions:
            The value to assign to the dimensions property of this SearchCriteria.
        :type dimensions: list[str]

        :param sort:
            The value to assign to the sort property of this SearchCriteria.
        :type sort: list[oci.data_catalog.models.FacetedSearchSortRequest]

        :param filters:
            The value to assign to the filters property of this SearchCriteria.
        :type filters: oci.data_catalog.models.FacetedSearchFilterRequest

        """
        self.swagger_types = {
            'query': 'str',
            'faceted_query': 'str',
            'dimensions': 'list[str]',
            'sort': 'list[FacetedSearchSortRequest]',
            'filters': 'FacetedSearchFilterRequest'
        }

        self.attribute_map = {
            'query': 'query',
            'faceted_query': 'facetedQuery',
            'dimensions': 'dimensions',
            'sort': 'sort',
            'filters': 'filters'
        }

        self._query = None
        self._faceted_query = None
        self._dimensions = None
        self._sort = None
        self._filters = None

    @property
    def query(self):
        """
        Gets the query of this SearchCriteria.
        Search query dsl that defines the query components including fields and predicates.


        :return: The query of this SearchCriteria.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this SearchCriteria.
        Search query dsl that defines the query components including fields and predicates.


        :param query: The query of this SearchCriteria.
        :type: str
        """
        self._query = query

    @property
    def faceted_query(self):
        """
        Gets the faceted_query of this SearchCriteria.
        Query string that a dataObject is to be searched with. Used in the faceted query request


        :return: The faceted_query of this SearchCriteria.
        :rtype: str
        """
        return self._faceted_query

    @faceted_query.setter
    def faceted_query(self, faceted_query):
        """
        Sets the faceted_query of this SearchCriteria.
        Query string that a dataObject is to be searched with. Used in the faceted query request


        :param faceted_query: The faceted_query of this SearchCriteria.
        :type: str
        """
        self._faceted_query = faceted_query

    @property
    def dimensions(self):
        """
        Gets the dimensions of this SearchCriteria.
        List of properties of dataObjects that needs to aggregated on for facets.


        :return: The dimensions of this SearchCriteria.
        :rtype: list[str]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this SearchCriteria.
        List of properties of dataObjects that needs to aggregated on for facets.


        :param dimensions: The dimensions of this SearchCriteria.
        :type: list[str]
        """
        self._dimensions = dimensions

    @property
    def sort(self):
        """
        Gets the sort of this SearchCriteria.
        Array of objects having details about sort field and order.


        :return: The sort of this SearchCriteria.
        :rtype: list[oci.data_catalog.models.FacetedSearchSortRequest]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this SearchCriteria.
        Array of objects having details about sort field and order.


        :param sort: The sort of this SearchCriteria.
        :type: list[oci.data_catalog.models.FacetedSearchSortRequest]
        """
        self._sort = sort

    @property
    def filters(self):
        """
        Gets the filters of this SearchCriteria.

        :return: The filters of this SearchCriteria.
        :rtype: oci.data_catalog.models.FacetedSearchFilterRequest
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this SearchCriteria.

        :param filters: The filters of this SearchCriteria.
        :type: oci.data_catalog.models.FacetedSearchFilterRequest
        """
        self._filters = filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
