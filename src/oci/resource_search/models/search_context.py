# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchContext(object):
    """
    Contains search context, such as highlighting, for found resources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchContext object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param highlights:
            The value to assign to the highlights property of this SearchContext.
        :type highlights: dict(str, list[str])

        """
        self.swagger_types = {
            'highlights': 'dict(str, list[str])'
        }

        self.attribute_map = {
            'highlights': 'highlights'
        }

        self._highlights = None

    @property
    def highlights(self):
        """
        Gets the highlights of this SearchContext.
        Describes what in each field matched the search criteria by showing highlighted values, but only for free text searches or for structured
        queries that use a MATCHING clause. The list of strings represents fragments of values that matched the query conditions. Highlighted
        values are wrapped with &lt;h1&gt;..&lt;/h1&gt; tags. All values are HTML-encoded (except &lt;h1&gt; tags).


        :return: The highlights of this SearchContext.
        :rtype: dict(str, list[str])
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """
        Sets the highlights of this SearchContext.
        Describes what in each field matched the search criteria by showing highlighted values, but only for free text searches or for structured
        queries that use a MATCHING clause. The list of strings represents fragments of values that matched the query conditions. Highlighted
        values are wrapped with &lt;h1&gt;..&lt;/h1&gt; tags. All values are HTML-encoded (except &lt;h1&gt; tags).


        :param highlights: The highlights of this SearchContext.
        :type: dict(str, list[str])
        """
        self._highlights = highlights

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
