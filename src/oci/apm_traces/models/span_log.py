# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SpanLog(object):
    """
    Definition of a log which is a key-value pair of log data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SpanLog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param log_key:
            The value to assign to the log_key property of this SpanLog.
        :type log_key: str

        :param log_value:
            The value to assign to the log_value property of this SpanLog.
        :type log_value: str

        """
        self.swagger_types = {
            'log_key': 'str',
            'log_value': 'str'
        }

        self.attribute_map = {
            'log_key': 'logKey',
            'log_value': 'logValue'
        }

        self._log_key = None
        self._log_value = None

    @property
    def log_key(self):
        """
        **[Required]** Gets the log_key of this SpanLog.
        Key that specifies the log name.


        :return: The log_key of this SpanLog.
        :rtype: str
        """
        return self._log_key

    @log_key.setter
    def log_key(self, log_key):
        """
        Sets the log_key of this SpanLog.
        Key that specifies the log name.


        :param log_key: The log_key of this SpanLog.
        :type: str
        """
        self._log_key = log_key

    @property
    def log_value(self):
        """
        **[Required]** Gets the log_value of this SpanLog.
        Value associated with the log key.


        :return: The log_value of this SpanLog.
        :rtype: str
        """
        return self._log_value

    @log_value.setter
    def log_value(self, log_value):
        """
        Sets the log_value of this SpanLog.
        Value associated with the log key.


        :param log_value: The log_value of this SpanLog.
        :type: str
        """
        self._log_value = log_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
