# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfiguration(object):
    """
    The model deployment instance configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_shape_name:
            The value to assign to the instance_shape_name property of this InstanceConfiguration.
        :type instance_shape_name: str

        :param model_deployment_instance_shape_config_details:
            The value to assign to the model_deployment_instance_shape_config_details property of this InstanceConfiguration.
        :type model_deployment_instance_shape_config_details: oci.data_science.models.ModelDeploymentInstanceShapeConfigDetails

        :param subnet_id:
            The value to assign to the subnet_id property of this InstanceConfiguration.
        :type subnet_id: str

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this InstanceConfiguration.
        :type private_endpoint_id: str

        """
        self.swagger_types = {
            'instance_shape_name': 'str',
            'model_deployment_instance_shape_config_details': 'ModelDeploymentInstanceShapeConfigDetails',
            'subnet_id': 'str',
            'private_endpoint_id': 'str'
        }

        self.attribute_map = {
            'instance_shape_name': 'instanceShapeName',
            'model_deployment_instance_shape_config_details': 'modelDeploymentInstanceShapeConfigDetails',
            'subnet_id': 'subnetId',
            'private_endpoint_id': 'privateEndpointId'
        }

        self._instance_shape_name = None
        self._model_deployment_instance_shape_config_details = None
        self._subnet_id = None
        self._private_endpoint_id = None

    @property
    def instance_shape_name(self):
        """
        **[Required]** Gets the instance_shape_name of this InstanceConfiguration.
        The shape used to launch the model deployment instances.


        :return: The instance_shape_name of this InstanceConfiguration.
        :rtype: str
        """
        return self._instance_shape_name

    @instance_shape_name.setter
    def instance_shape_name(self, instance_shape_name):
        """
        Sets the instance_shape_name of this InstanceConfiguration.
        The shape used to launch the model deployment instances.


        :param instance_shape_name: The instance_shape_name of this InstanceConfiguration.
        :type: str
        """
        self._instance_shape_name = instance_shape_name

    @property
    def model_deployment_instance_shape_config_details(self):
        """
        Gets the model_deployment_instance_shape_config_details of this InstanceConfiguration.

        :return: The model_deployment_instance_shape_config_details of this InstanceConfiguration.
        :rtype: oci.data_science.models.ModelDeploymentInstanceShapeConfigDetails
        """
        return self._model_deployment_instance_shape_config_details

    @model_deployment_instance_shape_config_details.setter
    def model_deployment_instance_shape_config_details(self, model_deployment_instance_shape_config_details):
        """
        Sets the model_deployment_instance_shape_config_details of this InstanceConfiguration.

        :param model_deployment_instance_shape_config_details: The model_deployment_instance_shape_config_details of this InstanceConfiguration.
        :type: oci.data_science.models.ModelDeploymentInstanceShapeConfigDetails
        """
        self._model_deployment_instance_shape_config_details = model_deployment_instance_shape_config_details

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this InstanceConfiguration.
        A model deployment instance is provided with a VNIC for network access.  This specifies the `OCID`__ of the subnet to create a VNIC in.  The subnet should be in a VCN with a NAT/SGW gateway for egress.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this InstanceConfiguration.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this InstanceConfiguration.
        A model deployment instance is provided with a VNIC for network access.  This specifies the `OCID`__ of the subnet to create a VNIC in.  The subnet should be in a VCN with a NAT/SGW gateway for egress.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this InstanceConfiguration.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_id(self):
        """
        Gets the private_endpoint_id of this InstanceConfiguration.
        The OCID of a Data Science private endpoint.


        :return: The private_endpoint_id of this InstanceConfiguration.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this InstanceConfiguration.
        The OCID of a Data Science private endpoint.


        :param private_endpoint_id: The private_endpoint_id of this InstanceConfiguration.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
