# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineSummary(object):
    """
    Summary details of the pipeline.
    """

    #: A constant which can be used with the recipe_type property of a PipelineSummary.
    #: This constant has a value of "ZERO_ETL"
    RECIPE_TYPE_ZERO_ETL = "ZERO_ETL"

    #: A constant which can be used with the license_model property of a PipelineSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a PipelineSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the lifecycle_sub_state property of a PipelineSummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_SUB_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_sub_state property of a PipelineSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_SUB_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_sub_state property of a PipelineSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_SUB_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_sub_state property of a PipelineSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_SUB_STATE_MOVING = "MOVING"

    #: A constant which can be used with the lifecycle_sub_state property of a PipelineSummary.
    #: This constant has a value of "RUNNING"
    LIFECYCLE_SUB_STATE_RUNNING = "RUNNING"

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.golden_gate.models.ZeroEtlPipelineSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recipe_type:
            The value to assign to the recipe_type property of this PipelineSummary.
            Allowed values for this property are: "ZERO_ETL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type recipe_type: str

        :param id:
            The value to assign to the id property of this PipelineSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this PipelineSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this PipelineSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PipelineSummary.
        :type compartment_id: str

        :param source_connection_details:
            The value to assign to the source_connection_details property of this PipelineSummary.
        :type source_connection_details: oci.golden_gate.models.SourcePipelineConnectionDetails

        :param target_connection_details:
            The value to assign to the target_connection_details property of this PipelineSummary.
        :type target_connection_details: oci.golden_gate.models.TargetPipelineConnectionDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PipelineSummary.
        :type freeform_tags: dict(str, str)

        :param license_model:
            The value to assign to the license_model property of this PipelineSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this PipelineSummary.
        :type cpu_core_count: int

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this PipelineSummary.
        :type is_auto_scaling_enabled: bool

        :param defined_tags:
            The value to assign to the defined_tags property of this PipelineSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this PipelineSummary.
        :type system_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this PipelineSummary.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PipelineSummary.
        :type lifecycle_state: str

        :param lifecycle_sub_state:
            The value to assign to the lifecycle_sub_state property of this PipelineSummary.
            Allowed values for this property are: "STARTING", "STOPPING", "STOPPED", "MOVING", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_sub_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PipelineSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this PipelineSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this PipelineSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'recipe_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'source_connection_details': 'SourcePipelineConnectionDetails',
            'target_connection_details': 'TargetPipelineConnectionDetails',
            'freeform_tags': 'dict(str, str)',
            'license_model': 'str',
            'cpu_core_count': 'int',
            'is_auto_scaling_enabled': 'bool',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'locks': 'list[ResourceLock]',
            'lifecycle_state': 'str',
            'lifecycle_sub_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'recipe_type': 'recipeType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'source_connection_details': 'sourceConnectionDetails',
            'target_connection_details': 'targetConnectionDetails',
            'freeform_tags': 'freeformTags',
            'license_model': 'licenseModel',
            'cpu_core_count': 'cpuCoreCount',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'locks': 'locks',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_sub_state': 'lifecycleSubState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._recipe_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._source_connection_details = None
        self._target_connection_details = None
        self._freeform_tags = None
        self._license_model = None
        self._cpu_core_count = None
        self._is_auto_scaling_enabled = None
        self._defined_tags = None
        self._system_tags = None
        self._locks = None
        self._lifecycle_state = None
        self._lifecycle_sub_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['recipeType']

        if type == 'ZERO_ETL':
            return 'ZeroEtlPipelineSummary'
        else:
            return 'PipelineSummary'

    @property
    def recipe_type(self):
        """
        **[Required]** Gets the recipe_type of this PipelineSummary.
        The type of the recipe

        Allowed values for this property are: "ZERO_ETL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The recipe_type of this PipelineSummary.
        :rtype: str
        """
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        """
        Sets the recipe_type of this PipelineSummary.
        The type of the recipe


        :param recipe_type: The recipe_type of this PipelineSummary.
        :type: str
        """
        allowed_values = ["ZERO_ETL"]
        if not value_allowed_none_or_none_sentinel(recipe_type, allowed_values):
            recipe_type = 'UNKNOWN_ENUM_VALUE'
        self._recipe_type = recipe_type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PipelineSummary.
        The `OCID`__ of the pipeline. This option applies when retrieving a pipeline.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this PipelineSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PipelineSummary.
        The `OCID`__ of the pipeline. This option applies when retrieving a pipeline.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this PipelineSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PipelineSummary.
        An object's Display Name.


        :return: The display_name of this PipelineSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PipelineSummary.
        An object's Display Name.


        :param display_name: The display_name of this PipelineSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this PipelineSummary.
        Metadata about this specific object.


        :return: The description of this PipelineSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PipelineSummary.
        Metadata about this specific object.


        :param description: The description of this PipelineSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PipelineSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PipelineSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PipelineSummary.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PipelineSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def source_connection_details(self):
        """
        **[Required]** Gets the source_connection_details of this PipelineSummary.

        :return: The source_connection_details of this PipelineSummary.
        :rtype: oci.golden_gate.models.SourcePipelineConnectionDetails
        """
        return self._source_connection_details

    @source_connection_details.setter
    def source_connection_details(self, source_connection_details):
        """
        Sets the source_connection_details of this PipelineSummary.

        :param source_connection_details: The source_connection_details of this PipelineSummary.
        :type: oci.golden_gate.models.SourcePipelineConnectionDetails
        """
        self._source_connection_details = source_connection_details

    @property
    def target_connection_details(self):
        """
        **[Required]** Gets the target_connection_details of this PipelineSummary.

        :return: The target_connection_details of this PipelineSummary.
        :rtype: oci.golden_gate.models.TargetPipelineConnectionDetails
        """
        return self._target_connection_details

    @target_connection_details.setter
    def target_connection_details(self, target_connection_details):
        """
        Sets the target_connection_details of this PipelineSummary.

        :param target_connection_details: The target_connection_details of this PipelineSummary.
        :type: oci.golden_gate.models.TargetPipelineConnectionDetails
        """
        self._target_connection_details = target_connection_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PipelineSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this PipelineSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PipelineSummary.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this PipelineSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def license_model(self):
        """
        **[Required]** Gets the license_model of this PipelineSummary.
        The Oracle license model that applies to a Deployment.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this PipelineSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this PipelineSummary.
        The Oracle license model that applies to a Deployment.


        :param license_model: The license_model of this PipelineSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this PipelineSummary.
        The Minimum number of OCPUs to be made available for this Deployment.


        :return: The cpu_core_count of this PipelineSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this PipelineSummary.
        The Minimum number of OCPUs to be made available for this Deployment.


        :param cpu_core_count: The cpu_core_count of this PipelineSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def is_auto_scaling_enabled(self):
        """
        **[Required]** Gets the is_auto_scaling_enabled of this PipelineSummary.
        Indicates if auto scaling is enabled for the Deployment's CPU core count.


        :return: The is_auto_scaling_enabled of this PipelineSummary.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this PipelineSummary.
        Indicates if auto scaling is enabled for the Deployment's CPU core count.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this PipelineSummary.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PipelineSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this PipelineSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PipelineSummary.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this PipelineSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this PipelineSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this PipelineSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this PipelineSummary.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this PipelineSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def locks(self):
        """
        Gets the locks of this PipelineSummary.
        Locks associated with this resource.


        :return: The locks of this PipelineSummary.
        :rtype: list[oci.golden_gate.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this PipelineSummary.
        Locks associated with this resource.


        :param locks: The locks of this PipelineSummary.
        :type: list[oci.golden_gate.models.ResourceLock]
        """
        self._locks = locks

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PipelineSummary.
        Lifecycle state for the pipeline summary.


        :return: The lifecycle_state of this PipelineSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PipelineSummary.
        Lifecycle state for the pipeline summary.


        :param lifecycle_state: The lifecycle_state of this PipelineSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_sub_state(self):
        """
        Gets the lifecycle_sub_state of this PipelineSummary.
        Possible lifecycle substates when retrieving a pipeline.

        Allowed values for this property are: "STARTING", "STOPPING", "STOPPED", "MOVING", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_sub_state of this PipelineSummary.
        :rtype: str
        """
        return self._lifecycle_sub_state

    @lifecycle_sub_state.setter
    def lifecycle_sub_state(self, lifecycle_sub_state):
        """
        Sets the lifecycle_sub_state of this PipelineSummary.
        Possible lifecycle substates when retrieving a pipeline.


        :param lifecycle_sub_state: The lifecycle_sub_state of this PipelineSummary.
        :type: str
        """
        allowed_values = ["STARTING", "STOPPING", "STOPPED", "MOVING", "RUNNING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_sub_state, allowed_values):
            lifecycle_sub_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_sub_state = lifecycle_sub_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PipelineSummary.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this PipelineSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PipelineSummary.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this PipelineSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PipelineSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PipelineSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PipelineSummary.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PipelineSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this PipelineSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this PipelineSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this PipelineSummary.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this PipelineSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
