# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOnDemandPingProbeDetails(object):
    """
    The request body used to create an on-demand ping probe.
    """

    #: A constant which can be used with the protocol property of a CreateOnDemandPingProbeDetails.
    #: This constant has a value of "ICMP"
    PROTOCOL_ICMP = "ICMP"

    #: A constant which can be used with the protocol property of a CreateOnDemandPingProbeDetails.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOnDemandPingProbeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOnDemandPingProbeDetails.
        :type compartment_id: str

        :param targets:
            The value to assign to the targets property of this CreateOnDemandPingProbeDetails.
        :type targets: list[str]

        :param vantage_point_names:
            The value to assign to the vantage_point_names property of this CreateOnDemandPingProbeDetails.
        :type vantage_point_names: list[str]

        :param port:
            The value to assign to the port property of this CreateOnDemandPingProbeDetails.
        :type port: int

        :param timeout_in_seconds:
            The value to assign to the timeout_in_seconds property of this CreateOnDemandPingProbeDetails.
        :type timeout_in_seconds: int

        :param protocol:
            The value to assign to the protocol property of this CreateOnDemandPingProbeDetails.
            Allowed values for this property are: "ICMP", "TCP"
        :type protocol: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'targets': 'list[str]',
            'vantage_point_names': 'list[str]',
            'port': 'int',
            'timeout_in_seconds': 'int',
            'protocol': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'targets': 'targets',
            'vantage_point_names': 'vantagePointNames',
            'port': 'port',
            'timeout_in_seconds': 'timeoutInSeconds',
            'protocol': 'protocol'
        }

        self._compartment_id = None
        self._targets = None
        self._vantage_point_names = None
        self._port = None
        self._timeout_in_seconds = None
        self._protocol = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOnDemandPingProbeDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateOnDemandPingProbeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOnDemandPingProbeDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateOnDemandPingProbeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def targets(self):
        """
        **[Required]** Gets the targets of this CreateOnDemandPingProbeDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :return: The targets of this CreateOnDemandPingProbeDetails.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """
        Sets the targets of this CreateOnDemandPingProbeDetails.
        A list of targets (hostnames or IP addresses) of the probe.


        :param targets: The targets of this CreateOnDemandPingProbeDetails.
        :type: list[str]
        """
        self._targets = targets

    @property
    def vantage_point_names(self):
        """
        Gets the vantage_point_names of this CreateOnDemandPingProbeDetails.
        A list of names of vantage points from which to execute the probe.


        :return: The vantage_point_names of this CreateOnDemandPingProbeDetails.
        :rtype: list[str]
        """
        return self._vantage_point_names

    @vantage_point_names.setter
    def vantage_point_names(self, vantage_point_names):
        """
        Sets the vantage_point_names of this CreateOnDemandPingProbeDetails.
        A list of names of vantage points from which to execute the probe.


        :param vantage_point_names: The vantage_point_names of this CreateOnDemandPingProbeDetails.
        :type: list[str]
        """
        self._vantage_point_names = vantage_point_names

    @property
    def port(self):
        """
        Gets the port of this CreateOnDemandPingProbeDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :return: The port of this CreateOnDemandPingProbeDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateOnDemandPingProbeDetails.
        The port on which to probe endpoints. If unspecified, probes will use the
        default port of their protocol.


        :param port: The port of this CreateOnDemandPingProbeDetails.
        :type: int
        """
        self._port = port

    @property
    def timeout_in_seconds(self):
        """
        Gets the timeout_in_seconds of this CreateOnDemandPingProbeDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :return: The timeout_in_seconds of this CreateOnDemandPingProbeDetails.
        :rtype: int
        """
        return self._timeout_in_seconds

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, timeout_in_seconds):
        """
        Sets the timeout_in_seconds of this CreateOnDemandPingProbeDetails.
        The probe timeout in seconds. Valid values: 10, 20, 30, and 60.
        The probe timeout must be less than or equal to `intervalInSeconds` for monitors.


        :param timeout_in_seconds: The timeout_in_seconds of this CreateOnDemandPingProbeDetails.
        :type: int
        """
        self._timeout_in_seconds = timeout_in_seconds

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreateOnDemandPingProbeDetails.
        Allowed values for this property are: "ICMP", "TCP"


        :return: The protocol of this CreateOnDemandPingProbeDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreateOnDemandPingProbeDetails.

        :param protocol: The protocol of this CreateOnDemandPingProbeDetails.
        :type: str
        """
        allowed_values = ["ICMP", "TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            raise ValueError(
                "Invalid value for `protocol`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
