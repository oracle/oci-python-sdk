# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BdsInstance(object):
    """
    Description of the BDS instance
    """

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "SUSPENDING"
    LIFECYCLE_STATE_SUSPENDING = "SUSPENDING"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "SUSPENDED"
    LIFECYCLE_STATE_SUSPENDED = "SUSPENDED"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "RESUMING"
    LIFECYCLE_STATE_RESUMING = "RESUMING"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a BdsInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the cluster_version property of a BdsInstance.
    #: This constant has a value of "CDH5"
    CLUSTER_VERSION_CDH5 = "CDH5"

    #: A constant which can be used with the cluster_version property of a BdsInstance.
    #: This constant has a value of "CDH6"
    CLUSTER_VERSION_CDH6 = "CDH6"

    def __init__(self, **kwargs):
        """
        Initializes a new BdsInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BdsInstance.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BdsInstance.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this BdsInstance.
        :type display_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BdsInstance.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "SUSPENDING", "SUSPENDED", "RESUMING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param cluster_version:
            The value to assign to the cluster_version property of this BdsInstance.
            Allowed values for this property are: "CDH5", "CDH6", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type cluster_version: str

        :param is_high_availability:
            The value to assign to the is_high_availability property of this BdsInstance.
        :type is_high_availability: bool

        :param is_secure:
            The value to assign to the is_secure property of this BdsInstance.
        :type is_secure: bool

        :param is_cloud_sql_configured:
            The value to assign to the is_cloud_sql_configured property of this BdsInstance.
        :type is_cloud_sql_configured: bool

        :param network_config:
            The value to assign to the network_config property of this BdsInstance.
        :type network_config: oci.bds.models.NetworkConfig

        :param cluster_details:
            The value to assign to the cluster_details property of this BdsInstance.
        :type cluster_details: oci.bds.models.ClusterDetails

        :param nodes:
            The value to assign to the nodes property of this BdsInstance.
        :type nodes: list[oci.bds.models.Node]

        :param cloud_sql_details:
            The value to assign to the cloud_sql_details property of this BdsInstance.
        :type cloud_sql_details: oci.bds.models.CloudSqlDetails

        :param created_by:
            The value to assign to the created_by property of this BdsInstance.
        :type created_by: str

        :param time_created:
            The value to assign to the time_created property of this BdsInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BdsInstance.
        :type time_updated: datetime

        :param number_of_nodes:
            The value to assign to the number_of_nodes property of this BdsInstance.
        :type number_of_nodes: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BdsInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BdsInstance.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'lifecycle_state': 'str',
            'cluster_version': 'str',
            'is_high_availability': 'bool',
            'is_secure': 'bool',
            'is_cloud_sql_configured': 'bool',
            'network_config': 'NetworkConfig',
            'cluster_details': 'ClusterDetails',
            'nodes': 'list[Node]',
            'cloud_sql_details': 'CloudSqlDetails',
            'created_by': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'number_of_nodes': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'lifecycle_state': 'lifecycleState',
            'cluster_version': 'clusterVersion',
            'is_high_availability': 'isHighAvailability',
            'is_secure': 'isSecure',
            'is_cloud_sql_configured': 'isCloudSqlConfigured',
            'network_config': 'networkConfig',
            'cluster_details': 'clusterDetails',
            'nodes': 'nodes',
            'cloud_sql_details': 'cloudSqlDetails',
            'created_by': 'createdBy',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'number_of_nodes': 'numberOfNodes',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._lifecycle_state = None
        self._cluster_version = None
        self._is_high_availability = None
        self._is_secure = None
        self._is_cloud_sql_configured = None
        self._network_config = None
        self._cluster_details = None
        self._nodes = None
        self._cloud_sql_details = None
        self._created_by = None
        self._time_created = None
        self._time_updated = None
        self._number_of_nodes = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BdsInstance.
        The OCID of the BDS resource


        :return: The id of this BdsInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BdsInstance.
        The OCID of the BDS resource


        :param id: The id of this BdsInstance.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BdsInstance.
        The OCID of the compartment


        :return: The compartment_id of this BdsInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BdsInstance.
        The OCID of the compartment


        :param compartment_id: The compartment_id of this BdsInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BdsInstance.
        Name of the BDS instance


        :return: The display_name of this BdsInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BdsInstance.
        Name of the BDS instance


        :param display_name: The display_name of this BdsInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BdsInstance.
        The state of the BDS instance

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "SUSPENDING", "SUSPENDED", "RESUMING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BdsInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BdsInstance.
        The state of the BDS instance


        :param lifecycle_state: The lifecycle_state of this BdsInstance.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "SUSPENDING", "SUSPENDED", "RESUMING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def cluster_version(self):
        """
        Gets the cluster_version of this BdsInstance.
        Version of the Hadoop distribution

        Allowed values for this property are: "CDH5", "CDH6", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The cluster_version of this BdsInstance.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """
        Sets the cluster_version of this BdsInstance.
        Version of the Hadoop distribution


        :param cluster_version: The cluster_version of this BdsInstance.
        :type: str
        """
        allowed_values = ["CDH5", "CDH6"]
        if not value_allowed_none_or_none_sentinel(cluster_version, allowed_values):
            cluster_version = 'UNKNOWN_ENUM_VALUE'
        self._cluster_version = cluster_version

    @property
    def is_high_availability(self):
        """
        **[Required]** Gets the is_high_availability of this BdsInstance.
        Boolean flag specifying whether or not the cluster is HA


        :return: The is_high_availability of this BdsInstance.
        :rtype: bool
        """
        return self._is_high_availability

    @is_high_availability.setter
    def is_high_availability(self, is_high_availability):
        """
        Sets the is_high_availability of this BdsInstance.
        Boolean flag specifying whether or not the cluster is HA


        :param is_high_availability: The is_high_availability of this BdsInstance.
        :type: bool
        """
        self._is_high_availability = is_high_availability

    @property
    def is_secure(self):
        """
        **[Required]** Gets the is_secure of this BdsInstance.
        Boolean flag specifying whether or not the cluster should be setup as secure.


        :return: The is_secure of this BdsInstance.
        :rtype: bool
        """
        return self._is_secure

    @is_secure.setter
    def is_secure(self, is_secure):
        """
        Sets the is_secure of this BdsInstance.
        Boolean flag specifying whether or not the cluster should be setup as secure.


        :param is_secure: The is_secure of this BdsInstance.
        :type: bool
        """
        self._is_secure = is_secure

    @property
    def is_cloud_sql_configured(self):
        """
        **[Required]** Gets the is_cloud_sql_configured of this BdsInstance.
        Boolean flag specifying whether we configure Cloud SQL or not


        :return: The is_cloud_sql_configured of this BdsInstance.
        :rtype: bool
        """
        return self._is_cloud_sql_configured

    @is_cloud_sql_configured.setter
    def is_cloud_sql_configured(self, is_cloud_sql_configured):
        """
        Sets the is_cloud_sql_configured of this BdsInstance.
        Boolean flag specifying whether we configure Cloud SQL or not


        :param is_cloud_sql_configured: The is_cloud_sql_configured of this BdsInstance.
        :type: bool
        """
        self._is_cloud_sql_configured = is_cloud_sql_configured

    @property
    def network_config(self):
        """
        Gets the network_config of this BdsInstance.

        :return: The network_config of this BdsInstance.
        :rtype: oci.bds.models.NetworkConfig
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        """
        Sets the network_config of this BdsInstance.

        :param network_config: The network_config of this BdsInstance.
        :type: oci.bds.models.NetworkConfig
        """
        self._network_config = network_config

    @property
    def cluster_details(self):
        """
        Gets the cluster_details of this BdsInstance.

        :return: The cluster_details of this BdsInstance.
        :rtype: oci.bds.models.ClusterDetails
        """
        return self._cluster_details

    @cluster_details.setter
    def cluster_details(self, cluster_details):
        """
        Sets the cluster_details of this BdsInstance.

        :param cluster_details: The cluster_details of this BdsInstance.
        :type: oci.bds.models.ClusterDetails
        """
        self._cluster_details = cluster_details

    @property
    def nodes(self):
        """
        **[Required]** Gets the nodes of this BdsInstance.
        The list of nodes in the BDS instance


        :return: The nodes of this BdsInstance.
        :rtype: list[oci.bds.models.Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this BdsInstance.
        The list of nodes in the BDS instance


        :param nodes: The nodes of this BdsInstance.
        :type: list[oci.bds.models.Node]
        """
        self._nodes = nodes

    @property
    def cloud_sql_details(self):
        """
        Gets the cloud_sql_details of this BdsInstance.

        :return: The cloud_sql_details of this BdsInstance.
        :rtype: oci.bds.models.CloudSqlDetails
        """
        return self._cloud_sql_details

    @cloud_sql_details.setter
    def cloud_sql_details(self, cloud_sql_details):
        """
        Sets the cloud_sql_details of this BdsInstance.

        :param cloud_sql_details: The cloud_sql_details of this BdsInstance.
        :type: oci.bds.models.CloudSqlDetails
        """
        self._cloud_sql_details = cloud_sql_details

    @property
    def created_by(self):
        """
        Gets the created_by of this BdsInstance.
        The user who created the BDS instance.


        :return: The created_by of this BdsInstance.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this BdsInstance.
        The user who created the BDS instance.


        :param created_by: The created_by of this BdsInstance.
        :type: str
        """
        self._created_by = created_by

    @property
    def time_created(self):
        """
        Gets the time_created of this BdsInstance.
        The time the BDS instance was created. An RFC3339 formatted datetime string


        :return: The time_created of this BdsInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BdsInstance.
        The time the BDS instance was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this BdsInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BdsInstance.
        The time the BDS instance was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this BdsInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BdsInstance.
        The time the BDS instance was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this BdsInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def number_of_nodes(self):
        """
        **[Required]** Gets the number_of_nodes of this BdsInstance.
        Number of nodes that forming the cluster


        :return: The number_of_nodes of this BdsInstance.
        :rtype: int
        """
        return self._number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, number_of_nodes):
        """
        Sets the number_of_nodes of this BdsInstance.
        Number of nodes that forming the cluster


        :param number_of_nodes: The number_of_nodes of this BdsInstance.
        :type: int
        """
        self._number_of_nodes = number_of_nodes

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BdsInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BdsInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BdsInstance.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BdsInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BdsInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BdsInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BdsInstance.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BdsInstance.
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
