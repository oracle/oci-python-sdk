# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApprovalAction(object):
    """
    Information about the approval action of DevOps deployment stages.
    """

    #: A constant which can be used with the action property of a ApprovalAction.
    #: This constant has a value of "APPROVE"
    ACTION_APPROVE = "APPROVE"

    #: A constant which can be used with the action property of a ApprovalAction.
    #: This constant has a value of "REJECT"
    ACTION_REJECT = "REJECT"

    def __init__(self, **kwargs):
        """
        Initializes a new ApprovalAction object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subject_id:
            The value to assign to the subject_id property of this ApprovalAction.
        :type subject_id: str

        :param action:
            The value to assign to the action property of this ApprovalAction.
            Allowed values for this property are: "APPROVE", "REJECT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param reason:
            The value to assign to the reason property of this ApprovalAction.
        :type reason: str

        """
        self.swagger_types = {
            'subject_id': 'str',
            'action': 'str',
            'reason': 'str'
        }

        self.attribute_map = {
            'subject_id': 'subjectId',
            'action': 'action',
            'reason': 'reason'
        }

        self._subject_id = None
        self._action = None
        self._reason = None

    @property
    def subject_id(self):
        """
        **[Required]** Gets the subject_id of this ApprovalAction.
        The subject ID of the user who approves or disapproves a DevOps deployment stage.


        :return: The subject_id of this ApprovalAction.
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """
        Sets the subject_id of this ApprovalAction.
        The subject ID of the user who approves or disapproves a DevOps deployment stage.


        :param subject_id: The subject_id of this ApprovalAction.
        :type: str
        """
        self._subject_id = subject_id

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ApprovalAction.
        The action of the user on the DevOps deployment stage.

        Allowed values for this property are: "APPROVE", "REJECT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this ApprovalAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ApprovalAction.
        The action of the user on the DevOps deployment stage.


        :param action: The action of this ApprovalAction.
        :type: str
        """
        allowed_values = ["APPROVE", "REJECT"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def reason(self):
        """
        Gets the reason of this ApprovalAction.
        The reason for approving or rejecting the deployment.


        :return: The reason of this ApprovalAction.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this ApprovalAction.
        The reason for approving or rejecting the deployment.


        :param reason: The reason of this ApprovalAction.
        :type: str
        """
        self._reason = reason

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
