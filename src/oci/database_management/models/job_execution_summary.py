# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobExecutionSummary(object):
    """
    A summary of a job execution on a Managed Database.
    """

    #: A constant which can be used with the database_type property of a JobExecutionSummary.
    #: This constant has a value of "EXTERNAL_SIDB"
    DATABASE_TYPE_EXTERNAL_SIDB = "EXTERNAL_SIDB"

    #: A constant which can be used with the database_type property of a JobExecutionSummary.
    #: This constant has a value of "EXTERNAL_RAC"
    DATABASE_TYPE_EXTERNAL_RAC = "EXTERNAL_RAC"

    #: A constant which can be used with the database_type property of a JobExecutionSummary.
    #: This constant has a value of "CLOUD_SIDB"
    DATABASE_TYPE_CLOUD_SIDB = "CLOUD_SIDB"

    #: A constant which can be used with the database_type property of a JobExecutionSummary.
    #: This constant has a value of "CLOUD_RAC"
    DATABASE_TYPE_CLOUD_RAC = "CLOUD_RAC"

    #: A constant which can be used with the database_type property of a JobExecutionSummary.
    #: This constant has a value of "SHARED"
    DATABASE_TYPE_SHARED = "SHARED"

    #: A constant which can be used with the database_type property of a JobExecutionSummary.
    #: This constant has a value of "DEDICATED"
    DATABASE_TYPE_DEDICATED = "DEDICATED"

    #: A constant which can be used with the database_type property of a JobExecutionSummary.
    #: This constant has a value of "CLOUD_AT_CUSTOMER"
    DATABASE_TYPE_CLOUD_AT_CUSTOMER = "CLOUD_AT_CUSTOMER"

    #: A constant which can be used with the database_sub_type property of a JobExecutionSummary.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a JobExecutionSummary.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a JobExecutionSummary.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the database_sub_type property of a JobExecutionSummary.
    #: This constant has a value of "ACD"
    DATABASE_SUB_TYPE_ACD = "ACD"

    #: A constant which can be used with the database_sub_type property of a JobExecutionSummary.
    #: This constant has a value of "ADB"
    DATABASE_SUB_TYPE_ADB = "ADB"

    #: A constant which can be used with the deployment_type property of a JobExecutionSummary.
    #: This constant has a value of "ONPREMISE"
    DEPLOYMENT_TYPE_ONPREMISE = "ONPREMISE"

    #: A constant which can be used with the deployment_type property of a JobExecutionSummary.
    #: This constant has a value of "BM"
    DEPLOYMENT_TYPE_BM = "BM"

    #: A constant which can be used with the deployment_type property of a JobExecutionSummary.
    #: This constant has a value of "VM"
    DEPLOYMENT_TYPE_VM = "VM"

    #: A constant which can be used with the deployment_type property of a JobExecutionSummary.
    #: This constant has a value of "EXADATA"
    DEPLOYMENT_TYPE_EXADATA = "EXADATA"

    #: A constant which can be used with the deployment_type property of a JobExecutionSummary.
    #: This constant has a value of "EXADATA_CC"
    DEPLOYMENT_TYPE_EXADATA_CC = "EXADATA_CC"

    #: A constant which can be used with the deployment_type property of a JobExecutionSummary.
    #: This constant has a value of "AUTONOMOUS"
    DEPLOYMENT_TYPE_AUTONOMOUS = "AUTONOMOUS"

    #: A constant which can be used with the deployment_type property of a JobExecutionSummary.
    #: This constant has a value of "EXADATA_XS"
    DEPLOYMENT_TYPE_EXADATA_XS = "EXADATA_XS"

    #: A constant which can be used with the workload_type property of a JobExecutionSummary.
    #: This constant has a value of "OLTP"
    WORKLOAD_TYPE_OLTP = "OLTP"

    #: A constant which can be used with the workload_type property of a JobExecutionSummary.
    #: This constant has a value of "DW"
    WORKLOAD_TYPE_DW = "DW"

    #: A constant which can be used with the workload_type property of a JobExecutionSummary.
    #: This constant has a value of "AJD"
    WORKLOAD_TYPE_AJD = "AJD"

    #: A constant which can be used with the workload_type property of a JobExecutionSummary.
    #: This constant has a value of "APEX"
    WORKLOAD_TYPE_APEX = "APEX"

    def __init__(self, **kwargs):
        """
        Initializes a new JobExecutionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JobExecutionSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this JobExecutionSummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this JobExecutionSummary.
        :type compartment_id: str

        :param managed_database_group_id:
            The value to assign to the managed_database_group_id property of this JobExecutionSummary.
        :type managed_database_group_id: str

        :param managed_database_id:
            The value to assign to the managed_database_id property of this JobExecutionSummary.
        :type managed_database_id: str

        :param managed_database_name:
            The value to assign to the managed_database_name property of this JobExecutionSummary.
        :type managed_database_name: str

        :param database_type:
            The value to assign to the database_type property of this JobExecutionSummary.
            Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_type: str

        :param database_sub_type:
            The value to assign to the database_sub_type property of this JobExecutionSummary.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param deployment_type:
            The value to assign to the deployment_type property of this JobExecutionSummary.
            Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", "EXADATA_XS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type deployment_type: str

        :param is_cluster:
            The value to assign to the is_cluster property of this JobExecutionSummary.
        :type is_cluster: bool

        :param workload_type:
            The value to assign to the workload_type property of this JobExecutionSummary.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type workload_type: str

        :param job_id:
            The value to assign to the job_id property of this JobExecutionSummary.
        :type job_id: str

        :param job_name:
            The value to assign to the job_name property of this JobExecutionSummary.
        :type job_name: str

        :param status:
            The value to assign to the status property of this JobExecutionSummary.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this JobExecutionSummary.
        :type time_created: datetime

        :param time_completed:
            The value to assign to the time_completed property of this JobExecutionSummary.
        :type time_completed: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'managed_database_group_id': 'str',
            'managed_database_id': 'str',
            'managed_database_name': 'str',
            'database_type': 'str',
            'database_sub_type': 'str',
            'deployment_type': 'str',
            'is_cluster': 'bool',
            'workload_type': 'str',
            'job_id': 'str',
            'job_name': 'str',
            'status': 'str',
            'time_created': 'datetime',
            'time_completed': 'datetime'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'managed_database_group_id': 'managedDatabaseGroupId',
            'managed_database_id': 'managedDatabaseId',
            'managed_database_name': 'managedDatabaseName',
            'database_type': 'databaseType',
            'database_sub_type': 'databaseSubType',
            'deployment_type': 'deploymentType',
            'is_cluster': 'isCluster',
            'workload_type': 'workloadType',
            'job_id': 'jobId',
            'job_name': 'jobName',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_completed': 'timeCompleted'
        }
        self._id = None
        self._name = None
        self._compartment_id = None
        self._managed_database_group_id = None
        self._managed_database_id = None
        self._managed_database_name = None
        self._database_type = None
        self._database_sub_type = None
        self._deployment_type = None
        self._is_cluster = None
        self._workload_type = None
        self._job_id = None
        self._job_name = None
        self._status = None
        self._time_created = None
        self._time_completed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this JobExecutionSummary.
        The identifier of the job execution.


        :return: The id of this JobExecutionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobExecutionSummary.
        The identifier of the job execution.


        :param id: The id of this JobExecutionSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this JobExecutionSummary.
        The name of the job execution.


        :return: The name of this JobExecutionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JobExecutionSummary.
        The name of the job execution.


        :param name: The name of this JobExecutionSummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this JobExecutionSummary.
        The `OCID`__ of the compartment in which the parent job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this JobExecutionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this JobExecutionSummary.
        The `OCID`__ of the compartment in which the parent job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this JobExecutionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def managed_database_group_id(self):
        """
        Gets the managed_database_group_id of this JobExecutionSummary.
        The `OCID`__ of the Managed Database Group where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_group_id of this JobExecutionSummary.
        :rtype: str
        """
        return self._managed_database_group_id

    @managed_database_group_id.setter
    def managed_database_group_id(self, managed_database_group_id):
        """
        Sets the managed_database_group_id of this JobExecutionSummary.
        The `OCID`__ of the Managed Database Group where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_group_id: The managed_database_group_id of this JobExecutionSummary.
        :type: str
        """
        self._managed_database_group_id = managed_database_group_id

    @property
    def managed_database_id(self):
        """
        **[Required]** Gets the managed_database_id of this JobExecutionSummary.
        The `OCID`__ of Managed Database associated with the job execution.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this JobExecutionSummary.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this JobExecutionSummary.
        The `OCID`__ of Managed Database associated with the job execution.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this JobExecutionSummary.
        :type: str
        """
        self._managed_database_id = managed_database_id

    @property
    def managed_database_name(self):
        """
        **[Required]** Gets the managed_database_name of this JobExecutionSummary.
        The name of the Managed Database associated with the job execution.


        :return: The managed_database_name of this JobExecutionSummary.
        :rtype: str
        """
        return self._managed_database_name

    @managed_database_name.setter
    def managed_database_name(self, managed_database_name):
        """
        Sets the managed_database_name of this JobExecutionSummary.
        The name of the Managed Database associated with the job execution.


        :param managed_database_name: The managed_database_name of this JobExecutionSummary.
        :type: str
        """
        self._managed_database_name = managed_database_name

    @property
    def database_type(self):
        """
        Gets the database_type of this JobExecutionSummary.
        The type of Oracle Database installation.

        Allowed values for this property are: "EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_type of this JobExecutionSummary.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this JobExecutionSummary.
        The type of Oracle Database installation.


        :param database_type: The database_type of this JobExecutionSummary.
        :type: str
        """
        allowed_values = ["EXTERNAL_SIDB", "EXTERNAL_RAC", "CLOUD_SIDB", "CLOUD_RAC", "SHARED", "DEDICATED", "CLOUD_AT_CUSTOMER"]
        if not value_allowed_none_or_none_sentinel(database_type, allowed_values):
            database_type = 'UNKNOWN_ENUM_VALUE'
        self._database_type = database_type

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this JobExecutionSummary.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", "ACD", "ADB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this JobExecutionSummary.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this JobExecutionSummary.
        The subtype of the Oracle Database. Indicates whether the database is a Container Database, Pluggable Database, or a Non-container Database.


        :param database_sub_type: The database_sub_type of this JobExecutionSummary.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB", "ACD", "ADB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this JobExecutionSummary.
        A list of the supported infrastructure that can be used to deploy the database.

        Allowed values for this property are: "ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", "EXADATA_XS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The deployment_type of this JobExecutionSummary.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this JobExecutionSummary.
        A list of the supported infrastructure that can be used to deploy the database.


        :param deployment_type: The deployment_type of this JobExecutionSummary.
        :type: str
        """
        allowed_values = ["ONPREMISE", "BM", "VM", "EXADATA", "EXADATA_CC", "AUTONOMOUS", "EXADATA_XS"]
        if not value_allowed_none_or_none_sentinel(deployment_type, allowed_values):
            deployment_type = 'UNKNOWN_ENUM_VALUE'
        self._deployment_type = deployment_type

    @property
    def is_cluster(self):
        """
        Gets the is_cluster of this JobExecutionSummary.
        Indicates whether the Oracle Database is part of a cluster.


        :return: The is_cluster of this JobExecutionSummary.
        :rtype: bool
        """
        return self._is_cluster

    @is_cluster.setter
    def is_cluster(self, is_cluster):
        """
        Sets the is_cluster of this JobExecutionSummary.
        Indicates whether the Oracle Database is part of a cluster.


        :param is_cluster: The is_cluster of this JobExecutionSummary.
        :type: bool
        """
        self._is_cluster = is_cluster

    @property
    def workload_type(self):
        """
        Gets the workload_type of this JobExecutionSummary.
        The workload type of the Autonomous Database.

        Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The workload_type of this JobExecutionSummary.
        :rtype: str
        """
        return self._workload_type

    @workload_type.setter
    def workload_type(self, workload_type):
        """
        Sets the workload_type of this JobExecutionSummary.
        The workload type of the Autonomous Database.


        :param workload_type: The workload_type of this JobExecutionSummary.
        :type: str
        """
        allowed_values = ["OLTP", "DW", "AJD", "APEX"]
        if not value_allowed_none_or_none_sentinel(workload_type, allowed_values):
            workload_type = 'UNKNOWN_ENUM_VALUE'
        self._workload_type = workload_type

    @property
    def job_id(self):
        """
        **[Required]** Gets the job_id of this JobExecutionSummary.
        The `OCID`__ of the parent job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The job_id of this JobExecutionSummary.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this JobExecutionSummary.
        The `OCID`__ of the parent job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param job_id: The job_id of this JobExecutionSummary.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """
        **[Required]** Gets the job_name of this JobExecutionSummary.
        The name of the parent job.


        :return: The job_name of this JobExecutionSummary.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """
        Sets the job_name of this JobExecutionSummary.
        The name of the parent job.


        :param job_name: The job_name of this JobExecutionSummary.
        :type: str
        """
        self._job_name = job_name

    @property
    def status(self):
        """
        **[Required]** Gets the status of this JobExecutionSummary.
        The status of the job execution.


        :return: The status of this JobExecutionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobExecutionSummary.
        The status of the job execution.


        :param status: The status of this JobExecutionSummary.
        :type: str
        """
        self._status = status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this JobExecutionSummary.
        The date and time when the job execution was created.


        :return: The time_created of this JobExecutionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobExecutionSummary.
        The date and time when the job execution was created.


        :param time_created: The time_created of this JobExecutionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_completed(self):
        """
        Gets the time_completed of this JobExecutionSummary.
        The date and time when the job execution was completed.


        :return: The time_completed of this JobExecutionSummary.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this JobExecutionSummary.
        The date and time when the job execution was completed.


        :param time_completed: The time_completed of this JobExecutionSummary.
        :type: datetime
        """
        self._time_completed = time_completed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
