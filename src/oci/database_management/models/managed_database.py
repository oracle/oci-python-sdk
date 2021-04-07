# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedDatabase(object):
    """
    The details of a Managed Database.
    """

    #: A constant which can be used with the database_type property of a ManagedDatabase.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a ManagedDatabase.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabase.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabase.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a ManagedDatabase.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_status property of a ManagedDatabase.
    #: This constant has a value of "UP"
    DATABASE_STATUS_UP = "UP"

    #: A constant which can be used with the database_status property of a ManagedDatabase.
    #: This constant has a value of "DOWN"
    DATABASE_STATUS_DOWN = "DOWN"

    #: A constant which can be used with the database_status property of a ManagedDatabase.
    #: This constant has a value of "UNKNOWN"
    DATABASE_STATUS_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedDatabase.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedDatabase.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this ManagedDatabase.
        :type name: str

        :param database_type:
            The value to assign to the database_type property of this ManagedDatabase.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this ManagedDatabase.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param is_cluster:
            The value to assign to the is_cluster property of this ManagedDatabase.
        :type is_cluster: bool

        :param parent_container_id:
            The value to assign to the parent_container_id property of this ManagedDatabase.
        :type parent_container_id: str

        :param managed_database_groups:
            The value to assign to the managed_database_groups property of this ManagedDatabase.
        :type managed_database_groups: list[oci.database_management.models.ParentGroup]

        :param time_created:
            The value to assign to the time_created property of this ManagedDatabase.
        :type time_created: datetime

        :param database_status:
            The value to assign to the database_status property of this ManagedDatabase.
            Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_status: str

        :param parent_container_name:
            The value to assign to the parent_container_name property of this ManagedDatabase.
        :type parent_container_name: str

        :param parent_container_compartment_id:
            The value to assign to the parent_container_compartment_id property of this ManagedDatabase.
        :type parent_container_compartment_id: str

        :param instance_count:
            The value to assign to the instance_count property of this ManagedDatabase.
        :type instance_count: int

        :param instance_details:
            The value to assign to the instance_details property of this ManagedDatabase.
        :type instance_details: list[oci.database_management.models.InstanceDetails]

        :param pdb_count:
            The value to assign to the pdb_count property of this ManagedDatabase.
        :type pdb_count: int

        :param pdb_status:
            The value to assign to the pdb_status property of this ManagedDatabase.
        :type pdb_status: list[oci.database_management.models.PdbStatusDetails]

        :param additional_details:
            The value to assign to the additional_details property of this ManagedDatabase.
        :type additional_details: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'is_cluster': 'bool',
            'parent_container_id': 'str',
            'managed_database_groups': 'list[ParentGroup]',
            'time_created': 'datetime',
            'database_status': 'str',
            'parent_container_name': 'str',
            'parent_container_compartment_id': 'str',
            'instance_count': 'int',
            'instance_details': 'list[InstanceDetails]',
            'pdb_count': 'int',
            'pdb_status': 'list[PdbStatusDetails]',
            'additional_details': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'is_cluster': 'isCluster',
            'parent_container_id': 'parentContainerId',
            'managed_database_groups': 'managedDatabaseGroups',
            'time_created': 'timeCreated',
            'database_status': 'databaseStatus',
            'parent_container_name': 'parentContainerName',
            'parent_container_compartment_id': 'parentContainerCompartmentId',
            'instance_count': 'instanceCount',
            'instance_details': 'instanceDetails',
            'pdb_count': 'pdbCount',
            'pdb_status': 'pdbStatus',
            'additional_details': 'additionalDetails'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._database_type = None
        self._database_sub_type = None
        self._is_cluster = None
        self._parent_container_id = None
        self._managed_database_groups = None
        self._time_created = None
        self._database_status = None
        self._parent_container_name = None
        self._parent_container_compartment_id = None
        self._instance_count = None
        self._instance_details = None
        self._pdb_count = None
        self._pdb_status = None
        self._additional_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ManagedDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ManagedDatabase.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedDatabase.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ManagedDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedDatabase.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ManagedDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedDatabase.
        The name of the Managed Database.


        :return: The name of this ManagedDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedDatabase.
        The name of the Managed Database.


        :param name: The name of this ManagedDatabase.
        :type: str
        """
        self._name = name

    @property
    def database_type(self):
        """
        **[Required]** Gets the database_type of this ManagedDatabase.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this ManagedDatabase.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this ManagedDatabase.
        The type of Oracle Database installation.


        :param database_type: The database_type of this ManagedDatabase.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        **[Required]** Gets the database_sub_type of this ManagedDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this ManagedDatabase.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this ManagedDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.


        :param database_sub_type: The database_sub_type of this ManagedDatabase.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def is_cluster(self):
        """
        **[Required]** Gets the is_cluster of this ManagedDatabase.
        Indicates whether the Oracle Database is part of a cluster.


        :return: The is_cluster of this ManagedDatabase.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this ManagedDatabase.
        Indicates whether the Oracle Database is part of a cluster.


        :param is_cluster: The is_cluster of this ManagedDatabase.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def parent_container_id(self):
        """
        Gets the parent_container_id of this ManagedDatabase.
        The `OCID`__ of the parent Container Database
        if Managed Database is a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The parent_container_id of this ManagedDatabase.
        :rtype: str
        """
        return self._parent_container_id

    @parent_container_id.setter
    def parent_container_id(self, parent_container_id):
        """
        Sets the parent_container_id of this ManagedDatabase.
        The `OCID`__ of the parent Container Database
        if Managed Database is a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param parent_container_id: The parent_container_id of this ManagedDatabase.
        :type: str
        """
        self._parent_container_id = parent_container_id

    @property
    def managed_database_groups(self):
        """
        Gets the managed_database_groups of this ManagedDatabase.
        A list of Managed Database Groups that the Managed Database belongs to.


        :return: The managed_database_groups of this ManagedDatabase.
        :rtype: list[oci.database_management.models.ParentGroup]
        """
        return self._managed_database_groups

    @managed_database_groups.setter
    def managed_database_groups(self, managed_database_groups):
        """
        Sets the managed_database_groups of this ManagedDatabase.
        A list of Managed Database Groups that the Managed Database belongs to.


        :param managed_database_groups: The managed_database_groups of this ManagedDatabase.
        :type: list[oci.database_management.models.ParentGroup]
        """
        self._managed_database_groups = managed_database_groups

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagedDatabase.
        The date and time the Managed Database was created.


        :return: The time_created of this ManagedDatabase.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedDatabase.
        The date and time the Managed Database was created.


        :param time_created: The time_created of this ManagedDatabase.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def database_status(self):
        """
        Gets the database_status of this ManagedDatabase.
        The status of the Oracle Database. Indicates whether the status of the database
        is UP, DOWN, or UNKNOWN at the current time.

        Allowed values for this property are: "UP", "DOWN", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_status of this ManagedDatabase.
        :rtype: str
        """
        return self._database_status

    @database_status.setter
    def database_status(self, database_status):
        """
        Sets the database_status of this ManagedDatabase.
        The status of the Oracle Database. Indicates whether the status of the database
        is UP, DOWN, or UNKNOWN at the current time.


        :param database_status: The database_status of this ManagedDatabase.
        :type: str
        """
        allowed_values = ["UP", "DOWN", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(database_status, allowed_values):
            database_status = 'UNKNOWN_ENUM_VALUE'
        self._database_status = database_status

    @property
    def parent_container_name(self):
        """
        Gets the parent_container_name of this ManagedDatabase.
        The name of the parent Container Database.


        :return: The parent_container_name of this ManagedDatabase.
        :rtype: str
        """
        return self._parent_container_name

    @parent_container_name.setter
    def parent_container_name(self, parent_container_name):
        """
        Sets the parent_container_name of this ManagedDatabase.
        The name of the parent Container Database.


        :param parent_container_name: The parent_container_name of this ManagedDatabase.
        :type: str
        """
        self._parent_container_name = parent_container_name

    @property
    def parent_container_compartment_id(self):
        """
        Gets the parent_container_compartment_id of this ManagedDatabase.
        The `OCID`__ of the compartment
        in which the parent Container Database resides, if the Managed Database
        is a Pluggable Database (PDB).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The parent_container_compartment_id of this ManagedDatabase.
        :rtype: str
        """
        return self._parent_container_compartment_id

    @parent_container_compartment_id.setter
    def parent_container_compartment_id(self, parent_container_compartment_id):
        """
        Sets the parent_container_compartment_id of this ManagedDatabase.
        The `OCID`__ of the compartment
        in which the parent Container Database resides, if the Managed Database
        is a Pluggable Database (PDB).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param parent_container_compartment_id: The parent_container_compartment_id of this ManagedDatabase.
        :type: str
        """
        self._parent_container_compartment_id = parent_container_compartment_id

    @property
    def instance_count(self):
        """
        Gets the instance_count of this ManagedDatabase.
        The number of Oracle Real Application Clusters (Oracle RAC) database instances.


        :return: The instance_count of this ManagedDatabase.
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """
        Sets the instance_count of this ManagedDatabase.
        The number of Oracle Real Application Clusters (Oracle RAC) database instances.


        :param instance_count: The instance_count of this ManagedDatabase.
        :type: int
        """
        self._instance_count = instance_count

    @property
    def instance_details(self):
        """
        Gets the instance_details of this ManagedDatabase.
        The details of the Oracle Real Application Clusters (Oracle RAC) database instances.


        :return: The instance_details of this ManagedDatabase.
        :rtype: list[oci.database_management.models.InstanceDetails]
        """
        return self._instance_details

    @instance_details.setter
    def instance_details(self, instance_details):
        """
        Sets the instance_details of this ManagedDatabase.
        The details of the Oracle Real Application Clusters (Oracle RAC) database instances.


        :param instance_details: The instance_details of this ManagedDatabase.
        :type: list[oci.database_management.models.InstanceDetails]
        """
        self._instance_details = instance_details

    @property
    def pdb_count(self):
        """
        Gets the pdb_count of this ManagedDatabase.
        The number of PDBs in the Container Database.


        :return: The pdb_count of this ManagedDatabase.
        :rtype: int
        """
        return self._pdb_count

    @pdb_count.setter
    def pdb_count(self, pdb_count):
        """
        Sets the pdb_count of this ManagedDatabase.
        The number of PDBs in the Container Database.


        :param pdb_count: The pdb_count of this ManagedDatabase.
        :type: int
        """
        self._pdb_count = pdb_count

    @property
    def pdb_status(self):
        """
        Gets the pdb_status of this ManagedDatabase.
        The status of the PDB in the Container Database.


        :return: The pdb_status of this ManagedDatabase.
        :rtype: list[oci.database_management.models.PdbStatusDetails]
        """
        return self._pdb_status

    @pdb_status.setter
    def pdb_status(self, pdb_status):
        """
        Sets the pdb_status of this ManagedDatabase.
        The status of the PDB in the Container Database.


        :param pdb_status: The pdb_status of this ManagedDatabase.
        :type: list[oci.database_management.models.PdbStatusDetails]
        """
        self._pdb_status = pdb_status

    @property
    def additional_details(self):
        """
        Gets the additional_details of this ManagedDatabase.
        The additional details specific to a type of database defined in `{\"key\": \"value\"}` format.
        Example: `{\"bar-key\": \"value\"}`


        :return: The additional_details of this ManagedDatabase.
        :rtype: dict(str, str)
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this ManagedDatabase.
        The additional details specific to a type of database defined in `{\"key\": \"value\"}` format.
        Example: `{\"bar-key\": \"value\"}`


        :param additional_details: The additional_details of this ManagedDatabase.
        :type: dict(str, str)
        """
        self._additional_details = additional_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
