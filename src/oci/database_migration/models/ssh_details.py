# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SshDetails(object):
    """
    Details of the SSH key that will be used.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SshDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host:
            The value to assign to the host property of this SshDetails.
        :type host: str

        :param user:
            The value to assign to the user property of this SshDetails.
        :type user: str

        :param sudo_location:
            The value to assign to the sudo_location property of this SshDetails.
        :type sudo_location: str

        """
        self.swagger_types = {
            'host': 'str',
            'user': 'str',
            'sudo_location': 'str'
        }

        self.attribute_map = {
            'host': 'host',
            'user': 'user',
            'sudo_location': 'sudoLocation'
        }

        self._host = None
        self._user = None
        self._sudo_location = None

    @property
    def host(self):
        """
        **[Required]** Gets the host of this SshDetails.
        Name of the host the SSH key is valid for.


        :return: The host of this SshDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this SshDetails.
        Name of the host the SSH key is valid for.


        :param host: The host of this SshDetails.
        :type: str
        """
        self._host = host

    @property
    def user(self):
        """
        **[Required]** Gets the user of this SshDetails.
        SSH user


        :return: The user of this SshDetails.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this SshDetails.
        SSH user


        :param user: The user of this SshDetails.
        :type: str
        """
        self._user = user

    @property
    def sudo_location(self):
        """
        **[Required]** Gets the sudo_location of this SshDetails.
        Sudo location


        :return: The sudo_location of this SshDetails.
        :rtype: str
        """
        return self._sudo_location

    @sudo_location.setter
    def sudo_location(self, sudo_location):
        """
        Sets the sudo_location of this SshDetails.
        Sudo location


        :param sudo_location: The sudo_location of this SshDetails.
        :type: str
        """
        self._sudo_location = sudo_location

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
