# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Trace(object):
    """
    Definition of a trace object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Trace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Trace.
        :type key: str

        :param root_span_operation_name:
            The value to assign to the root_span_operation_name property of this Trace.
        :type root_span_operation_name: str

        :param time_earliest_span_started:
            The value to assign to the time_earliest_span_started property of this Trace.
        :type time_earliest_span_started: datetime

        :param time_latest_span_ended:
            The value to assign to the time_latest_span_ended property of this Trace.
        :type time_latest_span_ended: datetime

        :param span_count:
            The value to assign to the span_count property of this Trace.
        :type span_count: int

        :param error_span_count:
            The value to assign to the error_span_count property of this Trace.
        :type error_span_count: int

        :param root_span_service_name:
            The value to assign to the root_span_service_name property of this Trace.
        :type root_span_service_name: str

        :param time_root_span_started:
            The value to assign to the time_root_span_started property of this Trace.
        :type time_root_span_started: datetime

        :param time_root_span_ended:
            The value to assign to the time_root_span_ended property of this Trace.
        :type time_root_span_ended: datetime

        :param root_span_duration_in_ms:
            The value to assign to the root_span_duration_in_ms property of this Trace.
        :type root_span_duration_in_ms: int

        :param trace_duration_in_ms:
            The value to assign to the trace_duration_in_ms property of this Trace.
        :type trace_duration_in_ms: int

        :param is_fault:
            The value to assign to the is_fault property of this Trace.
        :type is_fault: bool

        :param trace_status:
            The value to assign to the trace_status property of this Trace.
        :type trace_status: str

        :param trace_error_type:
            The value to assign to the trace_error_type property of this Trace.
        :type trace_error_type: str

        :param trace_error_code:
            The value to assign to the trace_error_code property of this Trace.
        :type trace_error_code: str

        :param service_summaries:
            The value to assign to the service_summaries property of this Trace.
        :type service_summaries: list[oci.apm_traces.models.TraceServiceSummary]

        :param span_summary:
            The value to assign to the span_summary property of this Trace.
        :type span_summary: oci.apm_traces.models.TraceSpanSummary

        :param spans:
            The value to assign to the spans property of this Trace.
        :type spans: list[oci.apm_traces.models.Span]

        """
        self.swagger_types = {
            'key': 'str',
            'root_span_operation_name': 'str',
            'time_earliest_span_started': 'datetime',
            'time_latest_span_ended': 'datetime',
            'span_count': 'int',
            'error_span_count': 'int',
            'root_span_service_name': 'str',
            'time_root_span_started': 'datetime',
            'time_root_span_ended': 'datetime',
            'root_span_duration_in_ms': 'int',
            'trace_duration_in_ms': 'int',
            'is_fault': 'bool',
            'trace_status': 'str',
            'trace_error_type': 'str',
            'trace_error_code': 'str',
            'service_summaries': 'list[TraceServiceSummary]',
            'span_summary': 'TraceSpanSummary',
            'spans': 'list[Span]'
        }

        self.attribute_map = {
            'key': 'key',
            'root_span_operation_name': 'rootSpanOperationName',
            'time_earliest_span_started': 'timeEarliestSpanStarted',
            'time_latest_span_ended': 'timeLatestSpanEnded',
            'span_count': 'spanCount',
            'error_span_count': 'errorSpanCount',
            'root_span_service_name': 'rootSpanServiceName',
            'time_root_span_started': 'timeRootSpanStarted',
            'time_root_span_ended': 'timeRootSpanEnded',
            'root_span_duration_in_ms': 'rootSpanDurationInMs',
            'trace_duration_in_ms': 'traceDurationInMs',
            'is_fault': 'isFault',
            'trace_status': 'traceStatus',
            'trace_error_type': 'traceErrorType',
            'trace_error_code': 'traceErrorCode',
            'service_summaries': 'serviceSummaries',
            'span_summary': 'spanSummary',
            'spans': 'spans'
        }

        self._key = None
        self._root_span_operation_name = None
        self._time_earliest_span_started = None
        self._time_latest_span_ended = None
        self._span_count = None
        self._error_span_count = None
        self._root_span_service_name = None
        self._time_root_span_started = None
        self._time_root_span_ended = None
        self._root_span_duration_in_ms = None
        self._trace_duration_in_ms = None
        self._is_fault = None
        self._trace_status = None
        self._trace_error_type = None
        self._trace_error_code = None
        self._service_summaries = None
        self._span_summary = None
        self._spans = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Trace.
        Unique identifier (traceId) for the trace that represents the span set.  Note that this field is
        defined as traceKey in the API to comply with OCI API fields naming conventions.  The traceKey maps to
        the traceId in the APM repository.


        :return: The key of this Trace.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Trace.
        Unique identifier (traceId) for the trace that represents the span set.  Note that this field is
        defined as traceKey in the API to comply with OCI API fields naming conventions.  The traceKey maps to
        the traceId in the APM repository.


        :param key: The key of this Trace.
        :type: str
        """
        self._key = key

    @property
    def root_span_operation_name(self):
        """
        Gets the root_span_operation_name of this Trace.
        Root span name associated with the trace. This is usually the flow start operation name.
        Null if the root span is not yet completed.


        :return: The root_span_operation_name of this Trace.
        :rtype: str
        """
        return self._root_span_operation_name

    @root_span_operation_name.setter
    def root_span_operation_name(self, root_span_operation_name):
        """
        Sets the root_span_operation_name of this Trace.
        Root span name associated with the trace. This is usually the flow start operation name.
        Null if the root span is not yet completed.


        :param root_span_operation_name: The root_span_operation_name of this Trace.
        :type: str
        """
        self._root_span_operation_name = root_span_operation_name

    @property
    def time_earliest_span_started(self):
        """
        Gets the time_earliest_span_started of this Trace.
        Start time of the earliest span in this span collection.


        :return: The time_earliest_span_started of this Trace.
        :rtype: datetime
        """
        return self._time_earliest_span_started

    @time_earliest_span_started.setter
    def time_earliest_span_started(self, time_earliest_span_started):
        """
        Sets the time_earliest_span_started of this Trace.
        Start time of the earliest span in this span collection.


        :param time_earliest_span_started: The time_earliest_span_started of this Trace.
        :type: datetime
        """
        self._time_earliest_span_started = time_earliest_span_started

    @property
    def time_latest_span_ended(self):
        """
        Gets the time_latest_span_ended of this Trace.
        End time of the span that most recently ended in this span collection.


        :return: The time_latest_span_ended of this Trace.
        :rtype: datetime
        """
        return self._time_latest_span_ended

    @time_latest_span_ended.setter
    def time_latest_span_ended(self, time_latest_span_ended):
        """
        Sets the time_latest_span_ended of this Trace.
        End time of the span that most recently ended in this span collection.


        :param time_latest_span_ended: The time_latest_span_ended of this Trace.
        :type: datetime
        """
        self._time_latest_span_ended = time_latest_span_ended

    @property
    def span_count(self):
        """
        Gets the span_count of this Trace.
        The number of spans that have been processed by the system for this trace.  Note that there
        could be additional spans that have not been processed or reported yet if the trace is still
        in progress.


        :return: The span_count of this Trace.
        :rtype: int
        """
        return self._span_count

    @span_count.setter
    def span_count(self, span_count):
        """
        Sets the span_count of this Trace.
        The number of spans that have been processed by the system for this trace.  Note that there
        could be additional spans that have not been processed or reported yet if the trace is still
        in progress.


        :param span_count: The span_count of this Trace.
        :type: int
        """
        self._span_count = span_count

    @property
    def error_span_count(self):
        """
        Gets the error_span_count of this Trace.
        The number of spans with error that have been processed by the system for this trace.
        Note that the number of spans with errors may be less than the total number of actual spans
        in this trace.


        :return: The error_span_count of this Trace.
        :rtype: int
        """
        return self._error_span_count

    @error_span_count.setter
    def error_span_count(self, error_span_count):
        """
        Sets the error_span_count of this Trace.
        The number of spans with error that have been processed by the system for this trace.
        Note that the number of spans with errors may be less than the total number of actual spans
        in this trace.


        :param error_span_count: The error_span_count of this Trace.
        :type: int
        """
        self._error_span_count = error_span_count

    @property
    def root_span_service_name(self):
        """
        Gets the root_span_service_name of this Trace.
        Service associated with this trace.


        :return: The root_span_service_name of this Trace.
        :rtype: str
        """
        return self._root_span_service_name

    @root_span_service_name.setter
    def root_span_service_name(self, root_span_service_name):
        """
        Sets the root_span_service_name of this Trace.
        Service associated with this trace.


        :param root_span_service_name: The root_span_service_name of this Trace.
        :type: str
        """
        self._root_span_service_name = root_span_service_name

    @property
    def time_root_span_started(self):
        """
        Gets the time_root_span_started of this Trace.
        Start time of the root span for this span collection.


        :return: The time_root_span_started of this Trace.
        :rtype: datetime
        """
        return self._time_root_span_started

    @time_root_span_started.setter
    def time_root_span_started(self, time_root_span_started):
        """
        Sets the time_root_span_started of this Trace.
        Start time of the root span for this span collection.


        :param time_root_span_started: The time_root_span_started of this Trace.
        :type: datetime
        """
        self._time_root_span_started = time_root_span_started

    @property
    def time_root_span_ended(self):
        """
        Gets the time_root_span_ended of this Trace.
        End time of the root span for this span collection.


        :return: The time_root_span_ended of this Trace.
        :rtype: datetime
        """
        return self._time_root_span_ended

    @time_root_span_ended.setter
    def time_root_span_ended(self, time_root_span_ended):
        """
        Sets the time_root_span_ended of this Trace.
        End time of the root span for this span collection.


        :param time_root_span_ended: The time_root_span_ended of this Trace.
        :type: datetime
        """
        self._time_root_span_ended = time_root_span_ended

    @property
    def root_span_duration_in_ms(self):
        """
        Gets the root_span_duration_in_ms of this Trace.
        Time taken for the root span operation to complete in milliseconds.


        :return: The root_span_duration_in_ms of this Trace.
        :rtype: int
        """
        return self._root_span_duration_in_ms

    @root_span_duration_in_ms.setter
    def root_span_duration_in_ms(self, root_span_duration_in_ms):
        """
        Sets the root_span_duration_in_ms of this Trace.
        Time taken for the root span operation to complete in milliseconds.


        :param root_span_duration_in_ms: The root_span_duration_in_ms of this Trace.
        :type: int
        """
        self._root_span_duration_in_ms = root_span_duration_in_ms

    @property
    def trace_duration_in_ms(self):
        """
        Gets the trace_duration_in_ms of this Trace.
        Time between the start of the earliest span and the end of the most recent span in milliseconds.


        :return: The trace_duration_in_ms of this Trace.
        :rtype: int
        """
        return self._trace_duration_in_ms

    @trace_duration_in_ms.setter
    def trace_duration_in_ms(self, trace_duration_in_ms):
        """
        Sets the trace_duration_in_ms of this Trace.
        Time between the start of the earliest span and the end of the most recent span in milliseconds.


        :param trace_duration_in_ms: The trace_duration_in_ms of this Trace.
        :type: int
        """
        self._trace_duration_in_ms = trace_duration_in_ms

    @property
    def is_fault(self):
        """
        Gets the is_fault of this Trace.
        Boolean flag that indicates whether the trace errored out.


        :return: The is_fault of this Trace.
        :rtype: bool
        """
        return self._is_fault

    @is_fault.setter
    def is_fault(self, is_fault):
        """
        Sets the is_fault of this Trace.
        Boolean flag that indicates whether the trace errored out.


        :param is_fault: The is_fault of this Trace.
        :type: bool
        """
        self._is_fault = is_fault

    @property
    def trace_status(self):
        """
        Gets the trace_status of this Trace.
        The status of the trace.
        The trace statuses are defined as follows:
        complete \u2013 a root span has been recorded, but there is no information on the errors.
        success - a complete root span is recorded there is a successful error type and error code - HTTP 200.
        incomplete - the root span has not yet been received.
        error - the root span returned with an error. There may or may not be an associated error code or error type.


        :return: The trace_status of this Trace.
        :rtype: str
        """
        return self._trace_status

    @trace_status.setter
    def trace_status(self, trace_status):
        """
        Sets the trace_status of this Trace.
        The status of the trace.
        The trace statuses are defined as follows:
        complete \u2013 a root span has been recorded, but there is no information on the errors.
        success - a complete root span is recorded there is a successful error type and error code - HTTP 200.
        incomplete - the root span has not yet been received.
        error - the root span returned with an error. There may or may not be an associated error code or error type.


        :param trace_status: The trace_status of this Trace.
        :type: str
        """
        self._trace_status = trace_status

    @property
    def trace_error_type(self):
        """
        Gets the trace_error_type of this Trace.
        Error type of the trace.


        :return: The trace_error_type of this Trace.
        :rtype: str
        """
        return self._trace_error_type

    @trace_error_type.setter
    def trace_error_type(self, trace_error_type):
        """
        Sets the trace_error_type of this Trace.
        Error type of the trace.


        :param trace_error_type: The trace_error_type of this Trace.
        :type: str
        """
        self._trace_error_type = trace_error_type

    @property
    def trace_error_code(self):
        """
        Gets the trace_error_code of this Trace.
        Error code of the trace.


        :return: The trace_error_code of this Trace.
        :rtype: str
        """
        return self._trace_error_code

    @trace_error_code.setter
    def trace_error_code(self, trace_error_code):
        """
        Sets the trace_error_code of this Trace.
        Error code of the trace.


        :param trace_error_code: The trace_error_code of this Trace.
        :type: str
        """
        self._trace_error_code = trace_error_code

    @property
    def service_summaries(self):
        """
        Gets the service_summaries of this Trace.
        A summary of the spans by service


        :return: The service_summaries of this Trace.
        :rtype: list[oci.apm_traces.models.TraceServiceSummary]
        """
        return self._service_summaries

    @service_summaries.setter
    def service_summaries(self, service_summaries):
        """
        Sets the service_summaries of this Trace.
        A summary of the spans by service


        :param service_summaries: The service_summaries of this Trace.
        :type: list[oci.apm_traces.models.TraceServiceSummary]
        """
        self._service_summaries = service_summaries

    @property
    def span_summary(self):
        """
        Gets the span_summary of this Trace.

        :return: The span_summary of this Trace.
        :rtype: oci.apm_traces.models.TraceSpanSummary
        """
        return self._span_summary

    @span_summary.setter
    def span_summary(self, span_summary):
        """
        Sets the span_summary of this Trace.

        :param span_summary: The span_summary of this Trace.
        :type: oci.apm_traces.models.TraceSpanSummary
        """
        self._span_summary = span_summary

    @property
    def spans(self):
        """
        **[Required]** Gets the spans of this Trace.
        An array of spans in the trace.


        :return: The spans of this Trace.
        :rtype: list[oci.apm_traces.models.Span]
        """
        return self._spans

    @spans.setter
    def spans(self, spans):
        """
        Sets the spans of this Trace.
        An array of spans in the trace.


        :param spans: The spans of this Trace.
        :type: list[oci.apm_traces.models.Span]
        """
        self._spans = spans

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
