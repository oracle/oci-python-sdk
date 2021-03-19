# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Backend(object):
    """
    The configuration of a backend server that is a member of a network load balancer backend set.
    For more information, see `Managing Backend Servers`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingbackendservers.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Backend object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Backend.
        :type name: str

        :param ip_address:
            The value to assign to the ip_address property of this Backend.
        :type ip_address: str

        :param target_id:
            The value to assign to the target_id property of this Backend.
        :type target_id: str

        :param port:
            The value to assign to the port property of this Backend.
        :type port: int

        :param weight:
            The value to assign to the weight property of this Backend.
        :type weight: int

        :param is_drain:
            The value to assign to the is_drain property of this Backend.
        :type is_drain: bool

        :param is_backup:
            The value to assign to the is_backup property of this Backend.
        :type is_backup: bool

        :param is_offline:
            The value to assign to the is_offline property of this Backend.
        :type is_offline: bool

        """
        self.swagger_types = {
            'name': 'str',
            'ip_address': 'str',
            'target_id': 'str',
            'port': 'int',
            'weight': 'int',
            'is_drain': 'bool',
            'is_backup': 'bool',
            'is_offline': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'ip_address': 'ipAddress',
            'target_id': 'targetId',
            'port': 'port',
            'weight': 'weight',
            'is_drain': 'isDrain',
            'is_backup': 'isBackup',
            'is_offline': 'isOffline'
        }

        self._name = None
        self._ip_address = None
        self._target_id = None
        self._port = None
        self._weight = None
        self._is_drain = None
        self._is_backup = None
        self._is_offline = None

    @property
    def name(self):
        """
        Gets the name of this Backend.
        A read-only field showing the IP address/IP OCID and port that uniquely identify this backend server in the backend set.

        Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:443` or `10.0.0.3:0`


        :return: The name of this Backend.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Backend.
        A read-only field showing the IP address/IP OCID and port that uniquely identify this backend server in the backend set.

        Example: `10.0.0.3:8080`, or `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>:443` or `10.0.0.3:0`


        :param name: The name of this Backend.
        :type: str
        """
        self._name = name

    @property
    def ip_address(self):
        """
        Gets the ip_address of this Backend.
        The IP address of the backend server.
        Example: `10.0.0.3`


        :return: The ip_address of this Backend.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this Backend.
        The IP address of the backend server.
        Example: `10.0.0.3`


        :param ip_address: The ip_address of this Backend.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def target_id(self):
        """
        Gets the target_id of this Backend.
        The IP OCID/Instance OCID associated with the backend server.
        Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`


        :return: The target_id of this Backend.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this Backend.
        The IP OCID/Instance OCID associated with the backend server.
        Example: `ocid1.privateip..oc1.<var>&lt;unique_ID&gt;</var>`


        :param target_id: The target_id of this Backend.
        :type: str
        """
        self._target_id = target_id

    @property
    def port(self):
        """
        **[Required]** Gets the port of this Backend.
        The communication port for the backend server.

        Example: `8080`


        :return: The port of this Backend.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Backend.
        The communication port for the backend server.

        Example: `8080`


        :param port: The port of this Backend.
        :type: int
        """
        self._port = port

    @property
    def weight(self):
        """
        Gets the weight of this Backend.
        The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
        as a server weighted '1'.
        For more information about load balancing policies, see
        `How Network Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :return: The weight of this Backend.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this Backend.
        The network load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
        proportion of incoming traffic. For example, a server weighted '3' receives three times the number of new connections
        as a server weighted '1'.
        For more information about load balancing policies, see
        `How Network Load Balancing Policies Work`__.

        Example: `3`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm


        :param weight: The weight of this Backend.
        :type: int
        """
        self._weight = weight

    @property
    def is_drain(self):
        """
        Gets the is_drain of this Backend.
        Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no
        incoming traffic.

        Example: `false`


        :return: The is_drain of this Backend.
        :rtype: bool
        """
        return self._is_drain

    @is_drain.setter
    def is_drain(self, is_drain):
        """
        Sets the is_drain of this Backend.
        Whether the network load balancer should drain this server. Servers marked \"isDrain\" receive no
        incoming traffic.

        Example: `false`


        :param is_drain: The is_drain of this Backend.
        :type: bool
        """
        self._is_drain = is_drain

    @property
    def is_backup(self):
        """
        Gets the is_backup of this Backend.
        Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy.

        Example: `false`


        :return: The is_backup of this Backend.
        :rtype: bool
        """
        return self._is_backup

    @is_backup.setter
    def is_backup(self, is_backup):
        """
        Sets the is_backup of this Backend.
        Whether the network load balancer should treat this server as a backup unit. If `true`, then the network load balancer forwards no ingress
        traffic to this backend server unless all other backend servers not marked as \"isBackup\" fail the health check policy.

        Example: `false`


        :param is_backup: The is_backup of this Backend.
        :type: bool
        """
        self._is_backup = is_backup

    @property
    def is_offline(self):
        """
        Gets the is_offline of this Backend.
        Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :return: The is_offline of this Backend.
        :rtype: bool
        """
        return self._is_offline

    @is_offline.setter
    def is_offline(self, is_offline):
        """
        Sets the is_offline of this Backend.
        Whether the network load balancer should treat this server as offline. Offline servers receive no incoming
        traffic.

        Example: `false`


        :param is_offline: The is_offline of this Backend.
        :type: bool
        """
        self._is_offline = is_offline

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
