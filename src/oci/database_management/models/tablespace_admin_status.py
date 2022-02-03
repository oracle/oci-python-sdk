# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TablespaceAdminStatus(object):
    """
    The status of a tablespace admin action.
    """

    #: A constant which can be used with the status property of a TablespaceAdminStatus.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a TablespaceAdminStatus.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new TablespaceAdminStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this TablespaceAdminStatus.
            Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param error_code:
            The value to assign to the error_code property of this TablespaceAdminStatus.
        :type error_code: int

        :param error_message:
            The value to assign to the error_message property of this TablespaceAdminStatus.
        :type error_message: str

        """
        self.swagger_types = {
            'status': 'str',
            'error_code': 'int',
            'error_message': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'error_code': 'errorCode',
            'error_message': 'errorMessage'
        }

        self._status = None
        self._error_code = None
        self._error_message = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this TablespaceAdminStatus.
        The status of a tablespace admin action.

        Allowed values for this property are: "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this TablespaceAdminStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TablespaceAdminStatus.
        The status of a tablespace admin action.


        :param status: The status of this TablespaceAdminStatus.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def error_code(self):
        """
        Gets the error_code of this TablespaceAdminStatus.
        The error code that denotes failure if the tablespace admin action is not successful. The error code is \"null\" if the admin action is successful.


        :return: The error_code of this TablespaceAdminStatus.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this TablespaceAdminStatus.
        The error code that denotes failure if the tablespace admin action is not successful. The error code is \"null\" if the admin action is successful.


        :param error_code: The error_code of this TablespaceAdminStatus.
        :type: int
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this TablespaceAdminStatus.
        The error message that indicates the reason for failure if the tablespace admin action is not successful. The error message is \"null\" if the admin action is successful.


        :return: The error_message of this TablespaceAdminStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this TablespaceAdminStatus.
        The error message that indicates the reason for failure if the tablespace admin action is not successful. The error message is \"null\" if the admin action is successful.


        :param error_message: The error_message of this TablespaceAdminStatus.
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
