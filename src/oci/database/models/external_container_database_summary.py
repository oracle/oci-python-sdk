# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalContainerDatabaseSummary(object):
    """
    An Oracle Cloud Infrastructure resource that allows you to manage an external Oracle container database.
    """

    #: A constant which can be used with the lifecycle_state property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "NOT_CONNECTED"
    LIFECYCLE_STATE_NOT_CONNECTED = "NOT_CONNECTED"

    #: A constant which can be used with the lifecycle_state property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the database_edition property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "STANDARD_EDITION"
    DATABASE_EDITION_STANDARD_EDITION = "STANDARD_EDITION"

    #: A constant which can be used with the database_edition property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "ENTERPRISE_EDITION"
    DATABASE_EDITION_ENTERPRISE_EDITION = "ENTERPRISE_EDITION"

    #: A constant which can be used with the database_edition property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "ENTERPRISE_EDITION_HIGH_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_HIGH_PERFORMANCE = "ENTERPRISE_EDITION_HIGH_PERFORMANCE"

    #: A constant which can be used with the database_edition property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_EXTREME_PERFORMANCE = "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"

    #: A constant which can be used with the database_configuration property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "RAC"
    DATABASE_CONFIGURATION_RAC = "RAC"

    #: A constant which can be used with the database_configuration property of a ExternalContainerDatabaseSummary.
    #: This constant has a value of "SINGLE_INSTANCE"
    DATABASE_CONFIGURATION_SINGLE_INSTANCE = "SINGLE_INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalContainerDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalContainerDatabaseSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExternalContainerDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExternalContainerDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this ExternalContainerDatabaseSummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ExternalContainerDatabaseSummary.
        :type id: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalContainerDatabaseSummary.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalContainerDatabaseSummary.
            Allowed values for this property are: "PROVISIONING", "NOT_CONNECTED", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ExternalContainerDatabaseSummary.
        :type time_created: datetime

        :param db_unique_name:
            The value to assign to the db_unique_name property of this ExternalContainerDatabaseSummary.
        :type db_unique_name: str

        :param db_id:
            The value to assign to the db_id property of this ExternalContainerDatabaseSummary.
        :type db_id: str

        :param database_version:
            The value to assign to the database_version property of this ExternalContainerDatabaseSummary.
        :type database_version: str

        :param database_edition:
            The value to assign to the database_edition property of this ExternalContainerDatabaseSummary.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_edition: str

        :param time_zone:
            The value to assign to the time_zone property of this ExternalContainerDatabaseSummary.
        :type time_zone: str

        :param character_set:
            The value to assign to the character_set property of this ExternalContainerDatabaseSummary.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this ExternalContainerDatabaseSummary.
        :type ncharacter_set: str

        :param db_packs:
            The value to assign to the db_packs property of this ExternalContainerDatabaseSummary.
        :type db_packs: str

        :param database_configuration:
            The value to assign to the database_configuration property of this ExternalContainerDatabaseSummary.
            Allowed values for this property are: "RAC", "SINGLE_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_configuration: str

        :param database_management_config:
            The value to assign to the database_management_config property of this ExternalContainerDatabaseSummary.
        :type database_management_config: oci.database.models.DatabaseManagementConfig

        :param stack_monitoring_config:
            The value to assign to the stack_monitoring_config property of this ExternalContainerDatabaseSummary.
        :type stack_monitoring_config: oci.database.models.StackMonitoringConfig

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'db_unique_name': 'str',
            'db_id': 'str',
            'database_version': 'str',
            'database_edition': 'str',
            'time_zone': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'db_packs': 'str',
            'database_configuration': 'str',
            'database_management_config': 'DatabaseManagementConfig',
            'stack_monitoring_config': 'StackMonitoringConfig'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'db_unique_name': 'dbUniqueName',
            'db_id': 'dbId',
            'database_version': 'databaseVersion',
            'database_edition': 'databaseEdition',
            'time_zone': 'timeZone',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'db_packs': 'dbPacks',
            'database_configuration': 'databaseConfiguration',
            'database_management_config': 'databaseManagementConfig',
            'stack_monitoring_config': 'stackMonitoringConfig'
        }

        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._time_created = None
        self._db_unique_name = None
        self._db_id = None
        self._database_version = None
        self._database_edition = None
        self._time_zone = None
        self._character_set = None
        self._ncharacter_set = None
        self._db_packs = None
        self._database_configuration = None
        self._database_management_config = None
        self._stack_monitoring_config = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalContainerDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalContainerDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExternalContainerDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExternalContainerDatabaseSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExternalContainerDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExternalContainerDatabaseSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExternalContainerDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExternalContainerDatabaseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExternalContainerDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExternalContainerDatabaseSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalContainerDatabaseSummary.
        The user-friendly name for the external database. The name does not have to be unique.


        :return: The display_name of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalContainerDatabaseSummary.
        The user-friendly name for the external database. The name does not have to be unique.


        :param display_name: The display_name of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalContainerDatabaseSummary.
        The `OCID`__ of the Oracle Cloud Infrastructure external database resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalContainerDatabaseSummary.
        The `OCID`__ of the Oracle Cloud Infrastructure external database resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExternalContainerDatabaseSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExternalContainerDatabaseSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExternalContainerDatabaseSummary.
        The current state of the Oracle Cloud Infrastructure external database resource.

        Allowed values for this property are: "PROVISIONING", "NOT_CONNECTED", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalContainerDatabaseSummary.
        The current state of the Oracle Cloud Infrastructure external database resource.


        :param lifecycle_state: The lifecycle_state of this ExternalContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "NOT_CONNECTED", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExternalContainerDatabaseSummary.
        The date and time the database was created.


        :return: The time_created of this ExternalContainerDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalContainerDatabaseSummary.
        The date and time the database was created.


        :param time_created: The time_created of this ExternalContainerDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def db_unique_name(self):
        """
        Gets the db_unique_name of this ExternalContainerDatabaseSummary.
        The `DB_UNIQUE_NAME` of the external database.


        :return: The db_unique_name of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this ExternalContainerDatabaseSummary.
        The `DB_UNIQUE_NAME` of the external database.


        :param db_unique_name: The db_unique_name of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def db_id(self):
        """
        Gets the db_id of this ExternalContainerDatabaseSummary.
        The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.


        :return: The db_id of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        """
        Sets the db_id of this ExternalContainerDatabaseSummary.
        The Oracle Database ID, which identifies an Oracle Database located outside of Oracle Cloud.


        :param db_id: The db_id of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._db_id = db_id

    @property
    def database_version(self):
        """
        Gets the database_version of this ExternalContainerDatabaseSummary.
        The Oracle Database version.


        :return: The database_version of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this ExternalContainerDatabaseSummary.
        The Oracle Database version.


        :param database_version: The database_version of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._database_version = database_version

    @property
    def database_edition(self):
        """
        Gets the database_edition of this ExternalContainerDatabaseSummary.
        The Oracle Database edition.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_edition of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this ExternalContainerDatabaseSummary.
        The Oracle Database edition.


        :param database_edition: The database_edition of this ExternalContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(database_edition, allowed_values):
            database_edition = 'UNKNOWN_ENUM_VALUE'
        self._database_edition = database_edition

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ExternalContainerDatabaseSummary.
        The time zone of the external database.
        It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name,
        depending on how the time zone value was specified when the database was created / last altered.


        :return: The time_zone of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ExternalContainerDatabaseSummary.
        The time zone of the external database.
        It is a time zone offset (a character type in the format '[+|-]TZH:TZM') or a time zone region name,
        depending on how the time zone value was specified when the database was created / last altered.


        :param time_zone: The time_zone of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def character_set(self):
        """
        Gets the character_set of this ExternalContainerDatabaseSummary.
        The character set of the external database.


        :return: The character_set of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this ExternalContainerDatabaseSummary.
        The character set of the external database.


        :param character_set: The character_set of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._character_set = character_set

    @property
    def ncharacter_set(self):
        """
        Gets the ncharacter_set of this ExternalContainerDatabaseSummary.
        The national character of the external database.


        :return: The ncharacter_set of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this ExternalContainerDatabaseSummary.
        The national character of the external database.


        :param ncharacter_set: The ncharacter_set of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def db_packs(self):
        """
        Gets the db_packs of this ExternalContainerDatabaseSummary.
        The database packs licensed for the external Oracle Database.


        :return: The db_packs of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._db_packs

    @db_packs.setter
    def db_packs(self, db_packs):
        """
        Sets the db_packs of this ExternalContainerDatabaseSummary.
        The database packs licensed for the external Oracle Database.


        :param db_packs: The db_packs of this ExternalContainerDatabaseSummary.
        :type: str
        """
        self._db_packs = db_packs

    @property
    def database_configuration(self):
        """
        Gets the database_configuration of this ExternalContainerDatabaseSummary.
        The Oracle Database configuration

        Allowed values for this property are: "RAC", "SINGLE_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_configuration of this ExternalContainerDatabaseSummary.
        :rtype: str
        """
        return self._database_configuration

    @database_configuration.setter
    def database_configuration(self, database_configuration):
        """
        Sets the database_configuration of this ExternalContainerDatabaseSummary.
        The Oracle Database configuration


        :param database_configuration: The database_configuration of this ExternalContainerDatabaseSummary.
        :type: str
        """
        allowed_values = ["RAC", "SINGLE_INSTANCE"]
        if not value_allowed_none_or_none_sentinel(database_configuration, allowed_values):
            database_configuration = 'UNKNOWN_ENUM_VALUE'
        self._database_configuration = database_configuration

    @property
    def database_management_config(self):
        """
        Gets the database_management_config of this ExternalContainerDatabaseSummary.

        :return: The database_management_config of this ExternalContainerDatabaseSummary.
        :rtype: oci.database.models.DatabaseManagementConfig
        """
        return self._database_management_config

    @database_management_config.setter
    def database_management_config(self, database_management_config):
        """
        Sets the database_management_config of this ExternalContainerDatabaseSummary.

        :param database_management_config: The database_management_config of this ExternalContainerDatabaseSummary.
        :type: oci.database.models.DatabaseManagementConfig
        """
        self._database_management_config = database_management_config

    @property
    def stack_monitoring_config(self):
        """
        Gets the stack_monitoring_config of this ExternalContainerDatabaseSummary.

        :return: The stack_monitoring_config of this ExternalContainerDatabaseSummary.
        :rtype: oci.database.models.StackMonitoringConfig
        """
        return self._stack_monitoring_config

    @stack_monitoring_config.setter
    def stack_monitoring_config(self, stack_monitoring_config):
        """
        Sets the stack_monitoring_config of this ExternalContainerDatabaseSummary.

        :param stack_monitoring_config: The stack_monitoring_config of this ExternalContainerDatabaseSummary.
        :type: oci.database.models.StackMonitoringConfig
        """
        self._stack_monitoring_config = stack_monitoring_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
