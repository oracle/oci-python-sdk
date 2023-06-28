# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630

from .update_deploy_stage_details import UpdateDeployStageDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateLoadBalancerTrafficShiftDeployStageDetails(UpdateDeployStageDetails):
    """
    Specifies load balancer traffic shift stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateLoadBalancerTrafficShiftDeployStageDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateLoadBalancerTrafficShiftDeployStageDetails.deploy_stage_type` attribute
        of this class is ``LOAD_BALANCER_TRAFFIC_SHIFT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type display_name: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type deploy_stage_type: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param blue_backend_ips:
            The value to assign to the blue_backend_ips property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type blue_backend_ips: oci.devops.models.BackendSetIpCollection

        :param green_backend_ips:
            The value to assign to the green_backend_ips property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type green_backend_ips: oci.devops.models.BackendSetIpCollection

        :param traffic_shift_target:
            The value to assign to the traffic_shift_target property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type traffic_shift_target: str

        :param rollout_policy:
            The value to assign to the rollout_policy property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type rollout_policy: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy

        :param load_balancer_config:
            The value to assign to the load_balancer_config property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type load_balancer_config: oci.devops.models.LoadBalancerConfig

        :param rollback_policy:
            The value to assign to the rollback_policy property of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type rollback_policy: oci.devops.models.DeployStageRollbackPolicy

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_stage_type': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'blue_backend_ips': 'BackendSetIpCollection',
            'green_backend_ips': 'BackendSetIpCollection',
            'traffic_shift_target': 'str',
            'rollout_policy': 'LoadBalancerTrafficShiftRolloutPolicy',
            'load_balancer_config': 'LoadBalancerConfig',
            'rollback_policy': 'DeployStageRollbackPolicy'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_stage_type': 'deployStageType',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'blue_backend_ips': 'blueBackendIps',
            'green_backend_ips': 'greenBackendIps',
            'traffic_shift_target': 'trafficShiftTarget',
            'rollout_policy': 'rolloutPolicy',
            'load_balancer_config': 'loadBalancerConfig',
            'rollback_policy': 'rollbackPolicy'
        }

        self._description = None
        self._display_name = None
        self._deploy_stage_type = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._blue_backend_ips = None
        self._green_backend_ips = None
        self._traffic_shift_target = None
        self._rollout_policy = None
        self._load_balancer_config = None
        self._rollback_policy = None
        self._deploy_stage_type = 'LOAD_BALANCER_TRAFFIC_SHIFT'

    @property
    def blue_backend_ips(self):
        """
        Gets the blue_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :return: The blue_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :rtype: oci.devops.models.BackendSetIpCollection
        """
        return self._blue_backend_ips

    @blue_backend_ips.setter
    def blue_backend_ips(self, blue_backend_ips):
        """
        Sets the blue_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :param blue_backend_ips: The blue_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type: oci.devops.models.BackendSetIpCollection
        """
        self._blue_backend_ips = blue_backend_ips

    @property
    def green_backend_ips(self):
        """
        Gets the green_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :return: The green_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :rtype: oci.devops.models.BackendSetIpCollection
        """
        return self._green_backend_ips

    @green_backend_ips.setter
    def green_backend_ips(self, green_backend_ips):
        """
        Sets the green_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :param green_backend_ips: The green_backend_ips of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type: oci.devops.models.BackendSetIpCollection
        """
        self._green_backend_ips = green_backend_ips

    @property
    def traffic_shift_target(self):
        """
        Gets the traffic_shift_target of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs ser as per rolloutPolicy.


        :return: The traffic_shift_target of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :rtype: str
        """
        return self._traffic_shift_target

    @traffic_shift_target.setter
    def traffic_shift_target(self, traffic_shift_target):
        """
        Sets the traffic_shift_target of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs ser as per rolloutPolicy.


        :param traffic_shift_target: The traffic_shift_target of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type: str
        """
        self._traffic_shift_target = traffic_shift_target

    @property
    def rollout_policy(self):
        """
        Gets the rollout_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :return: The rollout_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :rtype: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy
        """
        return self._rollout_policy

    @rollout_policy.setter
    def rollout_policy(self, rollout_policy):
        """
        Sets the rollout_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :param rollout_policy: The rollout_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type: oci.devops.models.LoadBalancerTrafficShiftRolloutPolicy
        """
        self._rollout_policy = rollout_policy

    @property
    def load_balancer_config(self):
        """
        Gets the load_balancer_config of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :return: The load_balancer_config of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :rtype: oci.devops.models.LoadBalancerConfig
        """
        return self._load_balancer_config

    @load_balancer_config.setter
    def load_balancer_config(self, load_balancer_config):
        """
        Sets the load_balancer_config of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :param load_balancer_config: The load_balancer_config of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type: oci.devops.models.LoadBalancerConfig
        """
        self._load_balancer_config = load_balancer_config

    @property
    def rollback_policy(self):
        """
        Gets the rollback_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :return: The rollback_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :rtype: oci.devops.models.DeployStageRollbackPolicy
        """
        return self._rollback_policy

    @rollback_policy.setter
    def rollback_policy(self, rollback_policy):
        """
        Sets the rollback_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.

        :param rollback_policy: The rollback_policy of this UpdateLoadBalancerTrafficShiftDeployStageDetails.
        :type: oci.devops.models.DeployStageRollbackPolicy
        """
        self._rollback_policy = rollback_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
