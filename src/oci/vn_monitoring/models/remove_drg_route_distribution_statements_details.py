# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveDrgRouteDistributionStatementsDetails(object):
    """
    Details request to remove statements from a route distribution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveDrgRouteDistributionStatementsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param statement_ids:
            The value to assign to the statement_ids property of this RemoveDrgRouteDistributionStatementsDetails.
        :type statement_ids: list[str]

        """
        self.swagger_types = {
            'statement_ids': 'list[str]'
        }

        self.attribute_map = {
            'statement_ids': 'statementIds'
        }

        self._statement_ids = None

    @property
    def statement_ids(self):
        """
        Gets the statement_ids of this RemoveDrgRouteDistributionStatementsDetails.
        The Oracle-assigned ID of each route distribution to remove.


        :return: The statement_ids of this RemoveDrgRouteDistributionStatementsDetails.
        :rtype: list[str]
        """
        return self._statement_ids

    @statement_ids.setter
    def statement_ids(self, statement_ids):
        """
        Sets the statement_ids of this RemoveDrgRouteDistributionStatementsDetails.
        The Oracle-assigned ID of each route distribution to remove.


        :param statement_ids: The statement_ids of this RemoveDrgRouteDistributionStatementsDetails.
        :type: list[str]
        """
        self._statement_ids = statement_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
