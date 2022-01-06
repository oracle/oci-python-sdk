# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SuggestResults(object):
    """
    The list of potential matches returned from the suggest operation for the given input text. The size of the list will be determined
    by the limit parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SuggestResults object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_count:
            The value to assign to the total_count property of this SuggestResults.
        :type total_count: int

        :param search_latency_in_ms:
            The value to assign to the search_latency_in_ms property of this SuggestResults.
        :type search_latency_in_ms: int

        :param input_text:
            The value to assign to the input_text property of this SuggestResults.
        :type input_text: str

        :param items:
            The value to assign to the items property of this SuggestResults.
        :type items: list[oci.data_catalog.models.SuggestListItem]

        """
        self.swagger_types = {
            'total_count': 'int',
            'search_latency_in_ms': 'int',
            'input_text': 'str',
            'items': 'list[SuggestListItem]'
        }

        self.attribute_map = {
            'total_count': 'totalCount',
            'search_latency_in_ms': 'searchLatencyInMs',
            'input_text': 'inputText',
            'items': 'items'
        }

        self._total_count = None
        self._search_latency_in_ms = None
        self._input_text = None
        self._items = None

    @property
    def total_count(self):
        """
        **[Required]** Gets the total_count of this SuggestResults.
        Total number of items returned.


        :return: The total_count of this SuggestResults.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this SuggestResults.
        Total number of items returned.


        :param total_count: The total_count of this SuggestResults.
        :type: int
        """
        self._total_count = total_count

    @property
    def search_latency_in_ms(self):
        """
        Gets the search_latency_in_ms of this SuggestResults.
        Time taken to compute the result, in milliseconds.


        :return: The search_latency_in_ms of this SuggestResults.
        :rtype: int
        """
        return self._search_latency_in_ms

    @search_latency_in_ms.setter
    def search_latency_in_ms(self, search_latency_in_ms):
        """
        Sets the search_latency_in_ms of this SuggestResults.
        Time taken to compute the result, in milliseconds.


        :param search_latency_in_ms: The search_latency_in_ms of this SuggestResults.
        :type: int
        """
        self._search_latency_in_ms = search_latency_in_ms

    @property
    def input_text(self):
        """
        **[Required]** Gets the input_text of this SuggestResults.
        Input string for which the potential matches are computed.


        :return: The input_text of this SuggestResults.
        :rtype: str
        """
        return self._input_text

    @input_text.setter
    def input_text(self, input_text):
        """
        Sets the input_text of this SuggestResults.
        Input string for which the potential matches are computed.


        :param input_text: The input_text of this SuggestResults.
        :type: str
        """
        self._input_text = input_text

    @property
    def items(self):
        """
        Gets the items of this SuggestResults.
        List of suggestions.


        :return: The items of this SuggestResults.
        :rtype: list[oci.data_catalog.models.SuggestListItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SuggestResults.
        List of suggestions.


        :param items: The items of this SuggestResults.
        :type: list[oci.data_catalog.models.SuggestListItem]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
