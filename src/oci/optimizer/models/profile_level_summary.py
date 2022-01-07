# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileLevelSummary(object):
    """
    The metadata associated with the profile level summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileLevelSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ProfileLevelSummary.
        :type name: str

        :param recommendation_name:
            The value to assign to the recommendation_name property of this ProfileLevelSummary.
        :type recommendation_name: str

        :param metrics:
            The value to assign to the metrics property of this ProfileLevelSummary.
        :type metrics: list[oci.optimizer.models.EvaluatedMetric]

        :param default_interval:
            The value to assign to the default_interval property of this ProfileLevelSummary.
        :type default_interval: int

        :param valid_intervals:
            The value to assign to the valid_intervals property of this ProfileLevelSummary.
        :type valid_intervals: list[int]

        :param time_created:
            The value to assign to the time_created property of this ProfileLevelSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ProfileLevelSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'recommendation_name': 'str',
            'metrics': 'list[EvaluatedMetric]',
            'default_interval': 'int',
            'valid_intervals': 'list[int]',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'name': 'name',
            'recommendation_name': 'recommendationName',
            'metrics': 'metrics',
            'default_interval': 'defaultInterval',
            'valid_intervals': 'validIntervals',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._name = None
        self._recommendation_name = None
        self._metrics = None
        self._default_interval = None
        self._valid_intervals = None
        self._time_created = None
        self._time_updated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ProfileLevelSummary.
        A unique name for the profile level.


        :return: The name of this ProfileLevelSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProfileLevelSummary.
        A unique name for the profile level.


        :param name: The name of this ProfileLevelSummary.
        :type: str
        """
        self._name = name

    @property
    def recommendation_name(self):
        """
        **[Required]** Gets the recommendation_name of this ProfileLevelSummary.
        The name of the recommendation this profile level applies to.


        :return: The recommendation_name of this ProfileLevelSummary.
        :rtype: str
        """
        return self._recommendation_name

    @recommendation_name.setter
    def recommendation_name(self, recommendation_name):
        """
        Sets the recommendation_name of this ProfileLevelSummary.
        The name of the recommendation this profile level applies to.


        :param recommendation_name: The recommendation_name of this ProfileLevelSummary.
        :type: str
        """
        self._recommendation_name = recommendation_name

    @property
    def metrics(self):
        """
        **[Required]** Gets the metrics of this ProfileLevelSummary.
        The metrics that will be evaluated by profiles using this profile level.


        :return: The metrics of this ProfileLevelSummary.
        :rtype: list[oci.optimizer.models.EvaluatedMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this ProfileLevelSummary.
        The metrics that will be evaluated by profiles using this profile level.


        :param metrics: The metrics of this ProfileLevelSummary.
        :type: list[oci.optimizer.models.EvaluatedMetric]
        """
        self._metrics = metrics

    @property
    def default_interval(self):
        """
        **[Required]** Gets the default_interval of this ProfileLevelSummary.
        The default aggregation interval (in days) for profiles using this profile level.


        :return: The default_interval of this ProfileLevelSummary.
        :rtype: int
        """
        return self._default_interval

    @default_interval.setter
    def default_interval(self, default_interval):
        """
        Sets the default_interval of this ProfileLevelSummary.
        The default aggregation interval (in days) for profiles using this profile level.


        :param default_interval: The default_interval of this ProfileLevelSummary.
        :type: int
        """
        self._default_interval = default_interval

    @property
    def valid_intervals(self):
        """
        **[Required]** Gets the valid_intervals of this ProfileLevelSummary.
        An array of aggregation intervals (in days) allowed for profiles using this profile level.


        :return: The valid_intervals of this ProfileLevelSummary.
        :rtype: list[int]
        """
        return self._valid_intervals

    @valid_intervals.setter
    def valid_intervals(self, valid_intervals):
        """
        Sets the valid_intervals of this ProfileLevelSummary.
        An array of aggregation intervals (in days) allowed for profiles using this profile level.


        :param valid_intervals: The valid_intervals of this ProfileLevelSummary.
        :type: list[int]
        """
        self._valid_intervals = valid_intervals

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ProfileLevelSummary.
        The date and time the category details were created, in the format defined by RFC3339.


        :return: The time_created of this ProfileLevelSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProfileLevelSummary.
        The date and time the category details were created, in the format defined by RFC3339.


        :param time_created: The time_created of this ProfileLevelSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ProfileLevelSummary.
        The date and time the category details were last updated, in the format defined by RFC3339.


        :return: The time_updated of this ProfileLevelSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ProfileLevelSummary.
        The date and time the category details were last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this ProfileLevelSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
