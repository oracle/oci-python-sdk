# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaxSummary(object):
    """
    Tax implication that current tenant may be eligible while using specific listing
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TaxSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param code:
            The value to assign to the code property of this TaxSummary.
        :type code: str

        :param name:
            The value to assign to the name property of this TaxSummary.
        :type name: str

        :param country:
            The value to assign to the country property of this TaxSummary.
        :type country: str

        :param url:
            The value to assign to the url property of this TaxSummary.
        :type url: str

        """
        self.swagger_types = {
            'code': 'str',
            'name': 'str',
            'country': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'name': 'name',
            'country': 'country',
            'url': 'url'
        }

        self._code = None
        self._name = None
        self._country = None
        self._url = None

    @property
    def code(self):
        """
        **[Required]** Gets the code of this TaxSummary.
        Unique code for the tax.


        :return: The code of this TaxSummary.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this TaxSummary.
        Unique code for the tax.


        :param code: The code of this TaxSummary.
        :type: str
        """
        self._code = code

    @property
    def name(self):
        """
        Gets the name of this TaxSummary.
        Name of the tax code.


        :return: The name of this TaxSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaxSummary.
        Name of the tax code.


        :param name: The name of this TaxSummary.
        :type: str
        """
        self._name = name

    @property
    def country(self):
        """
        Gets the country of this TaxSummary.
        Country, which imposes the tax.


        :return: The country of this TaxSummary.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this TaxSummary.
        Country, which imposes the tax.


        :param country: The country of this TaxSummary.
        :type: str
        """
        self._country = country

    @property
    def url(self):
        """
        Gets the url of this TaxSummary.
        The URL with more details about this tax.


        :return: The url of this TaxSummary.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this TaxSummary.
        The URL with more details about this tax.


        :param url: The url of this TaxSummary.
        :type: str
        """
        self._url = url

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
