# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190501


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryParameterValidationRequestPolicy(object):
    """
    Validate the URL query parameters on the incoming API requests on a specific route.
    """

    #: A constant which can be used with the validation_mode property of a QueryParameterValidationRequestPolicy.
    #: This constant has a value of "ENFORCING"
    VALIDATION_MODE_ENFORCING = "ENFORCING"

    #: A constant which can be used with the validation_mode property of a QueryParameterValidationRequestPolicy.
    #: This constant has a value of "PERMISSIVE"
    VALIDATION_MODE_PERMISSIVE = "PERMISSIVE"

    #: A constant which can be used with the validation_mode property of a QueryParameterValidationRequestPolicy.
    #: This constant has a value of "DISABLED"
    VALIDATION_MODE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new QueryParameterValidationRequestPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parameters:
            The value to assign to the parameters property of this QueryParameterValidationRequestPolicy.
        :type parameters: list[oci.apigateway.models.QueryParameterValidationItem]

        :param validation_mode:
            The value to assign to the validation_mode property of this QueryParameterValidationRequestPolicy.
            Allowed values for this property are: "ENFORCING", "PERMISSIVE", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type validation_mode: str

        """
        self.swagger_types = {
            'parameters': 'list[QueryParameterValidationItem]',
            'validation_mode': 'str'
        }
        self.attribute_map = {
            'parameters': 'parameters',
            'validation_mode': 'validationMode'
        }
        self._parameters = None
        self._validation_mode = None

    @property
    def parameters(self):
        """
        Gets the parameters of this QueryParameterValidationRequestPolicy.

        :return: The parameters of this QueryParameterValidationRequestPolicy.
        :rtype: list[oci.apigateway.models.QueryParameterValidationItem]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this QueryParameterValidationRequestPolicy.

        :param parameters: The parameters of this QueryParameterValidationRequestPolicy.
        :type: list[oci.apigateway.models.QueryParameterValidationItem]
        """
        self._parameters = parameters

    @property
    def validation_mode(self):
        """
        Gets the validation_mode of this QueryParameterValidationRequestPolicy.
        Validation behavior mode.

        In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
        and not sent to the backend.

        In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
        will follow the normal path.

        `DISABLED` type turns the validation off.

        Allowed values for this property are: "ENFORCING", "PERMISSIVE", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The validation_mode of this QueryParameterValidationRequestPolicy.
        :rtype: str
        """
        return self._validation_mode

    @validation_mode.setter
    def validation_mode(self, validation_mode):
        """
        Sets the validation_mode of this QueryParameterValidationRequestPolicy.
        Validation behavior mode.

        In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
        and not sent to the backend.

        In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
        will follow the normal path.

        `DISABLED` type turns the validation off.


        :param validation_mode: The validation_mode of this QueryParameterValidationRequestPolicy.
        :type: str
        """
        allowed_values = ["ENFORCING", "PERMISSIVE", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(validation_mode, allowed_values):
            validation_mode = 'UNKNOWN_ENUM_VALUE'
        self._validation_mode = validation_mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
