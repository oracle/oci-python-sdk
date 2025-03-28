# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AsmConnectionString(object):
    """
    The ASM instance connection string.
    """

    #: A constant which can be used with the protocol property of a AsmConnectionString.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new AsmConnectionString object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hosts:
            The value to assign to the hosts property of this AsmConnectionString.
        :type hosts: list[str]

        :param port:
            The value to assign to the port property of this AsmConnectionString.
        :type port: int

        :param service:
            The value to assign to the service property of this AsmConnectionString.
        :type service: str

        :param protocol:
            The value to assign to the protocol property of this AsmConnectionString.
            Allowed values for this property are: "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        """
        self.swagger_types = {
            'hosts': 'list[str]',
            'port': 'int',
            'service': 'str',
            'protocol': 'str'
        }
        self.attribute_map = {
            'hosts': 'hosts',
            'port': 'port',
            'service': 'service',
            'protocol': 'protocol'
        }
        self._hosts = None
        self._port = None
        self._service = None
        self._protocol = None

    @property
    def hosts(self):
        """
        **[Required]** Gets the hosts of this AsmConnectionString.
        The list of host names of the ASM instances.


        :return: The hosts of this AsmConnectionString.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this AsmConnectionString.
        The list of host names of the ASM instances.


        :param hosts: The hosts of this AsmConnectionString.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def port(self):
        """
        **[Required]** Gets the port of this AsmConnectionString.
        The port used to connect to the ASM instance.


        :return: The port of this AsmConnectionString.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this AsmConnectionString.
        The port used to connect to the ASM instance.


        :param port: The port of this AsmConnectionString.
        :type: int
        """
        self._port = port

    @property
    def service(self):
        """
        **[Required]** Gets the service of this AsmConnectionString.
        The service name of the ASM instance.


        :return: The service of this AsmConnectionString.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this AsmConnectionString.
        The service name of the ASM instance.


        :param service: The service of this AsmConnectionString.
        :type: str
        """
        self._service = service

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this AsmConnectionString.
        The protocol used to connect to the ASM instance.

        Allowed values for this property are: "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this AsmConnectionString.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this AsmConnectionString.
        The protocol used to connect to the ASM instance.


        :param protocol: The protocol of this AsmConnectionString.
        :type: str
        """
        allowed_values = ["TCP"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
