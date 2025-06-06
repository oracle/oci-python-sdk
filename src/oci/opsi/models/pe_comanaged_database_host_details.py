# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeComanagedDatabaseHostDetails(object):
    """
    Input Host Details used for connection requests for private endpoint accessed db resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PeComanagedDatabaseHostDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_ip:
            The value to assign to the host_ip property of this PeComanagedDatabaseHostDetails.
        :type host_ip: str

        :param port:
            The value to assign to the port property of this PeComanagedDatabaseHostDetails.
        :type port: int

        """
        self.swagger_types = {
            'host_ip': 'str',
            'port': 'int'
        }
        self.attribute_map = {
            'host_ip': 'hostIp',
            'port': 'port'
        }
        self._host_ip = None
        self._port = None

    @property
    def host_ip(self):
        """
        Gets the host_ip of this PeComanagedDatabaseHostDetails.
        Host IP used for connection requests for Cloud DB resource.


        :return: The host_ip of this PeComanagedDatabaseHostDetails.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """
        Sets the host_ip of this PeComanagedDatabaseHostDetails.
        Host IP used for connection requests for Cloud DB resource.


        :param host_ip: The host_ip of this PeComanagedDatabaseHostDetails.
        :type: str
        """
        self._host_ip = host_ip

    @property
    def port(self):
        """
        Gets the port of this PeComanagedDatabaseHostDetails.
        Listener port number used for connection requests for rivate endpoint accessed db resource.


        :return: The port of this PeComanagedDatabaseHostDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this PeComanagedDatabaseHostDetails.
        Listener port number used for connection requests for rivate endpoint accessed db resource.


        :param port: The port of this PeComanagedDatabaseHostDetails.
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
