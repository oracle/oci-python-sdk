# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousExadataInfrastructure(object):
    """
    AutonomousExadataInfrastructure model.
    """

    #: A constant which can be used with the lifecycle_state property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the license_model property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a AutonomousExadataInfrastructure.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousExadataInfrastructure object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousExadataInfrastructure.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousExadataInfrastructure.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AutonomousExadataInfrastructure.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this AutonomousExadataInfrastructure.
        :type availability_domain: str

        :param subnet_id:
            The value to assign to the subnet_id property of this AutonomousExadataInfrastructure.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this AutonomousExadataInfrastructure.
        :type nsg_ids: list[str]

        :param shape:
            The value to assign to the shape property of this AutonomousExadataInfrastructure.
        :type shape: str

        :param hostname:
            The value to assign to the hostname property of this AutonomousExadataInfrastructure.
        :type hostname: str

        :param domain:
            The value to assign to the domain property of this AutonomousExadataInfrastructure.
        :type domain: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousExadataInfrastructure.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousExadataInfrastructure.
        :type lifecycle_details: str

        :param license_model:
            The value to assign to the license_model property of this AutonomousExadataInfrastructure.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param time_created:
            The value to assign to the time_created property of this AutonomousExadataInfrastructure.
        :type time_created: datetime

        :param maintenance_window:
            The value to assign to the maintenance_window property of this AutonomousExadataInfrastructure.
        :type maintenance_window: oci.database.models.MaintenanceWindow

        :param last_maintenance_run_id:
            The value to assign to the last_maintenance_run_id property of this AutonomousExadataInfrastructure.
        :type last_maintenance_run_id: str

        :param next_maintenance_run_id:
            The value to assign to the next_maintenance_run_id property of this AutonomousExadataInfrastructure.
        :type next_maintenance_run_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousExadataInfrastructure.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousExadataInfrastructure.
        :type defined_tags: dict(str, dict(str, object))

        :param scan_dns_name:
            The value to assign to the scan_dns_name property of this AutonomousExadataInfrastructure.
        :type scan_dns_name: str

        :param zone_id:
            The value to assign to the zone_id property of this AutonomousExadataInfrastructure.
        :type zone_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'shape': 'str',
            'hostname': 'str',
            'domain': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'license_model': 'str',
            'time_created': 'datetime',
            'maintenance_window': 'MaintenanceWindow',
            'last_maintenance_run_id': 'str',
            'next_maintenance_run_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'scan_dns_name': 'str',
            'zone_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'shape': 'shape',
            'hostname': 'hostname',
            'domain': 'domain',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'license_model': 'licenseModel',
            'time_created': 'timeCreated',
            'maintenance_window': 'maintenanceWindow',
            'last_maintenance_run_id': 'lastMaintenanceRunId',
            'next_maintenance_run_id': 'nextMaintenanceRunId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'scan_dns_name': 'scanDnsName',
            'zone_id': 'zoneId'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._availability_domain = None
        self._subnet_id = None
        self._nsg_ids = None
        self._shape = None
        self._hostname = None
        self._domain = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._license_model = None
        self._time_created = None
        self._maintenance_window = None
        self._last_maintenance_run_id = None
        self._next_maintenance_run_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._scan_dns_name = None
        self._zone_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousExadataInfrastructure.
        The OCID of the Autonomous Exadata Infrastructure.


        :return: The id of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousExadataInfrastructure.
        The OCID of the Autonomous Exadata Infrastructure.


        :param id: The id of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousExadataInfrastructure.
        The OCID of the compartment.


        :return: The compartment_id of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousExadataInfrastructure.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutonomousExadataInfrastructure.
        The user-friendly name for the Autonomous Exadata Infrastructure.


        :return: The display_name of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousExadataInfrastructure.
        The user-friendly name for the Autonomous Exadata Infrastructure.


        :param display_name: The display_name of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._display_name = display_name

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this AutonomousExadataInfrastructure.
        The name of the availability domain that the Autonomous Exadata Infrastructure is located in.


        :return: The availability_domain of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this AutonomousExadataInfrastructure.
        The name of the availability domain that the Autonomous Exadata Infrastructure is located in.


        :param availability_domain: The availability_domain of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this AutonomousExadataInfrastructure.
        The OCID of the subnet the Autonomous Exadata Infrastructure is associated with.

        **Subnet Restrictions:**
        - For Autonomous Databases with Autonomous Exadata Infrastructure, do not use a subnet that overlaps with 192.168.128.0/20

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :return: The subnet_id of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this AutonomousExadataInfrastructure.
        The OCID of the subnet the Autonomous Exadata Infrastructure is associated with.

        **Subnet Restrictions:**
        - For Autonomous Databases with Autonomous Exadata Infrastructure, do not use a subnet that overlaps with 192.168.128.0/20

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :param subnet_id: The subnet_id of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this AutonomousExadataInfrastructure.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this AutonomousExadataInfrastructure.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this AutonomousExadataInfrastructure.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this AutonomousExadataInfrastructure.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this AutonomousExadataInfrastructure.
        The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU cores, memory and storage).


        :return: The shape of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this AutonomousExadataInfrastructure.
        The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU cores, memory and storage).


        :param shape: The shape of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._shape = shape

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this AutonomousExadataInfrastructure.
        The host name for the Autonomous Exadata Infrastructure node.


        :return: The hostname of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this AutonomousExadataInfrastructure.
        The host name for the Autonomous Exadata Infrastructure node.


        :param hostname: The hostname of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._hostname = hostname

    @property
    def domain(self):
        """
        **[Required]** Gets the domain of this AutonomousExadataInfrastructure.
        The domain name for the Autonomous Exadata Infrastructure.


        :return: The domain of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this AutonomousExadataInfrastructure.
        The domain name for the Autonomous Exadata Infrastructure.


        :param domain: The domain of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._domain = domain

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousExadataInfrastructure.
        The current lifecycle state of the Autonomous Exadata Infrastructure.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousExadataInfrastructure.
        The current lifecycle state of the Autonomous Exadata Infrastructure.


        :param lifecycle_state: The lifecycle_state of this AutonomousExadataInfrastructure.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", "MAINTENANCE_IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousExadataInfrastructure.
        Additional information about the current lifecycle state of the Autonomous Exadata Infrastructure.


        :return: The lifecycle_details of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousExadataInfrastructure.
        Additional information about the current lifecycle state of the Autonomous Exadata Infrastructure.


        :param lifecycle_details: The lifecycle_details of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def license_model(self):
        """
        Gets the license_model of this AutonomousExadataInfrastructure.
        The Oracle license model that applies to all databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this AutonomousExadataInfrastructure.
        The Oracle license model that applies to all databases in the Autonomous Exadata Infrastructure. The default is BRING_YOUR_OWN_LICENSE.


        :param license_model: The license_model of this AutonomousExadataInfrastructure.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousExadataInfrastructure.
        The date and time the Autonomous Exadata Infrastructure was created.


        :return: The time_created of this AutonomousExadataInfrastructure.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousExadataInfrastructure.
        The date and time the Autonomous Exadata Infrastructure was created.


        :param time_created: The time_created of this AutonomousExadataInfrastructure.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def maintenance_window(self):
        """
        **[Required]** Gets the maintenance_window of this AutonomousExadataInfrastructure.

        :return: The maintenance_window of this AutonomousExadataInfrastructure.
        :rtype: oci.database.models.MaintenanceWindow
        """
        return self._maintenance_window

    @maintenance_window.setter
    def maintenance_window(self, maintenance_window):
        """
        Sets the maintenance_window of this AutonomousExadataInfrastructure.

        :param maintenance_window: The maintenance_window of this AutonomousExadataInfrastructure.
        :type: oci.database.models.MaintenanceWindow
        """
        self._maintenance_window = maintenance_window

    @property
    def last_maintenance_run_id(self):
        """
        Gets the last_maintenance_run_id of this AutonomousExadataInfrastructure.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The last_maintenance_run_id of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._last_maintenance_run_id

    @last_maintenance_run_id.setter
    def last_maintenance_run_id(self, last_maintenance_run_id):
        """
        Sets the last_maintenance_run_id of this AutonomousExadataInfrastructure.
        The `OCID`__ of the last maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param last_maintenance_run_id: The last_maintenance_run_id of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._last_maintenance_run_id = last_maintenance_run_id

    @property
    def next_maintenance_run_id(self):
        """
        Gets the next_maintenance_run_id of this AutonomousExadataInfrastructure.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The next_maintenance_run_id of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._next_maintenance_run_id

    @next_maintenance_run_id.setter
    def next_maintenance_run_id(self, next_maintenance_run_id):
        """
        Sets the next_maintenance_run_id of this AutonomousExadataInfrastructure.
        The `OCID`__ of the next maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param next_maintenance_run_id: The next_maintenance_run_id of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._next_maintenance_run_id = next_maintenance_run_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousExadataInfrastructure.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousExadataInfrastructure.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousExadataInfrastructure.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousExadataInfrastructure.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousExadataInfrastructure.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousExadataInfrastructure.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def scan_dns_name(self):
        """
        Gets the scan_dns_name of this AutonomousExadataInfrastructure.
        The FQDN of the DNS record for the SCAN IP addresses that are associated with the Autonomous Exadata Infrastructure.


        :return: The scan_dns_name of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._scan_dns_name

    @scan_dns_name.setter
    def scan_dns_name(self, scan_dns_name):
        """
        Sets the scan_dns_name of this AutonomousExadataInfrastructure.
        The FQDN of the DNS record for the SCAN IP addresses that are associated with the Autonomous Exadata Infrastructure.


        :param scan_dns_name: The scan_dns_name of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._scan_dns_name = scan_dns_name

    @property
    def zone_id(self):
        """
        Gets the zone_id of this AutonomousExadataInfrastructure.
        The OCID of the zone the Autonomous Exadata Infrastructure is associated with.


        :return: The zone_id of this AutonomousExadataInfrastructure.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this AutonomousExadataInfrastructure.
        The OCID of the zone the Autonomous Exadata Infrastructure is associated with.


        :param zone_id: The zone_id of this AutonomousExadataInfrastructure.
        :type: str
        """
        self._zone_id = zone_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
