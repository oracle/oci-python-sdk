# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .push_down_operation import PushDownOperation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Sort(PushDownOperation):
    """
    The information about the sort object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Sort object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Sort.model_type` attribute
        of this class is ``SORT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Sort.
            Allowed values for this property are: "FILTER", "JOIN", "SELECT", "SORT", "QUERY"
        :type model_type: str

        :param sort_clauses:
            The value to assign to the sort_clauses property of this Sort.
        :type sort_clauses: list[oci.data_integration.models.SortClause]

        """
        self.swagger_types = {
            'model_type': 'str',
            'sort_clauses': 'list[SortClause]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'sort_clauses': 'sortClauses'
        }

        self._model_type = None
        self._sort_clauses = None
        self._model_type = 'SORT'

    @property
    def sort_clauses(self):
        """
        Gets the sort_clauses of this Sort.
        The sort clause.


        :return: The sort_clauses of this Sort.
        :rtype: list[oci.data_integration.models.SortClause]
        """
        return self._sort_clauses

    @sort_clauses.setter
    def sort_clauses(self, sort_clauses):
        """
        Sets the sort_clauses of this Sort.
        The sort clause.


        :param sort_clauses: The sort_clauses of this Sort.
        :type: list[oci.data_integration.models.SortClause]
        """
        self._sort_clauses = sort_clauses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
