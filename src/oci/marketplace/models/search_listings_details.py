# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchListingsDetails(object):
    """
    A base request type that contains common criteria for Marketplace Search Listings details.
    """

    #: A constant which can be used with the type property of a SearchListingsDetails.
    #: This constant has a value of "FreeText"
    TYPE_FREE_TEXT = "FreeText"

    #: A constant which can be used with the type property of a SearchListingsDetails.
    #: This constant has a value of "Structured"
    TYPE_STRUCTURED = "Structured"

    #: A constant which can be used with the matching_context_type property of a SearchListingsDetails.
    #: This constant has a value of "NONE"
    MATCHING_CONTEXT_TYPE_NONE = "NONE"

    #: A constant which can be used with the matching_context_type property of a SearchListingsDetails.
    #: This constant has a value of "HIGHLIGHTS"
    MATCHING_CONTEXT_TYPE_HIGHLIGHTS = "HIGHLIGHTS"

    def __init__(self, **kwargs):
        """
        Initializes a new SearchListingsDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.marketplace.models.StructuredSearchDetails`
        * :class:`~oci.marketplace.models.FreeTextSearchDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SearchListingsDetails.
            Allowed values for this property are: "FreeText", "Structured"
        :type type: str

        :param matching_context_type:
            The value to assign to the matching_context_type property of this SearchListingsDetails.
            Allowed values for this property are: "NONE", "HIGHLIGHTS"
        :type matching_context_type: str

        """
        self.swagger_types = {
            'type': 'str',
            'matching_context_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'matching_context_type': 'matchingContextType'
        }

        self._type = None
        self._matching_context_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'Structured':
            return 'StructuredSearchDetails'

        if type == 'FreeText':
            return 'FreeTextSearchDetails'
        else:
            return 'SearchListingsDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SearchListingsDetails.
        The type of SearchDetails, whether FreeText or Structured.

        Allowed values for this property are: "FreeText", "Structured"


        :return: The type of this SearchListingsDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SearchListingsDetails.
        The type of SearchDetails, whether FreeText or Structured.


        :param type: The type of this SearchListingsDetails.
        :type: str
        """
        allowed_values = ["FreeText", "Structured"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def matching_context_type(self):
        """
        Gets the matching_context_type of this SearchListingsDetails.
        The type of matching context returned in the response. If you specify HIGHLIGHTS, then the service will highlight fragments in its response. The default value is NONE.

        Allowed values for this property are: "NONE", "HIGHLIGHTS"


        :return: The matching_context_type of this SearchListingsDetails.
        :rtype: str
        """
        return self._matching_context_type

    @matching_context_type.setter
    def matching_context_type(self, matching_context_type):
        """
        Sets the matching_context_type of this SearchListingsDetails.
        The type of matching context returned in the response. If you specify HIGHLIGHTS, then the service will highlight fragments in its response. The default value is NONE.


        :param matching_context_type: The matching_context_type of this SearchListingsDetails.
        :type: str
        """
        allowed_values = ["NONE", "HIGHLIGHTS"]
        if not value_allowed_none_or_none_sentinel(matching_context_type, allowed_values):
            raise ValueError(
                "Invalid value for `matching_context_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._matching_context_type = matching_context_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
