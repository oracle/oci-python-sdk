# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UploadSummary(object):
    """
    Summary of the Upload.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UploadSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference:
            The value to assign to the reference property of this UploadSummary.
        :type reference: str

        :param name:
            The value to assign to the name property of this UploadSummary.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this UploadSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this UploadSummary.
        :type time_updated: datetime

        :param time_earliest_log_entry:
            The value to assign to the time_earliest_log_entry property of this UploadSummary.
        :type time_earliest_log_entry: datetime

        :param time_latest_log_entry:
            The value to assign to the time_latest_log_entry property of this UploadSummary.
        :type time_latest_log_entry: datetime

        :param warnings_count:
            The value to assign to the warnings_count property of this UploadSummary.
        :type warnings_count: int

        """
        self.swagger_types = {
            'reference': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'time_earliest_log_entry': 'datetime',
            'time_latest_log_entry': 'datetime',
            'warnings_count': 'int'
        }

        self.attribute_map = {
            'reference': 'reference',
            'name': 'name',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'time_earliest_log_entry': 'timeEarliestLogEntry',
            'time_latest_log_entry': 'timeLatestLogEntry',
            'warnings_count': 'warningsCount'
        }

        self._reference = None
        self._name = None
        self._time_created = None
        self._time_updated = None
        self._time_earliest_log_entry = None
        self._time_latest_log_entry = None
        self._warnings_count = None

    @property
    def reference(self):
        """
        **[Required]** Gets the reference of this UploadSummary.
        Unique internal identifier to refer the upload container.


        :return: The reference of this UploadSummary.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this UploadSummary.
        Unique internal identifier to refer the upload container.


        :param reference: The reference of this UploadSummary.
        :type: str
        """
        self._reference = reference

    @property
    def name(self):
        """
        **[Required]** Gets the name of this UploadSummary.
        The name of the upload container.


        :return: The name of this UploadSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UploadSummary.
        The name of the upload container.


        :param name: The name of this UploadSummary.
        :type: str
        """
        self._name = name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this UploadSummary.
        The time when this upload container is created. An RFC3339 formatted datetime string.


        :return: The time_created of this UploadSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UploadSummary.
        The time when this upload container is created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this UploadSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this UploadSummary.
        The latest time when this upload container is modified. An RFC3339 formatted datetime string.


        :return: The time_updated of this UploadSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this UploadSummary.
        The latest time when this upload container is modified. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this UploadSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_earliest_log_entry(self):
        """
        Gets the time_earliest_log_entry of this UploadSummary.
        This time represents the earliest time of the log entry in this container. An RFC3339 formatted datetime string.


        :return: The time_earliest_log_entry of this UploadSummary.
        :rtype: datetime
        """
        return self._time_earliest_log_entry

    @time_earliest_log_entry.setter
    def time_earliest_log_entry(self, time_earliest_log_entry):
        """
        Sets the time_earliest_log_entry of this UploadSummary.
        This time represents the earliest time of the log entry in this container. An RFC3339 formatted datetime string.


        :param time_earliest_log_entry: The time_earliest_log_entry of this UploadSummary.
        :type: datetime
        """
        self._time_earliest_log_entry = time_earliest_log_entry

    @property
    def time_latest_log_entry(self):
        """
        Gets the time_latest_log_entry of this UploadSummary.
        This time represents the latest time of the log entry in this container. An RFC3339 formatted datetime string.


        :return: The time_latest_log_entry of this UploadSummary.
        :rtype: datetime
        """
        return self._time_latest_log_entry

    @time_latest_log_entry.setter
    def time_latest_log_entry(self, time_latest_log_entry):
        """
        Sets the time_latest_log_entry of this UploadSummary.
        This time represents the latest time of the log entry in this container. An RFC3339 formatted datetime string.


        :param time_latest_log_entry: The time_latest_log_entry of this UploadSummary.
        :type: datetime
        """
        self._time_latest_log_entry = time_latest_log_entry

    @property
    def warnings_count(self):
        """
        Gets the warnings_count of this UploadSummary.
        Number of warnings associated to the upload.


        :return: The warnings_count of this UploadSummary.
        :rtype: int
        """
        return self._warnings_count

    @warnings_count.setter
    def warnings_count(self, warnings_count):
        """
        Sets the warnings_count of this UploadSummary.
        Number of warnings associated to the upload.


        :param warnings_count: The warnings_count of this UploadSummary.
        :type: int
        """
        self._warnings_count = warnings_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
