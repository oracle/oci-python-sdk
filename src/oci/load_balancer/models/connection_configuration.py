# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectionConfiguration(object):

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectionConfiguration object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param idle_timeout:
            The value to assign to the idle_timeout property of this ConnectionConfiguration.
        :type idle_timeout: int

        """
        self.swagger_types = {
            'idle_timeout': 'int'
        }

        self.attribute_map = {
            'idle_timeout': 'idleTimeout'
        }

        self._idle_timeout = None

    @property
    def idle_timeout(self):
        """
        **[Required]** Gets the idle_timeout of this ConnectionConfiguration.
        The maximum idle time, in seconds, allowed between two successive receive or two successive send operations
        between the client and backend servers. A send operation does not reset the timer for receive operations. A
        receive operation does not reset the timer for send operations.

        The default values are:

        *  300 seconds for TCP

        *  60 seconds for HTTP and WebSocket protocols.

        Note: The protocol is set at the listener.

        Modify this parameter if the client or backend server stops transmitting data for more than the default time.
        Some examples include:

        *  The client sends a database query to the backend server and the database takes over 300 seconds to execute.
           Therefore, the backend server does not transmit any data within 300 seconds.

        *  The client uploads data using the HTTP protocol. During the upload, the backend does not transmit any data
           to the client for more than 60 seconds.

        *  The client downloads data using the HTTP protocol.  After the initial request, it stops transmitting data to
           the backend server for more than 60 seconds.

        *  The client starts transmitting data after establishing a WebSocket connection, but the backend server does
           not transmit data for more than 60 seconds.

        *  The backend server starts transmitting data after establishing a WebSocket connection, but the client does
           not transmit data for more than 60 seconds.

        The maximum value is 7200 seconds. Contact My Oracle Support to file a service request if you want to increase
        this limit for your tenancy. For more information, see `Service Limits`__.

        Example: `1200`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/servicelimits.htm


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

        The default values are:

        *  300 seconds for TCP

        *  60 seconds for HTTP and WebSocket protocols.

        Note: The protocol is set at the listener.

        Modify this parameter if the client or backend server stops transmitting data for more than the default time.
        Some examples include:

        *  The client sends a database query to the backend server and the database takes over 300 seconds to execute.
           Therefore, the backend server does not transmit any data within 300 seconds.

        *  The client uploads data using the HTTP protocol. During the upload, the backend does not transmit any data
           to the client for more than 60 seconds.

        *  The client downloads data using the HTTP protocol.  After the initial request, it stops transmitting data to
           the backend server for more than 60 seconds.

        *  The client starts transmitting data after establishing a WebSocket connection, but the backend server does
           not transmit data for more than 60 seconds.

        *  The backend server starts transmitting data after establishing a WebSocket connection, but the client does
           not transmit data for more than 60 seconds.

        The maximum value is 7200 seconds. Contact My Oracle Support to file a service request if you want to increase
        this limit for your tenancy. For more information, see `Service Limits`__.

        Example: `1200`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/servicelimits.htm


        :param idle_timeout: The idle_timeout of this ConnectionConfiguration.
        :type: int
        """
        self._idle_timeout = idle_timeout

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
