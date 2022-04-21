# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressGatewayHost(object):
    """
    Host for the ingress listener.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IngressGatewayHost object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this IngressGatewayHost.
        :type name: str

        :param hostnames:
            The value to assign to the hostnames property of this IngressGatewayHost.
        :type hostnames: list[str]

        :param listeners:
            The value to assign to the listeners property of this IngressGatewayHost.
        :type listeners: list[oci.service_mesh.models.IngressGatewayListener]

        """
        self.swagger_types = {
            'name': 'str',
            'hostnames': 'list[str]',
            'listeners': 'list[IngressGatewayListener]'
        }

        self.attribute_map = {
            'name': 'name',
            'hostnames': 'hostnames',
            'listeners': 'listeners'
        }

        self._name = None
        self._hostnames = None
        self._listeners = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this IngressGatewayHost.
        A user-friendly name for the host. The name must be unique within the same ingress gateway.
        This name can be used in the ingress gateway route table resource to attach a route to this host.

        Example: `MyExampleHost`


        :return: The name of this IngressGatewayHost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IngressGatewayHost.
        A user-friendly name for the host. The name must be unique within the same ingress gateway.
        This name can be used in the ingress gateway route table resource to attach a route to this host.

        Example: `MyExampleHost`


        :param name: The name of this IngressGatewayHost.
        :type: str
        """
        self._name = name

    @property
    def hostnames(self):
        """
        Gets the hostnames of this IngressGatewayHost.
        Hostnames of the host. Applicable only for HTTP and TLS_PASSTHROUGH listeners.
        Wildcard hostnames are supported in the prefix form.
        Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\".


        :return: The hostnames of this IngressGatewayHost.
        :rtype: list[str]
        """
        return self._hostnames

    @hostnames.setter
    def hostnames(self, hostnames):
        """
        Sets the hostnames of this IngressGatewayHost.
        Hostnames of the host. Applicable only for HTTP and TLS_PASSTHROUGH listeners.
        Wildcard hostnames are supported in the prefix form.
        Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\".


        :param hostnames: The hostnames of this IngressGatewayHost.
        :type: list[str]
        """
        self._hostnames = hostnames

    @property
    def listeners(self):
        """
        **[Required]** Gets the listeners of this IngressGatewayHost.
        The listeners for the ingress gateway.


        :return: The listeners of this IngressGatewayHost.
        :rtype: list[oci.service_mesh.models.IngressGatewayListener]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """
        Sets the listeners of this IngressGatewayHost.
        The listeners for the ingress gateway.


        :param listeners: The listeners of this IngressGatewayHost.
        :type: list[oci.service_mesh.models.IngressGatewayListener]
        """
        self._listeners = listeners

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
