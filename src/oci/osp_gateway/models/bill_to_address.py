# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BillToAddress(object):
    """
    Address details model
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BillToAddress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param contact_name:
            The value to assign to the contact_name property of this BillToAddress.
        :type contact_name: str

        :param company_name:
            The value to assign to the company_name property of this BillToAddress.
        :type company_name: str

        :param address_line1:
            The value to assign to the address_line1 property of this BillToAddress.
        :type address_line1: str

        :param address_line2:
            The value to assign to the address_line2 property of this BillToAddress.
        :type address_line2: str

        :param address_line3:
            The value to assign to the address_line3 property of this BillToAddress.
        :type address_line3: str

        :param address_line4:
            The value to assign to the address_line4 property of this BillToAddress.
        :type address_line4: str

        :param street_name:
            The value to assign to the street_name property of this BillToAddress.
        :type street_name: str

        :param street_number:
            The value to assign to the street_number property of this BillToAddress.
        :type street_number: str

        :param city:
            The value to assign to the city property of this BillToAddress.
        :type city: str

        :param country:
            The value to assign to the country property of this BillToAddress.
        :type country: oci.osp_gateway.models.Country

        :param county:
            The value to assign to the county property of this BillToAddress.
        :type county: str

        :param state:
            The value to assign to the state property of this BillToAddress.
        :type state: str

        :param postal_code:
            The value to assign to the postal_code property of this BillToAddress.
        :type postal_code: str

        :param province:
            The value to assign to the province property of this BillToAddress.
        :type province: str

        """
        self.swagger_types = {
            'contact_name': 'str',
            'company_name': 'str',
            'address_line1': 'str',
            'address_line2': 'str',
            'address_line3': 'str',
            'address_line4': 'str',
            'street_name': 'str',
            'street_number': 'str',
            'city': 'str',
            'country': 'Country',
            'county': 'str',
            'state': 'str',
            'postal_code': 'str',
            'province': 'str'
        }

        self.attribute_map = {
            'contact_name': 'contactName',
            'company_name': 'companyName',
            'address_line1': 'addressLine1',
            'address_line2': 'addressLine2',
            'address_line3': 'addressLine3',
            'address_line4': 'addressLine4',
            'street_name': 'streetName',
            'street_number': 'streetNumber',
            'city': 'city',
            'country': 'country',
            'county': 'county',
            'state': 'state',
            'postal_code': 'postalCode',
            'province': 'province'
        }

        self._contact_name = None
        self._company_name = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._address_line4 = None
        self._street_name = None
        self._street_number = None
        self._city = None
        self._country = None
        self._county = None
        self._state = None
        self._postal_code = None
        self._province = None

    @property
    def contact_name(self):
        """
        Gets the contact_name of this BillToAddress.
        Name of the contact person


        :return: The contact_name of this BillToAddress.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """
        Sets the contact_name of this BillToAddress.
        Name of the contact person


        :param contact_name: The contact_name of this BillToAddress.
        :type: str
        """
        self._contact_name = contact_name

    @property
    def company_name(self):
        """
        Gets the company_name of this BillToAddress.
        Name of the customer company


        :return: The company_name of this BillToAddress.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """
        Sets the company_name of this BillToAddress.
        Name of the customer company


        :param company_name: The company_name of this BillToAddress.
        :type: str
        """
        self._company_name = company_name

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this BillToAddress.
        Address line 1


        :return: The address_line1 of this BillToAddress.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this BillToAddress.
        Address line 1


        :param address_line1: The address_line1 of this BillToAddress.
        :type: str
        """
        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this BillToAddress.
        Address line 2


        :return: The address_line2 of this BillToAddress.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this BillToAddress.
        Address line 2


        :param address_line2: The address_line2 of this BillToAddress.
        :type: str
        """
        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """
        Gets the address_line3 of this BillToAddress.
        Address line 3


        :return: The address_line3 of this BillToAddress.
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """
        Sets the address_line3 of this BillToAddress.
        Address line 3


        :param address_line3: The address_line3 of this BillToAddress.
        :type: str
        """
        self._address_line3 = address_line3

    @property
    def address_line4(self):
        """
        Gets the address_line4 of this BillToAddress.
        Address line 4


        :return: The address_line4 of this BillToAddress.
        :rtype: str
        """
        return self._address_line4

    @address_line4.setter
    def address_line4(self, address_line4):
        """
        Sets the address_line4 of this BillToAddress.
        Address line 4


        :param address_line4: The address_line4 of this BillToAddress.
        :type: str
        """
        self._address_line4 = address_line4

    @property
    def street_name(self):
        """
        Gets the street_name of this BillToAddress.
        Street name


        :return: The street_name of this BillToAddress.
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """
        Sets the street_name of this BillToAddress.
        Street name


        :param street_name: The street_name of this BillToAddress.
        :type: str
        """
        self._street_name = street_name

    @property
    def street_number(self):
        """
        Gets the street_number of this BillToAddress.
        House no


        :return: The street_number of this BillToAddress.
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """
        Sets the street_number of this BillToAddress.
        House no


        :param street_number: The street_number of this BillToAddress.
        :type: str
        """
        self._street_number = street_number

    @property
    def city(self):
        """
        Gets the city of this BillToAddress.
        Name of the city


        :return: The city of this BillToAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this BillToAddress.
        Name of the city


        :param city: The city of this BillToAddress.
        :type: str
        """
        self._city = city

    @property
    def country(self):
        """
        Gets the country of this BillToAddress.

        :return: The country of this BillToAddress.
        :rtype: oci.osp_gateway.models.Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this BillToAddress.

        :param country: The country of this BillToAddress.
        :type: oci.osp_gateway.models.Country
        """
        self._country = country

    @property
    def county(self):
        """
        Gets the county of this BillToAddress.
        County name


        :return: The county of this BillToAddress.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this BillToAddress.
        County name


        :param county: The county of this BillToAddress.
        :type: str
        """
        self._county = county

    @property
    def state(self):
        """
        Gets the state of this BillToAddress.
        Name of the state


        :return: The state of this BillToAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this BillToAddress.
        Name of the state


        :param state: The state of this BillToAddress.
        :type: str
        """
        self._state = state

    @property
    def postal_code(self):
        """
        Gets the postal_code of this BillToAddress.
        ZIP no


        :return: The postal_code of this BillToAddress.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this BillToAddress.
        ZIP no


        :param postal_code: The postal_code of this BillToAddress.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def province(self):
        """
        Gets the province of this BillToAddress.
        Name of the province


        :return: The province of this BillToAddress.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """
        Sets the province of this BillToAddress.
        Name of the province


        :param province: The province of this BillToAddress.
        :type: str
        """
        self._province = province

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
