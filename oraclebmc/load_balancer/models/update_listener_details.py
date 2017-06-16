# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateListenerDetails(object):

    def __init__(self):

        self.swagger_types = {
            'default_backend_set_name': 'str',
            'port': 'int',
            'protocol': 'str',
            'ssl_configuration': 'SSLConfigurationDetails'
        }

        self.attribute_map = {
            'default_backend_set_name': 'defaultBackendSetName',
            'port': 'port',
            'protocol': 'protocol',
            'ssl_configuration': 'sslConfiguration'
        }

        self._default_backend_set_name = None
        self._port = None
        self._protocol = None
        self._ssl_configuration = None

    @property
    def default_backend_set_name(self):
        """
        Gets the default_backend_set_name of this UpdateListenerDetails.
        The name of the associated backend set.


        :return: The default_backend_set_name of this UpdateListenerDetails.
        :rtype: str
        """
        return self._default_backend_set_name

    @default_backend_set_name.setter
    def default_backend_set_name(self, default_backend_set_name):
        """
        Sets the default_backend_set_name of this UpdateListenerDetails.
        The name of the associated backend set.


        :param default_backend_set_name: The default_backend_set_name of this UpdateListenerDetails.
        :type: str
        """
        self._default_backend_set_name = default_backend_set_name

    @property
    def port(self):
        """
        Gets the port of this UpdateListenerDetails.
        The communication port for the listener.

        Example: `80`


        :return: The port of this UpdateListenerDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateListenerDetails.
        The communication port for the listener.

        Example: `80`


        :param port: The port of this UpdateListenerDetails.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this UpdateListenerDetails.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :return: The protocol of this UpdateListenerDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this UpdateListenerDetails.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :param protocol: The protocol of this UpdateListenerDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def ssl_configuration(self):
        """
        Gets the ssl_configuration of this UpdateListenerDetails.

        :return: The ssl_configuration of this UpdateListenerDetails.
        :rtype: SSLConfigurationDetails
        """
        return self._ssl_configuration

    @ssl_configuration.setter
    def ssl_configuration(self, ssl_configuration):
        """
        Sets the ssl_configuration of this UpdateListenerDetails.

        :param ssl_configuration: The ssl_configuration of this UpdateListenerDetails.
        :type: SSLConfigurationDetails
        """
        self._ssl_configuration = ssl_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
