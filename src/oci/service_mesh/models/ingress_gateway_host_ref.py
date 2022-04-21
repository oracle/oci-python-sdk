# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressGatewayHostRef(object):
    """
    The ingress gateway host to which the route rule attaches. If not specified, the route rule gets attached to all hosts on the ingress gateway.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IngressGatewayHostRef object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this IngressGatewayHostRef.
        :type name: str

        :param port:
            The value to assign to the port property of this IngressGatewayHostRef.
        :type port: int

        """
        self.swagger_types = {
            'name': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'port': 'port'
        }

        self._name = None
        self._port = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this IngressGatewayHostRef.
        Name of the ingress gateway host that this route should apply to.


        :return: The name of this IngressGatewayHostRef.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IngressGatewayHostRef.
        Name of the ingress gateway host that this route should apply to.


        :param name: The name of this IngressGatewayHostRef.
        :type: str
        """
        self._name = name

    @property
    def port(self):
        """
        Gets the port of this IngressGatewayHostRef.
        The port of the ingress gateway host listener. Leave empty to match all ports for the host.


        :return: The port of this IngressGatewayHostRef.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this IngressGatewayHostRef.
        The port of the ingress gateway host listener. Leave empty to match all ports for the host.


        :param port: The port of this IngressGatewayHostRef.
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
