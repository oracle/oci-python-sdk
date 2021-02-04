# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseUsageMetrics(object):
    """
    The list of aggregated metrics for Managed Databases in the fleet.
    """

    #: A constant which can be used with the database_type property of a DatabaseUsageMetrics.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a DatabaseUsageMetrics.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_sub_type property of a DatabaseUsageMetrics.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a DatabaseUsageMetrics.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a DatabaseUsageMetrics.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseUsageMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param db_id:
            The value to assign to the db_id property of this DatabaseUsageMetrics.
        :type db_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseUsageMetrics.
        :type compartment_id: str

        :param database_type:
            The value to assign to the database_type property of this DatabaseUsageMetrics.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this DatabaseUsageMetrics.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param database_name:
            The value to assign to the database_name property of this DatabaseUsageMetrics.
        :type database_name: str

        :param database_container_id:
            The value to assign to the database_container_id property of this DatabaseUsageMetrics.
        :type database_container_id: str

        :param metrics:
            The value to assign to the metrics property of this DatabaseUsageMetrics.
        :type metrics: list[oci.database_management.models.FleetMetricDefinition]

        """
        self.swagger_types = {
            'db_id': 'str',
            'compartment_id': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'database_name': 'str',
            'database_container_id': 'str',
            'metrics': 'list[FleetMetricDefinition]'
        }

        self.attribute_map = {
            'db_id': 'dbId',
            'compartment_id': 'compartmentId',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'database_name': 'databaseName',
            'database_container_id': 'databaseContainerId',
            'metrics': 'metrics'
        }

        self._db_id = None
        self._compartment_id = None
        self._database_type = None
        self._database_sub_type = None
        self._database_name = None
        self._database_container_id = None
        self._metrics = None

    @property
    def db_id(self):
        """
        Gets the db_id of this DatabaseUsageMetrics.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_id of this DatabaseUsageMetrics.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        """
        Sets the db_id of this DatabaseUsageMetrics.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_id: The db_id of this DatabaseUsageMetrics.
        :type: str
        """
        self._db_id = db_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DatabaseUsageMetrics.
        The `OCID`__ of the compartment where the Managed Database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DatabaseUsageMetrics.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseUsageMetrics.
        The `OCID`__ of the compartment where the Managed Database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DatabaseUsageMetrics.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_type(self):
        """
        Gets the database_type of this DatabaseUsageMetrics.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this DatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this DatabaseUsageMetrics.
        The type of Oracle Database installation.


        :param database_type: The database_type of this DatabaseUsageMetrics.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this DatabaseUsageMetrics.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this DatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this DatabaseUsageMetrics.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.


        :param database_sub_type: The database_sub_type of this DatabaseUsageMetrics.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def database_name(self):
        """
        Gets the database_name of this DatabaseUsageMetrics.
        The display name of the Managed Database.


        :return: The database_name of this DatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this DatabaseUsageMetrics.
        The display name of the Managed Database.


        :param database_name: The database_name of this DatabaseUsageMetrics.
        :type: str
        """
        self._database_name = database_name

    @property
    def database_container_id(self):
        """
        Gets the database_container_id of this DatabaseUsageMetrics.
        The `OCID`__ of the parent Container Database, in the case of a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_container_id of this DatabaseUsageMetrics.
        :rtype: str
        """
        return self._database_container_id

    @database_container_id.setter
    def database_container_id(self, database_container_id):
        """
        Sets the database_container_id of this DatabaseUsageMetrics.
        The `OCID`__ of the parent Container Database, in the case of a Pluggable Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_container_id: The database_container_id of this DatabaseUsageMetrics.
        :type: str
        """
        self._database_container_id = database_container_id

    @property
    def metrics(self):
        """
        Gets the metrics of this DatabaseUsageMetrics.
        A list of the database health metrics like CPU, Storage, and Memory.


        :return: The metrics of this DatabaseUsageMetrics.
        :rtype: list[oci.database_management.models.FleetMetricDefinition]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this DatabaseUsageMetrics.
        A list of the database health metrics like CPU, Storage, and Memory.


        :param metrics: The metrics of this DatabaseUsageMetrics.
        :type: list[oci.database_management.models.FleetMetricDefinition]
        """
        self._metrics = metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
