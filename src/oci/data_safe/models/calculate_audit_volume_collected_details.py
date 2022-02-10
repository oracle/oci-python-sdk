# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CalculateAuditVolumeCollectedDetails(object):
    """
    The details for calculating audit data volume collected by data safe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CalculateAuditVolumeCollectedDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_from_month:
            The value to assign to the time_from_month property of this CalculateAuditVolumeCollectedDetails.
        :type time_from_month: datetime

        :param time_to_month:
            The value to assign to the time_to_month property of this CalculateAuditVolumeCollectedDetails.
        :type time_to_month: datetime

        """
        self.swagger_types = {
            'time_from_month': 'datetime',
            'time_to_month': 'datetime'
        }

        self.attribute_map = {
            'time_from_month': 'timeFromMonth',
            'time_to_month': 'timeToMonth'
        }

        self._time_from_month = None
        self._time_to_month = None

    @property
    def time_from_month(self):
        """
        **[Required]** Gets the time_from_month of this CalculateAuditVolumeCollectedDetails.
        The date from which the audit volume collected by data safe has to be calculated, in the format defined by RFC3339.


        :return: The time_from_month of this CalculateAuditVolumeCollectedDetails.
        :rtype: datetime
        """
        return self._time_from_month

    @time_from_month.setter
    def time_from_month(self, time_from_month):
        """
        Sets the time_from_month of this CalculateAuditVolumeCollectedDetails.
        The date from which the audit volume collected by data safe has to be calculated, in the format defined by RFC3339.


        :param time_from_month: The time_from_month of this CalculateAuditVolumeCollectedDetails.
        :type: datetime
        """
        self._time_from_month = time_from_month

    @property
    def time_to_month(self):
        """
        Gets the time_to_month of this CalculateAuditVolumeCollectedDetails.
        The date from which the audit volume collected by data safe has to be calculated, in the format defined by RFC3339. If not specified, this will default to the current date.


        :return: The time_to_month of this CalculateAuditVolumeCollectedDetails.
        :rtype: datetime
        """
        return self._time_to_month

    @time_to_month.setter
    def time_to_month(self, time_to_month):
        """
        Sets the time_to_month of this CalculateAuditVolumeCollectedDetails.
        The date from which the audit volume collected by data safe has to be calculated, in the format defined by RFC3339. If not specified, this will default to the current date.


        :param time_to_month: The time_to_month of this CalculateAuditVolumeCollectedDetails.
        :type: datetime
        """
        self._time_to_month = time_to_month

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
