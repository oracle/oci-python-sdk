# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployStage(object):
    """
    A single node in a pipeline. It is usually associated with some action on a specific set of OCI resources such as environments. For example, updating a Function or a Kubernetes cluster.
    """

    #: A constant which can be used with the deploy_stage_type property of a DeployStage.
    #: This constant has a value of "WAIT"
    DEPLOY_STAGE_TYPE_WAIT = "WAIT"

    #: A constant which can be used with the deploy_stage_type property of a DeployStage.
    #: This constant has a value of "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT"
    DEPLOY_STAGE_TYPE_COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT = "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT"

    #: A constant which can be used with the deploy_stage_type property of a DeployStage.
    #: This constant has a value of "OKE_DEPLOYMENT"
    DEPLOY_STAGE_TYPE_OKE_DEPLOYMENT = "OKE_DEPLOYMENT"

    #: A constant which can be used with the deploy_stage_type property of a DeployStage.
    #: This constant has a value of "DEPLOY_FUNCTION"
    DEPLOY_STAGE_TYPE_DEPLOY_FUNCTION = "DEPLOY_FUNCTION"

    #: A constant which can be used with the deploy_stage_type property of a DeployStage.
    #: This constant has a value of "INVOKE_FUNCTION"
    DEPLOY_STAGE_TYPE_INVOKE_FUNCTION = "INVOKE_FUNCTION"

    #: A constant which can be used with the deploy_stage_type property of a DeployStage.
    #: This constant has a value of "LOAD_BALANCER_TRAFFIC_SHIFT"
    DEPLOY_STAGE_TYPE_LOAD_BALANCER_TRAFFIC_SHIFT = "LOAD_BALANCER_TRAFFIC_SHIFT"

    #: A constant which can be used with the deploy_stage_type property of a DeployStage.
    #: This constant has a value of "MANUAL_APPROVAL"
    DEPLOY_STAGE_TYPE_MANUAL_APPROVAL = "MANUAL_APPROVAL"

    #: A constant which can be used with the lifecycle_state property of a DeployStage.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DeployStage.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DeployStage.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeployStage.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DeployStage.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DeployStage.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeployStage object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.LoadBalancerTrafficShiftDeployStage`
        * :class:`~oci.devops.models.InvokeFunctionDeployStage`
        * :class:`~oci.devops.models.WaitDeployStage`
        * :class:`~oci.devops.models.OkeDeployStage`
        * :class:`~oci.devops.models.ManualApprovalDeployStage`
        * :class:`~oci.devops.models.ComputeInstanceGroupDeployStage`
        * :class:`~oci.devops.models.FunctionDeployStage`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DeployStage.
        :type id: str

        :param description:
            The value to assign to the description property of this DeployStage.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this DeployStage.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this DeployStage.
        :type project_id: str

        :param deploy_pipeline_id:
            The value to assign to the deploy_pipeline_id property of this DeployStage.
        :type deploy_pipeline_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeployStage.
        :type compartment_id: str

        :param deploy_stage_type:
            The value to assign to the deploy_stage_type property of this DeployStage.
            Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deploy_stage_type: str

        :param time_created:
            The value to assign to the time_created property of this DeployStage.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeployStage.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeployStage.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeployStage.
        :type lifecycle_details: str

        :param deploy_stage_predecessor_collection:
            The value to assign to the deploy_stage_predecessor_collection property of this DeployStage.
        :type deploy_stage_predecessor_collection: oci.devops.models.DeployStagePredecessorCollection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeployStage.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeployStage.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeployStage.
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

        if type == 'LOAD_BALANCER_TRAFFIC_SHIFT':
            return 'LoadBalancerTrafficShiftDeployStage'

        if type == 'INVOKE_FUNCTION':
            return 'InvokeFunctionDeployStage'

        if type == 'WAIT':
            return 'WaitDeployStage'

        if type == 'OKE_DEPLOYMENT':
            return 'OkeDeployStage'

        if type == 'MANUAL_APPROVAL':
            return 'ManualApprovalDeployStage'

        if type == 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT':
            return 'ComputeInstanceGroupDeployStage'

        if type == 'DEPLOY_FUNCTION':
            return 'FunctionDeployStage'
        else:
            return 'DeployStage'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DeployStage.
        Unique identifier that is immutable on creation.


        :return: The id of this DeployStage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeployStage.
        Unique identifier that is immutable on creation.


        :param id: The id of this DeployStage.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this DeployStage.
        Optional description about the deployment stage.


        :return: The description of this DeployStage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeployStage.
        Optional description about the deployment stage.


        :param description: The description of this DeployStage.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this DeployStage.
        Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this DeployStage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeployStage.
        Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this DeployStage.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this DeployStage.
        The OCID of a project.


        :return: The project_id of this DeployStage.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this DeployStage.
        The OCID of a project.


        :param project_id: The project_id of this DeployStage.
        :type: str
        """
        self._project_id = project_id

    @property
    def deploy_pipeline_id(self):
        """
        **[Required]** Gets the deploy_pipeline_id of this DeployStage.
        The OCID of a pipeline.


        :return: The deploy_pipeline_id of this DeployStage.
        :rtype: str
        """
        return self._deploy_pipeline_id

    @deploy_pipeline_id.setter
    def deploy_pipeline_id(self, deploy_pipeline_id):
        """
        Sets the deploy_pipeline_id of this DeployStage.
        The OCID of a pipeline.


        :param deploy_pipeline_id: The deploy_pipeline_id of this DeployStage.
        :type: str
        """
        self._deploy_pipeline_id = deploy_pipeline_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DeployStage.
        The OCID of a compartment.


        :return: The compartment_id of this DeployStage.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DeployStage.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this DeployStage.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deploy_stage_type(self):
        """
        **[Required]** Gets the deploy_stage_type of this DeployStage.
        Deployment stage type.

        Allowed values for this property are: "WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deploy_stage_type of this DeployStage.
        :rtype: str
        """
        return self._deploy_stage_type

    @deploy_stage_type.setter
    def deploy_stage_type(self, deploy_stage_type):
        """
        Sets the deploy_stage_type of this DeployStage.
        Deployment stage type.


        :param deploy_stage_type: The deploy_stage_type of this DeployStage.
        :type: str
        """
        allowed_values = ["WAIT", "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT", "OKE_DEPLOYMENT", "DEPLOY_FUNCTION", "INVOKE_FUNCTION", "LOAD_BALANCER_TRAFFIC_SHIFT", "MANUAL_APPROVAL"]
        if not value_allowed_none_or_none_sentinel(deploy_stage_type, allowed_values):
            deploy_stage_type = 'UNKNOWN_ENUM_VALUE'
        self._deploy_stage_type = deploy_stage_type

    @property
    def time_created(self):
        """
        Gets the time_created of this DeployStage.
        Time the deployment stage was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this DeployStage.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DeployStage.
        Time the deployment stage was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this DeployStage.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DeployStage.
        Time the deployment stage was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this DeployStage.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DeployStage.
        Time the deployment stage was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this DeployStage.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DeployStage.
        The current state of the deployment stage.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DeployStage.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DeployStage.
        The current state of the deployment stage.


        :param lifecycle_state: The lifecycle_state of this DeployStage.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DeployStage.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DeployStage.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DeployStage.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DeployStage.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def deploy_stage_predecessor_collection(self):
        """
        Gets the deploy_stage_predecessor_collection of this DeployStage.

        :return: The deploy_stage_predecessor_collection of this DeployStage.
        :rtype: oci.devops.models.DeployStagePredecessorCollection
        """
        return self._deploy_stage_predecessor_collection

    @deploy_stage_predecessor_collection.setter
    def deploy_stage_predecessor_collection(self, deploy_stage_predecessor_collection):
        """
        Sets the deploy_stage_predecessor_collection of this DeployStage.

        :param deploy_stage_predecessor_collection: The deploy_stage_predecessor_collection of this DeployStage.
        :type: oci.devops.models.DeployStagePredecessorCollection
        """
        self._deploy_stage_predecessor_collection = deploy_stage_predecessor_collection

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DeployStage.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DeployStage.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DeployStage.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DeployStage.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DeployStage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DeployStage.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DeployStage.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DeployStage.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DeployStage.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DeployStage.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DeployStage.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DeployStage.
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
