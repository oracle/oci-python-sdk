# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScimClientCredentials(object):
    """
    The OAuth2 client credentials.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScimClientCredentials object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param client_id:
            The value to assign to the client_id property of this ScimClientCredentials.
        :type client_id: str

        :param client_secret:
            The value to assign to the client_secret property of this ScimClientCredentials.
        :type client_secret: str

        """
        self.swagger_types = {
            'client_id': 'str',
            'client_secret': 'str'
        }

        self.attribute_map = {
            'client_id': 'clientId',
            'client_secret': 'clientSecret'
        }

        self._client_id = None
        self._client_secret = None

    @property
    def client_id(self):
        """
        Gets the client_id of this ScimClientCredentials.
        The client identifier.


        :return: The client_id of this ScimClientCredentials.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this ScimClientCredentials.
        The client identifier.


        :param client_id: The client_id of this ScimClientCredentials.
        :type: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        """
        Gets the client_secret of this ScimClientCredentials.
        The client secret.


        :return: The client_secret of this ScimClientCredentials.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this ScimClientCredentials.
        The client secret.


        :param client_secret: The client_secret of this ScimClientCredentials.
        :type: str
        """
        self._client_secret = client_secret

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
