# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200601


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EndpointProxy(object):
    """
    An object containing the endpoint proxy details.
    """

    #: A constant which can be used with the credential_type property of a EndpointProxy.
    #: This constant has a value of "NONE"
    CREDENTIAL_TYPE_NONE = "NONE"

    #: A constant which can be used with the credential_type property of a EndpointProxy.
    #: This constant has a value of "BASIC_AUTH"
    CREDENTIAL_TYPE_BASIC_AUTH = "BASIC_AUTH"

    #: A constant which can be used with the credential_type property of a EndpointProxy.
    #: This constant has a value of "TOKEN"
    CREDENTIAL_TYPE_TOKEN = "TOKEN"

    def __init__(self, **kwargs):
        """
        Initializes a new EndpointProxy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param url:
            The value to assign to the url property of this EndpointProxy.
        :type url: str

        :param credential_name:
            The value to assign to the credential_name property of this EndpointProxy.
        :type credential_name: str

        :param credential_type:
            The value to assign to the credential_type property of this EndpointProxy.
            Allowed values for this property are: "NONE", "BASIC_AUTH", "TOKEN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type credential_type: str

        """
        self.swagger_types = {
            'url': 'str',
            'credential_name': 'str',
            'credential_type': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'credential_name': 'credentialName',
            'credential_type': 'credentialType'
        }

        self._url = None
        self._credential_name = None
        self._credential_type = None

    @property
    def url(self):
        """
        **[Required]** Gets the url of this EndpointProxy.
        The proxy URL.


        :return: The url of this EndpointProxy.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this EndpointProxy.
        The proxy URL.


        :param url: The url of this EndpointProxy.
        :type: str
        """
        self._url = url

    @property
    def credential_name(self):
        """
        Gets the credential_name of this EndpointProxy.
        The named credential name on the management agent, containing the proxy credentials.


        :return: The credential_name of this EndpointProxy.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this EndpointProxy.
        The named credential name on the management agent, containing the proxy credentials.


        :param credential_name: The credential_name of this EndpointProxy.
        :type: str
        """
        self._credential_name = credential_name

    @property
    def credential_type(self):
        """
        Gets the credential_type of this EndpointProxy.
        The credential type. NONE indicates credentials are not needed to access the proxy.
        BASIC_AUTH represents a username and password based model. TOKEN represents a token based model.

        Allowed values for this property are: "NONE", "BASIC_AUTH", "TOKEN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The credential_type of this EndpointProxy.
        :rtype: str
        """
        return self._credential_type

    @credential_type.setter
    def credential_type(self, credential_type):
        """
        Sets the credential_type of this EndpointProxy.
        The credential type. NONE indicates credentials are not needed to access the proxy.
        BASIC_AUTH represents a username and password based model. TOKEN represents a token based model.


        :param credential_type: The credential_type of this EndpointProxy.
        :type: str
        """
        allowed_values = ["NONE", "BASIC_AUTH", "TOKEN"]
        if not value_allowed_none_or_none_sentinel(credential_type, allowed_values):
            credential_type = 'UNKNOWN_ENUM_VALUE'
        self._credential_type = credential_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other