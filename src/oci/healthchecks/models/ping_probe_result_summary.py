# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PingProbeResultSummary(object):
    """
    The results returned by running a ping probe.  All times and durations are
    returned in milliseconds. All times are relative to the POSIX epoch
    (1970-01-01T00:00Z).
    """

    #: A constant which can be used with the error_category property of a PingProbeResultSummary.
    #: This constant has a value of "NONE"
    ERROR_CATEGORY_NONE = "NONE"

    #: A constant which can be used with the error_category property of a PingProbeResultSummary.
    #: This constant has a value of "DNS"
    ERROR_CATEGORY_DNS = "DNS"

    #: A constant which can be used with the error_category property of a PingProbeResultSummary.
    #: This constant has a value of "TRANSPORT"
    ERROR_CATEGORY_TRANSPORT = "TRANSPORT"

    #: A constant which can be used with the error_category property of a PingProbeResultSummary.
    #: This constant has a value of "NETWORK"
    ERROR_CATEGORY_NETWORK = "NETWORK"

    #: A constant which can be used with the error_category property of a PingProbeResultSummary.
    #: This constant has a value of "SYSTEM"
    ERROR_CATEGORY_SYSTEM = "SYSTEM"

    #: A constant which can be used with the protocol property of a PingProbeResultSummary.
    #: This constant has a value of "ICMP"
    PROTOCOL_ICMP = "ICMP"

    #: A constant which can be used with the protocol property of a PingProbeResultSummary.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new PingProbeResultSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this PingProbeResultSummary.
        :type key: str

        :param probe_configuration_id:
            The value to assign to the probe_configuration_id property of this PingProbeResultSummary.
        :type probe_configuration_id: str

        :param start_time:
            The value to assign to the start_time property of this PingProbeResultSummary.
        :type start_time: float

        :param target:
            The value to assign to the target property of this PingProbeResultSummary.
        :type target: str

        :param vantage_point_name:
            The value to assign to the vantage_point_name property of this PingProbeResultSummary.
        :type vantage_point_name: str

        :param is_timed_out:
            The value to assign to the is_timed_out property of this PingProbeResultSummary.
        :type is_timed_out: bool

        :param is_healthy:
            The value to assign to the is_healthy property of this PingProbeResultSummary.
        :type is_healthy: bool

        :param error_category:
            The value to assign to the error_category property of this PingProbeResultSummary.
            Allowed values for this property are: "NONE", "DNS", "TRANSPORT", "NETWORK", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type error_category: str

        :param error_message:
            The value to assign to the error_message property of this PingProbeResultSummary.
        :type error_message: str

        :param protocol:
            The value to assign to the protocol property of this PingProbeResultSummary.
            Allowed values for this property are: "ICMP", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param connection:
            The value to assign to the connection property of this PingProbeResultSummary.
        :type connection: Connection

        :param dns:
            The value to assign to the dns property of this PingProbeResultSummary.
        :type dns: DNS

        :param domain_lookup_start:
            The value to assign to the domain_lookup_start property of this PingProbeResultSummary.
        :type domain_lookup_start: float

        :param domain_lookup_end:
            The value to assign to the domain_lookup_end property of this PingProbeResultSummary.
        :type domain_lookup_end: float

        :param latency_in_ms:
            The value to assign to the latency_in_ms property of this PingProbeResultSummary.
        :type latency_in_ms: float

        :param icmp_code:
            The value to assign to the icmp_code property of this PingProbeResultSummary.
        :type icmp_code: int

        """
        self.swagger_types = {
            'key': 'str',
            'probe_configuration_id': 'str',
            'start_time': 'float',
            'target': 'str',
            'vantage_point_name': 'str',
            'is_timed_out': 'bool',
            'is_healthy': 'bool',
            'error_category': 'str',
            'error_message': 'str',
            'protocol': 'str',
            'connection': 'Connection',
            'dns': 'DNS',
            'domain_lookup_start': 'float',
            'domain_lookup_end': 'float',
            'latency_in_ms': 'float',
            'icmp_code': 'int'
        }

        self.attribute_map = {
            'key': 'key',
            'probe_configuration_id': 'probeConfigurationId',
            'start_time': 'startTime',
            'target': 'target',
            'vantage_point_name': 'vantagePointName',
            'is_timed_out': 'isTimedOut',
            'is_healthy': 'isHealthy',
            'error_category': 'errorCategory',
            'error_message': 'errorMessage',
            'protocol': 'protocol',
            'connection': 'connection',
            'dns': 'dns',
            'domain_lookup_start': 'domainLookupStart',
            'domain_lookup_end': 'domainLookupEnd',
            'latency_in_ms': 'latencyInMs',
            'icmp_code': 'icmpCode'
        }

        self._key = None
        self._probe_configuration_id = None
        self._start_time = None
        self._target = None
        self._vantage_point_name = None
        self._is_timed_out = None
        self._is_healthy = None
        self._error_category = None
        self._error_message = None
        self._protocol = None
        self._connection = None
        self._dns = None
        self._domain_lookup_start = None
        self._domain_lookup_end = None
        self._latency_in_ms = None
        self._icmp_code = None

    @property
    def key(self):
        """
        Gets the key of this PingProbeResultSummary.
        A value identifying this specific probe result. The key is only unique within
        the results of its probe configuration. The key may be reused after 90 days.


        :return: The key of this PingProbeResultSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PingProbeResultSummary.
        A value identifying this specific probe result. The key is only unique within
        the results of its probe configuration. The key may be reused after 90 days.


        :param key: The key of this PingProbeResultSummary.
        :type: str
        """
        self._key = key

    @property
    def probe_configuration_id(self):
        """
        Gets the probe_configuration_id of this PingProbeResultSummary.
        The OCID of the monitor or on-demand probe responsible for creating this result.


        :return: The probe_configuration_id of this PingProbeResultSummary.
        :rtype: str
        """
        return self._probe_configuration_id

    @probe_configuration_id.setter
    def probe_configuration_id(self, probe_configuration_id):
        """
        Sets the probe_configuration_id of this PingProbeResultSummary.
        The OCID of the monitor or on-demand probe responsible for creating this result.


        :param probe_configuration_id: The probe_configuration_id of this PingProbeResultSummary.
        :type: str
        """
        self._probe_configuration_id = probe_configuration_id

    @property
    def start_time(self):
        """
        Gets the start_time of this PingProbeResultSummary.
        The date and time the probe was executed, expressed in milliseconds since the
        POSIX epoch. This field is defined by the PerformanceResourceTiming interface
        of the W3C Resource Timing specification. For more information, see
        `Resource Timing`__.

        __ https://w3c.github.io/resource-timing/#sec-resource-timing


        :return: The start_time of this PingProbeResultSummary.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this PingProbeResultSummary.
        The date and time the probe was executed, expressed in milliseconds since the
        POSIX epoch. This field is defined by the PerformanceResourceTiming interface
        of the W3C Resource Timing specification. For more information, see
        `Resource Timing`__.

        __ https://w3c.github.io/resource-timing/#sec-resource-timing


        :param start_time: The start_time of this PingProbeResultSummary.
        :type: float
        """
        self._start_time = start_time

    @property
    def target(self):
        """
        Gets the target of this PingProbeResultSummary.
        The target hostname or IP address of the probe.


        :return: The target of this PingProbeResultSummary.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this PingProbeResultSummary.
        The target hostname or IP address of the probe.


        :param target: The target of this PingProbeResultSummary.
        :type: str
        """
        self._target = target

    @property
    def vantage_point_name(self):
        """
        Gets the vantage_point_name of this PingProbeResultSummary.
        The name of the vantage point that executed the probe.


        :return: The vantage_point_name of this PingProbeResultSummary.
        :rtype: str
        """
        return self._vantage_point_name

    @vantage_point_name.setter
    def vantage_point_name(self, vantage_point_name):
        """
        Sets the vantage_point_name of this PingProbeResultSummary.
        The name of the vantage point that executed the probe.


        :param vantage_point_name: The vantage_point_name of this PingProbeResultSummary.
        :type: str
        """
        self._vantage_point_name = vantage_point_name

    @property
    def is_timed_out(self):
        """
        Gets the is_timed_out of this PingProbeResultSummary.
        True if the probe did not complete before the configured `timeoutInSeconds` value.


        :return: The is_timed_out of this PingProbeResultSummary.
        :rtype: bool
        """
        return self._is_timed_out

    @is_timed_out.setter
    def is_timed_out(self, is_timed_out):
        """
        Sets the is_timed_out of this PingProbeResultSummary.
        True if the probe did not complete before the configured `timeoutInSeconds` value.


        :param is_timed_out: The is_timed_out of this PingProbeResultSummary.
        :type: bool
        """
        self._is_timed_out = is_timed_out

    @property
    def is_healthy(self):
        """
        Gets the is_healthy of this PingProbeResultSummary.
        True if the probe result is determined to be healthy based on probe
        type-specific criteria.  For HTTP probes, a probe result is considered
        healthy if the HTTP response code is greater than or equal to 200 and
        less than 300.


        :return: The is_healthy of this PingProbeResultSummary.
        :rtype: bool
        """
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, is_healthy):
        """
        Sets the is_healthy of this PingProbeResultSummary.
        True if the probe result is determined to be healthy based on probe
        type-specific criteria.  For HTTP probes, a probe result is considered
        healthy if the HTTP response code is greater than or equal to 200 and
        less than 300.


        :param is_healthy: The is_healthy of this PingProbeResultSummary.
        :type: bool
        """
        self._is_healthy = is_healthy

    @property
    def error_category(self):
        """
        Gets the error_category of this PingProbeResultSummary.
        The category of error if an error occurs executing the probe.
        The `errorMessage` field provides a message with the error details.
        * NONE - No error
        * DNS - DNS errors
        * TRANSPORT - Transport-related errors, for example a \"TLS certificate expired\" error.
        * NETWORK - Network-related errors, for example a \"network unreachable\" error.
        * SYSTEM - Internal system errors.

        Allowed values for this property are: "NONE", "DNS", "TRANSPORT", "NETWORK", "SYSTEM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The error_category of this PingProbeResultSummary.
        :rtype: str
        """
        return self._error_category

    @error_category.setter
    def error_category(self, error_category):
        """
        Sets the error_category of this PingProbeResultSummary.
        The category of error if an error occurs executing the probe.
        The `errorMessage` field provides a message with the error details.
        * NONE - No error
        * DNS - DNS errors
        * TRANSPORT - Transport-related errors, for example a \"TLS certificate expired\" error.
        * NETWORK - Network-related errors, for example a \"network unreachable\" error.
        * SYSTEM - Internal system errors.


        :param error_category: The error_category of this PingProbeResultSummary.
        :type: str
        """
        allowed_values = ["NONE", "DNS", "TRANSPORT", "NETWORK", "SYSTEM"]
        if not value_allowed_none_or_none_sentinel(error_category, allowed_values):
            error_category = 'UNKNOWN_ENUM_VALUE'
        self._error_category = error_category

    @property
    def error_message(self):
        """
        Gets the error_message of this PingProbeResultSummary.
        The error information indicating why a probe execution failed.


        :return: The error_message of this PingProbeResultSummary.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this PingProbeResultSummary.
        The error information indicating why a probe execution failed.


        :param error_message: The error_message of this PingProbeResultSummary.
        :type: str
        """
        self._error_message = error_message

    @property
    def protocol(self):
        """
        Gets the protocol of this PingProbeResultSummary.
        Allowed values for this property are: "ICMP", "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this PingProbeResultSummary.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this PingProbeResultSummary.

        :param protocol: The protocol of this PingProbeResultSummary.
        :type: str
        """
        allowed_values = ["ICMP", "TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def connection(self):
        """
        Gets the connection of this PingProbeResultSummary.

        :return: The connection of this PingProbeResultSummary.
        :rtype: Connection
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """
        Sets the connection of this PingProbeResultSummary.

        :param connection: The connection of this PingProbeResultSummary.
        :type: Connection
        """
        self._connection = connection

    @property
    def dns(self):
        """
        Gets the dns of this PingProbeResultSummary.

        :return: The dns of this PingProbeResultSummary.
        :rtype: DNS
        """
        return self._dns

    @dns.setter
    def dns(self, dns):
        """
        Sets the dns of this PingProbeResultSummary.

        :param dns: The dns of this PingProbeResultSummary.
        :type: DNS
        """
        self._dns = dns

    @property
    def domain_lookup_start(self):
        """
        Gets the domain_lookup_start of this PingProbeResultSummary.
        The time immediately before the vantage point starts the domain name lookup for
        the resource.


        :return: The domain_lookup_start of this PingProbeResultSummary.
        :rtype: float
        """
        return self._domain_lookup_start

    @domain_lookup_start.setter
    def domain_lookup_start(self, domain_lookup_start):
        """
        Sets the domain_lookup_start of this PingProbeResultSummary.
        The time immediately before the vantage point starts the domain name lookup for
        the resource.


        :param domain_lookup_start: The domain_lookup_start of this PingProbeResultSummary.
        :type: float
        """
        self._domain_lookup_start = domain_lookup_start

    @property
    def domain_lookup_end(self):
        """
        Gets the domain_lookup_end of this PingProbeResultSummary.
        The time immediately before the vantage point finishes the domain name lookup for
        the resource.


        :return: The domain_lookup_end of this PingProbeResultSummary.
        :rtype: float
        """
        return self._domain_lookup_end

    @domain_lookup_end.setter
    def domain_lookup_end(self, domain_lookup_end):
        """
        Sets the domain_lookup_end of this PingProbeResultSummary.
        The time immediately before the vantage point finishes the domain name lookup for
        the resource.


        :param domain_lookup_end: The domain_lookup_end of this PingProbeResultSummary.
        :type: float
        """
        self._domain_lookup_end = domain_lookup_end

    @property
    def latency_in_ms(self):
        """
        Gets the latency_in_ms of this PingProbeResultSummary.
        The latency of the probe execution, in milliseconds.


        :return: The latency_in_ms of this PingProbeResultSummary.
        :rtype: float
        """
        return self._latency_in_ms

    @latency_in_ms.setter
    def latency_in_ms(self, latency_in_ms):
        """
        Sets the latency_in_ms of this PingProbeResultSummary.
        The latency of the probe execution, in milliseconds.


        :param latency_in_ms: The latency_in_ms of this PingProbeResultSummary.
        :type: float
        """
        self._latency_in_ms = latency_in_ms

    @property
    def icmp_code(self):
        """
        Gets the icmp_code of this PingProbeResultSummary.
        The ICMP code of the response message.  This field is not used when the protocol
        is set to TCP.  For more information on ICMP codes, see
        `Internet Control Message Protocol (ICMP) Parameters`__.

        __ https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


        :return: The icmp_code of this PingProbeResultSummary.
        :rtype: int
        """
        return self._icmp_code

    @icmp_code.setter
    def icmp_code(self, icmp_code):
        """
        Sets the icmp_code of this PingProbeResultSummary.
        The ICMP code of the response message.  This field is not used when the protocol
        is set to TCP.  For more information on ICMP codes, see
        `Internet Control Message Protocol (ICMP) Parameters`__.

        __ https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


        :param icmp_code: The icmp_code of this PingProbeResultSummary.
        :type: int
        """
        self._icmp_code = icmp_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
