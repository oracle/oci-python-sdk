# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ListenerDetails(object):
    """
    The listener's configuration details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ListenerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_backend_set_name:
            The value to assign to the default_backend_set_name property of this ListenerDetails.
        :type default_backend_set_name: str

        :param port:
            The value to assign to the port property of this ListenerDetails.
        :type port: int

        :param protocol:
            The value to assign to the protocol property of this ListenerDetails.
        :type protocol: str

        :param hostname_names:
            The value to assign to the hostname_names property of this ListenerDetails.
        :type hostname_names: list[str]

        :param path_route_set_name:
            The value to assign to the path_route_set_name property of this ListenerDetails.
        :type path_route_set_name: str

        :param ssl_configuration:
            The value to assign to the ssl_configuration property of this ListenerDetails.
        :type ssl_configuration: oci.load_balancer.models.SSLConfigurationDetails

        :param connection_configuration:
            The value to assign to the connection_configuration property of this ListenerDetails.
        :type connection_configuration: oci.load_balancer.models.ConnectionConfiguration

        :param rule_set_names:
            The value to assign to the rule_set_names property of this ListenerDetails.
        :type rule_set_names: list[str]

        """
        self.swagger_types = {
            'default_backend_set_name': 'str',
            'port': 'int',
            'protocol': 'str',
            'hostname_names': 'list[str]',
            'path_route_set_name': 'str',
            'ssl_configuration': 'SSLConfigurationDetails',
            'connection_configuration': 'ConnectionConfiguration',
            'rule_set_names': 'list[str]'
        }

        self.attribute_map = {
            'default_backend_set_name': 'defaultBackendSetName',
            'port': 'port',
            'protocol': 'protocol',
            'hostname_names': 'hostnameNames',
            'path_route_set_name': 'pathRouteSetName',
            'ssl_configuration': 'sslConfiguration',
            'connection_configuration': 'connectionConfiguration',
            'rule_set_names': 'ruleSetNames'
        }

        self._default_backend_set_name = None
        self._port = None
        self._protocol = None
        self._hostname_names = None
        self._path_route_set_name = None
        self._ssl_configuration = None
        self._connection_configuration = None
        self._rule_set_names = None

    @property
    def default_backend_set_name(self):
        """
        **[Required]** Gets the default_backend_set_name of this ListenerDetails.
        The name of the associated backend set.

        Example: `example_backend_set`


        :return: The default_backend_set_name of this ListenerDetails.
        :rtype: str
        """
        return self._default_backend_set_name

    @default_backend_set_name.setter
    def default_backend_set_name(self, default_backend_set_name):
        """
        Sets the default_backend_set_name of this ListenerDetails.
        The name of the associated backend set.

        Example: `example_backend_set`


        :param default_backend_set_name: The default_backend_set_name of this ListenerDetails.
        :type: str
        """
        self._default_backend_set_name = default_backend_set_name

    @property
    def port(self):
        """
        **[Required]** Gets the port of this ListenerDetails.
        The communication port for the listener.

        Example: `80`


        :return: The port of this ListenerDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ListenerDetails.
        The communication port for the listener.

        Example: `80`


        :param port: The port of this ListenerDetails.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this ListenerDetails.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :return: The protocol of this ListenerDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this ListenerDetails.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :param protocol: The protocol of this ListenerDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def hostname_names(self):
        """
        Gets the hostname_names of this ListenerDetails.
        An array of hostname resource names.


        :return: The hostname_names of this ListenerDetails.
        :rtype: list[str]
        """
        return self._hostname_names

    @hostname_names.setter
    def hostname_names(self, hostname_names):
        """
        Sets the hostname_names of this ListenerDetails.
        An array of hostname resource names.


        :param hostname_names: The hostname_names of this ListenerDetails.
        :type: list[str]
        """
        self._hostname_names = hostname_names

    @property
    def path_route_set_name(self):
        """
        Gets the path_route_set_name of this ListenerDetails.
        The name of the set of path-based routing rules, :class:`PathRouteSet`,
        applied to this listener's traffic.

        Example: `example_path_route_set`


        :return: The path_route_set_name of this ListenerDetails.
        :rtype: str
        """
        return self._path_route_set_name

    @path_route_set_name.setter
    def path_route_set_name(self, path_route_set_name):
        """
        Sets the path_route_set_name of this ListenerDetails.
        The name of the set of path-based routing rules, :class:`PathRouteSet`,
        applied to this listener's traffic.

        Example: `example_path_route_set`


        :param path_route_set_name: The path_route_set_name of this ListenerDetails.
        :type: str
        """
        self._path_route_set_name = path_route_set_name

    @property
    def ssl_configuration(self):
        """
        Gets the ssl_configuration of this ListenerDetails.

        :return: The ssl_configuration of this ListenerDetails.
        :rtype: oci.load_balancer.models.SSLConfigurationDetails
        """
        return self._ssl_configuration

    @ssl_configuration.setter
    def ssl_configuration(self, ssl_configuration):
        """
        Sets the ssl_configuration of this ListenerDetails.

        :param ssl_configuration: The ssl_configuration of this ListenerDetails.
        :type: oci.load_balancer.models.SSLConfigurationDetails
        """
        self._ssl_configuration = ssl_configuration

    @property
    def connection_configuration(self):
        """
        Gets the connection_configuration of this ListenerDetails.

        :return: The connection_configuration of this ListenerDetails.
        :rtype: oci.load_balancer.models.ConnectionConfiguration
        """
        return self._connection_configuration

    @connection_configuration.setter
    def connection_configuration(self, connection_configuration):
        """
        Sets the connection_configuration of this ListenerDetails.

        :param connection_configuration: The connection_configuration of this ListenerDetails.
        :type: oci.load_balancer.models.ConnectionConfiguration
        """
        self._connection_configuration = connection_configuration

    @property
    def rule_set_names(self):
        """
        Gets the rule_set_names of this ListenerDetails.
        The names of the :class:`RuleSet` to apply to the listener.

         Example: [\"example_rule_set\"]


        :return: The rule_set_names of this ListenerDetails.
        :rtype: list[str]
        """
        return self._rule_set_names

    @rule_set_names.setter
    def rule_set_names(self, rule_set_names):
        """
        Sets the rule_set_names of this ListenerDetails.
        The names of the :class:`RuleSet` to apply to the listener.

         Example: [\"example_rule_set\"]


        :param rule_set_names: The rule_set_names of this ListenerDetails.
        :type: list[str]
        """
        self._rule_set_names = rule_set_names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
