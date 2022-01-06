# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .http_response_body import HttpResponseBody
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StaticTextHttpResponseBody(HttpResponseBody):
    """
    Allows returning static text as HTTP response body.
    Example:
    {
    \"type\": \"STATIC_TEXT\",
    \"text\": \"{\
    \\\"code\\\": 403,\
    \\\"message\\\":\\\"Unauthorised\\\"\
    }\"
    }
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StaticTextHttpResponseBody object with values from keyword arguments. The default value of the :py:attr:`~oci.waf.models.StaticTextHttpResponseBody.type` attribute
        of this class is ``STATIC_TEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this StaticTextHttpResponseBody.
            Allowed values for this property are: "STATIC_TEXT"
        :type type: str

        :param text:
            The value to assign to the text property of this StaticTextHttpResponseBody.
        :type text: str

        """
        self.swagger_types = {
            'type': 'str',
            'text': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'text': 'text'
        }

        self._type = None
        self._text = None
        self._type = 'STATIC_TEXT'

    @property
    def text(self):
        """
        **[Required]** Gets the text of this StaticTextHttpResponseBody.
        Static response body text.


        :return: The text of this StaticTextHttpResponseBody.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this StaticTextHttpResponseBody.
        Static response body text.


        :param text: The text of this StaticTextHttpResponseBody.
        :type: str
        """
        self._text = text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
