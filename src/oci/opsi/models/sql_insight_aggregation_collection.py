# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlInsightAggregationCollection(object):
    """
    SQL Insights response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlInsightAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SqlInsightAggregationCollection.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SqlInsightAggregationCollection.
        :type time_interval_end: datetime

        :param inventory:
            The value to assign to the inventory property of this SqlInsightAggregationCollection.
        :type inventory: oci.opsi.models.SqlInventory

        :param items:
            The value to assign to the items property of this SqlInsightAggregationCollection.
        :type items: list[oci.opsi.models.SqlInsightAggregation]

        :param thresholds:
            The value to assign to the thresholds property of this SqlInsightAggregationCollection.
        :type thresholds: oci.opsi.models.SqlInsightThresholds

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'inventory': 'SqlInventory',
            'items': 'list[SqlInsightAggregation]',
            'thresholds': 'SqlInsightThresholds'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'inventory': 'inventory',
            'items': 'items',
            'thresholds': 'thresholds'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._inventory = None
        self._items = None
        self._thresholds = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SqlInsightAggregationCollection.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SqlInsightAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SqlInsightAggregationCollection.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SqlInsightAggregationCollection.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SqlInsightAggregationCollection.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SqlInsightAggregationCollection.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SqlInsightAggregationCollection.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SqlInsightAggregationCollection.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def inventory(self):
        """
        **[Required]** Gets the inventory of this SqlInsightAggregationCollection.

        :return: The inventory of this SqlInsightAggregationCollection.
        :rtype: oci.opsi.models.SqlInventory
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """
        Sets the inventory of this SqlInsightAggregationCollection.

        :param inventory: The inventory of this SqlInsightAggregationCollection.
        :type: oci.opsi.models.SqlInventory
        """
        self._inventory = inventory

    @property
    def items(self):
        """
        **[Required]** Gets the items of this SqlInsightAggregationCollection.
        List of insights.


        :return: The items of this SqlInsightAggregationCollection.
        :rtype: list[oci.opsi.models.SqlInsightAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SqlInsightAggregationCollection.
        List of insights.


        :param items: The items of this SqlInsightAggregationCollection.
        :type: list[oci.opsi.models.SqlInsightAggregation]
        """
        self._items = items

    @property
    def thresholds(self):
        """
        **[Required]** Gets the thresholds of this SqlInsightAggregationCollection.

        :return: The thresholds of this SqlInsightAggregationCollection.
        :rtype: oci.opsi.models.SqlInsightThresholds
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, thresholds):
        """
        Sets the thresholds of this SqlInsightAggregationCollection.

        :param thresholds: The thresholds of this SqlInsightAggregationCollection.
        :type: oci.opsi.models.SqlInsightThresholds
        """
        self._thresholds = thresholds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
