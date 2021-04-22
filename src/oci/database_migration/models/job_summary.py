# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobSummary(object):
    """
    Job description
    """

    #: A constant which can be used with the type property of a JobSummary.
    #: This constant has a value of "EVALUATION"
    TYPE_EVALUATION = "EVALUATION"

    #: A constant which can be used with the type property of a JobSummary.
    #: This constant has a value of "MIGRATION"
    TYPE_MIGRATION = "MIGRATION"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "UNKNOWN"
    LIFECYCLE_STATE_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a JobSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new JobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JobSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this JobSummary.
        :type display_name: str

        :param migration_id:
            The value to assign to the migration_id property of this JobSummary.
        :type migration_id: str

        :param type:
            The value to assign to the type property of this JobSummary.
            Allowed values for this property are: "EVALUATION", "MIGRATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param progress:
            The value to assign to the progress property of this JobSummary.
        :type progress: oci.database_migration.models.MigrationJobProgressSummary

        :param time_created:
            The value to assign to the time_created property of this JobSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this JobSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JobSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this JobSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this JobSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this JobSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this JobSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'migration_id': 'str',
            'type': 'str',
            'progress': 'MigrationJobProgressSummary',
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
            'display_name': 'displayName',
            'migration_id': 'migrationId',
            'type': 'type',
            'progress': 'progress',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._migration_id = None
        self._type = None
        self._progress = None
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
        **[Required]** Gets the id of this JobSummary.
        The OCID of the Migration Job.


        :return: The id of this JobSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobSummary.
        The OCID of the Migration Job.


        :param id: The id of this JobSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this JobSummary.
        Name of the job.


        :return: The display_name of this JobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JobSummary.
        Name of the job.


        :param display_name: The display_name of this JobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def migration_id(self):
        """
        **[Required]** Gets the migration_id of this JobSummary.
        The OCID of the Migration that this job belongs to.


        :return: The migration_id of this JobSummary.
        :rtype: str
        """
        return self._migration_id

    @migration_id.setter
    def migration_id(self, migration_id):
        """
        Sets the migration_id of this JobSummary.
        The OCID of the Migration that this job belongs to.


        :param migration_id: The migration_id of this JobSummary.
        :type: str
        """
        self._migration_id = migration_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this JobSummary.
        The job type.

        Allowed values for this property are: "EVALUATION", "MIGRATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this JobSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this JobSummary.
        The job type.


        :param type: The type of this JobSummary.
        :type: str
        """
        allowed_values = ["EVALUATION", "MIGRATION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def progress(self):
        """
        Gets the progress of this JobSummary.

        :return: The progress of this JobSummary.
        :rtype: oci.database_migration.models.MigrationJobProgressSummary
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """
        Sets the progress of this JobSummary.

        :param progress: The progress of this JobSummary.
        :type: oci.database_migration.models.MigrationJobProgressSummary
        """
        self._progress = progress

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this JobSummary.
        The time the Migration Job was created. An RFC3339 formatted datetime string


        :return: The time_created of this JobSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobSummary.
        The time the Migration Job was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this JobSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this JobSummary.
        The time the Migration Job was last updated. An RFC3339 formatted datetime string


        :return: The time_updated of this JobSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this JobSummary.
        The time the Migration Job was last updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this JobSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this JobSummary.
        The current state of the migration Deployment.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this JobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JobSummary.
        The current state of the migration Deployment.


        :param lifecycle_state: The lifecycle_state of this JobSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "UNKNOWN", "TERMINATED", "FAILED", "SUCCEEDED", "WAITING", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this JobSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information
        for a resource in Failed state.


        :return: The lifecycle_details of this JobSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this JobSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information
        for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this JobSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this JobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this JobSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this JobSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this JobSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this JobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this JobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this JobSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this JobSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this JobSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this JobSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this JobSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this JobSummary.
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
