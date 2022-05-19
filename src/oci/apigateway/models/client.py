# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Client(object):
    """
    A Client.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Client object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Client.
        :type name: str

        :param token:
            The value to assign to the token property of this Client.
        :type token: str

        """
        self.swagger_types = {
            'name': 'str',
            'token': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'token': 'token'
        }

        self._name = None
        self._token = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Client.
        The name of the client. Must be unique within a subscriber.


        :return: The name of this Client.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Client.
        The name of the client. Must be unique within a subscriber.


        :param name: The name of this Client.
        :type: str
        """
        self._name = name

    @property
    def token(self):
        """
        **[Required]** Gets the token of this Client.
        The token for the client. Must be unique within a tenancy.


        :return: The token of this Client.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this Client.
        The token for the client. Must be unique within a tenancy.


        :param token: The token of this Client.
        :type: str
        """
        self._token = token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
