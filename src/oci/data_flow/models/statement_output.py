# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StatementOutput(object):
    """
    The execution output of a statement.
    """

    #: A constant which can be used with the status property of a StatementOutput.
    #: This constant has a value of "OK"
    STATUS_OK = "OK"

    #: A constant which can be used with the status property of a StatementOutput.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new StatementOutput object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data:
            The value to assign to the data property of this StatementOutput.
        :type data: oci.data_flow.models.StatementOutputData

        :param status:
            The value to assign to the status property of this StatementOutput.
            Allowed values for this property are: "OK", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param error_name:
            The value to assign to the error_name property of this StatementOutput.
        :type error_name: str

        :param error_value:
            The value to assign to the error_value property of this StatementOutput.
        :type error_value: str

        :param traceback:
            The value to assign to the traceback property of this StatementOutput.
        :type traceback: list[str]

        """
        self.swagger_types = {
            'data': 'StatementOutputData',
            'status': 'str',
            'error_name': 'str',
            'error_value': 'str',
            'traceback': 'list[str]'
        }

        self.attribute_map = {
            'data': 'data',
            'status': 'status',
            'error_name': 'errorName',
            'error_value': 'errorValue',
            'traceback': 'traceback'
        }

        self._data = None
        self._status = None
        self._error_name = None
        self._error_value = None
        self._traceback = None

    @property
    def data(self):
        """
        Gets the data of this StatementOutput.

        :return: The data of this StatementOutput.
        :rtype: oci.data_flow.models.StatementOutputData
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this StatementOutput.

        :param data: The data of this StatementOutput.
        :type: oci.data_flow.models.StatementOutputData
        """
        self._data = data

    @property
    def status(self):
        """
        Gets the status of this StatementOutput.
        Status of the statement output.

        Allowed values for this property are: "OK", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this StatementOutput.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StatementOutput.
        Status of the statement output.


        :param status: The status of this StatementOutput.
        :type: str
        """
        allowed_values = ["OK", "ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def error_name(self):
        """
        Gets the error_name of this StatementOutput.
        The name of the error in the statement output.


        :return: The error_name of this StatementOutput.
        :rtype: str
        """
        return self._error_name

    @error_name.setter
    def error_name(self, error_name):
        """
        Sets the error_name of this StatementOutput.
        The name of the error in the statement output.


        :param error_name: The error_name of this StatementOutput.
        :type: str
        """
        self._error_name = error_name

    @property
    def error_value(self):
        """
        Gets the error_value of this StatementOutput.
        The value of the error in the statement output.


        :return: The error_value of this StatementOutput.
        :rtype: str
        """
        return self._error_value

    @error_value.setter
    def error_value(self, error_value):
        """
        Sets the error_value of this StatementOutput.
        The value of the error in the statement output.


        :param error_value: The error_value of this StatementOutput.
        :type: str
        """
        self._error_value = error_value

    @property
    def traceback(self):
        """
        Gets the traceback of this StatementOutput.
        The traceback of the statement output.


        :return: The traceback of this StatementOutput.
        :rtype: list[str]
        """
        return self._traceback

    @traceback.setter
    def traceback(self, traceback):
        """
        Sets the traceback of this StatementOutput.
        The traceback of the statement output.


        :param traceback: The traceback of this StatementOutput.
        :type: list[str]
        """
        self._traceback = traceback

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
