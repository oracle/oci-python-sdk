# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobLogSummary(object):
    """
    A list of job execution logs.
    A job log is an audit log record inserted during the lifecycle of a job execution instance.
    There can be one or more logs for an execution instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobLogSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobLogSummary.
        :type key: str

        :param job_execution_key:
            The value to assign to the job_execution_key property of this JobLogSummary.
        :type job_execution_key: str

        :param uri:
            The value to assign to the uri property of this JobLogSummary.
        :type uri: str

        :param time_created:
            The value to assign to the time_created property of this JobLogSummary.
        :type time_created: datetime

        :param severity:
            The value to assign to the severity property of this JobLogSummary.
        :type severity: str

        :param log_message:
            The value to assign to the log_message property of this JobLogSummary.
        :type log_message: str

        """
        self.swagger_types = {
            'key': 'str',
            'job_execution_key': 'str',
            'uri': 'str',
            'time_created': 'datetime',
            'severity': 'str',
            'log_message': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'job_execution_key': 'jobExecutionKey',
            'uri': 'uri',
            'time_created': 'timeCreated',
            'severity': 'severity',
            'log_message': 'logMessage'
        }

        self._key = None
        self._job_execution_key = None
        self._uri = None
        self._time_created = None
        self._severity = None
        self._log_message = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobLogSummary.
        Unique key of the job log that is immutable.


        :return: The key of this JobLogSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobLogSummary.
        Unique key of the job log that is immutable.


        :param key: The key of this JobLogSummary.
        :type: str
        """
        self._key = key

    @property
    def job_execution_key(self):
        """
        Gets the job_execution_key of this JobLogSummary.
        The unique key of the parent job execution for which the log resource was created.


        :return: The job_execution_key of this JobLogSummary.
        :rtype: str
        """
        return self._job_execution_key

    @job_execution_key.setter
    def job_execution_key(self, job_execution_key):
        """
        Sets the job_execution_key of this JobLogSummary.
        The unique key of the parent job execution for which the log resource was created.


        :param job_execution_key: The job_execution_key of this JobLogSummary.
        :type: str
        """
        self._job_execution_key = job_execution_key

    @property
    def uri(self):
        """
        Gets the uri of this JobLogSummary.
        URI to the job log instance in the API.


        :return: The uri of this JobLogSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobLogSummary.
        URI to the job log instance in the API.


        :param uri: The uri of this JobLogSummary.
        :type: str
        """
        self._uri = uri

    @property
    def time_created(self):
        """
        Gets the time_created of this JobLogSummary.
        The date and time the job log was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobLogSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobLogSummary.
        The date and time the job log was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobLogSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def severity(self):
        """
        Gets the severity of this JobLogSummary.
        Severity level for this log.


        :return: The severity of this JobLogSummary.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this JobLogSummary.
        Severity level for this log.


        :param severity: The severity of this JobLogSummary.
        :type: str
        """
        self._severity = severity

    @property
    def log_message(self):
        """
        Gets the log_message of this JobLogSummary.
        Message for this job log.


        :return: The log_message of this JobLogSummary.
        :rtype: str
        """
        return self._log_message

    @log_message.setter
    def log_message(self, log_message):
        """
        Sets the log_message of this JobLogSummary.
        Message for this job log.


        :param log_message: The log_message of this JobLogSummary.
        :type: str
        """
        self._log_message = log_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
