# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20250101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DistributedDatabasePrivateEndpoint(object):
    """
    DistributedDatabasePrivateEndpoint resource.
    """

    #: A constant which can be used with the lifecycle_state property of a DistributedDatabasePrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DistributedDatabasePrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DistributedDatabasePrivateEndpoint.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DistributedDatabasePrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DistributedDatabasePrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DistributedDatabasePrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DistributedDatabasePrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    def __init__(self, **kwargs):
        """
        Initializes a new DistributedDatabasePrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DistributedDatabasePrivateEndpoint.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DistributedDatabasePrivateEndpoint.
        :type compartment_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DistributedDatabasePrivateEndpoint.
        :type subnet_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this DistributedDatabasePrivateEndpoint.
        :type vcn_id: str

        :param display_name:
            The value to assign to the display_name property of this DistributedDatabasePrivateEndpoint.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DistributedDatabasePrivateEndpoint.
        :type description: str

        :param private_ip:
            The value to assign to the private_ip property of this DistributedDatabasePrivateEndpoint.
        :type private_ip: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DistributedDatabasePrivateEndpoint.
        :type nsg_ids: list[str]

        :param globally_distributed_databases:
            The value to assign to the globally_distributed_databases property of this DistributedDatabasePrivateEndpoint.
        :type globally_distributed_databases: list[oci.distributed_database.models.DistributedDatabaseAssociatedWithPrivateEndpoint]

        :param globally_distributed_autonomous_databases:
            The value to assign to the globally_distributed_autonomous_databases property of this DistributedDatabasePrivateEndpoint.
        :type globally_distributed_autonomous_databases: list[oci.distributed_database.models.DistributedAutonomousDatabaseAssociatedWithPrivateEndpoint]

        :param time_created:
            The value to assign to the time_created property of this DistributedDatabasePrivateEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DistributedDatabasePrivateEndpoint.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DistributedDatabasePrivateEndpoint.
            Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DistributedDatabasePrivateEndpoint.
        :type lifecycle_details: str

        :param proxy_compute_instance_id:
            The value to assign to the proxy_compute_instance_id property of this DistributedDatabasePrivateEndpoint.
        :type proxy_compute_instance_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DistributedDatabasePrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DistributedDatabasePrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DistributedDatabasePrivateEndpoint.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'subnet_id': 'str',
            'vcn_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'private_ip': 'str',
            'nsg_ids': 'list[str]',
            'globally_distributed_databases': 'list[DistributedDatabaseAssociatedWithPrivateEndpoint]',
            'globally_distributed_autonomous_databases': 'list[DistributedAutonomousDatabaseAssociatedWithPrivateEndpoint]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'proxy_compute_instance_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'subnet_id': 'subnetId',
            'vcn_id': 'vcnId',
            'display_name': 'displayName',
            'description': 'description',
            'private_ip': 'privateIp',
            'nsg_ids': 'nsgIds',
            'globally_distributed_databases': 'globallyDistributedDatabases',
            'globally_distributed_autonomous_databases': 'globallyDistributedAutonomousDatabases',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'proxy_compute_instance_id': 'proxyComputeInstanceId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._compartment_id = None
        self._subnet_id = None
        self._vcn_id = None
        self._display_name = None
        self._description = None
        self._private_ip = None
        self._nsg_ids = None
        self._globally_distributed_databases = None
        self._globally_distributed_autonomous_databases = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._proxy_compute_instance_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DistributedDatabasePrivateEndpoint.
        The identifier of the Private Endpoint.


        :return: The id of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DistributedDatabasePrivateEndpoint.
        The identifier of the Private Endpoint.


        :param id: The id of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DistributedDatabasePrivateEndpoint.
        Identifier of the compartment in which private endpoint exists.


        :return: The compartment_id of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DistributedDatabasePrivateEndpoint.
        Identifier of the compartment in which private endpoint exists.


        :param compartment_id: The compartment_id of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DistributedDatabasePrivateEndpoint.
        Identifier of the subnet in which private endpoint exists.


        :return: The subnet_id of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DistributedDatabasePrivateEndpoint.
        Identifier of the subnet in which private endpoint exists.


        :param subnet_id: The subnet_id of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this DistributedDatabasePrivateEndpoint.
        Identifier of the VCN in which subnet exists.


        :return: The vcn_id of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DistributedDatabasePrivateEndpoint.
        Identifier of the VCN in which subnet exists.


        :param vcn_id: The vcn_id of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DistributedDatabasePrivateEndpoint.
        DistributedDatabasePrivateEndpoint display name.


        :return: The display_name of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DistributedDatabasePrivateEndpoint.
        DistributedDatabasePrivateEndpoint display name.


        :param display_name: The display_name of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DistributedDatabasePrivateEndpoint.
        DistributedDatabasePrivateEndpoint description.


        :return: The description of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DistributedDatabasePrivateEndpoint.
        DistributedDatabasePrivateEndpoint description.


        :param description: The description of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._description = description

    @property
    def private_ip(self):
        """
        Gets the private_ip of this DistributedDatabasePrivateEndpoint.
        IP address of the Private Endpoint.


        :return: The private_ip of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this DistributedDatabasePrivateEndpoint.
        IP address of the Private Endpoint.


        :param private_ip: The private_ip of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DistributedDatabasePrivateEndpoint.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :return: The nsg_ids of this DistributedDatabasePrivateEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DistributedDatabasePrivateEndpoint.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :param nsg_ids: The nsg_ids of this DistributedDatabasePrivateEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def globally_distributed_databases(self):
        """
        Gets the globally_distributed_databases of this DistributedDatabasePrivateEndpoint.
        The details of the non-deleted Globally distributed databases that consumes the given private endpoint.


        :return: The globally_distributed_databases of this DistributedDatabasePrivateEndpoint.
        :rtype: list[oci.distributed_database.models.DistributedDatabaseAssociatedWithPrivateEndpoint]
        """
        return self._globally_distributed_databases

    @globally_distributed_databases.setter
    def globally_distributed_databases(self, globally_distributed_databases):
        """
        Sets the globally_distributed_databases of this DistributedDatabasePrivateEndpoint.
        The details of the non-deleted Globally distributed databases that consumes the given private endpoint.


        :param globally_distributed_databases: The globally_distributed_databases of this DistributedDatabasePrivateEndpoint.
        :type: list[oci.distributed_database.models.DistributedDatabaseAssociatedWithPrivateEndpoint]
        """
        self._globally_distributed_databases = globally_distributed_databases

    @property
    def globally_distributed_autonomous_databases(self):
        """
        Gets the globally_distributed_autonomous_databases of this DistributedDatabasePrivateEndpoint.
        The details of the non-deleted Globally distributed autonomous databases that consumes the given private endpoint.


        :return: The globally_distributed_autonomous_databases of this DistributedDatabasePrivateEndpoint.
        :rtype: list[oci.distributed_database.models.DistributedAutonomousDatabaseAssociatedWithPrivateEndpoint]
        """
        return self._globally_distributed_autonomous_databases

    @globally_distributed_autonomous_databases.setter
    def globally_distributed_autonomous_databases(self, globally_distributed_autonomous_databases):
        """
        Sets the globally_distributed_autonomous_databases of this DistributedDatabasePrivateEndpoint.
        The details of the non-deleted Globally distributed autonomous databases that consumes the given private endpoint.


        :param globally_distributed_autonomous_databases: The globally_distributed_autonomous_databases of this DistributedDatabasePrivateEndpoint.
        :type: list[oci.distributed_database.models.DistributedAutonomousDatabaseAssociatedWithPrivateEndpoint]
        """
        self._globally_distributed_autonomous_databases = globally_distributed_autonomous_databases

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DistributedDatabasePrivateEndpoint.
        The time the DistributedDatabasePrivateEndpoint was first created. An RFC3339 formatted datetime string


        :return: The time_created of this DistributedDatabasePrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DistributedDatabasePrivateEndpoint.
        The time the DistributedDatabasePrivateEndpoint was first created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this DistributedDatabasePrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DistributedDatabasePrivateEndpoint.
        The time the Private Endpoint was last updated. An RFC3339 formatted datetime string


        :return: The time_updated of this DistributedDatabasePrivateEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DistributedDatabasePrivateEndpoint.
        The time the Private Endpoint was last updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this DistributedDatabasePrivateEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DistributedDatabasePrivateEndpoint.
        Lifecycle states for private endpoint.

        Allowed values for this property are: "ACTIVE", "FAILED", "INACTIVE", "DELETING", "DELETED", "UPDATING", "CREATING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DistributedDatabasePrivateEndpoint.
        Lifecycle states for private endpoint.


        :param lifecycle_state: The lifecycle_state of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        allowed_values = ["ACTIVE", "FAILED", "INACTIVE", "DELETING", "DELETED", "UPDATING", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DistributedDatabasePrivateEndpoint.
        Detailed message for the lifecycle state.


        :return: The lifecycle_details of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DistributedDatabasePrivateEndpoint.
        Detailed message for the lifecycle state.


        :param lifecycle_details: The lifecycle_details of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def proxy_compute_instance_id(self):
        """
        Gets the proxy_compute_instance_id of this DistributedDatabasePrivateEndpoint.
        The identifier of the proxy compute instance.


        :return: The proxy_compute_instance_id of this DistributedDatabasePrivateEndpoint.
        :rtype: str
        """
        return self._proxy_compute_instance_id

    @proxy_compute_instance_id.setter
    def proxy_compute_instance_id(self, proxy_compute_instance_id):
        """
        Sets the proxy_compute_instance_id of this DistributedDatabasePrivateEndpoint.
        The identifier of the proxy compute instance.


        :param proxy_compute_instance_id: The proxy_compute_instance_id of this DistributedDatabasePrivateEndpoint.
        :type: str
        """
        self._proxy_compute_instance_id = proxy_compute_instance_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DistributedDatabasePrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DistributedDatabasePrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DistributedDatabasePrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DistributedDatabasePrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DistributedDatabasePrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DistributedDatabasePrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DistributedDatabasePrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DistributedDatabasePrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DistributedDatabasePrivateEndpoint.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DistributedDatabasePrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DistributedDatabasePrivateEndpoint.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DistributedDatabasePrivateEndpoint.
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
