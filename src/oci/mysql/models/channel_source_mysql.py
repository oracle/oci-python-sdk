# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .channel_source import ChannelSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChannelSourceMysql(ChannelSource):
    """
    Core properties of a Mysql Channel source.
    """

    #: A constant which can be used with the ssl_mode property of a ChannelSourceMysql.
    #: This constant has a value of "VERIFY_IDENTITY"
    SSL_MODE_VERIFY_IDENTITY = "VERIFY_IDENTITY"

    #: A constant which can be used with the ssl_mode property of a ChannelSourceMysql.
    #: This constant has a value of "VERIFY_CA"
    SSL_MODE_VERIFY_CA = "VERIFY_CA"

    #: A constant which can be used with the ssl_mode property of a ChannelSourceMysql.
    #: This constant has a value of "REQUIRED"
    SSL_MODE_REQUIRED = "REQUIRED"

    #: A constant which can be used with the ssl_mode property of a ChannelSourceMysql.
    #: This constant has a value of "DISABLED"
    SSL_MODE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new ChannelSourceMysql object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.ChannelSourceMysql.source_type` attribute
        of this class is ``MYSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this ChannelSourceMysql.
            Allowed values for this property are: "MYSQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param hostname:
            The value to assign to the hostname property of this ChannelSourceMysql.
        :type hostname: str

        :param port:
            The value to assign to the port property of this ChannelSourceMysql.
        :type port: int

        :param username:
            The value to assign to the username property of this ChannelSourceMysql.
        :type username: str

        :param ssl_mode:
            The value to assign to the ssl_mode property of this ChannelSourceMysql.
            Allowed values for this property are: "VERIFY_IDENTITY", "VERIFY_CA", "REQUIRED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ssl_mode: str

        :param ssl_ca_certificate:
            The value to assign to the ssl_ca_certificate property of this ChannelSourceMysql.
        :type ssl_ca_certificate: oci.mysql.models.CaCertificate

        """
        self.swagger_types = {
            'source_type': 'str',
            'hostname': 'str',
            'port': 'int',
            'username': 'str',
            'ssl_mode': 'str',
            'ssl_ca_certificate': 'CaCertificate'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'hostname': 'hostname',
            'port': 'port',
            'username': 'username',
            'ssl_mode': 'sslMode',
            'ssl_ca_certificate': 'sslCaCertificate'
        }

        self._source_type = None
        self._hostname = None
        self._port = None
        self._username = None
        self._ssl_mode = None
        self._ssl_ca_certificate = None
        self._source_type = 'MYSQL'

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this ChannelSourceMysql.
        The network address of the MySQL instance.


        :return: The hostname of this ChannelSourceMysql.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this ChannelSourceMysql.
        The network address of the MySQL instance.


        :param hostname: The hostname of this ChannelSourceMysql.
        :type: str
        """
        self._hostname = hostname

    @property
    def port(self):
        """
        **[Required]** Gets the port of this ChannelSourceMysql.
        The port the source MySQL instance listens on.


        :return: The port of this ChannelSourceMysql.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ChannelSourceMysql.
        The port the source MySQL instance listens on.


        :param port: The port of this ChannelSourceMysql.
        :type: int
        """
        self._port = port

    @property
    def username(self):
        """
        **[Required]** Gets the username of this ChannelSourceMysql.
        The name of the replication user on the source MySQL instance.
        The username has a maximum length of 96 characters. For more information,
        please see the `MySQL documentation`__

        __ https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html


        :return: The username of this ChannelSourceMysql.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ChannelSourceMysql.
        The name of the replication user on the source MySQL instance.
        The username has a maximum length of 96 characters. For more information,
        please see the `MySQL documentation`__

        __ https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html


        :param username: The username of this ChannelSourceMysql.
        :type: str
        """
        self._username = username

    @property
    def ssl_mode(self):
        """
        **[Required]** Gets the ssl_mode of this ChannelSourceMysql.
        The SSL mode of the Channel.

        Allowed values for this property are: "VERIFY_IDENTITY", "VERIFY_CA", "REQUIRED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ssl_mode of this ChannelSourceMysql.
        :rtype: str
        """
        return self._ssl_mode

    @ssl_mode.setter
    def ssl_mode(self, ssl_mode):
        """
        Sets the ssl_mode of this ChannelSourceMysql.
        The SSL mode of the Channel.


        :param ssl_mode: The ssl_mode of this ChannelSourceMysql.
        :type: str
        """
        allowed_values = ["VERIFY_IDENTITY", "VERIFY_CA", "REQUIRED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(ssl_mode, allowed_values):
            ssl_mode = 'UNKNOWN_ENUM_VALUE'
        self._ssl_mode = ssl_mode

    @property
    def ssl_ca_certificate(self):
        """
        Gets the ssl_ca_certificate of this ChannelSourceMysql.

        :return: The ssl_ca_certificate of this ChannelSourceMysql.
        :rtype: oci.mysql.models.CaCertificate
        """
        return self._ssl_ca_certificate

    @ssl_ca_certificate.setter
    def ssl_ca_certificate(self, ssl_ca_certificate):
        """
        Sets the ssl_ca_certificate of this ChannelSourceMysql.

        :param ssl_ca_certificate: The ssl_ca_certificate of this ChannelSourceMysql.
        :type: oci.mysql.models.CaCertificate
        """
        self._ssl_ca_certificate = ssl_ca_certificate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
