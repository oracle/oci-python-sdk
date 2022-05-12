# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployStageSummary(object):
    """
    Summary of the deployment stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeployStageSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.ComputeInstanceGroupBlueGreenDeployStageSummary`
        * :class:`~oci.devops.models.ComputeInstanceGroupBlueGreenTrafficShiftDeployStageSummary`
        * :class:`~oci.devops.models.OkeBlueGreenDeployStageSummary`
        * :class:`~oci.devops.models.WaitDeployStageSummary`
        * :class:`~oci.devops.models.OkeDeployStageSummary`
        * :class:`~oci.devops.models.ComputeInstanceGroupCanaryApprovalDeployStageSummary`
        * :class:`~oci.devops.models.InvokeFunctionDeployStageSummary`
        * :class:`~oci.devops.models.OkeHelmChartDeployStageSummary`
        * :class:`~oci.devops.models.OkeCanaryTrafficShiftDeployStageSummary`
        * :class:`~oci.devops.models.ComputeInstanceGroupDeployStageSummary`
        * :class:`~oci.devops.models.ComputeInstanceGroupCanaryDeployStageSummary`
        * :class:`~oci.devops.models.OkeCanaryApprovalDeployStageSummary`
        * :class:`~oci.devops.models.OkeCanaryDeployStageSummary`
        * :class:`~oci.devops.models.LoadBalancerTrafficShiftDeployStageSummary`
        * :class:`~oci.devops.models.ManualApprovalDeployStageSummary`
        * :class:`~oci.devops.models.OkeBlueGreenTrafficShiftDeployStageSummary`
        * :class:`~oci.devops.models.FunctionDeployStageSummary`
        * :class:`~oci.devops.models.ComputeInstanceGroupCanaryTrafficShiftDeployStageSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DeployStageSummary.
        :type id: str

        :param description:
            The value to assign to the description property of this DeployStageSummary.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this DeployStageSummary.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this DeployStageSummary.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this DeployStageSummary.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeployStageSummary.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this DeployStageSummary.
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this DeployStageSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeployStageSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeployStageSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeployStageSummary.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this DeployStageSummary.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeployStageSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeployStageSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeployStageSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'deploy_pipeline_id': 'str',
            'compartment_id': 'str',
            'deploy_stage_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'deploy_stage_predecessor_collection': 'DeployStagePredecessorCollection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'display_name': 'displayName',
            'project_id': 'projectId',
            'deploy_pipeline_id': 'deployPipelineId',
            'compartment_id': 'compartmentId',
            'deploy_stage_type': 'deployStageType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'deploy_stage_predecessor_collection': 'deployStagePredecessorCollection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._description = None
        self._display_name = None
        self._project_id = None
        self._deploy_pipeline_id = None
        self._compartment_id = None
        self._deploy_stage_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._deploy_stage_predecessor_collection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deployStageType']

        if type == 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT':
            return 'ComputeInstanceGroupBlueGreenDeployStageSummary'

        if type == 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT':
            return 'ComputeInstanceGroupBlueGreenTrafficShiftDeployStageSummary'

        if type == 'OKE_BLUE_GREEN_DEPLOYMENT':
            return 'OkeBlueGreenDeployStageSummary'

        if type == 'WAIT':
            return 'WaitDeployStageSummary'

        if type == 'OKE_DEPLOYMENT':
            return 'OkeDeployStageSummary'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL':
            return 'ComputeInstanceGroupCanaryApprovalDeployStageSummary'

        if type == 'INVOKE_FUNCTION':
            return 'InvokeFunctionDeployStageSummary'

        if type == 'OKE_HELM_CHART_DEPLOYMENT':
            return 'OkeHelmChartDeployStageSummary'

        if type == 'OKE_CANARY_TRAFFIC_SHIFT':
            return 'OkeCanaryTrafficShiftDeployStageSummary'

        if type == 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT':
            return 'ComputeInstanceGroupDeployStageSummary'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT':
            return 'ComputeInstanceGroupCanaryDeployStageSummary'

        if type == 'OKE_CANARY_APPROVAL':
            return 'OkeCanaryApprovalDeployStageSummary'

        if type == 'OKE_CANARY_DEPLOYMENT':
            return 'OkeCanaryDeployStageSummary'

        if type == 'LOAD_BALANCER_TRAFFIC_SHIFT':
            return 'LoadBalancerTrafficShiftDeployStageSummary'

        if type == 'MANUAL_APPROVAL':
            return 'ManualApprovalDeployStageSummary'

        if type == 'OKE_BLUE_GREEN_TRAFFIC_SHIFT':
            return 'OkeBlueGreenTrafficShiftDeployStageSummary'

        if type == 'DEPLOY_FUNCTION':
            return 'FunctionDeployStageSummary'

        if type == 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT':
            return 'ComputeInstanceGroupCanaryTrafficShiftDeployStageSummary'
        else:
            return 'DeployStageSummary'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DeployStageSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this DeployStageSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeployStageSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this DeployStageSummary.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this DeployStageSummary.
        Optional description about the deployment stage.


        :return: The description of this DeployStageSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeployStageSummary.
        Optional description about the deployment stage.


        :param description: The description of this DeployStageSummary.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this DeployStageSummary.
        Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this DeployStageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeployStageSummary.
        Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this DeployStageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this DeployStageSummary.
        The OCID of a project.


        :return: The project_id of this DeployStageSummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this DeployStageSummary.
        The OCID of a project.


        :param project_id: The project_id of this DeployStageSummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def deploy_pipeline_id(self):
        """
        **[Required]** Gets the deploy_pipeline_id of this DeployStageSummary.
        The OCID of a pipeline.


        :return: The deploy_pipeline_id of this DeployStageSummary.
        :rtype: str
        """
        return self._deploy_pipeline_id

    @deploy_pipeline_id.setter
    def deploy_pipeline_id(self, deploy_pipeline_id):
        """
        Sets the deploy_pipeline_id of this DeployStageSummary.
        The OCID of a pipeline.


        :param deploy_pipeline_id: The deploy_pipeline_id of this DeployStageSummary.
        :type: str
        """
        self._deploy_pipeline_id = deploy_pipeline_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DeployStageSummary.
        The OCID of a compartment.


        :return: The compartment_id of this DeployStageSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DeployStageSummary.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this DeployStageSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deploy_stage_type(self):
        """
        **[Required]** Gets the deploy_stage_type of this DeployStageSummary.
        Deployment stage type.


        :return: The deploy_stage_type of this DeployStageSummary.
        :rtype: str
        """
        return self._deploy_stage_type

    @deploy_stage_type.setter
    def deploy_stage_type(self, deploy_stage_type):
        """
        Sets the deploy_stage_type of this DeployStageSummary.
        Deployment stage type.


        :param deploy_stage_type: The deploy_stage_type of this DeployStageSummary.
        :type: str
        """
        self._deploy_stage_type = deploy_stage_type

    @property
    def time_created(self):
        """
        Gets the time_created of this DeployStageSummary.
        Time the deployment stage was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this DeployStageSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DeployStageSummary.
        Time the deployment stage was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this DeployStageSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DeployStageSummary.
        Time the deployment stage was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this DeployStageSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DeployStageSummary.
        Time the deployment stage was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this DeployStageSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DeployStageSummary.
        The current state of the deployment stage.


        :return: The lifecycle_state of this DeployStageSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DeployStageSummary.
        The current state of the deployment stage.


        :param lifecycle_state: The lifecycle_state of this DeployStageSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DeployStageSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DeployStageSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DeployStageSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DeployStageSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def deploy_stage_predecessor_collection(self):
        """
        Gets the deploy_stage_predecessor_collection of this DeployStageSummary.

        :return: The deploy_stage_predecessor_collection of this DeployStageSummary.
        :rtype: oci.devops.models.DeployStagePredecessorCollection
        """
        return self._deploy_stage_predecessor_collection

    @deploy_stage_predecessor_collection.setter
    def deploy_stage_predecessor_collection(self, deploy_stage_predecessor_collection):
        """
        Sets the deploy_stage_predecessor_collection of this DeployStageSummary.

        :param deploy_stage_predecessor_collection: The deploy_stage_predecessor_collection of this DeployStageSummary.
        :type: oci.devops.models.DeployStagePredecessorCollection
        """
        self._deploy_stage_predecessor_collection = deploy_stage_predecessor_collection

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DeployStageSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DeployStageSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DeployStageSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DeployStageSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DeployStageSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DeployStageSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DeployStageSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DeployStageSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DeployStageSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DeployStageSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DeployStageSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DeployStageSummary.
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
