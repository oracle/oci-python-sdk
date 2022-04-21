# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .add_auto_scale_policy_details import AddAutoScalePolicyDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddMetricBasedVerticalScalingPolicyDetails(AddAutoScalePolicyDetails):
    """
    Details of a metric based vertical autoscaling policy.

    In a metric-based autoscaling policy, an autoscaling action is triggered when a performance metric exceeds a threshold.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddMetricBasedVerticalScalingPolicyDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.bds.models.AddMetricBasedVerticalScalingPolicyDetails.policy_type` attribute
        of this class is ``METRIC_BASED_VERTICAL_SCALING_POLICY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy_type:
            The value to assign to the policy_type property of this AddMetricBasedVerticalScalingPolicyDetails.
        :type policy_type: str

        :param scale_up_config:
            The value to assign to the scale_up_config property of this AddMetricBasedVerticalScalingPolicyDetails.
        :type scale_up_config: oci.bds.models.MetricBasedVerticalScaleUpConfig

        :param scale_down_config:
            The value to assign to the scale_down_config property of this AddMetricBasedVerticalScalingPolicyDetails.
        :type scale_down_config: oci.bds.models.MetricBasedVerticalScaleDownConfig

        """
        self.swagger_types = {
            'policy_type': 'str',
            'scale_up_config': 'MetricBasedVerticalScaleUpConfig',
            'scale_down_config': 'MetricBasedVerticalScaleDownConfig'
        }

        self.attribute_map = {
            'policy_type': 'policyType',
            'scale_up_config': 'scaleUpConfig',
            'scale_down_config': 'scaleDownConfig'
        }

        self._policy_type = None
        self._scale_up_config = None
        self._scale_down_config = None
        self._policy_type = 'METRIC_BASED_VERTICAL_SCALING_POLICY'

    @property
    def scale_up_config(self):
        """
        Gets the scale_up_config of this AddMetricBasedVerticalScalingPolicyDetails.

        :return: The scale_up_config of this AddMetricBasedVerticalScalingPolicyDetails.
        :rtype: oci.bds.models.MetricBasedVerticalScaleUpConfig
        """
        return self._scale_up_config

    @scale_up_config.setter
    def scale_up_config(self, scale_up_config):
        """
        Sets the scale_up_config of this AddMetricBasedVerticalScalingPolicyDetails.

        :param scale_up_config: The scale_up_config of this AddMetricBasedVerticalScalingPolicyDetails.
        :type: oci.bds.models.MetricBasedVerticalScaleUpConfig
        """
        self._scale_up_config = scale_up_config

    @property
    def scale_down_config(self):
        """
        Gets the scale_down_config of this AddMetricBasedVerticalScalingPolicyDetails.

        :return: The scale_down_config of this AddMetricBasedVerticalScalingPolicyDetails.
        :rtype: oci.bds.models.MetricBasedVerticalScaleDownConfig
        """
        return self._scale_down_config

    @scale_down_config.setter
    def scale_down_config(self, scale_down_config):
        """
        Sets the scale_down_config of this AddMetricBasedVerticalScalingPolicyDetails.

        :param scale_down_config: The scale_down_config of this AddMetricBasedVerticalScalingPolicyDetails.
        :type: oci.bds.models.MetricBasedVerticalScaleDownConfig
        """
        self._scale_down_config = scale_down_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
