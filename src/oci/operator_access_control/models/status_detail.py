# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StatusDetail(object):
    """
    Detail of execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StatusDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status_id:
            The value to assign to the status_id property of this StatusDetail.
        :type status_id: int

        :param command_name:
            The value to assign to the command_name property of this StatusDetail.
        :type command_name: str

        :param status:
            The value to assign to the status property of this StatusDetail.
        :type status: str

        :param time_of_validation:
            The value to assign to the time_of_validation property of this StatusDetail.
        :type time_of_validation: datetime

        """
        self.swagger_types = {
            'status_id': 'int',
            'command_name': 'str',
            'status': 'str',
            'time_of_validation': 'datetime'
        }
        self.attribute_map = {
            'status_id': 'statusId',
            'command_name': 'commandName',
            'status': 'status',
            'time_of_validation': 'timeOfValidation'
        }
        self._status_id = None
        self._command_name = None
        self._status = None
        self._time_of_validation = None

    @property
    def status_id(self):
        """
        Gets the status_id of this StatusDetail.
        running unique number of the command executed


        :return: The status_id of this StatusDetail.
        :rtype: int
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """
        Sets the status_id of this StatusDetail.
        running unique number of the command executed


        :param status_id: The status_id of this StatusDetail.
        :type: int
        """
        self._status_id = status_id

    @property
    def command_name(self):
        """
        Gets the command_name of this StatusDetail.
        Name of the process or command executed.


        :return: The command_name of this StatusDetail.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """
        Sets the command_name of this StatusDetail.
        Name of the process or command executed.


        :param command_name: The command_name of this StatusDetail.
        :type: str
        """
        self._command_name = command_name

    @property
    def status(self):
        """
        Gets the status of this StatusDetail.
        Status of the process or command executed Success or Failure.


        :return: The status of this StatusDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StatusDetail.
        Status of the process or command executed Success or Failure.


        :param status: The status of this StatusDetail.
        :type: str
        """
        self._status = status

    @property
    def time_of_validation(self):
        """
        Gets the time_of_validation of this StatusDetail.
        Time when the execution happened in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_validation of this StatusDetail.
        :rtype: datetime
        """
        return self._time_of_validation

    @time_of_validation.setter
    def time_of_validation(self, time_of_validation):
        """
        Sets the time_of_validation of this StatusDetail.
        Time when the execution happened in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'.

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_validation: The time_of_validation of this StatusDetail.
        :type: datetime
        """
        self._time_of_validation = time_of_validation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
