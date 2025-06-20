# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApprovePrivilegedApiRequestDetails(object):
    """
    Details of the privilegedApi request approval such as when the approver approved and any comment provided by the approver.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApprovePrivilegedApiRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param approver_comment:
            The value to assign to the approver_comment property of this ApprovePrivilegedApiRequestDetails.
        :type approver_comment: str

        :param time_of_user_creation:
            The value to assign to the time_of_user_creation property of this ApprovePrivilegedApiRequestDetails.
        :type time_of_user_creation: datetime

        """
        self.swagger_types = {
            'approver_comment': 'str',
            'time_of_user_creation': 'datetime'
        }
        self.attribute_map = {
            'approver_comment': 'approverComment',
            'time_of_user_creation': 'timeOfUserCreation'
        }
        self._approver_comment = None
        self._time_of_user_creation = None

    @property
    def approver_comment(self):
        """
        Gets the approver_comment of this ApprovePrivilegedApiRequestDetails.
        Comment by the approver during approval.


        :return: The approver_comment of this ApprovePrivilegedApiRequestDetails.
        :rtype: str
        """
        return self._approver_comment

    @approver_comment.setter
    def approver_comment(self, approver_comment):
        """
        Sets the approver_comment of this ApprovePrivilegedApiRequestDetails.
        Comment by the approver during approval.


        :param approver_comment: The approver_comment of this ApprovePrivilegedApiRequestDetails.
        :type: str
        """
        self._approver_comment = approver_comment

    @property
    def time_of_user_creation(self):
        """
        Gets the time_of_user_creation of this ApprovePrivilegedApiRequestDetails.
        The time when access request is scheduled to be approved in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_user_creation of this ApprovePrivilegedApiRequestDetails.
        :rtype: datetime
        """
        return self._time_of_user_creation

    @time_of_user_creation.setter
    def time_of_user_creation(self, time_of_user_creation):
        """
        Sets the time_of_user_creation of this ApprovePrivilegedApiRequestDetails.
        The time when access request is scheduled to be approved in `RFC 3339`__ timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_user_creation: The time_of_user_creation of this ApprovePrivilegedApiRequestDetails.
        :type: datetime
        """
        self._time_of_user_creation = time_of_user_creation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
