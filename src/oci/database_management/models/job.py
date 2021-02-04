# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Job(object):
    """
    The details of the job.
    """

    #: A constant which can be used with the database_sub_type property of a Job.
    #: This constant has a value of "CDB"
    DATABASE_SUB_TYPE_CDB = "CDB"

    #: A constant which can be used with the database_sub_type property of a Job.
    #: This constant has a value of "PDB"
    DATABASE_SUB_TYPE_PDB = "PDB"

    #: A constant which can be used with the database_sub_type property of a Job.
    #: This constant has a value of "NON_CDB"
    DATABASE_SUB_TYPE_NON_CDB = "NON_CDB"

    #: A constant which can be used with the schedule_type property of a Job.
    #: This constant has a value of "IMMEDIATE"
    SCHEDULE_TYPE_IMMEDIATE = "IMMEDIATE"

    #: A constant which can be used with the job_type property of a Job.
    #: This constant has a value of "SQL"
    JOB_TYPE_SQL = "SQL"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Job.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new Job object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database_management.models.SqlJob`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Job.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Job.
        :type compartment_id: str

        :param name:
            The value to assign to the name property of this Job.
        :type name: str

        :param description:
            The value to assign to the description property of this Job.
        :type description: str

        :param managed_database_group_id:
            The value to assign to the managed_database_group_id property of this Job.
        :type managed_database_group_id: str

        :param managed_database_id:
            The value to assign to the managed_database_id property of this Job.
        :type managed_database_id: str

        :param managed_databases_details:
            The value to assign to the managed_databases_details property of this Job.
        :type managed_databases_details: list[oci.database_management.models.JobDatabase]

        :param database_sub_type:
            The value to assign to the database_sub_type property of this Job.
            Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_sub_type: str

        :param schedule_type:
            The value to assign to the schedule_type property of this Job.
            Allowed values for this property are: "IMMEDIATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schedule_type: str

        :param job_type:
            The value to assign to the job_type property of this Job.
            Allowed values for this property are: "SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Job.
            Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param timeout:
            The value to assign to the timeout property of this Job.
        :type timeout: str

        :param result_location:
            The value to assign to the result_location property of this Job.
        :type result_location: oci.database_management.models.JobExecutionResultLocation

        :param submission_error_message:
            The value to assign to the submission_error_message property of this Job.
        :type submission_error_message: str

        :param time_created:
            The value to assign to the time_created property of this Job.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Job.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'name': 'str',
            'description': 'str',
            'managed_database_group_id': 'str',
            'managed_database_id': 'str',
            'managed_databases_details': 'list[JobDatabase]',
            'database_sub_type': 'str',
            'schedule_type': 'str',
            'job_type': 'str',
            'lifecycle_state': 'str',
            'timeout': 'str',
            'result_location': 'JobExecutionResultLocation',
            'submission_error_message': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'name': 'name',
            'description': 'description',
            'managed_database_group_id': 'managedDatabaseGroupId',
            'managed_database_id': 'managedDatabaseId',
            'managed_databases_details': 'managedDatabasesDetails',
            'database_sub_type': 'databaseSubType',
            'schedule_type': 'scheduleType',
            'job_type': 'jobType',
            'lifecycle_state': 'lifecycleState',
            'timeout': 'timeout',
            'result_location': 'resultLocation',
            'submission_error_message': 'submissionErrorMessage',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._name = None
        self._description = None
        self._managed_database_group_id = None
        self._managed_database_id = None
        self._managed_databases_details = None
        self._database_sub_type = None
        self._schedule_type = None
        self._job_type = None
        self._lifecycle_state = None
        self._timeout = None
        self._result_location = None
        self._submission_error_message = None
        self._time_created = None
        self._time_updated = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['jobType']

        if type == 'SQL':
            return 'SqlJob'
        else:
            return 'Job'

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Job.
        The `OCID`__ of the job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Job.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Job.
        The `OCID`__ of the compartment in which the job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Job.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Job.
        The `OCID`__ of the compartment in which the job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Job.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Job.
        The display name of the job.


        :return: The name of this Job.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Job.
        The display name of the job.


        :param name: The name of this Job.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Job.
        The description of the job.


        :return: The description of this Job.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Job.
        The description of the job.


        :param description: The description of this Job.
        :type: str
        """
        self._description = description

    @property
    def managed_database_group_id(self):
        """
        Gets the managed_database_group_id of this Job.
        The `OCID`__ of the Managed Database Group where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_group_id of this Job.
        :rtype: str
        """
        return self._managed_database_group_id

    @managed_database_group_id.setter
    def managed_database_group_id(self, managed_database_group_id):
        """
        Sets the managed_database_group_id of this Job.
        The `OCID`__ of the Managed Database Group where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_group_id: The managed_database_group_id of this Job.
        :type: str
        """
        self._managed_database_group_id = managed_database_group_id

    @property
    def managed_database_id(self):
        """
        Gets the managed_database_id of this Job.
        The `OCID`__ of the Managed Database where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this Job.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this Job.
        The `OCID`__ of the Managed Database where the job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this Job.
        :type: str
        """
        self._managed_database_id = managed_database_id

    @property
    def managed_databases_details(self):
        """
        Gets the managed_databases_details of this Job.
        The details of the Managed Databases where the job has to be executed.


        :return: The managed_databases_details of this Job.
        :rtype: list[oci.database_management.models.JobDatabase]
        """
        return self._managed_databases_details

    @managed_databases_details.setter
    def managed_databases_details(self, managed_databases_details):
        """
        Sets the managed_databases_details of this Job.
        The details of the Managed Databases where the job has to be executed.


        :param managed_databases_details: The managed_databases_details of this Job.
        :type: list[oci.database_management.models.JobDatabase]
        """
        self._managed_databases_details = managed_databases_details

    @property
    def database_sub_type(self):
        """
        Gets the database_sub_type of this Job.
        The subtype of the Oracle Database where the job has to be executed. Applicable only when managedDatabaseGroupId is provided.

        Allowed values for this property are: "CDB", "PDB", "NON_CDB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_sub_type of this Job.
        :rtype: str
        """
        return self._database_sub_type

    @database_sub_type.setter
    def database_sub_type(self, database_sub_type):
        """
        Sets the database_sub_type of this Job.
        The subtype of the Oracle Database where the job has to be executed. Applicable only when managedDatabaseGroupId is provided.


        :param database_sub_type: The database_sub_type of this Job.
        :type: str
        """
        allowed_values = ["CDB", "PDB", "NON_CDB"]
        if not value_allowed_none_or_none_sentinel(database_sub_type, allowed_values):
            database_sub_type = 'UNKNOWN_ENUM_VALUE'
        self._database_sub_type = database_sub_type

    @property
    def schedule_type(self):
        """
        **[Required]** Gets the schedule_type of this Job.
        The schedule type of the job.

        Allowed values for this property are: "IMMEDIATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The schedule_type of this Job.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this Job.
        The schedule type of the job.


        :param schedule_type: The schedule_type of this Job.
        :type: str
        """
        allowed_values = ["IMMEDIATE"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            schedule_type = 'UNKNOWN_ENUM_VALUE'
        self._schedule_type = schedule_type

    @property
    def job_type(self):
        """
        **[Required]** Gets the job_type of this Job.
        The type of job.

        Allowed values for this property are: "SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_type of this Job.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this Job.
        The type of job.


        :param job_type: The job_type of this Job.
        :type: str
        """
        allowed_values = ["SQL"]
        if not value_allowed_none_or_none_sentinel(job_type, allowed_values):
            job_type = 'UNKNOWN_ENUM_VALUE'
        self._job_type = job_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Job.
        The lifecycle state of the job.

        Allowed values for this property are: "ACTIVE", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Job.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Job.
        The lifecycle state of the job.


        :param lifecycle_state: The lifecycle_state of this Job.
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def timeout(self):
        """
        Gets the timeout of this Job.
        The job timeout duration, which is expressed like \"1h 10m 15s\".


        :return: The timeout of this Job.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this Job.
        The job timeout duration, which is expressed like \"1h 10m 15s\".


        :param timeout: The timeout of this Job.
        :type: str
        """
        self._timeout = timeout

    @property
    def result_location(self):
        """
        Gets the result_location of this Job.

        :return: The result_location of this Job.
        :rtype: oci.database_management.models.JobExecutionResultLocation
        """
        return self._result_location

    @result_location.setter
    def result_location(self, result_location):
        """
        Sets the result_location of this Job.

        :param result_location: The result_location of this Job.
        :type: oci.database_management.models.JobExecutionResultLocation
        """
        self._result_location = result_location

    @property
    def submission_error_message(self):
        """
        Gets the submission_error_message of this Job.
        The error message that is returned if the job submission fails. Null is returned in all other scenarios.


        :return: The submission_error_message of this Job.
        :rtype: str
        """
        return self._submission_error_message

    @submission_error_message.setter
    def submission_error_message(self, submission_error_message):
        """
        Sets the submission_error_message of this Job.
        The error message that is returned if the job submission fails. Null is returned in all other scenarios.


        :param submission_error_message: The submission_error_message of this Job.
        :type: str
        """
        self._submission_error_message = submission_error_message

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Job.
        The date and time when the job was created.


        :return: The time_created of this Job.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Job.
        The date and time when the job was created.


        :param time_created: The time_created of this Job.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Job.
        The date and time when the job was last updated.


        :return: The time_updated of this Job.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Job.
        The date and time when the job was last updated.


        :param time_updated: The time_updated of this Job.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
