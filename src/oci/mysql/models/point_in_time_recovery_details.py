# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PointInTimeRecoveryDetails(object):
    """
    Point-in-time Recovery details like earliest and latest recovery time point for the DB System.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PointInTimeRecoveryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_earliest_recovery_point:
            The value to assign to the time_earliest_recovery_point property of this PointInTimeRecoveryDetails.
        :type time_earliest_recovery_point: datetime

        :param time_latest_recovery_point:
            The value to assign to the time_latest_recovery_point property of this PointInTimeRecoveryDetails.
        :type time_latest_recovery_point: datetime

        """
        self.swagger_types = {
            'time_earliest_recovery_point': 'datetime',
            'time_latest_recovery_point': 'datetime'
        }

        self.attribute_map = {
            'time_earliest_recovery_point': 'timeEarliestRecoveryPoint',
            'time_latest_recovery_point': 'timeLatestRecoveryPoint'
        }

        self._time_earliest_recovery_point = None
        self._time_latest_recovery_point = None

    @property
    def time_earliest_recovery_point(self):
        """
        **[Required]** Gets the time_earliest_recovery_point of this PointInTimeRecoveryDetails.
        Earliest recovery time point for the DB System, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_earliest_recovery_point of this PointInTimeRecoveryDetails.
        :rtype: datetime
        """
        return self._time_earliest_recovery_point

    @time_earliest_recovery_point.setter
    def time_earliest_recovery_point(self, time_earliest_recovery_point):
        """
        Sets the time_earliest_recovery_point of this PointInTimeRecoveryDetails.
        Earliest recovery time point for the DB System, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_earliest_recovery_point: The time_earliest_recovery_point of this PointInTimeRecoveryDetails.
        :type: datetime
        """
        self._time_earliest_recovery_point = time_earliest_recovery_point

    @property
    def time_latest_recovery_point(self):
        """
        **[Required]** Gets the time_latest_recovery_point of this PointInTimeRecoveryDetails.
        Latest recovery time point for the DB System, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_latest_recovery_point of this PointInTimeRecoveryDetails.
        :rtype: datetime
        """
        return self._time_latest_recovery_point

    @time_latest_recovery_point.setter
    def time_latest_recovery_point(self, time_latest_recovery_point):
        """
        Sets the time_latest_recovery_point of this PointInTimeRecoveryDetails.
        Latest recovery time point for the DB System, as described by `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_latest_recovery_point: The time_latest_recovery_point of this PointInTimeRecoveryDetails.
        :type: datetime
        """
        self._time_latest_recovery_point = time_latest_recovery_point

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
