# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParseConnectionDetails(object):
    """
    Parse connections from the connection metadata and oracle wallet file.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParseConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_detail:
            The value to assign to the connection_detail property of this ParseConnectionDetails.
        :type connection_detail: Connection

        :param connection_payload:
            The value to assign to the connection_payload property of this ParseConnectionDetails.
        :type connection_payload: str

        """
        self.swagger_types = {
            'connection_detail': 'Connection',
            'connection_payload': 'str'
        }

        self.attribute_map = {
            'connection_detail': 'connectionDetail',
            'connection_payload': 'connectionPayload'
        }

        self._connection_detail = None
        self._connection_payload = None

    @property
    def connection_detail(self):
        """
        Gets the connection_detail of this ParseConnectionDetails.

        :return: The connection_detail of this ParseConnectionDetails.
        :rtype: Connection
        """
        return self._connection_detail

    @connection_detail.setter
    def connection_detail(self, connection_detail):
        """
        Sets the connection_detail of this ParseConnectionDetails.

        :param connection_detail: The connection_detail of this ParseConnectionDetails.
        :type: Connection
        """
        self._connection_detail = connection_detail

    @property
    def connection_payload(self):
        """
        Gets the connection_payload of this ParseConnectionDetails.
        The information used to parse the connection from the wallet file payload.


        :return: The connection_payload of this ParseConnectionDetails.
        :rtype: str
        """
        return self._connection_payload

    @connection_payload.setter
    def connection_payload(self, connection_payload):
        """
        Sets the connection_payload of this ParseConnectionDetails.
        The information used to parse the connection from the wallet file payload.


        :param connection_payload: The connection_payload of this ParseConnectionDetails.
        :type: str
        """
        self._connection_payload = connection_payload

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
