# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConnectionStringProfile(object):
    """
    The connection string profile to allow clients to group, filter and select connection string values based on structured metadata.
    """

    #: A constant which can be used with the consumer_group property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "HIGH"
    CONSUMER_GROUP_HIGH = "HIGH"

    #: A constant which can be used with the consumer_group property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "MEDIUM"
    CONSUMER_GROUP_MEDIUM = "MEDIUM"

    #: A constant which can be used with the consumer_group property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "LOW"
    CONSUMER_GROUP_LOW = "LOW"

    #: A constant which can be used with the consumer_group property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "TP"
    CONSUMER_GROUP_TP = "TP"

    #: A constant which can be used with the consumer_group property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "TPURGENT"
    CONSUMER_GROUP_TPURGENT = "TPURGENT"

    #: A constant which can be used with the protocol property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "TCPS"
    PROTOCOL_TCPS = "TCPS"

    #: A constant which can be used with the tls_authentication property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "SERVER"
    TLS_AUTHENTICATION_SERVER = "SERVER"

    #: A constant which can be used with the tls_authentication property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "MUTUAL"
    TLS_AUTHENTICATION_MUTUAL = "MUTUAL"

    #: A constant which can be used with the host_format property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "FQDN"
    HOST_FORMAT_FQDN = "FQDN"

    #: A constant which can be used with the host_format property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "IP"
    HOST_FORMAT_IP = "IP"

    #: A constant which can be used with the session_mode property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "DIRECT"
    SESSION_MODE_DIRECT = "DIRECT"

    #: A constant which can be used with the session_mode property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "REDIRECT"
    SESSION_MODE_REDIRECT = "REDIRECT"

    #: A constant which can be used with the syntax_format property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "LONG"
    SYNTAX_FORMAT_LONG = "LONG"

    #: A constant which can be used with the syntax_format property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "EZCONNECT"
    SYNTAX_FORMAT_EZCONNECT = "EZCONNECT"

    #: A constant which can be used with the syntax_format property of a DatabaseConnectionStringProfile.
    #: This constant has a value of "EZCONNECTPLUS"
    SYNTAX_FORMAT_EZCONNECTPLUS = "EZCONNECTPLUS"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConnectionStringProfile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this DatabaseConnectionStringProfile.
        :type display_name: str

        :param value:
            The value to assign to the value property of this DatabaseConnectionStringProfile.
        :type value: str

        :param consumer_group:
            The value to assign to the consumer_group property of this DatabaseConnectionStringProfile.
            Allowed values for this property are: "HIGH", "MEDIUM", "LOW", "TP", "TPURGENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type consumer_group: str

        :param protocol:
            The value to assign to the protocol property of this DatabaseConnectionStringProfile.
            Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        :param tls_authentication:
            The value to assign to the tls_authentication property of this DatabaseConnectionStringProfile.
            Allowed values for this property are: "SERVER", "MUTUAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type tls_authentication: str

        :param host_format:
            The value to assign to the host_format property of this DatabaseConnectionStringProfile.
            Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type host_format: str

        :param session_mode:
            The value to assign to the session_mode property of this DatabaseConnectionStringProfile.
            Allowed values for this property are: "DIRECT", "REDIRECT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type session_mode: str

        :param syntax_format:
            The value to assign to the syntax_format property of this DatabaseConnectionStringProfile.
            Allowed values for this property are: "LONG", "EZCONNECT", "EZCONNECTPLUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type syntax_format: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'value': 'str',
            'consumer_group': 'str',
            'protocol': 'str',
            'tls_authentication': 'str',
            'host_format': 'str',
            'session_mode': 'str',
            'syntax_format': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'value': 'value',
            'consumer_group': 'consumerGroup',
            'protocol': 'protocol',
            'tls_authentication': 'tlsAuthentication',
            'host_format': 'hostFormat',
            'session_mode': 'sessionMode',
            'syntax_format': 'syntaxFormat'
        }

        self._display_name = None
        self._value = None
        self._consumer_group = None
        self._protocol = None
        self._tls_authentication = None
        self._host_format = None
        self._session_mode = None
        self._syntax_format = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DatabaseConnectionStringProfile.
        A user-friendly name for the connection.


        :return: The display_name of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DatabaseConnectionStringProfile.
        A user-friendly name for the connection.


        :param display_name: The display_name of this DatabaseConnectionStringProfile.
        :type: str
        """
        self._display_name = display_name

    @property
    def value(self):
        """
        **[Required]** Gets the value of this DatabaseConnectionStringProfile.
        Connection string value.


        :return: The value of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DatabaseConnectionStringProfile.
        Connection string value.


        :param value: The value of this DatabaseConnectionStringProfile.
        :type: str
        """
        self._value = value

    @property
    def consumer_group(self):
        """
        Gets the consumer_group of this DatabaseConnectionStringProfile.
        Consumer group used by the connection.

        Allowed values for this property are: "HIGH", "MEDIUM", "LOW", "TP", "TPURGENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The consumer_group of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._consumer_group

    @consumer_group.setter
    def consumer_group(self, consumer_group):
        """
        Sets the consumer_group of this DatabaseConnectionStringProfile.
        Consumer group used by the connection.


        :param consumer_group: The consumer_group of this DatabaseConnectionStringProfile.
        :type: str
        """
        allowed_values = ["HIGH", "MEDIUM", "LOW", "TP", "TPURGENT"]
        if not value_allowed_none_or_none_sentinel(consumer_group, allowed_values):
            consumer_group = 'UNKNOWN_ENUM_VALUE'
        self._consumer_group = consumer_group

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this DatabaseConnectionStringProfile.
        Protocol used by the connection.

        Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this DatabaseConnectionStringProfile.
        Protocol used by the connection.


        :param protocol: The protocol of this DatabaseConnectionStringProfile.
        :type: str
        """
        allowed_values = ["TCP", "TCPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    @property
    def tls_authentication(self):
        """
        Gets the tls_authentication of this DatabaseConnectionStringProfile.
        Specifies whether the TLS handshake is using one-way (`SERVER`) or mutual (`MUTUAL`) authentication.

        Allowed values for this property are: "SERVER", "MUTUAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The tls_authentication of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._tls_authentication

    @tls_authentication.setter
    def tls_authentication(self, tls_authentication):
        """
        Sets the tls_authentication of this DatabaseConnectionStringProfile.
        Specifies whether the TLS handshake is using one-way (`SERVER`) or mutual (`MUTUAL`) authentication.


        :param tls_authentication: The tls_authentication of this DatabaseConnectionStringProfile.
        :type: str
        """
        allowed_values = ["SERVER", "MUTUAL"]
        if not value_allowed_none_or_none_sentinel(tls_authentication, allowed_values):
            tls_authentication = 'UNKNOWN_ENUM_VALUE'
        self._tls_authentication = tls_authentication

    @property
    def host_format(self):
        """
        **[Required]** Gets the host_format of this DatabaseConnectionStringProfile.
        Host format used in connection string.

        Allowed values for this property are: "FQDN", "IP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The host_format of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._host_format

    @host_format.setter
    def host_format(self, host_format):
        """
        Sets the host_format of this DatabaseConnectionStringProfile.
        Host format used in connection string.


        :param host_format: The host_format of this DatabaseConnectionStringProfile.
        :type: str
        """
        allowed_values = ["FQDN", "IP"]
        if not value_allowed_none_or_none_sentinel(host_format, allowed_values):
            host_format = 'UNKNOWN_ENUM_VALUE'
        self._host_format = host_format

    @property
    def session_mode(self):
        """
        **[Required]** Gets the session_mode of this DatabaseConnectionStringProfile.
        Specifies whether the listener performs a direct hand-off of the session, or redirects the session. In RAC deployments where SCAN is used, sessions are redirected to a Node VIP. Use `DIRECT` for direct hand-offs. Use `REDIRECT` to redirect the session.

        Allowed values for this property are: "DIRECT", "REDIRECT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The session_mode of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._session_mode

    @session_mode.setter
    def session_mode(self, session_mode):
        """
        Sets the session_mode of this DatabaseConnectionStringProfile.
        Specifies whether the listener performs a direct hand-off of the session, or redirects the session. In RAC deployments where SCAN is used, sessions are redirected to a Node VIP. Use `DIRECT` for direct hand-offs. Use `REDIRECT` to redirect the session.


        :param session_mode: The session_mode of this DatabaseConnectionStringProfile.
        :type: str
        """
        allowed_values = ["DIRECT", "REDIRECT"]
        if not value_allowed_none_or_none_sentinel(session_mode, allowed_values):
            session_mode = 'UNKNOWN_ENUM_VALUE'
        self._session_mode = session_mode

    @property
    def syntax_format(self):
        """
        **[Required]** Gets the syntax_format of this DatabaseConnectionStringProfile.
        Specifies whether the connection string is using the long (`LONG`), Easy Connect (`EZCONNECT`), or Easy Connect Plus (`EZCONNECTPLUS`) format.
        Autonomous Databases on shared Exadata infrastructure always use the long format.

        Allowed values for this property are: "LONG", "EZCONNECT", "EZCONNECTPLUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The syntax_format of this DatabaseConnectionStringProfile.
        :rtype: str
        """
        return self._syntax_format

    @syntax_format.setter
    def syntax_format(self, syntax_format):
        """
        Sets the syntax_format of this DatabaseConnectionStringProfile.
        Specifies whether the connection string is using the long (`LONG`), Easy Connect (`EZCONNECT`), or Easy Connect Plus (`EZCONNECTPLUS`) format.
        Autonomous Databases on shared Exadata infrastructure always use the long format.


        :param syntax_format: The syntax_format of this DatabaseConnectionStringProfile.
        :type: str
        """
        allowed_values = ["LONG", "EZCONNECT", "EZCONNECTPLUS"]
        if not value_allowed_none_or_none_sentinel(syntax_format, allowed_values):
            syntax_format = 'UNKNOWN_ENUM_VALUE'
        self._syntax_format = syntax_format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
