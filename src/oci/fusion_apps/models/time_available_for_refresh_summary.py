# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20211201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TimeAvailableForRefreshSummary(object):
    """
    one available refresh time.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TimeAvailableForRefreshSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_available_for_refresh:
            The value to assign to the time_available_for_refresh property of this TimeAvailableForRefreshSummary.
        :type time_available_for_refresh: datetime

        """
        self.swagger_types = {
            'time_available_for_refresh': 'datetime'
        }
        self.attribute_map = {
            'time_available_for_refresh': 'timeAvailableForRefresh'
        }
        self._time_available_for_refresh = None

    @property
    def time_available_for_refresh(self):
        """
        **[Required]** Gets the time_available_for_refresh of this TimeAvailableForRefreshSummary.
        refresh time.


        :return: The time_available_for_refresh of this TimeAvailableForRefreshSummary.
        :rtype: datetime
        """
        return self._time_available_for_refresh

    @time_available_for_refresh.setter
    def time_available_for_refresh(self, time_available_for_refresh):
        """
        Sets the time_available_for_refresh of this TimeAvailableForRefreshSummary.
        refresh time.


        :param time_available_for_refresh: The time_available_for_refresh of this TimeAvailableForRefreshSummary.
        :type: datetime
        """
        self._time_available_for_refresh = time_available_for_refresh

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
