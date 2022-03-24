# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Deployment(object):
    """
    A single execution or run of a pipeline.
    """

    #: A constant which can be used with the deployment_type property of a Deployment.
    #: This constant has a value of "PIPELINE_DEPLOYMENT"
    DEPLOYMENT_TYPE_PIPELINE_DEPLOYMENT = "PIPELINE_DEPLOYMENT"

    #: A constant which can be used with the deployment_type property of a Deployment.
    #: This constant has a value of "PIPELINE_REDEPLOYMENT"
    DEPLOYMENT_TYPE_PIPELINE_REDEPLOYMENT = "PIPELINE_REDEPLOYMENT"

    #: A constant which can be used with the deployment_type property of a Deployment.
    #: This constant has a value of "SINGLE_STAGE_DEPLOYMENT"
    DEPLOYMENT_TYPE_SINGLE_STAGE_DEPLOYMENT = "SINGLE_STAGE_DEPLOYMENT"

    #: A constant which can be used with the deployment_type property of a Deployment.
    #: This constant has a value of "SINGLE_STAGE_REDEPLOYMENT"
    DEPLOYMENT_TYPE_SINGLE_STAGE_REDEPLOYMENT = "SINGLE_STAGE_REDEPLOYMENT"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a Deployment.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new Deployment object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.SingleDeployStageRedeployment`
        * :class:`~oci.devops.models.DeployPipelineDeployment`
        * :class:`~oci.devops.models.DeployPipelineRedeployment`
        * :class:`~oci.devops.models.SingleDeployStageDeployment`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param deploy_pipeline_artifacts:
            The value to assign to the deploy_pipeline_artifacts property of this Deployment.
        :type deploy_pipeline_artifacts: oci.devops.models.DeployPipelineArtifactCollection

        :param deploy_pipeline_environments:
            The value to assign to the deploy_pipeline_environments property of this Deployment.
        :type deploy_pipeline_environments: oci.devops.models.DeployPipelineEnvironmentCollection

        :param deployment_type:
            The value to assign to the deployment_type property of this Deployment.
            Allowed values for this property are: "PIPELINE_DEPLOYMENT", "PIPELINE_REDEPLOYMENT", "SINGLE_STAGE_DEPLOYMENT", "SINGLE_STAGE_REDEPLOYMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param id:
            The value to assign to the id property of this Deployment.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Deployment.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this Deployment.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this Deployment.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Deployment.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this Deployment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Deployment.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Deployment.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Deployment.
        :type lifecycle_details: str

        :param deployment_arguments:
            The value to assign to the deployment_arguments property of this Deployment.
        :type deployment_arguments: oci.devops.models.DeploymentArgumentCollection

        :param deploy_artifact_override_arguments:
            The value to assign to the deploy_artifact_override_arguments property of this Deployment.
        :type deploy_artifact_override_arguments: oci.devops.models.DeployArtifactOverrideArgumentCollection

        :param deployment_execution_progress:
            The value to assign to the deployment_execution_progress property of this Deployment.
        :type deployment_execution_progress: oci.devops.models.DeploymentExecutionProgress

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Deployment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Deployment.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Deployment.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'deploy_pipeline_artifacts': 'DeployPipelineArtifactCollection',
            'deploy_pipeline_environments': 'DeployPipelineEnvironmentCollection',
            'deployment_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deployment_arguments': 'DeploymentArgumentCollection',
            'deploy_artifact_override_arguments': 'DeployArtifactOverrideArgumentCollection',
            'deployment_execution_progress': 'DeploymentExecutionProgress',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'deploy_pipeline_artifacts': 'deployPipelineArtifacts',
            'deploy_pipeline_environments': 'deployPipelineEnvironments',
            'deployment_type': 'deploymentType',
            'id': 'id',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deployment_arguments': 'deploymentArguments',
            'deploy_artifact_override_arguments': 'deployArtifactOverrideArguments',
            'deployment_execution_progress': 'deploymentExecutionProgress',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._deploy_pipeline_artifacts = None
        self._deploy_pipeline_environments = None
        self._deployment_type = None
        self._id = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deployment_arguments = None
        self._deploy_artifact_override_arguments = None
        self._deployment_execution_progress = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deploymentType']

        if type == 'SINGLE_STAGE_REDEPLOYMENT':
            return 'SingleDeployStageRedeployment'

        if type == 'PIPELINE_DEPLOYMENT':
            return 'DeployPipelineDeployment'

        if type == 'PIPELINE_REDEPLOYMENT':
            return 'DeployPipelineRedeployment'

        if type == 'SINGLE_STAGE_DEPLOYMENT':
            return 'SingleDeployStageDeployment'
        else:
            return 'Deployment'

    @property
    def deploy_pipeline_artifacts(self):
        """
        Gets the deploy_pipeline_artifacts of this Deployment.

        :return: The deploy_pipeline_artifacts of this Deployment.
        :rtype: oci.devops.models.DeployPipelineArtifactCollection
        """
        return self._deploy_pipeline_artifacts

    @deploy_pipeline_artifacts.setter
    def deploy_pipeline_artifacts(self, deploy_pipeline_artifacts):
        """
        Sets the deploy_pipeline_artifacts of this Deployment.

        :param deploy_pipeline_artifacts: The deploy_pipeline_artifacts of this Deployment.
        :type: oci.devops.models.DeployPipelineArtifactCollection
        """
        self._deploy_pipeline_artifacts = deploy_pipeline_artifacts

    @property
    def deploy_pipeline_environments(self):
        """
        Gets the deploy_pipeline_environments of this Deployment.

        :return: The deploy_pipeline_environments of this Deployment.
        :rtype: oci.devops.models.DeployPipelineEnvironmentCollection
        """
        return self._deploy_pipeline_environments

    @deploy_pipeline_environments.setter
    def deploy_pipeline_environments(self, deploy_pipeline_environments):
        """
        Sets the deploy_pipeline_environments of this Deployment.

        :param deploy_pipeline_environments: The deploy_pipeline_environments of this Deployment.
        :type: oci.devops.models.DeployPipelineEnvironmentCollection
        """
        self._deploy_pipeline_environments = deploy_pipeline_environments

    @property
    def deployment_type(self):
        """
        **[Required]** Gets the deployment_type of this Deployment.
        Specifies type of deployment.

        Allowed values for this property are: "PIPELINE_DEPLOYMENT", "PIPELINE_REDEPLOYMENT", "SINGLE_STAGE_DEPLOYMENT", "SINGLE_STAGE_REDEPLOYMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this Deployment.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this Deployment.
        Specifies type of deployment.


        :param deployment_type: The deployment_type of this Deployment.
        :type: str
        """
        allowed_values = ["PIPELINE_DEPLOYMENT", "PIPELINE_REDEPLOYMENT", "SINGLE_STAGE_DEPLOYMENT", "SINGLE_STAGE_REDEPLOYMENT"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Deployment.
        Unique identifier that is immutable on creation.


        :return: The id of this Deployment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Deployment.
        Unique identifier that is immutable on creation.


        :param id: The id of this Deployment.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Deployment.
        Deployment identifier which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this Deployment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Deployment.
        Deployment identifier which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this Deployment.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this Deployment.
        The OCID of a project.


        :return: The project_id of this Deployment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this Deployment.
        The OCID of a project.


        :param project_id: The project_id of this Deployment.
        :type: str
        """
        self._project_id = project_id

    @property
    def deploy_pipeline_id(self):
        """
        **[Required]** Gets the deploy_pipeline_id of this Deployment.
        The OCID of a pipeline.


        :return: The deploy_pipeline_id of this Deployment.
        :rtype: str
        """
        return self._deploy_pipeline_id

    @deploy_pipeline_id.setter
    def deploy_pipeline_id(self, deploy_pipeline_id):
        """
        Sets the deploy_pipeline_id of this Deployment.
        The OCID of a pipeline.


        :param deploy_pipeline_id: The deploy_pipeline_id of this Deployment.
        :type: str
        """
        self._deploy_pipeline_id = deploy_pipeline_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Deployment.
        The OCID of a compartment.


        :return: The compartment_id of this Deployment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Deployment.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this Deployment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Deployment.
        Time the deployment was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this Deployment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Deployment.
        Time the deployment was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this Deployment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Deployment.
        Time the deployment was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this Deployment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Deployment.
        Time the deployment was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this Deployment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Deployment.
        The current state of the deployment.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Deployment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Deployment.
        The current state of the deployment.


        :param lifecycle_state: The lifecycle_state of this Deployment.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Deployment.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this Deployment.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Deployment.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Deployment.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def deployment_arguments(self):
        """
        Gets the deployment_arguments of this Deployment.

        :return: The deployment_arguments of this Deployment.
        :rtype: oci.devops.models.DeploymentArgumentCollection
        """
        return self._deployment_arguments

    @deployment_arguments.setter
    def deployment_arguments(self, deployment_arguments):
        """
        Sets the deployment_arguments of this Deployment.

        :param deployment_arguments: The deployment_arguments of this Deployment.
        :type: oci.devops.models.DeploymentArgumentCollection
        """
        self._deployment_arguments = deployment_arguments

    @property
    def deploy_artifact_override_arguments(self):
        """
        Gets the deploy_artifact_override_arguments of this Deployment.

        :return: The deploy_artifact_override_arguments of this Deployment.
        :rtype: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        return self._deploy_artifact_override_arguments

    @deploy_artifact_override_arguments.setter
    def deploy_artifact_override_arguments(self, deploy_artifact_override_arguments):
        """
        Sets the deploy_artifact_override_arguments of this Deployment.

        :param deploy_artifact_override_arguments: The deploy_artifact_override_arguments of this Deployment.
        :type: oci.devops.models.DeployArtifactOverrideArgumentCollection
        """
        self._deploy_artifact_override_arguments = deploy_artifact_override_arguments

    @property
    def deployment_execution_progress(self):
        """
        Gets the deployment_execution_progress of this Deployment.

        :return: The deployment_execution_progress of this Deployment.
        :rtype: oci.devops.models.DeploymentExecutionProgress
        """
        return self._deployment_execution_progress

    @deployment_execution_progress.setter
    def deployment_execution_progress(self, deployment_execution_progress):
        """
        Sets the deployment_execution_progress of this Deployment.

        :param deployment_execution_progress: The deployment_execution_progress of this Deployment.
        :type: oci.devops.models.DeploymentExecutionProgress
        """
        self._deployment_execution_progress = deployment_execution_progress

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Deployment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Deployment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Deployment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Deployment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Deployment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Deployment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Deployment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Deployment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Deployment.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Deployment.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Deployment.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Deployment.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
