# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalMaster(object):
    """
    An external master name server used as the source of zone data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalMaster object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address:
            The value to assign to the address property of this ExternalMaster.
        :type address: str

        :param port:
            The value to assign to the port property of this ExternalMaster.
        :type port: int

        :param tsig:
            The value to assign to the tsig property of this ExternalMaster.
        :type tsig: TSIG

        """
        self.swagger_types = {
            'address': 'str',
            'port': 'int',
            'tsig': 'TSIG'
        }

        self.attribute_map = {
            'address': 'address',
            'port': 'port',
            'tsig': 'tsig'
        }

        self._address = None
        self._port = None
        self._tsig = None

    @property
    def address(self):
        """
        **[Required]** Gets the address of this ExternalMaster.
        The server's IP address (IPv4 or IPv6).


        :return: The address of this ExternalMaster.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ExternalMaster.
        The server's IP address (IPv4 or IPv6).


        :param address: The address of this ExternalMaster.
        :type: str
        """
        self._address = address

    @property
    def port(self):
        """
        Gets the port of this ExternalMaster.
        The server's port.


        :return: The port of this ExternalMaster.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ExternalMaster.
        The server's port.


        :param port: The port of this ExternalMaster.
        :type: int
        """
        self._port = port

    @property
    def tsig(self):
        """
        Gets the tsig of this ExternalMaster.

        :return: The tsig of this ExternalMaster.
        :rtype: TSIG
        """
        return self._tsig

    @tsig.setter
    def tsig(self, tsig):
        """
        Sets the tsig of this ExternalMaster.

        :param tsig: The tsig of this ExternalMaster.
        :type: TSIG
        """
        self._tsig = tsig

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
