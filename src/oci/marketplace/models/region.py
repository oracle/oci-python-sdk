# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Region(object):
    """
    The model for regions supported by a listing.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Region object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Region.
        :type name: str

        :param code:
            The value to assign to the code property of this Region.
        :type code: str

        :param countries:
            The value to assign to the countries property of this Region.
        :type countries: list[Item]

        """
        self.swagger_types = {
            'name': 'str',
            'code': 'str',
            'countries': 'list[Item]'
        }

        self.attribute_map = {
            'name': 'name',
            'code': 'code',
            'countries': 'countries'
        }

        self._name = None
        self._code = None
        self._countries = None

    @property
    def name(self):
        """
        Gets the name of this Region.
        The name of the region.


        :return: The name of this Region.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Region.
        The name of the region.


        :param name: The name of this Region.
        :type: str
        """
        self._name = name

    @property
    def code(self):
        """
        Gets the code of this Region.
        The code of the region.


        :return: The code of this Region.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Region.
        The code of the region.


        :param code: The code of this Region.
        :type: str
        """
        self._code = code

    @property
    def countries(self):
        """
        Gets the countries of this Region.
        Countries in the region.


        :return: The countries of this Region.
        :rtype: list[Item]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """
        Sets the countries of this Region.
        Countries in the region.


        :param countries: The countries of this Region.
        :type: list[Item]
        """
        self._countries = countries

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
