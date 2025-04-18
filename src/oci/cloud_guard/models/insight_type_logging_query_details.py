# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131

from .logging_query_details import LoggingQueryDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InsightTypeLoggingQueryDetails(LoggingQueryDetails):
    """
    Additional details for Insight type queries on a data source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InsightTypeLoggingQueryDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.InsightTypeLoggingQueryDetails.logging_query_type` attribute
        of this class is ``INSIGHT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param logging_query_type:
            The value to assign to the logging_query_type property of this InsightTypeLoggingQueryDetails.
            Allowed values for this property are: "INSIGHT"
        :type logging_query_type: str

        :param key_entities_count:
            The value to assign to the key_entities_count property of this InsightTypeLoggingQueryDetails.
        :type key_entities_count: int

        """
        self.swagger_types = {
            'logging_query_type': 'str',
            'key_entities_count': 'int'
        }
        self.attribute_map = {
            'logging_query_type': 'loggingQueryType',
            'key_entities_count': 'keyEntitiesCount'
        }
        self._logging_query_type = None
        self._key_entities_count = None
        self._logging_query_type = 'INSIGHT'

    @property
    def key_entities_count(self):
        """
        Gets the key_entities_count of this InsightTypeLoggingQueryDetails.
        The key entities count used for data source query


        :return: The key_entities_count of this InsightTypeLoggingQueryDetails.
        :rtype: int
        """
        return self._key_entities_count

    @key_entities_count.setter
    def key_entities_count(self, key_entities_count):
        """
        Sets the key_entities_count of this InsightTypeLoggingQueryDetails.
        The key entities count used for data source query


        :param key_entities_count: The key_entities_count of this InsightTypeLoggingQueryDetails.
        :type: int
        """
        self._key_entities_count = key_entities_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
