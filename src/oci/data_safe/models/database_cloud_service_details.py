# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_details import DatabaseDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseCloudServiceDetails(DatabaseDetails):
    """
    The details of the Oracle Database Cloud Service to be registered as a target database in Data Safe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseCloudServiceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.DatabaseCloudServiceDetails.database_type` attribute
        of this class is ``DATABASE_CLOUD_SERVICE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_type:
            The value to assign to the database_type property of this DatabaseCloudServiceDetails.
            Allowed values for this property are: "DATABASE_CLOUD_SERVICE", "AUTONOMOUS_DATABASE", "INSTALLED_DATABASE"
        :type database_type: str

        :param infrastructure_type:
            The value to assign to the infrastructure_type property of this DatabaseCloudServiceDetails.
            Allowed values for this property are: "ORACLE_CLOUD", "CLOUD_AT_CUSTOMER", "ON_PREMISES", "NON_ORACLE_CLOUD"
        :type infrastructure_type: str

        :param vm_cluster_id:
            The value to assign to the vm_cluster_id property of this DatabaseCloudServiceDetails.
        :type vm_cluster_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this DatabaseCloudServiceDetails.
        :type db_system_id: str

        :param service_name:
            The value to assign to the service_name property of this DatabaseCloudServiceDetails.
        :type service_name: str

        """
        self.swagger_types = {
            'database_type': 'str',
            'infrastructure_type': 'str',
            'vm_cluster_id': 'str',
            'db_system_id': 'str',
            'service_name': 'str'
        }

        self.attribute_map = {
            'database_type': 'databaseType',
            'infrastructure_type': 'infrastructureType',
            'vm_cluster_id': 'vmClusterId',
            'db_system_id': 'dbSystemId',
            'service_name': 'serviceName'
        }

        self._database_type = None
        self._infrastructure_type = None
        self._vm_cluster_id = None
        self._db_system_id = None
        self._service_name = None
        self._database_type = 'DATABASE_CLOUD_SERVICE'

    @property
    def vm_cluster_id(self):
        """
        Gets the vm_cluster_id of this DatabaseCloudServiceDetails.
        The OCID of the VM cluster in which the database is running.


        :return: The vm_cluster_id of this DatabaseCloudServiceDetails.
        :rtype: str
        """
        return self._vm_cluster_id

    @vm_cluster_id.setter
    def vm_cluster_id(self, vm_cluster_id):
        """
        Sets the vm_cluster_id of this DatabaseCloudServiceDetails.
        The OCID of the VM cluster in which the database is running.


        :param vm_cluster_id: The vm_cluster_id of this DatabaseCloudServiceDetails.
        :type: str
        """
        self._vm_cluster_id = vm_cluster_id

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this DatabaseCloudServiceDetails.
        The OCID of the cloud database system registered as a target database in Data Safe.


        :return: The db_system_id of this DatabaseCloudServiceDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DatabaseCloudServiceDetails.
        The OCID of the cloud database system registered as a target database in Data Safe.


        :param db_system_id: The db_system_id of this DatabaseCloudServiceDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def service_name(self):
        """
        Gets the service_name of this DatabaseCloudServiceDetails.
        The database service name.


        :return: The service_name of this DatabaseCloudServiceDetails.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this DatabaseCloudServiceDetails.
        The database service name.


        :param service_name: The service_name of this DatabaseCloudServiceDetails.
        :type: str
        """
        self._service_name = service_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
