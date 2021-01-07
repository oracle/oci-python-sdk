# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .search_details import SearchDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FreeTextSearchDetails(SearchDetails):
    """
    A request containing arbitrary text that must be present in the resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FreeTextSearchDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_search.models.FreeTextSearchDetails.type` attribute
        of this class is ``FreeText`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FreeTextSearchDetails.
        :type type: str

        :param matching_context_type:
            The value to assign to the matching_context_type property of this FreeTextSearchDetails.
            Allowed values for this property are: "NONE", "HIGHLIGHTS"
        :type matching_context_type: str

        :param text:
            The value to assign to the text property of this FreeTextSearchDetails.
        :type text: str

        """
        self.swagger_types = {
            'type': 'str',
            'matching_context_type': 'str',
            'text': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'matching_context_type': 'matchingContextType',
            'text': 'text'
        }

        self._type = None
        self._matching_context_type = None
        self._text = None
        self._type = 'FreeText'

    @property
    def text(self):
        """
        **[Required]** Gets the text of this FreeTextSearchDetails.
        The text to search for.


        :return: The text of this FreeTextSearchDetails.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this FreeTextSearchDetails.
        The text to search for.


        :param text: The text of this FreeTextSearchDetails.
        :type: str
        """
        self._text = text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
