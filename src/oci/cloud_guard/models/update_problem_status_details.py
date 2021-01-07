# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateProblemStatusDetails(object):
    """
    The additional details for the problem
    """

    #: A constant which can be used with the status property of a UpdateProblemStatusDetails.
    #: This constant has a value of "OPEN"
    STATUS_OPEN = "OPEN"

    #: A constant which can be used with the status property of a UpdateProblemStatusDetails.
    #: This constant has a value of "RESOLVED"
    STATUS_RESOLVED = "RESOLVED"

    #: A constant which can be used with the status property of a UpdateProblemStatusDetails.
    #: This constant has a value of "DISMISSED"
    STATUS_DISMISSED = "DISMISSED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateProblemStatusDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this UpdateProblemStatusDetails.
            Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED"
        :type status: str

        :param comment:
            The value to assign to the comment property of this UpdateProblemStatusDetails.
        :type comment: str

        """
        self.swagger_types = {
            'status': 'str',
            'comment': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'comment': 'comment'
        }

        self._status = None
        self._comment = None

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpdateProblemStatusDetails.
        Action taken by user

        Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED"


        :return: The status of this UpdateProblemStatusDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateProblemStatusDetails.
        Action taken by user


        :param status: The status of this UpdateProblemStatusDetails.
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
    def comment(self):
        """
        Gets the comment of this UpdateProblemStatusDetails.
        User Comments


        :return: The comment of this UpdateProblemStatusDetails.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this UpdateProblemStatusDetails.
        User Comments


        :param comment: The comment of this UpdateProblemStatusDetails.
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
