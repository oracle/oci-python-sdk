# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbSystemDetails(object):
    """
    Details required to update a DB System.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDbSystemDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDbSystemDetails.
        :type description: str

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateDbSystemDetails.
        :type subnet_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this UpdateDbSystemDetails.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this UpdateDbSystemDetails.
        :type fault_domain: str

        :param shape_name:
            The value to assign to the shape_name property of this UpdateDbSystemDetails.
        :type shape_name: str

        :param mysql_version:
            The value to assign to the mysql_version property of this UpdateDbSystemDetails.
        :type mysql_version: str

        :param configuration_id:
            The value to assign to the configuration_id property of this UpdateDbSystemDetails.
        :type configuration_id: str

        :param admin_username:
            The value to assign to the admin_username property of this UpdateDbSystemDetails.
        :type admin_username: str

        :param admin_password:
            The value to assign to the admin_password property of this UpdateDbSystemDetails.
        :type admin_password: str

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this UpdateDbSystemDetails.
        :type data_storage_size_in_gbs: int

        :param hostname_label:
            The value to assign to the hostname_label property of this UpdateDbSystemDetails.
        :type hostname_label: str

        :param ip_address:
            The value to assign to the ip_address property of this UpdateDbSystemDetails.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this UpdateDbSystemDetails.
        :type port: int

        :param port_x:
            The value to assign to the port_x property of this UpdateDbSystemDetails.
        :type port_x: int

        :param backup_policy:
            The value to assign to the backup_policy property of this UpdateDbSystemDetails.
        :type backup_policy: UpdateBackupPolicyDetails

        :param maintenance:
            The value to assign to the maintenance property of this UpdateDbSystemDetails.
        :type maintenance: UpdateMaintenanceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDbSystemDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDbSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'subnet_id': 'str',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'shape_name': 'str',
            'mysql_version': 'str',
            'configuration_id': 'str',
            'admin_username': 'str',
            'admin_password': 'str',
            'data_storage_size_in_gbs': 'int',
            'hostname_label': 'str',
            'ip_address': 'str',
            'port': 'int',
            'port_x': 'int',
            'backup_policy': 'UpdateBackupPolicyDetails',
            'maintenance': 'UpdateMaintenanceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'subnet_id': 'subnetId',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'shape_name': 'shapeName',
            'mysql_version': 'mysqlVersion',
            'configuration_id': 'configurationId',
            'admin_username': 'adminUsername',
            'admin_password': 'adminPassword',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'hostname_label': 'hostnameLabel',
            'ip_address': 'ipAddress',
            'port': 'port',
            'port_x': 'portX',
            'backup_policy': 'backupPolicy',
            'maintenance': 'maintenance',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._subnet_id = None
        self._availability_domain = None
        self._fault_domain = None
        self._shape_name = None
        self._mysql_version = None
        self._configuration_id = None
        self._admin_username = None
        self._admin_password = None
        self._data_storage_size_in_gbs = None
        self._hostname_label = None
        self._ip_address = None
        self._port = None
        self._port_x = None
        self._backup_policy = None
        self._maintenance = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDbSystemDetails.
        The user-friendly name for the DB System. It does not have to be unique.


        :return: The display_name of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDbSystemDetails.
        The user-friendly name for the DB System. It does not have to be unique.


        :param display_name: The display_name of this UpdateDbSystemDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateDbSystemDetails.
        User-provided data about the DB System.


        :return: The description of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDbSystemDetails.
        User-provided data about the DB System.


        :param description: The description of this UpdateDbSystemDetails.
        :type: str
        """
        self._description = description

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this UpdateDbSystemDetails.
        The OCID of the subnet the DB System is associated with.


        :return: The subnet_id of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this UpdateDbSystemDetails.
        The OCID of the subnet the DB System is associated with.


        :param subnet_id: The subnet_id of this UpdateDbSystemDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this UpdateDbSystemDetails.
        The Availability Domain where the primary instance should be located.


        :return: The availability_domain of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this UpdateDbSystemDetails.
        The Availability Domain where the primary instance should be located.


        :param availability_domain: The availability_domain of this UpdateDbSystemDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this UpdateDbSystemDetails.
        The name of the Fault Domain the DB System is located in.


        :return: The fault_domain of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this UpdateDbSystemDetails.
        The name of the Fault Domain the DB System is located in.


        :param fault_domain: The fault_domain of this UpdateDbSystemDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def shape_name(self):
        """
        Gets the shape_name of this UpdateDbSystemDetails.
        The shape of the DB System. The shape determines resources
        allocated to the DB System - CPU cores and memory for VM
        shapes; CPU cores, memory and storage for non-VM (or bare metal)
        shapes. To get a list of shapes, use the
        :func:`list_shapes`
        operation.

        Changes in Shape will result in a downtime as the MySQL DB System is
        migrated to the new Compute instance.


        :return: The shape_name of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this UpdateDbSystemDetails.
        The shape of the DB System. The shape determines resources
        allocated to the DB System - CPU cores and memory for VM
        shapes; CPU cores, memory and storage for non-VM (or bare metal)
        shapes. To get a list of shapes, use the
        :func:`list_shapes`
        operation.

        Changes in Shape will result in a downtime as the MySQL DB System is
        migrated to the new Compute instance.


        :param shape_name: The shape_name of this UpdateDbSystemDetails.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def mysql_version(self):
        """
        Gets the mysql_version of this UpdateDbSystemDetails.
        The specific MySQL version identifier.


        :return: The mysql_version of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this UpdateDbSystemDetails.
        The specific MySQL version identifier.


        :param mysql_version: The mysql_version of this UpdateDbSystemDetails.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def configuration_id(self):
        """
        Gets the configuration_id of this UpdateDbSystemDetails.
        The OCID of the Configuration to be used for Instances in this DB System.


        :return: The configuration_id of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """
        Sets the configuration_id of this UpdateDbSystemDetails.
        The OCID of the Configuration to be used for Instances in this DB System.


        :param configuration_id: The configuration_id of this UpdateDbSystemDetails.
        :type: str
        """
        self._configuration_id = configuration_id

    @property
    def admin_username(self):
        """
        Gets the admin_username of this UpdateDbSystemDetails.
        The username for the administrative user for the MySQL Instance.


        :return: The admin_username of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._admin_username

    @admin_username.setter
    def admin_username(self, admin_username):
        """
        Sets the admin_username of this UpdateDbSystemDetails.
        The username for the administrative user for the MySQL Instance.


        :param admin_username: The admin_username of this UpdateDbSystemDetails.
        :type: str
        """
        self._admin_username = admin_username

    @property
    def admin_password(self):
        """
        Gets the admin_password of this UpdateDbSystemDetails.
        The password for the administrative user. The password must be
        between 8 and 32 characters long, and must contain at least 1
        numeric character, 1 lowercase character, 1 uppercase character, and
        1 special (nonalphanumeric) character.


        :return: The admin_password of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this UpdateDbSystemDetails.
        The password for the administrative user. The password must be
        between 8 and 32 characters long, and must contain at least 1
        numeric character, 1 lowercase character, 1 uppercase character, and
        1 special (nonalphanumeric) character.


        :param admin_password: The admin_password of this UpdateDbSystemDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        New size of the data volume in GBs that will be created and attached.

        Increases in data storage size will happen asynchronously and will require DB System downtime.

        Decreases in data storage size are not supported.


        :return: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this UpdateDbSystemDetails.
        New size of the data volume in GBs that will be created and attached.

        Increases in data storage size will happen asynchronously and will require DB System downtime.

        Decreases in data storage size are not supported.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this UpdateDbSystemDetails.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this UpdateDbSystemDetails.
        The hostname for the primary endpoint of the DB System. Used for DNS.
        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").
        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :return: The hostname_label of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this UpdateDbSystemDetails.
        The hostname for the primary endpoint of the DB System. Used for DNS.
        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").
        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :param hostname_label: The hostname_label of this UpdateDbSystemDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def ip_address(self):
        """
        Gets the ip_address of this UpdateDbSystemDetails.
        The IP address the DB System should be configured to listen on the provided subnet.
        It must be a free private IP address within the subnet's CIDR. If you don't specify a
        value, Oracle automatically assigns a private IP address from the subnet. This should
        be a \"dotted-quad\" style IPv4 address.


        :return: The ip_address of this UpdateDbSystemDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this UpdateDbSystemDetails.
        The IP address the DB System should be configured to listen on the provided subnet.
        It must be a free private IP address within the subnet's CIDR. If you don't specify a
        value, Oracle automatically assigns a private IP address from the subnet. This should
        be a \"dotted-quad\" style IPv4 address.


        :param ip_address: The ip_address of this UpdateDbSystemDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        Gets the port of this UpdateDbSystemDetails.
        The port for primary endpoint of the DB System to listen on.


        :return: The port of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateDbSystemDetails.
        The port for primary endpoint of the DB System to listen on.


        :param port: The port of this UpdateDbSystemDetails.
        :type: int
        """
        self._port = port

    @property
    def port_x(self):
        """
        Gets the port_x of this UpdateDbSystemDetails.
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.


        :return: The port_x of this UpdateDbSystemDetails.
        :rtype: int
        """
        return self._port_x

    @port_x.setter
    def port_x(self, port_x):
        """
        Sets the port_x of this UpdateDbSystemDetails.
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.


        :param port_x: The port_x of this UpdateDbSystemDetails.
        :type: int
        """
        self._port_x = port_x

    @property
    def backup_policy(self):
        """
        Gets the backup_policy of this UpdateDbSystemDetails.

        :return: The backup_policy of this UpdateDbSystemDetails.
        :rtype: UpdateBackupPolicyDetails
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        """
        Sets the backup_policy of this UpdateDbSystemDetails.

        :param backup_policy: The backup_policy of this UpdateDbSystemDetails.
        :type: UpdateBackupPolicyDetails
        """
        self._backup_policy = backup_policy

    @property
    def maintenance(self):
        """
        Gets the maintenance of this UpdateDbSystemDetails.

        :return: The maintenance of this UpdateDbSystemDetails.
        :rtype: UpdateMaintenanceDetails
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """
        Sets the maintenance of this UpdateDbSystemDetails.

        :param maintenance: The maintenance of this UpdateDbSystemDetails.
        :type: UpdateMaintenanceDetails
        """
        self._maintenance = maintenance

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateDbSystemDetails.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateDbSystemDetails.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateDbSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateDbSystemDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateDbSystemDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateDbSystemDetails.
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
