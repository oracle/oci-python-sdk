# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseConsoleTokenDetails(object):
    """
    The token that allows the OCI Console to access the Autonomous Database Service Console.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseConsoleTokenDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param token:
            The value to assign to the token property of this AutonomousDatabaseConsoleTokenDetails.
        :type token: str

        :param login_url:
            The value to assign to the login_url property of this AutonomousDatabaseConsoleTokenDetails.
        :type login_url: str

        """
        self.swagger_types = {
            'token': 'str',
            'login_url': 'str'
        }

        self.attribute_map = {
            'token': 'token',
            'login_url': 'loginUrl'
        }

        self._token = None
        self._login_url = None

    @property
    def token(self):
        """
        Gets the token of this AutonomousDatabaseConsoleTokenDetails.
        The token that allows the OCI Console to access the Autonomous Transaction Processing Service Console.


        :return: The token of this AutonomousDatabaseConsoleTokenDetails.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this AutonomousDatabaseConsoleTokenDetails.
        The token that allows the OCI Console to access the Autonomous Transaction Processing Service Console.


        :param token: The token of this AutonomousDatabaseConsoleTokenDetails.
        :type: str
        """
        self._token = token

    @property
    def login_url(self):
        """
        Gets the login_url of this AutonomousDatabaseConsoleTokenDetails.
        The login URL that allows the OCI Console to access the Autonomous Transaction Processing Service Console.


        :return: The login_url of this AutonomousDatabaseConsoleTokenDetails.
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        """
        Sets the login_url of this AutonomousDatabaseConsoleTokenDetails.
        The login URL that allows the OCI Console to access the Autonomous Transaction Processing Service Console.


        :param login_url: The login_url of this AutonomousDatabaseConsoleTokenDetails.
        :type: str
        """
        self._login_url = login_url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
