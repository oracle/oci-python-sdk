# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseSummary(object):
    """
    An Oracle Autonomous Database.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "RESTORE_IN_PROGRESS"
    LIFECYCLE_STATE_RESTORE_IN_PROGRESS = "RESTORE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "RESTORE_FAILED"
    LIFECYCLE_STATE_RESTORE_FAILED = "RESTORE_FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "SCALE_IN_PROGRESS"
    LIFECYCLE_STATE_SCALE_IN_PROGRESS = "SCALE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "AVAILABLE_NEEDS_ATTENTION"
    LIFECYCLE_STATE_AVAILABLE_NEEDS_ATTENTION = "AVAILABLE_NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the license_model property of a AutonomousDatabaseSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a AutonomousDatabaseSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the db_workload property of a AutonomousDatabaseSummary.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a AutonomousDatabaseSummary.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousDatabaseSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousDatabaseSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDatabaseSummary.
        :type lifecycle_details: str

        :param db_name:
            The value to assign to the db_name property of this AutonomousDatabaseSummary.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this AutonomousDatabaseSummary.
        :type cpu_core_count: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this AutonomousDatabaseSummary.
        :type data_storage_size_in_tbs: int

        :param is_dedicated:
            The value to assign to the is_dedicated property of this AutonomousDatabaseSummary.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this AutonomousDatabaseSummary.
        :type autonomous_container_database_id: str

        :param time_created:
            The value to assign to the time_created property of this AutonomousDatabaseSummary.
        :type time_created: datetime

        :param display_name:
            The value to assign to the display_name property of this AutonomousDatabaseSummary.
        :type display_name: str

        :param service_console_url:
            The value to assign to the service_console_url property of this AutonomousDatabaseSummary.
        :type service_console_url: str

        :param connection_strings:
            The value to assign to the connection_strings property of this AutonomousDatabaseSummary.
        :type connection_strings: AutonomousDatabaseConnectionStrings

        :param connection_urls:
            The value to assign to the connection_urls property of this AutonomousDatabaseSummary.
        :type connection_urls: AutonomousDatabaseConnectionUrls

        :param license_model:
            The value to assign to the license_model property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param used_data_storage_size_in_tbs:
            The value to assign to the used_data_storage_size_in_tbs property of this AutonomousDatabaseSummary.
        :type used_data_storage_size_in_tbs: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param db_version:
            The value to assign to the db_version property of this AutonomousDatabaseSummary.
        :type db_version: str

        :param is_preview:
            The value to assign to the is_preview property of this AutonomousDatabaseSummary.
        :type is_preview: bool

        :param db_workload:
            The value to assign to the db_workload property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_workload: str

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this AutonomousDatabaseSummary.
        :type whitelisted_ips: list[str]

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this AutonomousDatabaseSummary.
        :type is_auto_scaling_enabled: bool

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'data_storage_size_in_tbs': 'int',
            'is_dedicated': 'bool',
            'autonomous_container_database_id': 'str',
            'time_created': 'datetime',
            'display_name': 'str',
            'service_console_url': 'str',
            'connection_strings': 'AutonomousDatabaseConnectionStrings',
            'connection_urls': 'AutonomousDatabaseConnectionUrls',
            'license_model': 'str',
            'used_data_storage_size_in_tbs': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'db_version': 'str',
            'is_preview': 'bool',
            'db_workload': 'str',
            'whitelisted_ips': 'list[str]',
            'is_auto_scaling_enabled': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'is_dedicated': 'isDedicated',
            'autonomous_container_database_id': 'autonomousContainerDatabaseId',
            'time_created': 'timeCreated',
            'display_name': 'displayName',
            'service_console_url': 'serviceConsoleUrl',
            'connection_strings': 'connectionStrings',
            'connection_urls': 'connectionUrls',
            'license_model': 'licenseModel',
            'used_data_storage_size_in_tbs': 'usedDataStorageSizeInTBs',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'db_version': 'dbVersion',
            'is_preview': 'isPreview',
            'db_workload': 'dbWorkload',
            'whitelisted_ips': 'whitelistedIps',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled'
        }

        self._id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._db_name = None
        self._cpu_core_count = None
        self._data_storage_size_in_tbs = None
        self._is_dedicated = None
        self._autonomous_container_database_id = None
        self._time_created = None
        self._display_name = None
        self._service_console_url = None
        self._connection_strings = None
        self._connection_urls = None
        self._license_model = None
        self._used_data_storage_size_in_tbs = None
        self._freeform_tags = None
        self._defined_tags = None
        self._db_version = None
        self._is_preview = None
        self._db_workload = None
        self._whitelisted_ips = None
        self._is_auto_scaling_enabled = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousDatabaseSummary.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousDatabaseSummary.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousDatabaseSummary.
        The current state of the database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousDatabaseSummary.
        The current state of the database.


        :param lifecycle_state: The lifecycle_state of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousDatabaseSummary.
        Information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousDatabaseSummary.
        Information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousDatabaseSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this AutonomousDatabaseSummary.
        The database name.


        :return: The db_name of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this AutonomousDatabaseSummary.
        The database name.


        :param db_name: The db_name of this AutonomousDatabaseSummary.
        :type: str
        """
        self._db_name = db_name

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this AutonomousDatabaseSummary.
        The number of CPU cores to be made available to the database.


        :return: The cpu_core_count of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this AutonomousDatabaseSummary.
        The number of CPU cores to be made available to the database.


        :param cpu_core_count: The cpu_core_count of this AutonomousDatabaseSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_size_in_tbs(self):
        """
        **[Required]** Gets the data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The quantity of data in the database, in terabytes.


        :return: The data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The quantity of data in the database, in terabytes.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def is_dedicated(self):
        """
        Gets the is_dedicated of this AutonomousDatabaseSummary.
        True if the database uses the `dedicated deployment`__ option.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm


        :return: The is_dedicated of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_dedicated

    @is_dedicated.setter
    def is_dedicated(self, is_dedicated):
        """
        Sets the is_dedicated of this AutonomousDatabaseSummary.
        True if the database uses the `dedicated deployment`__ option.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adbddoverview.htm


        :param is_dedicated: The is_dedicated of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_dedicated = is_dedicated

    @property
    def autonomous_container_database_id(self):
        """
        Gets the autonomous_container_database_id of this AutonomousDatabaseSummary.
        The Autonomous Container Database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_container_database_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._autonomous_container_database_id

    @autonomous_container_database_id.setter
    def autonomous_container_database_id(self, autonomous_container_database_id):
        """
        Sets the autonomous_container_database_id of this AutonomousDatabaseSummary.
        The Autonomous Container Database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_container_database_id: The autonomous_container_database_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._autonomous_container_database_id = autonomous_container_database_id

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousDatabaseSummary.
        The date and time the database was created.


        :return: The time_created of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousDatabaseSummary.
        The date and time the database was created.


        :param time_created: The time_created of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def display_name(self):
        """
        Gets the display_name of this AutonomousDatabaseSummary.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :return: The display_name of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousDatabaseSummary.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :param display_name: The display_name of this AutonomousDatabaseSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def service_console_url(self):
        """
        Gets the service_console_url of this AutonomousDatabaseSummary.
        The URL of the Service Console for the Autonomous Database.


        :return: The service_console_url of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._service_console_url

    @service_console_url.setter
    def service_console_url(self, service_console_url):
        """
        Sets the service_console_url of this AutonomousDatabaseSummary.
        The URL of the Service Console for the Autonomous Database.


        :param service_console_url: The service_console_url of this AutonomousDatabaseSummary.
        :type: str
        """
        self._service_console_url = service_console_url

    @property
    def connection_strings(self):
        """
        Gets the connection_strings of this AutonomousDatabaseSummary.
        The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.


        :return: The connection_strings of this AutonomousDatabaseSummary.
        :rtype: AutonomousDatabaseConnectionStrings
        """
        return self._connection_strings

    @connection_strings.setter
    def connection_strings(self, connection_strings):
        """
        Sets the connection_strings of this AutonomousDatabaseSummary.
        The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.


        :param connection_strings: The connection_strings of this AutonomousDatabaseSummary.
        :type: AutonomousDatabaseConnectionStrings
        """
        self._connection_strings = connection_strings

    @property
    def connection_urls(self):
        """
        Gets the connection_urls of this AutonomousDatabaseSummary.

        :return: The connection_urls of this AutonomousDatabaseSummary.
        :rtype: AutonomousDatabaseConnectionUrls
        """
        return self._connection_urls

    @connection_urls.setter
    def connection_urls(self, connection_urls):
        """
        Sets the connection_urls of this AutonomousDatabaseSummary.

        :param connection_urls: The connection_urls of this AutonomousDatabaseSummary.
        :type: AutonomousDatabaseConnectionUrls
        """
        self._connection_urls = connection_urls

    @property
    def license_model(self):
        """
        Gets the license_model of this AutonomousDatabaseSummary.
        The Oracle license model that applies to the Oracle Autonomous Database. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this AutonomousDatabaseSummary.
        The Oracle license model that applies to the Oracle Autonomous Database. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def used_data_storage_size_in_tbs(self):
        """
        Gets the used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The amount of storage that has been used, in terabytes.


        :return: The used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._used_data_storage_size_in_tbs

    @used_data_storage_size_in_tbs.setter
    def used_data_storage_size_in_tbs(self, used_data_storage_size_in_tbs):
        """
        Sets the used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The amount of storage that has been used, in terabytes.


        :param used_data_storage_size_in_tbs: The used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :type: int
        """
        self._used_data_storage_size_in_tbs = used_data_storage_size_in_tbs

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousDatabaseSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousDatabaseSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousDatabaseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousDatabaseSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def db_version(self):
        """
        Gets the db_version of this AutonomousDatabaseSummary.
        A valid Oracle Database version for Autonomous Database.


        :return: The db_version of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this AutonomousDatabaseSummary.
        A valid Oracle Database version for Autonomous Database.


        :param db_version: The db_version of this AutonomousDatabaseSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def is_preview(self):
        """
        Gets the is_preview of this AutonomousDatabaseSummary.
        Indicates if the Autonomous Database version is a preview version.


        :return: The is_preview of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_preview

    @is_preview.setter
    def is_preview(self, is_preview):
        """
        Sets the is_preview of this AutonomousDatabaseSummary.
        Indicates if the Autonomous Database version is a preview version.


        :param is_preview: The is_preview of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_preview = is_preview

    @property
    def db_workload(self):
        """
        Gets the db_workload of this AutonomousDatabaseSummary.
        The Autonomous Database workload type. OLTP indicates an Autonomous Transaction Processing database and DW indicates an Autonomous Data Warehouse database.

        Allowed values for this property are: "OLTP", "DW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_workload of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this AutonomousDatabaseSummary.
        The Autonomous Database workload type. OLTP indicates an Autonomous Transaction Processing database and DW indicates an Autonomous Data Warehouse database.


        :param db_workload: The db_workload of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["OLTP", "DW"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            db_workload = 'UNKNOWN_ENUM_VALUE'
        self._db_workload = db_workload

    @property
    def whitelisted_ips(self):
        """
        Gets the whitelisted_ips of this AutonomousDatabaseSummary.
        The client IP access control list (ACL). This feature is available for `serverless deployments`__ only.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :return: The whitelisted_ips of this AutonomousDatabaseSummary.
        :rtype: list[str]
        """
        return self._whitelisted_ips

    @whitelisted_ips.setter
    def whitelisted_ips(self, whitelisted_ips):
        """
        Sets the whitelisted_ips of this AutonomousDatabaseSummary.
        The client IP access control list (ACL). This feature is available for `serverless deployments`__ only.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance. This is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param whitelisted_ips: The whitelisted_ips of this AutonomousDatabaseSummary.
        :type: list[str]
        """
        self._whitelisted_ips = whitelisted_ips

    @property
    def is_auto_scaling_enabled(self):
        """
        Gets the is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        Indicates if auto scaling is enabled for the Autonomous Database CPU core count. Note that auto scaling is available for `serverless deployments`__ only.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :return: The is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        Indicates if auto scaling is enabled for the Autonomous Database CPU core count. Note that auto scaling is available for `serverless deployments`__ only.

        __ https://docs.cloud.oracle.com/Content/Database/Concepts/adboverview.htm#AEI


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
