# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RedeemableUserSummary(object):
    """
    User summary that can redeem rewards.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RedeemableUserSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param email_id:
            The value to assign to the email_id property of this RedeemableUserSummary.
        :type email_id: str

        :param first_name:
            The value to assign to the first_name property of this RedeemableUserSummary.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this RedeemableUserSummary.
        :type last_name: str

        """
        self.swagger_types = {
            'email_id': 'str',
            'first_name': 'str',
            'last_name': 'str'
        }

        self.attribute_map = {
            'email_id': 'emailId',
            'first_name': 'firstName',
            'last_name': 'lastName'
        }

        self._email_id = None
        self._first_name = None
        self._last_name = None

    @property
    def email_id(self):
        """
        Gets the email_id of this RedeemableUserSummary.
        The email ID of the user that can redeem rewards.


        :return: The email_id of this RedeemableUserSummary.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """
        Sets the email_id of this RedeemableUserSummary.
        The email ID of the user that can redeem rewards.


        :param email_id: The email_id of this RedeemableUserSummary.
        :type: str
        """
        self._email_id = email_id

    @property
    def first_name(self):
        """
        Gets the first_name of this RedeemableUserSummary.
        The first name of the user that can redeem rewards.


        :return: The first_name of this RedeemableUserSummary.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this RedeemableUserSummary.
        The first name of the user that can redeem rewards.


        :param first_name: The first_name of this RedeemableUserSummary.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this RedeemableUserSummary.
        The last name of the user that can redeem rewards.


        :return: The last_name of this RedeemableUserSummary.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this RedeemableUserSummary.
        The last name of the user that can redeem rewards.


        :param last_name: The last_name of this RedeemableUserSummary.
        :type: str
        """
        self._last_name = last_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
