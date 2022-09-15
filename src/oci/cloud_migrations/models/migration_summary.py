# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationSummary(object):
    """
    Summary of the migration project.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MigrationSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MigrationSummary.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MigrationSummary.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this MigrationSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MigrationSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MigrationSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MigrationSummary.
        :type lifecycle_details: str

        :param is_completed:
            The value to assign to the is_completed property of this MigrationSummary.
        :type is_completed: bool

        :param replication_schedule_id:
            The value to assign to the replication_schedule_id property of this MigrationSummary.
        :type replication_schedule_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MigrationSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MigrationSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MigrationSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'is_completed': 'bool',
            'replication_schedule_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'is_completed': 'isCompleted',
            'replication_schedule_id': 'replicationScheduleId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._is_completed = None
        self._replication_schedule_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MigrationSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this MigrationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MigrationSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this MigrationSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this MigrationSummary.
        Migration identifier that can be renamed


        :return: The display_name of this MigrationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MigrationSummary.
        Migration identifier that can be renamed


        :param display_name: The display_name of this MigrationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MigrationSummary.
        Compartment identifier


        :return: The compartment_id of this MigrationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MigrationSummary.
        Compartment identifier


        :param compartment_id: The compartment_id of this MigrationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MigrationSummary.
        The time when the migration project was created. An RFC3339 formatted datetime string.


        :return: The time_created of this MigrationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MigrationSummary.
        The time when the migration project was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MigrationSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MigrationSummary.
        The time when the migration project was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this MigrationSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MigrationSummary.
        The time when the migration project was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MigrationSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MigrationSummary.
        The current state of migration.


        :return: The lifecycle_state of this MigrationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MigrationSummary.
        The current state of migration.


        :param lifecycle_state: The lifecycle_state of this MigrationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this MigrationSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this MigrationSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this MigrationSummary.
        A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this MigrationSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def is_completed(self):
        """
        Gets the is_completed of this MigrationSummary.
        Indicates whether migration is marked as complete.


        :return: The is_completed of this MigrationSummary.
        :rtype: bool
        """
        return self._is_completed

    @is_completed.setter
    def is_completed(self, is_completed):
        """
        Sets the is_completed of this MigrationSummary.
        Indicates whether migration is marked as complete.


        :param is_completed: The is_completed of this MigrationSummary.
        :type: bool
        """
        self._is_completed = is_completed

    @property
    def replication_schedule_id(self):
        """
        Gets the replication_schedule_id of this MigrationSummary.
        Replication schedule identifier


        :return: The replication_schedule_id of this MigrationSummary.
        :rtype: str
        """
        return self._replication_schedule_id

    @replication_schedule_id.setter
    def replication_schedule_id(self, replication_schedule_id):
        """
        Sets the replication_schedule_id of this MigrationSummary.
        Replication schedule identifier


        :param replication_schedule_id: The replication_schedule_id of this MigrationSummary.
        :type: str
        """
        self._replication_schedule_id = replication_schedule_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MigrationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MigrationSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MigrationSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MigrationSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MigrationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MigrationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MigrationSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MigrationSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MigrationSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MigrationSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MigrationSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MigrationSummary.
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
