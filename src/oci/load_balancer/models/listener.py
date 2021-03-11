# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Listener(object):
    """
    The listener's configuration.
    For more information on backend set configuration, see
    `Managing Load Balancer Listeners`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managinglisteners.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Listener object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Listener.
        :type name: str

        :param default_backend_set_name:
            The value to assign to the default_backend_set_name property of this Listener.
        :type default_backend_set_name: str

        :param port:
            The value to assign to the port property of this Listener.
        :type port: int

        :param protocol:
            The value to assign to the protocol property of this Listener.
        :type protocol: str

        :param hostname_names:
            The value to assign to the hostname_names property of this Listener.
        :type hostname_names: list[str]

        :param path_route_set_name:
            The value to assign to the path_route_set_name property of this Listener.
        :type path_route_set_name: str

        :param ssl_configuration:
            The value to assign to the ssl_configuration property of this Listener.
        :type ssl_configuration: oci.load_balancer.models.SSLConfiguration

        :param connection_configuration:
            The value to assign to the connection_configuration property of this Listener.
        :type connection_configuration: oci.load_balancer.models.ConnectionConfiguration

        :param rule_set_names:
            The value to assign to the rule_set_names property of this Listener.
        :type rule_set_names: list[str]

        :param routing_policy_name:
            The value to assign to the routing_policy_name property of this Listener.
        :type routing_policy_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'default_backend_set_name': 'str',
            'port': 'int',
            'protocol': 'str',
            'hostname_names': 'list[str]',
            'path_route_set_name': 'str',
            'ssl_configuration': 'SSLConfiguration',
            'connection_configuration': 'ConnectionConfiguration',
            'rule_set_names': 'list[str]',
            'routing_policy_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'default_backend_set_name': 'defaultBackendSetName',
            'port': 'port',
            'protocol': 'protocol',
            'hostname_names': 'hostnameNames',
            'path_route_set_name': 'pathRouteSetName',
            'ssl_configuration': 'sslConfiguration',
            'connection_configuration': 'connectionConfiguration',
            'rule_set_names': 'ruleSetNames',
            'routing_policy_name': 'routingPolicyName'
        }

        self._name = None
        self._default_backend_set_name = None
        self._port = None
        self._protocol = None
        self._hostname_names = None
        self._path_route_set_name = None
        self._ssl_configuration = None
        self._connection_configuration = None
        self._rule_set_names = None
        self._routing_policy_name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Listener.
        A friendly name for the listener. It must be unique and it cannot be changed.

        Example: `example_listener`


        :return: The name of this Listener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Listener.
        A friendly name for the listener. It must be unique and it cannot be changed.

        Example: `example_listener`


        :param name: The name of this Listener.
        :type: str
        """
        self._name = name

    @property
    def default_backend_set_name(self):
        """
        **[Required]** Gets the default_backend_set_name of this Listener.
        The name of the associated backend set.

        Example: `example_backend_set`


        :return: The default_backend_set_name of this Listener.
        :rtype: str
        """
        return self._default_backend_set_name

    @default_backend_set_name.setter
    def default_backend_set_name(self, default_backend_set_name):
        """
        Sets the default_backend_set_name of this Listener.
        The name of the associated backend set.

        Example: `example_backend_set`


        :param default_backend_set_name: The default_backend_set_name of this Listener.
        :type: str
        """
        self._default_backend_set_name = default_backend_set_name

    @property
    def port(self):
        """
        **[Required]** Gets the port of this Listener.
        The communication port for the listener.

        Example: `80`


        :return: The port of this Listener.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Listener.
        The communication port for the listener.

        Example: `80`


        :param port: The port of this Listener.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this Listener.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :return: The protocol of this Listener.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this Listener.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :param protocol: The protocol of this Listener.
        :type: str
        """
        self._protocol = protocol

    @property
    def hostname_names(self):
        """
        Gets the hostname_names of this Listener.
        An array of hostname resource names.


        :return: The hostname_names of this Listener.
        :rtype: list[str]
        """
        return self._hostname_names

    @hostname_names.setter
    def hostname_names(self, hostname_names):
        """
        Sets the hostname_names of this Listener.
        An array of hostname resource names.


        :param hostname_names: The hostname_names of this Listener.
        :type: list[str]
        """
        self._hostname_names = hostname_names

    @property
    def path_route_set_name(self):
        """
        Gets the path_route_set_name of this Listener.
        Deprecated. Please use `routingPolicies` instead.

        The name of the set of path-based routing rules, :class:`PathRouteSet`,
        applied to this listener's traffic.

        Example: `example_path_route_set`


        :return: The path_route_set_name of this Listener.
        :rtype: str
        """
        return self._path_route_set_name

    @path_route_set_name.setter
    def path_route_set_name(self, path_route_set_name):
        """
        Sets the path_route_set_name of this Listener.
        Deprecated. Please use `routingPolicies` instead.

        The name of the set of path-based routing rules, :class:`PathRouteSet`,
        applied to this listener's traffic.

        Example: `example_path_route_set`


        :param path_route_set_name: The path_route_set_name of this Listener.
        :type: str
        """
        self._path_route_set_name = path_route_set_name

    @property
    def ssl_configuration(self):
        """
        Gets the ssl_configuration of this Listener.

        :return: The ssl_configuration of this Listener.
        :rtype: oci.load_balancer.models.SSLConfiguration
        """
        return self._ssl_configuration

    @ssl_configuration.setter
    def ssl_configuration(self, ssl_configuration):
        """
        Sets the ssl_configuration of this Listener.

        :param ssl_configuration: The ssl_configuration of this Listener.
        :type: oci.load_balancer.models.SSLConfiguration
        """
        self._ssl_configuration = ssl_configuration

    @property
    def connection_configuration(self):
        """
        Gets the connection_configuration of this Listener.

        :return: The connection_configuration of this Listener.
        :rtype: oci.load_balancer.models.ConnectionConfiguration
        """
        return self._connection_configuration

    @connection_configuration.setter
    def connection_configuration(self, connection_configuration):
        """
        Sets the connection_configuration of this Listener.

        :param connection_configuration: The connection_configuration of this Listener.
        :type: oci.load_balancer.models.ConnectionConfiguration
        """
        self._connection_configuration = connection_configuration

    @property
    def rule_set_names(self):
        """
        Gets the rule_set_names of this Listener.
        The names of the :class:`RuleSet` to apply to the listener.

        Example: [\"example_rule_set\"]


        :return: The rule_set_names of this Listener.
        :rtype: list[str]
        """
        return self._rule_set_names

    @rule_set_names.setter
    def rule_set_names(self, rule_set_names):
        """
        Sets the rule_set_names of this Listener.
        The names of the :class:`RuleSet` to apply to the listener.

        Example: [\"example_rule_set\"]


        :param rule_set_names: The rule_set_names of this Listener.
        :type: list[str]
        """
        self._rule_set_names = rule_set_names

    @property
    def routing_policy_name(self):
        """
        Gets the routing_policy_name of this Listener.
        The name of the routing policy applied to this listener's traffic.

        Example: `example_routing_policy_name`


        :return: The routing_policy_name of this Listener.
        :rtype: str
        """
        return self._routing_policy_name

    @routing_policy_name.setter
    def routing_policy_name(self, routing_policy_name):
        """
        Sets the routing_policy_name of this Listener.
        The name of the routing policy applied to this listener's traffic.

        Example: `example_routing_policy_name`


        :param routing_policy_name: The routing_policy_name of this Listener.
        :type: str
        """
        self._routing_policy_name = routing_policy_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
