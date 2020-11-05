# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataGuardAssociationWithNewDbSystemDetails(CreateDataGuardAssociationDetails):
    """
    The configuration details for creating a Data Guard association for a virtual machine DB system database. For this type of DB system database, the `creationType` should be `NewDbSystem`. A new DB system will be launched to create the standby database.

    To create a Data Guard association for a database in a bare metal or Exadata DB system, use the :func:`create_data_guard_association_to_existing_db_system_details` subtype instead.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataGuardAssociationWithNewDbSystemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDataGuardAssociationWithNewDbSystemDetails.creation_type` attribute
        of this class is ``NewDbSystem`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type database_software_image_id: str

        :param database_admin_password:
            The value to assign to the database_admin_password property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type database_admin_password: str

        :param protection_mode:
            The value to assign to the protection_mode property of this CreateDataGuardAssociationWithNewDbSystemDetails.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"
        :type protection_mode: str

        :param transport_type:
            The value to assign to the transport_type property of this CreateDataGuardAssociationWithNewDbSystemDetails.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC"
        :type transport_type: str

        :param creation_type:
            The value to assign to the creation_type property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type creation_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type display_name: str

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type availability_domain: str

        :param shape:
            The value to assign to the shape property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type shape: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type nsg_ids: list[str]

        :param backup_network_nsg_ids:
            The value to assign to the backup_network_nsg_ids property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type backup_network_nsg_ids: list[str]

        :param hostname:
            The value to assign to the hostname property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type hostname: str

        """
        self.swagger_types = {
            'database_software_image_id': 'str',
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'creation_type': 'str',
            'display_name': 'str',
            'availability_domain': 'str',
            'shape': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'backup_network_nsg_ids': 'list[str]',
            'hostname': 'str'
        }

        self.attribute_map = {
            'database_software_image_id': 'databaseSoftwareImageId',
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'creation_type': 'creationType',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'shape': 'shape',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'backup_network_nsg_ids': 'backupNetworkNsgIds',
            'hostname': 'hostname'
        }

        self._database_software_image_id = None
        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._creation_type = None
        self._display_name = None
        self._availability_domain = None
        self._shape = None
        self._subnet_id = None
        self._nsg_ids = None
        self._backup_network_nsg_ids = None
        self._hostname = None
        self._creation_type = 'NewDbSystem'

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.


        :return: The display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The user-friendly name of the DB system that will contain the the standby database. The display name does not have to be unique.


        :param display_name: The display_name of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The name of the availability domain that the standby database DB system will be located in. For example- \"Uocm:PHX-AD-1\".


        :return: The availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The name of the availability domain that the standby database DB system will be located in. For example- \"Uocm:PHX-AD-1\".


        :param availability_domain: The availability_domain of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def shape(self):
        """
        Gets the shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores and the amount of memory available for the DB system.
        Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system.

        To get a list of all shapes, use the :func:`list_db_system_shapes` operation.


        :return: The shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The virtual machine DB system shape to launch for the standby database in the Data Guard association. The shape determines the number of CPU cores and the amount of memory available for the DB system.
        Only virtual machine shapes are valid options. If you do not supply this parameter, the default shape is the shape of the primary DB system.

        To get a list of all shapes, use the :func:`list_db_system_shapes` operation.


        :param shape: The shape of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._shape = shape

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The OCID of the subnet the DB system is associated with.
        **Subnet Restrictions:**
        - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :return: The subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The OCID of the subnet the DB system is associated with.
        **Subnet Restrictions:**
        - For 1- and 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.16.16/28

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and backup subnet.


        :param subnet_id: The subnet_id of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def backup_network_nsg_ids(self):
        """
        Gets the backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: list[str]
        """
        return self._backup_network_nsg_ids

    @backup_network_nsg_ids.setter
    def backup_network_nsg_ids(self, backup_network_nsg_ids):
        """
        Sets the backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        A list of the `OCIDs`__ of the network security groups (NSGs) that the backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__. Applicable only to Exadata systems.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param backup_network_nsg_ids: The backup_network_nsg_ids of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: list[str]
        """
        self._backup_network_nsg_ids = backup_network_nsg_ids

    @property
    def hostname(self):
        """
        Gets the hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The hostname for the DB node.


        :return: The hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The hostname for the DB node.


        :param hostname: The hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type: str
        """
        self._hostname = hostname

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
