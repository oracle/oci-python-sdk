# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeploymentDetails(object):
    """
    The information about new deployment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeploymentDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.CreateDeployPipelineRedeploymentDetails`
        * :class:`~oci.devops.models.CreateDeployPipelineDeploymentDetails`
        * :class:`~oci.devops.models.CreateSingleDeployStageDeploymentDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this CreateDeploymentDetails.
        :type deploy_pipeline_id: str

        :param deployment_type:
            The value to assign to the deployment_type property of this CreateDeploymentDetails.
        :type deployment_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateDeploymentDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeploymentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeploymentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'deploy_pipeline_id': 'str',
            'deployment_type': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'deploy_pipeline_id': 'deployPipelineId',
            'deployment_type': 'deploymentType',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._deploy_pipeline_id = None
        self._deployment_type = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deploymentType']

        if type == 'PIPELINE_REDEPLOYMENT':
            return 'CreateDeployPipelineRedeploymentDetails'

        if type == 'PIPELINE_DEPLOYMENT':
            return 'CreateDeployPipelineDeploymentDetails'

        if type == 'SINGLE_STAGE_DEPLOYMENT':
            return 'CreateSingleDeployStageDeploymentDetails'
        else:
            return 'CreateDeploymentDetails'

    @property
    def deploy_pipeline_id(self):
        """
        **[Required]** Gets the deploy_pipeline_id of this CreateDeploymentDetails.
        The OCID of a pipeline.


        :return: The deploy_pipeline_id of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._deploy_pipeline_id

    @deploy_pipeline_id.setter
    def deploy_pipeline_id(self, deploy_pipeline_id):
        """
        Sets the deploy_pipeline_id of this CreateDeploymentDetails.
        The OCID of a pipeline.


        :param deploy_pipeline_id: The deploy_pipeline_id of this CreateDeploymentDetails.
        :type: str
        """
        self._deploy_pipeline_id = deploy_pipeline_id

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this CreateDeploymentDetails.
        Specifies type for this deployment.


        :return: The deployment_type of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this CreateDeploymentDetails.
        Specifies type for this deployment.


        :param deployment_type: The deployment_type of this CreateDeploymentDetails.
        :type: str
        """
        self._deployment_type = deployment_type

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDeploymentDetails.
        Deployment display name. Avoid entering confidential information.


        :return: The display_name of this CreateDeploymentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDeploymentDetails.
        Deployment display name. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDeploymentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDeploymentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDeploymentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDeploymentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDeploymentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDeploymentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDeploymentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDeploymentDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
