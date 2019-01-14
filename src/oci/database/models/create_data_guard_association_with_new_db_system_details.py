# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .create_data_guard_association_details import CreateDataGuardAssociationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataGuardAssociationWithNewDbSystemDetails(CreateDataGuardAssociationDetails):
    """
    The configuration details for creating a Data Guard association to an existing database. A new DbSystem will be launched for standby database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataGuardAssociationWithNewDbSystemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDataGuardAssociationWithNewDbSystemDetails.creation_type` attribute
        of this class is ``NewDbSystem`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

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

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type subnet_id: str

        :param hostname:
            The value to assign to the hostname property of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :type hostname: str

        """
        self.swagger_types = {
            'database_admin_password': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'creation_type': 'str',
            'display_name': 'str',
            'availability_domain': 'str',
            'subnet_id': 'str',
            'hostname': 'str'
        }

        self.attribute_map = {
            'database_admin_password': 'databaseAdminPassword',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'creation_type': 'creationType',
            'display_name': 'displayName',
            'availability_domain': 'availabilityDomain',
            'subnet_id': 'subnetId',
            'hostname': 'hostname'
        }

        self._database_admin_password = None
        self._protection_mode = None
        self._transport_type = None
        self._creation_type = None
        self._display_name = None
        self._availability_domain = None
        self._subnet_id = None
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
    def hostname(self):
        """
        Gets the hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The host name for the DB Node.


        :return: The hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this CreateDataGuardAssociationWithNewDbSystemDetails.
        The host name for the DB Node.


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
