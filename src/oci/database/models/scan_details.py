# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScanDetails(object):
    """
    The Single Client Access Name (SCAN) details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this ScanDetails.
        :type hostname: str

        :param port:
            The value to assign to the port property of this ScanDetails.
        :type port: int

        :param ips:
            The value to assign to the ips property of this ScanDetails.
        :type ips: list[str]

        """
        self.swagger_types = {
            'hostname': 'str',
            'port': 'int',
            'ips': 'list[str]'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'port': 'port',
            'ips': 'ips'
        }

        self._hostname = None
        self._port = None
        self._ips = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this ScanDetails.
        The SCAN hostname.


        :return: The hostname of this ScanDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this ScanDetails.
        The SCAN hostname.


        :param hostname: The hostname of this ScanDetails.
        :type: str
        """
        self._hostname = hostname

    @property
    def port(self):
        """
        **[Required]** Gets the port of this ScanDetails.
        The SCAN port. Default is 1521.


        :return: The port of this ScanDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this ScanDetails.
        The SCAN port. Default is 1521.


        :param port: The port of this ScanDetails.
        :type: int
        """
        self._port = port

    @property
    def ips(self):
        """
        **[Required]** Gets the ips of this ScanDetails.
        The list of SCAN IP addresses. Three addresses should be provided.


        :return: The ips of this ScanDetails.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """
        Sets the ips of this ScanDetails.
        The list of SCAN IP addresses. Three addresses should be provided.


        :param ips: The ips of this ScanDetails.
        :type: list[str]
        """
        self._ips = ips

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
