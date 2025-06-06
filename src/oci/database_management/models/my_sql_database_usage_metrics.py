# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlDatabaseUsageMetrics(object):
    """
    The list of aggregated metrics for Managed MySQL Databases in the fleet.
    """

    #: A constant which can be used with the database_status property of a MySqlDatabaseUsageMetrics.
    #: This constant has a value of "UP"
    DATABASE_STATUS_UP = "UP"

    #: A constant which can be used with the database_status property of a MySqlDatabaseUsageMetrics.
    #: This constant has a value of "DOWN"
    DATABASE_STATUS_DOWN = "DOWN"

    #: A constant which can be used with the database_status property of a MySqlDatabaseUsageMetrics.
    #: This constant has a value of "UNKNOWN"
    DATABASE_STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlDatabaseUsageMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this MySqlDatabaseUsageMetrics.
        :type compartment_id: str

        :param database_name:
            The value to assign to the database_name property of this MySqlDatabaseUsageMetrics.
        :type database_name: str

        :param database_type:
            The value to assign to the database_type property of this MySqlDatabaseUsageMetrics.
        :type database_type: str

        :param mds_deployment_type:
            The value to assign to the mds_deployment_type property of this MySqlDatabaseUsageMetrics.
        :type mds_deployment_type: str

        :param mdslifecycle_state:
            The value to assign to the mdslifecycle_state property of this MySqlDatabaseUsageMetrics.
        :type mdslifecycle_state: str

        :param database_version:
            The value to assign to the database_version property of this MySqlDatabaseUsageMetrics.
        :type database_version: str

        :param db_id:
            The value to assign to the db_id property of this MySqlDatabaseUsageMetrics.
        :type db_id: str

        :param database_status:
            The value to assign to the database_status property of this MySqlDatabaseUsageMetrics.
            Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_status: str

        :param heat_wave_management_type:
            The value to assign to the heat_wave_management_type property of this MySqlDatabaseUsageMetrics.
        :type heat_wave_management_type: str

        :param is_heat_wave_enabled:
            The value to assign to the is_heat_wave_enabled property of this MySqlDatabaseUsageMetrics.
        :type is_heat_wave_enabled: bool

        :param heat_wave_cluster_display_name:
            The value to assign to the heat_wave_cluster_display_name property of this MySqlDatabaseUsageMetrics.
        :type heat_wave_cluster_display_name: str

        :param heat_wave_node_count:
            The value to assign to the heat_wave_node_count property of this MySqlDatabaseUsageMetrics.
        :type heat_wave_node_count: int

        :param metrics:
            The value to assign to the metrics property of this MySqlDatabaseUsageMetrics.
        :type metrics: list[oci.database_management.models.MySqlFleetMetricDefinition]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'database_name': 'str',
            'database_type': 'str',
            'mds_deployment_type': 'str',
            'mdslifecycle_state': 'str',
            'database_version': 'str',
            'db_id': 'str',
            'database_status': 'str',
            'heat_wave_management_type': 'str',
            'is_heat_wave_enabled': 'bool',
            'heat_wave_cluster_display_name': 'str',
            'heat_wave_node_count': 'int',
            'metrics': 'list[MySqlFleetMetricDefinition]'
        }
        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'database_name': 'databaseName',
            'database_type': 'databaseType',
            'mds_deployment_type': 'mdsDeploymentType',
            'mdslifecycle_state': 'mdslifecycleState',
            'database_version': 'databaseVersion',
            'db_id': 'dbId',
            'database_status': 'databaseStatus',
            'heat_wave_management_type': 'heatWaveManagementType',
            'is_heat_wave_enabled': 'isHeatWaveEnabled',
            'heat_wave_cluster_display_name': 'heatWaveClusterDisplayName',
            'heat_wave_node_count': 'heatWaveNodeCount',
            'metrics': 'metrics'
        }
        self._compartment_id = None
        self._database_name = None
        self._database_type = None
        self._mds_deployment_type = None
        self._mdslifecycle_state = None
        self._database_version = None
        self._db_id = None
        self._database_status = None
        self._heat_wave_management_type = None
        self._is_heat_wave_enabled = None
        self._heat_wave_cluster_display_name = None
        self._heat_wave_node_count = None
        self._metrics = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MySqlDatabaseUsageMetrics.
        The OCID of the compartment where the Managed MySQL Database resides.


        :return: The compartment_id of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MySqlDatabaseUsageMetrics.
        The OCID of the compartment where the Managed MySQL Database resides.


        :param compartment_id: The compartment_id of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this MySqlDatabaseUsageMetrics.
        The display name of the Managed MySQL Database.


        :return: The database_name of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this MySqlDatabaseUsageMetrics.
        The display name of the Managed MySQL Database.


        :param database_name: The database_name of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._database_name = database_name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this MySqlDatabaseUsageMetrics.
        Indicates MySQL Database type, ONPREMISE or MySQL Database System.


        :return: The database_type of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this MySqlDatabaseUsageMetrics.
        Indicates MySQL Database type, ONPREMISE or MySQL Database System.


        :param database_type: The database_type of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._database_type = database_type

    @property
    def mds_deployment_type(self):
        """
        **[Required]** Gets the mds_deployment_type of this MySqlDatabaseUsageMetrics.
        The type of MySQL Database System.


        :return: The mds_deployment_type of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._mds_deployment_type

    @mds_deployment_type.setter
    def mds_deployment_type(self, mds_deployment_type):
        """
        Sets the mds_deployment_type of this MySqlDatabaseUsageMetrics.
        The type of MySQL Database System.


        :param mds_deployment_type: The mds_deployment_type of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._mds_deployment_type = mds_deployment_type

    @property
    def mdslifecycle_state(self):
        """
        **[Required]** Gets the mdslifecycle_state of this MySqlDatabaseUsageMetrics.
        The lifecycle state of the MySQL Database System.


        :return: The mdslifecycle_state of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._mdslifecycle_state

    @mdslifecycle_state.setter
    def mdslifecycle_state(self, mdslifecycle_state):
        """
        Sets the mdslifecycle_state of this MySqlDatabaseUsageMetrics.
        The lifecycle state of the MySQL Database System.


        :param mdslifecycle_state: The mdslifecycle_state of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._mdslifecycle_state = mdslifecycle_state

    @property
    def database_version(self):
        """
        **[Required]** Gets the database_version of this MySqlDatabaseUsageMetrics.
        The version of the MySQL Database.


        :return: The database_version of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_version

    @database_version.setter
    def database_version(self, database_version):
        """
        Sets the database_version of this MySqlDatabaseUsageMetrics.
        The version of the MySQL Database.


        :param database_version: The database_version of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._database_version = database_version

    @property
    def db_id(self):
        """
        **[Required]** Gets the db_id of this MySqlDatabaseUsageMetrics.
        The OCID of the Managed MySQL Database.


        :return: The db_id of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        """
        Sets the db_id of this MySqlDatabaseUsageMetrics.
        The OCID of the Managed MySQL Database.


        :param db_id: The db_id of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._db_id = db_id

    @property
    def database_status(self):
        """
        **[Required]** Gets the database_status of this MySqlDatabaseUsageMetrics.
        The status of the MySQL Database. Indicates whether the status of the database
        is UP, DOWN, or UNKNOWN at the current time.

        Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_status of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_status

    @database_status.setter
    def database_status(self, database_status):
        """
        Sets the database_status of this MySqlDatabaseUsageMetrics.
        The status of the MySQL Database. Indicates whether the status of the database
        is UP, DOWN, or UNKNOWN at the current time.


        :param database_status: The database_status of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(database_status, allowed_values):
            database_status = 'UNKNOWN_ENUM_VALUE'
        self._database_status = database_status

    @property
    def heat_wave_management_type(self):
        """
        Gets the heat_wave_management_type of this MySqlDatabaseUsageMetrics.
        The customer's selected type for HeatWave management.


        :return: The heat_wave_management_type of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._heat_wave_management_type

    @heat_wave_management_type.setter
    def heat_wave_management_type(self, heat_wave_management_type):
        """
        Sets the heat_wave_management_type of this MySqlDatabaseUsageMetrics.
        The customer's selected type for HeatWave management.


        :param heat_wave_management_type: The heat_wave_management_type of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._heat_wave_management_type = heat_wave_management_type

    @property
    def is_heat_wave_enabled(self):
        """
        Gets the is_heat_wave_enabled of this MySqlDatabaseUsageMetrics.
        Indicates whether HeatWave is enabled for the MySQL Database System or not.


        :return: The is_heat_wave_enabled of this MySqlDatabaseUsageMetrics.
        :rtype: bool
        """
        return self._is_heat_wave_enabled

    @is_heat_wave_enabled.setter
    def is_heat_wave_enabled(self, is_heat_wave_enabled):
        """
        Sets the is_heat_wave_enabled of this MySqlDatabaseUsageMetrics.
        Indicates whether HeatWave is enabled for the MySQL Database System or not.


        :param is_heat_wave_enabled: The is_heat_wave_enabled of this MySqlDatabaseUsageMetrics.
        :type: bool
        """
        self._is_heat_wave_enabled = is_heat_wave_enabled

    @property
    def heat_wave_cluster_display_name(self):
        """
        Gets the heat_wave_cluster_display_name of this MySqlDatabaseUsageMetrics.
        The name of the HeatWave cluster.


        :return: The heat_wave_cluster_display_name of this MySqlDatabaseUsageMetrics.
        :rtype: str
        """
        return self._heat_wave_cluster_display_name

    @heat_wave_cluster_display_name.setter
    def heat_wave_cluster_display_name(self, heat_wave_cluster_display_name):
        """
        Sets the heat_wave_cluster_display_name of this MySqlDatabaseUsageMetrics.
        The name of the HeatWave cluster.


        :param heat_wave_cluster_display_name: The heat_wave_cluster_display_name of this MySqlDatabaseUsageMetrics.
        :type: str
        """
        self._heat_wave_cluster_display_name = heat_wave_cluster_display_name

    @property
    def heat_wave_node_count(self):
        """
        Gets the heat_wave_node_count of this MySqlDatabaseUsageMetrics.
        The number of nodes in the HeatWave cluster.


        :return: The heat_wave_node_count of this MySqlDatabaseUsageMetrics.
        :rtype: int
        """
        return self._heat_wave_node_count

    @heat_wave_node_count.setter
    def heat_wave_node_count(self, heat_wave_node_count):
        """
        Sets the heat_wave_node_count of this MySqlDatabaseUsageMetrics.
        The number of nodes in the HeatWave cluster.


        :param heat_wave_node_count: The heat_wave_node_count of this MySqlDatabaseUsageMetrics.
        :type: int
        """
        self._heat_wave_node_count = heat_wave_node_count

    @property
    def metrics(self):
        """
        **[Required]** Gets the metrics of this MySqlDatabaseUsageMetrics.
        A list of the database health metrics like CPU, Storage, and Memory.


        :return: The metrics of this MySqlDatabaseUsageMetrics.
        :rtype: list[oci.database_management.models.MySqlFleetMetricDefinition]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this MySqlDatabaseUsageMetrics.
        A list of the database health metrics like CPU, Storage, and Memory.


        :param metrics: The metrics of this MySqlDatabaseUsageMetrics.
        :type: list[oci.database_management.models.MySqlFleetMetricDefinition]
        """
        self._metrics = metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
