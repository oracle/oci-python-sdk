# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Scan(object):
    """
    Single Client Access Name (SCAN) is the object with a fully-qualified domain name and a port number.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Scan object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param fqdn:
            The value to assign to the fqdn property of this Scan.
        :type fqdn: str

        :param port:
            The value to assign to the port property of this Scan.
        :type port: str

        """
        self.swagger_types = {
            'fqdn': 'str',
            'port': 'str'
        }

        self.attribute_map = {
            'fqdn': 'fqdn',
            'port': 'port'
        }

        self._fqdn = None
        self._port = None

    @property
    def fqdn(self):
        """
        Gets the fqdn of this Scan.
        A fully-qualified domain name (FQDN).


        :return: The fqdn of this Scan.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this Scan.
        A fully-qualified domain name (FQDN).


        :param fqdn: The fqdn of this Scan.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def port(self):
        """
        Gets the port of this Scan.
        The port number of the FQDN


        :return: The port of this Scan.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this Scan.
        The port number of the FQDN


        :param port: The port of this Scan.
        :type: str
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
