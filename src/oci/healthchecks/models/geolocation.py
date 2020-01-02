# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Geolocation(object):
    """
    Geographic information about a vantage point.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Geolocation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param geo_key:
            The value to assign to the geo_key property of this Geolocation.
        :type geo_key: str

        :param admin_div_code:
            The value to assign to the admin_div_code property of this Geolocation.
        :type admin_div_code: str

        :param city_name:
            The value to assign to the city_name property of this Geolocation.
        :type city_name: str

        :param country_code:
            The value to assign to the country_code property of this Geolocation.
        :type country_code: str

        :param country_name:
            The value to assign to the country_name property of this Geolocation.
        :type country_name: str

        :param latitude:
            The value to assign to the latitude property of this Geolocation.
        :type latitude: float

        :param longitude:
            The value to assign to the longitude property of this Geolocation.
        :type longitude: float

        """
        self.swagger_types = {
            'geo_key': 'str',
            'admin_div_code': 'str',
            'city_name': 'str',
            'country_code': 'str',
            'country_name': 'str',
            'latitude': 'float',
            'longitude': 'float'
        }

        self.attribute_map = {
            'geo_key': 'geoKey',
            'admin_div_code': 'adminDivCode',
            'city_name': 'cityName',
            'country_code': 'countryCode',
            'country_name': 'countryName',
            'latitude': 'latitude',
            'longitude': 'longitude'
        }

        self._geo_key = None
        self._admin_div_code = None
        self._city_name = None
        self._country_code = None
        self._country_name = None
        self._latitude = None
        self._longitude = None

    @property
    def geo_key(self):
        """
        Gets the geo_key of this Geolocation.
        An opaque identifier for the geographic location of the vantage point.


        :return: The geo_key of this Geolocation.
        :rtype: str
        """
        return self._geo_key

    @geo_key.setter
    def geo_key(self, geo_key):
        """
        Sets the geo_key of this Geolocation.
        An opaque identifier for the geographic location of the vantage point.


        :param geo_key: The geo_key of this Geolocation.
        :type: str
        """
        self._geo_key = geo_key

    @property
    def admin_div_code(self):
        """
        Gets the admin_div_code of this Geolocation.
        The ISO 3166-2 code for this location's first-level administrative
        division, either a US state or Canadian province. Only included for locations
        in the US or Canada. For a list of codes, see
        `Country Codes`__.

        __ https://www.iso.org/obp/ui/#search


        :return: The admin_div_code of this Geolocation.
        :rtype: str
        """
        return self._admin_div_code

    @admin_div_code.setter
    def admin_div_code(self, admin_div_code):
        """
        Sets the admin_div_code of this Geolocation.
        The ISO 3166-2 code for this location's first-level administrative
        division, either a US state or Canadian province. Only included for locations
        in the US or Canada. For a list of codes, see
        `Country Codes`__.

        __ https://www.iso.org/obp/ui/#search


        :param admin_div_code: The admin_div_code of this Geolocation.
        :type: str
        """
        self._admin_div_code = admin_div_code

    @property
    def city_name(self):
        """
        Gets the city_name of this Geolocation.
        Common English-language name for the city.


        :return: The city_name of this Geolocation.
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name):
        """
        Sets the city_name of this Geolocation.
        Common English-language name for the city.


        :param city_name: The city_name of this Geolocation.
        :type: str
        """
        self._city_name = city_name

    @property
    def country_code(self):
        """
        Gets the country_code of this Geolocation.
        The ISO 3166-1 alpha-2 country code. For a list of codes,
        see `Country Codes`__.

        __ https://www.iso.org/obp/ui/#search


        :return: The country_code of this Geolocation.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this Geolocation.
        The ISO 3166-1 alpha-2 country code. For a list of codes,
        see `Country Codes`__.

        __ https://www.iso.org/obp/ui/#search


        :param country_code: The country_code of this Geolocation.
        :type: str
        """
        self._country_code = country_code

    @property
    def country_name(self):
        """
        Gets the country_name of this Geolocation.
        The common English-language name for the country.


        :return: The country_name of this Geolocation.
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """
        Sets the country_name of this Geolocation.
        The common English-language name for the country.


        :param country_name: The country_name of this Geolocation.
        :type: str
        """
        self._country_name = country_name

    @property
    def latitude(self):
        """
        Gets the latitude of this Geolocation.
        Degrees north of the Equator.


        :return: The latitude of this Geolocation.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this Geolocation.
        Degrees north of the Equator.


        :param latitude: The latitude of this Geolocation.
        :type: float
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this Geolocation.
        Degrees east of the prime meridian.


        :return: The longitude of this Geolocation.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this Geolocation.
        Degrees east of the prime meridian.


        :param longitude: The longitude of this Geolocation.
        :type: float
        """
        self._longitude = longitude

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
