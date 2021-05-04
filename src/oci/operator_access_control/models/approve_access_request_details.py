# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApproveAccessRequestDetails(object):
    """
    Details of the access request approval.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ApproveAccessRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param approver_comment:
            The value to assign to the approver_comment property of this ApproveAccessRequestDetails.
        :type approver_comment: str

        :param audit_type:
            The value to assign to the audit_type property of this ApproveAccessRequestDetails.
        :type audit_type: list[str]

        :param additional_message:
            The value to assign to the additional_message property of this ApproveAccessRequestDetails.
        :type additional_message: str

        """
        self.swagger_types = {
            'approver_comment': 'str',
            'audit_type': 'list[str]',
            'additional_message': 'str'
        }

        self.attribute_map = {
            'approver_comment': 'approverComment',
            'audit_type': 'auditType',
            'additional_message': 'additionalMessage'
        }

        self._approver_comment = None
        self._audit_type = None
        self._additional_message = None

    @property
    def approver_comment(self):
        """
        Gets the approver_comment of this ApproveAccessRequestDetails.
        Comment by the approver during approval.


        :return: The approver_comment of this ApproveAccessRequestDetails.
        :rtype: str
        """
        return self._approver_comment

    @approver_comment.setter
    def approver_comment(self, approver_comment):
        """
        Sets the approver_comment of this ApproveAccessRequestDetails.
        Comment by the approver during approval.


        :param approver_comment: The approver_comment of this ApproveAccessRequestDetails.
        :type: str
        """
        self._approver_comment = approver_comment

    @property
    def audit_type(self):
        """
        Gets the audit_type of this ApproveAccessRequestDetails.
        Specifies the type of auditing to be enabled. There are two levels of auditing: command-level and keystroke-level.
        By default, auditing is enabled at the command level i.e., each command issued by the operator is audited. When keystroke-level is chosen,
        in addition to command level logging, key strokes are also logged.


        :return: The audit_type of this ApproveAccessRequestDetails.
        :rtype: list[str]
        """
        return self._audit_type

    @audit_type.setter
    def audit_type(self, audit_type):
        """
        Sets the audit_type of this ApproveAccessRequestDetails.
        Specifies the type of auditing to be enabled. There are two levels of auditing: command-level and keystroke-level.
        By default, auditing is enabled at the command level i.e., each command issued by the operator is audited. When keystroke-level is chosen,
        in addition to command level logging, key strokes are also logged.


        :param audit_type: The audit_type of this ApproveAccessRequestDetails.
        :type: list[str]
        """
        self._audit_type = audit_type

    @property
    def additional_message(self):
        """
        Gets the additional_message of this ApproveAccessRequestDetails.
        Message that needs to be displayed to the Ops User.


        :return: The additional_message of this ApproveAccessRequestDetails.
        :rtype: str
        """
        return self._additional_message

    @additional_message.setter
    def additional_message(self, additional_message):
        """
        Sets the additional_message of this ApproveAccessRequestDetails.
        Message that needs to be displayed to the Ops User.


        :param additional_message: The additional_message of this ApproveAccessRequestDetails.
        :type: str
        """
        self._additional_message = additional_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
