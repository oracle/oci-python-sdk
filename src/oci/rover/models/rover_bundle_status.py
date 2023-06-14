# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverBundleStatus(object):
    """
    The status of the rover bundle status by a specified work request id.
    """

    #: A constant which can be used with the status property of a RoverBundleStatus.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a RoverBundleStatus.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a RoverBundleStatus.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a RoverBundleStatus.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a RoverBundleStatus.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a RoverBundleStatus.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new RoverBundleStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this RoverBundleStatus.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "COMPLETED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param percent_complete:
            The value to assign to the percent_complete property of this RoverBundleStatus.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this RoverBundleStatus.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this RoverBundleStatus.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this RoverBundleStatus.
        :type time_finished: datetime

        :param bundle_name:
            The value to assign to the bundle_name property of this RoverBundleStatus.
        :type bundle_name: str

        :param error_message:
            The value to assign to the error_message property of this RoverBundleStatus.
        :type error_message: str

        """
        self.swagger_types = {
            'status': 'str',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'bundle_name': 'str',
            'error_message': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'bundle_name': 'bundleName',
            'error_message': 'errorMessage'
        }

        self._status = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._bundle_name = None
        self._error_message = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this RoverBundleStatus.
        The progress of the workflow.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "COMPLETED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RoverBundleStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RoverBundleStatus.
        The progress of the workflow.


        :param status: The status of this RoverBundleStatus.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "COMPLETED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this RoverBundleStatus.
        Percentage of the work request completed.


        :return: The percent_complete of this RoverBundleStatus.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this RoverBundleStatus.
        Percentage of the work request completed.


        :param percent_complete: The percent_complete of this RoverBundleStatus.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this RoverBundleStatus.
        The date and time the work request was created. An RFC3339 formatted datetime string.


        :return: The time_accepted of this RoverBundleStatus.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this RoverBundleStatus.
        The date and time the work request was created. An RFC3339 formatted datetime string.


        :param time_accepted: The time_accepted of this RoverBundleStatus.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this RoverBundleStatus.
        The date and time the work request was started. An RFC3339 formatted datetime string.


        :return: The time_started of this RoverBundleStatus.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this RoverBundleStatus.
        The date and time the work request was started. An RFC3339 formatted datetime string.


        :param time_started: The time_started of this RoverBundleStatus.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this RoverBundleStatus.
        The date and time the work request was finished. An RFC3339 formatted datetime string.


        :return: The time_finished of this RoverBundleStatus.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this RoverBundleStatus.
        The date and time the work request was finished. An RFC3339 formatted datetime string.


        :param time_finished: The time_finished of this RoverBundleStatus.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def bundle_name(self):
        """
        Gets the bundle_name of this RoverBundleStatus.
        The full name of the bundle.


        :return: The bundle_name of this RoverBundleStatus.
        :rtype: str
        """
        return self._bundle_name

    @bundle_name.setter
    def bundle_name(self, bundle_name):
        """
        Sets the bundle_name of this RoverBundleStatus.
        The full name of the bundle.


        :param bundle_name: The bundle_name of this RoverBundleStatus.
        :type: str
        """
        self._bundle_name = bundle_name

    @property
    def error_message(self):
        """
        Gets the error_message of this RoverBundleStatus.
        The error message if work request fails.


        :return: The error_message of this RoverBundleStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this RoverBundleStatus.
        The error message if work request fails.


        :param error_message: The error_message of this RoverBundleStatus.
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
