# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230801


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApproveDelegatedResourceAccessRequestDetails(object):
    """
    Details of the Delegated Resource Access Request approval.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApproveDelegatedResourceAccessRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param approver_comment:
            The value to assign to the approver_comment property of this ApproveDelegatedResourceAccessRequestDetails.
        :type approver_comment: str

        :param additional_message:
            The value to assign to the additional_message property of this ApproveDelegatedResourceAccessRequestDetails.
        :type additional_message: str

        :param time_approved_for_access:
            The value to assign to the time_approved_for_access property of this ApproveDelegatedResourceAccessRequestDetails.
        :type time_approved_for_access: datetime

        """
        self.swagger_types = {
            'approver_comment': 'str',
            'additional_message': 'str',
            'time_approved_for_access': 'datetime'
        }
        self.attribute_map = {
            'approver_comment': 'approverComment',
            'additional_message': 'additionalMessage',
            'time_approved_for_access': 'timeApprovedForAccess'
        }
        self._approver_comment = None
        self._additional_message = None
        self._time_approved_for_access = None

    @property
    def approver_comment(self):
        """
        Gets the approver_comment of this ApproveDelegatedResourceAccessRequestDetails.
        Comment by the approver during approval.


        :return: The approver_comment of this ApproveDelegatedResourceAccessRequestDetails.
        :rtype: str
        """
        return self._approver_comment

    @approver_comment.setter
    def approver_comment(self, approver_comment):
        """
        Sets the approver_comment of this ApproveDelegatedResourceAccessRequestDetails.
        Comment by the approver during approval.


        :param approver_comment: The approver_comment of this ApproveDelegatedResourceAccessRequestDetails.
        :type: str
        """
        self._approver_comment = approver_comment

    @property
    def additional_message(self):
        """
        Gets the additional_message of this ApproveDelegatedResourceAccessRequestDetails.
        Message that needs to be displayed to the operator.


        :return: The additional_message of this ApproveDelegatedResourceAccessRequestDetails.
        :rtype: str
        """
        return self._additional_message

    @additional_message.setter
    def additional_message(self, additional_message):
        """
        Sets the additional_message of this ApproveDelegatedResourceAccessRequestDetails.
        Message that needs to be displayed to the operator.


        :param additional_message: The additional_message of this ApproveDelegatedResourceAccessRequestDetails.
        :type: str
        """
        self._additional_message = additional_message

    @property
    def time_approved_for_access(self):
        """
        Gets the time_approved_for_access of this ApproveDelegatedResourceAccessRequestDetails.
        Access start time that is actually approved by the customer in `RFC 3339`__timestamp format, e.g. '2020-05-22T21:10:29.600Z'.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_approved_for_access of this ApproveDelegatedResourceAccessRequestDetails.
        :rtype: datetime
        """
        return self._time_approved_for_access

    @time_approved_for_access.setter
    def time_approved_for_access(self, time_approved_for_access):
        """
        Sets the time_approved_for_access of this ApproveDelegatedResourceAccessRequestDetails.
        Access start time that is actually approved by the customer in `RFC 3339`__timestamp format, e.g. '2020-05-22T21:10:29.600Z'.

        __ https://tools.ietf.org/html/rfc3339


        :param time_approved_for_access: The time_approved_for_access of this ApproveDelegatedResourceAccessRequestDetails.
        :type: datetime
        """
        self._time_approved_for_access = time_approved_for_access

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
