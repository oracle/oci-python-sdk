# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudSqlDetails(object):
    """
    The information about added Cloud SQL capability
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloudSqlDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this CloudSqlDetails.
        :type shape: str

        :param block_volume_size_in_gbs:
            The value to assign to the block_volume_size_in_gbs property of this CloudSqlDetails.
        :type block_volume_size_in_gbs: int

        :param is_kerberos_mapped_to_database_users:
            The value to assign to the is_kerberos_mapped_to_database_users property of this CloudSqlDetails.
        :type is_kerberos_mapped_to_database_users: bool

        :param ip_address:
            The value to assign to the ip_address property of this CloudSqlDetails.
        :type ip_address: str

        :param kerberos_details:
            The value to assign to the kerberos_details property of this CloudSqlDetails.
        :type kerberos_details: list[KerberosDetails]

        """
        self.swagger_types = {
            'shape': 'str',
            'block_volume_size_in_gbs': 'int',
            'is_kerberos_mapped_to_database_users': 'bool',
            'ip_address': 'str',
            'kerberos_details': 'list[KerberosDetails]'
        }

        self.attribute_map = {
            'shape': 'shape',
            'block_volume_size_in_gbs': 'blockVolumeSizeInGBs',
            'is_kerberos_mapped_to_database_users': 'isKerberosMappedToDatabaseUsers',
            'ip_address': 'ipAddress',
            'kerberos_details': 'kerberosDetails'
        }

        self._shape = None
        self._block_volume_size_in_gbs = None
        self._is_kerberos_mapped_to_database_users = None
        self._ip_address = None
        self._kerberos_details = None

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CloudSqlDetails.
        Shape of the node


        :return: The shape of this CloudSqlDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CloudSqlDetails.
        Shape of the node


        :param shape: The shape of this CloudSqlDetails.
        :type: str
        """
        self._shape = shape

    @property
    def block_volume_size_in_gbs(self):
        """
        Gets the block_volume_size_in_gbs of this CloudSqlDetails.
        The size of block volume in GB that needs to be attached to a given node.
        All the necessary details needed for attachment are managed by service itself.


        :return: The block_volume_size_in_gbs of this CloudSqlDetails.
        :rtype: int
        """
        return self._block_volume_size_in_gbs

    @block_volume_size_in_gbs.setter
    def block_volume_size_in_gbs(self, block_volume_size_in_gbs):
        """
        Sets the block_volume_size_in_gbs of this CloudSqlDetails.
        The size of block volume in GB that needs to be attached to a given node.
        All the necessary details needed for attachment are managed by service itself.


        :param block_volume_size_in_gbs: The block_volume_size_in_gbs of this CloudSqlDetails.
        :type: int
        """
        self._block_volume_size_in_gbs = block_volume_size_in_gbs

    @property
    def is_kerberos_mapped_to_database_users(self):
        """
        Gets the is_kerberos_mapped_to_database_users of this CloudSqlDetails.
        Boolean flag specifying whether or not are Kerberos principals mapped
        to database users.


        :return: The is_kerberos_mapped_to_database_users of this CloudSqlDetails.
        :rtype: bool
        """
        return self._is_kerberos_mapped_to_database_users

    @is_kerberos_mapped_to_database_users.setter
    def is_kerberos_mapped_to_database_users(self, is_kerberos_mapped_to_database_users):
        """
        Sets the is_kerberos_mapped_to_database_users of this CloudSqlDetails.
        Boolean flag specifying whether or not are Kerberos principals mapped
        to database users.


        :param is_kerberos_mapped_to_database_users: The is_kerberos_mapped_to_database_users of this CloudSqlDetails.
        :type: bool
        """
        self._is_kerberos_mapped_to_database_users = is_kerberos_mapped_to_database_users

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this CloudSqlDetails.
        IP address of the Cloud SQL node


        :return: The ip_address of this CloudSqlDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CloudSqlDetails.
        IP address of the Cloud SQL node


        :param ip_address: The ip_address of this CloudSqlDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def kerberos_details(self):
        """
        Gets the kerberos_details of this CloudSqlDetails.
        Details about Kerberos principals


        :return: The kerberos_details of this CloudSqlDetails.
        :rtype: list[KerberosDetails]
        """
        return self._kerberos_details

    @kerberos_details.setter
    def kerberos_details(self, kerberos_details):
        """
        Sets the kerberos_details of this CloudSqlDetails.
        Details about Kerberos principals


        :param kerberos_details: The kerberos_details of this CloudSqlDetails.
        :type: list[KerberosDetails]
        """
        self._kerberos_details = kerberos_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
