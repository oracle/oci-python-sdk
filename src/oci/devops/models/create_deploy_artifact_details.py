# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDeployArtifactDetails(object):
    """
    Information about a new deployment artifact.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDeployArtifactDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this CreateDeployArtifactDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateDeployArtifactDetails.
        :type display_name: str

        :param deploy_artifact_type:
            The value to assign to the deploy_artifact_type property of this CreateDeployArtifactDetails.
        :type deploy_artifact_type: str

        :param deploy_artifact_source:
            The value to assign to the deploy_artifact_source property of this CreateDeployArtifactDetails.
        :type deploy_artifact_source: oci.devops.models.DeployArtifactSource

        :param argument_substitution_mode:
            The value to assign to the argument_substitution_mode property of this CreateDeployArtifactDetails.
        :type argument_substitution_mode: str

        :param project_id:
            The value to assign to the project_id property of this CreateDeployArtifactDetails.
        :type project_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDeployArtifactDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDeployArtifactDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'deploy_artifact_type': 'str',
            'deploy_artifact_source': 'DeployArtifactSource',
            'argument_substitution_mode': 'str',
            'project_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'deploy_artifact_type': 'deployArtifactType',
            'deploy_artifact_source': 'deployArtifactSource',
            'argument_substitution_mode': 'argumentSubstitutionMode',
            'project_id': 'projectId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._description = None
        self._display_name = None
        self._deploy_artifact_type = None
        self._deploy_artifact_source = None
        self._argument_substitution_mode = None
        self._project_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def description(self):
        """
        Gets the description of this CreateDeployArtifactDetails.
        Optional description about the deployment artifact.


        :return: The description of this CreateDeployArtifactDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDeployArtifactDetails.
        Optional description about the deployment artifact.


        :param description: The description of this CreateDeployArtifactDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDeployArtifactDetails.
        Deployment artifact display name. Avoid entering confidential information.


        :return: The display_name of this CreateDeployArtifactDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDeployArtifactDetails.
        Deployment artifact display name. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDeployArtifactDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def deploy_artifact_type(self):
        """
        **[Required]** Gets the deploy_artifact_type of this CreateDeployArtifactDetails.
        Type of the deployment artifact.


        :return: The deploy_artifact_type of this CreateDeployArtifactDetails.
        :rtype: str
        """
        return self._deploy_artifact_type

    @deploy_artifact_type.setter
    def deploy_artifact_type(self, deploy_artifact_type):
        """
        Sets the deploy_artifact_type of this CreateDeployArtifactDetails.
        Type of the deployment artifact.


        :param deploy_artifact_type: The deploy_artifact_type of this CreateDeployArtifactDetails.
        :type: str
        """
        self._deploy_artifact_type = deploy_artifact_type

    @property
    def deploy_artifact_source(self):
        """
        **[Required]** Gets the deploy_artifact_source of this CreateDeployArtifactDetails.

        :return: The deploy_artifact_source of this CreateDeployArtifactDetails.
        :rtype: oci.devops.models.DeployArtifactSource
        """
        return self._deploy_artifact_source

    @deploy_artifact_source.setter
    def deploy_artifact_source(self, deploy_artifact_source):
        """
        Sets the deploy_artifact_source of this CreateDeployArtifactDetails.

        :param deploy_artifact_source: The deploy_artifact_source of this CreateDeployArtifactDetails.
        :type: oci.devops.models.DeployArtifactSource
        """
        self._deploy_artifact_source = deploy_artifact_source

    @property
    def argument_substitution_mode(self):
        """
        **[Required]** Gets the argument_substitution_mode of this CreateDeployArtifactDetails.
        Mode for artifact parameter substitution.


        :return: The argument_substitution_mode of this CreateDeployArtifactDetails.
        :rtype: str
        """
        return self._argument_substitution_mode

    @argument_substitution_mode.setter
    def argument_substitution_mode(self, argument_substitution_mode):
        """
        Sets the argument_substitution_mode of this CreateDeployArtifactDetails.
        Mode for artifact parameter substitution.


        :param argument_substitution_mode: The argument_substitution_mode of this CreateDeployArtifactDetails.
        :type: str
        """
        self._argument_substitution_mode = argument_substitution_mode

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateDeployArtifactDetails.
        The OCID of a project.


        :return: The project_id of this CreateDeployArtifactDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateDeployArtifactDetails.
        The OCID of a project.


        :param project_id: The project_id of this CreateDeployArtifactDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDeployArtifactDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDeployArtifactDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDeployArtifactDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDeployArtifactDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDeployArtifactDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDeployArtifactDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDeployArtifactDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDeployArtifactDetails.
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
