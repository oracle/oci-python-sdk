# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemEndpoint(object):
    """
    A particular functional endpoint for access to a DB System, and the properties that apply to it.
    """

    #: A constant which can be used with the modes property of a DbSystemEndpoint.
    #: This constant has a value of "READ"
    MODES_READ = "READ"

    #: A constant which can be used with the modes property of a DbSystemEndpoint.
    #: This constant has a value of "WRITE"
    MODES_WRITE = "WRITE"

    #: A constant which can be used with the status property of a DbSystemEndpoint.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a DbSystemEndpoint.
    #: This constant has a value of "INACTIVE"
    STATUS_INACTIVE = "INACTIVE"

    #: A constant which can be used with the status property of a DbSystemEndpoint.
    #: This constant has a value of "UPDATING"
    STATUS_UPDATING = "UPDATING"

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this DbSystemEndpoint.
        :type hostname: str

        :param ip_address:
            The value to assign to the ip_address property of this DbSystemEndpoint.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this DbSystemEndpoint.
        :type port: int

        :param port_x:
            The value to assign to the port_x property of this DbSystemEndpoint.
        :type port_x: int

        :param modes:
            The value to assign to the modes property of this DbSystemEndpoint.
            Allowed values for items in this list are: "READ", "WRITE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type modes: list[str]

        :param status:
            The value to assign to the status property of this DbSystemEndpoint.
            Allowed values for this property are: "ACTIVE", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_details:
            The value to assign to the status_details property of this DbSystemEndpoint.
        :type status_details: str

        """
        self.swagger_types = {
            'hostname': 'str',
            'ip_address': 'str',
            'port': 'int',
            'port_x': 'int',
            'modes': 'list[str]',
            'status': 'str',
            'status_details': 'str'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'ip_address': 'ipAddress',
            'port': 'port',
            'port_x': 'portX',
            'modes': 'modes',
            'status': 'status',
            'status_details': 'statusDetails'
        }

        self._hostname = None
        self._ip_address = None
        self._port = None
        self._port_x = None
        self._modes = None
        self._status = None
        self._status_details = None

    @property
    def hostname(self):
        """
        Gets the hostname of this DbSystemEndpoint.
        The network address of the DB System.


        :return: The hostname of this DbSystemEndpoint.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DbSystemEndpoint.
        The network address of the DB System.


        :param hostname: The hostname of this DbSystemEndpoint.
        :type: str
        """
        self._hostname = hostname

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this DbSystemEndpoint.
        The IP address the DB System is configured to listen on.


        :return: The ip_address of this DbSystemEndpoint.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this DbSystemEndpoint.
        The IP address the DB System is configured to listen on.


        :param ip_address: The ip_address of this DbSystemEndpoint.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        **[Required]** Gets the port of this DbSystemEndpoint.
        The port the MySQL instance listens on.


        :return: The port of this DbSystemEndpoint.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this DbSystemEndpoint.
        The port the MySQL instance listens on.


        :param port: The port of this DbSystemEndpoint.
        :type: int
        """
        self._port = port

    @property
    def port_x(self):
        """
        **[Required]** Gets the port_x of this DbSystemEndpoint.
        The network port where to connect to use this endpoint using the X protocol.


        :return: The port_x of this DbSystemEndpoint.
        :rtype: int
        """
        return self._port_x

    @port_x.setter
    def port_x(self, port_x):
        """
        Sets the port_x of this DbSystemEndpoint.
        The network port where to connect to use this endpoint using the X protocol.


        :param port_x: The port_x of this DbSystemEndpoint.
        :type: int
        """
        self._port_x = port_x

    @property
    def modes(self):
        """
        Gets the modes of this DbSystemEndpoint.
        The access modes from the client that this endpoint supports.

        Allowed values for items in this list are: "READ", "WRITE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The modes of this DbSystemEndpoint.
        :rtype: list[str]
        """
        return self._modes

    @modes.setter
    def modes(self, modes):
        """
        Sets the modes of this DbSystemEndpoint.
        The access modes from the client that this endpoint supports.


        :param modes: The modes of this DbSystemEndpoint.
        :type: list[str]
        """
        allowed_values = ["READ", "WRITE"]
        if modes:
            modes[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in modes]
        self._modes = modes

    @property
    def status(self):
        """
        Gets the status of this DbSystemEndpoint.
        The state of the endpoints, as far as it can seen from the DB System.
        There may be some inconsistency with the actual state of the MySQL service.

        Allowed values for this property are: "ACTIVE", "INACTIVE", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DbSystemEndpoint.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DbSystemEndpoint.
        The state of the endpoints, as far as it can seen from the DB System.
        There may be some inconsistency with the actual state of the MySQL service.


        :param status: The status of this DbSystemEndpoint.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_details(self):
        """
        Gets the status_details of this DbSystemEndpoint.
        Additional information about the current endpoint status.


        :return: The status_details of this DbSystemEndpoint.
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """
        Sets the status_details of this DbSystemEndpoint.
        Additional information about the current endpoint status.


        :param status_details: The status_details of this DbSystemEndpoint.
        :type: str
        """
        self._status_details = status_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
