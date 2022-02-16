# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemSummary(object):
    """
    A summary of a DB System.
    """

    #: A constant which can be used with the crash_recovery property of a DbSystemSummary.
    #: This constant has a value of "ENABLED"
    CRASH_RECOVERY_ENABLED = "ENABLED"

    #: A constant which can be used with the crash_recovery property of a DbSystemSummary.
    #: This constant has a value of "DISABLED"
    CRASH_RECOVERY_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbSystemSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DbSystemSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DbSystemSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DbSystemSummary.
        :type compartment_id: str

        :param is_highly_available:
            The value to assign to the is_highly_available property of this DbSystemSummary.
        :type is_highly_available: bool

        :param current_placement:
            The value to assign to the current_placement property of this DbSystemSummary.
        :type current_placement: oci.mysql.models.DbSystemPlacement

        :param is_analytics_cluster_attached:
            The value to assign to the is_analytics_cluster_attached property of this DbSystemSummary.
        :type is_analytics_cluster_attached: bool

        :param analytics_cluster:
            The value to assign to the analytics_cluster property of this DbSystemSummary.
        :type analytics_cluster: oci.mysql.models.AnalyticsClusterSummary

        :param is_heat_wave_cluster_attached:
            The value to assign to the is_heat_wave_cluster_attached property of this DbSystemSummary.
        :type is_heat_wave_cluster_attached: bool

        :param heat_wave_cluster:
            The value to assign to the heat_wave_cluster property of this DbSystemSummary.
        :type heat_wave_cluster: oci.mysql.models.HeatWaveClusterSummary

        :param availability_domain:
            The value to assign to the availability_domain property of this DbSystemSummary.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this DbSystemSummary.
        :type fault_domain: str

        :param endpoints:
            The value to assign to the endpoints property of this DbSystemSummary.
        :type endpoints: list[oci.mysql.models.DbSystemEndpoint]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbSystemSummary.
        :type lifecycle_state: str

        :param mysql_version:
            The value to assign to the mysql_version property of this DbSystemSummary.
        :type mysql_version: str

        :param time_created:
            The value to assign to the time_created property of this DbSystemSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DbSystemSummary.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DbSystemSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DbSystemSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param crash_recovery:
            The value to assign to the crash_recovery property of this DbSystemSummary.
            Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type crash_recovery: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'is_highly_available': 'bool',
            'current_placement': 'DbSystemPlacement',
            'is_analytics_cluster_attached': 'bool',
            'analytics_cluster': 'AnalyticsClusterSummary',
            'is_heat_wave_cluster_attached': 'bool',
            'heat_wave_cluster': 'HeatWaveClusterSummary',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'endpoints': 'list[DbSystemEndpoint]',
            'lifecycle_state': 'str',
            'mysql_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'crash_recovery': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'is_highly_available': 'isHighlyAvailable',
            'current_placement': 'currentPlacement',
            'is_analytics_cluster_attached': 'isAnalyticsClusterAttached',
            'analytics_cluster': 'analyticsCluster',
            'is_heat_wave_cluster_attached': 'isHeatWaveClusterAttached',
            'heat_wave_cluster': 'heatWaveCluster',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'endpoints': 'endpoints',
            'lifecycle_state': 'lifecycleState',
            'mysql_version': 'mysqlVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'crash_recovery': 'crashRecovery'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._is_highly_available = None
        self._current_placement = None
        self._is_analytics_cluster_attached = None
        self._analytics_cluster = None
        self._is_heat_wave_cluster_attached = None
        self._heat_wave_cluster = None
        self._availability_domain = None
        self._fault_domain = None
        self._endpoints = None
        self._lifecycle_state = None
        self._mysql_version = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._crash_recovery = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbSystemSummary.
        The OCID of the DB System.


        :return: The id of this DbSystemSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbSystemSummary.
        The OCID of the DB System.


        :param id: The id of this DbSystemSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DbSystemSummary.
        The user-friendly name for the DB System. It does not have to be unique.


        :return: The display_name of this DbSystemSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbSystemSummary.
        The user-friendly name for the DB System. It does not have to be unique.


        :param display_name: The display_name of this DbSystemSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DbSystemSummary.
        User-provided data about the DB System.


        :return: The description of this DbSystemSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DbSystemSummary.
        User-provided data about the DB System.


        :param description: The description of this DbSystemSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DbSystemSummary.
        The OCID of the compartment the DB System belongs in.


        :return: The compartment_id of this DbSystemSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbSystemSummary.
        The OCID of the compartment the DB System belongs in.


        :param compartment_id: The compartment_id of this DbSystemSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_highly_available(self):
        """
        Gets the is_highly_available of this DbSystemSummary.
        If the policy is to enable high availability of the instance, by
        maintaining secondary/failover capacity as necessary.


        :return: The is_highly_available of this DbSystemSummary.
        :rtype: bool
        """
        return self._is_highly_available

    @is_highly_available.setter
    def is_highly_available(self, is_highly_available):
        """
        Sets the is_highly_available of this DbSystemSummary.
        If the policy is to enable high availability of the instance, by
        maintaining secondary/failover capacity as necessary.


        :param is_highly_available: The is_highly_available of this DbSystemSummary.
        :type: bool
        """
        self._is_highly_available = is_highly_available

    @property
    def current_placement(self):
        """
        Gets the current_placement of this DbSystemSummary.

        :return: The current_placement of this DbSystemSummary.
        :rtype: oci.mysql.models.DbSystemPlacement
        """
        return self._current_placement

    @current_placement.setter
    def current_placement(self, current_placement):
        """
        Sets the current_placement of this DbSystemSummary.

        :param current_placement: The current_placement of this DbSystemSummary.
        :type: oci.mysql.models.DbSystemPlacement
        """
        self._current_placement = current_placement

    @property
    def is_analytics_cluster_attached(self):
        """
        Gets the is_analytics_cluster_attached of this DbSystemSummary.
        DEPRECATED -- please use `isHeatWaveClusterAttached` instead.
        If the DB System has an Analytics Cluster attached.


        :return: The is_analytics_cluster_attached of this DbSystemSummary.
        :rtype: bool
        """
        return self._is_analytics_cluster_attached

    @is_analytics_cluster_attached.setter
    def is_analytics_cluster_attached(self, is_analytics_cluster_attached):
        """
        Sets the is_analytics_cluster_attached of this DbSystemSummary.
        DEPRECATED -- please use `isHeatWaveClusterAttached` instead.
        If the DB System has an Analytics Cluster attached.


        :param is_analytics_cluster_attached: The is_analytics_cluster_attached of this DbSystemSummary.
        :type: bool
        """
        self._is_analytics_cluster_attached = is_analytics_cluster_attached

    @property
    def analytics_cluster(self):
        """
        Gets the analytics_cluster of this DbSystemSummary.

        :return: The analytics_cluster of this DbSystemSummary.
        :rtype: oci.mysql.models.AnalyticsClusterSummary
        """
        return self._analytics_cluster

    @analytics_cluster.setter
    def analytics_cluster(self, analytics_cluster):
        """
        Sets the analytics_cluster of this DbSystemSummary.

        :param analytics_cluster: The analytics_cluster of this DbSystemSummary.
        :type: oci.mysql.models.AnalyticsClusterSummary
        """
        self._analytics_cluster = analytics_cluster

    @property
    def is_heat_wave_cluster_attached(self):
        """
        Gets the is_heat_wave_cluster_attached of this DbSystemSummary.
        If the DB System has a HeatWave Cluster attached.


        :return: The is_heat_wave_cluster_attached of this DbSystemSummary.
        :rtype: bool
        """
        return self._is_heat_wave_cluster_attached

    @is_heat_wave_cluster_attached.setter
    def is_heat_wave_cluster_attached(self, is_heat_wave_cluster_attached):
        """
        Sets the is_heat_wave_cluster_attached of this DbSystemSummary.
        If the DB System has a HeatWave Cluster attached.


        :param is_heat_wave_cluster_attached: The is_heat_wave_cluster_attached of this DbSystemSummary.
        :type: bool
        """
        self._is_heat_wave_cluster_attached = is_heat_wave_cluster_attached

    @property
    def heat_wave_cluster(self):
        """
        Gets the heat_wave_cluster of this DbSystemSummary.

        :return: The heat_wave_cluster of this DbSystemSummary.
        :rtype: oci.mysql.models.HeatWaveClusterSummary
        """
        return self._heat_wave_cluster

    @heat_wave_cluster.setter
    def heat_wave_cluster(self, heat_wave_cluster):
        """
        Sets the heat_wave_cluster of this DbSystemSummary.

        :param heat_wave_cluster: The heat_wave_cluster of this DbSystemSummary.
        :type: oci.mysql.models.HeatWaveClusterSummary
        """
        self._heat_wave_cluster = heat_wave_cluster

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this DbSystemSummary.
        The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the availability domain in which the DB System is placed.


        :return: The availability_domain of this DbSystemSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this DbSystemSummary.
        The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the availability domain in which the DB System is placed.


        :param availability_domain: The availability_domain of this DbSystemSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this DbSystemSummary.
        The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the fault domain in which the DB System is placed.


        :return: The fault_domain of this DbSystemSummary.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this DbSystemSummary.
        The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.

        In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains
        and the MySQL instance in that domain is promoted to the primary instance.
        This redirection does not affect the IP address of the DB System in any way.

        For a standalone DB System, this defines the fault domain in which the DB System is placed.


        :param fault_domain: The fault_domain of this DbSystemSummary.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def endpoints(self):
        """
        Gets the endpoints of this DbSystemSummary.
        The network endpoints available for this DB System.


        :return: The endpoints of this DbSystemSummary.
        :rtype: list[oci.mysql.models.DbSystemEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """
        Sets the endpoints of this DbSystemSummary.
        The network endpoints available for this DB System.


        :param endpoints: The endpoints of this DbSystemSummary.
        :type: list[oci.mysql.models.DbSystemEndpoint]
        """
        self._endpoints = endpoints

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DbSystemSummary.
        The current state of the DB System.


        :return: The lifecycle_state of this DbSystemSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbSystemSummary.
        The current state of the DB System.


        :param lifecycle_state: The lifecycle_state of this DbSystemSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def mysql_version(self):
        """
        **[Required]** Gets the mysql_version of this DbSystemSummary.
        Name of the MySQL Version in use for the DB System.


        :return: The mysql_version of this DbSystemSummary.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this DbSystemSummary.
        Name of the MySQL Version in use for the DB System.


        :param mysql_version: The mysql_version of this DbSystemSummary.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DbSystemSummary.
        The date and time the DB System was created.


        :return: The time_created of this DbSystemSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbSystemSummary.
        The date and time the DB System was created.


        :param time_created: The time_created of this DbSystemSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DbSystemSummary.
        The time the DB System was last updated.


        :return: The time_updated of this DbSystemSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DbSystemSummary.
        The time the DB System was last updated.


        :param time_updated: The time_updated of this DbSystemSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DbSystemSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DbSystemSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DbSystemSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DbSystemSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DbSystemSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DbSystemSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DbSystemSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DbSystemSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def crash_recovery(self):
        """
        Gets the crash_recovery of this DbSystemSummary.
        Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled,
        and whether to enable or disable syncing of the Binary Logs.

        Allowed values for this property are: "ENABLED", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The crash_recovery of this DbSystemSummary.
        :rtype: str
        """
        return self._crash_recovery

    @crash_recovery.setter
    def crash_recovery(self, crash_recovery):
        """
        Sets the crash_recovery of this DbSystemSummary.
        Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled,
        and whether to enable or disable syncing of the Binary Logs.


        :param crash_recovery: The crash_recovery of this DbSystemSummary.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(crash_recovery, allowed_values):
            crash_recovery = 'UNKNOWN_ENUM_VALUE'
        self._crash_recovery = crash_recovery

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
