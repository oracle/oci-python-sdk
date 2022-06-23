# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgRouteDistributionStatementsDetails(object):
    """
    Details request to update statements in a route distribution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgRouteDistributionStatementsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param statements:
            The value to assign to the statements property of this UpdateDrgRouteDistributionStatementsDetails.
        :type statements: list[oci.vn_monitoring.models.UpdateDrgRouteDistributionStatementDetails]

        """
        self.swagger_types = {
            'statements': 'list[UpdateDrgRouteDistributionStatementDetails]'
        }

        self.attribute_map = {
            'statements': 'statements'
        }

        self._statements = None

    @property
    def statements(self):
        """
        **[Required]** Gets the statements of this UpdateDrgRouteDistributionStatementsDetails.
        The route distribution statements to update, and the details to be updated.


        :return: The statements of this UpdateDrgRouteDistributionStatementsDetails.
        :rtype: list[oci.vn_monitoring.models.UpdateDrgRouteDistributionStatementDetails]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        """
        Sets the statements of this UpdateDrgRouteDistributionStatementsDetails.
        The route distribution statements to update, and the details to be updated.


        :param statements: The statements of this UpdateDrgRouteDistributionStatementsDetails.
        :type: list[oci.vn_monitoring.models.UpdateDrgRouteDistributionStatementDetails]
        """
        self._statements = statements

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
