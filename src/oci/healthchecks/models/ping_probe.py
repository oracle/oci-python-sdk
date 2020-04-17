# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PingProbe(object):
    """
    This model contains all of the mutable and immutable properties for a ping probe.
    """

    #: A constant which can be used with the protocol property of a PingProbe.
    #: This constant has a value of "ICMP"
    PROTOCOL_ICMP = "ICMP"

    #: A constant which can be used with the protocol property of a PingProbe.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new PingProbe object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PingProbe.
        :type id: str

        :param results_url:
            The value to assign to the results_url property of this PingProbe.
        :type results_url: str

        :param home_region:
            The value to assign to the home_region property of this PingProbe.
        :type home_region: str

        :param time_created:
            The value to assign to the time_created property of this PingProbe.
        :type time_created: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this PingProbe.
        :type compartment_id: str

        :param targets:
            The value to assign to the targets property of this PingProbe.
        :type targets: list[str]

        :param vantage_point_names:
            The value to assign to the vantage_point_names property of this PingProbe.
        :type vantage_point_names: list[str]

        :param port:
            The value to assign to the port property of this PingProbe.
        :type port: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this PingProbe.
        :type timeout_in_seconds: int

        :param protocol:
            The value to assign to the protocol property of this PingProbe.
            Allowed values for this property are: "ICMP", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        """
        self.swagger_types = {
            'id': 'str',
            'results_url': 'str',
            'home_region': 'str',
            'time_created': 'datetime',
            'compartment_id': 'str',
            'targets': 'list[str]',
            'vantage_point_names': 'list[str]',
            'port': 'int',
            'timeout_in_seconds': 'int',
            'protocol': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'results_url': 'resultsUrl',
            'home_region': 'homeRegion',
            'time_created': 'timeCreated',
            'compartment_id': 'compartmentId',
            'targets': 'targets',
            'vantage_point_names': 'vantagePointNames',
            'port': 'port',
            'timeout_in_seconds': 'timeoutInSeconds',
            'protocol': 'protocol'
        }

        self._id = None
        self._results_url = None
        self._home_region = None
        self._time_created = None
        self._compartment_id = None
        self._targets = None
        self._vantage_point_names = None
        self._port = None
        self._timeout_in_seconds = None
        self._protocol = None

    @property
    def id(self):
        """
        Gets the id of this PingProbe.
        The OCID of the resource.


        :return: The id of this PingProbe.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PingProbe.
        The OCID of the resource.


        :param id: The id of this PingProbe.
        :type: str
        """
        self._id = id

    @property
    def results_url(self):
        """
        Gets the results_url of this PingProbe.
        A URL for fetching the probe results.


        :return: The results_url of this PingProbe.
        :rtype: str
        """
        return self._results_url

    @results_url.setter
    def results_url(self, results_url):
        """
        Sets the results_url of this PingProbe.
        A URL for fetching the probe results.


        :param results_url: The results_url of this PingProbe.
        :type: str
        """
        self._results_url = results_url

    @property
    def home_region(self):
        """
        Gets the home_region of this PingProbe.
        The region where updates must be made and where results must be fetched from.


        :return: The home_region of this PingProbe.
        :rtype: str
        """
        return self._home_region

    @home_region.setter
    def home_region(self, home_region):
        """
        Sets the home_region of this PingProbe.
        The region where updates must be made and where results must be fetched from.


        :param home_region: The home_region of this PingProbe.
        :type: str
        """
        self._home_region = home_region

    @property
    def time_created(self):
        """
        Gets the time_created of this PingProbe.
        The RFC 3339-formatted creation date and time of the probe.


        :return: The time_created of this PingProbe.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PingProbe.
        The RFC 3339-formatted creation date and time of the probe.


        :param time_created: The time_created of this PingProbe.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this PingProbe.
        The OCID of the compartment.


        :return: The compartment_id of this PingProbe.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PingProbe.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this PingProbe.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def targets(self):
        """
        Gets the targets of this PingProbe.
        A list of targets (hostnames or IP addresses) of the probe.


        :return: The targets of this PingProbe.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this PingProbe.
        A list of targets (hostnames or IP addresses) of the probe.


        :param targets: The targets of this PingProbe.
        :type: list[str]
        """
        self._targets = targets

    @property
    def vantage_point_names(self):
        """
        Gets the vantage_point_names of this PingProbe.
        A list of names of vantage points from which to execute the probe.


        :return: The vantage_point_names of this PingProbe.
        :rtype: list[str]
        """
        return self._vantage_point_names

    @vantage_point_names.setter
    def vantage_point_names(self, vantage_point_names):
        """
        Sets the vantage_point_names of this PingProbe.
        A list of names of vantage points from which to execute the probe.


        :param vantage_point_names: The vantage_point_names of this PingProbe.
        :type: list[str]
        """
        self._vantage_point_names = vantage_point_names

    @property
    def port(self):
        """
        Gets the port of this PingProbe.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :return: The port of this PingProbe.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this PingProbe.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :param port: The port of this PingProbe.
        :type: int
        """
        self._port = port

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this PingProbe.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :return: The timeout_in_seconds of this PingProbe.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this PingProbe.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :param timeout_in_seconds: The timeout_in_seconds of this PingProbe.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def protocol(self):
        """
        Gets the protocol of this PingProbe.
        Allowed values for this property are: "ICMP", "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this PingProbe.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this PingProbe.

        :param protocol: The protocol of this PingProbe.
        :type: str
        """
        allowed_values = ["ICMP", "TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
