# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApproveDeploymentDetails(object):
    """
    The stage information for submitting for approval.
    """

    #: A constant which can be used with the action property of a ApproveDeploymentDetails.
    #: This constant has a value of "APPROVE"
    ACTION_APPROVE = "APPROVE"

    #: A constant which can be used with the action property of a ApproveDeploymentDetails.
    #: This constant has a value of "REJECT"
    ACTION_REJECT = "REJECT"

    def __init__(self, **kwargs):
        """
        Initializes a new ApproveDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_stage_id:
            The value to assign to the deploy_stage_id property of this ApproveDeploymentDetails.
        :type deploy_stage_id: str

        :param reason:
            The value to assign to the reason property of this ApproveDeploymentDetails.
        :type reason: str

        :param action:
            The value to assign to the action property of this ApproveDeploymentDetails.
            Allowed values for this property are: "APPROVE", "REJECT"
        :type action: str

        """
        self.swagger_types = {
            'deploy_stage_id': 'str',
            'reason': 'str',
            'action': 'str'
        }

        self.attribute_map = {
            'deploy_stage_id': 'deployStageId',
            'reason': 'reason',
            'action': 'action'
        }

        self._deploy_stage_id = None
        self._reason = None
        self._action = None

    @property
    def deploy_stage_id(self):
        """
        **[Required]** Gets the deploy_stage_id of this ApproveDeploymentDetails.
        The `OCID`__ of the stage which is marked for approval.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The deploy_stage_id of this ApproveDeploymentDetails.
        :rtype: str
        """
        return self._deploy_stage_id

    @deploy_stage_id.setter
    def deploy_stage_id(self, deploy_stage_id):
        """
        Sets the deploy_stage_id of this ApproveDeploymentDetails.
        The `OCID`__ of the stage which is marked for approval.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param deploy_stage_id: The deploy_stage_id of this ApproveDeploymentDetails.
        :type: str
        """
        self._deploy_stage_id = deploy_stage_id

    @property
    def reason(self):
        """
        Gets the reason of this ApproveDeploymentDetails.
        The reason for approving or rejecting the deployment.


        :return: The reason of this ApproveDeploymentDetails.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this ApproveDeploymentDetails.
        The reason for approving or rejecting the deployment.


        :param reason: The reason of this ApproveDeploymentDetails.
        :type: str
        """
        self._reason = reason

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ApproveDeploymentDetails.
        The action of Approve or Reject.

        Allowed values for this property are: "APPROVE", "REJECT"


        :return: The action of this ApproveDeploymentDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ApproveDeploymentDetails.
        The action of Approve or Reject.


        :param action: The action of this ApproveDeploymentDetails.
        :type: str
        """
        allowed_values = ["APPROVE", "REJECT"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
