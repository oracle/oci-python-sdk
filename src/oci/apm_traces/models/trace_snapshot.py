# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TraceSnapshot(object):
    """
    Definition of a trace snapshot object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TraceSnapshot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TraceSnapshot.
        :type key: str

        :param time_started:
            The value to assign to the time_started property of this TraceSnapshot.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this TraceSnapshot.
        :type time_ended: datetime

        :param trace_snapshot_details:
            The value to assign to the trace_snapshot_details property of this TraceSnapshot.
        :type trace_snapshot_details: list[oci.apm_traces.models.SnapshotDetail]

        :param span_snapshots:
            The value to assign to the span_snapshots property of this TraceSnapshot.
        :type span_snapshots: list[oci.apm_traces.models.SpanSnapshot]

        """
        self.swagger_types = {
            'key': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'trace_snapshot_details': 'list[SnapshotDetail]',
            'span_snapshots': 'list[SpanSnapshot]'
        }

        self.attribute_map = {
            'key': 'key',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'trace_snapshot_details': 'traceSnapshotDetails',
            'span_snapshots': 'spanSnapshots'
        }

        self._key = None
        self._time_started = None
        self._time_ended = None
        self._trace_snapshot_details = None
        self._span_snapshots = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TraceSnapshot.
        Unique identifier (traceId) for the trace that represents the span set.  Note that this field is
        defined as traceKey in the API and it maps to the traceId in the trace data in Application Performance
        Monitoring.


        :return: The key of this TraceSnapshot.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TraceSnapshot.
        Unique identifier (traceId) for the trace that represents the span set.  Note that this field is
        defined as traceKey in the API and it maps to the traceId in the trace data in Application Performance
        Monitoring.


        :param key: The key of this TraceSnapshot.
        :type: str
        """
        self._key = key

    @property
    def time_started(self):
        """
        Gets the time_started of this TraceSnapshot.
        Start time of the trace.


        :return: The time_started of this TraceSnapshot.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this TraceSnapshot.
        Start time of the trace.


        :param time_started: The time_started of this TraceSnapshot.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this TraceSnapshot.
        End time of the trace.


        :return: The time_ended of this TraceSnapshot.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this TraceSnapshot.
        End time of the trace.


        :param time_ended: The time_ended of this TraceSnapshot.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def trace_snapshot_details(self):
        """
        Gets the trace_snapshot_details of this TraceSnapshot.
        Trace snapshots properties.


        :return: The trace_snapshot_details of this TraceSnapshot.
        :rtype: list[oci.apm_traces.models.SnapshotDetail]
        """
        return self._trace_snapshot_details

    @trace_snapshot_details.setter
    def trace_snapshot_details(self, trace_snapshot_details):
        """
        Sets the trace_snapshot_details of this TraceSnapshot.
        Trace snapshots properties.


        :param trace_snapshot_details: The trace_snapshot_details of this TraceSnapshot.
        :type: list[oci.apm_traces.models.SnapshotDetail]
        """
        self._trace_snapshot_details = trace_snapshot_details

    @property
    def span_snapshots(self):
        """
        **[Required]** Gets the span_snapshots of this TraceSnapshot.
        List of spans.


        :return: The span_snapshots of this TraceSnapshot.
        :rtype: list[oci.apm_traces.models.SpanSnapshot]
        """
        return self._span_snapshots

    @span_snapshots.setter
    def span_snapshots(self, span_snapshots):
        """
        Sets the span_snapshots of this TraceSnapshot.
        List of spans.


        :param span_snapshots: The span_snapshots of this TraceSnapshot.
        :type: list[oci.apm_traces.models.SpanSnapshot]
        """
        self._span_snapshots = span_snapshots

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
