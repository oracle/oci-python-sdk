# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .validation_failure_policy import ValidationFailurePolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifyResponseValidationFailurePolicy(ValidationFailurePolicy):
    """
    Policy to specify how to modify the response code, body and headers.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModifyResponseValidationFailurePolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.ModifyResponseValidationFailurePolicy.type` attribute
        of this class is ``MODIFY_RESPONSE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ModifyResponseValidationFailurePolicy.
            Allowed values for this property are: "MODIFY_RESPONSE"
        :type type: str

        :param response_code:
            The value to assign to the response_code property of this ModifyResponseValidationFailurePolicy.
        :type response_code: str

        :param response_message:
            The value to assign to the response_message property of this ModifyResponseValidationFailurePolicy.
        :type response_message: str

        :param response_header_transformations:
            The value to assign to the response_header_transformations property of this ModifyResponseValidationFailurePolicy.
        :type response_header_transformations: oci.apigateway.models.HeaderTransformationPolicy

        """
        self.swagger_types = {
            'type': 'str',
            'response_code': 'str',
            'response_message': 'str',
            'response_header_transformations': 'HeaderTransformationPolicy'
        }

        self.attribute_map = {
            'type': 'type',
            'response_code': 'responseCode',
            'response_message': 'responseMessage',
            'response_header_transformations': 'responseHeaderTransformations'
        }

        self._type = None
        self._response_code = None
        self._response_message = None
        self._response_header_transformations = None
        self._type = 'MODIFY_RESPONSE'

    @property
    def response_code(self):
        """
        Gets the response_code of this ModifyResponseValidationFailurePolicy.
        HTTP response code, can include context variables.


        :return: The response_code of this ModifyResponseValidationFailurePolicy.
        :rtype: str
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """
        Sets the response_code of this ModifyResponseValidationFailurePolicy.
        HTTP response code, can include context variables.


        :param response_code: The response_code of this ModifyResponseValidationFailurePolicy.
        :type: str
        """
        self._response_code = response_code

    @property
    def response_message(self):
        """
        Gets the response_message of this ModifyResponseValidationFailurePolicy.
        HTTP response message.


        :return: The response_message of this ModifyResponseValidationFailurePolicy.
        :rtype: str
        """
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        """
        Sets the response_message of this ModifyResponseValidationFailurePolicy.
        HTTP response message.


        :param response_message: The response_message of this ModifyResponseValidationFailurePolicy.
        :type: str
        """
        self._response_message = response_message

    @property
    def response_header_transformations(self):
        """
        Gets the response_header_transformations of this ModifyResponseValidationFailurePolicy.

        :return: The response_header_transformations of this ModifyResponseValidationFailurePolicy.
        :rtype: oci.apigateway.models.HeaderTransformationPolicy
        """
        return self._response_header_transformations

    @response_header_transformations.setter
    def response_header_transformations(self, response_header_transformations):
        """
        Sets the response_header_transformations of this ModifyResponseValidationFailurePolicy.

        :param response_header_transformations: The response_header_transformations of this ModifyResponseValidationFailurePolicy.
        :type: oci.apigateway.models.HeaderTransformationPolicy
        """
        self._response_header_transformations = response_header_transformations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
