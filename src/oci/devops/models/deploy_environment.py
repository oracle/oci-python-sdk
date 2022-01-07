# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeployEnvironment(object):
    """
    The target OCI resources, such as Compute instances, Container Engine for Kubernetes(OKE) clusters, or Function, where artifacts will be deployed.
    """

    #: A constant which can be used with the deploy_environment_type property of a DeployEnvironment.
    #: This constant has a value of "OKE_CLUSTER"
    DEPLOY_ENVIRONMENT_TYPE_OKE_CLUSTER = "OKE_CLUSTER"

    #: A constant which can be used with the deploy_environment_type property of a DeployEnvironment.
    #: This constant has a value of "COMPUTE_INSTANCE_GROUP"
    DEPLOY_ENVIRONMENT_TYPE_COMPUTE_INSTANCE_GROUP = "COMPUTE_INSTANCE_GROUP"

    #: A constant which can be used with the deploy_environment_type property of a DeployEnvironment.
    #: This constant has a value of "FUNCTION"
    DEPLOY_ENVIRONMENT_TYPE_FUNCTION = "FUNCTION"

    #: A constant which can be used with the lifecycle_state property of a DeployEnvironment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DeployEnvironment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DeployEnvironment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DeployEnvironment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DeployEnvironment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DeployEnvironment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DeployEnvironment object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.ComputeInstanceGroupDeployEnvironment`
        * :class:`~oci.devops.models.OkeClusterDeployEnvironment`
        * :class:`~oci.devops.models.FunctionDeployEnvironment`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DeployEnvironment.
        :type id: str

        :param description:
            The value to assign to the description property of this DeployEnvironment.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this DeployEnvironment.
        :type display_name: str

        :param project_id:
            The value to assign to the project_id property of this DeployEnvironment.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DeployEnvironment.
        :type compartment_id: str

        :param deploy_environment_type:
            The value to assign to the deploy_environment_type property of this DeployEnvironment.
            Allowed values for this property are: "OKE_CLUSTER", "COMPUTE_INSTANCE_GROUP", "FUNCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deploy_environment_type: str

        :param time_created:
            The value to assign to the time_created property of this DeployEnvironment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DeployEnvironment.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DeployEnvironment.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DeployEnvironment.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DeployEnvironment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DeployEnvironment.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DeployEnvironment.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'display_name': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'deploy_environment_type': 'str',
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
            'deploy_environment_type': 'deployEnvironmentType',
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
        self._deploy_environment_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['deployEnvironmentType']

        if type == 'COMPUTE_INSTANCE_GROUP':
            return 'ComputeInstanceGroupDeployEnvironment'

        if type == 'OKE_CLUSTER':
            return 'OkeClusterDeployEnvironment'

        if type == 'FUNCTION':
            return 'FunctionDeployEnvironment'
        else:
            return 'DeployEnvironment'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DeployEnvironment.
        Unique identifier that is immutable on creation.


        :return: The id of this DeployEnvironment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DeployEnvironment.
        Unique identifier that is immutable on creation.


        :param id: The id of this DeployEnvironment.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this DeployEnvironment.
        Optional description about the deployment environment.


        :return: The description of this DeployEnvironment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeployEnvironment.
        Optional description about the deployment environment.


        :param description: The description of this DeployEnvironment.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this DeployEnvironment.
        Deployment environment display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :return: The display_name of this DeployEnvironment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DeployEnvironment.
        Deployment environment display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.


        :param display_name: The display_name of this DeployEnvironment.
        :type: str
        """
        self._display_name = display_name

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this DeployEnvironment.
        The OCID of a project.


        :return: The project_id of this DeployEnvironment.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this DeployEnvironment.
        The OCID of a project.


        :param project_id: The project_id of this DeployEnvironment.
        :type: str
        """
        self._project_id = project_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DeployEnvironment.
        The OCID of a compartment.


        :return: The compartment_id of this DeployEnvironment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DeployEnvironment.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this DeployEnvironment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deploy_environment_type(self):
        """
        **[Required]** Gets the deploy_environment_type of this DeployEnvironment.
        Deployment environment type.

        Allowed values for this property are: "OKE_CLUSTER", "COMPUTE_INSTANCE_GROUP", "FUNCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deploy_environment_type of this DeployEnvironment.
        :rtype: str
        """
        return self._deploy_environment_type

    @deploy_environment_type.setter
    def deploy_environment_type(self, deploy_environment_type):
        """
        Sets the deploy_environment_type of this DeployEnvironment.
        Deployment environment type.


        :param deploy_environment_type: The deploy_environment_type of this DeployEnvironment.
        :type: str
        """
        allowed_values = ["OKE_CLUSTER", "COMPUTE_INSTANCE_GROUP", "FUNCTION"]
        if not value_allowed_none_or_none_sentinel(deploy_environment_type, allowed_values):
            deploy_environment_type = 'UNKNOWN_ENUM_VALUE'
        self._deploy_environment_type = deploy_environment_type

    @property
    def time_created(self):
        """
        Gets the time_created of this DeployEnvironment.
        Time the deployment environment was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this DeployEnvironment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DeployEnvironment.
        Time the deployment environment was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this DeployEnvironment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DeployEnvironment.
        Time the deployment environment was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this DeployEnvironment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DeployEnvironment.
        Time the deployment environment was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this DeployEnvironment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DeployEnvironment.
        The current state of the deployment environment.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DeployEnvironment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DeployEnvironment.
        The current state of the deployment environment.


        :param lifecycle_state: The lifecycle_state of this DeployEnvironment.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DeployEnvironment.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DeployEnvironment.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DeployEnvironment.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DeployEnvironment.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DeployEnvironment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this DeployEnvironment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DeployEnvironment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this DeployEnvironment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DeployEnvironment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this DeployEnvironment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DeployEnvironment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this DeployEnvironment.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DeployEnvironment.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DeployEnvironment.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DeployEnvironment.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DeployEnvironment.
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
