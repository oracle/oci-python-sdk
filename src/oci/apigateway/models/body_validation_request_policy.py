# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BodyValidationRequestPolicy(object):
    """
    Validate the payload body of the incoming API requests on a specific route.
    """

    #: A constant which can be used with the validation_mode property of a BodyValidationRequestPolicy.
    #: This constant has a value of "ENFORCING"
    VALIDATION_MODE_ENFORCING = "ENFORCING"

    #: A constant which can be used with the validation_mode property of a BodyValidationRequestPolicy.
    #: This constant has a value of "PERMISSIVE"
    VALIDATION_MODE_PERMISSIVE = "PERMISSIVE"

    #: A constant which can be used with the validation_mode property of a BodyValidationRequestPolicy.
    #: This constant has a value of "DISABLED"
    VALIDATION_MODE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new BodyValidationRequestPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param required:
            The value to assign to the required property of this BodyValidationRequestPolicy.
        :type required: bool

        :param content:
            The value to assign to the content property of this BodyValidationRequestPolicy.
        :type content: dict(str, ContentValidation)

        :param validation_mode:
            The value to assign to the validation_mode property of this BodyValidationRequestPolicy.
            Allowed values for this property are: "ENFORCING", "PERMISSIVE", "DISABLED"
        :type validation_mode: str

        """
        self.swagger_types = {
            'required': 'bool',
            'content': 'dict(str, ContentValidation)',
            'validation_mode': 'str'
        }

        self.attribute_map = {
            'required': 'required',
            'content': 'content',
            'validation_mode': 'validationMode'
        }

        self._required = None
        self._content = None
        self._validation_mode = None

    @property
    def required(self):
        """
        Gets the required of this BodyValidationRequestPolicy.
        Determines if the request body is required in the request.


        :return: The required of this BodyValidationRequestPolicy.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this BodyValidationRequestPolicy.
        Determines if the request body is required in the request.


        :param required: The required of this BodyValidationRequestPolicy.
        :type: bool
        """
        self._required = required

    @property
    def content(self):
        """
        **[Required]** Gets the content of this BodyValidationRequestPolicy.
        The content of the request body. The key is a `media type range`__
        subset restricted to the following schema

            key ::= (
                  / (  \"*\" \"/\" \"*\" )
                  / ( type \"/\" \"*\" )
                  / ( type \"/\" subtype )
                  )

        For requests that match multiple keys, only the most specific key is applicable.
        e.g. `text/plain` overrides `text/*`

        __ https://tools.ietf.org/html/rfc7231#appendix-D


        :return: The content of this BodyValidationRequestPolicy.
        :rtype: dict(str, ContentValidation)
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this BodyValidationRequestPolicy.
        The content of the request body. The key is a `media type range`__
        subset restricted to the following schema

            key ::= (
                  / (  \"*\" \"/\" \"*\" )
                  / ( type \"/\" \"*\" )
                  / ( type \"/\" subtype )
                  )

        For requests that match multiple keys, only the most specific key is applicable.
        e.g. `text/plain` overrides `text/*`

        __ https://tools.ietf.org/html/rfc7231#appendix-D


        :param content: The content of this BodyValidationRequestPolicy.
        :type: dict(str, ContentValidation)
        """
        self._content = content

    @property
    def validation_mode(self):
        """
        Gets the validation_mode of this BodyValidationRequestPolicy.
        Validation behavior mode.

        In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
        and not sent to the backend.

        In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
        will follow the normal path.

        `DISABLED` type turns the validation off.

        Allowed values for this property are: "ENFORCING", "PERMISSIVE", "DISABLED"


        :return: The validation_mode of this BodyValidationRequestPolicy.
        :rtype: str
        """
        return self._validation_mode

    @validation_mode.setter
    def validation_mode(self, validation_mode):
        """
        Sets the validation_mode of this BodyValidationRequestPolicy.
        Validation behavior mode.

        In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
        and not sent to the backend.

        In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
        will follow the normal path.

        `DISABLED` type turns the validation off.


        :param validation_mode: The validation_mode of this BodyValidationRequestPolicy.
        :type: str
        """
        allowed_values = ["ENFORCING", "PERMISSIVE", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(validation_mode, allowed_values):
            raise ValueError(
                "Invalid value for `validation_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._validation_mode = validation_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
