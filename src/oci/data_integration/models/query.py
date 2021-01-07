# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .push_down_operation import PushDownOperation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Query(PushDownOperation):
    """
    A query object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Query object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Query.model_type` attribute
        of this class is ``QUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Query.
            Allowed values for this property are: "FILTER", "JOIN", "SELECT", "SORT", "QUERY"
        :type model_type: str

        :param query:
            The value to assign to the query property of this Query.
        :type query: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'query': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'query': 'query'
        }

        self._model_type = None
        self._query = None
        self._model_type = 'QUERY'

    @property
    def query(self):
        """
        Gets the query of this Query.
        A query string.


        :return: The query of this Query.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this Query.
        A query string.


        :param query: The query of this Query.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
