# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgRouteDistributionStatementDetails(object):
    """
    Route distribution statements to update in the route distribution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgRouteDistributionStatementDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UpdateDrgRouteDistributionStatementDetails.
        :type id: str

        :param match_criteria:
            The value to assign to the match_criteria property of this UpdateDrgRouteDistributionStatementDetails.
        :type match_criteria: list[oci.vn_monitoring.models.DrgRouteDistributionMatchCriteria]

        :param priority:
            The value to assign to the priority property of this UpdateDrgRouteDistributionStatementDetails.
        :type priority: int

        """
        self.swagger_types = {
            'id': 'str',
            'match_criteria': 'list[DrgRouteDistributionMatchCriteria]',
            'priority': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'match_criteria': 'matchCriteria',
            'priority': 'priority'
        }

        self._id = None
        self._match_criteria = None
        self._priority = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this UpdateDrgRouteDistributionStatementDetails.
        The Oracle-assigned ID of each route distribution statement to be updated.


        :return: The id of this UpdateDrgRouteDistributionStatementDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateDrgRouteDistributionStatementDetails.
        The Oracle-assigned ID of each route distribution statement to be updated.


        :param id: The id of this UpdateDrgRouteDistributionStatementDetails.
        :type: str
        """
        self._id = id

    @property
    def match_criteria(self):
        """
        Gets the match_criteria of this UpdateDrgRouteDistributionStatementDetails.
        The action is applied only if all of the match criteria is met.


        :return: The match_criteria of this UpdateDrgRouteDistributionStatementDetails.
        :rtype: list[oci.vn_monitoring.models.DrgRouteDistributionMatchCriteria]
        """
        return self._match_criteria

    @match_criteria.setter
    def match_criteria(self, match_criteria):
        """
        Sets the match_criteria of this UpdateDrgRouteDistributionStatementDetails.
        The action is applied only if all of the match criteria is met.


        :param match_criteria: The match_criteria of this UpdateDrgRouteDistributionStatementDetails.
        :type: list[oci.vn_monitoring.models.DrgRouteDistributionMatchCriteria]
        """
        self._match_criteria = match_criteria

    @property
    def priority(self):
        """
        Gets the priority of this UpdateDrgRouteDistributionStatementDetails.
        The priority of the statement you'd like to update.


        :return: The priority of this UpdateDrgRouteDistributionStatementDetails.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this UpdateDrgRouteDistributionStatementDetails.
        The priority of the statement you'd like to update.


        :param priority: The priority of this UpdateDrgRouteDistributionStatementDetails.
        :type: int
        """
        self._priority = priority

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
