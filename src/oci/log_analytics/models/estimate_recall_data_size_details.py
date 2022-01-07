# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EstimateRecallDataSizeDetails(object):
    """
    This is the input used to estimate the size of data to be recalled
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EstimateRecallDataSizeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_data_started:
            The value to assign to the time_data_started property of this EstimateRecallDataSizeDetails.
        :type time_data_started: datetime

        :param time_data_ended:
            The value to assign to the time_data_ended property of this EstimateRecallDataSizeDetails.
        :type time_data_ended: datetime

        """
        self.swagger_types = {
            'time_data_started': 'datetime',
            'time_data_ended': 'datetime'
        }

        self.attribute_map = {
            'time_data_started': 'timeDataStarted',
            'time_data_ended': 'timeDataEnded'
        }

        self._time_data_started = None
        self._time_data_ended = None

    @property
    def time_data_started(self):
        """
        **[Required]** Gets the time_data_started of this EstimateRecallDataSizeDetails.
        This is the start of the time range for the data to be recalled


        :return: The time_data_started of this EstimateRecallDataSizeDetails.
        :rtype: datetime
        """
        return self._time_data_started

    @time_data_started.setter
    def time_data_started(self, time_data_started):
        """
        Sets the time_data_started of this EstimateRecallDataSizeDetails.
        This is the start of the time range for the data to be recalled


        :param time_data_started: The time_data_started of this EstimateRecallDataSizeDetails.
        :type: datetime
        """
        self._time_data_started = time_data_started

    @property
    def time_data_ended(self):
        """
        **[Required]** Gets the time_data_ended of this EstimateRecallDataSizeDetails.
        This is the end of the time range for the data to be recalled


        :return: The time_data_ended of this EstimateRecallDataSizeDetails.
        :rtype: datetime
        """
        return self._time_data_ended

    @time_data_ended.setter
    def time_data_ended(self, time_data_ended):
        """
        Sets the time_data_ended of this EstimateRecallDataSizeDetails.
        This is the end of the time range for the data to be recalled


        :param time_data_ended: The time_data_ended of this EstimateRecallDataSizeDetails.
        :type: datetime
        """
        self._time_data_ended = time_data_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
