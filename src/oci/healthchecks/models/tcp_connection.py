# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TcpConnection(object):
    """
    TCP connection results.  All durations are in milliseconds.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TcpConnection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address:
            The value to assign to the address property of this TcpConnection.
        :type address: str

        :param port:
            The value to assign to the port property of this TcpConnection.
        :type port: int

        :param connect_duration:
            The value to assign to the connect_duration property of this TcpConnection.
        :type connect_duration: float

        :param secure_connect_duration:
            The value to assign to the secure_connect_duration property of this TcpConnection.
        :type secure_connect_duration: float

        """
        self.swagger_types = {
            'address': 'str',
            'port': 'int',
            'connect_duration': 'float',
            'secure_connect_duration': 'float'
        }

        self.attribute_map = {
            'address': 'address',
            'port': 'port',
            'connect_duration': 'connectDuration',
            'secure_connect_duration': 'secureConnectDuration'
        }

        self._address = None
        self._port = None
        self._connect_duration = None
        self._secure_connect_duration = None

    @property
    def address(self):
        """
        Gets the address of this TcpConnection.
        The connection IP address.


        :return: The address of this TcpConnection.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this TcpConnection.
        The connection IP address.


        :param address: The address of this TcpConnection.
        :type: str
        """
        self._address = address

    @property
    def port(self):
        """
        Gets the port of this TcpConnection.
        The port.


        :return: The port of this TcpConnection.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this TcpConnection.
        The port.


        :param port: The port of this TcpConnection.
        :type: int
        """
        self._port = port

    @property
    def connect_duration(self):
        """
        Gets the connect_duration of this TcpConnection.
        Total connect duration, calculated using `connectEnd` minus `connectStart`.


        :return: The connect_duration of this TcpConnection.
        :rtype: float
        """
        return self._connect_duration

    @connect_duration.setter
    def connect_duration(self, connect_duration):
        """
        Sets the connect_duration of this TcpConnection.
        Total connect duration, calculated using `connectEnd` minus `connectStart`.


        :param connect_duration: The connect_duration of this TcpConnection.
        :type: float
        """
        self._connect_duration = connect_duration

    @property
    def secure_connect_duration(self):
        """
        Gets the secure_connect_duration of this TcpConnection.
        The duration to secure the connection.  This value will be zero for
        insecure connections.  Calculated using `connectEnd` minus `secureConnectionStart`.


        :return: The secure_connect_duration of this TcpConnection.
        :rtype: float
        """
        return self._secure_connect_duration

    @secure_connect_duration.setter
    def secure_connect_duration(self, secure_connect_duration):
        """
        Sets the secure_connect_duration of this TcpConnection.
        The duration to secure the connection.  This value will be zero for
        insecure connections.  Calculated using `connectEnd` minus `secureConnectionStart`.


        :param secure_connect_duration: The secure_connect_duration of this TcpConnection.
        :type: float
        """
        self._secure_connect_duration = secure_connect_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
