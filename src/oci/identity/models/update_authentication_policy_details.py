# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAuthenticationPolicyDetails(object):
    """
    Update request for authentication policy, describes set of validation rules and their parameters to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAuthenticationPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password_policy:
            The value to assign to the password_policy property of this UpdateAuthenticationPolicyDetails.
        :type password_policy: PasswordPolicy

        :param network_policy:
            The value to assign to the network_policy property of this UpdateAuthenticationPolicyDetails.
        :type network_policy: NetworkPolicy

        """
        self.swagger_types = {
            'password_policy': 'PasswordPolicy',
            'network_policy': 'NetworkPolicy'
        }

        self.attribute_map = {
            'password_policy': 'passwordPolicy',
            'network_policy': 'networkPolicy'
        }

        self._password_policy = None
        self._network_policy = None

    @property
    def password_policy(self):
        """
        Gets the password_policy of this UpdateAuthenticationPolicyDetails.

        :return: The password_policy of this UpdateAuthenticationPolicyDetails.
        :rtype: PasswordPolicy
        """
        return self._password_policy

    @password_policy.setter
    def password_policy(self, password_policy):
        """
        Sets the password_policy of this UpdateAuthenticationPolicyDetails.

        :param password_policy: The password_policy of this UpdateAuthenticationPolicyDetails.
        :type: PasswordPolicy
        """
        self._password_policy = password_policy

    @property
    def network_policy(self):
        """
        Gets the network_policy of this UpdateAuthenticationPolicyDetails.

        :return: The network_policy of this UpdateAuthenticationPolicyDetails.
        :rtype: NetworkPolicy
        """
        return self._network_policy

    @network_policy.setter
    def network_policy(self, network_policy):
        """
        Sets the network_policy of this UpdateAuthenticationPolicyDetails.

        :param network_policy: The network_policy of this UpdateAuthenticationPolicyDetails.
        :type: NetworkPolicy
        """
        self._network_policy = network_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
