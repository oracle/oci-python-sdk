# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystem(object):
    """
    A DB System is the core logical unit of MySQL Database Service.
    """

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DbSystem.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbSystem.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DbSystem.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DbSystem.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbSystem.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DbSystem.
        :type subnet_id: str

        :param is_highly_available:
            The value to assign to the is_highly_available property of this DbSystem.
        :type is_highly_available: bool

        :param current_placement:
            The value to assign to the current_placement property of this DbSystem.
        :type current_placement: oci.mysql.models.DbSystemPlacement

        :param is_analytics_cluster_attached:
            The value to assign to the is_analytics_cluster_attached property of this DbSystem.
        :type is_analytics_cluster_attached: bool

        :param analytics_cluster:
            The value to assign to the analytics_cluster property of this DbSystem.
        :type analytics_cluster: oci.mysql.models.AnalyticsClusterSummary

        :param is_heat_wave_cluster_attached:
            The value to assign to the is_heat_wave_cluster_attached property of this DbSystem.
        :type is_heat_wave_cluster_attached: bool

        :param heat_wave_cluster:
            The value to assign to the heat_wave_cluster property of this DbSystem.
        :type heat_wave_cluster: oci.mysql.models.HeatWaveClusterSummary

        :param availability_domain:
            The value to assign to the availability_domain property of this DbSystem.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this DbSystem.
        :type fault_domain: str

        :param shape_name:
            The value to assign to the shape_name property of this DbSystem.
        :type shape_name: str

        :param mysql_version:
            The value to assign to the mysql_version property of this DbSystem.
        :type mysql_version: str

        :param backup_policy:
            The value to assign to the backup_policy property of this DbSystem.
        :type backup_policy: oci.mysql.models.BackupPolicy

        :param source:
            The value to assign to the source property of this DbSystem.
        :type source: oci.mysql.models.DbSystemSource

        :param configuration_id:
            The value to assign to the configuration_id property of this DbSystem.
        :type configuration_id: str

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this DbSystem.
        :type data_storage_size_in_gbs: int

        :param hostname_label:
            The value to assign to the hostname_label property of this DbSystem.
        :type hostname_label: str

        :param ip_address:
            The value to assign to the ip_address property of this DbSystem.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this DbSystem.
        :type port: int

        :param port_x:
            The value to assign to the port_x property of this DbSystem.
        :type port_x: int

        :param endpoints:
            The value to assign to the endpoints property of this DbSystem.
        :type endpoints: list[oci.mysql.models.DbSystemEndpoint]

        :param channels:
            The value to assign to the channels property of this DbSystem.
        :type channels: list[oci.mysql.models.ChannelSummary]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbSystem.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DbSystem.
        :type lifecycle_details: str

        :param maintenance:
            The value to assign to the maintenance property of this DbSystem.
        :type maintenance: oci.mysql.models.MaintenanceDetails

        :param time_created:
            The value to assign to the time_created property of this DbSystem.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DbSystem.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DbSystem.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DbSystem.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'subnet_id': 'str',
            'is_highly_available': 'bool',
            'current_placement': 'DbSystemPlacement',
            'is_analytics_cluster_attached': 'bool',
            'analytics_cluster': 'AnalyticsClusterSummary',
            'is_heat_wave_cluster_attached': 'bool',
            'heat_wave_cluster': 'HeatWaveClusterSummary',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'shape_name': 'str',
            'mysql_version': 'str',
            'backup_policy': 'BackupPolicy',
            'source': 'DbSystemSource',
            'configuration_id': 'str',
            'data_storage_size_in_gbs': 'int',
            'hostname_label': 'str',
            'ip_address': 'str',
            'port': 'int',
            'port_x': 'int',
            'endpoints': 'list[DbSystemEndpoint]',
            'channels': 'list[ChannelSummary]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'maintenance': 'MaintenanceDetails',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'subnet_id': 'subnetId',
            'is_highly_available': 'isHighlyAvailable',
            'current_placement': 'currentPlacement',
            'is_analytics_cluster_attached': 'isAnalyticsClusterAttached',
            'analytics_cluster': 'analyticsCluster',
            'is_heat_wave_cluster_attached': 'isHeatWaveClusterAttached',
            'heat_wave_cluster': 'heatWaveCluster',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'shape_name': 'shapeName',
            'mysql_version': 'mysqlVersion',
            'backup_policy': 'backupPolicy',
            'source': 'source',
            'configuration_id': 'configurationId',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'hostname_label': 'hostnameLabel',
            'ip_address': 'ipAddress',
            'port': 'port',
            'port_x': 'portX',
            'endpoints': 'endpoints',
            'channels': 'channels',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'maintenance': 'maintenance',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._subnet_id = None
        self._is_highly_available = None
        self._current_placement = None
        self._is_analytics_cluster_attached = None
        self._analytics_cluster = None
        self._is_heat_wave_cluster_attached = None
        self._heat_wave_cluster = None
        self._availability_domain = None
        self._fault_domain = None
        self._shape_name = None
        self._mysql_version = None
        self._backup_policy = None
        self._source = None
        self._configuration_id = None
        self._data_storage_size_in_gbs = None
        self._hostname_label = None
        self._ip_address = None
        self._port = None
        self._port_x = None
        self._endpoints = None
        self._channels = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._maintenance = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbSystem.
        The OCID of the DB System.


        :return: The id of this DbSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbSystem.
        The OCID of the DB System.


        :param id: The id of this DbSystem.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DbSystem.
        The user-friendly name for the DB System. It does not have to be unique.


        :return: The display_name of this DbSystem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbSystem.
        The user-friendly name for the DB System. It does not have to be unique.


        :param display_name: The display_name of this DbSystem.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DbSystem.
        User-provided data about the DB System.


        :return: The description of this DbSystem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DbSystem.
        User-provided data about the DB System.


        :param description: The description of this DbSystem.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DbSystem.
        The OCID of the compartment the DB System belongs in.


        :return: The compartment_id of this DbSystem.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbSystem.
        The OCID of the compartment the DB System belongs in.


        :param compartment_id: The compartment_id of this DbSystem.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DbSystem.
        The OCID of the subnet the DB System is associated with.


        :return: The subnet_id of this DbSystem.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DbSystem.
        The OCID of the subnet the DB System is associated with.


        :param subnet_id: The subnet_id of this DbSystem.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def is_highly_available(self):
        """
        Gets the is_highly_available of this DbSystem.
        If the policy is to enable high availability of the instance, by
        maintaining secondary/failover capacity as necessary.


        :return: The is_highly_available of this DbSystem.
        :rtype: bool
        """
        return self._is_highly_available

    @is_highly_available.setter
    def is_highly_available(self, is_highly_available):
        """
        Sets the is_highly_available of this DbSystem.
        If the policy is to enable high availability of the instance, by
        maintaining secondary/failover capacity as necessary.


        :param is_highly_available: The is_highly_available of this DbSystem.
        :type: bool
        """
        self._is_highly_available = is_highly_available

    @property
    def current_placement(self):
        """
        Gets the current_placement of this DbSystem.

        :return: The current_placement of this DbSystem.
        :rtype: oci.mysql.models.DbSystemPlacement
        """
        return self._current_placement

    @current_placement.setter
    def current_placement(self, current_placement):
        """
        Sets the current_placement of this DbSystem.

        :param current_placement: The current_placement of this DbSystem.
        :type: oci.mysql.models.DbSystemPlacement
        """
        self._current_placement = current_placement

    @property
    def is_analytics_cluster_attached(self):
        """
        Gets the is_analytics_cluster_attached of this DbSystem.
        DEPRECATED -- please use `isHeatWaveClusterAttached` instead.
        If the DB System has an Analytics Cluster attached.


        :return: The is_analytics_cluster_attached of this DbSystem.
        :rtype: bool
        """
        return self._is_analytics_cluster_attached

    @is_analytics_cluster_attached.setter
    def is_analytics_cluster_attached(self, is_analytics_cluster_attached):
        """
        Sets the is_analytics_cluster_attached of this DbSystem.
        DEPRECATED -- please use `isHeatWaveClusterAttached` instead.
        If the DB System has an Analytics Cluster attached.


        :param is_analytics_cluster_attached: The is_analytics_cluster_attached of this DbSystem.
        :type: bool
        """
        self._is_analytics_cluster_attached = is_analytics_cluster_attached

    @property
    def analytics_cluster(self):
        """
        Gets the analytics_cluster of this DbSystem.

        :return: The analytics_cluster of this DbSystem.
        :rtype: oci.mysql.models.AnalyticsClusterSummary
        """
        return self._analytics_cluster

    @analytics_cluster.setter
    def analytics_cluster(self, analytics_cluster):
        """
        Sets the analytics_cluster of this DbSystem.

        :param analytics_cluster: The analytics_cluster of this DbSystem.
        :type: oci.mysql.models.AnalyticsClusterSummary
        """
        self._analytics_cluster = analytics_cluster

    @property
    def is_heat_wave_cluster_attached(self):
        """
        Gets the is_heat_wave_cluster_attached of this DbSystem.
        If the DB System has a HeatWave Cluster attached.


        :return: The is_heat_wave_cluster_attached of this DbSystem.
        :rtype: bool
        """
        return self._is_heat_wave_cluster_attached

    @is_heat_wave_cluster_attached.setter
    def is_heat_wave_cluster_attached(self, is_heat_wave_cluster_attached):
        """
        Sets the is_heat_wave_cluster_attached of this DbSystem.
        If the DB System has a HeatWave Cluster attached.


        :param is_heat_wave_cluster_attached: The is_heat_wave_cluster_attached of this DbSystem.
        :type: bool
        """
        self._is_heat_wave_cluster_attached = is_heat_wave_cluster_attached

    @property
    def heat_wave_cluster(self):
        """
        Gets the heat_wave_cluster of this DbSystem.

        :return: The heat_wave_cluster of this DbSystem.
        :rtype: oci.mysql.models.HeatWaveClusterSummary
        """
        return self._heat_wave_cluster

    @heat_wave_cluster.setter
    def heat_wave_cluster(self, heat_wave_cluster):
        """
        Sets the heat_wave_cluster of this DbSystem.

        :param heat_wave_cluster: The heat_wave_cluster of this DbSystem.
        :type: oci.mysql.models.HeatWaveClusterSummary
        """
        self._heat_wave_cluster = heat_wave_cluster

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this DbSystem.
        The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the availability domain in which the DB System is placed.


        :return: The availability_domain of this DbSystem.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DbSystem.
        The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the availability domain in which the DB System is placed.


        :param availability_domain: The availability_domain of this DbSystem.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this DbSystem.
        The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the fault domain in which the DB System is placed.


        :return: The fault_domain of this DbSystem.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this DbSystem.
        The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the fault domain in which the DB System is placed.


        :param fault_domain: The fault_domain of this DbSystem.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def shape_name(self):
        """
        Gets the shape_name of this DbSystem.
        The shape of the primary instances of the DB System. The shape
        determines resources allocated to a DB System - CPU cores
        and memory for VM shapes; CPU cores, memory and storage for non-VM
        (or bare metal) shapes. To get a list of shapes, use (the
        :func:`list_shapes` operation.


        :return: The shape_name of this DbSystem.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this DbSystem.
        The shape of the primary instances of the DB System. The shape
        determines resources allocated to a DB System - CPU cores
        and memory for VM shapes; CPU cores, memory and storage for non-VM
        (or bare metal) shapes. To get a list of shapes, use (the
        :func:`list_shapes` operation.


        :param shape_name: The shape_name of this DbSystem.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def mysql_version(self):
        """
        **[Required]** Gets the mysql_version of this DbSystem.
        Name of the MySQL Version in use for the DB System.


        :return: The mysql_version of this DbSystem.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this DbSystem.
        Name of the MySQL Version in use for the DB System.


        :param mysql_version: The mysql_version of this DbSystem.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def backup_policy(self):
        """
        Gets the backup_policy of this DbSystem.

        :return: The backup_policy of this DbSystem.
        :rtype: oci.mysql.models.BackupPolicy
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        """
        Sets the backup_policy of this DbSystem.

        :param backup_policy: The backup_policy of this DbSystem.
        :type: oci.mysql.models.BackupPolicy
        """
        self._backup_policy = backup_policy

    @property
    def source(self):
        """
        Gets the source of this DbSystem.

        :return: The source of this DbSystem.
        :rtype: oci.mysql.models.DbSystemSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this DbSystem.

        :param source: The source of this DbSystem.
        :type: oci.mysql.models.DbSystemSource
        """
        self._source = source

    @property
    def configuration_id(self):
        """
        Gets the configuration_id of this DbSystem.
        The OCID of the Configuration to be used for Instances in this DB System.


        :return: The configuration_id of this DbSystem.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """
        Sets the configuration_id of this DbSystem.
        The OCID of the Configuration to be used for Instances in this DB System.


        :param configuration_id: The configuration_id of this DbSystem.
        :type: str
        """
        self._configuration_id = configuration_id

    @property
    def data_storage_size_in_gbs(self):
        """
        **[Required]** Gets the data_storage_size_in_gbs of this DbSystem.
        Initial size of the data volume in GiBs that will be created and attached.


        :return: The data_storage_size_in_gbs of this DbSystem.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this DbSystem.
        Initial size of the data volume in GiBs that will be created and attached.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this DbSystem.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this DbSystem.
        The hostname for the primary endpoint of the DB System. Used for DNS.
        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").
        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :return: The hostname_label of this DbSystem.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this DbSystem.
        The hostname for the primary endpoint of the DB System. Used for DNS.
        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").
        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :param hostname_label: The hostname_label of this DbSystem.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def ip_address(self):
        """
        Gets the ip_address of this DbSystem.
        The IP address the DB System is configured to listen on. A private
        IP address of the primary endpoint of the DB System. Must be an
        available IP address within the subnet's CIDR. This will be a
        \"dotted-quad\" style IPv4 address.


        :return: The ip_address of this DbSystem.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this DbSystem.
        The IP address the DB System is configured to listen on. A private
        IP address of the primary endpoint of the DB System. Must be an
        available IP address within the subnet's CIDR. This will be a
        \"dotted-quad\" style IPv4 address.


        :param ip_address: The ip_address of this DbSystem.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        Gets the port of this DbSystem.
        The port for primary endpoint of the DB System to listen on.


        :return: The port of this DbSystem.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this DbSystem.
        The port for primary endpoint of the DB System to listen on.


        :param port: The port of this DbSystem.
        :type: int
        """
        self._port = port

    @property
    def port_x(self):
        """
        Gets the port_x of this DbSystem.
        The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.


        :return: The port_x of this DbSystem.
        :rtype: int
        """
        return self._port_x

    @port_x.setter
    def port_x(self, port_x):
        """
        Sets the port_x of this DbSystem.
        The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.


        :param port_x: The port_x of this DbSystem.
        :type: int
        """
        self._port_x = port_x

    @property
    def endpoints(self):
        """
        Gets the endpoints of this DbSystem.
        The network endpoints available for this DB System.


        :return: The endpoints of this DbSystem.
        :rtype: list[oci.mysql.models.DbSystemEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this DbSystem.
        The network endpoints available for this DB System.


        :param endpoints: The endpoints of this DbSystem.
        :type: list[oci.mysql.models.DbSystemEndpoint]
        """
        self._endpoints = endpoints

    @property
    def channels(self):
        """
        Gets the channels of this DbSystem.
        A list with a summary of all the Channels attached to the DB System.


        :return: The channels of this DbSystem.
        :rtype: list[oci.mysql.models.ChannelSummary]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """
        Sets the channels of this DbSystem.
        A list with a summary of all the Channels attached to the DB System.


        :param channels: The channels of this DbSystem.
        :type: list[oci.mysql.models.ChannelSummary]
        """
        self._channels = channels

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DbSystem.
        The current state of the DB System.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbSystem.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbSystem.
        The current state of the DB System.


        :param lifecycle_state: The lifecycle_state of this DbSystem.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DbSystem.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this DbSystem.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DbSystem.
        Additional information about the current lifecycleState.


        :param lifecycle_details: The lifecycle_details of this DbSystem.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def maintenance(self):
        """
        **[Required]** Gets the maintenance of this DbSystem.

        :return: The maintenance of this DbSystem.
        :rtype: oci.mysql.models.MaintenanceDetails
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """
        Sets the maintenance of this DbSystem.

        :param maintenance: The maintenance of this DbSystem.
        :type: oci.mysql.models.MaintenanceDetails
        """
        self._maintenance = maintenance

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DbSystem.
        The date and time the DB System was created.


        :return: The time_created of this DbSystem.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbSystem.
        The date and time the DB System was created.


        :param time_created: The time_created of this DbSystem.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DbSystem.
        The time the DB System was last updated.


        :return: The time_updated of this DbSystem.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DbSystem.
        The time the DB System was last updated.


        :param time_updated: The time_updated of this DbSystem.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DbSystem.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DbSystem.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DbSystem.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DbSystem.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DbSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DbSystem.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DbSystem.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DbSystem.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
