# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployStageExecutionProgressDetails(object):
    """
    Details about stage execution for each target environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployStageExecutionProgressDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param target_id:
            The value to assign to the target_id property of this DeployStageExecutionProgressDetails.
        :type target_id: str

        :param target_group:
            The value to assign to the target_group property of this DeployStageExecutionProgressDetails.
        :type target_group: str

        :param steps:
            The value to assign to the steps property of this DeployStageExecutionProgressDetails.
        :type steps: list[oci.devops.models.DeployStageExecutionStep]

        :param rollback_steps:
            The value to assign to the rollback_steps property of this DeployStageExecutionProgressDetails.
        :type rollback_steps: list[oci.devops.models.DeployStageExecutionStep]

        """
        self.swagger_types = {
            'target_id': 'str',
            'target_group': 'str',
            'steps': 'list[DeployStageExecutionStep]',
            'rollback_steps': 'list[DeployStageExecutionStep]'
        }

        self.attribute_map = {
            'target_id': 'targetId',
            'target_group': 'targetGroup',
            'steps': 'steps',
            'rollback_steps': 'rollbackSteps'
        }

        self._target_id = None
        self._target_group = None
        self._steps = None
        self._rollback_steps = None

    @property
    def target_id(self):
        """
        Gets the target_id of this DeployStageExecutionProgressDetails.
        The function ID, instance ID or the cluster ID. For Wait stage it will be the stage ID.


        :return: The target_id of this DeployStageExecutionProgressDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this DeployStageExecutionProgressDetails.
        The function ID, instance ID or the cluster ID. For Wait stage it will be the stage ID.


        :param target_id: The target_id of this DeployStageExecutionProgressDetails.
        :type: str
        """
        self._target_id = target_id

    @property
    def target_group(self):
        """
        Gets the target_group of this DeployStageExecutionProgressDetails.
        Group for the target environment for example, the batch number for an Instance Group deployment.


        :return: The target_group of this DeployStageExecutionProgressDetails.
        :rtype: str
        """
        return self._target_group

    @target_group.setter
    def target_group(self, target_group):
        """
        Sets the target_group of this DeployStageExecutionProgressDetails.
        Group for the target environment for example, the batch number for an Instance Group deployment.


        :param target_group: The target_group of this DeployStageExecutionProgressDetails.
        :type: str
        """
        self._target_group = target_group

    @property
    def steps(self):
        """
        Gets the steps of this DeployStageExecutionProgressDetails.
        Details about all the steps for one target environment.


        :return: The steps of this DeployStageExecutionProgressDetails.
        :rtype: list[oci.devops.models.DeployStageExecutionStep]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps of this DeployStageExecutionProgressDetails.
        Details about all the steps for one target environment.


        :param steps: The steps of this DeployStageExecutionProgressDetails.
        :type: list[oci.devops.models.DeployStageExecutionStep]
        """
        self._steps = steps

    @property
    def rollback_steps(self):
        """
        Gets the rollback_steps of this DeployStageExecutionProgressDetails.
        Details about all the rollback steps for one target environment.


        :return: The rollback_steps of this DeployStageExecutionProgressDetails.
        :rtype: list[oci.devops.models.DeployStageExecutionStep]
        """
        return self._rollback_steps

    @rollback_steps.setter
    def rollback_steps(self, rollback_steps):
        """
        Sets the rollback_steps of this DeployStageExecutionProgressDetails.
        Details about all the rollback steps for one target environment.


        :param rollback_steps: The rollback_steps of this DeployStageExecutionProgressDetails.
        :type: list[oci.devops.models.DeployStageExecutionStep]
        """
        self._rollback_steps = rollback_steps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
