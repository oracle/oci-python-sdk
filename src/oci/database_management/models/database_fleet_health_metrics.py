# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseFleetHealthMetrics(object):
    """
    The details of the fleet health metrics.
    """

    #: A constant which can be used with the compare_type property of a DatabaseFleetHealthMetrics.
    #: This constant has a value of "HOUR"
    COMPARE_TYPE_HOUR = "HOUR"

    #: A constant which can be used with the compare_type property of a DatabaseFleetHealthMetrics.
    #: This constant has a value of "DAY"
    COMPARE_TYPE_DAY = "DAY"

    #: A constant which can be used with the compare_type property of a DatabaseFleetHealthMetrics.
    #: This constant has a value of "WEEK"
    COMPARE_TYPE_WEEK = "WEEK"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseFleetHealthMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compare_baseline_time:
            The value to assign to the compare_baseline_time property of this DatabaseFleetHealthMetrics.
        :type compare_baseline_time: str

        :param compare_target_time:
            The value to assign to the compare_target_time property of this DatabaseFleetHealthMetrics.
        :type compare_target_time: str

        :param compare_type:
            The value to assign to the compare_type property of this DatabaseFleetHealthMetrics.
            Allowed values for this property are: "HOUR", "DAY", "WEEK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type compare_type: str

        :param fleet_summary:
            The value to assign to the fleet_summary property of this DatabaseFleetHealthMetrics.
        :type fleet_summary: oci.database_management.models.FleetSummary

        :param fleet_databases:
            The value to assign to the fleet_databases property of this DatabaseFleetHealthMetrics.
        :type fleet_databases: list[oci.database_management.models.DatabaseUsageMetrics]

        """
        self.swagger_types = {
            'compare_baseline_time': 'str',
            'compare_target_time': 'str',
            'compare_type': 'str',
            'fleet_summary': 'FleetSummary',
            'fleet_databases': 'list[DatabaseUsageMetrics]'
        }

        self.attribute_map = {
            'compare_baseline_time': 'compareBaselineTime',
            'compare_target_time': 'compareTargetTime',
            'compare_type': 'compareType',
            'fleet_summary': 'fleetSummary',
            'fleet_databases': 'fleetDatabases'
        }

        self._compare_baseline_time = None
        self._compare_target_time = None
        self._compare_type = None
        self._fleet_summary = None
        self._fleet_databases = None

    @property
    def compare_baseline_time(self):
        """
        **[Required]** Gets the compare_baseline_time of this DatabaseFleetHealthMetrics.
        The baseline date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".
        This is the date and time against which percentage change is calculated.


        :return: The compare_baseline_time of this DatabaseFleetHealthMetrics.
        :rtype: str
        """
        return self._compare_baseline_time

    @compare_baseline_time.setter
    def compare_baseline_time(self, compare_baseline_time):
        """
        Sets the compare_baseline_time of this DatabaseFleetHealthMetrics.
        The baseline date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".
        This is the date and time against which percentage change is calculated.


        :param compare_baseline_time: The compare_baseline_time of this DatabaseFleetHealthMetrics.
        :type: str
        """
        self._compare_baseline_time = compare_baseline_time

    @property
    def compare_target_time(self):
        """
        **[Required]** Gets the compare_target_time of this DatabaseFleetHealthMetrics.
        The target date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".
        All the metrics are returned for the target date and time and the percentage change
        is calculated against the baseline date and time.


        :return: The compare_target_time of this DatabaseFleetHealthMetrics.
        :rtype: str
        """
        return self._compare_target_time

    @compare_target_time.setter
    def compare_target_time(self, compare_target_time):
        """
        Sets the compare_target_time of this DatabaseFleetHealthMetrics.
        The target date and time in UTC in ISO-8601 format, which is \"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\".
        All the metrics are returned for the target date and time and the percentage change
        is calculated against the baseline date and time.


        :param compare_target_time: The compare_target_time of this DatabaseFleetHealthMetrics.
        :type: str
        """
        self._compare_target_time = compare_target_time

    @property
    def compare_type(self):
        """
        Gets the compare_type of this DatabaseFleetHealthMetrics.
        The time window used for metrics comparison.

        Allowed values for this property are: "HOUR", "DAY", "WEEK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The compare_type of this DatabaseFleetHealthMetrics.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """
        Sets the compare_type of this DatabaseFleetHealthMetrics.
        The time window used for metrics comparison.


        :param compare_type: The compare_type of this DatabaseFleetHealthMetrics.
        :type: str
        """
        allowed_values = ["HOUR", "DAY", "WEEK"]
        if not value_allowed_none_or_none_sentinel(compare_type, allowed_values):
            compare_type = 'UNKNOWN_ENUM_VALUE'
        self._compare_type = compare_type

    @property
    def fleet_summary(self):
        """
        Gets the fleet_summary of this DatabaseFleetHealthMetrics.

        :return: The fleet_summary of this DatabaseFleetHealthMetrics.
        :rtype: oci.database_management.models.FleetSummary
        """
        return self._fleet_summary

    @fleet_summary.setter
    def fleet_summary(self, fleet_summary):
        """
        Sets the fleet_summary of this DatabaseFleetHealthMetrics.

        :param fleet_summary: The fleet_summary of this DatabaseFleetHealthMetrics.
        :type: oci.database_management.models.FleetSummary
        """
        self._fleet_summary = fleet_summary

    @property
    def fleet_databases(self):
        """
        **[Required]** Gets the fleet_databases of this DatabaseFleetHealthMetrics.
        A list of the databases present in the fleet and their usage metrics.


        :return: The fleet_databases of this DatabaseFleetHealthMetrics.
        :rtype: list[oci.database_management.models.DatabaseUsageMetrics]
        """
        return self._fleet_databases

    @fleet_databases.setter
    def fleet_databases(self, fleet_databases):
        """
        Sets the fleet_databases of this DatabaseFleetHealthMetrics.
        A list of the databases present in the fleet and their usage metrics.


        :param fleet_databases: The fleet_databases of this DatabaseFleetHealthMetrics.
        :type: list[oci.database_management.models.DatabaseUsageMetrics]
        """
        self._fleet_databases = fleet_databases

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
