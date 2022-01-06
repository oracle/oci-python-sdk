# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .deploy_stage_rollback_policy import DeployStageRollbackPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutomatedDeployStageRollbackPolicy(DeployStageRollbackPolicy):
    """
    Specifies the automated rollback policy for a stage on failure.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutomatedDeployStageRollbackPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.AutomatedDeployStageRollbackPolicy.policy_type` attribute
        of this class is ``AUTOMATED_STAGE_ROLLBACK_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this AutomatedDeployStageRollbackPolicy.
            Allowed values for this property are: "AUTOMATED_STAGE_ROLLBACK_POLICY", "NO_STAGE_ROLLBACK_POLICY"
        :type policy_type: str

        """
        self.swagger_types = {
            'policy_type': 'str'
        }

        self.attribute_map = {
            'policy_type': 'policyType'
        }

        self._policy_type = None
        self._policy_type = 'AUTOMATED_STAGE_ROLLBACK_POLICY'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
