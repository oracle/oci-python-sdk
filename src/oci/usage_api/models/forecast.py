# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Forecast(object):
    """
    Forcast configuration of usage/cost.
    """

    #: A constant which can be used with the forcast_type property of a Forecast.
    #: This constant has a value of "BASIC"
    FORCAST_TYPE_BASIC = "BASIC"

    def __init__(self, **kwargs):
        """
        Initializes a new Forecast object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param forcast_type:
            The value to assign to the forcast_type property of this Forecast.
            Allowed values for this property are: "BASIC"
        :type forcast_type: str

        :param time_forecast_started:
            The value to assign to the time_forecast_started property of this Forecast.
        :type time_forecast_started: datetime

        :param time_forecast_ended:
            The value to assign to the time_forecast_ended property of this Forecast.
        :type time_forecast_ended: datetime

        """
        self.swagger_types = {
            'forcast_type': 'str',
            'time_forecast_started': 'datetime',
            'time_forecast_ended': 'datetime'
        }

        self.attribute_map = {
            'forcast_type': 'forcastType',
            'time_forecast_started': 'timeForecastStarted',
            'time_forecast_ended': 'timeForecastEnded'
        }

        self._forcast_type = None
        self._time_forecast_started = None
        self._time_forecast_ended = None

    @property
    def forcast_type(self):
        """
        Gets the forcast_type of this Forecast.
        BASIC uses ETS to project future usage/cost based on history data. The basis for projections will be a rolling set of equivalent historical days for which projection is being made.

        Allowed values for this property are: "BASIC"


        :return: The forcast_type of this Forecast.
        :rtype: str
        """
        return self._forcast_type

    @forcast_type.setter
    def forcast_type(self, forcast_type):
        """
        Sets the forcast_type of this Forecast.
        BASIC uses ETS to project future usage/cost based on history data. The basis for projections will be a rolling set of equivalent historical days for which projection is being made.


        :param forcast_type: The forcast_type of this Forecast.
        :type: str
        """
        allowed_values = ["BASIC"]
        if not value_allowed_none_or_none_sentinel(forcast_type, allowed_values):
            raise ValueError(
                "Invalid value for `forcast_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._forcast_type = forcast_type

    @property
    def time_forecast_started(self):
        """
        **[Required]** Gets the time_forecast_started of this Forecast.
        forecast start time.


        :return: The time_forecast_started of this Forecast.
        :rtype: datetime
        """
        return self._time_forecast_started

    @time_forecast_started.setter
    def time_forecast_started(self, time_forecast_started):
        """
        Sets the time_forecast_started of this Forecast.
        forecast start time.


        :param time_forecast_started: The time_forecast_started of this Forecast.
        :type: datetime
        """
        self._time_forecast_started = time_forecast_started

    @property
    def time_forecast_ended(self):
        """
        **[Required]** Gets the time_forecast_ended of this Forecast.
        forecast end time.


        :return: The time_forecast_ended of this Forecast.
        :rtype: datetime
        """
        return self._time_forecast_ended

    @time_forecast_ended.setter
    def time_forecast_ended(self, time_forecast_ended):
        """
        Sets the time_forecast_ended of this Forecast.
        forecast end time.


        :param time_forecast_ended: The time_forecast_ended of this Forecast.
        :type: datetime
        """
        self._time_forecast_ended = time_forecast_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
