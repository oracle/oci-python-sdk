# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .application import Application
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TcpApplication(Application):
    """
    TCP Application used on the firewall policy rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TcpApplication object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.TcpApplication.type` attribute
        of this class is ``TCP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this TcpApplication.
        :type type: str

        :param minimum_port:
            The value to assign to the minimum_port property of this TcpApplication.
        :type minimum_port: int

        :param maximum_port:
            The value to assign to the maximum_port property of this TcpApplication.
        :type maximum_port: int

        """
        self.swagger_types = {
            'type': 'str',
            'minimum_port': 'int',
            'maximum_port': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'minimum_port': 'minimumPort',
            'maximum_port': 'maximumPort'
        }

        self._type = None
        self._minimum_port = None
        self._maximum_port = None
        self._type = 'TCP'

    @property
    def minimum_port(self):
        """
        **[Required]** Gets the minimum_port of this TcpApplication.
        The minimum port in the range (inclusive), or the sole port of a single-port range.


        :return: The minimum_port of this TcpApplication.
        :rtype: int
        """
        return self._minimum_port

    @minimum_port.setter
    def minimum_port(self, minimum_port):
        """
        Sets the minimum_port of this TcpApplication.
        The minimum port in the range (inclusive), or the sole port of a single-port range.


        :param minimum_port: The minimum_port of this TcpApplication.
        :type: int
        """
        self._minimum_port = minimum_port

    @property
    def maximum_port(self):
        """
        Gets the maximum_port of this TcpApplication.
        The maximum port in the range (inclusive), which may be absent for a single-port range.


        :return: The maximum_port of this TcpApplication.
        :rtype: int
        """
        return self._maximum_port

    @maximum_port.setter
    def maximum_port(self, maximum_port):
        """
        Sets the maximum_port of this TcpApplication.
        The maximum port in the range (inclusive), which may be absent for a single-port range.


        :param maximum_port: The maximum_port of this TcpApplication.
        :type: int
        """
        self._maximum_port = maximum_port

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
