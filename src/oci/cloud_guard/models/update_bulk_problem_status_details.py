# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBulkProblemStatusDetails(object):
    """
    List of problem ids to be passed in to update the Problem status.
    """

    #: A constant which can be used with the status property of a UpdateBulkProblemStatusDetails.
    #: This constant has a value of "OPEN"
    STATUS_OPEN = "OPEN"

    #: A constant which can be used with the status property of a UpdateBulkProblemStatusDetails.
    #: This constant has a value of "RESOLVED"
    STATUS_RESOLVED = "RESOLVED"

    #: A constant which can be used with the status property of a UpdateBulkProblemStatusDetails.
    #: This constant has a value of "DISMISSED"
    STATUS_DISMISSED = "DISMISSED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBulkProblemStatusDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateBulkProblemStatusDetails.
            Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED"
        :type status: str

        :param problem_ids:
            The value to assign to the problem_ids property of this UpdateBulkProblemStatusDetails.
        :type problem_ids: list[str]

        :param comment:
            The value to assign to the comment property of this UpdateBulkProblemStatusDetails.
        :type comment: str

        """
        self.swagger_types = {
            'status': 'str',
            'problem_ids': 'list[str]',
            'comment': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'problem_ids': 'problemIds',
            'comment': 'comment'
        }

        self._status = None
        self._problem_ids = None
        self._comment = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateBulkProblemStatusDetails.
        Action taken by user

        Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED"


        :return: The status of this UpdateBulkProblemStatusDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateBulkProblemStatusDetails.
        Action taken by user


        :param status: The status of this UpdateBulkProblemStatusDetails.
        :type: str
        """
        allowed_values = ["OPEN", "RESOLVED", "DISMISSED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            raise ValueError(
                "Invalid value for `status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def problem_ids(self):
        """
        **[Required]** Gets the problem_ids of this UpdateBulkProblemStatusDetails.
        List of ProblemIds to be passed in to update the Problem status.


        :return: The problem_ids of this UpdateBulkProblemStatusDetails.
        :rtype: list[str]
        """
        return self._problem_ids

    @problem_ids.setter
    def problem_ids(self, problem_ids):
        """
        Sets the problem_ids of this UpdateBulkProblemStatusDetails.
        List of ProblemIds to be passed in to update the Problem status.


        :param problem_ids: The problem_ids of this UpdateBulkProblemStatusDetails.
        :type: list[str]
        """
        self._problem_ids = problem_ids

    @property
    def comment(self):
        """
        Gets the comment of this UpdateBulkProblemStatusDetails.
        User defined comment to be passed in to update the problem.


        :return: The comment of this UpdateBulkProblemStatusDetails.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this UpdateBulkProblemStatusDetails.
        User defined comment to be passed in to update the problem.


        :param comment: The comment of this UpdateBulkProblemStatusDetails.
        :type: str
        """
        self._comment = comment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
