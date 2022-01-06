# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FleetStatusByCategory(object):
    """
    The number of databases in the fleet, grouped by database type and sub type.
    """

    #: A constant which can be used with the database_type property of a FleetStatusByCategory.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a FleetStatusByCategory.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_type property of a FleetStatusByCategory.
    #: This constant has a value of "CLOUD_SIDB"
    DATABASE_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the database_type property of a FleetStatusByCategory.
    #: This constant has a value of "CLOUD_RAC"
    DATABASE_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the database_type property of a FleetStatusByCategory.
    #: This constant has a value of "SHARED"
    DATABASE_TYPE_SHARED = "SHARED"

    #: A constant which can be used with the database_type property of a FleetStatusByCategory.
    #: This constant has a value of "DEDICATED"
    DATABASE_TYPE_DEDICATED = "DEDICATED"

    #: A constant which can be used with the database_sub_type property of a FleetStatusByCategory.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a FleetStatusByCategory.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a FleetStatusByCategory.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_sub_type property of a FleetStatusByCategory.
    #: This constant has a value of "ACD"
    DATABASE_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the database_sub_type property of a FleetStatusByCategory.
    #: This constant has a value of "ADB"
    DATABASE_SUB_TYPE_ADB = "ADB"

    #: A constant which can be used with the deployment_type property of a FleetStatusByCategory.
    #: This constant has a value of "ONPREMISE"
    DEPLOYMENT_TYPE_ONPREMISE = "ONPREMISE"

    #: A constant which can be used with the deployment_type property of a FleetStatusByCategory.
    #: This constant has a value of "BM"
    DEPLOYMENT_TYPE_BM = "BM"

    #: A constant which can be used with the deployment_type property of a FleetStatusByCategory.
    #: This constant has a value of "VM"
    DEPLOYMENT_TYPE_VM = "VM"

    #: A constant which can be used with the deployment_type property of a FleetStatusByCategory.
    #: This constant has a value of "EXADATA"
    DEPLOYMENT_TYPE_EXADATA = "EXADATA"

    #: A constant which can be used with the deployment_type property of a FleetStatusByCategory.
    #: This constant has a value of "EXADATA_CC"
    DEPLOYMENT_TYPE_EXADATA_CC = "EXADATA_CC"

    #: A constant which can be used with the deployment_type property of a FleetStatusByCategory.
    #: This constant has a value of "AUTONOMOUS"
    DEPLOYMENT_TYPE_AUTONOMOUS = "AUTONOMOUS"

    def __init__(self, **kwargs):
        """
        Initializes a new FleetStatusByCategory object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_type:
            The value to assign to the database_type property of this FleetStatusByCategory.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this FleetStatusByCategory.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param deployment_type:
            The value to assign to the deployment_type property of this FleetStatusByCategory.
            Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param inventory_count:
            The value to assign to the inventory_count property of this FleetStatusByCategory.
        :type inventory_count: int

        """
        self.swagger_types = {
            'database_type': 'str',
            'database_sub_type': 'str',
            'deployment_type': 'str',
            'inventory_count': 'int'
        }

        self.attribute_map = {
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'deployment_type': 'deploymentType',
            'inventory_count': 'inventoryCount'
        }

        self._database_type = None
        self._database_sub_type = None
        self._deployment_type = None
        self._inventory_count = None

    @property
    def database_type(self):
        """
        Gets the database_type of this FleetStatusByCategory.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this FleetStatusByCategory.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this FleetStatusByCategory.
        The type of Oracle Database installation.


        :param database_type: The database_type of this FleetStatusByCategory.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this FleetStatusByCategory.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this FleetStatusByCategory.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this FleetStatusByCategory.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.


        :param database_sub_type: The database_sub_type of this FleetStatusByCategory.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this FleetStatusByCategory.
        The infrastructure used to deploy the Oracle Database.

        Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this FleetStatusByCategory.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this FleetStatusByCategory.
        The infrastructure used to deploy the Oracle Database.


        :param deployment_type: The deployment_type of this FleetStatusByCategory.
        :type: str
        """
        allowed_values = ["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def inventory_count(self):
        """
        Gets the inventory_count of this FleetStatusByCategory.
        The number of databases in the fleet.


        :return: The inventory_count of this FleetStatusByCategory.
        :rtype: int
        """
        return self._inventory_count

    @inventory_count.setter
    def inventory_count(self, inventory_count):
        """
        Sets the inventory_count of this FleetStatusByCategory.
        The number of databases in the fleet.


        :param inventory_count: The inventory_count of this FleetStatusByCategory.
        :type: int
        """
        self._inventory_count = inventory_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
