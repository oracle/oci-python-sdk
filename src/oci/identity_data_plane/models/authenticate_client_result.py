# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticateClientResult(object):
    """
    AuthenticateClientResult model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticateClientResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param principal:
            The value to assign to the principal property of this AuthenticateClientResult.
        :type principal: oci.identity_data_plane.models.Principal

        :param error_message:
            The value to assign to the error_message property of this AuthenticateClientResult.
        :type error_message: str

        """
        self.swagger_types = {
            'principal': 'Principal',
            'error_message': 'str'
        }

        self.attribute_map = {
            'principal': 'principal',
            'error_message': 'errorMessage'
        }

        self._principal = None
        self._error_message = None

    @property
    def principal(self):
        """
        Gets the principal of this AuthenticateClientResult.
        The original caller's resolved principal object if the authentication succeeds, null otherwise.


        :return: The principal of this AuthenticateClientResult.
        :rtype: oci.identity_data_plane.models.Principal
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """
        Sets the principal of this AuthenticateClientResult.
        The original caller's resolved principal object if the authentication succeeds, null otherwise.


        :param principal: The principal of this AuthenticateClientResult.
        :type: oci.identity_data_plane.models.Principal
        """
        self._principal = principal

    @property
    def error_message(self):
        """
        Gets the error_message of this AuthenticateClientResult.
        If the authentication fails for the original caller (not failing authentication of the calling service, in which case we return 401), we return a 200, but with null principal and an error message


        :return: The error_message of this AuthenticateClientResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this AuthenticateClientResult.
        If the authentication fails for the original caller (not failing authentication of the calling service, in which case we return 401), we return a 200, but with null principal and an error message


        :param error_message: The error_message of this AuthenticateClientResult.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
