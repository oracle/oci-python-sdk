# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiscoveryJobLogSummary(object):
    """
    Log of a specific job
    """

    #: A constant which can be used with the log_type property of a DiscoveryJobLogSummary.
    #: This constant has a value of "INFO"
    LOG_TYPE_INFO = "INFO"

    #: A constant which can be used with the log_type property of a DiscoveryJobLogSummary.
    #: This constant has a value of "WARNING"
    LOG_TYPE_WARNING = "WARNING"

    #: A constant which can be used with the log_type property of a DiscoveryJobLogSummary.
    #: This constant has a value of "ERROR"
    LOG_TYPE_ERROR = "ERROR"

    #: A constant which can be used with the log_type property of a DiscoveryJobLogSummary.
    #: This constant has a value of "SUCCESS"
    LOG_TYPE_SUCCESS = "SUCCESS"

    def __init__(self, **kwargs):
        """
        Initializes a new DiscoveryJobLogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DiscoveryJobLogSummary.
        :type id: str

        :param log_type:
            The value to assign to the log_type property of this DiscoveryJobLogSummary.
            Allowed values for this property are: "INFO", "WARNING", "ERROR", "SUCCESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type log_type: str

        :param log_message:
            The value to assign to the log_message property of this DiscoveryJobLogSummary.
        :type log_message: str

        :param time_created:
            The value to assign to the time_created property of this DiscoveryJobLogSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'log_type': 'str',
            'log_message': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'log_type': 'logType',
            'log_message': 'logMessage',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._log_type = None
        self._log_message = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DiscoveryJobLogSummary.
        The OCID of Discovery job


        :return: The id of this DiscoveryJobLogSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DiscoveryJobLogSummary.
        The OCID of Discovery job


        :param id: The id of this DiscoveryJobLogSummary.
        :type: str
        """
        self._id = id

    @property
    def log_type(self):
        """
        **[Required]** Gets the log_type of this DiscoveryJobLogSummary.
        Type of log (INFO, WARNING, ERROR or SUCCESS)

        Allowed values for this property are: "INFO", "WARNING", "ERROR", "SUCCESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The log_type of this DiscoveryJobLogSummary.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """
        Sets the log_type of this DiscoveryJobLogSummary.
        Type of log (INFO, WARNING, ERROR or SUCCESS)


        :param log_type: The log_type of this DiscoveryJobLogSummary.
        :type: str
        """
        allowed_values = ["INFO", "WARNING", "ERROR", "SUCCESS"]
        if not value_allowed_none_or_none_sentinel(log_type, allowed_values):
            log_type = 'UNKNOWN_ENUM_VALUE'
        self._log_type = log_type

    @property
    def log_message(self):
        """
        **[Required]** Gets the log_message of this DiscoveryJobLogSummary.
        Log message


        :return: The log_message of this DiscoveryJobLogSummary.
        :rtype: str
        """
        return self._log_message

    @log_message.setter
    def log_message(self, log_message):
        """
        Sets the log_message of this DiscoveryJobLogSummary.
        Log message


        :param log_message: The log_message of this DiscoveryJobLogSummary.
        :type: str
        """
        self._log_message = log_message

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DiscoveryJobLogSummary.
        Time the Job log was created


        :return: The time_created of this DiscoveryJobLogSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DiscoveryJobLogSummary.
        Time the Job log was created


        :param time_created: The time_created of this DiscoveryJobLogSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
