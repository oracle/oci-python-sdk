# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionConfiguration(object):
    """
    Configuration details for the connection between the client and backend servers.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param idle_timeout:
            The value to assign to the idle_timeout property of this ConnectionConfiguration.
        :type idle_timeout: int

        :param backend_tcp_proxy_protocol_version:
            The value to assign to the backend_tcp_proxy_protocol_version property of this ConnectionConfiguration.
        :type backend_tcp_proxy_protocol_version: int

        """
        self.swagger_types = {
            'idle_timeout': 'int',
            'backend_tcp_proxy_protocol_version': 'int'
        }

        self.attribute_map = {
            'idle_timeout': 'idleTimeout',
            'backend_tcp_proxy_protocol_version': 'backendTcpProxyProtocolVersion'
        }

        self._idle_timeout = None
        self._backend_tcp_proxy_protocol_version = None

    @property
    def idle_timeout(self):
        """
        **[Required]** Gets the idle_timeout of this ConnectionConfiguration.
        The maximum idle time, in seconds, allowed between two successive receive or two successive send operations
        between the client and backend servers. A send operation does not reset the timer for receive operations. A
        receive operation does not reset the timer for send operations.

        For more information, see `Connection Configuration`__.

        Example: `1200`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration


        :return: The idle_timeout of this ConnectionConfiguration.
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """
        Sets the idle_timeout of this ConnectionConfiguration.
        The maximum idle time, in seconds, allowed between two successive receive or two successive send operations
        between the client and backend servers. A send operation does not reset the timer for receive operations. A
        receive operation does not reset the timer for send operations.

        For more information, see `Connection Configuration`__.

        Example: `1200`

        __ https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration


        :param idle_timeout: The idle_timeout of this ConnectionConfiguration.
        :type: int
        """
        self._idle_timeout = idle_timeout

    @property
    def backend_tcp_proxy_protocol_version(self):
        """
        Gets the backend_tcp_proxy_protocol_version of this ConnectionConfiguration.
        The backend TCP Proxy Protocol version.

        Example: `1`


        :return: The backend_tcp_proxy_protocol_version of this ConnectionConfiguration.
        :rtype: int
        """
        return self._backend_tcp_proxy_protocol_version

    @backend_tcp_proxy_protocol_version.setter
    def backend_tcp_proxy_protocol_version(self, backend_tcp_proxy_protocol_version):
        """
        Sets the backend_tcp_proxy_protocol_version of this ConnectionConfiguration.
        The backend TCP Proxy Protocol version.

        Example: `1`


        :param backend_tcp_proxy_protocol_version: The backend_tcp_proxy_protocol_version of this ConnectionConfiguration.
        :type: int
        """
        self._backend_tcp_proxy_protocol_version = backend_tcp_proxy_protocol_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
