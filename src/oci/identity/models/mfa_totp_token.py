# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MfaTotpToken(object):
    """
    Totp token for MFA
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MfaTotpToken object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param totp_token:
            The value to assign to the totp_token property of this MfaTotpToken.
        :type totp_token: str

        """
        self.swagger_types = {
            'totp_token': 'str'
        }

        self.attribute_map = {
            'totp_token': 'totpToken'
        }

        self._totp_token = None

    @property
    def totp_token(self):
        """
        Gets the totp_token of this MfaTotpToken.
        The Totp token for MFA.


        :return: The totp_token of this MfaTotpToken.
        :rtype: str
        """
        return self._totp_token

    @totp_token.setter
    def totp_token(self, totp_token):
        """
        Sets the totp_token of this MfaTotpToken.
        The Totp token for MFA.


        :param totp_token: The totp_token of this MfaTotpToken.
        :type: str
        """
        self._totp_token = totp_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
