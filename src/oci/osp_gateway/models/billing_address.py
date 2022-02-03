# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BillingAddress(object):
    """
    Billing address details model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BillingAddress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address_key:
            The value to assign to the address_key property of this BillingAddress.
        :type address_key: str

        :param line1:
            The value to assign to the line1 property of this BillingAddress.
        :type line1: str

        :param line2:
            The value to assign to the line2 property of this BillingAddress.
        :type line2: str

        :param city:
            The value to assign to the city property of this BillingAddress.
        :type city: str

        :param country:
            The value to assign to the country property of this BillingAddress.
        :type country: str

        :param postal_code:
            The value to assign to the postal_code property of this BillingAddress.
        :type postal_code: str

        :param state:
            The value to assign to the state property of this BillingAddress.
        :type state: str

        :param email_address:
            The value to assign to the email_address property of this BillingAddress.
        :type email_address: str

        :param company_name:
            The value to assign to the company_name property of this BillingAddress.
        :type company_name: str

        :param first_name:
            The value to assign to the first_name property of this BillingAddress.
        :type first_name: str

        :param last_name:
            The value to assign to the last_name property of this BillingAddress.
        :type last_name: str

        """
        self.swagger_types = {
            'address_key': 'str',
            'line1': 'str',
            'line2': 'str',
            'city': 'str',
            'country': 'str',
            'postal_code': 'str',
            'state': 'str',
            'email_address': 'str',
            'company_name': 'str',
            'first_name': 'str',
            'last_name': 'str'
        }

        self.attribute_map = {
            'address_key': 'addressKey',
            'line1': 'line1',
            'line2': 'line2',
            'city': 'city',
            'country': 'country',
            'postal_code': 'postalCode',
            'state': 'state',
            'email_address': 'emailAddress',
            'company_name': 'companyName',
            'first_name': 'firstName',
            'last_name': 'lastName'
        }

        self._address_key = None
        self._line1 = None
        self._line2 = None
        self._city = None
        self._country = None
        self._postal_code = None
        self._state = None
        self._email_address = None
        self._company_name = None
        self._first_name = None
        self._last_name = None

    @property
    def address_key(self):
        """
        Gets the address_key of this BillingAddress.
        Address identifier.


        :return: The address_key of this BillingAddress.
        :rtype: str
        """
        return self._address_key

    @address_key.setter
    def address_key(self, address_key):
        """
        Sets the address_key of this BillingAddress.
        Address identifier.


        :param address_key: The address_key of this BillingAddress.
        :type: str
        """
        self._address_key = address_key

    @property
    def line1(self):
        """
        Gets the line1 of this BillingAddress.
        Address line 1.


        :return: The line1 of this BillingAddress.
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """
        Sets the line1 of this BillingAddress.
        Address line 1.


        :param line1: The line1 of this BillingAddress.
        :type: str
        """
        self._line1 = line1

    @property
    def line2(self):
        """
        Gets the line2 of this BillingAddress.
        Address line 2.


        :return: The line2 of this BillingAddress.
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """
        Sets the line2 of this BillingAddress.
        Address line 2.


        :param line2: The line2 of this BillingAddress.
        :type: str
        """
        self._line2 = line2

    @property
    def city(self):
        """
        Gets the city of this BillingAddress.
        Name of the city.


        :return: The city of this BillingAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this BillingAddress.
        Name of the city.


        :param city: The city of this BillingAddress.
        :type: str
        """
        self._city = city

    @property
    def country(self):
        """
        Gets the country of this BillingAddress.
        Country of the address.


        :return: The country of this BillingAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillingAddress.
        Country of the address.


        :param country: The country of this BillingAddress.
        :type: str
        """
        self._country = country

    @property
    def postal_code(self):
        """
        Gets the postal_code of this BillingAddress.
        Post code of the address.


        :return: The postal_code of this BillingAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this BillingAddress.
        Post code of the address.


        :param postal_code: The postal_code of this BillingAddress.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def state(self):
        """
        Gets the state of this BillingAddress.
        State of the address.


        :return: The state of this BillingAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this BillingAddress.
        State of the address.


        :param state: The state of this BillingAddress.
        :type: str
        """
        self._state = state

    @property
    def email_address(self):
        """
        Gets the email_address of this BillingAddress.
        Contact person email address.


        :return: The email_address of this BillingAddress.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this BillingAddress.
        Contact person email address.


        :param email_address: The email_address of this BillingAddress.
        :type: str
        """
        self._email_address = email_address

    @property
    def company_name(self):
        """
        Gets the company_name of this BillingAddress.
        Name of the customer company.


        :return: The company_name of this BillingAddress.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this BillingAddress.
        Name of the customer company.


        :param company_name: The company_name of this BillingAddress.
        :type: str
        """
        self._company_name = company_name

    @property
    def first_name(self):
        """
        Gets the first_name of this BillingAddress.
        First name of the contact person.


        :return: The first_name of this BillingAddress.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this BillingAddress.
        First name of the contact person.


        :param first_name: The first_name of this BillingAddress.
        :type: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this BillingAddress.
        Last name of the contact person.


        :return: The last_name of this BillingAddress.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this BillingAddress.
        Last name of the contact person.


        :param last_name: The last_name of this BillingAddress.
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
