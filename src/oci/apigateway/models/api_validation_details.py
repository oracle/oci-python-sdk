# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiValidationDetails(object):
    """
    Detail of an error or warning.
    """

    #: A constant which can be used with the result property of a ApiValidationDetails.
    #: This constant has a value of "ERROR"
    RESULT_ERROR = "ERROR"

    #: A constant which can be used with the result property of a ApiValidationDetails.
    #: This constant has a value of "WARNING"
    RESULT_WARNING = "WARNING"

    #: A constant which can be used with the result property of a ApiValidationDetails.
    #: This constant has a value of "OK"
    RESULT_OK = "OK"

    #: A constant which can be used with the result property of a ApiValidationDetails.
    #: This constant has a value of "FAILED"
    RESULT_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApiValidationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param details:
            The value to assign to the details property of this ApiValidationDetails.
        :type details: list[oci.apigateway.models.ApiValidationDetail]

        :param name:
            The value to assign to the name property of this ApiValidationDetails.
        :type name: str

        :param result:
            The value to assign to the result property of this ApiValidationDetails.
            Allowed values for this property are: "ERROR", "WARNING", "OK", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type result: str

        """
        self.swagger_types = {
            'details': 'list[ApiValidationDetail]',
            'name': 'str',
            'result': 'str'
        }

        self.attribute_map = {
            'details': 'details',
            'name': 'name',
            'result': 'result'
        }

        self._details = None
        self._name = None
        self._result = None

    @property
    def details(self):
        """
        Gets the details of this ApiValidationDetails.
        Details of validation.


        :return: The details of this ApiValidationDetails.
        :rtype: list[oci.apigateway.models.ApiValidationDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this ApiValidationDetails.
        Details of validation.


        :param details: The details of this ApiValidationDetails.
        :type: list[oci.apigateway.models.ApiValidationDetail]
        """
        self._details = details

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ApiValidationDetails.
        Name of the validation.


        :return: The name of this ApiValidationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiValidationDetails.
        Name of the validation.


        :param name: The name of this ApiValidationDetails.
        :type: str
        """
        self._name = name

    @property
    def result(self):
        """
        **[Required]** Gets the result of this ApiValidationDetails.
        Result of the validation.

        Allowed values for this property are: "ERROR", "WARNING", "OK", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The result of this ApiValidationDetails.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this ApiValidationDetails.
        Result of the validation.


        :param result: The result of this ApiValidationDetails.
        :type: str
        """
        allowed_values = ["ERROR", "WARNING", "OK", "FAILED"]
        if not value_allowed_none_or_none_sentinel(result, allowed_values):
            result = 'UNKNOWN_ENUM_VALUE'
        self._result = result

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
