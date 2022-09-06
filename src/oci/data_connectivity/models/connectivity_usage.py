# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectivityUsage(object):
    """
    Contains details of ConnectivityUsage.
    """

    #: A constant which can be used with the status property of a ConnectivityUsage.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a ConnectivityUsage.
    #: This constant has a value of "SUCCESS"
    STATUS_SUCCESS = "SUCCESS"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectivityUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this ConnectivityUsage.
            Allowed values for this property are: "FAILED", "SUCCESS"
        :type status: str

        :param error_message:
            The value to assign to the error_message property of this ConnectivityUsage.
        :type error_message: str

        """
        self.swagger_types = {
            'status': 'str',
            'error_message': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'error_message': 'errorMessage'
        }

        self._status = None
        self._error_message = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ConnectivityUsage.
        The status of the usage report/update.

        Allowed values for this property are: "FAILED", "SUCCESS"


        :return: The status of this ConnectivityUsage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ConnectivityUsage.
        The status of the usage report/update.


        :param status: The status of this ConnectivityUsage.
        :type: str
        """
        allowed_values = ["FAILED", "SUCCESS"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this ConnectivityUsage.
        Error message when usage report/update.


        :return: The error_message of this ConnectivityUsage.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ConnectivityUsage.
        Error message when usage report/update.


        :param error_message: The error_message of this ConnectivityUsage.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
