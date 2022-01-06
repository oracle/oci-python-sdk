# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExadataInsightResourceForecastTrendSummary(object):
    """
    List of resource id, name , capacity insight value, pattern, historical usage and projected data.
    """

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "LINEAR"
    PATTERN_LINEAR = "LINEAR"

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "MONTHLY_SEASONS"
    PATTERN_MONTHLY_SEASONS = "MONTHLY_SEASONS"

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "MONTHLY_AND_YEARLY_SEASONS"
    PATTERN_MONTHLY_AND_YEARLY_SEASONS = "MONTHLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "WEEKLY_SEASONS"
    PATTERN_WEEKLY_SEASONS = "WEEKLY_SEASONS"

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "WEEKLY_AND_MONTHLY_SEASONS"
    PATTERN_WEEKLY_AND_MONTHLY_SEASONS = "WEEKLY_AND_MONTHLY_SEASONS"

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "WEEKLY_MONTHLY_AND_YEARLY_SEASONS"
    PATTERN_WEEKLY_MONTHLY_AND_YEARLY_SEASONS = "WEEKLY_MONTHLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "WEEKLY_AND_YEARLY_SEASONS"
    PATTERN_WEEKLY_AND_YEARLY_SEASONS = "WEEKLY_AND_YEARLY_SEASONS"

    #: A constant which can be used with the pattern property of a ExadataInsightResourceForecastTrendSummary.
    #: This constant has a value of "YEARLY_SEASONS"
    PATTERN_YEARLY_SEASONS = "YEARLY_SEASONS"

    def __init__(self, **kwargs):
        """
        Initializes a new ExadataInsightResourceForecastTrendSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExadataInsightResourceForecastTrendSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this ExadataInsightResourceForecastTrendSummary.
        :type name: str

        :param days_to_reach_capacity:
            The value to assign to the days_to_reach_capacity property of this ExadataInsightResourceForecastTrendSummary.
        :type days_to_reach_capacity: int

        :param pattern:
            The value to assign to the pattern property of this ExadataInsightResourceForecastTrendSummary.
            Allowed values for this property are: "LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type pattern: str

        :param historical_data:
            The value to assign to the historical_data property of this ExadataInsightResourceForecastTrendSummary.
        :type historical_data: list[oci.opsi.models.HistoricalDataItem]

        :param projected_data:
            The value to assign to the projected_data property of this ExadataInsightResourceForecastTrendSummary.
        :type projected_data: list[oci.opsi.models.ProjectedDataItem]

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'days_to_reach_capacity': 'int',
            'pattern': 'str',
            'historical_data': 'list[HistoricalDataItem]',
            'projected_data': 'list[ProjectedDataItem]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'days_to_reach_capacity': 'daysToReachCapacity',
            'pattern': 'pattern',
            'historical_data': 'historicalData',
            'projected_data': 'projectedData'
        }

        self._id = None
        self._name = None
        self._days_to_reach_capacity = None
        self._pattern = None
        self._historical_data = None
        self._projected_data = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExadataInsightResourceForecastTrendSummary.
        The `OCID`__ of the database insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this ExadataInsightResourceForecastTrendSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExadataInsightResourceForecastTrendSummary.
        The `OCID`__ of the database insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExadataInsightResourceForecastTrendSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ExadataInsightResourceForecastTrendSummary.
        The name of the resource.


        :return: The name of this ExadataInsightResourceForecastTrendSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExadataInsightResourceForecastTrendSummary.
        The name of the resource.


        :param name: The name of this ExadataInsightResourceForecastTrendSummary.
        :type: str
        """
        self._name = name

    @property
    def days_to_reach_capacity(self):
        """
        **[Required]** Gets the days_to_reach_capacity of this ExadataInsightResourceForecastTrendSummary.
        Days to reach capacity for a storage server


        :return: The days_to_reach_capacity of this ExadataInsightResourceForecastTrendSummary.
        :rtype: int
        """
        return self._days_to_reach_capacity

    @days_to_reach_capacity.setter
    def days_to_reach_capacity(self, days_to_reach_capacity):
        """
        Sets the days_to_reach_capacity of this ExadataInsightResourceForecastTrendSummary.
        Days to reach capacity for a storage server


        :param days_to_reach_capacity: The days_to_reach_capacity of this ExadataInsightResourceForecastTrendSummary.
        :type: int
        """
        self._days_to_reach_capacity = days_to_reach_capacity

    @property
    def pattern(self):
        """
        **[Required]** Gets the pattern of this ExadataInsightResourceForecastTrendSummary.
        Time series patterns used in the forecasting.

        Allowed values for this property are: "LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The pattern of this ExadataInsightResourceForecastTrendSummary.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this ExadataInsightResourceForecastTrendSummary.
        Time series patterns used in the forecasting.


        :param pattern: The pattern of this ExadataInsightResourceForecastTrendSummary.
        :type: str
        """
        allowed_values = ["LINEAR", "MONTHLY_SEASONS", "MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_SEASONS", "WEEKLY_AND_MONTHLY_SEASONS", "WEEKLY_MONTHLY_AND_YEARLY_SEASONS", "WEEKLY_AND_YEARLY_SEASONS", "YEARLY_SEASONS"]
        if not value_allowed_none_or_none_sentinel(pattern, allowed_values):
            pattern = 'UNKNOWN_ENUM_VALUE'
        self._pattern = pattern

    @property
    def historical_data(self):
        """
        **[Required]** Gets the historical_data of this ExadataInsightResourceForecastTrendSummary.
        Time series data used for the forecast analysis.


        :return: The historical_data of this ExadataInsightResourceForecastTrendSummary.
        :rtype: list[oci.opsi.models.HistoricalDataItem]
        """
        return self._historical_data

    @historical_data.setter
    def historical_data(self, historical_data):
        """
        Sets the historical_data of this ExadataInsightResourceForecastTrendSummary.
        Time series data used for the forecast analysis.


        :param historical_data: The historical_data of this ExadataInsightResourceForecastTrendSummary.
        :type: list[oci.opsi.models.HistoricalDataItem]
        """
        self._historical_data = historical_data

    @property
    def projected_data(self):
        """
        **[Required]** Gets the projected_data of this ExadataInsightResourceForecastTrendSummary.
        Time series data result of the forecasting analysis.


        :return: The projected_data of this ExadataInsightResourceForecastTrendSummary.
        :rtype: list[oci.opsi.models.ProjectedDataItem]
        """
        return self._projected_data

    @projected_data.setter
    def projected_data(self, projected_data):
        """
        Sets the projected_data of this ExadataInsightResourceForecastTrendSummary.
        Time series data result of the forecasting analysis.


        :param projected_data: The projected_data of this ExadataInsightResourceForecastTrendSummary.
        :type: list[oci.opsi.models.ProjectedDataItem]
        """
        self._projected_data = projected_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
