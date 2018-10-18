# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDataWarehouseSummary(object):
    """
    An Oracle Autonomous Data Warehouse.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the license_model property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "RESTORE_IN_PROGRESS"
    LIFECYCLE_STATE_RESTORE_IN_PROGRESS = "RESTORE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "SCALE_IN_PROGRESS"
    LIFECYCLE_STATE_SCALE_IN_PROGRESS = "SCALE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseSummary.
    #: This constant has a value of "AVAILABLE_NEEDS_ATTENTION"
    LIFECYCLE_STATE_AVAILABLE_NEEDS_ATTENTION = "AVAILABLE_NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDataWarehouseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousDataWarehouseSummary.
        :type compartment_id: str

        :param connection_strings:
            The value to assign to the connection_strings property of this AutonomousDataWarehouseSummary.
        :type connection_strings: AutonomousDataWarehouseConnectionStrings

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this AutonomousDataWarehouseSummary.
        :type cpu_core_count: int

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this AutonomousDataWarehouseSummary.
        :type data_storage_size_in_tbs: int

        :param db_name:
            The value to assign to the db_name property of this AutonomousDataWarehouseSummary.
        :type db_name: str

        :param db_version:
            The value to assign to the db_version property of this AutonomousDataWarehouseSummary.
        :type db_version: str

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousDataWarehouseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this AutonomousDataWarehouseSummary.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousDataWarehouseSummary.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this AutonomousDataWarehouseSummary.
        :type id: str

        :param license_model:
            The value to assign to the license_model property of this AutonomousDataWarehouseSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDataWarehouseSummary.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDataWarehouseSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param service_console_url:
            The value to assign to the service_console_url property of this AutonomousDataWarehouseSummary.
        :type service_console_url: str

        :param time_created:
            The value to assign to the time_created property of this AutonomousDataWarehouseSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'connection_strings': 'AutonomousDataWarehouseConnectionStrings',
            'cpu_core_count': 'int',
            'data_storage_size_in_tbs': 'int',
            'db_name': 'str',
            'db_version': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'license_model': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'service_console_url': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'connection_strings': 'connectionStrings',
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'db_name': 'dbName',
            'db_version': 'dbVersion',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'license_model': 'licenseModel',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'service_console_url': 'serviceConsoleUrl',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._connection_strings = None
        self._cpu_core_count = None
        self._data_storage_size_in_tbs = None
        self._db_name = None
        self._db_version = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._license_model = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._service_console_url = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousDataWarehouseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousDataWarehouseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AutonomousDataWarehouseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def connection_strings(self):
        """
        Gets the connection_strings of this AutonomousDataWarehouseSummary.
        The connection string used to connect to the Data Warehouse. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Data Warehouse for the password value.


        :return: The connection_strings of this AutonomousDataWarehouseSummary.
        :rtype: AutonomousDataWarehouseConnectionStrings
        """
        return self._connection_strings

    @connection_strings.setter
    def connection_strings(self, connection_strings):
        """
        Sets the connection_strings of this AutonomousDataWarehouseSummary.
        The connection string used to connect to the Data Warehouse. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Data Warehouse for the password value.


        :param connection_strings: The connection_strings of this AutonomousDataWarehouseSummary.
        :type: AutonomousDataWarehouseConnectionStrings
        """
        self._connection_strings = connection_strings

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this AutonomousDataWarehouseSummary.
        The number of CPU cores to be made available to the database.


        :return: The cpu_core_count of this AutonomousDataWarehouseSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this AutonomousDataWarehouseSummary.
        The number of CPU cores to be made available to the database.


        :param cpu_core_count: The cpu_core_count of this AutonomousDataWarehouseSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def data_storage_size_in_tbs(self):
        """
        **[Required]** Gets the data_storage_size_in_tbs of this AutonomousDataWarehouseSummary.
        The quantity of data in the database, in terabytes.


        :return: The data_storage_size_in_tbs of this AutonomousDataWarehouseSummary.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this AutonomousDataWarehouseSummary.
        The quantity of data in the database, in terabytes.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this AutonomousDataWarehouseSummary.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this AutonomousDataWarehouseSummary.
        The database name.


        :return: The db_name of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this AutonomousDataWarehouseSummary.
        The database name.


        :param db_name: The db_name of this AutonomousDataWarehouseSummary.
        :type: str
        """
        self._db_name = db_name

    @property
    def db_version(self):
        """
        Gets the db_version of this AutonomousDataWarehouseSummary.
        A valid Oracle Database version for Autonomous Data Warehouse.


        :return: The db_version of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this AutonomousDataWarehouseSummary.
        A valid Oracle Database version for Autonomous Data Warehouse.


        :param db_version: The db_version of this AutonomousDataWarehouseSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousDataWarehouseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousDataWarehouseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousDataWarehouseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousDataWarehouseSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this AutonomousDataWarehouseSummary.
        The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.


        :return: The display_name of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousDataWarehouseSummary.
        The user-friendly name for the Autonomous Data Warehouse. The name does not have to be unique.


        :param display_name: The display_name of this AutonomousDataWarehouseSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousDataWarehouseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousDataWarehouseSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousDataWarehouseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousDataWarehouseSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousDataWarehouseSummary.
        The `OCID`__ of the Autonomous Data Warehouse.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousDataWarehouseSummary.
        The `OCID`__ of the Autonomous Data Warehouse.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousDataWarehouseSummary.
        :type: str
        """
        self._id = id

    @property
    def license_model(self):
        """
        Gets the license_model of this AutonomousDataWarehouseSummary.
        The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this AutonomousDataWarehouseSummary.
        The Oracle license model that applies to the Oracle Autonomous Data Warehouse. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this AutonomousDataWarehouseSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousDataWarehouseSummary.
        Information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousDataWarehouseSummary.
        Information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousDataWarehouseSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousDataWarehouseSummary.
        The current state of the database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousDataWarehouseSummary.
        The current state of the database.


        :param lifecycle_state: The lifecycle_state of this AutonomousDataWarehouseSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def service_console_url(self):
        """
        Gets the service_console_url of this AutonomousDataWarehouseSummary.
        The URL of the Service Console for the Data Warehouse.


        :return: The service_console_url of this AutonomousDataWarehouseSummary.
        :rtype: str
        """
        return self._service_console_url

    @service_console_url.setter
    def service_console_url(self, service_console_url):
        """
        Sets the service_console_url of this AutonomousDataWarehouseSummary.
        The URL of the Service Console for the Data Warehouse.


        :param service_console_url: The service_console_url of this AutonomousDataWarehouseSummary.
        :type: str
        """
        self._service_console_url = service_console_url

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousDataWarehouseSummary.
        The date and time the database was created.


        :return: The time_created of this AutonomousDataWarehouseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousDataWarehouseSummary.
        The date and time the database was created.


        :param time_created: The time_created of this AutonomousDataWarehouseSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
