# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TranscriptionModelDetails(object):
    """
    Model details.
    """

    #: A constant which can be used with the domain property of a TranscriptionModelDetails.
    #: This constant has a value of "GENERIC"
    DOMAIN_GENERIC = "GENERIC"

    #: A constant which can be used with the language_code property of a TranscriptionModelDetails.
    #: This constant has a value of "en-US"
    LANGUAGE_CODE_EN_US = "en-US"

    #: A constant which can be used with the language_code property of a TranscriptionModelDetails.
    #: This constant has a value of "es-ES"
    LANGUAGE_CODE_ES_ES = "es-ES"

    #: A constant which can be used with the language_code property of a TranscriptionModelDetails.
    #: This constant has a value of "pt-BR"
    LANGUAGE_CODE_PT_BR = "pt-BR"

    def __init__(self, **kwargs):
        """
        Initializes a new TranscriptionModelDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param domain:
            The value to assign to the domain property of this TranscriptionModelDetails.
            Allowed values for this property are: "GENERIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type domain: str

        :param language_code:
            The value to assign to the language_code property of this TranscriptionModelDetails.
            Allowed values for this property are: "en-US", "es-ES", "pt-BR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type language_code: str

        """
        self.swagger_types = {
            'domain': 'str',
            'language_code': 'str'
        }

        self.attribute_map = {
            'domain': 'domain',
            'language_code': 'languageCode'
        }

        self._domain = None
        self._language_code = None

    @property
    def domain(self):
        """
        Gets the domain of this TranscriptionModelDetails.
        Domain for input files.

        Allowed values for this property are: "GENERIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The domain of this TranscriptionModelDetails.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this TranscriptionModelDetails.
        Domain for input files.


        :param domain: The domain of this TranscriptionModelDetails.
        :type: str
        """
        allowed_values = ["GENERIC"]
        if not value_allowed_none_or_none_sentinel(domain, allowed_values):
            domain = 'UNKNOWN_ENUM_VALUE'
        self._domain = domain

    @property
    def language_code(self):
        """
        Gets the language_code of this TranscriptionModelDetails.
        Locale value as per given in [https://datatracker.ietf.org/doc/html/rfc5646].

        Allowed values for this property are: "en-US", "es-ES", "pt-BR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The language_code of this TranscriptionModelDetails.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this TranscriptionModelDetails.
        Locale value as per given in [https://datatracker.ietf.org/doc/html/rfc5646].


        :param language_code: The language_code of this TranscriptionModelDetails.
        :type: str
        """
        allowed_values = ["en-US", "es-ES", "pt-BR"]
        if not value_allowed_none_or_none_sentinel(language_code, allowed_values):
            language_code = 'UNKNOWN_ENUM_VALUE'
        self._language_code = language_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
