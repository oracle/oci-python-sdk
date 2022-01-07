# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SuggestListItem(object):
    """
    Details of a potential match returned from the suggest operation for the given input text.
    by the limit parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SuggestListItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param suggestion:
            The value to assign to the suggestion property of this SuggestListItem.
        :type suggestion: str

        :param object_count:
            The value to assign to the object_count property of this SuggestListItem.
        :type object_count: int

        """
        self.swagger_types = {
            'suggestion': 'str',
            'object_count': 'int'
        }

        self.attribute_map = {
            'suggestion': 'suggestion',
            'object_count': 'objectCount'
        }

        self._suggestion = None
        self._object_count = None

    @property
    def suggestion(self):
        """
        Gets the suggestion of this SuggestListItem.
        Potential string match. Matching is based on the frequency of usage within the catalog.


        :return: The suggestion of this SuggestListItem.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """
        Sets the suggestion of this SuggestListItem.
        Potential string match. Matching is based on the frequency of usage within the catalog.


        :param suggestion: The suggestion of this SuggestListItem.
        :type: str
        """
        self._suggestion = suggestion

    @property
    def object_count(self):
        """
        Gets the object_count of this SuggestListItem.
        The number of objects which contain this suggestion.


        :return: The object_count of this SuggestListItem.
        :rtype: int
        """
        return self._object_count

    @object_count.setter
    def object_count(self, object_count):
        """
        Sets the object_count of this SuggestListItem.
        The number of objects which contain this suggestion.


        :param object_count: The object_count of this SuggestListItem.
        :type: int
        """
        self._object_count = object_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
