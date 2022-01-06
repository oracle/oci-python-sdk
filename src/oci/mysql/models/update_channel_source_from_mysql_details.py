# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_channel_source_details import UpdateChannelSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateChannelSourceFromMysqlDetails(UpdateChannelSourceDetails):
    """
    Parameters detailing how to provision the source endpoint that is a MySQL Server.
    Typically a MySQL Server that is not managed by the MySQL Database Service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateChannelSourceFromMysqlDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.UpdateChannelSourceFromMysqlDetails.source_type` attribute
        of this class is ``MYSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this UpdateChannelSourceFromMysqlDetails.
        :type source_type: str

        :param hostname:
            The value to assign to the hostname property of this UpdateChannelSourceFromMysqlDetails.
        :type hostname: str

        :param port:
            The value to assign to the port property of this UpdateChannelSourceFromMysqlDetails.
        :type port: int

        :param username:
            The value to assign to the username property of this UpdateChannelSourceFromMysqlDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this UpdateChannelSourceFromMysqlDetails.
        :type password: str

        :param ssl_mode:
            The value to assign to the ssl_mode property of this UpdateChannelSourceFromMysqlDetails.
        :type ssl_mode: str

        :param ssl_ca_certificate:
            The value to assign to the ssl_ca_certificate property of this UpdateChannelSourceFromMysqlDetails.
        :type ssl_ca_certificate: oci.mysql.models.CaCertificate

        """
        self.swagger_types = {
            'source_type': 'str',
            'hostname': 'str',
            'port': 'int',
            'username': 'str',
            'password': 'str',
            'ssl_mode': 'str',
            'ssl_ca_certificate': 'CaCertificate'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'hostname': 'hostname',
            'port': 'port',
            'username': 'username',
            'password': 'password',
            'ssl_mode': 'sslMode',
            'ssl_ca_certificate': 'sslCaCertificate'
        }

        self._source_type = None
        self._hostname = None
        self._port = None
        self._username = None
        self._password = None
        self._ssl_mode = None
        self._ssl_ca_certificate = None
        self._source_type = 'MYSQL'

    @property
    def hostname(self):
        """
        Gets the hostname of this UpdateChannelSourceFromMysqlDetails.
        The network address of the MySQL instance.


        :return: The hostname of this UpdateChannelSourceFromMysqlDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this UpdateChannelSourceFromMysqlDetails.
        The network address of the MySQL instance.


        :param hostname: The hostname of this UpdateChannelSourceFromMysqlDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def port(self):
        """
        Gets the port of this UpdateChannelSourceFromMysqlDetails.
        The port the source MySQL instance listens on.


        :return: The port of this UpdateChannelSourceFromMysqlDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateChannelSourceFromMysqlDetails.
        The port the source MySQL instance listens on.


        :param port: The port of this UpdateChannelSourceFromMysqlDetails.
        :type: int
        """
        self._port = port

    @property
    def username(self):
        """
        Gets the username of this UpdateChannelSourceFromMysqlDetails.
        The name of the replication user on the source MySQL instance.
        The username has a maximum length of 96 characters. For more information,
        please see the `MySQL documentation`__

        __ https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html


        :return: The username of this UpdateChannelSourceFromMysqlDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UpdateChannelSourceFromMysqlDetails.
        The name of the replication user on the source MySQL instance.
        The username has a maximum length of 96 characters. For more information,
        please see the `MySQL documentation`__

        __ https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html


        :param username: The username of this UpdateChannelSourceFromMysqlDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        Gets the password of this UpdateChannelSourceFromMysqlDetails.
        The password for the replication user. The password must be
        between 8 and 32 characters long, and must contain at least 1
        numeric character, 1 lowercase character, 1 uppercase character,
        and 1 special (nonalphanumeric) character.


        :return: The password of this UpdateChannelSourceFromMysqlDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateChannelSourceFromMysqlDetails.
        The password for the replication user. The password must be
        between 8 and 32 characters long, and must contain at least 1
        numeric character, 1 lowercase character, 1 uppercase character,
        and 1 special (nonalphanumeric) character.


        :param password: The password of this UpdateChannelSourceFromMysqlDetails.
        :type: str
        """
        self._password = password

    @property
    def ssl_mode(self):
        """
        Gets the ssl_mode of this UpdateChannelSourceFromMysqlDetails.
        The SSL mode of the Channel.


        :return: The ssl_mode of this UpdateChannelSourceFromMysqlDetails.
        :rtype: str
        """
        return self._ssl_mode

    @ssl_mode.setter
    def ssl_mode(self, ssl_mode):
        """
        Sets the ssl_mode of this UpdateChannelSourceFromMysqlDetails.
        The SSL mode of the Channel.


        :param ssl_mode: The ssl_mode of this UpdateChannelSourceFromMysqlDetails.
        :type: str
        """
        self._ssl_mode = ssl_mode

    @property
    def ssl_ca_certificate(self):
        """
        Gets the ssl_ca_certificate of this UpdateChannelSourceFromMysqlDetails.

        :return: The ssl_ca_certificate of this UpdateChannelSourceFromMysqlDetails.
        :rtype: oci.mysql.models.CaCertificate
        """
        return self._ssl_ca_certificate

    @ssl_ca_certificate.setter
    def ssl_ca_certificate(self, ssl_ca_certificate):
        """
        Sets the ssl_ca_certificate of this UpdateChannelSourceFromMysqlDetails.

        :param ssl_ca_certificate: The ssl_ca_certificate of this UpdateChannelSourceFromMysqlDetails.
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
