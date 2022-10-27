# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KafkaBootstrapServer(object):
    """
    Represents a Kafka bootstrap server with host name, optional port defaults to 9092, and an optional private ip.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KafkaBootstrapServer object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host:
            The value to assign to the host property of this KafkaBootstrapServer.
        :type host: str

        :param port:
            The value to assign to the port property of this KafkaBootstrapServer.
        :type port: int

        :param private_ip:
            The value to assign to the private_ip property of this KafkaBootstrapServer.
        :type private_ip: str

        """
        self.swagger_types = {
            'host': 'str',
            'port': 'int',
            'private_ip': 'str'
        }

        self.attribute_map = {
            'host': 'host',
            'port': 'port',
            'private_ip': 'privateIp'
        }

        self._host = None
        self._port = None
        self._private_ip = None

    @property
    def host(self):
        """
        **[Required]** Gets the host of this KafkaBootstrapServer.
        The name or address of a host.


        :return: The host of this KafkaBootstrapServer.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this KafkaBootstrapServer.
        The name or address of a host.


        :param host: The host of this KafkaBootstrapServer.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this KafkaBootstrapServer.
        The port of an endpoint usually specified for a connection.


        :return: The port of this KafkaBootstrapServer.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this KafkaBootstrapServer.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this KafkaBootstrapServer.
        :type: int
        """
        self._port = port

    @property
    def private_ip(self):
        """
        Gets the private_ip of this KafkaBootstrapServer.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this KafkaBootstrapServer.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this KafkaBootstrapServer.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this KafkaBootstrapServer.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
