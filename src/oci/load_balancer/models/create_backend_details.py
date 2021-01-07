# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBackendDetails(object):
    """
    The configuration details for creating a backend server in a backend set.
    For more information on backend server configuration, see
    `Managing Backend Servers`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingbackendservers.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBackendDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ip_address:
            The value to assign to the ip_address property of this CreateBackendDetails.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this CreateBackendDetails.
        :type port: int

        :param weight:
            The value to assign to the weight property of this CreateBackendDetails.
        :type weight: int

        :param backup:
            The value to assign to the backup property of this CreateBackendDetails.
        :type backup: bool

        :param drain:
            The value to assign to the drain property of this CreateBackendDetails.
        :type drain: bool

        :param offline:
            The value to assign to the offline property of this CreateBackendDetails.
        :type offline: bool

        """
        self.swagger_types = {
            'ip_address': 'str',
            'port': 'int',
            'weight': 'int',
            'backup': 'bool',
            'drain': 'bool',
            'offline': 'bool'
        }

        self.attribute_map = {
            'ip_address': 'ipAddress',
            'port': 'port',
            'weight': 'weight',
            'backup': 'backup',
            'drain': 'drain',
            'offline': 'offline'
        }

        self._ip_address = None
        self._port = None
        self._weight = None
        self._backup = None
        self._drain = None
        self._offline = None

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this CreateBackendDetails.
        The IP address of the backend server.

        Example: `10.0.0.3`


        :return: The ip_address of this CreateBackendDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateBackendDetails.
        The IP address of the backend server.

        Example: `10.0.0.3`


        :param ip_address: The ip_address of this CreateBackendDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        **[Required]** Gets the port of this CreateBackendDetails.
        The communication port for the backend server.

        Example: `8080`


        :return: The port of this CreateBackendDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateBackendDetails.
        The communication port for the backend server.

        Example: `8080`


        :param port: The port of this CreateBackendDetails.
        :type: int
        """
        self._port = port

    @property
    def weight(self):
        """
        Gets the weight of this CreateBackendDetails.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
        as a server weighted '1'.
        For more information on load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :return: The weight of this CreateBackendDetails.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this CreateBackendDetails.
        The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
        as a server weighted '1'.
        For more information on load balancing policies, see
        `How Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :param weight: The weight of this CreateBackendDetails.
        :type: int
        """
        self._weight = weight

    @property
    def backup(self):
        """
        Gets the backup of this CreateBackendDetails.
        Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

        **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy.

        Example: `false`


        :return: The backup of this CreateBackendDetails.
        :rtype: bool
        """
        return self._backup

    @backup.setter
    def backup(self, backup):
        """
        Sets the backup of this CreateBackendDetails.
        Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"backup\" fail the health check policy.

        **Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy.

        Example: `false`


        :param backup: The backup of this CreateBackendDetails.
        :type: bool
        """
        self._backup = backup

    @property
    def drain(self):
        """
        Gets the drain of this CreateBackendDetails.
        Whether the load balancer should drain this server. Servers marked \"drain\" receive no new
        incoming traffic.

        Example: `false`


        :return: The drain of this CreateBackendDetails.
        :rtype: bool
        """
        return self._drain

    @drain.setter
    def drain(self, drain):
        """
        Sets the drain of this CreateBackendDetails.
        Whether the load balancer should drain this server. Servers marked \"drain\" receive no new
        incoming traffic.

        Example: `false`


        :param drain: The drain of this CreateBackendDetails.
        :type: bool
        """
        self._drain = drain

    @property
    def offline(self):
        """
        Gets the offline of this CreateBackendDetails.
        Whether the load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :return: The offline of this CreateBackendDetails.
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """
        Sets the offline of this CreateBackendDetails.
        Whether the load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :param offline: The offline of this CreateBackendDetails.
        :type: bool
        """
        self._offline = offline

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
