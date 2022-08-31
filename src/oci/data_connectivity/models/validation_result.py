# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValidationResult(object):
    """
    Validation result object for a single data asset.
    """

    #: A constant which can be used with the status property of a ValidationResult.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the status property of a ValidationResult.
    #: This constant has a value of "SUCCESS"
    STATUS_SUCCESS = "SUCCESS"

    def __init__(self, **kwargs):
        """
        Initializes a new ValidationResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param error_msg:
            The value to assign to the error_msg property of this ValidationResult.
        :type error_msg: str

        :param status:
            The value to assign to the status property of this ValidationResult.
            Allowed values for this property are: "ERROR", "SUCCESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'error_msg': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'error_msg': 'errorMsg',
            'status': 'status'
        }

        self._error_msg = None
        self._status = None

    @property
    def error_msg(self):
        """
        Gets the error_msg of this ValidationResult.
        Error text for validation failure.


        :return: The error_msg of this ValidationResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """
        Sets the error_msg of this ValidationResult.
        Error text for validation failure.


        :param error_msg: The error_msg of this ValidationResult.
        :type: str
        """
        self._error_msg = error_msg

    @property
    def status(self):
        """
        Gets the status of this ValidationResult.
        Status of the validation result execution.

        Allowed values for this property are: "ERROR", "SUCCESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ValidationResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ValidationResult.
        Status of the validation result execution.


        :param status: The status of this ValidationResult.
        :type: str
        """
        allowed_values = ["ERROR", "SUCCESS"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
