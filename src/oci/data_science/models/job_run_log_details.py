# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobRunLogDetails(object):
    """
    Customer logging details for job run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobRunLogDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param log_group_id:
            The value to assign to the log_group_id property of this JobRunLogDetails.
        :type log_group_id: str

        :param log_id:
            The value to assign to the log_id property of this JobRunLogDetails.
        :type log_id: str

        """
        self.swagger_types = {
            'log_group_id': 'str',
            'log_id': 'str'
        }

        self.attribute_map = {
            'log_group_id': 'logGroupId',
            'log_id': 'logId'
        }

        self._log_group_id = None
        self._log_id = None

    @property
    def log_group_id(self):
        """
        **[Required]** Gets the log_group_id of this JobRunLogDetails.
        The log group id for where log objects will be for job runs.


        :return: The log_group_id of this JobRunLogDetails.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this JobRunLogDetails.
        The log group id for where log objects will be for job runs.


        :param log_group_id: The log_group_id of this JobRunLogDetails.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_id(self):
        """
        **[Required]** Gets the log_id of this JobRunLogDetails.
        The log id of the log object the job run logs will be shipped to.


        :return: The log_id of this JobRunLogDetails.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """
        Sets the log_id of this JobRunLogDetails.
        The log id of the log object the job run logs will be shipped to.


        :param log_id: The log_id of this JobRunLogDetails.
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
