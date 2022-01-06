# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FacetedSearchFilterRequest(object):
    """
    Object with details about filter criteria.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FacetedSearchFilterRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param search_date_filters:
            The value to assign to the search_date_filters property of this FacetedSearchFilterRequest.
        :type search_date_filters: list[oci.data_catalog.models.FacetedSearchDateFilterRequest]

        :param search_string_filters:
            The value to assign to the search_string_filters property of this FacetedSearchFilterRequest.
        :type search_string_filters: list[oci.data_catalog.models.FacetedSearchStringFilterRequest]

        """
        self.swagger_types = {
            'search_date_filters': 'list[FacetedSearchDateFilterRequest]',
            'search_string_filters': 'list[FacetedSearchStringFilterRequest]'
        }

        self.attribute_map = {
            'search_date_filters': 'searchDateFilters',
            'search_string_filters': 'searchStringFilters'
        }

        self._search_date_filters = None
        self._search_string_filters = None

    @property
    def search_date_filters(self):
        """
        Gets the search_date_filters of this FacetedSearchFilterRequest.
        Object with date filter criteria


        :return: The search_date_filters of this FacetedSearchFilterRequest.
        :rtype: list[oci.data_catalog.models.FacetedSearchDateFilterRequest]
        """
        return self._search_date_filters

    @search_date_filters.setter
    def search_date_filters(self, search_date_filters):
        """
        Sets the search_date_filters of this FacetedSearchFilterRequest.
        Object with date filter criteria


        :param search_date_filters: The search_date_filters of this FacetedSearchFilterRequest.
        :type: list[oci.data_catalog.models.FacetedSearchDateFilterRequest]
        """
        self._search_date_filters = search_date_filters

    @property
    def search_string_filters(self):
        """
        Gets the search_string_filters of this FacetedSearchFilterRequest.
        Object with string filter criteria


        :return: The search_string_filters of this FacetedSearchFilterRequest.
        :rtype: list[oci.data_catalog.models.FacetedSearchStringFilterRequest]
        """
        return self._search_string_filters

    @search_string_filters.setter
    def search_string_filters(self, search_string_filters):
        """
        Sets the search_string_filters of this FacetedSearchFilterRequest.
        Object with string filter criteria


        :param search_string_filters: The search_string_filters of this FacetedSearchFilterRequest.
        :type: list[oci.data_catalog.models.FacetedSearchStringFilterRequest]
        """
        self._search_string_filters = search_string_filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
