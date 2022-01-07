# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateModelDeploymentConfigurationDetails(object):
    """
    The model deployment configuration details for update.
    """

    #: A constant which can be used with the deployment_type property of a UpdateModelDeploymentConfigurationDetails.
    #: This constant has a value of "SINGLE_MODEL"
    DEPLOYMENT_TYPE_SINGLE_MODEL = "SINGLE_MODEL"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateModelDeploymentConfigurationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.UpdateSingleModelDeploymentConfigurationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deployment_type:
            The value to assign to the deployment_type property of this UpdateModelDeploymentConfigurationDetails.
            Allowed values for this property are: "SINGLE_MODEL"
        :type deployment_type: str

        """
        self.swagger_types = {
            'deployment_type': 'str'
        }

        self.attribute_map = {
            'deployment_type': 'deploymentType'
        }

        self._deployment_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deploymentType']

        if type == 'SINGLE_MODEL':
            return 'UpdateSingleModelDeploymentConfigurationDetails'
        else:
            return 'UpdateModelDeploymentConfigurationDetails'

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this UpdateModelDeploymentConfigurationDetails.
        The type of the model deployment.

        Allowed values for this property are: "SINGLE_MODEL"


        :return: The deployment_type of this UpdateModelDeploymentConfigurationDetails.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this UpdateModelDeploymentConfigurationDetails.
        The type of the model deployment.


        :param deployment_type: The deployment_type of this UpdateModelDeploymentConfigurationDetails.
        :type: str
        """
        allowed_values = ["SINGLE_MODEL"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            raise ValueError(
                "Invalid value for `deployment_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._deployment_type = deployment_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
