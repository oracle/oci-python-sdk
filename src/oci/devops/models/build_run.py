# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildRun(object):
    """
    Each time you attempt to run a build pipeline you create one build run.
    A build can be running currently, or it can be a record of the run that happened in the past.
    The set of build runs constitutes a build pipeline's history.
    """

    #: A constant which can be used with the lifecycle_state property of a BuildRun.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a BuildRun.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a BuildRun.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a BuildRun.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a BuildRun.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a BuildRun.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new BuildRun object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BuildRun.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BuildRun.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BuildRun.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this BuildRun.
        :type project_id: str

        :param build_pipeline_id:
            The value to assign to the build_pipeline_id property of this BuildRun.
        :type build_pipeline_id: str

        :param build_run_source:
            The value to assign to the build_run_source property of this BuildRun.
        :type build_run_source: oci.devops.models.BuildRunSource

        :param build_run_arguments:
            The value to assign to the build_run_arguments property of this BuildRun.
        :type build_run_arguments: oci.devops.models.BuildRunArgumentCollection

        :param time_created:
            The value to assign to the time_created property of this BuildRun.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BuildRun.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BuildRun.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this BuildRun.
        :type lifecycle_details: str

        :param build_run_progress:
            The value to assign to the build_run_progress property of this BuildRun.
        :type build_run_progress: oci.devops.models.BuildRunProgress

        :param commit_info:
            The value to assign to the commit_info property of this BuildRun.
        :type commit_info: oci.devops.models.CommitInfo

        :param build_outputs:
            The value to assign to the build_outputs property of this BuildRun.
        :type build_outputs: oci.devops.models.BuildOutputs

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BuildRun.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BuildRun.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this BuildRun.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'build_pipeline_id': 'str',
            'build_run_source': 'BuildRunSource',
            'build_run_arguments': 'BuildRunArgumentCollection',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'build_run_progress': 'BuildRunProgress',
            'commit_info': 'CommitInfo',
            'build_outputs': 'BuildOutputs',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'build_pipeline_id': 'buildPipelineId',
            'build_run_source': 'buildRunSource',
            'build_run_arguments': 'buildRunArguments',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'build_run_progress': 'buildRunProgress',
            'commit_info': 'commitInfo',
            'build_outputs': 'buildOutputs',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._project_id = None
        self._build_pipeline_id = None
        self._build_run_source = None
        self._build_run_arguments = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._build_run_progress = None
        self._commit_info = None
        self._build_outputs = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BuildRun.
        Unique identifier that is immutable on creation.


        :return: The id of this BuildRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildRun.
        Unique identifier that is immutable on creation.


        :param id: The id of this BuildRun.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this BuildRun.
        Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this BuildRun.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BuildRun.
        Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this BuildRun.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BuildRun.
        The OCID of the compartment where the build is running.


        :return: The compartment_id of this BuildRun.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BuildRun.
        The OCID of the compartment where the build is running.


        :param compartment_id: The compartment_id of this BuildRun.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        Gets the project_id of this BuildRun.
        The OCID of the DevOps project.


        :return: The project_id of this BuildRun.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this BuildRun.
        The OCID of the DevOps project.


        :param project_id: The project_id of this BuildRun.
        :type: str
        """
        self._project_id = project_id

    @property
    def build_pipeline_id(self):
        """
        Gets the build_pipeline_id of this BuildRun.
        The OCID of the build pipeline.


        :return: The build_pipeline_id of this BuildRun.
        :rtype: str
        """
        return self._build_pipeline_id

    @build_pipeline_id.setter
    def build_pipeline_id(self, build_pipeline_id):
        """
        Sets the build_pipeline_id of this BuildRun.
        The OCID of the build pipeline.


        :param build_pipeline_id: The build_pipeline_id of this BuildRun.
        :type: str
        """
        self._build_pipeline_id = build_pipeline_id

    @property
    def build_run_source(self):
        """
        **[Required]** Gets the build_run_source of this BuildRun.

        :return: The build_run_source of this BuildRun.
        :rtype: oci.devops.models.BuildRunSource
        """
        return self._build_run_source

    @build_run_source.setter
    def build_run_source(self, build_run_source):
        """
        Sets the build_run_source of this BuildRun.

        :param build_run_source: The build_run_source of this BuildRun.
        :type: oci.devops.models.BuildRunSource
        """
        self._build_run_source = build_run_source

    @property
    def build_run_arguments(self):
        """
        Gets the build_run_arguments of this BuildRun.

        :return: The build_run_arguments of this BuildRun.
        :rtype: oci.devops.models.BuildRunArgumentCollection
        """
        return self._build_run_arguments

    @build_run_arguments.setter
    def build_run_arguments(self, build_run_arguments):
        """
        Sets the build_run_arguments of this BuildRun.

        :param build_run_arguments: The build_run_arguments of this BuildRun.
        :type: oci.devops.models.BuildRunArgumentCollection
        """
        self._build_run_arguments = build_run_arguments

    @property
    def time_created(self):
        """
        Gets the time_created of this BuildRun.
        The time the build run was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this BuildRun.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BuildRun.
        The time the build run was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this BuildRun.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BuildRun.
        The time the build run was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this BuildRun.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BuildRun.
        The time the build run was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this BuildRun.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BuildRun.
        The current state of the build run.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BuildRun.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BuildRun.
        The current state of the build run.


        :param lifecycle_state: The lifecycle_state of this BuildRun.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this BuildRun.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this BuildRun.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this BuildRun.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this BuildRun.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def build_run_progress(self):
        """
        Gets the build_run_progress of this BuildRun.

        :return: The build_run_progress of this BuildRun.
        :rtype: oci.devops.models.BuildRunProgress
        """
        return self._build_run_progress

    @build_run_progress.setter
    def build_run_progress(self, build_run_progress):
        """
        Sets the build_run_progress of this BuildRun.

        :param build_run_progress: The build_run_progress of this BuildRun.
        :type: oci.devops.models.BuildRunProgress
        """
        self._build_run_progress = build_run_progress

    @property
    def commit_info(self):
        """
        Gets the commit_info of this BuildRun.

        :return: The commit_info of this BuildRun.
        :rtype: oci.devops.models.CommitInfo
        """
        return self._commit_info

    @commit_info.setter
    def commit_info(self, commit_info):
        """
        Sets the commit_info of this BuildRun.

        :param commit_info: The commit_info of this BuildRun.
        :type: oci.devops.models.CommitInfo
        """
        self._commit_info = commit_info

    @property
    def build_outputs(self):
        """
        Gets the build_outputs of this BuildRun.

        :return: The build_outputs of this BuildRun.
        :rtype: oci.devops.models.BuildOutputs
        """
        return self._build_outputs

    @build_outputs.setter
    def build_outputs(self, build_outputs):
        """
        Sets the build_outputs of this BuildRun.

        :param build_outputs: The build_outputs of this BuildRun.
        :type: oci.devops.models.BuildOutputs
        """
        self._build_outputs = build_outputs

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BuildRun.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BuildRun.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BuildRun.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BuildRun.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BuildRun.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BuildRun.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BuildRun.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BuildRun.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this BuildRun.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this BuildRun.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this BuildRun.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this BuildRun.
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
