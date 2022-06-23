# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GetPathAnalysisDetails(object):
    """
    Defines the configuration for getting a path analysis.
    """

    #: A constant which can be used with the type property of a GetPathAnalysisDetails.
    #: This constant has a value of "PERSISTED_QUERY"
    TYPE_PERSISTED_QUERY = "PERSISTED_QUERY"

    #: A constant which can be used with the type property of a GetPathAnalysisDetails.
    #: This constant has a value of "ADHOC_QUERY"
    TYPE_ADHOC_QUERY = "ADHOC_QUERY"

    def __init__(self, **kwargs):
        """
        Initializes a new GetPathAnalysisDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.vn_monitoring.models.AdhocGetPathAnalysisDetails`
        * :class:`~oci.vn_monitoring.models.PersistedGetPathAnalysisDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this GetPathAnalysisDetails.
            Allowed values for this property are: "PERSISTED_QUERY", "ADHOC_QUERY"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'ADHOC_QUERY':
            return 'AdhocGetPathAnalysisDetails'

        if type == 'PERSISTED_QUERY':
            return 'PersistedGetPathAnalysisDetails'
        else:
            return 'GetPathAnalysisDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this GetPathAnalysisDetails.
        The type of the `PathAnalysis` query.

        Allowed values for this property are: "PERSISTED_QUERY", "ADHOC_QUERY"


        :return: The type of this GetPathAnalysisDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GetPathAnalysisDetails.
        The type of the `PathAnalysis` query.


        :param type: The type of this GetPathAnalysisDetails.
        :type: str
        """
        allowed_values = ["PERSISTED_QUERY", "ADHOC_QUERY"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
