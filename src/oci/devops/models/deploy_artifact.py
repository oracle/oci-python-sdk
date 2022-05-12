# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployArtifact(object):
    """
    Artifacts are deployment manifests that are referenced in a pipeline stage for automated deployment to the target environment.  DevOps artifacts can be an OCI Container image repository, Kubernetes manifest, an Artifact Registry artifact, or defined inline.
    """

    #: A constant which can be used with the deploy_artifact_type property of a DeployArtifact.
    #: This constant has a value of "DEPLOYMENT_SPEC"
    DEPLOY_ARTIFACT_TYPE_DEPLOYMENT_SPEC = "DEPLOYMENT_SPEC"

    #: A constant which can be used with the deploy_artifact_type property of a DeployArtifact.
    #: This constant has a value of "JOB_SPEC"
    DEPLOY_ARTIFACT_TYPE_JOB_SPEC = "JOB_SPEC"

    #: A constant which can be used with the deploy_artifact_type property of a DeployArtifact.
    #: This constant has a value of "KUBERNETES_MANIFEST"
    DEPLOY_ARTIFACT_TYPE_KUBERNETES_MANIFEST = "KUBERNETES_MANIFEST"

    #: A constant which can be used with the deploy_artifact_type property of a DeployArtifact.
    #: This constant has a value of "GENERIC_FILE"
    DEPLOY_ARTIFACT_TYPE_GENERIC_FILE = "GENERIC_FILE"

    #: A constant which can be used with the deploy_artifact_type property of a DeployArtifact.
    #: This constant has a value of "DOCKER_IMAGE"
    DEPLOY_ARTIFACT_TYPE_DOCKER_IMAGE = "DOCKER_IMAGE"

    #: A constant which can be used with the deploy_artifact_type property of a DeployArtifact.
    #: This constant has a value of "HELM_CHART"
    DEPLOY_ARTIFACT_TYPE_HELM_CHART = "HELM_CHART"

    #: A constant which can be used with the argument_substitution_mode property of a DeployArtifact.
    #: This constant has a value of "NONE"
    ARGUMENT_SUBSTITUTION_MODE_NONE = "NONE"

    #: A constant which can be used with the argument_substitution_mode property of a DeployArtifact.
    #: This constant has a value of "SUBSTITUTE_PLACEHOLDERS"
    ARGUMENT_SUBSTITUTION_MODE_SUBSTITUTE_PLACEHOLDERS = "SUBSTITUTE_PLACEHOLDERS"

    #: A constant which can be used with the lifecycle_state property of a DeployArtifact.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DeployArtifact.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DeployArtifact.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeployArtifact.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DeployArtifact.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DeployArtifact.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeployArtifact object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DeployArtifact.
        :type id: str

        :param description:
            The value to assign to the description property of this DeployArtifact.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this DeployArtifact.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this DeployArtifact.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeployArtifact.
        :type compartment_id: str

        :param deploy_artifact_type:
            The value to assign to the deploy_artifact_type property of this DeployArtifact.
            Allowed values for this property are: "DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deploy_artifact_type: str

        :param argument_substitution_mode:
            The value to assign to the argument_substitution_mode property of this DeployArtifact.
            Allowed values for this property are: "NONE", "SUBSTITUTE_PLACEHOLDERS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type argument_substitution_mode: str

        :param deploy_artifact_source:
            The value to assign to the deploy_artifact_source property of this DeployArtifact.
        :type deploy_artifact_source: oci.devops.models.DeployArtifactSource

        :param time_created:
            The value to assign to the time_created property of this DeployArtifact.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeployArtifact.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeployArtifact.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeployArtifact.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeployArtifact.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeployArtifact.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeployArtifact.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'deploy_artifact_type': 'str',
            'argument_substitution_mode': 'str',
            'deploy_artifact_source': 'DeployArtifactSource',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'deploy_artifact_type': 'deployArtifactType',
            'argument_substitution_mode': 'argumentSubstitutionMode',
            'deploy_artifact_source': 'deployArtifactSource',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._compartment_id = None
        self._deploy_artifact_type = None
        self._argument_substitution_mode = None
        self._deploy_artifact_source = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DeployArtifact.
        Unique identifier that is immutable on creation.


        :return: The id of this DeployArtifact.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeployArtifact.
        Unique identifier that is immutable on creation.


        :param id: The id of this DeployArtifact.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this DeployArtifact.
        Optional description about the artifact to be deployed.


        :return: The description of this DeployArtifact.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeployArtifact.
        Optional description about the artifact to be deployed.


        :param description: The description of this DeployArtifact.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this DeployArtifact.
        Deployment artifact identifier, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this DeployArtifact.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeployArtifact.
        Deployment artifact identifier, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this DeployArtifact.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this DeployArtifact.
        The OCID of a project.


        :return: The project_id of this DeployArtifact.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this DeployArtifact.
        The OCID of a project.


        :param project_id: The project_id of this DeployArtifact.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DeployArtifact.
        The OCID of a compartment.


        :return: The compartment_id of this DeployArtifact.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DeployArtifact.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this DeployArtifact.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deploy_artifact_type(self):
        """
        **[Required]** Gets the deploy_artifact_type of this DeployArtifact.
        Type of the deployment artifact.

        Allowed values for this property are: "DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE", "HELM_CHART", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deploy_artifact_type of this DeployArtifact.
        :rtype: str
        """
        return self._deploy_artifact_type

    @deploy_artifact_type.setter
    def deploy_artifact_type(self, deploy_artifact_type):
        """
        Sets the deploy_artifact_type of this DeployArtifact.
        Type of the deployment artifact.


        :param deploy_artifact_type: The deploy_artifact_type of this DeployArtifact.
        :type: str
        """
        allowed_values = ["DEPLOYMENT_SPEC", "JOB_SPEC", "KUBERNETES_MANIFEST", "GENERIC_FILE", "DOCKER_IMAGE", "HELM_CHART"]
        if not value_allowed_none_or_none_sentinel(deploy_artifact_type, allowed_values):
            deploy_artifact_type = 'UNKNOWN_ENUM_VALUE'
        self._deploy_artifact_type = deploy_artifact_type

    @property
    def argument_substitution_mode(self):
        """
        **[Required]** Gets the argument_substitution_mode of this DeployArtifact.
        Mode for artifact parameter substitution.

        Allowed values for this property are: "NONE", "SUBSTITUTE_PLACEHOLDERS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The argument_substitution_mode of this DeployArtifact.
        :rtype: str
        """
        return self._argument_substitution_mode

    @argument_substitution_mode.setter
    def argument_substitution_mode(self, argument_substitution_mode):
        """
        Sets the argument_substitution_mode of this DeployArtifact.
        Mode for artifact parameter substitution.


        :param argument_substitution_mode: The argument_substitution_mode of this DeployArtifact.
        :type: str
        """
        allowed_values = ["NONE", "SUBSTITUTE_PLACEHOLDERS"]
        if not value_allowed_none_or_none_sentinel(argument_substitution_mode, allowed_values):
            argument_substitution_mode = 'UNKNOWN_ENUM_VALUE'
        self._argument_substitution_mode = argument_substitution_mode

    @property
    def deploy_artifact_source(self):
        """
        **[Required]** Gets the deploy_artifact_source of this DeployArtifact.

        :return: The deploy_artifact_source of this DeployArtifact.
        :rtype: oci.devops.models.DeployArtifactSource
        """
        return self._deploy_artifact_source

    @deploy_artifact_source.setter
    def deploy_artifact_source(self, deploy_artifact_source):
        """
        Sets the deploy_artifact_source of this DeployArtifact.

        :param deploy_artifact_source: The deploy_artifact_source of this DeployArtifact.
        :type: oci.devops.models.DeployArtifactSource
        """
        self._deploy_artifact_source = deploy_artifact_source

    @property
    def time_created(self):
        """
        Gets the time_created of this DeployArtifact.
        Time the deployment artifact was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this DeployArtifact.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DeployArtifact.
        Time the deployment artifact was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this DeployArtifact.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DeployArtifact.
        Time the deployment artifact was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this DeployArtifact.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DeployArtifact.
        Time the deployment artifact was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this DeployArtifact.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DeployArtifact.
        Current state of the deployment artifact.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DeployArtifact.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DeployArtifact.
        Current state of the deployment artifact.


        :param lifecycle_state: The lifecycle_state of this DeployArtifact.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DeployArtifact.
        A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DeployArtifact.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DeployArtifact.
        A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DeployArtifact.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DeployArtifact.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DeployArtifact.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DeployArtifact.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DeployArtifact.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DeployArtifact.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DeployArtifact.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DeployArtifact.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DeployArtifact.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DeployArtifact.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DeployArtifact.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DeployArtifact.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DeployArtifact.
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
