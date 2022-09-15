# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GeodataDetails(object):
    """
    Geodata information for a given IP address
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GeodataDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param routed_prefix:
            The value to assign to the routed_prefix property of this GeodataDetails.
        :type routed_prefix: str

        :param origin:
            The value to assign to the origin property of this GeodataDetails.
        :type origin: str

        :param geo_id:
            The value to assign to the geo_id property of this GeodataDetails.
        :type geo_id: str

        :param country_code:
            The value to assign to the country_code property of this GeodataDetails.
        :type country_code: str

        :param admin_div:
            The value to assign to the admin_div property of this GeodataDetails.
        :type admin_div: str

        :param city:
            The value to assign to the city property of this GeodataDetails.
        :type city: str

        :param latitude:
            The value to assign to the latitude property of this GeodataDetails.
        :type latitude: str

        :param longitude:
            The value to assign to the longitude property of this GeodataDetails.
        :type longitude: str

        :param label:
            The value to assign to the label property of this GeodataDetails.
        :type label: str

        """
        self.swagger_types = {
            'routed_prefix': 'str',
            'origin': 'str',
            'geo_id': 'str',
            'country_code': 'str',
            'admin_div': 'str',
            'city': 'str',
            'latitude': 'str',
            'longitude': 'str',
            'label': 'str'
        }

        self.attribute_map = {
            'routed_prefix': 'routedPrefix',
            'origin': 'origin',
            'geo_id': 'geoId',
            'country_code': 'countryCode',
            'admin_div': 'adminDiv',
            'city': 'city',
            'latitude': 'latitude',
            'longitude': 'longitude',
            'label': 'label'
        }

        self._routed_prefix = None
        self._origin = None
        self._geo_id = None
        self._country_code = None
        self._admin_div = None
        self._city = None
        self._latitude = None
        self._longitude = None
        self._label = None

    @property
    def routed_prefix(self):
        """
        Gets the routed_prefix of this GeodataDetails.
        Encompassing assigned prefix for the IP


        :return: The routed_prefix of this GeodataDetails.
        :rtype: str
        """
        return self._routed_prefix

    @routed_prefix.setter
    def routed_prefix(self, routed_prefix):
        """
        Sets the routed_prefix of this GeodataDetails.
        Encompassing assigned prefix for the IP


        :param routed_prefix: The routed_prefix of this GeodataDetails.
        :type: str
        """
        self._routed_prefix = routed_prefix

    @property
    def origin(self):
        """
        **[Required]** Gets the origin of this GeodataDetails.
        ASN entry


        :return: The origin of this GeodataDetails.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this GeodataDetails.
        ASN entry


        :param origin: The origin of this GeodataDetails.
        :type: str
        """
        self._origin = origin

    @property
    def geo_id(self):
        """
        Gets the geo_id of this GeodataDetails.
        Unique Identifier (optional)


        :return: The geo_id of this GeodataDetails.
        :rtype: str
        """
        return self._geo_id

    @geo_id.setter
    def geo_id(self, geo_id):
        """
        Sets the geo_id of this GeodataDetails.
        Unique Identifier (optional)


        :param geo_id: The geo_id of this GeodataDetails.
        :type: str
        """
        self._geo_id = geo_id

    @property
    def country_code(self):
        """
        **[Required]** Gets the country_code of this GeodataDetails.
        Two-letter abbreviation for country of origin


        :return: The country_code of this GeodataDetails.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this GeodataDetails.
        Two-letter abbreviation for country of origin


        :param country_code: The country_code of this GeodataDetails.
        :type: str
        """
        self._country_code = country_code

    @property
    def admin_div(self):
        """
        **[Required]** Gets the admin_div of this GeodataDetails.
        State/Province/subdivision within the country


        :return: The admin_div of this GeodataDetails.
        :rtype: str
        """
        return self._admin_div

    @admin_div.setter
    def admin_div(self, admin_div):
        """
        Sets the admin_div of this GeodataDetails.
        State/Province/subdivision within the country


        :param admin_div: The admin_div of this GeodataDetails.
        :type: str
        """
        self._admin_div = admin_div

    @property
    def city(self):
        """
        **[Required]** Gets the city of this GeodataDetails.
        City of origin


        :return: The city of this GeodataDetails.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this GeodataDetails.
        City of origin


        :param city: The city of this GeodataDetails.
        :type: str
        """
        self._city = city

    @property
    def latitude(self):
        """
        **[Required]** Gets the latitude of this GeodataDetails.
        Latitude


        :return: The latitude of this GeodataDetails.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this GeodataDetails.
        Latitude


        :param latitude: The latitude of this GeodataDetails.
        :type: str
        """
        self._latitude = latitude

    @property
    def longitude(self):
        """
        **[Required]** Gets the longitude of this GeodataDetails.
        Longitude


        :return: The longitude of this GeodataDetails.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this GeodataDetails.
        Longitude


        :param longitude: The longitude of this GeodataDetails.
        :type: str
        """
        self._longitude = longitude

    @property
    def label(self):
        """
        **[Required]** Gets the label of this GeodataDetails.
        Information on source providing the information


        :return: The label of this GeodataDetails.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this GeodataDetails.
        Information on source providing the information


        :param label: The label of this GeodataDetails.
        :type: str
        """
        self._label = label

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
