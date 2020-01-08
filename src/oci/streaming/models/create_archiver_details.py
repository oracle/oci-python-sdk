# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateArchiverDetails(object):
    """
    Represents the parameters of the stream archiver.
    """

    #: A constant which can be used with the start_position property of a CreateArchiverDetails.
    #: This constant has a value of "LATEST"
    START_POSITION_LATEST = "LATEST"

    #: A constant which can be used with the start_position property of a CreateArchiverDetails.
    #: This constant has a value of "TRIM_HORIZON"
    START_POSITION_TRIM_HORIZON = "TRIM_HORIZON"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateArchiverDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bucket_name:
            The value to assign to the bucket_name property of this CreateArchiverDetails.
        :type bucket_name: str

        :param use_existing_bucket:
            The value to assign to the use_existing_bucket property of this CreateArchiverDetails.
        :type use_existing_bucket: bool

        :param start_position:
            The value to assign to the start_position property of this CreateArchiverDetails.
            Allowed values for this property are: "LATEST", "TRIM_HORIZON"
        :type start_position: str

        :param batch_rollover_size_in_mbs:
            The value to assign to the batch_rollover_size_in_mbs property of this CreateArchiverDetails.
        :type batch_rollover_size_in_mbs: int

        :param batch_rollover_time_in_seconds:
            The value to assign to the batch_rollover_time_in_seconds property of this CreateArchiverDetails.
        :type batch_rollover_time_in_seconds: int

        """
        self.swagger_types = {
            'bucket_name': 'str',
            'use_existing_bucket': 'bool',
            'start_position': 'str',
            'batch_rollover_size_in_mbs': 'int',
            'batch_rollover_time_in_seconds': 'int'
        }

        self.attribute_map = {
            'bucket_name': 'bucketName',
            'use_existing_bucket': 'useExistingBucket',
            'start_position': 'startPosition',
            'batch_rollover_size_in_mbs': 'batchRolloverSizeInMBs',
            'batch_rollover_time_in_seconds': 'batchRolloverTimeInSeconds'
        }

        self._bucket_name = None
        self._use_existing_bucket = None
        self._start_position = None
        self._batch_rollover_size_in_mbs = None
        self._batch_rollover_time_in_seconds = None

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this CreateArchiverDetails.
        The name of the bucket.


        :return: The bucket_name of this CreateArchiverDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this CreateArchiverDetails.
        The name of the bucket.


        :param bucket_name: The bucket_name of this CreateArchiverDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def use_existing_bucket(self):
        """
        **[Required]** Gets the use_existing_bucket of this CreateArchiverDetails.
        The flag to create a new bucket or use existing one.


        :return: The use_existing_bucket of this CreateArchiverDetails.
        :rtype: bool
        """
        return self._use_existing_bucket

    @use_existing_bucket.setter
    def use_existing_bucket(self, use_existing_bucket):
        """
        Sets the use_existing_bucket of this CreateArchiverDetails.
        The flag to create a new bucket or use existing one.


        :param use_existing_bucket: The use_existing_bucket of this CreateArchiverDetails.
        :type: bool
        """
        self._use_existing_bucket = use_existing_bucket

    @property
    def start_position(self):
        """
        **[Required]** Gets the start_position of this CreateArchiverDetails.
        The start message.

        Allowed values for this property are: "LATEST", "TRIM_HORIZON"


        :return: The start_position of this CreateArchiverDetails.
        :rtype: str
        """
        return self._start_position

    @start_position.setter
    def start_position(self, start_position):
        """
        Sets the start_position of this CreateArchiverDetails.
        The start message.


        :param start_position: The start_position of this CreateArchiverDetails.
        :type: str
        """
        allowed_values = ["LATEST", "TRIM_HORIZON"]
        if not value_allowed_none_or_none_sentinel(start_position, allowed_values):
            raise ValueError(
                "Invalid value for `start_position`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._start_position = start_position

    @property
    def batch_rollover_size_in_mbs(self):
        """
        **[Required]** Gets the batch_rollover_size_in_mbs of this CreateArchiverDetails.
        The batch rollover size in megabytes.


        :return: The batch_rollover_size_in_mbs of this CreateArchiverDetails.
        :rtype: int
        """
        return self._batch_rollover_size_in_mbs

    @batch_rollover_size_in_mbs.setter
    def batch_rollover_size_in_mbs(self, batch_rollover_size_in_mbs):
        """
        Sets the batch_rollover_size_in_mbs of this CreateArchiverDetails.
        The batch rollover size in megabytes.


        :param batch_rollover_size_in_mbs: The batch_rollover_size_in_mbs of this CreateArchiverDetails.
        :type: int
        """
        self._batch_rollover_size_in_mbs = batch_rollover_size_in_mbs

    @property
    def batch_rollover_time_in_seconds(self):
        """
        **[Required]** Gets the batch_rollover_time_in_seconds of this CreateArchiverDetails.
        The rollover time in seconds.


        :return: The batch_rollover_time_in_seconds of this CreateArchiverDetails.
        :rtype: int
        """
        return self._batch_rollover_time_in_seconds

    @batch_rollover_time_in_seconds.setter
    def batch_rollover_time_in_seconds(self, batch_rollover_time_in_seconds):
        """
        Sets the batch_rollover_time_in_seconds of this CreateArchiverDetails.
        The rollover time in seconds.


        :param batch_rollover_time_in_seconds: The batch_rollover_time_in_seconds of this CreateArchiverDetails.
        :type: int
        """
        self._batch_rollover_time_in_seconds = batch_rollover_time_in_seconds

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
