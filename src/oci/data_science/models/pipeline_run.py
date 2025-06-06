# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineRun(object):
    """
    Description of PipelineRun.
    """

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a PipelineRun.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineRun object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PipelineRun.
        :type id: str

        :param time_accepted:
            The value to assign to the time_accepted property of this PipelineRun.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this PipelineRun.
        :type time_started: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PipelineRun.
        :type time_updated: datetime

        :param time_finished:
            The value to assign to the time_finished property of this PipelineRun.
        :type time_finished: datetime

        :param created_by:
            The value to assign to the created_by property of this PipelineRun.
        :type created_by: str

        :param project_id:
            The value to assign to the project_id property of this PipelineRun.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PipelineRun.
        :type compartment_id: str

        :param pipeline_id:
            The value to assign to the pipeline_id property of this PipelineRun.
        :type pipeline_id: str

        :param display_name:
            The value to assign to the display_name property of this PipelineRun.
        :type display_name: str

        :param configuration_details:
            The value to assign to the configuration_details property of this PipelineRun.
        :type configuration_details: oci.data_science.models.PipelineConfigurationDetails

        :param configuration_override_details:
            The value to assign to the configuration_override_details property of this PipelineRun.
        :type configuration_override_details: oci.data_science.models.PipelineConfigurationDetails

        :param log_configuration_override_details:
            The value to assign to the log_configuration_override_details property of this PipelineRun.
        :type log_configuration_override_details: oci.data_science.models.PipelineLogConfigurationDetails

        :param step_override_details:
            The value to assign to the step_override_details property of this PipelineRun.
        :type step_override_details: list[oci.data_science.models.PipelineStepOverrideDetails]

        :param log_details:
            The value to assign to the log_details property of this PipelineRun.
        :type log_details: oci.data_science.models.PipelineRunLogDetails

        :param step_runs:
            The value to assign to the step_runs property of this PipelineRun.
        :type step_runs: list[oci.data_science.models.PipelineStepRun]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PipelineRun.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PipelineRun.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PipelineRun.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PipelineRun.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PipelineRun.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_updated': 'datetime',
            'time_finished': 'datetime',
            'created_by': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'pipeline_id': 'str',
            'display_name': 'str',
            'configuration_details': 'PipelineConfigurationDetails',
            'configuration_override_details': 'PipelineConfigurationDetails',
            'log_configuration_override_details': 'PipelineLogConfigurationDetails',
            'step_override_details': 'list[PipelineStepOverrideDetails]',
            'log_details': 'PipelineRunLogDetails',
            'step_runs': 'list[PipelineStepRun]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_updated': 'timeUpdated',
            'time_finished': 'timeFinished',
            'created_by': 'createdBy',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'pipeline_id': 'pipelineId',
            'display_name': 'displayName',
            'configuration_details': 'configurationDetails',
            'configuration_override_details': 'configurationOverrideDetails',
            'log_configuration_override_details': 'logConfigurationOverrideDetails',
            'step_override_details': 'stepOverrideDetails',
            'log_details': 'logDetails',
            'step_runs': 'stepRuns',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._time_accepted = None
        self._time_started = None
        self._time_updated = None
        self._time_finished = None
        self._created_by = None
        self._project_id = None
        self._compartment_id = None
        self._pipeline_id = None
        self._display_name = None
        self._configuration_details = None
        self._configuration_override_details = None
        self._log_configuration_override_details = None
        self._step_override_details = None
        self._log_details = None
        self._step_runs = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PipelineRun.
        The `OCID`__ of the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this PipelineRun.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelineRun.
        The `OCID`__ of the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this PipelineRun.
        :type: str
        """
        self._id = id

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this PipelineRun.
        The date and time the pipeline run was accepted in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_accepted of this PipelineRun.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this PipelineRun.
        The date and time the pipeline run was accepted in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_accepted: The time_accepted of this PipelineRun.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this PipelineRun.
        The date and time the pipeline run request was started in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this PipelineRun.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PipelineRun.
        The date and time the pipeline run request was started in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this PipelineRun.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_updated(self):
        """
        Gets the time_updated of this PipelineRun.
        The date and time the pipeline run was updated in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this PipelineRun.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PipelineRun.
        The date and time the pipeline run was updated in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this PipelineRun.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_finished(self):
        """
        Gets the time_finished of this PipelineRun.
        The date and time the pipeline run request was finished in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this PipelineRun.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this PipelineRun.
        The date and time the pipeline run request was finished in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_finished: The time_finished of this PipelineRun.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def created_by(self):
        """
        **[Required]** Gets the created_by of this PipelineRun.
        The `OCID`__ of the user who created the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The created_by of this PipelineRun.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this PipelineRun.
        The `OCID`__ of the user who created the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param created_by: The created_by of this PipelineRun.
        :type: str
        """
        self._created_by = created_by

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this PipelineRun.
        The `OCID`__ of the project to associate the pipeline run with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this PipelineRun.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this PipelineRun.
        The `OCID`__ of the project to associate the pipeline run with.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this PipelineRun.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PipelineRun.
        The `OCID`__ of the compartment where you want to create the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PipelineRun.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PipelineRun.
        The `OCID`__ of the compartment where you want to create the pipeline run.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PipelineRun.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def pipeline_id(self):
        """
        **[Required]** Gets the pipeline_id of this PipelineRun.
        The `OCID`__ of the pipeline.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The pipeline_id of this PipelineRun.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """
        Sets the pipeline_id of this PipelineRun.
        The `OCID`__ of the pipeline.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param pipeline_id: The pipeline_id of this PipelineRun.
        :type: str
        """
        self._pipeline_id = pipeline_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PipelineRun.
        A user-friendly display name for the resource.


        :return: The display_name of this PipelineRun.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PipelineRun.
        A user-friendly display name for the resource.


        :param display_name: The display_name of this PipelineRun.
        :type: str
        """
        self._display_name = display_name

    @property
    def configuration_details(self):
        """
        Gets the configuration_details of this PipelineRun.

        :return: The configuration_details of this PipelineRun.
        :rtype: oci.data_science.models.PipelineConfigurationDetails
        """
        return self._configuration_details

    @configuration_details.setter
    def configuration_details(self, configuration_details):
        """
        Sets the configuration_details of this PipelineRun.

        :param configuration_details: The configuration_details of this PipelineRun.
        :type: oci.data_science.models.PipelineConfigurationDetails
        """
        self._configuration_details = configuration_details

    @property
    def configuration_override_details(self):
        """
        Gets the configuration_override_details of this PipelineRun.

        :return: The configuration_override_details of this PipelineRun.
        :rtype: oci.data_science.models.PipelineConfigurationDetails
        """
        return self._configuration_override_details

    @configuration_override_details.setter
    def configuration_override_details(self, configuration_override_details):
        """
        Sets the configuration_override_details of this PipelineRun.

        :param configuration_override_details: The configuration_override_details of this PipelineRun.
        :type: oci.data_science.models.PipelineConfigurationDetails
        """
        self._configuration_override_details = configuration_override_details

    @property
    def log_configuration_override_details(self):
        """
        Gets the log_configuration_override_details of this PipelineRun.

        :return: The log_configuration_override_details of this PipelineRun.
        :rtype: oci.data_science.models.PipelineLogConfigurationDetails
        """
        return self._log_configuration_override_details

    @log_configuration_override_details.setter
    def log_configuration_override_details(self, log_configuration_override_details):
        """
        Sets the log_configuration_override_details of this PipelineRun.

        :param log_configuration_override_details: The log_configuration_override_details of this PipelineRun.
        :type: oci.data_science.models.PipelineLogConfigurationDetails
        """
        self._log_configuration_override_details = log_configuration_override_details

    @property
    def step_override_details(self):
        """
        Gets the step_override_details of this PipelineRun.
        Array of step override details. Only Step Configuration is allowed to be overridden.


        :return: The step_override_details of this PipelineRun.
        :rtype: list[oci.data_science.models.PipelineStepOverrideDetails]
        """
        return self._step_override_details

    @step_override_details.setter
    def step_override_details(self, step_override_details):
        """
        Sets the step_override_details of this PipelineRun.
        Array of step override details. Only Step Configuration is allowed to be overridden.


        :param step_override_details: The step_override_details of this PipelineRun.
        :type: list[oci.data_science.models.PipelineStepOverrideDetails]
        """
        self._step_override_details = step_override_details

    @property
    def log_details(self):
        """
        Gets the log_details of this PipelineRun.

        :return: The log_details of this PipelineRun.
        :rtype: oci.data_science.models.PipelineRunLogDetails
        """
        return self._log_details

    @log_details.setter
    def log_details(self, log_details):
        """
        Sets the log_details of this PipelineRun.

        :param log_details: The log_details of this PipelineRun.
        :type: oci.data_science.models.PipelineRunLogDetails
        """
        self._log_details = log_details

    @property
    def step_runs(self):
        """
        **[Required]** Gets the step_runs of this PipelineRun.
        Array of StepRun object for each step.


        :return: The step_runs of this PipelineRun.
        :rtype: list[oci.data_science.models.PipelineStepRun]
        """
        return self._step_runs

    @step_runs.setter
    def step_runs(self, step_runs):
        """
        Sets the step_runs of this PipelineRun.
        Array of StepRun object for each step.


        :param step_runs: The step_runs of this PipelineRun.
        :type: list[oci.data_science.models.PipelineStepRun]
        """
        self._step_runs = step_runs

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PipelineRun.
        The current state of the pipeline run.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PipelineRun.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PipelineRun.
        The current state of the pipeline run.


        :param lifecycle_state: The lifecycle_state of this PipelineRun.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PipelineRun.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :return: The lifecycle_details of this PipelineRun.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PipelineRun.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed' state.


        :param lifecycle_details: The lifecycle_details of this PipelineRun.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PipelineRun.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PipelineRun.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PipelineRun.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PipelineRun.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PipelineRun.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PipelineRun.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PipelineRun.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PipelineRun.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this PipelineRun.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this PipelineRun.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this PipelineRun.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this PipelineRun.
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
