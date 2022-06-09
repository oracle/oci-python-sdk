# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoicingUser(object):
    """
    User.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvoicingUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this InvoicingUser.
        :type name: str

        :param user_name:
            The value to assign to the user_name property of this InvoicingUser.
        :type user_name: str

        :param first_name:
            The value to assign to the first_name property of this InvoicingUser.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this InvoicingUser.
        :type last_name: str

        :param email:
            The value to assign to the email property of this InvoicingUser.
        :type email: str

        :param tca_contact_id:
            The value to assign to the tca_contact_id property of this InvoicingUser.
        :type tca_contact_id: int

        :param tca_cust_accnt_site_id:
            The value to assign to the tca_cust_accnt_site_id property of this InvoicingUser.
        :type tca_cust_accnt_site_id: int

        :param tca_party_id:
            The value to assign to the tca_party_id property of this InvoicingUser.
        :type tca_party_id: int

        """
        self.swagger_types = {
            'name': 'str',
            'user_name': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'email': 'str',
            'tca_contact_id': 'int',
            'tca_cust_accnt_site_id': 'int',
            'tca_party_id': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'user_name': 'userName',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'tca_contact_id': 'tcaContactId',
            'tca_cust_accnt_site_id': 'tcaCustAccntSiteId',
            'tca_party_id': 'tcaPartyId'
        }

        self._name = None
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._tca_contact_id = None
        self._tca_cust_accnt_site_id = None
        self._tca_party_id = None

    @property
    def name(self):
        """
        Gets the name of this InvoicingUser.
        Name.


        :return: The name of this InvoicingUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InvoicingUser.
        Name.


        :param name: The name of this InvoicingUser.
        :type: str
        """
        self._name = name

    @property
    def user_name(self):
        """
        Gets the user_name of this InvoicingUser.
        userName.


        :return: The user_name of this InvoicingUser.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this InvoicingUser.
        userName.


        :param user_name: The user_name of this InvoicingUser.
        :type: str
        """
        self._user_name = user_name

    @property
    def first_name(self):
        """
        Gets the first_name of this InvoicingUser.
        First name.


        :return: The first_name of this InvoicingUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this InvoicingUser.
        First name.


        :param first_name: The first_name of this InvoicingUser.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this InvoicingUser.
        Last name.


        :return: The last_name of this InvoicingUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this InvoicingUser.
        Last name.


        :param last_name: The last_name of this InvoicingUser.
        :type: str
        """
        self._last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this InvoicingUser.
        Email.


        :return: The email of this InvoicingUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this InvoicingUser.
        Email.


        :param email: The email of this InvoicingUser.
        :type: str
        """
        self._email = email

    @property
    def tca_contact_id(self):
        """
        Gets the tca_contact_id of this InvoicingUser.
        TCA contact ID.


        :return: The tca_contact_id of this InvoicingUser.
        :rtype: int
        """
        return self._tca_contact_id

    @tca_contact_id.setter
    def tca_contact_id(self, tca_contact_id):
        """
        Sets the tca_contact_id of this InvoicingUser.
        TCA contact ID.


        :param tca_contact_id: The tca_contact_id of this InvoicingUser.
        :type: int
        """
        self._tca_contact_id = tca_contact_id

    @property
    def tca_cust_accnt_site_id(self):
        """
        Gets the tca_cust_accnt_site_id of this InvoicingUser.
        TCA customer account site ID.


        :return: The tca_cust_accnt_site_id of this InvoicingUser.
        :rtype: int
        """
        return self._tca_cust_accnt_site_id

    @tca_cust_accnt_site_id.setter
    def tca_cust_accnt_site_id(self, tca_cust_accnt_site_id):
        """
        Sets the tca_cust_accnt_site_id of this InvoicingUser.
        TCA customer account site ID.


        :param tca_cust_accnt_site_id: The tca_cust_accnt_site_id of this InvoicingUser.
        :type: int
        """
        self._tca_cust_accnt_site_id = tca_cust_accnt_site_id

    @property
    def tca_party_id(self):
        """
        Gets the tca_party_id of this InvoicingUser.
        TCA party ID.


        :return: The tca_party_id of this InvoicingUser.
        :rtype: int
        """
        return self._tca_party_id

    @tca_party_id.setter
    def tca_party_id(self, tca_party_id):
        """
        Sets the tca_party_id of this InvoicingUser.
        TCA party ID.


        :param tca_party_id: The tca_party_id of this InvoicingUser.
        :type: int
        """
        self._tca_party_id = tca_party_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
