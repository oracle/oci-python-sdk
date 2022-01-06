# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobLogConfigurationDetails(object):
    """
    Logging configuration for resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobLogConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param enable_logging:
            The value to assign to the enable_logging property of this JobLogConfigurationDetails.
        :type enable_logging: bool

        :param enable_auto_log_creation:
            The value to assign to the enable_auto_log_creation property of this JobLogConfigurationDetails.
        :type enable_auto_log_creation: bool

        :param log_group_id:
            The value to assign to the log_group_id property of this JobLogConfigurationDetails.
        :type log_group_id: str

        :param log_id:
            The value to assign to the log_id property of this JobLogConfigurationDetails.
        :type log_id: str

        """
        self.swagger_types = {
            'enable_logging': 'bool',
            'enable_auto_log_creation': 'bool',
            'log_group_id': 'str',
            'log_id': 'str'
        }

        self.attribute_map = {
            'enable_logging': 'enableLogging',
            'enable_auto_log_creation': 'enableAutoLogCreation',
            'log_group_id': 'logGroupId',
            'log_id': 'logId'
        }

        self._enable_logging = None
        self._enable_auto_log_creation = None
        self._log_group_id = None
        self._log_id = None

    @property
    def enable_logging(self):
        """
        Gets the enable_logging of this JobLogConfigurationDetails.
        If customer logging is enabled for job runs.


        :return: The enable_logging of this JobLogConfigurationDetails.
        :rtype: bool
        """
        return self._enable_logging

    @enable_logging.setter
    def enable_logging(self, enable_logging):
        """
        Sets the enable_logging of this JobLogConfigurationDetails.
        If customer logging is enabled for job runs.


        :param enable_logging: The enable_logging of this JobLogConfigurationDetails.
        :type: bool
        """
        self._enable_logging = enable_logging

    @property
    def enable_auto_log_creation(self):
        """
        Gets the enable_auto_log_creation of this JobLogConfigurationDetails.
        If automatic on-behalf-of log object creation is enabled for job runs.


        :return: The enable_auto_log_creation of this JobLogConfigurationDetails.
        :rtype: bool
        """
        return self._enable_auto_log_creation

    @enable_auto_log_creation.setter
    def enable_auto_log_creation(self, enable_auto_log_creation):
        """
        Sets the enable_auto_log_creation of this JobLogConfigurationDetails.
        If automatic on-behalf-of log object creation is enabled for job runs.


        :param enable_auto_log_creation: The enable_auto_log_creation of this JobLogConfigurationDetails.
        :type: bool
        """
        self._enable_auto_log_creation = enable_auto_log_creation

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this JobLogConfigurationDetails.
        The log group id for where log objects are for job runs.


        :return: The log_group_id of this JobLogConfigurationDetails.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this JobLogConfigurationDetails.
        The log group id for where log objects are for job runs.


        :param log_group_id: The log_group_id of this JobLogConfigurationDetails.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_id(self):
        """
        Gets the log_id of this JobLogConfigurationDetails.
        The log id the job run will push logs too.


        :return: The log_id of this JobLogConfigurationDetails.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """
        Sets the log_id of this JobLogConfigurationDetails.
        The log id the job run will push logs too.


        :param log_id: The log_id of this JobLogConfigurationDetails.
        :type: str
        """
        self._log_id = log_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
