# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryMirrorRecord(object):
    """
    Object containing information about a mirror record.
    """

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecord.
    #: This constant has a value of "NONE"
    MIRROR_STATUS_NONE = "NONE"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecord.
    #: This constant has a value of "QUEUED"
    MIRROR_STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecord.
    #: This constant has a value of "RUNNING"
    MIRROR_STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecord.
    #: This constant has a value of "PASSED"
    MIRROR_STATUS_PASSED = "PASSED"

    #: A constant which can be used with the mirror_status property of a RepositoryMirrorRecord.
    #: This constant has a value of "FAILED"
    MIRROR_STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryMirrorRecord object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mirror_status:
            The value to assign to the mirror_status property of this RepositoryMirrorRecord.
            Allowed values for this property are: "NONE", "QUEUED", "RUNNING", "PASSED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mirror_status: str

        :param work_request_id:
            The value to assign to the work_request_id property of this RepositoryMirrorRecord.
        :type work_request_id: str

        :param time_enqueued:
            The value to assign to the time_enqueued property of this RepositoryMirrorRecord.
        :type time_enqueued: datetime

        :param time_started:
            The value to assign to the time_started property of this RepositoryMirrorRecord.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this RepositoryMirrorRecord.
        :type time_ended: datetime

        """
        self.swagger_types = {
            'mirror_status': 'str',
            'work_request_id': 'str',
            'time_enqueued': 'datetime',
            'time_started': 'datetime',
            'time_ended': 'datetime'
        }

        self.attribute_map = {
            'mirror_status': 'mirrorStatus',
            'work_request_id': 'workRequestId',
            'time_enqueued': 'timeEnqueued',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded'
        }

        self._mirror_status = None
        self._work_request_id = None
        self._time_enqueued = None
        self._time_started = None
        self._time_ended = None

    @property
    def mirror_status(self):
        """
        **[Required]** Gets the mirror_status of this RepositoryMirrorRecord.
        Mirror status of current mirror entry.
        QUEUED - Mirroring Queued
        RUNNING - Mirroring is Running
        PASSED - Mirroring Passed
        FAILED - Mirroring Failed

        Allowed values for this property are: "NONE", "QUEUED", "RUNNING", "PASSED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mirror_status of this RepositoryMirrorRecord.
        :rtype: str
        """
        return self._mirror_status

    @mirror_status.setter
    def mirror_status(self, mirror_status):
        """
        Sets the mirror_status of this RepositoryMirrorRecord.
        Mirror status of current mirror entry.
        QUEUED - Mirroring Queued
        RUNNING - Mirroring is Running
        PASSED - Mirroring Passed
        FAILED - Mirroring Failed


        :param mirror_status: The mirror_status of this RepositoryMirrorRecord.
        :type: str
        """
        allowed_values = ["NONE", "QUEUED", "RUNNING", "PASSED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(mirror_status, allowed_values):
            mirror_status = 'UNKNOWN_ENUM_VALUE'
        self._mirror_status = mirror_status

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this RepositoryMirrorRecord.
        Workrequest ID to track current mirror operation.


        :return: The work_request_id of this RepositoryMirrorRecord.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this RepositoryMirrorRecord.
        Workrequest ID to track current mirror operation.


        :param work_request_id: The work_request_id of this RepositoryMirrorRecord.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def time_enqueued(self):
        """
        Gets the time_enqueued of this RepositoryMirrorRecord.
        The time to enqueue a mirror operation.


        :return: The time_enqueued of this RepositoryMirrorRecord.
        :rtype: datetime
        """
        return self._time_enqueued

    @time_enqueued.setter
    def time_enqueued(self, time_enqueued):
        """
        Sets the time_enqueued of this RepositoryMirrorRecord.
        The time to enqueue a mirror operation.


        :param time_enqueued: The time_enqueued of this RepositoryMirrorRecord.
        :type: datetime
        """
        self._time_enqueued = time_enqueued

    @property
    def time_started(self):
        """
        Gets the time_started of this RepositoryMirrorRecord.
        The time to start a mirror operation.


        :return: The time_started of this RepositoryMirrorRecord.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this RepositoryMirrorRecord.
        The time to start a mirror operation.


        :param time_started: The time_started of this RepositoryMirrorRecord.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this RepositoryMirrorRecord.
        The time taken to complete a mirror operation. Value is null if not completed.


        :return: The time_ended of this RepositoryMirrorRecord.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this RepositoryMirrorRecord.
        The time taken to complete a mirror operation. Value is null if not completed.


        :param time_ended: The time_ended of this RepositoryMirrorRecord.
        :type: datetime
        """
        self._time_ended = time_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
