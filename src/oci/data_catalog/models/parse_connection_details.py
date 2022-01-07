# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParseConnectionDetails(object):
    """
    Parse connections from the connection metadata and Oracle wallet file.
    An error will be returned if more than one of connectionPayload, walletSecretId or walletSecretName are present in the request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParseConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_detail:
            The value to assign to the connection_detail property of this ParseConnectionDetails.
        :type connection_detail: oci.data_catalog.models.Connection

        :param connection_payload:
            The value to assign to the connection_payload property of this ParseConnectionDetails.
        :type connection_payload: str

        :param wallet_secret_id:
            The value to assign to the wallet_secret_id property of this ParseConnectionDetails.
        :type wallet_secret_id: str

        :param wallet_secret_name:
            The value to assign to the wallet_secret_name property of this ParseConnectionDetails.
        :type wallet_secret_name: str

        """
        self.swagger_types = {
            'connection_detail': 'Connection',
            'connection_payload': 'str',
            'wallet_secret_id': 'str',
            'wallet_secret_name': 'str'
        }

        self.attribute_map = {
            'connection_detail': 'connectionDetail',
            'connection_payload': 'connectionPayload',
            'wallet_secret_id': 'walletSecretId',
            'wallet_secret_name': 'walletSecretName'
        }

        self._connection_detail = None
        self._connection_payload = None
        self._wallet_secret_id = None
        self._wallet_secret_name = None

    @property
    def connection_detail(self):
        """
        Gets the connection_detail of this ParseConnectionDetails.

        :return: The connection_detail of this ParseConnectionDetails.
        :rtype: oci.data_catalog.models.Connection
        """
        return self._connection_detail

    @connection_detail.setter
    def connection_detail(self, connection_detail):
        """
        Sets the connection_detail of this ParseConnectionDetails.

        :param connection_detail: The connection_detail of this ParseConnectionDetails.
        :type: oci.data_catalog.models.Connection
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

    @property
    def wallet_secret_id(self):
        """
        Gets the wallet_secret_id of this ParseConnectionDetails.
        OCID of the OCI Vault secret holding the Oracle wallet to parse.


        :return: The wallet_secret_id of this ParseConnectionDetails.
        :rtype: str
        """
        return self._wallet_secret_id

    @wallet_secret_id.setter
    def wallet_secret_id(self, wallet_secret_id):
        """
        Sets the wallet_secret_id of this ParseConnectionDetails.
        OCID of the OCI Vault secret holding the Oracle wallet to parse.


        :param wallet_secret_id: The wallet_secret_id of this ParseConnectionDetails.
        :type: str
        """
        self._wallet_secret_id = wallet_secret_id

    @property
    def wallet_secret_name(self):
        """
        Gets the wallet_secret_name of this ParseConnectionDetails.
        Name of the OCI Vault secret holding the Oracle wallet to parse.


        :return: The wallet_secret_name of this ParseConnectionDetails.
        :rtype: str
        """
        return self._wallet_secret_name

    @wallet_secret_name.setter
    def wallet_secret_name(self, wallet_secret_name):
        """
        Sets the wallet_secret_name of this ParseConnectionDetails.
        Name of the OCI Vault secret holding the Oracle wallet to parse.


        :param wallet_secret_name: The wallet_secret_name of this ParseConnectionDetails.
        :type: str
        """
        self._wallet_secret_name = wallet_secret_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
