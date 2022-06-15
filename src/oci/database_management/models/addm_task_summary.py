# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmTaskSummary(object):
    """
    The object containing the ADDM task metadata.
    """

    #: A constant which can be used with the status property of a AddmTaskSummary.
    #: This constant has a value of "INITIAL"
    STATUS_INITIAL = "INITIAL"

    #: A constant which can be used with the status property of a AddmTaskSummary.
    #: This constant has a value of "EXECUTING"
    STATUS_EXECUTING = "EXECUTING"

    #: A constant which can be used with the status property of a AddmTaskSummary.
    #: This constant has a value of "INTERRUPTED"
    STATUS_INTERRUPTED = "INTERRUPTED"

    #: A constant which can be used with the status property of a AddmTaskSummary.
    #: This constant has a value of "COMPLETED"
    STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the status property of a AddmTaskSummary.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the how_created property of a AddmTaskSummary.
    #: This constant has a value of "AUTO"
    HOW_CREATED_AUTO = "AUTO"

    #: A constant which can be used with the how_created property of a AddmTaskSummary.
    #: This constant has a value of "MANUAL"
    HOW_CREATED_MANUAL = "MANUAL"

    def __init__(self, **kwargs):
        """
        Initializes a new AddmTaskSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_name:
            The value to assign to the task_name property of this AddmTaskSummary.
        :type task_name: str

        :param task_id:
            The value to assign to the task_id property of this AddmTaskSummary.
        :type task_id: int

        :param description:
            The value to assign to the description property of this AddmTaskSummary.
        :type description: str

        :param db_user:
            The value to assign to the db_user property of this AddmTaskSummary.
        :type db_user: str

        :param status:
            The value to assign to the status property of this AddmTaskSummary.
            Allowed values for this property are: "INITIAL", "EXECUTING", "INTERRUPTED", "COMPLETED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this AddmTaskSummary.
        :type time_created: datetime

        :param how_created:
            The value to assign to the how_created property of this AddmTaskSummary.
            Allowed values for this property are: "AUTO", "MANUAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type how_created: str

        :param start_snapshot_time:
            The value to assign to the start_snapshot_time property of this AddmTaskSummary.
        :type start_snapshot_time: datetime

        :param end_snapshot_time:
            The value to assign to the end_snapshot_time property of this AddmTaskSummary.
        :type end_snapshot_time: datetime

        :param begin_snapshot_id:
            The value to assign to the begin_snapshot_id property of this AddmTaskSummary.
        :type begin_snapshot_id: int

        :param end_snapshot_id:
            The value to assign to the end_snapshot_id property of this AddmTaskSummary.
        :type end_snapshot_id: int

        :param findings:
            The value to assign to the findings property of this AddmTaskSummary.
        :type findings: int

        """
        self.swagger_types = {
            'task_name': 'str',
            'task_id': 'int',
            'description': 'str',
            'db_user': 'str',
            'status': 'str',
            'time_created': 'datetime',
            'how_created': 'str',
            'start_snapshot_time': 'datetime',
            'end_snapshot_time': 'datetime',
            'begin_snapshot_id': 'int',
            'end_snapshot_id': 'int',
            'findings': 'int'
        }

        self.attribute_map = {
            'task_name': 'taskName',
            'task_id': 'taskId',
            'description': 'description',
            'db_user': 'dbUser',
            'status': 'status',
            'time_created': 'timeCreated',
            'how_created': 'howCreated',
            'start_snapshot_time': 'startSnapshotTime',
            'end_snapshot_time': 'endSnapshotTime',
            'begin_snapshot_id': 'beginSnapshotId',
            'end_snapshot_id': 'endSnapshotId',
            'findings': 'findings'
        }

        self._task_name = None
        self._task_id = None
        self._description = None
        self._db_user = None
        self._status = None
        self._time_created = None
        self._how_created = None
        self._start_snapshot_time = None
        self._end_snapshot_time = None
        self._begin_snapshot_id = None
        self._end_snapshot_id = None
        self._findings = None

    @property
    def task_name(self):
        """
        Gets the task_name of this AddmTaskSummary.
        The name of the ADDM task.


        :return: The task_name of this AddmTaskSummary.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """
        Sets the task_name of this AddmTaskSummary.
        The name of the ADDM task.


        :param task_name: The task_name of this AddmTaskSummary.
        :type: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        """
        **[Required]** Gets the task_id of this AddmTaskSummary.
        The ID number of the ADDM task.


        :return: The task_id of this AddmTaskSummary.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """
        Sets the task_id of this AddmTaskSummary.
        The ID number of the ADDM task.


        :param task_id: The task_id of this AddmTaskSummary.
        :type: int
        """
        self._task_id = task_id

    @property
    def description(self):
        """
        Gets the description of this AddmTaskSummary.
        The description of the ADDM task.


        :return: The description of this AddmTaskSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AddmTaskSummary.
        The description of the ADDM task.


        :param description: The description of this AddmTaskSummary.
        :type: str
        """
        self._description = description

    @property
    def db_user(self):
        """
        Gets the db_user of this AddmTaskSummary.
        The database user who owns the ADDM task.


        :return: The db_user of this AddmTaskSummary.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """
        Sets the db_user of this AddmTaskSummary.
        The database user who owns the ADDM task.


        :param db_user: The db_user of this AddmTaskSummary.
        :type: str
        """
        self._db_user = db_user

    @property
    def status(self):
        """
        Gets the status of this AddmTaskSummary.
        The status of the ADDM task.

        Allowed values for this property are: "INITIAL", "EXECUTING", "INTERRUPTED", "COMPLETED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this AddmTaskSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AddmTaskSummary.
        The status of the ADDM task.


        :param status: The status of this AddmTaskSummary.
        :type: str
        """
        allowed_values = ["INITIAL", "EXECUTING", "INTERRUPTED", "COMPLETED", "ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this AddmTaskSummary.
        The creation date of the ADDM task.


        :return: The time_created of this AddmTaskSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AddmTaskSummary.
        The creation date of the ADDM task.


        :param time_created: The time_created of this AddmTaskSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def how_created(self):
        """
        Gets the how_created of this AddmTaskSummary.
        A description of how the task was created.

        Allowed values for this property are: "AUTO", "MANUAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The how_created of this AddmTaskSummary.
        :rtype: str
        """
        return self._how_created

    @how_created.setter
    def how_created(self, how_created):
        """
        Sets the how_created of this AddmTaskSummary.
        A description of how the task was created.


        :param how_created: The how_created of this AddmTaskSummary.
        :type: str
        """
        allowed_values = ["AUTO", "MANUAL"]
        if not value_allowed_none_or_none_sentinel(how_created, allowed_values):
            how_created = 'UNKNOWN_ENUM_VALUE'
        self._how_created = how_created

    @property
    def start_snapshot_time(self):
        """
        Gets the start_snapshot_time of this AddmTaskSummary.
        The timestamp of the beginning AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.


        :return: The start_snapshot_time of this AddmTaskSummary.
        :rtype: datetime
        """
        return self._start_snapshot_time

    @start_snapshot_time.setter
    def start_snapshot_time(self, start_snapshot_time):
        """
        Sets the start_snapshot_time of this AddmTaskSummary.
        The timestamp of the beginning AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.


        :param start_snapshot_time: The start_snapshot_time of this AddmTaskSummary.
        :type: datetime
        """
        self._start_snapshot_time = start_snapshot_time

    @property
    def end_snapshot_time(self):
        """
        Gets the end_snapshot_time of this AddmTaskSummary.
        The timestamp of the ending AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.


        :return: The end_snapshot_time of this AddmTaskSummary.
        :rtype: datetime
        """
        return self._end_snapshot_time

    @end_snapshot_time.setter
    def end_snapshot_time(self, end_snapshot_time):
        """
        Sets the end_snapshot_time of this AddmTaskSummary.
        The timestamp of the ending AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.


        :param end_snapshot_time: The end_snapshot_time of this AddmTaskSummary.
        :type: datetime
        """
        self._end_snapshot_time = end_snapshot_time

    @property
    def begin_snapshot_id(self):
        """
        Gets the begin_snapshot_id of this AddmTaskSummary.
        The ID number of the beginning AWR snapshot.


        :return: The begin_snapshot_id of this AddmTaskSummary.
        :rtype: int
        """
        return self._begin_snapshot_id

    @begin_snapshot_id.setter
    def begin_snapshot_id(self, begin_snapshot_id):
        """
        Sets the begin_snapshot_id of this AddmTaskSummary.
        The ID number of the beginning AWR snapshot.


        :param begin_snapshot_id: The begin_snapshot_id of this AddmTaskSummary.
        :type: int
        """
        self._begin_snapshot_id = begin_snapshot_id

    @property
    def end_snapshot_id(self):
        """
        Gets the end_snapshot_id of this AddmTaskSummary.
        The ID number of the ending AWR snapshot.


        :return: The end_snapshot_id of this AddmTaskSummary.
        :rtype: int
        """
        return self._end_snapshot_id

    @end_snapshot_id.setter
    def end_snapshot_id(self, end_snapshot_id):
        """
        Sets the end_snapshot_id of this AddmTaskSummary.
        The ID number of the ending AWR snapshot.


        :param end_snapshot_id: The end_snapshot_id of this AddmTaskSummary.
        :type: int
        """
        self._end_snapshot_id = end_snapshot_id

    @property
    def findings(self):
        """
        Gets the findings of this AddmTaskSummary.
        The number of ADDM findings.


        :return: The findings of this AddmTaskSummary.
        :rtype: int
        """
        return self._findings

    @findings.setter
    def findings(self, findings):
        """
        Sets the findings of this AddmTaskSummary.
        The number of ADDM findings.


        :param findings: The findings of this AddmTaskSummary.
        :type: int
        """
        self._findings = findings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
