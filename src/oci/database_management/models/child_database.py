# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChildDatabase(object):
    """
    The child Managed Database of a Managed Database Group.
    """

    #: A constant which can be used with the deployment_type property of a ChildDatabase.
    #: This constant has a value of "ONPREMISE"
    DEPLOYMENT_TYPE_ONPREMISE = "ONPREMISE"

    #: A constant which can be used with the deployment_type property of a ChildDatabase.
    #: This constant has a value of "BM"
    DEPLOYMENT_TYPE_BM = "BM"

    #: A constant which can be used with the deployment_type property of a ChildDatabase.
    #: This constant has a value of "VM"
    DEPLOYMENT_TYPE_VM = "VM"

    #: A constant which can be used with the deployment_type property of a ChildDatabase.
    #: This constant has a value of "EXADATA"
    DEPLOYMENT_TYPE_EXADATA = "EXADATA"

    #: A constant which can be used with the deployment_type property of a ChildDatabase.
    #: This constant has a value of "EXADATA_CC"
    DEPLOYMENT_TYPE_EXADATA_CC = "EXADATA_CC"

    #: A constant which can be used with the deployment_type property of a ChildDatabase.
    #: This constant has a value of "AUTONOMOUS"
    DEPLOYMENT_TYPE_AUTONOMOUS = "AUTONOMOUS"

    #: A constant which can be used with the workload_type property of a ChildDatabase.
    #: This constant has a value of "OLTP"
    WORKLOAD_TYPE_OLTP = "OLTP"

    #: A constant which can be used with the workload_type property of a ChildDatabase.
    #: This constant has a value of "DW"
    WORKLOAD_TYPE_DW = "DW"

    #: A constant which can be used with the workload_type property of a ChildDatabase.
    #: This constant has a value of "AJD"
    WORKLOAD_TYPE_AJD = "AJD"

    #: A constant which can be used with the workload_type property of a ChildDatabase.
    #: This constant has a value of "APEX"
    WORKLOAD_TYPE_APEX = "APEX"

    #: A constant which can be used with the database_type property of a ChildDatabase.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a ChildDatabase.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_type property of a ChildDatabase.
    #: This constant has a value of "CLOUD_SIDB"
    DATABASE_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the database_type property of a ChildDatabase.
    #: This constant has a value of "CLOUD_RAC"
    DATABASE_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the database_type property of a ChildDatabase.
    #: This constant has a value of "SHARED"
    DATABASE_TYPE_SHARED = "SHARED"

    #: A constant which can be used with the database_type property of a ChildDatabase.
    #: This constant has a value of "DEDICATED"
    DATABASE_TYPE_DEDICATED = "DEDICATED"

    #: A constant which can be used with the database_sub_type property of a ChildDatabase.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a ChildDatabase.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a ChildDatabase.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_sub_type property of a ChildDatabase.
    #: This constant has a value of "ACD"
    DATABASE_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the database_sub_type property of a ChildDatabase.
    #: This constant has a value of "ADB"
    DATABASE_SUB_TYPE_ADB = "ADB"

    def __init__(self, **kwargs):
        """
        Initializes a new ChildDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ChildDatabase.
        :type id: str

        :param name:
            The value to assign to the name property of this ChildDatabase.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ChildDatabase.
        :type compartment_id: str

        :param deployment_type:
            The value to assign to the deployment_type property of this ChildDatabase.
            Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param workload_type:
            The value to assign to the workload_type property of this ChildDatabase.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type workload_type: str

        :param database_type:
            The value to assign to the database_type property of this ChildDatabase.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this ChildDatabase.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param time_added:
            The value to assign to the time_added property of this ChildDatabase.
        :type time_added: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'deployment_type': 'str',
            'workload_type': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'time_added': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'deployment_type': 'deploymentType',
            'workload_type': 'workloadType',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'time_added': 'timeAdded'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._deployment_type = None
        self._workload_type = None
        self._database_type = None
        self._database_sub_type = None
        self._time_added = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ChildDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ChildDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ChildDatabase.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ChildDatabase.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ChildDatabase.
        The name of the Managed Database.


        :return: The name of this ChildDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ChildDatabase.
        The name of the Managed Database.


        :param name: The name of this ChildDatabase.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ChildDatabase.
        The `OCID`__ of the compartment in which the Managed Database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ChildDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ChildDatabase.
        The `OCID`__ of the compartment in which the Managed Database resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ChildDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this ChildDatabase.
        The infrastructure used to deploy the Oracle Database.

        Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this ChildDatabase.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this ChildDatabase.
        The infrastructure used to deploy the Oracle Database.


        :param deployment_type: The deployment_type of this ChildDatabase.
        :type: str
        """
        allowed_values = ["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def workload_type(self):
        """
        Gets the workload_type of this ChildDatabase.
        The workload type of the Autonomous Database.

        Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The workload_type of this ChildDatabase.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """
        Sets the workload_type of this ChildDatabase.
        The workload type of the Autonomous Database.


        :param workload_type: The workload_type of this ChildDatabase.
        :type: str
        """
        allowed_values = ["OLTP", "DW", "AJD", "APEX"]
        if not value_allowed_none_or_none_sentinel(workload_type, allowed_values):
            workload_type = 'UNKNOWN_ENUM_VALUE'
        self._workload_type = workload_type

    @property
    def database_type(self):
        """
        Gets the database_type of this ChildDatabase.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this ChildDatabase.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this ChildDatabase.
        The type of Oracle Database installation.


        :param database_type: The database_type of this ChildDatabase.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this ChildDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this ChildDatabase.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this ChildDatabase.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database,
        Pluggable Database, Non-container Database, Autonomous Database, or Autonomous Container Database.


        :param database_sub_type: The database_sub_type of this ChildDatabase.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def time_added(self):
        """
        **[Required]** Gets the time_added of this ChildDatabase.
        The date and time the Managed Database was added to the group.


        :return: The time_added of this ChildDatabase.
        :rtype: datetime
        """
        return self._time_added

    @time_added.setter
    def time_added(self, time_added):
        """
        Sets the time_added of this ChildDatabase.
        The date and time the Managed Database was added to the group.


        :param time_added: The time_added of this ChildDatabase.
        :type: datetime
        """
        self._time_added = time_added

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
