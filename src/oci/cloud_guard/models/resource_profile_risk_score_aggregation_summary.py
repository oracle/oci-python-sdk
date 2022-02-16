# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceProfileRiskScoreAggregationSummary(object):
    """
    Resource profile risk score trend-line
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceProfileRiskScoreAggregationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_profile_id:
            The value to assign to the resource_profile_id property of this ResourceProfileRiskScoreAggregationSummary.
        :type resource_profile_id: str

        :param resource_profile_display_name:
            The value to assign to the resource_profile_display_name property of this ResourceProfileRiskScoreAggregationSummary.
        :type resource_profile_display_name: str

        :param risk_threshold:
            The value to assign to the risk_threshold property of this ResourceProfileRiskScoreAggregationSummary.
        :type risk_threshold: int

        :param items:
            The value to assign to the items property of this ResourceProfileRiskScoreAggregationSummary.
        :type items: list[oci.cloud_guard.models.ResourceRiskScoreAggregation]

        """
        self.swagger_types = {
            'resource_profile_id': 'str',
            'resource_profile_display_name': 'str',
            'risk_threshold': 'int',
            'items': 'list[ResourceRiskScoreAggregation]'
        }

        self.attribute_map = {
            'resource_profile_id': 'resourceProfileId',
            'resource_profile_display_name': 'resourceProfileDisplayName',
            'risk_threshold': 'riskThreshold',
            'items': 'items'
        }

        self._resource_profile_id = None
        self._resource_profile_display_name = None
        self._risk_threshold = None
        self._items = None

    @property
    def resource_profile_id(self):
        """
        **[Required]** Gets the resource_profile_id of this ResourceProfileRiskScoreAggregationSummary.
        OCID for the resource profile


        :return: The resource_profile_id of this ResourceProfileRiskScoreAggregationSummary.
        :rtype: str
        """
        return self._resource_profile_id

    @resource_profile_id.setter
    def resource_profile_id(self, resource_profile_id):
        """
        Sets the resource_profile_id of this ResourceProfileRiskScoreAggregationSummary.
        OCID for the resource profile


        :param resource_profile_id: The resource_profile_id of this ResourceProfileRiskScoreAggregationSummary.
        :type: str
        """
        self._resource_profile_id = resource_profile_id

    @property
    def resource_profile_display_name(self):
        """
        **[Required]** Gets the resource_profile_display_name of this ResourceProfileRiskScoreAggregationSummary.
        Display name for the resource profile


        :return: The resource_profile_display_name of this ResourceProfileRiskScoreAggregationSummary.
        :rtype: str
        """
        return self._resource_profile_display_name

    @resource_profile_display_name.setter
    def resource_profile_display_name(self, resource_profile_display_name):
        """
        Sets the resource_profile_display_name of this ResourceProfileRiskScoreAggregationSummary.
        Display name for the resource profile


        :param resource_profile_display_name: The resource_profile_display_name of this ResourceProfileRiskScoreAggregationSummary.
        :type: str
        """
        self._resource_profile_display_name = resource_profile_display_name

    @property
    def risk_threshold(self):
        """
        Gets the risk_threshold of this ResourceProfileRiskScoreAggregationSummary.
        Risk threshold


        :return: The risk_threshold of this ResourceProfileRiskScoreAggregationSummary.
        :rtype: int
        """
        return self._risk_threshold

    @risk_threshold.setter
    def risk_threshold(self, risk_threshold):
        """
        Sets the risk_threshold of this ResourceProfileRiskScoreAggregationSummary.
        Risk threshold


        :param risk_threshold: The risk_threshold of this ResourceProfileRiskScoreAggregationSummary.
        :type: int
        """
        self._risk_threshold = risk_threshold

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ResourceProfileRiskScoreAggregationSummary.
        List of ResourceRiskScoreAggregation


        :return: The items of this ResourceProfileRiskScoreAggregationSummary.
        :rtype: list[oci.cloud_guard.models.ResourceRiskScoreAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ResourceProfileRiskScoreAggregationSummary.
        List of ResourceRiskScoreAggregation


        :param items: The items of this ResourceProfileRiskScoreAggregationSummary.
        :type: list[oci.cloud_guard.models.ResourceRiskScoreAggregation]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
