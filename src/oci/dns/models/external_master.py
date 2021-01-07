# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalMaster(object):
    """
    An external master name server used as the source of zone data.
    May either have a zone-embedded TSIG or reference a TSIG key by OCID,
    but not both.
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
        :type tsig: oci.dns.models.TSIG

        :param tsig_key_id:
            The value to assign to the tsig_key_id property of this ExternalMaster.
        :type tsig_key_id: str

        """
        self.swagger_types = {
            'address': 'str',
            'port': 'int',
            'tsig': 'TSIG',
            'tsig_key_id': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'port': 'port',
            'tsig': 'tsig',
            'tsig_key_id': 'tsigKeyId'
        }

        self._address = None
        self._port = None
        self._tsig = None
        self._tsig_key_id = None

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
        The server's port. Port value must be a value of 53, otherwise omit
        the port value.


        :return: The port of this ExternalMaster.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ExternalMaster.
        The server's port. Port value must be a value of 53, otherwise omit
        the port value.


        :param port: The port of this ExternalMaster.
        :type: int
        """
        self._port = port

    @property
    def tsig(self):
        """
        Gets the tsig of this ExternalMaster.

        :return: The tsig of this ExternalMaster.
        :rtype: oci.dns.models.TSIG
        """
        return self._tsig

    @tsig.setter
    def tsig(self, tsig):
        """
        Sets the tsig of this ExternalMaster.

        :param tsig: The tsig of this ExternalMaster.
        :type: oci.dns.models.TSIG
        """
        self._tsig = tsig

    @property
    def tsig_key_id(self):
        """
        Gets the tsig_key_id of this ExternalMaster.
        The OCID of the TSIG key.


        :return: The tsig_key_id of this ExternalMaster.
        :rtype: str
        """
        return self._tsig_key_id

    @tsig_key_id.setter
    def tsig_key_id(self, tsig_key_id):
        """
        Sets the tsig_key_id of this ExternalMaster.
        The OCID of the TSIG key.


        :param tsig_key_id: The tsig_key_id of this ExternalMaster.
        :type: str
        """
        self._tsig_key_id = tsig_key_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
