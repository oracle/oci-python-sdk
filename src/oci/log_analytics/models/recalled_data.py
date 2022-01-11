# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecalledData(object):
    """
    This is the information about recalled data
    """

    #: A constant which can be used with the status property of a RecalledData.
    #: This constant has a value of "RECALLED"
    STATUS_RECALLED = "RECALLED"

    #: A constant which can be used with the status property of a RecalledData.
    #: This constant has a value of "PENDING"
    STATUS_PENDING = "PENDING"

    def __init__(self, **kwargs):
        """
        Initializes a new RecalledData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_data_ended:
            The value to assign to the time_data_ended property of this RecalledData.
        :type time_data_ended: datetime

        :param time_data_started:
            The value to assign to the time_data_started property of this RecalledData.
        :type time_data_started: datetime

        :param time_started:
            The value to assign to the time_started property of this RecalledData.
        :type time_started: datetime

        :param status:
            The value to assign to the status property of this RecalledData.
            Allowed values for this property are: "RECALLED", "PENDING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param recall_count:
            The value to assign to the recall_count property of this RecalledData.
        :type recall_count: int

        :param storage_usage_in_bytes:
            The value to assign to the storage_usage_in_bytes property of this RecalledData.
        :type storage_usage_in_bytes: int

        """
        self.swagger_types = {
            'time_data_ended': 'datetime',
            'time_data_started': 'datetime',
            'time_started': 'datetime',
            'status': 'str',
            'recall_count': 'int',
            'storage_usage_in_bytes': 'int'
        }

        self.attribute_map = {
            'time_data_ended': 'timeDataEnded',
            'time_data_started': 'timeDataStarted',
            'time_started': 'timeStarted',
            'status': 'status',
            'recall_count': 'recallCount',
            'storage_usage_in_bytes': 'storageUsageInBytes'
        }

        self._time_data_ended = None
        self._time_data_started = None
        self._time_started = None
        self._status = None
        self._recall_count = None
        self._storage_usage_in_bytes = None

    @property
    def time_data_ended(self):
        """
        **[Required]** Gets the time_data_ended of this RecalledData.
        This is the end of the time range of the related data


        :return: The time_data_ended of this RecalledData.
        :rtype: datetime
        """
        return self._time_data_ended

    @time_data_ended.setter
    def time_data_ended(self, time_data_ended):
        """
        Sets the time_data_ended of this RecalledData.
        This is the end of the time range of the related data


        :param time_data_ended: The time_data_ended of this RecalledData.
        :type: datetime
        """
        self._time_data_ended = time_data_ended

    @property
    def time_data_started(self):
        """
        **[Required]** Gets the time_data_started of this RecalledData.
        This is the start of the time range of the related data


        :return: The time_data_started of this RecalledData.
        :rtype: datetime
        """
        return self._time_data_started

    @time_data_started.setter
    def time_data_started(self, time_data_started):
        """
        Sets the time_data_started of this RecalledData.
        This is the start of the time range of the related data


        :param time_data_started: The time_data_started of this RecalledData.
        :type: datetime
        """
        self._time_data_started = time_data_started

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this RecalledData.
        This is the time when the first recall operation was started for this RecalledData


        :return: The time_started of this RecalledData.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this RecalledData.
        This is the time when the first recall operation was started for this RecalledData


        :param time_started: The time_started of this RecalledData.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def status(self):
        """
        **[Required]** Gets the status of this RecalledData.
        This is the status of the recall

        Allowed values for this property are: "RECALLED", "PENDING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RecalledData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RecalledData.
        This is the status of the recall


        :param status: The status of this RecalledData.
        :type: str
        """
        allowed_values = ["RECALLED", "PENDING"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def recall_count(self):
        """
        **[Required]** Gets the recall_count of this RecalledData.
        This is the number of recall operations for this recall.  Note one RecalledData can be merged from the results
        of several recall operations if the time duration of the results of the recall operations overlap.


        :return: The recall_count of this RecalledData.
        :rtype: int
        """
        return self._recall_count

    @recall_count.setter
    def recall_count(self, recall_count):
        """
        Sets the recall_count of this RecalledData.
        This is the number of recall operations for this recall.  Note one RecalledData can be merged from the results
        of several recall operations if the time duration of the results of the recall operations overlap.


        :param recall_count: The recall_count of this RecalledData.
        :type: int
        """
        self._recall_count = recall_count

    @property
    def storage_usage_in_bytes(self):
        """
        **[Required]** Gets the storage_usage_in_bytes of this RecalledData.
        This is the size in bytes


        :return: The storage_usage_in_bytes of this RecalledData.
        :rtype: int
        """
        return self._storage_usage_in_bytes

    @storage_usage_in_bytes.setter
    def storage_usage_in_bytes(self, storage_usage_in_bytes):
        """
        Sets the storage_usage_in_bytes of this RecalledData.
        This is the size in bytes


        :param storage_usage_in_bytes: The storage_usage_in_bytes of this RecalledData.
        :type: int
        """
        self._storage_usage_in_bytes = storage_usage_in_bytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
