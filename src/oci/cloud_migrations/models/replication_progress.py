# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReplicationProgress(object):
    """
    Progress of a migration asset's replication process.
    """

    #: A constant which can be used with the status property of a ReplicationProgress.
    #: This constant has a value of "NONE"
    STATUS_NONE = "NONE"

    #: A constant which can be used with the status property of a ReplicationProgress.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the last_replication_status property of a ReplicationProgress.
    #: This constant has a value of "NONE"
    LAST_REPLICATION_STATUS_NONE = "NONE"

    #: A constant which can be used with the last_replication_status property of a ReplicationProgress.
    #: This constant has a value of "COMPLETED"
    LAST_REPLICATION_STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the last_replication_status property of a ReplicationProgress.
    #: This constant has a value of "FAILED"
    LAST_REPLICATION_STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ReplicationProgress object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param percentage:
            The value to assign to the percentage property of this ReplicationProgress.
        :type percentage: int

        :param status:
            The value to assign to the status property of this ReplicationProgress.
            Allowed values for this property are: "NONE", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_started:
            The value to assign to the time_started property of this ReplicationProgress.
        :type time_started: datetime

        :param time_oflast_replication_start:
            The value to assign to the time_oflast_replication_start property of this ReplicationProgress.
        :type time_oflast_replication_start: datetime

        :param time_of_last_replication_end:
            The value to assign to the time_of_last_replication_end property of this ReplicationProgress.
        :type time_of_last_replication_end: datetime

        :param time_of_last_replication_success:
            The value to assign to the time_of_last_replication_success property of this ReplicationProgress.
        :type time_of_last_replication_success: datetime

        :param last_replication_status:
            The value to assign to the last_replication_status property of this ReplicationProgress.
            Allowed values for this property are: "NONE", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_replication_status: str

        :param last_replication_error:
            The value to assign to the last_replication_error property of this ReplicationProgress.
        :type last_replication_error: str

        """
        self.swagger_types = {
            'percentage': 'int',
            'status': 'str',
            'time_started': 'datetime',
            'time_oflast_replication_start': 'datetime',
            'time_of_last_replication_end': 'datetime',
            'time_of_last_replication_success': 'datetime',
            'last_replication_status': 'str',
            'last_replication_error': 'str'
        }

        self.attribute_map = {
            'percentage': 'percentage',
            'status': 'status',
            'time_started': 'timeStarted',
            'time_oflast_replication_start': 'timeOflastReplicationStart',
            'time_of_last_replication_end': 'timeOfLastReplicationEnd',
            'time_of_last_replication_success': 'timeOfLastReplicationSuccess',
            'last_replication_status': 'lastReplicationStatus',
            'last_replication_error': 'lastReplicationError'
        }

        self._percentage = None
        self._status = None
        self._time_started = None
        self._time_oflast_replication_start = None
        self._time_of_last_replication_end = None
        self._time_of_last_replication_success = None
        self._last_replication_status = None
        self._last_replication_error = None

    @property
    def percentage(self):
        """
        **[Required]** Gets the percentage of this ReplicationProgress.
        Percentage of the current replication progress from 0 to 100.


        :return: The percentage of this ReplicationProgress.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this ReplicationProgress.
        Percentage of the current replication progress from 0 to 100.


        :param percentage: The percentage of this ReplicationProgress.
        :type: int
        """
        self._percentage = percentage

    @property
    def status(self):
        """
        Gets the status of this ReplicationProgress.
        Status of the current replication progress. It can be None or InProgress.

        Allowed values for this property are: "NONE", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ReplicationProgress.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ReplicationProgress.
        Status of the current replication progress. It can be None or InProgress.


        :param status: The status of this ReplicationProgress.
        :type: str
        """
        allowed_values = ["NONE", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_started(self):
        """
        Gets the time_started of this ReplicationProgress.
        Start time of the current replication process


        :return: The time_started of this ReplicationProgress.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this ReplicationProgress.
        Start time of the current replication process


        :param time_started: The time_started of this ReplicationProgress.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_oflast_replication_start(self):
        """
        Gets the time_oflast_replication_start of this ReplicationProgress.
        Start time of the last replication process. It can be Completed or Failed.


        :return: The time_oflast_replication_start of this ReplicationProgress.
        :rtype: datetime
        """
        return self._time_oflast_replication_start

    @time_oflast_replication_start.setter
    def time_oflast_replication_start(self, time_oflast_replication_start):
        """
        Sets the time_oflast_replication_start of this ReplicationProgress.
        Start time of the last replication process. It can be Completed or Failed.


        :param time_oflast_replication_start: The time_oflast_replication_start of this ReplicationProgress.
        :type: datetime
        """
        self._time_oflast_replication_start = time_oflast_replication_start

    @property
    def time_of_last_replication_end(self):
        """
        Gets the time_of_last_replication_end of this ReplicationProgress.
        End time of the last replication process. It can be Completed or Failed.


        :return: The time_of_last_replication_end of this ReplicationProgress.
        :rtype: datetime
        """
        return self._time_of_last_replication_end

    @time_of_last_replication_end.setter
    def time_of_last_replication_end(self, time_of_last_replication_end):
        """
        Sets the time_of_last_replication_end of this ReplicationProgress.
        End time of the last replication process. It can be Completed or Failed.


        :param time_of_last_replication_end: The time_of_last_replication_end of this ReplicationProgress.
        :type: datetime
        """
        self._time_of_last_replication_end = time_of_last_replication_end

    @property
    def time_of_last_replication_success(self):
        """
        Gets the time_of_last_replication_success of this ReplicationProgress.
        End time of the last successful replication process, which has been completed.


        :return: The time_of_last_replication_success of this ReplicationProgress.
        :rtype: datetime
        """
        return self._time_of_last_replication_success

    @time_of_last_replication_success.setter
    def time_of_last_replication_success(self, time_of_last_replication_success):
        """
        Sets the time_of_last_replication_success of this ReplicationProgress.
        End time of the last successful replication process, which has been completed.


        :param time_of_last_replication_success: The time_of_last_replication_success of this ReplicationProgress.
        :type: datetime
        """
        self._time_of_last_replication_success = time_of_last_replication_success

    @property
    def last_replication_status(self):
        """
        Gets the last_replication_status of this ReplicationProgress.
        Status of the last replication task. It can be Completed or Failed.

        Allowed values for this property are: "NONE", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_replication_status of this ReplicationProgress.
        :rtype: str
        """
        return self._last_replication_status

    @last_replication_status.setter
    def last_replication_status(self, last_replication_status):
        """
        Sets the last_replication_status of this ReplicationProgress.
        Status of the last replication task. It can be Completed or Failed.


        :param last_replication_status: The last_replication_status of this ReplicationProgress.
        :type: str
        """
        allowed_values = ["NONE", "COMPLETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(last_replication_status, allowed_values):
            last_replication_status = 'UNKNOWN_ENUM_VALUE'
        self._last_replication_status = last_replication_status

    @property
    def last_replication_error(self):
        """
        Gets the last_replication_error of this ReplicationProgress.
        Error message if the last finished replication failed.


        :return: The last_replication_error of this ReplicationProgress.
        :rtype: str
        """
        return self._last_replication_error

    @last_replication_error.setter
    def last_replication_error(self, last_replication_error):
        """
        Sets the last_replication_error of this ReplicationProgress.
        Error message if the last finished replication failed.


        :param last_replication_error: The last_replication_error of this ReplicationProgress.
        :type: str
        """
        self._last_replication_error = last_replication_error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
