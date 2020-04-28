# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbSystemDetails(object):
    """
    Details required to create a DB System.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbSystemDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDbSystemDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDbSystemDetails.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateDbSystemDetails.
        :type availability_domain: str

        :param fault_domain:
            The value to assign to the fault_domain property of this CreateDbSystemDetails.
        :type fault_domain: str

        :param configuration_id:
            The value to assign to the configuration_id property of this CreateDbSystemDetails.
        :type configuration_id: str

        :param shape_name:
            The value to assign to the shape_name property of this CreateDbSystemDetails.
        :type shape_name: str

        :param mysql_version:
            The value to assign to the mysql_version property of this CreateDbSystemDetails.
        :type mysql_version: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDbSystemDetails.
        :type subnet_id: str

        :param admin_username:
            The value to assign to the admin_username property of this CreateDbSystemDetails.
        :type admin_username: str

        :param admin_password:
            The value to assign to the admin_password property of this CreateDbSystemDetails.
        :type admin_password: str

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this CreateDbSystemDetails.
        :type data_storage_size_in_gbs: int

        :param hostname_label:
            The value to assign to the hostname_label property of this CreateDbSystemDetails.
        :type hostname_label: str

        :param ip_address:
            The value to assign to the ip_address property of this CreateDbSystemDetails.
        :type ip_address: str

        :param port:
            The value to assign to the port property of this CreateDbSystemDetails.
        :type port: int

        :param port_x:
            The value to assign to the port_x property of this CreateDbSystemDetails.
        :type port_x: int

        :param backup_policy:
            The value to assign to the backup_policy property of this CreateDbSystemDetails.
        :type backup_policy: CreateBackupPolicyDetails

        :param source:
            The value to assign to the source property of this CreateDbSystemDetails.
        :type source: CreateDbSystemSourceDetails

        :param maintenance:
            The value to assign to the maintenance property of this CreateDbSystemDetails.
        :type maintenance: CreateMaintenanceDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDbSystemDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDbSystemDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str',
            'fault_domain': 'str',
            'configuration_id': 'str',
            'shape_name': 'str',
            'mysql_version': 'str',
            'subnet_id': 'str',
            'admin_username': 'str',
            'admin_password': 'str',
            'data_storage_size_in_gbs': 'int',
            'hostname_label': 'str',
            'ip_address': 'str',
            'port': 'int',
            'port_x': 'int',
            'backup_policy': 'CreateBackupPolicyDetails',
            'source': 'CreateDbSystemSourceDetails',
            'maintenance': 'CreateMaintenanceDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'fault_domain': 'faultDomain',
            'configuration_id': 'configurationId',
            'shape_name': 'shapeName',
            'mysql_version': 'mysqlVersion',
            'subnet_id': 'subnetId',
            'admin_username': 'adminUsername',
            'admin_password': 'adminPassword',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'hostname_label': 'hostnameLabel',
            'ip_address': 'ipAddress',
            'port': 'port',
            'port_x': 'portX',
            'backup_policy': 'backupPolicy',
            'source': 'source',
            'maintenance': 'maintenance',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._availability_domain = None
        self._fault_domain = None
        self._configuration_id = None
        self._shape_name = None
        self._mysql_version = None
        self._subnet_id = None
        self._admin_username = None
        self._admin_password = None
        self._data_storage_size_in_gbs = None
        self._hostname_label = None
        self._ip_address = None
        self._port = None
        self._port_x = None
        self._backup_policy = None
        self._source = None
        self._maintenance = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDbSystemDetails.
        The user-friendly name for the DB System. It does not have to be unique.


        :return: The display_name of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDbSystemDetails.
        The user-friendly name for the DB System. It does not have to be unique.


        :param display_name: The display_name of this CreateDbSystemDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDbSystemDetails.
        User-provided data about the DB System.


        :return: The description of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDbSystemDetails.
        User-provided data about the DB System.


        :param description: The description of this CreateDbSystemDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDbSystemDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDbSystemDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateDbSystemDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateDbSystemDetails.
        The Availability Domain where the primary instance should be located.


        :return: The availability_domain of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateDbSystemDetails.
        The Availability Domain where the primary instance should be located.


        :param availability_domain: The availability_domain of this CreateDbSystemDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this CreateDbSystemDetails.
        The name of the Fault Domain the DB System is located in.


        :return: The fault_domain of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this CreateDbSystemDetails.
        The name of the Fault Domain the DB System is located in.


        :param fault_domain: The fault_domain of this CreateDbSystemDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def configuration_id(self):
        """
        **[Required]** Gets the configuration_id of this CreateDbSystemDetails.
        The OCID of the Configuration to be used for this DB System.


        :return: The configuration_id of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """
        Sets the configuration_id of this CreateDbSystemDetails.
        The OCID of the Configuration to be used for this DB System.


        :param configuration_id: The configuration_id of this CreateDbSystemDetails.
        :type: str
        """
        self._configuration_id = configuration_id

    @property
    def shape_name(self):
        """
        **[Required]** Gets the shape_name of this CreateDbSystemDetails.
        The name of the shape. The shape determines the resources allocated
        - CPU cores and memory for VM shapes; CPU cores, memory and storage
        for non-VM (or bare metal) shapes. To get a list of shapes, use the
        :func:`list_shapes` operation.


        :return: The shape_name of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this CreateDbSystemDetails.
        The name of the shape. The shape determines the resources allocated
        - CPU cores and memory for VM shapes; CPU cores, memory and storage
        for non-VM (or bare metal) shapes. To get a list of shapes, use the
        :func:`list_shapes` operation.


        :param shape_name: The shape_name of this CreateDbSystemDetails.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def mysql_version(self):
        """
        Gets the mysql_version of this CreateDbSystemDetails.
        The specific MySQL version identifier.


        :return: The mysql_version of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this CreateDbSystemDetails.
        The specific MySQL version identifier.


        :param mysql_version: The mysql_version of this CreateDbSystemDetails.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateDbSystemDetails.
        The OCID of the subnet the DB System is associated with.


        :return: The subnet_id of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDbSystemDetails.
        The OCID of the subnet the DB System is associated with.


        :param subnet_id: The subnet_id of this CreateDbSystemDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def admin_username(self):
        """
        **[Required]** Gets the admin_username of this CreateDbSystemDetails.
        The username for the administrative user.


        :return: The admin_username of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._admin_username

    @admin_username.setter
    def admin_username(self, admin_username):
        """
        Sets the admin_username of this CreateDbSystemDetails.
        The username for the administrative user.


        :param admin_username: The admin_username of this CreateDbSystemDetails.
        :type: str
        """
        self._admin_username = admin_username

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateDbSystemDetails.
        The password for the administrative user. The password must be
        between 8 and 32 characters long, and must contain at least 1
        numeric character, 1 lowercase character, 1 uppercase character, and
        1 special (nonalphanumeric) character.


        :return: The admin_password of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateDbSystemDetails.
        The password for the administrative user. The password must be
        between 8 and 32 characters long, and must contain at least 1
        numeric character, 1 lowercase character, 1 uppercase character, and
        1 special (nonalphanumeric) character.


        :param admin_password: The admin_password of this CreateDbSystemDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this CreateDbSystemDetails.
        Initial size of the data volume in GBs that will be created and attached.
        Keep in mind that this only specifies the size of the database data volume,
        the log volume for the database will be scaled appropriately with its shape.


        :return: The data_storage_size_in_gbs of this CreateDbSystemDetails.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this CreateDbSystemDetails.
        Initial size of the data volume in GBs that will be created and attached.
        Keep in mind that this only specifies the size of the database data volume,
        the log volume for the database will be scaled appropriately with its shape.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this CreateDbSystemDetails.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def hostname_label(self):
        """
        Gets the hostname_label of this CreateDbSystemDetails.
        The hostname for the primary endpoint of the DB System. Used for DNS.

        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").

        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :return: The hostname_label of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._hostname_label

    @hostname_label.setter
    def hostname_label(self, hostname_label):
        """
        Sets the hostname_label of this CreateDbSystemDetails.
        The hostname for the primary endpoint of the DB System. Used for DNS.

        The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
        (for example, \"dbsystem-1\" in FQDN \"dbsystem-1.subnet123.vcn1.oraclevcn.com\").

        Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.


        :param hostname_label: The hostname_label of this CreateDbSystemDetails.
        :type: str
        """
        self._hostname_label = hostname_label

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreateDbSystemDetails.
        The IP address the DB System is configured to listen on.
        A private IP address of your choice to assign to the primary endpoint of the DB System.
        Must be an available IP address within the subnet's CIDR. If you don't specify a value,
        Oracle automatically assigns a private IP address from the subnet. This should be a
        \"dotted-quad\" style IPv4 address.


        :return: The ip_address of this CreateDbSystemDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateDbSystemDetails.
        The IP address the DB System is configured to listen on.
        A private IP address of your choice to assign to the primary endpoint of the DB System.
        Must be an available IP address within the subnet's CIDR. If you don't specify a value,
        Oracle automatically assigns a private IP address from the subnet. This should be a
        \"dotted-quad\" style IPv4 address.


        :param ip_address: The ip_address of this CreateDbSystemDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def port(self):
        """
        Gets the port of this CreateDbSystemDetails.
        The port for primary endpoint of the DB System to listen on.


        :return: The port of this CreateDbSystemDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateDbSystemDetails.
        The port for primary endpoint of the DB System to listen on.


        :param port: The port of this CreateDbSystemDetails.
        :type: int
        """
        self._port = port

    @property
    def port_x(self):
        """
        Gets the port_x of this CreateDbSystemDetails.
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.


        :return: The port_x of this CreateDbSystemDetails.
        :rtype: int
        """
        return self._port_x

    @port_x.setter
    def port_x(self, port_x):
        """
        Sets the port_x of this CreateDbSystemDetails.
        The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.


        :param port_x: The port_x of this CreateDbSystemDetails.
        :type: int
        """
        self._port_x = port_x

    @property
    def backup_policy(self):
        """
        Gets the backup_policy of this CreateDbSystemDetails.

        :return: The backup_policy of this CreateDbSystemDetails.
        :rtype: CreateBackupPolicyDetails
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        """
        Sets the backup_policy of this CreateDbSystemDetails.

        :param backup_policy: The backup_policy of this CreateDbSystemDetails.
        :type: CreateBackupPolicyDetails
        """
        self._backup_policy = backup_policy

    @property
    def source(self):
        """
        Gets the source of this CreateDbSystemDetails.

        :return: The source of this CreateDbSystemDetails.
        :rtype: CreateDbSystemSourceDetails
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateDbSystemDetails.

        :param source: The source of this CreateDbSystemDetails.
        :type: CreateDbSystemSourceDetails
        """
        self._source = source

    @property
    def maintenance(self):
        """
        Gets the maintenance of this CreateDbSystemDetails.

        :return: The maintenance of this CreateDbSystemDetails.
        :rtype: CreateMaintenanceDetails
        """
        return self._maintenance

    @maintenance.setter
    def maintenance(self, maintenance):
        """
        Sets the maintenance of this CreateDbSystemDetails.

        :param maintenance: The maintenance of this CreateDbSystemDetails.
        :type: CreateMaintenanceDetails
        """
        self._maintenance = maintenance

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDbSystemDetails.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDbSystemDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDbSystemDetails.
        Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDbSystemDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDbSystemDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDbSystemDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDbSystemDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDbSystemDetails.
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
