# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MultipathDevice(object):
    """
    Secondary multipath device, it uses the charUsername and chapSecret from primary volume attachment
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MultipathDevice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ipv4:
            The value to assign to the ipv4 property of this MultipathDevice.
        :type ipv4: str

        :param iqn:
            The value to assign to the iqn property of this MultipathDevice.
        :type iqn: str

        :param port:
            The value to assign to the port property of this MultipathDevice.
        :type port: int

        """
        self.swagger_types = {
            'ipv4': 'str',
            'iqn': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'ipv4': 'ipv4',
            'iqn': 'iqn',
            'port': 'port'
        }

        self._ipv4 = None
        self._iqn = None
        self._port = None

    @property
    def ipv4(self):
        """
        **[Required]** Gets the ipv4 of this MultipathDevice.
        The volume's iSCSI IP address.

        Example: `169.254.2.2`


        :return: The ipv4 of this MultipathDevice.
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """
        Sets the ipv4 of this MultipathDevice.
        The volume's iSCSI IP address.

        Example: `169.254.2.2`


        :param ipv4: The ipv4 of this MultipathDevice.
        :type: str
        """
        self._ipv4 = ipv4

    @property
    def iqn(self):
        """
        **[Required]** Gets the iqn of this MultipathDevice.
        The target volume's iSCSI Qualified Name in the format defined
        by `RFC 3720`__.

        Example: `iqn.2015-12.com.oracleiaas:40b7ee03-883f-46c6-a951-63d2841d2195`

        __ https://tools.ietf.org/html/rfc3720#page-32


        :return: The iqn of this MultipathDevice.
        :rtype: str
        """
        return self._iqn

    @iqn.setter
    def iqn(self, iqn):
        """
        Sets the iqn of this MultipathDevice.
        The target volume's iSCSI Qualified Name in the format defined
        by `RFC 3720`__.

        Example: `iqn.2015-12.com.oracleiaas:40b7ee03-883f-46c6-a951-63d2841d2195`

        __ https://tools.ietf.org/html/rfc3720#page-32


        :param iqn: The iqn of this MultipathDevice.
        :type: str
        """
        self._iqn = iqn

    @property
    def port(self):
        """
        Gets the port of this MultipathDevice.
        The volume's iSCSI port, usually port 860 or 3260.

        Example: `3260`


        :return: The port of this MultipathDevice.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this MultipathDevice.
        The volume's iSCSI port, usually port 860 or 3260.

        Example: `3260`


        :param port: The port of this MultipathDevice.
        :type: int
        """
        self._port = port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
