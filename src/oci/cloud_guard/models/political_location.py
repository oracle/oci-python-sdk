# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PoliticalLocation(object):
    """
    Political location of a problem
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PoliticalLocation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param city:
            The value to assign to the city property of this PoliticalLocation.
        :type city: str

        :param state:
            The value to assign to the state property of this PoliticalLocation.
        :type state: str

        :param country:
            The value to assign to the country property of this PoliticalLocation.
        :type country: str

        """
        self.swagger_types = {
            'city': 'str',
            'state': 'str',
            'country': 'str'
        }

        self.attribute_map = {
            'city': 'city',
            'state': 'state',
            'country': 'country'
        }

        self._city = None
        self._state = None
        self._country = None

    @property
    def city(self):
        """
        **[Required]** Gets the city of this PoliticalLocation.
        City


        :return: The city of this PoliticalLocation.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this PoliticalLocation.
        City


        :param city: The city of this PoliticalLocation.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        **[Required]** Gets the state of this PoliticalLocation.
        State


        :return: The state of this PoliticalLocation.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PoliticalLocation.
        State


        :param state: The state of this PoliticalLocation.
        :type: str
        """
        self._state = state

    @property
    def country(self):
        """
        **[Required]** Gets the country of this PoliticalLocation.
        Country


        :return: The country of this PoliticalLocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PoliticalLocation.
        Country


        :param country: The country of this PoliticalLocation.
        :type: str
        """
        self._country = country

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
