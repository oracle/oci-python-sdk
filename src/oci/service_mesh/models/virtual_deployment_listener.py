# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualDeploymentListener(object):
    """
    Listener configuration for a virtual deployment.
    """

    #: A constant which can be used with the protocol property of a VirtualDeploymentListener.
    #: This constant has a value of "HTTP"
    PROTOCOL_HTTP = "HTTP"

    #: A constant which can be used with the protocol property of a VirtualDeploymentListener.
    #: This constant has a value of "TLS_PASSTHROUGH"
    PROTOCOL_TLS_PASSTHROUGH = "TLS_PASSTHROUGH"

    #: A constant which can be used with the protocol property of a VirtualDeploymentListener.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a VirtualDeploymentListener.
    #: This constant has a value of "HTTP2"
    PROTOCOL_HTTP2 = "HTTP2"

    #: A constant which can be used with the protocol property of a VirtualDeploymentListener.
    #: This constant has a value of "GRPC"
    PROTOCOL_GRPC = "GRPC"

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualDeploymentListener object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param protocol:
            The value to assign to the protocol property of this VirtualDeploymentListener.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", "HTTP2", "GRPC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param port:
            The value to assign to the port property of this VirtualDeploymentListener.
        :type port: int

        """
        self.swagger_types = {
            'protocol': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'protocol': 'protocol',
            'port': 'port'
        }

        self._protocol = None
        self._port = None

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this VirtualDeploymentListener.
        Type of protocol used in virtual deployment.

        Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", "HTTP2", "GRPC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this VirtualDeploymentListener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this VirtualDeploymentListener.
        Type of protocol used in virtual deployment.


        :param protocol: The protocol of this VirtualDeploymentListener.
        :type: str
        """
        allowed_values = ["HTTP", "TLS_PASSTHROUGH", "TCP", "HTTP2", "GRPC"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def port(self):
        """
        **[Required]** Gets the port of this VirtualDeploymentListener.
        Port in which virtual deployment is running.


        :return: The port of this VirtualDeploymentListener.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this VirtualDeploymentListener.
        Port in which virtual deployment is running.


        :param port: The port of this VirtualDeploymentListener.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
