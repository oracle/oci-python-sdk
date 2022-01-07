# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlBucket(object):
    """
    Sql bucket type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlBucket object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this SqlBucket.
        :type version: float

        :param database_type:
            The value to assign to the database_type property of this SqlBucket.
        :type database_type: str

        :param time_collected:
            The value to assign to the time_collected property of this SqlBucket.
        :type time_collected: datetime

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlBucket.
        :type sql_identifier: str

        :param plan_hash:
            The value to assign to the plan_hash property of this SqlBucket.
        :type plan_hash: int

        :param bucket_id:
            The value to assign to the bucket_id property of this SqlBucket.
        :type bucket_id: str

        :param executions_count:
            The value to assign to the executions_count property of this SqlBucket.
        :type executions_count: int

        :param cpu_time_in_sec:
            The value to assign to the cpu_time_in_sec property of this SqlBucket.
        :type cpu_time_in_sec: float

        :param io_time_in_sec:
            The value to assign to the io_time_in_sec property of this SqlBucket.
        :type io_time_in_sec: float

        :param other_wait_time_in_sec:
            The value to assign to the other_wait_time_in_sec property of this SqlBucket.
        :type other_wait_time_in_sec: float

        :param total_time_in_sec:
            The value to assign to the total_time_in_sec property of this SqlBucket.
        :type total_time_in_sec: float

        """
        self.swagger_types = {
            'version': 'float',
            'database_type': 'str',
            'time_collected': 'datetime',
            'sql_identifier': 'str',
            'plan_hash': 'int',
            'bucket_id': 'str',
            'executions_count': 'int',
            'cpu_time_in_sec': 'float',
            'io_time_in_sec': 'float',
            'other_wait_time_in_sec': 'float',
            'total_time_in_sec': 'float'
        }

        self.attribute_map = {
            'version': 'version',
            'database_type': 'databaseType',
            'time_collected': 'timeCollected',
            'sql_identifier': 'sqlIdentifier',
            'plan_hash': 'planHash',
            'bucket_id': 'bucketId',
            'executions_count': 'executionsCount',
            'cpu_time_in_sec': 'cpuTimeInSec',
            'io_time_in_sec': 'ioTimeInSec',
            'other_wait_time_in_sec': 'otherWaitTimeInSec',
            'total_time_in_sec': 'totalTimeInSec'
        }

        self._version = None
        self._database_type = None
        self._time_collected = None
        self._sql_identifier = None
        self._plan_hash = None
        self._bucket_id = None
        self._executions_count = None
        self._cpu_time_in_sec = None
        self._io_time_in_sec = None
        self._other_wait_time_in_sec = None
        self._total_time_in_sec = None

    @property
    def version(self):
        """
        Gets the version of this SqlBucket.
        Version
        Example: `1`


        :return: The version of this SqlBucket.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SqlBucket.
        Version
        Example: `1`


        :param version: The version of this SqlBucket.
        :type: float
        """
        self._version = version

    @property
    def database_type(self):
        """
        Gets the database_type of this SqlBucket.
        Operations Insights internal representation of the database type.


        :return: The database_type of this SqlBucket.
        :rtype: str
        """
        return self._database_type

    @database_type.setter
    def database_type(self, database_type):
        """
        Sets the database_type of this SqlBucket.
        Operations Insights internal representation of the database type.


        :param database_type: The database_type of this SqlBucket.
        :type: str
        """
        self._database_type = database_type

    @property
    def time_collected(self):
        """
        **[Required]** Gets the time_collected of this SqlBucket.
        Collection timestamp
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :return: The time_collected of this SqlBucket.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this SqlBucket.
        Collection timestamp
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :param time_collected: The time_collected of this SqlBucket.
        :type: datetime
        """
        self._time_collected = time_collected

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlBucket.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlBucket.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlBucket.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlBucket.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def plan_hash(self):
        """
        **[Required]** Gets the plan_hash of this SqlBucket.
        Plan hash value for the SQL Execution Plan


        :return: The plan_hash of this SqlBucket.
        :rtype: int
        """
        return self._plan_hash

    @plan_hash.setter
    def plan_hash(self, plan_hash):
        """
        Sets the plan_hash of this SqlBucket.
        Plan hash value for the SQL Execution Plan


        :param plan_hash: The plan_hash of this SqlBucket.
        :type: int
        """
        self._plan_hash = plan_hash

    @property
    def bucket_id(self):
        """
        **[Required]** Gets the bucket_id of this SqlBucket.
        SQL Bucket ID, examples <= 3 secs, 3-10 secs, 10-60 secs, 1-5 min, > 5 min
        Example: `\"<= 3 secs\"`


        :return: The bucket_id of this SqlBucket.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """
        Sets the bucket_id of this SqlBucket.
        SQL Bucket ID, examples <= 3 secs, 3-10 secs, 10-60 secs, 1-5 min, > 5 min
        Example: `\"<= 3 secs\"`


        :param bucket_id: The bucket_id of this SqlBucket.
        :type: str
        """
        self._bucket_id = bucket_id

    @property
    def executions_count(self):
        """
        Gets the executions_count of this SqlBucket.
        Total number of executions
        Example: `60`


        :return: The executions_count of this SqlBucket.
        :rtype: int
        """
        return self._executions_count

    @executions_count.setter
    def executions_count(self, executions_count):
        """
        Sets the executions_count of this SqlBucket.
        Total number of executions
        Example: `60`


        :param executions_count: The executions_count of this SqlBucket.
        :type: int
        """
        self._executions_count = executions_count

    @property
    def cpu_time_in_sec(self):
        """
        Gets the cpu_time_in_sec of this SqlBucket.
        Total CPU time
        Example: `1046`


        :return: The cpu_time_in_sec of this SqlBucket.
        :rtype: float
        """
        return self._cpu_time_in_sec

    @cpu_time_in_sec.setter
    def cpu_time_in_sec(self, cpu_time_in_sec):
        """
        Sets the cpu_time_in_sec of this SqlBucket.
        Total CPU time
        Example: `1046`


        :param cpu_time_in_sec: The cpu_time_in_sec of this SqlBucket.
        :type: float
        """
        self._cpu_time_in_sec = cpu_time_in_sec

    @property
    def io_time_in_sec(self):
        """
        Gets the io_time_in_sec of this SqlBucket.
        Total IO time
        Example: `5810`


        :return: The io_time_in_sec of this SqlBucket.
        :rtype: float
        """
        return self._io_time_in_sec

    @io_time_in_sec.setter
    def io_time_in_sec(self, io_time_in_sec):
        """
        Sets the io_time_in_sec of this SqlBucket.
        Total IO time
        Example: `5810`


        :param io_time_in_sec: The io_time_in_sec of this SqlBucket.
        :type: float
        """
        self._io_time_in_sec = io_time_in_sec

    @property
    def other_wait_time_in_sec(self):
        """
        Gets the other_wait_time_in_sec of this SqlBucket.
        Total other wait time
        Example: `24061`


        :return: The other_wait_time_in_sec of this SqlBucket.
        :rtype: float
        """
        return self._other_wait_time_in_sec

    @other_wait_time_in_sec.setter
    def other_wait_time_in_sec(self, other_wait_time_in_sec):
        """
        Sets the other_wait_time_in_sec of this SqlBucket.
        Total other wait time
        Example: `24061`


        :param other_wait_time_in_sec: The other_wait_time_in_sec of this SqlBucket.
        :type: float
        """
        self._other_wait_time_in_sec = other_wait_time_in_sec

    @property
    def total_time_in_sec(self):
        """
        Gets the total_time_in_sec of this SqlBucket.
        Total time
        Example: `30917`


        :return: The total_time_in_sec of this SqlBucket.
        :rtype: float
        """
        return self._total_time_in_sec

    @total_time_in_sec.setter
    def total_time_in_sec(self, total_time_in_sec):
        """
        Sets the total_time_in_sec of this SqlBucket.
        Total time
        Example: `30917`


        :param total_time_in_sec: The total_time_in_sec of this SqlBucket.
        :type: float
        """
        self._total_time_in_sec = total_time_in_sec

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
