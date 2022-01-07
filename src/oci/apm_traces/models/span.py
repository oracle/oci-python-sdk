# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Span(object):
    """
    Definition of a span object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Span object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Span.
        :type key: str

        :param parent_span_key:
            The value to assign to the parent_span_key property of this Span.
        :type parent_span_key: str

        :param trace_key:
            The value to assign to the trace_key property of this Span.
        :type trace_key: str

        :param time_started:
            The value to assign to the time_started property of this Span.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this Span.
        :type time_ended: datetime

        :param duration_in_ms:
            The value to assign to the duration_in_ms property of this Span.
        :type duration_in_ms: int

        :param operation_name:
            The value to assign to the operation_name property of this Span.
        :type operation_name: str

        :param service_name:
            The value to assign to the service_name property of this Span.
        :type service_name: str

        :param kind:
            The value to assign to the kind property of this Span.
        :type kind: str

        :param tags:
            The value to assign to the tags property of this Span.
        :type tags: list[oci.apm_traces.models.Tag]

        :param logs:
            The value to assign to the logs property of this Span.
        :type logs: list[oci.apm_traces.models.SpanLogCollection]

        :param is_error:
            The value to assign to the is_error property of this Span.
        :type is_error: bool

        """
        self.swagger_types = {
            'key': 'str',
            'parent_span_key': 'str',
            'trace_key': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'duration_in_ms': 'int',
            'operation_name': 'str',
            'service_name': 'str',
            'kind': 'str',
            'tags': 'list[Tag]',
            'logs': 'list[SpanLogCollection]',
            'is_error': 'bool'
        }

        self.attribute_map = {
            'key': 'key',
            'parent_span_key': 'parentSpanKey',
            'trace_key': 'traceKey',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'duration_in_ms': 'durationInMs',
            'operation_name': 'operationName',
            'service_name': 'serviceName',
            'kind': 'kind',
            'tags': 'tags',
            'logs': 'logs',
            'is_error': 'isError'
        }

        self._key = None
        self._parent_span_key = None
        self._trace_key = None
        self._time_started = None
        self._time_ended = None
        self._duration_in_ms = None
        self._operation_name = None
        self._service_name = None
        self._kind = None
        self._tags = None
        self._logs = None
        self._is_error = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this Span.
        Unique identifier (spanId) for the span.  Note that this field is
        defined as spanKey in the API to comply with OCI API fields naming conventions.
        The spanKey maps to the spanId in the APM repository.


        :return: The key of this Span.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Span.
        Unique identifier (spanId) for the span.  Note that this field is
        defined as spanKey in the API to comply with OCI API fields naming conventions.
        The spanKey maps to the spanId in the APM repository.


        :param key: The key of this Span.
        :type: str
        """
        self._key = key

    @property
    def parent_span_key(self):
        """
        Gets the parent_span_key of this Span.
        Unique parent identifier for the span if one exists. For root spans this will be null.


        :return: The parent_span_key of this Span.
        :rtype: str
        """
        return self._parent_span_key

    @parent_span_key.setter
    def parent_span_key(self, parent_span_key):
        """
        Sets the parent_span_key of this Span.
        Unique parent identifier for the span if one exists. For root spans this will be null.


        :param parent_span_key: The parent_span_key of this Span.
        :type: str
        """
        self._parent_span_key = parent_span_key

    @property
    def trace_key(self):
        """
        **[Required]** Gets the trace_key of this Span.
        Unique identifier for the trace.


        :return: The trace_key of this Span.
        :rtype: str
        """
        return self._trace_key

    @trace_key.setter
    def trace_key(self, trace_key):
        """
        Sets the trace_key of this Span.
        Unique identifier for the trace.


        :param trace_key: The trace_key of this Span.
        :type: str
        """
        self._trace_key = trace_key

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this Span.
        Span start time.  Timestamp when the span was started.


        :return: The time_started of this Span.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this Span.
        Span start time.  Timestamp when the span was started.


        :param time_started: The time_started of this Span.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        **[Required]** Gets the time_ended of this Span.
        Span end time.  Timestamp when the span was completed.


        :return: The time_ended of this Span.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this Span.
        Span end time.  Timestamp when the span was completed.


        :param time_ended: The time_ended of this Span.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def duration_in_ms(self):
        """
        **[Required]** Gets the duration_in_ms of this Span.
        Total span duration in milliseconds.


        :return: The duration_in_ms of this Span.
        :rtype: int
        """
        return self._duration_in_ms

    @duration_in_ms.setter
    def duration_in_ms(self, duration_in_ms):
        """
        Sets the duration_in_ms of this Span.
        Total span duration in milliseconds.


        :param duration_in_ms: The duration_in_ms of this Span.
        :type: int
        """
        self._duration_in_ms = duration_in_ms

    @property
    def operation_name(self):
        """
        **[Required]** Gets the operation_name of this Span.
        Span name associated with the trace.  This is usually the method or uri of the request.


        :return: The operation_name of this Span.
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """
        Sets the operation_name of this Span.
        Span name associated with the trace.  This is usually the method or uri of the request.


        :param operation_name: The operation_name of this Span.
        :type: str
        """
        self._operation_name = operation_name

    @property
    def service_name(self):
        """
        Gets the service_name of this Span.
        Service name associated with the span.


        :return: The service_name of this Span.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this Span.
        Service name associated with the span.


        :param service_name: The service_name of this Span.
        :type: str
        """
        self._service_name = service_name

    @property
    def kind(self):
        """
        Gets the kind of this Span.
        Kind associated with the span.


        :return: The kind of this Span.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this Span.
        Kind associated with the span.


        :param kind: The kind of this Span.
        :type: str
        """
        self._kind = kind

    @property
    def tags(self):
        """
        Gets the tags of this Span.
        List of tags associated with the span.


        :return: The tags of this Span.
        :rtype: list[oci.apm_traces.models.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Span.
        List of tags associated with the span.


        :param tags: The tags of this Span.
        :type: list[oci.apm_traces.models.Tag]
        """
        self._tags = tags

    @property
    def logs(self):
        """
        Gets the logs of this Span.
        List of logs associated with the span.


        :return: The logs of this Span.
        :rtype: list[oci.apm_traces.models.SpanLogCollection]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """
        Sets the logs of this Span.
        List of logs associated with the span.


        :param logs: The logs of this Span.
        :type: list[oci.apm_traces.models.SpanLogCollection]
        """
        self._logs = logs

    @property
    def is_error(self):
        """
        **[Required]** Gets the is_error of this Span.
        Indicates if the span has an error


        :return: The is_error of this Span.
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        """
        Sets the is_error of this Span.
        Indicates if the span has an error


        :param is_error: The is_error of this Span.
        :type: bool
        """
        self._is_error = is_error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
