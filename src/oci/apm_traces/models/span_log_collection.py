# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SpanLogCollection(object):
    """
    Definition of span log collection object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SpanLogCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_created:
            The value to assign to the time_created property of this SpanLogCollection.
        :type time_created: datetime

        :param span_logs:
            The value to assign to the span_logs property of this SpanLogCollection.
        :type span_logs: list[oci.apm_traces.models.SpanLog]

        """
        self.swagger_types = {
            'time_created': 'datetime',
            'span_logs': 'list[SpanLog]'
        }

        self.attribute_map = {
            'time_created': 'timeCreated',
            'span_logs': 'spanLogs'
        }

        self._time_created = None
        self._span_logs = None

    @property
    def time_created(self):
        """
        Gets the time_created of this SpanLogCollection.
        Timestamp at which the log is created.


        :return: The time_created of this SpanLogCollection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SpanLogCollection.
        Timestamp at which the log is created.


        :param time_created: The time_created of this SpanLogCollection.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def span_logs(self):
        """
        Gets the span_logs of this SpanLogCollection.
        List of logs associated with the span at the given timestamp.


        :return: The span_logs of this SpanLogCollection.
        :rtype: list[oci.apm_traces.models.SpanLog]
        """
        return self._span_logs

    @span_logs.setter
    def span_logs(self, span_logs):
        """
        Sets the span_logs of this SpanLogCollection.
        List of logs associated with the span at the given timestamp.


        :param span_logs: The span_logs of this SpanLogCollection.
        :type: list[oci.apm_traces.models.SpanLog]
        """
        self._span_logs = span_logs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
