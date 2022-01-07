# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobExecutionsStatusSummary(object):
    """
    A summary of the status of the job executions.
    """

    #: A constant which can be used with the status property of a JobExecutionsStatusSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a JobExecutionsStatusSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a JobExecutionsStatusSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new JobExecutionsStatusSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this JobExecutionsStatusSummary.
            Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param count:
            The value to assign to the count property of this JobExecutionsStatusSummary.
        :type count: int

        """
        self.swagger_types = {
            'status': 'str',
            'count': 'int'
        }

        self.attribute_map = {
            'status': 'status',
            'count': 'count'
        }

        self._status = None
        self._count = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this JobExecutionsStatusSummary.
        The status of the job execution.

        Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this JobExecutionsStatusSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobExecutionsStatusSummary.
        The status of the job execution.


        :param status: The status of this JobExecutionsStatusSummary.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def count(self):
        """
        **[Required]** Gets the count of this JobExecutionsStatusSummary.
        The number of job executions of a particular status.


        :return: The count of this JobExecutionsStatusSummary.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this JobExecutionsStatusSummary.
        The number of job executions of a particular status.


        :param count: The count of this JobExecutionsStatusSummary.
        :type: int
        """
        self._count = count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
