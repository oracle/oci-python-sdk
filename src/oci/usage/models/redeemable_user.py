# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RedeemableUser(object):
    """
    The email object for a user that can redeem rewards.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RedeemableUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param email_id:
            The value to assign to the email_id property of this RedeemableUser.
        :type email_id: str

        """
        self.swagger_types = {
            'email_id': 'str'
        }

        self.attribute_map = {
            'email_id': 'emailId'
        }

        self._email_id = None

    @property
    def email_id(self):
        """
        **[Required]** Gets the email_id of this RedeemableUser.
        The email ID for a user that can redeem rewards.


        :return: The email_id of this RedeemableUser.
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """
        Sets the email_id of this RedeemableUser.
        The email ID for a user that can redeem rewards.


        :param email_id: The email_id of this RedeemableUser.
        :type: str
        """
        self._email_id = email_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
