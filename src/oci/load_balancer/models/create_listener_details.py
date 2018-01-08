# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateListenerDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateListenerDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_backend_set_name:
            The value to assign to the default_backend_set_name property of this CreateListenerDetails.
        :type default_backend_set_name: str

        :param name:
            The value to assign to the name property of this CreateListenerDetails.
        :type name: str

        :param port:
            The value to assign to the port property of this CreateListenerDetails.
        :type port: int

        :param protocol:
            The value to assign to the protocol property of this CreateListenerDetails.
        :type protocol: str

        :param ssl_configuration:
            The value to assign to the ssl_configuration property of this CreateListenerDetails.
        :type ssl_configuration: SSLConfigurationDetails

        """
        self.swagger_types = {
            'default_backend_set_name': 'str',
            'name': 'str',
            'port': 'int',
            'protocol': 'str',
            'ssl_configuration': 'SSLConfigurationDetails'
        }

        self.attribute_map = {
            'default_backend_set_name': 'defaultBackendSetName',
            'name': 'name',
            'port': 'port',
            'protocol': 'protocol',
            'ssl_configuration': 'sslConfiguration'
        }

        self._default_backend_set_name = None
        self._name = None
        self._port = None
        self._protocol = None
        self._ssl_configuration = None

    @property
    def default_backend_set_name(self):
        """
        **[Required]** Gets the default_backend_set_name of this CreateListenerDetails.
        The name of the associated backend set.


        :return: The default_backend_set_name of this CreateListenerDetails.
        :rtype: str
        """
        return self._default_backend_set_name

    @default_backend_set_name.setter
    def default_backend_set_name(self, default_backend_set_name):
        """
        Sets the default_backend_set_name of this CreateListenerDetails.
        The name of the associated backend set.


        :param default_backend_set_name: The default_backend_set_name of this CreateListenerDetails.
        :type: str
        """
        self._default_backend_set_name = default_backend_set_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateListenerDetails.
        A friendly name for the listener. It must be unique and it cannot be changed.
        Avoid entering confidential information.

        Example: `My listener`


        :return: The name of this CreateListenerDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateListenerDetails.
        A friendly name for the listener. It must be unique and it cannot be changed.
        Avoid entering confidential information.

        Example: `My listener`


        :param name: The name of this CreateListenerDetails.
        :type: str
        """
        self._name = name

    @property
    def port(self):
        """
        **[Required]** Gets the port of this CreateListenerDetails.
        The communication port for the listener.

        Example: `80`


        :return: The port of this CreateListenerDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateListenerDetails.
        The communication port for the listener.

        Example: `80`


        :param port: The port of this CreateListenerDetails.
        :type: int
        """
        self._port = port

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this CreateListenerDetails.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :return: The protocol of this CreateListenerDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this CreateListenerDetails.
        The protocol on which the listener accepts connection requests.
        To get a list of valid protocols, use the :func:`list_protocols`
        operation.

        Example: `HTTP`


        :param protocol: The protocol of this CreateListenerDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def ssl_configuration(self):
        """
        Gets the ssl_configuration of this CreateListenerDetails.

        :return: The ssl_configuration of this CreateListenerDetails.
        :rtype: SSLConfigurationDetails
        """
        return self._ssl_configuration

    @ssl_configuration.setter
    def ssl_configuration(self, ssl_configuration):
        """
        Sets the ssl_configuration of this CreateListenerDetails.

        :param ssl_configuration: The ssl_configuration of this CreateListenerDetails.
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
