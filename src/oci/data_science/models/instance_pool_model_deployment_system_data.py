# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .model_deployment_system_data import ModelDeploymentSystemData
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstancePoolModelDeploymentSystemData(ModelDeploymentSystemData):
    """
    Instance pool based model deployment system data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstancePoolModelDeploymentSystemData object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.InstancePoolModelDeploymentSystemData.system_infra_type` attribute
        of this class is ``INSTANCE_POOL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param system_infra_type:
            The value to assign to the system_infra_type property of this InstancePoolModelDeploymentSystemData.
            Allowed values for this property are: "INSTANCE_POOL"
        :type system_infra_type: str

        :param current_instance_count:
            The value to assign to the current_instance_count property of this InstancePoolModelDeploymentSystemData.
        :type current_instance_count: int

        """
        self.swagger_types = {
            'system_infra_type': 'str',
            'current_instance_count': 'int'
        }
        self.attribute_map = {
            'system_infra_type': 'systemInfraType',
            'current_instance_count': 'currentInstanceCount'
        }
        self._system_infra_type = None
        self._current_instance_count = None
        self._system_infra_type = 'INSTANCE_POOL'

    @property
    def current_instance_count(self):
        """
        Gets the current_instance_count of this InstancePoolModelDeploymentSystemData.
        This value is the current count of the model deployment instances.


        :return: The current_instance_count of this InstancePoolModelDeploymentSystemData.
        :rtype: int
        """
        return self._current_instance_count

    @current_instance_count.setter
    def current_instance_count(self, current_instance_count):
        """
        Sets the current_instance_count of this InstancePoolModelDeploymentSystemData.
        This value is the current count of the model deployment instances.


        :param current_instance_count: The current_instance_count of this InstancePoolModelDeploymentSystemData.
        :type: int
        """
        self._current_instance_count = current_instance_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
