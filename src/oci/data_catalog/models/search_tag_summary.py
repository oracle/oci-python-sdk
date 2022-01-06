# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchTagSummary(object):
    """
    Represents the association of an object to a term. Returned as part of search result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchTagSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this SearchTagSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this SearchTagSummary.
        :type display_name: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName'
        }

        self._key = None
        self._display_name = None

    @property
    def key(self):
        """
        Gets the key of this SearchTagSummary.
        Unique tag key that is immutable.


        :return: The key of this SearchTagSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SearchTagSummary.
        Unique tag key that is immutable.


        :param key: The key of this SearchTagSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SearchTagSummary.
        Name of the tag that matches the term name.


        :return: The display_name of this SearchTagSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SearchTagSummary.
        Name of the tag that matches the term name.


        :param display_name: The display_name of this SearchTagSummary.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
