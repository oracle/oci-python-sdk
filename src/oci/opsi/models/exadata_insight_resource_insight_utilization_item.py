# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInsightResourceInsightUtilizationItem(object):
    """
    Object containing current utilization, projected utilization, id and daysToReach high and low utilization value.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInsightResourceInsightUtilizationItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this ExadataInsightResourceInsightUtilizationItem.
        :type exadata_insight_id: str

        :param exadata_display_name:
            The value to assign to the exadata_display_name property of this ExadataInsightResourceInsightUtilizationItem.
        :type exadata_display_name: str

        :param current_utilization:
            The value to assign to the current_utilization property of this ExadataInsightResourceInsightUtilizationItem.
        :type current_utilization: float

        :param projected_utilization:
            The value to assign to the projected_utilization property of this ExadataInsightResourceInsightUtilizationItem.
        :type projected_utilization: float

        :param days_to_reach_high_utilization:
            The value to assign to the days_to_reach_high_utilization property of this ExadataInsightResourceInsightUtilizationItem.
        :type days_to_reach_high_utilization: int

        :param days_to_reach_low_utilization:
            The value to assign to the days_to_reach_low_utilization property of this ExadataInsightResourceInsightUtilizationItem.
        :type days_to_reach_low_utilization: int

        """
        self.swagger_types = {
            'exadata_insight_id': 'str',
            'exadata_display_name': 'str',
            'current_utilization': 'float',
            'projected_utilization': 'float',
            'days_to_reach_high_utilization': 'int',
            'days_to_reach_low_utilization': 'int'
        }
        self.attribute_map = {
            'exadata_insight_id': 'exadataInsightId',
            'exadata_display_name': 'exadataDisplayName',
            'current_utilization': 'currentUtilization',
            'projected_utilization': 'projectedUtilization',
            'days_to_reach_high_utilization': 'daysToReachHighUtilization',
            'days_to_reach_low_utilization': 'daysToReachLowUtilization'
        }
        self._exadata_insight_id = None
        self._exadata_display_name = None
        self._current_utilization = None
        self._projected_utilization = None
        self._days_to_reach_high_utilization = None
        self._days_to_reach_low_utilization = None

    @property
    def exadata_insight_id(self):
        """
        **[Required]** Gets the exadata_insight_id of this ExadataInsightResourceInsightUtilizationItem.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_insight_id of this ExadataInsightResourceInsightUtilizationItem.
        :rtype: str
        """
        return self._exadata_insight_id

    @exadata_insight_id.setter
    def exadata_insight_id(self, exadata_insight_id):
        """
        Sets the exadata_insight_id of this ExadataInsightResourceInsightUtilizationItem.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_insight_id: The exadata_insight_id of this ExadataInsightResourceInsightUtilizationItem.
        :type: str
        """
        self._exadata_insight_id = exadata_insight_id

    @property
    def exadata_display_name(self):
        """
        Gets the exadata_display_name of this ExadataInsightResourceInsightUtilizationItem.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :return: The exadata_display_name of this ExadataInsightResourceInsightUtilizationItem.
        :rtype: str
        """
        return self._exadata_display_name

    @exadata_display_name.setter
    def exadata_display_name(self, exadata_display_name):
        """
        Sets the exadata_display_name of this ExadataInsightResourceInsightUtilizationItem.
        The user-friendly name for the Exadata system. The name does not have to be unique.


        :param exadata_display_name: The exadata_display_name of this ExadataInsightResourceInsightUtilizationItem.
        :type: str
        """
        self._exadata_display_name = exadata_display_name

    @property
    def current_utilization(self):
        """
        **[Required]** Gets the current_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Current utilization


        :return: The current_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :rtype: float
        """
        return self._current_utilization

    @current_utilization.setter
    def current_utilization(self, current_utilization):
        """
        Sets the current_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Current utilization


        :param current_utilization: The current_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :type: float
        """
        self._current_utilization = current_utilization

    @property
    def projected_utilization(self):
        """
        **[Required]** Gets the projected_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Projected utilization


        :return: The projected_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :rtype: float
        """
        return self._projected_utilization

    @projected_utilization.setter
    def projected_utilization(self, projected_utilization):
        """
        Sets the projected_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Projected utilization


        :param projected_utilization: The projected_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :type: float
        """
        self._projected_utilization = projected_utilization

    @property
    def days_to_reach_high_utilization(self):
        """
        **[Required]** Gets the days_to_reach_high_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Days to reach projected high utilization


        :return: The days_to_reach_high_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :rtype: int
        """
        return self._days_to_reach_high_utilization

    @days_to_reach_high_utilization.setter
    def days_to_reach_high_utilization(self, days_to_reach_high_utilization):
        """
        Sets the days_to_reach_high_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Days to reach projected high utilization


        :param days_to_reach_high_utilization: The days_to_reach_high_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :type: int
        """
        self._days_to_reach_high_utilization = days_to_reach_high_utilization

    @property
    def days_to_reach_low_utilization(self):
        """
        **[Required]** Gets the days_to_reach_low_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Days to reach projected low utilization


        :return: The days_to_reach_low_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :rtype: int
        """
        return self._days_to_reach_low_utilization

    @days_to_reach_low_utilization.setter
    def days_to_reach_low_utilization(self, days_to_reach_low_utilization):
        """
        Sets the days_to_reach_low_utilization of this ExadataInsightResourceInsightUtilizationItem.
        Days to reach projected low utilization


        :param days_to_reach_low_utilization: The days_to_reach_low_utilization of this ExadataInsightResourceInsightUtilizationItem.
        :type: int
        """
        self._days_to_reach_low_utilization = days_to_reach_low_utilization

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
