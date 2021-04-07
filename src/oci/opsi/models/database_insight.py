# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseInsight(object):
    """
    Database insight resource.
    """

    #: A constant which can be used with the entity_source property of a DatabaseInsight.
    #: This constant has a value of "AUTONOMOUS_DATABASE"
    ENTITY_SOURCE_AUTONOMOUS_DATABASE = "AUTONOMOUS_DATABASE"

    #: A constant which can be used with the entity_source property of a DatabaseInsight.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_DATABASE"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_DATABASE = "EM_MANAGED_EXTERNAL_DATABASE"

    #: A constant which can be used with the entity_source property of a DatabaseInsight.
    #: This constant has a value of "MACS_MANAGED_EXTERNAL_DATABASE"
    ENTITY_SOURCE_MACS_MANAGED_EXTERNAL_DATABASE = "MACS_MANAGED_EXTERNAL_DATABASE"

    #: A constant which can be used with the status property of a DatabaseInsight.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a DatabaseInsight.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a DatabaseInsight.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseInsight.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseInsight.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseInsight.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseInsight.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseInsight.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseInsight.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseInsight object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.EmManagedExternalDatabaseInsight`
        * :class:`~oci.opsi.models.MacsManagedExternalDatabaseInsight`
        * :class:`~oci.opsi.models.AutonomousDatabaseInsight`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this DatabaseInsight.
            Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param id:
            The value to assign to the id property of this DatabaseInsight.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseInsight.
        :type compartment_id: str

        :param status:
            The value to assign to the status property of this DatabaseInsight.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param database_type:
            The value to assign to the database_type property of this DatabaseInsight.
        :type database_type: str

        :param database_version:
            The value to assign to the database_version property of this DatabaseInsight.
        :type database_version: str

        :param processor_count:
            The value to assign to the processor_count property of this DatabaseInsight.
        :type processor_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseInsight.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseInsight.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseInsight.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this DatabaseInsight.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseInsight.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseInsight.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseInsight.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'status': 'str',
            'database_type': 'str',
            'database_version': 'str',
            'processor_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'status': 'status',
            'database_type': 'databaseType',
            'database_version': 'databaseVersion',
            'processor_count': 'processorCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._status = None
        self._database_type = None
        self._database_version = None
        self._processor_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'EM_MANAGED_EXTERNAL_DATABASE':
            return 'EmManagedExternalDatabaseInsight'

        if type == 'MACS_MANAGED_EXTERNAL_DATABASE':
            return 'MacsManagedExternalDatabaseInsight'

        if type == 'AUTONOMOUS_DATABASE':
            return 'AutonomousDatabaseInsight'
        else:
            return 'DatabaseInsight'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this DatabaseInsight.
        Source of the database entity.

        Allowed values for this property are: "AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this DatabaseInsight.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this DatabaseInsight.
        Source of the database entity.


        :param entity_source: The entity_source of this DatabaseInsight.
        :type: str
        """
        allowed_values = ["AUTONOMOUS_DATABASE", "EM_MANAGED_EXTERNAL_DATABASE", "MACS_MANAGED_EXTERNAL_DATABASE"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatabaseInsight.
        Database insight identifier


        :return: The id of this DatabaseInsight.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseInsight.
        Database insight identifier


        :param id: The id of this DatabaseInsight.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DatabaseInsight.
        Compartment identifier of the database


        :return: The compartment_id of this DatabaseInsight.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseInsight.
        Compartment identifier of the database


        :param compartment_id: The compartment_id of this DatabaseInsight.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this DatabaseInsight.
        Indicates the status of a database insight in Operations Insights

        Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this DatabaseInsight.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DatabaseInsight.
        Indicates the status of a database insight in Operations Insights


        :param status: The status of this DatabaseInsight.
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def database_type(self):
        """
        Gets the database_type of this DatabaseInsight.
        Operations Insights internal representation of the database type.


        :return: The database_type of this DatabaseInsight.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this DatabaseInsight.
        Operations Insights internal representation of the database type.


        :param database_type: The database_type of this DatabaseInsight.
        :type: str
        """
        self._database_type = database_type

    @property
    def database_version(self):
        """
        Gets the database_version of this DatabaseInsight.
        The version of the database.


        :return: The database_version of this DatabaseInsight.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this DatabaseInsight.
        The version of the database.


        :param database_version: The database_version of this DatabaseInsight.
        :type: str
        """
        self._database_version = database_version

    @property
    def processor_count(self):
        """
        Gets the processor_count of this DatabaseInsight.
        Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.


        :return: The processor_count of this DatabaseInsight.
        :rtype: int
        """
        return self._processor_count

    @processor_count.setter
    def processor_count(self, processor_count):
        """
        Sets the processor_count of this DatabaseInsight.
        Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.


        :param processor_count: The processor_count of this DatabaseInsight.
        :type: int
        """
        self._processor_count = processor_count

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this DatabaseInsight.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatabaseInsight.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseInsight.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatabaseInsight.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this DatabaseInsight.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatabaseInsight.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseInsight.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatabaseInsight.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DatabaseInsight.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DatabaseInsight.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DatabaseInsight.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DatabaseInsight.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DatabaseInsight.
        The time the the database insight was first enabled. An RFC3339 formatted datetime string


        :return: The time_created of this DatabaseInsight.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatabaseInsight.
        The time the the database insight was first enabled. An RFC3339 formatted datetime string


        :param time_created: The time_created of this DatabaseInsight.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DatabaseInsight.
        The time the database insight was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this DatabaseInsight.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DatabaseInsight.
        The time the database insight was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this DatabaseInsight.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DatabaseInsight.
        The current state of the database.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseInsight.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseInsight.
        The current state of the database.


        :param lifecycle_state: The lifecycle_state of this DatabaseInsight.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseInsight.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DatabaseInsight.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseInsight.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DatabaseInsight.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
