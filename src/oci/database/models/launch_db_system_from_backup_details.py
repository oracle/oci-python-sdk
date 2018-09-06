# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .launch_db_system_base import LaunchDbSystemBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchDbSystemFromBackupDetails(LaunchDbSystemBase):
    """
    LaunchDbSystemFromBackupDetails model.
    """

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "STANDARD_EDITION"
    DATABASE_EDITION_STANDARD_EDITION = "STANDARD_EDITION"

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "ENTERPRISE_EDITION"
    DATABASE_EDITION_ENTERPRISE_EDITION = "ENTERPRISE_EDITION"

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "ENTERPRISE_EDITION_HIGH_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_HIGH_PERFORMANCE = "ENTERPRISE_EDITION_HIGH_PERFORMANCE"

    #: A constant which can be used with the database_edition property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
    DATABASE_EDITION_ENTERPRISE_EDITION_EXTREME_PERFORMANCE = "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"

    #: A constant which can be used with the disk_redundancy property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "HIGH"
    DISK_REDUNDANCY_HIGH = "HIGH"

    #: A constant which can be used with the disk_redundancy property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "NORMAL"
    DISK_REDUNDANCY_NORMAL = "NORMAL"

    #: A constant which can be used with the license_model property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a LaunchDbSystemFromBackupDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchDbSystemFromBackupDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.LaunchDbSystemFromBackupDetails.source` attribute
        of this class is ``DB_BACKUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this LaunchDbSystemFromBackupDetails.
        :type availability_domain: str

        :param backup_subnet_id:
            The value to assign to the backup_subnet_id property of this LaunchDbSystemFromBackupDetails.
        :type backup_subnet_id: str

        :param cluster_name:
            The value to assign to the cluster_name property of this LaunchDbSystemFromBackupDetails.
        :type cluster_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LaunchDbSystemFromBackupDetails.
        :type compartment_id: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this LaunchDbSystemFromBackupDetails.
        :type cpu_core_count: int

        :param data_storage_percentage:
            The value to assign to the data_storage_percentage property of this LaunchDbSystemFromBackupDetails.
        :type data_storage_percentage: int

        :param defined_tags:
            The value to assign to the defined_tags property of this LaunchDbSystemFromBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this LaunchDbSystemFromBackupDetails.
        :type display_name: str

        :param domain:
            The value to assign to the domain property of this LaunchDbSystemFromBackupDetails.
        :type domain: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LaunchDbSystemFromBackupDetails.
        :type freeform_tags: dict(str, str)

        :param hostname:
            The value to assign to the hostname property of this LaunchDbSystemFromBackupDetails.
        :type hostname: str

        :param initial_data_storage_size_in_gb:
            The value to assign to the initial_data_storage_size_in_gb property of this LaunchDbSystemFromBackupDetails.
        :type initial_data_storage_size_in_gb: int

        :param node_count:
            The value to assign to the node_count property of this LaunchDbSystemFromBackupDetails.
        :type node_count: int

        :param shape:
            The value to assign to the shape property of this LaunchDbSystemFromBackupDetails.
        :type shape: str

        :param source:
            The value to assign to the source property of this LaunchDbSystemFromBackupDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP"
        :type source: str

        :param ssh_public_keys:
            The value to assign to the ssh_public_keys property of this LaunchDbSystemFromBackupDetails.
        :type ssh_public_keys: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this LaunchDbSystemFromBackupDetails.
        :type subnet_id: str

        :param database_edition:
            The value to assign to the database_edition property of this LaunchDbSystemFromBackupDetails.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
        :type database_edition: str

        :param db_home:
            The value to assign to the db_home property of this LaunchDbSystemFromBackupDetails.
        :type db_home: CreateDbHomeFromBackupDetails

        :param disk_redundancy:
            The value to assign to the disk_redundancy property of this LaunchDbSystemFromBackupDetails.
            Allowed values for this property are: "HIGH", "NORMAL"
        :type disk_redundancy: str

        :param license_model:
            The value to assign to the license_model property of this LaunchDbSystemFromBackupDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'backup_subnet_id': 'str',
            'cluster_name': 'str',
            'compartment_id': 'str',
            'cpu_core_count': 'int',
            'data_storage_percentage': 'int',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'domain': 'str',
            'freeform_tags': 'dict(str, str)',
            'hostname': 'str',
            'initial_data_storage_size_in_gb': 'int',
            'node_count': 'int',
            'shape': 'str',
            'source': 'str',
            'ssh_public_keys': 'list[str]',
            'subnet_id': 'str',
            'database_edition': 'str',
            'db_home': 'CreateDbHomeFromBackupDetails',
            'disk_redundancy': 'str',
            'license_model': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'backup_subnet_id': 'backupSubnetId',
            'cluster_name': 'clusterName',
            'compartment_id': 'compartmentId',
            'cpu_core_count': 'cpuCoreCount',
            'data_storage_percentage': 'dataStoragePercentage',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'domain': 'domain',
            'freeform_tags': 'freeformTags',
            'hostname': 'hostname',
            'initial_data_storage_size_in_gb': 'initialDataStorageSizeInGB',
            'node_count': 'nodeCount',
            'shape': 'shape',
            'source': 'source',
            'ssh_public_keys': 'sshPublicKeys',
            'subnet_id': 'subnetId',
            'database_edition': 'databaseEdition',
            'db_home': 'dbHome',
            'disk_redundancy': 'diskRedundancy',
            'license_model': 'licenseModel'
        }

        self._availability_domain = None
        self._backup_subnet_id = None
        self._cluster_name = None
        self._compartment_id = None
        self._cpu_core_count = None
        self._data_storage_percentage = None
        self._defined_tags = None
        self._display_name = None
        self._domain = None
        self._freeform_tags = None
        self._hostname = None
        self._initial_data_storage_size_in_gb = None
        self._node_count = None
        self._shape = None
        self._source = None
        self._ssh_public_keys = None
        self._subnet_id = None
        self._database_edition = None
        self._db_home = None
        self._disk_redundancy = None
        self._license_model = None
        self._source = 'DB_BACKUP'

    @property
    def database_edition(self):
        """
        **[Required]** Gets the database_edition of this LaunchDbSystemFromBackupDetails.
        The Oracle Database Edition that applies to all the databases on the DB system.
        Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"


        :return: The database_edition of this LaunchDbSystemFromBackupDetails.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this LaunchDbSystemFromBackupDetails.
        The Oracle Database Edition that applies to all the databases on the DB system.
        Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.


        :param database_edition: The database_edition of this LaunchDbSystemFromBackupDetails.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_HIGH_PERFORMANCE", "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(database_edition, allowed_values):
            raise ValueError(
                "Invalid value for `database_edition`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._database_edition = database_edition

    @property
    def db_home(self):
        """
        **[Required]** Gets the db_home of this LaunchDbSystemFromBackupDetails.

        :return: The db_home of this LaunchDbSystemFromBackupDetails.
        :rtype: CreateDbHomeFromBackupDetails
        """
        return self._db_home

    @db_home.setter
    def db_home(self, db_home):
        """
        Sets the db_home of this LaunchDbSystemFromBackupDetails.

        :param db_home: The db_home of this LaunchDbSystemFromBackupDetails.
        :type: CreateDbHomeFromBackupDetails
        """
        self._db_home = db_home

    @property
    def disk_redundancy(self):
        """
        Gets the disk_redundancy of this LaunchDbSystemFromBackupDetails.
        The type of redundancy configured for the DB system.
        NORMAL 2-way redundancy, recommended for test and development systems.
        HIGH is 3-way redundancy, recommended for production systems.

        Allowed values for this property are: "HIGH", "NORMAL"


        :return: The disk_redundancy of this LaunchDbSystemFromBackupDetails.
        :rtype: str
        """
        return self._disk_redundancy

    @disk_redundancy.setter
    def disk_redundancy(self, disk_redundancy):
        """
        Sets the disk_redundancy of this LaunchDbSystemFromBackupDetails.
        The type of redundancy configured for the DB system.
        NORMAL 2-way redundancy, recommended for test and development systems.
        HIGH is 3-way redundancy, recommended for production systems.


        :param disk_redundancy: The disk_redundancy of this LaunchDbSystemFromBackupDetails.
        :type: str
        """
        allowed_values = ["HIGH", "NORMAL"]
        if not value_allowed_none_or_none_sentinel(disk_redundancy, allowed_values):
            raise ValueError(
                "Invalid value for `disk_redundancy`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._disk_redundancy = disk_redundancy

    @property
    def license_model(self):
        """
        Gets the license_model of this LaunchDbSystemFromBackupDetails.
        The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this LaunchDbSystemFromBackupDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this LaunchDbSystemFromBackupDetails.
        The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.


        :param license_model: The license_model of this LaunchDbSystemFromBackupDetails.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                "Invalid value for `license_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_model = license_model

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
