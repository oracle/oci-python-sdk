# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePingMonitorDetails(object):
    """
    The request body used to update a ping monitor.
    """

    #: A constant which can be used with the protocol property of a UpdatePingMonitorDetails.
    #: This constant has a value of "ICMP"
    PROTOCOL_ICMP = "ICMP"

    #: A constant which can be used with the protocol property of a UpdatePingMonitorDetails.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePingMonitorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param targets:
            The value to assign to the targets property of this UpdatePingMonitorDetails.
        :type targets: list[str]

        :param vantage_point_names:
            The value to assign to the vantage_point_names property of this UpdatePingMonitorDetails.
        :type vantage_point_names: list[str]

        :param port:
            The value to assign to the port property of this UpdatePingMonitorDetails.
        :type port: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this UpdatePingMonitorDetails.
        :type timeout_in_seconds: int

        :param protocol:
            The value to assign to the protocol property of this UpdatePingMonitorDetails.
            Allowed values for this property are: "ICMP", "TCP"
        :type protocol: str

        :param display_name:
            The value to assign to the display_name property of this UpdatePingMonitorDetails.
        :type display_name: str

        :param interval_in_seconds:
            The value to assign to the interval_in_seconds property of this UpdatePingMonitorDetails.
        :type interval_in_seconds: int

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdatePingMonitorDetails.
        :type is_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdatePingMonitorDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdatePingMonitorDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'targets': 'list[str]',
            'vantage_point_names': 'list[str]',
            'port': 'int',
            'timeout_in_seconds': 'int',
            'protocol': 'str',
            'display_name': 'str',
            'interval_in_seconds': 'int',
            'is_enabled': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'targets': 'targets',
            'vantage_point_names': 'vantagePointNames',
            'port': 'port',
            'timeout_in_seconds': 'timeoutInSeconds',
            'protocol': 'protocol',
            'display_name': 'displayName',
            'interval_in_seconds': 'intervalInSeconds',
            'is_enabled': 'isEnabled',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._targets = None
        self._vantage_point_names = None
        self._port = None
        self._timeout_in_seconds = None
        self._protocol = None
        self._display_name = None
        self._interval_in_seconds = None
        self._is_enabled = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def targets(self):
        """
        Gets the targets of this UpdatePingMonitorDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :return: The targets of this UpdatePingMonitorDetails.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this UpdatePingMonitorDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :param targets: The targets of this UpdatePingMonitorDetails.
        :type: list[str]
        """
        self._targets = targets

    @property
    def vantage_point_names(self):
        """
        Gets the vantage_point_names of this UpdatePingMonitorDetails.
        A list of names of vantage points from which to execute the probe.


        :return: The vantage_point_names of this UpdatePingMonitorDetails.
        :rtype: list[str]
        """
        return self._vantage_point_names

    @vantage_point_names.setter
    def vantage_point_names(self, vantage_point_names):
        """
        Sets the vantage_point_names of this UpdatePingMonitorDetails.
        A list of names of vantage points from which to execute the probe.


        :param vantage_point_names: The vantage_point_names of this UpdatePingMonitorDetails.
        :type: list[str]
        """
        self._vantage_point_names = vantage_point_names

    @property
    def port(self):
        """
        Gets the port of this UpdatePingMonitorDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :return: The port of this UpdatePingMonitorDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdatePingMonitorDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :param port: The port of this UpdatePingMonitorDetails.
        :type: int
        """
        self._port = port

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this UpdatePingMonitorDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :return: The timeout_in_seconds of this UpdatePingMonitorDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this UpdatePingMonitorDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :param timeout_in_seconds: The timeout_in_seconds of this UpdatePingMonitorDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def protocol(self):
        """
        Gets the protocol of this UpdatePingMonitorDetails.
        Allowed values for this property are: "ICMP", "TCP"


        :return: The protocol of this UpdatePingMonitorDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UpdatePingMonitorDetails.

        :param protocol: The protocol of this UpdatePingMonitorDetails.
        :type: str
        """
        allowed_values = ["ICMP", "TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdatePingMonitorDetails.
        A user-friendly and mutable name suitable for display in a user interface.


        :return: The display_name of this UpdatePingMonitorDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdatePingMonitorDetails.
        A user-friendly and mutable name suitable for display in a user interface.


        :param display_name: The display_name of this UpdatePingMonitorDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def interval_in_seconds(self):
        """
        Gets the interval_in_seconds of this UpdatePingMonitorDetails.
        The monitor interval in seconds. Valid values: 10, 30, and 60.


        :return: The interval_in_seconds of this UpdatePingMonitorDetails.
        :rtype: int
        """
        return self._interval_in_seconds

    @interval_in_seconds.setter
    def interval_in_seconds(self, interval_in_seconds):
        """
        Sets the interval_in_seconds of this UpdatePingMonitorDetails.
        The monitor interval in seconds. Valid values: 10, 30, and 60.


        :param interval_in_seconds: The interval_in_seconds of this UpdatePingMonitorDetails.
        :type: int
        """
        self._interval_in_seconds = interval_in_seconds

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdatePingMonitorDetails.
        Enables or disables the monitor. Set to 'true' to launch monitoring.


        :return: The is_enabled of this UpdatePingMonitorDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdatePingMonitorDetails.
        Enables or disables the monitor. Set to 'true' to launch monitoring.


        :param is_enabled: The is_enabled of this UpdatePingMonitorDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdatePingMonitorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace.  For more information,
        see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdatePingMonitorDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdatePingMonitorDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace.  For more information,
        see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdatePingMonitorDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdatePingMonitorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdatePingMonitorDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdatePingMonitorDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdatePingMonitorDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
