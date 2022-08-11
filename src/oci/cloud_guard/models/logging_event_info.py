# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_source_event_info import DataSourceEventInfo
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoggingEventInfo(DataSourceEventInfo):
    """
    The information about new Logging event detail of DataSource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LoggingEventInfo object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.LoggingEventInfo.data_source_feed_provider` attribute
        of this class is ``LOGGINGQUERY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_source_feed_provider:
            The value to assign to the data_source_feed_provider property of this LoggingEventInfo.
            Allowed values for this property are: "LOGGINGQUERY"
        :type data_source_feed_provider: str

        :param observed_value:
            The value to assign to the observed_value property of this LoggingEventInfo.
        :type observed_value: str

        :param trigger_value:
            The value to assign to the trigger_value property of this LoggingEventInfo.
        :type trigger_value: str

        :param operator:
            The value to assign to the operator property of this LoggingEventInfo.
        :type operator: str

        :param log_result:
            The value to assign to the log_result property of this LoggingEventInfo.
        :type log_result: str

        """
        self.swagger_types = {
            'data_source_feed_provider': 'str',
            'observed_value': 'str',
            'trigger_value': 'str',
            'operator': 'str',
            'log_result': 'str'
        }

        self.attribute_map = {
            'data_source_feed_provider': 'dataSourceFeedProvider',
            'observed_value': 'observedValue',
            'trigger_value': 'triggerValue',
            'operator': 'operator',
            'log_result': 'logResult'
        }

        self._data_source_feed_provider = None
        self._observed_value = None
        self._trigger_value = None
        self._operator = None
        self._log_result = None
        self._data_source_feed_provider = 'LOGGINGQUERY'

    @property
    def observed_value(self):
        """
        Gets the observed_value of this LoggingEventInfo.

        :return: The observed_value of this LoggingEventInfo.
        :rtype: str
        """
        return self._observed_value

    @observed_value.setter
    def observed_value(self, observed_value):
        """
        Sets the observed_value of this LoggingEventInfo.

        :param observed_value: The observed_value of this LoggingEventInfo.
        :type: str
        """
        self._observed_value = observed_value

    @property
    def trigger_value(self):
        """
        Gets the trigger_value of this LoggingEventInfo.

        :return: The trigger_value of this LoggingEventInfo.
        :rtype: str
        """
        return self._trigger_value

    @trigger_value.setter
    def trigger_value(self, trigger_value):
        """
        Sets the trigger_value of this LoggingEventInfo.

        :param trigger_value: The trigger_value of this LoggingEventInfo.
        :type: str
        """
        self._trigger_value = trigger_value

    @property
    def operator(self):
        """
        Gets the operator of this LoggingEventInfo.

        :return: The operator of this LoggingEventInfo.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this LoggingEventInfo.

        :param operator: The operator of this LoggingEventInfo.
        :type: str
        """
        self._operator = operator

    @property
    def log_result(self):
        """
        Gets the log_result of this LoggingEventInfo.

        :return: The log_result of this LoggingEventInfo.
        :rtype: str
        """
        return self._log_result

    @log_result.setter
    def log_result(self, log_result):
        """
        Sets the log_result of this LoggingEventInfo.

        :param log_result: The log_result of this LoggingEventInfo.
        :type: str
        """
        self._log_result = log_result

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
