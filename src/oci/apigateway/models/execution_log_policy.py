# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionLogPolicy(object):
    """
    Configures the logging policies for the execution logs of an API Deployment.
    """

    #: A constant which can be used with the log_level property of a ExecutionLogPolicy.
    #: This constant has a value of "INFO"
    LOG_LEVEL_INFO = "INFO"

    #: A constant which can be used with the log_level property of a ExecutionLogPolicy.
    #: This constant has a value of "WARN"
    LOG_LEVEL_WARN = "WARN"

    #: A constant which can be used with the log_level property of a ExecutionLogPolicy.
    #: This constant has a value of "ERROR"
    LOG_LEVEL_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionLogPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this ExecutionLogPolicy.
        :type is_enabled: bool

        :param log_level:
            The value to assign to the log_level property of this ExecutionLogPolicy.
            Allowed values for this property are: "INFO", "WARN", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type log_level: str

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'log_level': 'str'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'log_level': 'logLevel'
        }

        self._is_enabled = None
        self._log_level = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this ExecutionLogPolicy.
        Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.

        Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs
        for an API Deployment. If there is an active log object for the API Deployment and its
        category is set to 'execution' in OCI Logging service, the logs will not be uploaded to the legacy
        OCI Object Storage log archival bucket.

        Please note that the functionality to push to the legacy OCI Object Storage log
        archival bucket has been deprecated and will be removed in the future.


        :return: The is_enabled of this ExecutionLogPolicy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ExecutionLogPolicy.
        Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.

        Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs
        for an API Deployment. If there is an active log object for the API Deployment and its
        category is set to 'execution' in OCI Logging service, the logs will not be uploaded to the legacy
        OCI Object Storage log archival bucket.

        Please note that the functionality to push to the legacy OCI Object Storage log
        archival bucket has been deprecated and will be removed in the future.


        :param is_enabled: The is_enabled of this ExecutionLogPolicy.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def log_level(self):
        """
        Gets the log_level of this ExecutionLogPolicy.
        Specifies the log level used to control logging output of execution logs.
        Enabling logging at a given level also enables logging at all higher levels.

        Allowed values for this property are: "INFO", "WARN", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The log_level of this ExecutionLogPolicy.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """
        Sets the log_level of this ExecutionLogPolicy.
        Specifies the log level used to control logging output of execution logs.
        Enabling logging at a given level also enables logging at all higher levels.


        :param log_level: The log_level of this ExecutionLogPolicy.
        :type: str
        """
        allowed_values = ["INFO", "WARN", "ERROR"]
        if not value_allowed_none_or_none_sentinel(log_level, allowed_values):
            log_level = 'UNKNOWN_ENUM_VALUE'
        self._log_level = log_level

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
