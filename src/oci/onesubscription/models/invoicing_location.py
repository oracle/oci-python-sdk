# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InvoicingLocation(object):
    """
    Address location.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InvoicingLocation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param address1:
            The value to assign to the address1 property of this InvoicingLocation.
        :type address1: str

        :param address2:
            The value to assign to the address2 property of this InvoicingLocation.
        :type address2: str

        :param postal_code:
            The value to assign to the postal_code property of this InvoicingLocation.
        :type postal_code: str

        :param city:
            The value to assign to the city property of this InvoicingLocation.
        :type city: str

        :param country:
            The value to assign to the country property of this InvoicingLocation.
        :type country: str

        :param region:
            The value to assign to the region property of this InvoicingLocation.
        :type region: str

        :param tca_location_id:
            The value to assign to the tca_location_id property of this InvoicingLocation.
        :type tca_location_id: int

        """
        self.swagger_types = {
            'address1': 'str',
            'address2': 'str',
            'postal_code': 'str',
            'city': 'str',
            'country': 'str',
            'region': 'str',
            'tca_location_id': 'int'
        }

        self.attribute_map = {
            'address1': 'address1',
            'address2': 'address2',
            'postal_code': 'postalCode',
            'city': 'city',
            'country': 'country',
            'region': 'region',
            'tca_location_id': 'tcaLocationId'
        }

        self._address1 = None
        self._address2 = None
        self._postal_code = None
        self._city = None
        self._country = None
        self._region = None
        self._tca_location_id = None

    @property
    def address1(self):
        """
        Gets the address1 of this InvoicingLocation.
        Address first line.


        :return: The address1 of this InvoicingLocation.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this InvoicingLocation.
        Address first line.


        :param address1: The address1 of this InvoicingLocation.
        :type: str
        """
        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this InvoicingLocation.
        Address second line.


        :return: The address2 of this InvoicingLocation.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this InvoicingLocation.
        Address second line.


        :param address2: The address2 of this InvoicingLocation.
        :type: str
        """
        self._address2 = address2

    @property
    def postal_code(self):
        """
        Gets the postal_code of this InvoicingLocation.
        Postal code.


        :return: The postal_code of this InvoicingLocation.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this InvoicingLocation.
        Postal code.


        :param postal_code: The postal_code of this InvoicingLocation.
        :type: str
        """
        self._postal_code = postal_code

    @property
    def city(self):
        """
        Gets the city of this InvoicingLocation.
        City.


        :return: The city of this InvoicingLocation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this InvoicingLocation.
        City.


        :param city: The city of this InvoicingLocation.
        :type: str
        """
        self._city = city

    @property
    def country(self):
        """
        Gets the country of this InvoicingLocation.
        Country.


        :return: The country of this InvoicingLocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this InvoicingLocation.
        Country.


        :param country: The country of this InvoicingLocation.
        :type: str
        """
        self._country = country

    @property
    def region(self):
        """
        Gets the region of this InvoicingLocation.
        Region.


        :return: The region of this InvoicingLocation.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this InvoicingLocation.
        Region.


        :param region: The region of this InvoicingLocation.
        :type: str
        """
        self._region = region

    @property
    def tca_location_id(self):
        """
        Gets the tca_location_id of this InvoicingLocation.
        TCA Location identifier.


        :return: The tca_location_id of this InvoicingLocation.
        :rtype: int
        """
        return self._tca_location_id

    @tca_location_id.setter
    def tca_location_id(self, tca_location_id):
        """
        Sets the tca_location_id of this InvoicingLocation.
        TCA Location identifier.


        :param tca_location_id: The tca_location_id of this InvoicingLocation.
        :type: int
        """
        self._tca_location_id = tca_location_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
