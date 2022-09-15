# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationPlanSummary(object):
    """
    Summary of the migration plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationPlanSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MigrationPlanSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MigrationPlanSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MigrationPlanSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this MigrationPlanSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MigrationPlanSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MigrationPlanSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MigrationPlanSummary.
        :type lifecycle_details: str

        :param migration_id:
            The value to assign to the migration_id property of this MigrationPlanSummary.
        :type migration_id: str

        :param strategies:
            The value to assign to the strategies property of this MigrationPlanSummary.
        :type strategies: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]

        :param migration_plan_stats:
            The value to assign to the migration_plan_stats property of this MigrationPlanSummary.
        :type migration_plan_stats: oci.cloud_migrations.models.MigrationPlanStats

        :param calculated_limits:
            The value to assign to the calculated_limits property of this MigrationPlanSummary.
        :type calculated_limits: dict(str, int)

        :param target_environments:
            The value to assign to the target_environments property of this MigrationPlanSummary.
        :type target_environments: list[oci.cloud_migrations.models.TargetEnvironment]

        :param reference_to_rms_stack:
            The value to assign to the reference_to_rms_stack property of this MigrationPlanSummary.
        :type reference_to_rms_stack: str

        :param source_migration_plan_id:
            The value to assign to the source_migration_plan_id property of this MigrationPlanSummary.
        :type source_migration_plan_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MigrationPlanSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MigrationPlanSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MigrationPlanSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'migration_id': 'str',
            'strategies': 'list[ResourceAssessmentStrategy]',
            'migration_plan_stats': 'MigrationPlanStats',
            'calculated_limits': 'dict(str, int)',
            'target_environments': 'list[TargetEnvironment]',
            'reference_to_rms_stack': 'str',
            'source_migration_plan_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'migration_id': 'migrationId',
            'strategies': 'strategies',
            'migration_plan_stats': 'migrationPlanStats',
            'calculated_limits': 'calculatedLimits',
            'target_environments': 'targetEnvironments',
            'reference_to_rms_stack': 'referenceToRmsStack',
            'source_migration_plan_id': 'sourceMigrationPlanId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._migration_id = None
        self._strategies = None
        self._migration_plan_stats = None
        self._calculated_limits = None
        self._target_environments = None
        self._reference_to_rms_stack = None
        self._source_migration_plan_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MigrationPlanSummary.
        The unique Oracle ID (OCID) that is immutable on creation.


        :return: The id of this MigrationPlanSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MigrationPlanSummary.
        The unique Oracle ID (OCID) that is immutable on creation.


        :param id: The id of this MigrationPlanSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MigrationPlanSummary.
        The OCID of the compartment containing the migration plan.


        :return: The compartment_id of this MigrationPlanSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MigrationPlanSummary.
        The OCID of the compartment containing the migration plan.


        :param compartment_id: The compartment_id of this MigrationPlanSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this MigrationPlanSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this MigrationPlanSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MigrationPlanSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this MigrationPlanSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MigrationPlanSummary.
        The time when the migration plan was created. An RFC3339 formatted datetime string.


        :return: The time_created of this MigrationPlanSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MigrationPlanSummary.
        The time when the migration plan was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MigrationPlanSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MigrationPlanSummary.
        The time when the migration plan was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this MigrationPlanSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MigrationPlanSummary.
        The time when the migration plan was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MigrationPlanSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MigrationPlanSummary.
        The current state of the migration plan.


        :return: The lifecycle_state of this MigrationPlanSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MigrationPlanSummary.
        The current state of the migration plan.


        :param lifecycle_state: The lifecycle_state of this MigrationPlanSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MigrationPlanSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this MigrationPlanSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MigrationPlanSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this MigrationPlanSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def migration_id(self):
        """
        **[Required]** Gets the migration_id of this MigrationPlanSummary.
        The OCID of the associated migration.


        :return: The migration_id of this MigrationPlanSummary.
        :rtype: str
        """
        return self._migration_id

    @migration_id.setter
    def migration_id(self, migration_id):
        """
        Sets the migration_id of this MigrationPlanSummary.
        The OCID of the associated migration.


        :param migration_id: The migration_id of this MigrationPlanSummary.
        :type: str
        """
        self._migration_id = migration_id

    @property
    def strategies(self):
        """
        **[Required]** Gets the strategies of this MigrationPlanSummary.
        List of strategies for the resources to be migrated.


        :return: The strategies of this MigrationPlanSummary.
        :rtype: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]
        """
        return self._strategies

    @strategies.setter
    def strategies(self, strategies):
        """
        Sets the strategies of this MigrationPlanSummary.
        List of strategies for the resources to be migrated.


        :param strategies: The strategies of this MigrationPlanSummary.
        :type: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]
        """
        self._strategies = strategies

    @property
    def migration_plan_stats(self):
        """
        Gets the migration_plan_stats of this MigrationPlanSummary.

        :return: The migration_plan_stats of this MigrationPlanSummary.
        :rtype: oci.cloud_migrations.models.MigrationPlanStats
        """
        return self._migration_plan_stats

    @migration_plan_stats.setter
    def migration_plan_stats(self, migration_plan_stats):
        """
        Sets the migration_plan_stats of this MigrationPlanSummary.

        :param migration_plan_stats: The migration_plan_stats of this MigrationPlanSummary.
        :type: oci.cloud_migrations.models.MigrationPlanStats
        """
        self._migration_plan_stats = migration_plan_stats

    @property
    def calculated_limits(self):
        """
        **[Required]** Gets the calculated_limits of this MigrationPlanSummary.
        Limits of the resources that are needed for migration. Example: {\"BlockVolume\": 2, \"VCN\": 1}


        :return: The calculated_limits of this MigrationPlanSummary.
        :rtype: dict(str, int)
        """
        return self._calculated_limits

    @calculated_limits.setter
    def calculated_limits(self, calculated_limits):
        """
        Sets the calculated_limits of this MigrationPlanSummary.
        Limits of the resources that are needed for migration. Example: {\"BlockVolume\": 2, \"VCN\": 1}


        :param calculated_limits: The calculated_limits of this MigrationPlanSummary.
        :type: dict(str, int)
        """
        self._calculated_limits = calculated_limits

    @property
    def target_environments(self):
        """
        **[Required]** Gets the target_environments of this MigrationPlanSummary.
        List of target environments.


        :return: The target_environments of this MigrationPlanSummary.
        :rtype: list[oci.cloud_migrations.models.TargetEnvironment]
        """
        return self._target_environments

    @target_environments.setter
    def target_environments(self, target_environments):
        """
        Sets the target_environments of this MigrationPlanSummary.
        List of target environments.


        :param target_environments: The target_environments of this MigrationPlanSummary.
        :type: list[oci.cloud_migrations.models.TargetEnvironment]
        """
        self._target_environments = target_environments

    @property
    def reference_to_rms_stack(self):
        """
        Gets the reference_to_rms_stack of this MigrationPlanSummary.
        OCID of the referenced ORM job.


        :return: The reference_to_rms_stack of this MigrationPlanSummary.
        :rtype: str
        """
        return self._reference_to_rms_stack

    @reference_to_rms_stack.setter
    def reference_to_rms_stack(self, reference_to_rms_stack):
        """
        Sets the reference_to_rms_stack of this MigrationPlanSummary.
        OCID of the referenced ORM job.


        :param reference_to_rms_stack: The reference_to_rms_stack of this MigrationPlanSummary.
        :type: str
        """
        self._reference_to_rms_stack = reference_to_rms_stack

    @property
    def source_migration_plan_id(self):
        """
        Gets the source_migration_plan_id of this MigrationPlanSummary.
        Source migraiton plan ID to be cloned.


        :return: The source_migration_plan_id of this MigrationPlanSummary.
        :rtype: str
        """
        return self._source_migration_plan_id

    @source_migration_plan_id.setter
    def source_migration_plan_id(self, source_migration_plan_id):
        """
        Sets the source_migration_plan_id of this MigrationPlanSummary.
        Source migraiton plan ID to be cloned.


        :param source_migration_plan_id: The source_migration_plan_id of this MigrationPlanSummary.
        :type: str
        """
        self._source_migration_plan_id = source_migration_plan_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MigrationPlanSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MigrationPlanSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MigrationPlanSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MigrationPlanSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MigrationPlanSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MigrationPlanSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MigrationPlanSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MigrationPlanSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MigrationPlanSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MigrationPlanSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MigrationPlanSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MigrationPlanSummary.
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
