# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PayInvoiceDetails(object):
    """
    Request object for invoice payment
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PayInvoiceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param language_code:
            The value to assign to the language_code property of this PayInvoiceDetails.
        :type language_code: str

        :param return_url:
            The value to assign to the return_url property of this PayInvoiceDetails.
        :type return_url: str

        :param email:
            The value to assign to the email property of this PayInvoiceDetails.
        :type email: str

        """
        self.swagger_types = {
            'language_code': 'str',
            'return_url': 'str',
            'email': 'str'
        }

        self.attribute_map = {
            'language_code': 'languageCode',
            'return_url': 'returnUrl',
            'email': 'email'
        }

        self._language_code = None
        self._return_url = None
        self._email = None

    @property
    def language_code(self):
        """
        Gets the language_code of this PayInvoiceDetails.
        Language code


        :return: The language_code of this PayInvoiceDetails.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this PayInvoiceDetails.
        Language code


        :param language_code: The language_code of this PayInvoiceDetails.
        :type: str
        """
        self._language_code = language_code

    @property
    def return_url(self):
        """
        Gets the return_url of this PayInvoiceDetails.
        Callback URL


        :return: The return_url of this PayInvoiceDetails.
        :rtype: str
        """
        return self._return_url

    @return_url.setter
    def return_url(self, return_url):
        """
        Sets the return_url of this PayInvoiceDetails.
        Callback URL


        :param return_url: The return_url of this PayInvoiceDetails.
        :type: str
        """
        self._return_url = return_url

    @property
    def email(self):
        """
        **[Required]** Gets the email of this PayInvoiceDetails.
        User email


        :return: The email of this PayInvoiceDetails.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PayInvoiceDetails.
        User email


        :param email: The email of this PayInvoiceDetails.
        :type: str
        """
        self._email = email

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
