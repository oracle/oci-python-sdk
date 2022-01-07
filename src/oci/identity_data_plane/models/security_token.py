# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecurityToken(object):
    """
    SecurityToken model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecurityToken object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param token:
            The value to assign to the token property of this SecurityToken.
        :type token: str

        """
        self.swagger_types = {
            'token': 'str'
        }

        self.attribute_map = {
            'token': 'token'
        }

        self._token = None

    @property
    def token(self):
        """
        **[Required]** Gets the token of this SecurityToken.
        The security token, signed by auth service


        :return: The token of this SecurityToken.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this SecurityToken.
        The security token, signed by auth service


        :param token: The token of this SecurityToken.
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
