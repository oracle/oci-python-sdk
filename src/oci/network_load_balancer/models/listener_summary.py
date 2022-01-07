# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListenerSummary(object):
    """
    The configuration of the listener.
    For more information about backend set configuration, see
    `Managing Load Balancer Listeners`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managinglisteners.htm
    """

    #: A constant which can be used with the protocol property of a ListenerSummary.
    #: This constant has a value of "ANY"
    PROTOCOL_ANY = "ANY"

    #: A constant which can be used with the protocol property of a ListenerSummary.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a ListenerSummary.
    #: This constant has a value of "UDP"
    PROTOCOL_UDP = "UDP"

    #: A constant which can be used with the protocol property of a ListenerSummary.
    #: This constant has a value of "TCP_AND_UDP"
    PROTOCOL_TCP_AND_UDP = "TCP_AND_UDP"

    #: A constant which can be used with the ip_version property of a ListenerSummary.
    #: This constant has a value of "IPV4"
    IP_VERSION_IPV4 = "IPV4"

    #: A constant which can be used with the ip_version property of a ListenerSummary.
    #: This constant has a value of "IPV6"
    IP_VERSION_IPV6 = "IPV6"

    def __init__(self, **kwargs):
        """
        Initializes a new ListenerSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ListenerSummary.
        :type name: str

        :param default_backend_set_name:
            The value to assign to the default_backend_set_name property of this ListenerSummary.
        :type default_backend_set_name: str

        :param port:
            The value to assign to the port property of this ListenerSummary.
        :type port: int

        :param protocol:
            The value to assign to the protocol property of this ListenerSummary.
            Allowed values for this property are: "ANY", "TCP", "UDP", "TCP_AND_UDP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param ip_version:
            The value to assign to the ip_version property of this ListenerSummary.
            Allowed values for this property are: "IPV4", "IPV6", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ip_version: str

        """
        self.swagger_types = {
            'name': 'str',
            'default_backend_set_name': 'str',
            'port': 'int',
            'protocol': 'str',
            'ip_version': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'default_backend_set_name': 'defaultBackendSetName',
            'port': 'port',
            'protocol': 'protocol',
            'ip_version': 'ipVersion'
        }

        self._name = None
        self._default_backend_set_name = None
        self._port = None
        self._protocol = None
        self._ip_version = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ListenerSummary.
        A friendly name for the listener. It must be unique and it cannot be changed.

        Example: `example_listener`


        :return: The name of this ListenerSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ListenerSummary.
        A friendly name for the listener. It must be unique and it cannot be changed.

        Example: `example_listener`


        :param name: The name of this ListenerSummary.
        :type: str
        """
        self._name = name

    @property
    def default_backend_set_name(self):
        """
        **[Required]** Gets the default_backend_set_name of this ListenerSummary.
        The name of the associated backend set.

        Example: `example_backend_set`


        :return: The default_backend_set_name of this ListenerSummary.
        :rtype: str
        """
        return self._default_backend_set_name

    @default_backend_set_name.setter
    def default_backend_set_name(self, default_backend_set_name):
        """
        Sets the default_backend_set_name of this ListenerSummary.
        The name of the associated backend set.

        Example: `example_backend_set`


        :param default_backend_set_name: The default_backend_set_name of this ListenerSummary.
        :type: str
        """
        self._default_backend_set_name = default_backend_set_name

    @property
    def port(self):
        """
        **[Required]** Gets the port of this ListenerSummary.
        The communication port for the listener.

        Example: `80`


        :return: The port of this ListenerSummary.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ListenerSummary.
        The communication port for the listener.

        Example: `80`


        :param port: The port of this ListenerSummary.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this ListenerSummary.
        The protocol on which the listener accepts connection requests.
        For public network load balancers, ANY protocol refers to TCP/UDP.
        For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true).
        To get a list of valid protocols, use the :func:`list_network_load_balancers_protocols`
        operation.

        Example: `TCP`

        Allowed values for this property are: "ANY", "TCP", "UDP", "TCP_AND_UDP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this ListenerSummary.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this ListenerSummary.
        The protocol on which the listener accepts connection requests.
        For public network load balancers, ANY protocol refers to TCP/UDP.
        For private network load balancers, ANY protocol refers to TCP/UDP/ICMP (note that ICMP requires isPreserveSourceDestination to be set to true).
        To get a list of valid protocols, use the :func:`list_network_load_balancers_protocols`
        operation.

        Example: `TCP`


        :param protocol: The protocol of this ListenerSummary.
        :type: str
        """
        allowed_values = ["ANY", "TCP", "UDP", "TCP_AND_UDP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def ip_version(self):
        """
        Gets the ip_version of this ListenerSummary.
        IP version associated with the listener.

        Allowed values for this property are: "IPV4", "IPV6", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ip_version of this ListenerSummary.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """
        Sets the ip_version of this ListenerSummary.
        IP version associated with the listener.


        :param ip_version: The ip_version of this ListenerSummary.
        :type: str
        """
        allowed_values = ["IPV4", "IPV6"]
        if not value_allowed_none_or_none_sentinel(ip_version, allowed_values):
            ip_version = 'UNKNOWN_ENUM_VALUE'
        self._ip_version = ip_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
