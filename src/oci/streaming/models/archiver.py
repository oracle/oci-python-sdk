# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Archiver(object):
    """
    Represents the current state of the stream archiver.
    """

    #: A constant which can be used with the lifecycle_state property of a Archiver.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Archiver.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a Archiver.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a Archiver.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_STATE_RUNNING = "RUNNING"

    #: A constant which can be used with the lifecycle_state property of a Archiver.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a Archiver.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the start_position property of a Archiver.
    #: This constant has a value of "LATEST"
    START_POSITION_LATEST = "LATEST"

    #: A constant which can be used with the start_position property of a Archiver.
    #: This constant has a value of "TRIM_HORIZON"
    START_POSITION_TRIM_HORIZON = "TRIM_HORIZON"

    def __init__(self, **kwargs):
        """
        Initializes a new Archiver object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_created:
            The value to assign to the time_created property of this Archiver.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Archiver.
            Allowed values for this property are: "CREATING", "STOPPED", "STARTING", "RUNNING", "STOPPING", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param bucket_name:
            The value to assign to the bucket_name property of this Archiver.
        :type bucket_name: str

        :param use_existing_bucket:
            The value to assign to the use_existing_bucket property of this Archiver.
        :type use_existing_bucket: bool

        :param start_position:
            The value to assign to the start_position property of this Archiver.
            Allowed values for this property are: "LATEST", "TRIM_HORIZON", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type start_position: str

        :param batch_rollover_size_in_mbs:
            The value to assign to the batch_rollover_size_in_mbs property of this Archiver.
        :type batch_rollover_size_in_mbs: int

        :param batch_rollover_time_in_seconds:
            The value to assign to the batch_rollover_time_in_seconds property of this Archiver.
        :type batch_rollover_time_in_seconds: int

        :param error:
            The value to assign to the error property of this Archiver.
        :type error: ArchiverError

        """
        self.swagger_types = {
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'bucket_name': 'str',
            'use_existing_bucket': 'bool',
            'start_position': 'str',
            'batch_rollover_size_in_mbs': 'int',
            'batch_rollover_time_in_seconds': 'int',
            'error': 'ArchiverError'
        }

        self.attribute_map = {
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'bucket_name': 'bucketName',
            'use_existing_bucket': 'useExistingBucket',
            'start_position': 'startPosition',
            'batch_rollover_size_in_mbs': 'batchRolloverSizeInMBs',
            'batch_rollover_time_in_seconds': 'batchRolloverTimeInSeconds',
            'error': 'error'
        }

        self._time_created = None
        self._lifecycle_state = None
        self._bucket_name = None
        self._use_existing_bucket = None
        self._start_position = None
        self._batch_rollover_size_in_mbs = None
        self._batch_rollover_time_in_seconds = None
        self._error = None

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Archiver.
        Time when the resource was created.


        :return: The time_created of this Archiver.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Archiver.
        Time when the resource was created.


        :param time_created: The time_created of this Archiver.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Archiver.
        The state of the stream archiver.

        Allowed values for this property are: "CREATING", "STOPPED", "STARTING", "RUNNING", "STOPPING", "UPDATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Archiver.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Archiver.
        The state of the stream archiver.


        :param lifecycle_state: The lifecycle_state of this Archiver.
        :type: str
        """
        allowed_values = ["CREATING", "STOPPED", "STARTING", "RUNNING", "STOPPING", "UPDATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this Archiver.
        The name of the bucket.


        :return: The bucket_name of this Archiver.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this Archiver.
        The name of the bucket.


        :param bucket_name: The bucket_name of this Archiver.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def use_existing_bucket(self):
        """
        Gets the use_existing_bucket of this Archiver.
        The flag to create a new bucket or use existing one.


        :return: The use_existing_bucket of this Archiver.
        :rtype: bool
        """
        return self._use_existing_bucket

    @use_existing_bucket.setter
    def use_existing_bucket(self, use_existing_bucket):
        """
        Sets the use_existing_bucket of this Archiver.
        The flag to create a new bucket or use existing one.


        :param use_existing_bucket: The use_existing_bucket of this Archiver.
        :type: bool
        """
        self._use_existing_bucket = use_existing_bucket

    @property
    def start_position(self):
        """
        Gets the start_position of this Archiver.
        The start message.

        Allowed values for this property are: "LATEST", "TRIM_HORIZON", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The start_position of this Archiver.
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """
        Sets the start_position of this Archiver.
        The start message.


        :param start_position: The start_position of this Archiver.
        :type: str
        """
        allowed_values = ["LATEST", "TRIM_HORIZON"]
        if not value_allowed_none_or_none_sentinel(start_position, allowed_values):
            start_position = 'UNKNOWN_ENUM_VALUE'
        self._start_position = start_position

    @property
    def batch_rollover_size_in_mbs(self):
        """
        Gets the batch_rollover_size_in_mbs of this Archiver.
        The batch rollover size in megabytes.


        :return: The batch_rollover_size_in_mbs of this Archiver.
        :rtype: int
        """
        return self._batch_rollover_size_in_mbs

    @batch_rollover_size_in_mbs.setter
    def batch_rollover_size_in_mbs(self, batch_rollover_size_in_mbs):
        """
        Sets the batch_rollover_size_in_mbs of this Archiver.
        The batch rollover size in megabytes.


        :param batch_rollover_size_in_mbs: The batch_rollover_size_in_mbs of this Archiver.
        :type: int
        """
        self._batch_rollover_size_in_mbs = batch_rollover_size_in_mbs

    @property
    def batch_rollover_time_in_seconds(self):
        """
        Gets the batch_rollover_time_in_seconds of this Archiver.
        The rollover time in seconds.


        :return: The batch_rollover_time_in_seconds of this Archiver.
        :rtype: int
        """
        return self._batch_rollover_time_in_seconds

    @batch_rollover_time_in_seconds.setter
    def batch_rollover_time_in_seconds(self, batch_rollover_time_in_seconds):
        """
        Sets the batch_rollover_time_in_seconds of this Archiver.
        The rollover time in seconds.


        :param batch_rollover_time_in_seconds: The batch_rollover_time_in_seconds of this Archiver.
        :type: int
        """
        self._batch_rollover_time_in_seconds = batch_rollover_time_in_seconds

    @property
    def error(self):
        """
        Gets the error of this Archiver.

        :return: The error of this Archiver.
        :rtype: ArchiverError
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this Archiver.

        :param error: The error of this Archiver.
        :type: ArchiverError
        """
        self._error = error

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
