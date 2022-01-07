# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelConfigurationDetails(object):
    """
    The model configuration details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModelConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_id:
            The value to assign to the model_id property of this ModelConfigurationDetails.
        :type model_id: str

        :param instance_configuration:
            The value to assign to the instance_configuration property of this ModelConfigurationDetails.
        :type instance_configuration: oci.data_science.models.InstanceConfiguration

        :param scaling_policy:
            The value to assign to the scaling_policy property of this ModelConfigurationDetails.
        :type scaling_policy: oci.data_science.models.ScalingPolicy

        :param bandwidth_mbps:
            The value to assign to the bandwidth_mbps property of this ModelConfigurationDetails.
        :type bandwidth_mbps: int

        """
        self.swagger_types = {
            'model_id': 'str',
            'instance_configuration': 'InstanceConfiguration',
            'scaling_policy': 'ScalingPolicy',
            'bandwidth_mbps': 'int'
        }

        self.attribute_map = {
            'model_id': 'modelId',
            'instance_configuration': 'instanceConfiguration',
            'scaling_policy': 'scalingPolicy',
            'bandwidth_mbps': 'bandwidthMbps'
        }

        self._model_id = None
        self._instance_configuration = None
        self._scaling_policy = None
        self._bandwidth_mbps = None

    @property
    def model_id(self):
        """
        **[Required]** Gets the model_id of this ModelConfigurationDetails.
        The OCID of the model you want to deploy.


        :return: The model_id of this ModelConfigurationDetails.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """
        Sets the model_id of this ModelConfigurationDetails.
        The OCID of the model you want to deploy.


        :param model_id: The model_id of this ModelConfigurationDetails.
        :type: str
        """
        self._model_id = model_id

    @property
    def instance_configuration(self):
        """
        **[Required]** Gets the instance_configuration of this ModelConfigurationDetails.

        :return: The instance_configuration of this ModelConfigurationDetails.
        :rtype: oci.data_science.models.InstanceConfiguration
        """
        return self._instance_configuration

    @instance_configuration.setter
    def instance_configuration(self, instance_configuration):
        """
        Sets the instance_configuration of this ModelConfigurationDetails.

        :param instance_configuration: The instance_configuration of this ModelConfigurationDetails.
        :type: oci.data_science.models.InstanceConfiguration
        """
        self._instance_configuration = instance_configuration

    @property
    def scaling_policy(self):
        """
        Gets the scaling_policy of this ModelConfigurationDetails.

        :return: The scaling_policy of this ModelConfigurationDetails.
        :rtype: oci.data_science.models.ScalingPolicy
        """
        return self._scaling_policy

    @scaling_policy.setter
    def scaling_policy(self, scaling_policy):
        """
        Sets the scaling_policy of this ModelConfigurationDetails.

        :param scaling_policy: The scaling_policy of this ModelConfigurationDetails.
        :type: oci.data_science.models.ScalingPolicy
        """
        self._scaling_policy = scaling_policy

    @property
    def bandwidth_mbps(self):
        """
        Gets the bandwidth_mbps of this ModelConfigurationDetails.
        The network bandwidth for the model.


        :return: The bandwidth_mbps of this ModelConfigurationDetails.
        :rtype: int
        """
        return self._bandwidth_mbps

    @bandwidth_mbps.setter
    def bandwidth_mbps(self, bandwidth_mbps):
        """
        Sets the bandwidth_mbps of this ModelConfigurationDetails.
        The network bandwidth for the model.


        :param bandwidth_mbps: The bandwidth_mbps of this ModelConfigurationDetails.
        :type: int
        """
        self._bandwidth_mbps = bandwidth_mbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
