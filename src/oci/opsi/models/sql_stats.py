# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlStats(object):
    """
    Sql Stats type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlStats object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_identifier:
            The value to assign to the sql_identifier property of this SqlStats.
        :type sql_identifier: str

        :param plan_hash_value:
            The value to assign to the plan_hash_value property of this SqlStats.
        :type plan_hash_value: int

        :param time_collected:
            The value to assign to the time_collected property of this SqlStats.
        :type time_collected: datetime

        :param instance_name:
            The value to assign to the instance_name property of this SqlStats.
        :type instance_name: str

        :param last_active_time:
            The value to assign to the last_active_time property of this SqlStats.
        :type last_active_time: str

        :param parse_calls:
            The value to assign to the parse_calls property of this SqlStats.
        :type parse_calls: int

        :param disk_reads:
            The value to assign to the disk_reads property of this SqlStats.
        :type disk_reads: int

        :param direct_reads:
            The value to assign to the direct_reads property of this SqlStats.
        :type direct_reads: int

        :param direct_writes:
            The value to assign to the direct_writes property of this SqlStats.
        :type direct_writes: int

        :param buffer_gets:
            The value to assign to the buffer_gets property of this SqlStats.
        :type buffer_gets: int

        :param rows_processed:
            The value to assign to the rows_processed property of this SqlStats.
        :type rows_processed: int

        :param serializable_aborts:
            The value to assign to the serializable_aborts property of this SqlStats.
        :type serializable_aborts: int

        :param fetches:
            The value to assign to the fetches property of this SqlStats.
        :type fetches: int

        :param executions:
            The value to assign to the executions property of this SqlStats.
        :type executions: int

        :param avoided_executions:
            The value to assign to the avoided_executions property of this SqlStats.
        :type avoided_executions: int

        :param end_of_fetch_count:
            The value to assign to the end_of_fetch_count property of this SqlStats.
        :type end_of_fetch_count: int

        :param loads:
            The value to assign to the loads property of this SqlStats.
        :type loads: int

        :param version_count:
            The value to assign to the version_count property of this SqlStats.
        :type version_count: int

        :param invalidations:
            The value to assign to the invalidations property of this SqlStats.
        :type invalidations: int

        :param obsolete_count:
            The value to assign to the obsolete_count property of this SqlStats.
        :type obsolete_count: int

        :param px_servers_executions:
            The value to assign to the px_servers_executions property of this SqlStats.
        :type px_servers_executions: int

        :param cpu_time_in_us:
            The value to assign to the cpu_time_in_us property of this SqlStats.
        :type cpu_time_in_us: int

        :param elapsed_time_in_us:
            The value to assign to the elapsed_time_in_us property of this SqlStats.
        :type elapsed_time_in_us: int

        :param avg_hard_parse_time_in_us:
            The value to assign to the avg_hard_parse_time_in_us property of this SqlStats.
        :type avg_hard_parse_time_in_us: int

        :param concurrency_wait_time_in_us:
            The value to assign to the concurrency_wait_time_in_us property of this SqlStats.
        :type concurrency_wait_time_in_us: int

        :param application_wait_time_in_us:
            The value to assign to the application_wait_time_in_us property of this SqlStats.
        :type application_wait_time_in_us: int

        :param cluster_wait_time_in_us:
            The value to assign to the cluster_wait_time_in_us property of this SqlStats.
        :type cluster_wait_time_in_us: int

        :param user_io_wait_time_in_us:
            The value to assign to the user_io_wait_time_in_us property of this SqlStats.
        :type user_io_wait_time_in_us: int

        :param plsql_exec_time_in_us:
            The value to assign to the plsql_exec_time_in_us property of this SqlStats.
        :type plsql_exec_time_in_us: int

        :param java_exec_time_in_us:
            The value to assign to the java_exec_time_in_us property of this SqlStats.
        :type java_exec_time_in_us: int

        :param sorts:
            The value to assign to the sorts property of this SqlStats.
        :type sorts: int

        :param sharable_mem:
            The value to assign to the sharable_mem property of this SqlStats.
        :type sharable_mem: int

        :param total_sharable_mem:
            The value to assign to the total_sharable_mem property of this SqlStats.
        :type total_sharable_mem: int

        :param type_check_mem:
            The value to assign to the type_check_mem property of this SqlStats.
        :type type_check_mem: int

        :param io_cell_offload_eligible_bytes:
            The value to assign to the io_cell_offload_eligible_bytes property of this SqlStats.
        :type io_cell_offload_eligible_bytes: int

        :param io_interconnect_bytes:
            The value to assign to the io_interconnect_bytes property of this SqlStats.
        :type io_interconnect_bytes: int

        :param physical_read_requests:
            The value to assign to the physical_read_requests property of this SqlStats.
        :type physical_read_requests: int

        :param physical_read_bytes:
            The value to assign to the physical_read_bytes property of this SqlStats.
        :type physical_read_bytes: int

        :param physical_write_requests:
            The value to assign to the physical_write_requests property of this SqlStats.
        :type physical_write_requests: int

        :param physical_write_bytes:
            The value to assign to the physical_write_bytes property of this SqlStats.
        :type physical_write_bytes: int

        :param exact_matching_signature:
            The value to assign to the exact_matching_signature property of this SqlStats.
        :type exact_matching_signature: str

        :param force_matching_signature:
            The value to assign to the force_matching_signature property of this SqlStats.
        :type force_matching_signature: str

        :param io_cell_uncompressed_bytes:
            The value to assign to the io_cell_uncompressed_bytes property of this SqlStats.
        :type io_cell_uncompressed_bytes: int

        :param io_cell_offload_returned_bytes:
            The value to assign to the io_cell_offload_returned_bytes property of this SqlStats.
        :type io_cell_offload_returned_bytes: int

        :param child_number:
            The value to assign to the child_number property of this SqlStats.
        :type child_number: int

        :param command_type:
            The value to assign to the command_type property of this SqlStats.
        :type command_type: int

        :param users_opening:
            The value to assign to the users_opening property of this SqlStats.
        :type users_opening: int

        :param users_executing:
            The value to assign to the users_executing property of this SqlStats.
        :type users_executing: int

        :param optimizer_cost:
            The value to assign to the optimizer_cost property of this SqlStats.
        :type optimizer_cost: int

        :param full_plan_hash_value:
            The value to assign to the full_plan_hash_value property of this SqlStats.
        :type full_plan_hash_value: str

        :param module:
            The value to assign to the module property of this SqlStats.
        :type module: str

        :param service:
            The value to assign to the service property of this SqlStats.
        :type service: str

        :param action:
            The value to assign to the action property of this SqlStats.
        :type action: str

        :param sql_profile:
            The value to assign to the sql_profile property of this SqlStats.
        :type sql_profile: str

        :param sql_patch:
            The value to assign to the sql_patch property of this SqlStats.
        :type sql_patch: str

        :param sql_plan_baseline:
            The value to assign to the sql_plan_baseline property of this SqlStats.
        :type sql_plan_baseline: str

        :param delta_execution_count:
            The value to assign to the delta_execution_count property of this SqlStats.
        :type delta_execution_count: int

        :param delta_cpu_time:
            The value to assign to the delta_cpu_time property of this SqlStats.
        :type delta_cpu_time: int

        :param delta_io_bytes:
            The value to assign to the delta_io_bytes property of this SqlStats.
        :type delta_io_bytes: int

        :param delta_cpu_rank:
            The value to assign to the delta_cpu_rank property of this SqlStats.
        :type delta_cpu_rank: int

        :param delta_execs_rank:
            The value to assign to the delta_execs_rank property of this SqlStats.
        :type delta_execs_rank: int

        :param sharable_mem_rank:
            The value to assign to the sharable_mem_rank property of this SqlStats.
        :type sharable_mem_rank: int

        :param delta_io_rank:
            The value to assign to the delta_io_rank property of this SqlStats.
        :type delta_io_rank: int

        :param harmonic_sum:
            The value to assign to the harmonic_sum property of this SqlStats.
        :type harmonic_sum: int

        :param wt_harmonic_sum:
            The value to assign to the wt_harmonic_sum property of this SqlStats.
        :type wt_harmonic_sum: int

        :param total_sql_count:
            The value to assign to the total_sql_count property of this SqlStats.
        :type total_sql_count: int

        """
        self.swagger_types = {
            'sql_identifier': 'str',
            'plan_hash_value': 'int',
            'time_collected': 'datetime',
            'instance_name': 'str',
            'last_active_time': 'str',
            'parse_calls': 'int',
            'disk_reads': 'int',
            'direct_reads': 'int',
            'direct_writes': 'int',
            'buffer_gets': 'int',
            'rows_processed': 'int',
            'serializable_aborts': 'int',
            'fetches': 'int',
            'executions': 'int',
            'avoided_executions': 'int',
            'end_of_fetch_count': 'int',
            'loads': 'int',
            'version_count': 'int',
            'invalidations': 'int',
            'obsolete_count': 'int',
            'px_servers_executions': 'int',
            'cpu_time_in_us': 'int',
            'elapsed_time_in_us': 'int',
            'avg_hard_parse_time_in_us': 'int',
            'concurrency_wait_time_in_us': 'int',
            'application_wait_time_in_us': 'int',
            'cluster_wait_time_in_us': 'int',
            'user_io_wait_time_in_us': 'int',
            'plsql_exec_time_in_us': 'int',
            'java_exec_time_in_us': 'int',
            'sorts': 'int',
            'sharable_mem': 'int',
            'total_sharable_mem': 'int',
            'type_check_mem': 'int',
            'io_cell_offload_eligible_bytes': 'int',
            'io_interconnect_bytes': 'int',
            'physical_read_requests': 'int',
            'physical_read_bytes': 'int',
            'physical_write_requests': 'int',
            'physical_write_bytes': 'int',
            'exact_matching_signature': 'str',
            'force_matching_signature': 'str',
            'io_cell_uncompressed_bytes': 'int',
            'io_cell_offload_returned_bytes': 'int',
            'child_number': 'int',
            'command_type': 'int',
            'users_opening': 'int',
            'users_executing': 'int',
            'optimizer_cost': 'int',
            'full_plan_hash_value': 'str',
            'module': 'str',
            'service': 'str',
            'action': 'str',
            'sql_profile': 'str',
            'sql_patch': 'str',
            'sql_plan_baseline': 'str',
            'delta_execution_count': 'int',
            'delta_cpu_time': 'int',
            'delta_io_bytes': 'int',
            'delta_cpu_rank': 'int',
            'delta_execs_rank': 'int',
            'sharable_mem_rank': 'int',
            'delta_io_rank': 'int',
            'harmonic_sum': 'int',
            'wt_harmonic_sum': 'int',
            'total_sql_count': 'int'
        }

        self.attribute_map = {
            'sql_identifier': 'sqlIdentifier',
            'plan_hash_value': 'planHashValue',
            'time_collected': 'timeCollected',
            'instance_name': 'instanceName',
            'last_active_time': 'lastActiveTime',
            'parse_calls': 'parseCalls',
            'disk_reads': 'diskReads',
            'direct_reads': 'directReads',
            'direct_writes': 'directWrites',
            'buffer_gets': 'bufferGets',
            'rows_processed': 'rowsProcessed',
            'serializable_aborts': 'serializableAborts',
            'fetches': 'fetches',
            'executions': 'executions',
            'avoided_executions': 'avoidedExecutions',
            'end_of_fetch_count': 'endOfFetchCount',
            'loads': 'loads',
            'version_count': 'versionCount',
            'invalidations': 'invalidations',
            'obsolete_count': 'obsoleteCount',
            'px_servers_executions': 'pxServersExecutions',
            'cpu_time_in_us': 'cpuTimeInUs',
            'elapsed_time_in_us': 'elapsedTimeInUs',
            'avg_hard_parse_time_in_us': 'avgHardParseTimeInUs',
            'concurrency_wait_time_in_us': 'concurrencyWaitTimeInUs',
            'application_wait_time_in_us': 'applicationWaitTimeInUs',
            'cluster_wait_time_in_us': 'clusterWaitTimeInUs',
            'user_io_wait_time_in_us': 'userIoWaitTimeInUs',
            'plsql_exec_time_in_us': 'plsqlExecTimeInUs',
            'java_exec_time_in_us': 'javaExecTimeInUs',
            'sorts': 'sorts',
            'sharable_mem': 'sharableMem',
            'total_sharable_mem': 'totalSharableMem',
            'type_check_mem': 'typeCheckMem',
            'io_cell_offload_eligible_bytes': 'ioCellOffloadEligibleBytes',
            'io_interconnect_bytes': 'ioInterconnectBytes',
            'physical_read_requests': 'physicalReadRequests',
            'physical_read_bytes': 'physicalReadBytes',
            'physical_write_requests': 'physicalWriteRequests',
            'physical_write_bytes': 'physicalWriteBytes',
            'exact_matching_signature': 'exactMatchingSignature',
            'force_matching_signature': 'forceMatchingSignature',
            'io_cell_uncompressed_bytes': 'ioCellUncompressedBytes',
            'io_cell_offload_returned_bytes': 'ioCellOffloadReturnedBytes',
            'child_number': 'childNumber',
            'command_type': 'commandType',
            'users_opening': 'usersOpening',
            'users_executing': 'usersExecuting',
            'optimizer_cost': 'optimizerCost',
            'full_plan_hash_value': 'fullPlanHashValue',
            'module': 'module',
            'service': 'service',
            'action': 'action',
            'sql_profile': 'sqlProfile',
            'sql_patch': 'sqlPatch',
            'sql_plan_baseline': 'sqlPlanBaseline',
            'delta_execution_count': 'deltaExecutionCount',
            'delta_cpu_time': 'deltaCpuTime',
            'delta_io_bytes': 'deltaIoBytes',
            'delta_cpu_rank': 'deltaCpuRank',
            'delta_execs_rank': 'deltaExecsRank',
            'sharable_mem_rank': 'sharableMemRank',
            'delta_io_rank': 'deltaIoRank',
            'harmonic_sum': 'harmonicSum',
            'wt_harmonic_sum': 'wtHarmonicSum',
            'total_sql_count': 'totalSqlCount'
        }

        self._sql_identifier = None
        self._plan_hash_value = None
        self._time_collected = None
        self._instance_name = None
        self._last_active_time = None
        self._parse_calls = None
        self._disk_reads = None
        self._direct_reads = None
        self._direct_writes = None
        self._buffer_gets = None
        self._rows_processed = None
        self._serializable_aborts = None
        self._fetches = None
        self._executions = None
        self._avoided_executions = None
        self._end_of_fetch_count = None
        self._loads = None
        self._version_count = None
        self._invalidations = None
        self._obsolete_count = None
        self._px_servers_executions = None
        self._cpu_time_in_us = None
        self._elapsed_time_in_us = None
        self._avg_hard_parse_time_in_us = None
        self._concurrency_wait_time_in_us = None
        self._application_wait_time_in_us = None
        self._cluster_wait_time_in_us = None
        self._user_io_wait_time_in_us = None
        self._plsql_exec_time_in_us = None
        self._java_exec_time_in_us = None
        self._sorts = None
        self._sharable_mem = None
        self._total_sharable_mem = None
        self._type_check_mem = None
        self._io_cell_offload_eligible_bytes = None
        self._io_interconnect_bytes = None
        self._physical_read_requests = None
        self._physical_read_bytes = None
        self._physical_write_requests = None
        self._physical_write_bytes = None
        self._exact_matching_signature = None
        self._force_matching_signature = None
        self._io_cell_uncompressed_bytes = None
        self._io_cell_offload_returned_bytes = None
        self._child_number = None
        self._command_type = None
        self._users_opening = None
        self._users_executing = None
        self._optimizer_cost = None
        self._full_plan_hash_value = None
        self._module = None
        self._service = None
        self._action = None
        self._sql_profile = None
        self._sql_patch = None
        self._sql_plan_baseline = None
        self._delta_execution_count = None
        self._delta_cpu_time = None
        self._delta_io_bytes = None
        self._delta_cpu_rank = None
        self._delta_execs_rank = None
        self._sharable_mem_rank = None
        self._delta_io_rank = None
        self._harmonic_sum = None
        self._wt_harmonic_sum = None
        self._total_sql_count = None

    @property
    def sql_identifier(self):
        """
        **[Required]** Gets the sql_identifier of this SqlStats.
        Unique SQL_ID for a SQL Statement.


        :return: The sql_identifier of this SqlStats.
        :rtype: str
        """
        return self._sql_identifier

    @sql_identifier.setter
    def sql_identifier(self, sql_identifier):
        """
        Sets the sql_identifier of this SqlStats.
        Unique SQL_ID for a SQL Statement.


        :param sql_identifier: The sql_identifier of this SqlStats.
        :type: str
        """
        self._sql_identifier = sql_identifier

    @property
    def plan_hash_value(self):
        """
        **[Required]** Gets the plan_hash_value of this SqlStats.
        Plan hash value for the SQL Execution Plan


        :return: The plan_hash_value of this SqlStats.
        :rtype: int
        """
        return self._plan_hash_value

    @plan_hash_value.setter
    def plan_hash_value(self, plan_hash_value):
        """
        Sets the plan_hash_value of this SqlStats.
        Plan hash value for the SQL Execution Plan


        :param plan_hash_value: The plan_hash_value of this SqlStats.
        :type: int
        """
        self._plan_hash_value = plan_hash_value

    @property
    def time_collected(self):
        """
        **[Required]** Gets the time_collected of this SqlStats.
        Collection timestamp
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :return: The time_collected of this SqlStats.
        :rtype: datetime
        """
        return self._time_collected

    @time_collected.setter
    def time_collected(self, time_collected):
        """
        Sets the time_collected of this SqlStats.
        Collection timestamp
        Example: `\"2020-03-31T00:00:00.000Z\"`


        :param time_collected: The time_collected of this SqlStats.
        :type: datetime
        """
        self._time_collected = time_collected

    @property
    def instance_name(self):
        """
        **[Required]** Gets the instance_name of this SqlStats.
        Name of Database Instance
        Example: `\"DB10902_1\"`


        :return: The instance_name of this SqlStats.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this SqlStats.
        Name of Database Instance
        Example: `\"DB10902_1\"`


        :param instance_name: The instance_name of this SqlStats.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def last_active_time(self):
        """
        Gets the last_active_time of this SqlStats.
        last_active_time
        Example: `\"0000000099CCE300\"`


        :return: The last_active_time of this SqlStats.
        :rtype: str
        """
        return self._last_active_time

    @last_active_time.setter
    def last_active_time(self, last_active_time):
        """
        Sets the last_active_time of this SqlStats.
        last_active_time
        Example: `\"0000000099CCE300\"`


        :param last_active_time: The last_active_time of this SqlStats.
        :type: str
        """
        self._last_active_time = last_active_time

    @property
    def parse_calls(self):
        """
        Gets the parse_calls of this SqlStats.
        Total integer of parse calls
         Example: `60`


        :return: The parse_calls of this SqlStats.
        :rtype: int
        """
        return self._parse_calls

    @parse_calls.setter
    def parse_calls(self, parse_calls):
        """
        Sets the parse_calls of this SqlStats.
        Total integer of parse calls
         Example: `60`


        :param parse_calls: The parse_calls of this SqlStats.
        :type: int
        """
        self._parse_calls = parse_calls

    @property
    def disk_reads(self):
        """
        Gets the disk_reads of this SqlStats.
        Number of disk reads


        :return: The disk_reads of this SqlStats.
        :rtype: int
        """
        return self._disk_reads

    @disk_reads.setter
    def disk_reads(self, disk_reads):
        """
        Sets the disk_reads of this SqlStats.
        Number of disk reads


        :param disk_reads: The disk_reads of this SqlStats.
        :type: int
        """
        self._disk_reads = disk_reads

    @property
    def direct_reads(self):
        """
        Gets the direct_reads of this SqlStats.
        Number of direct reads


        :return: The direct_reads of this SqlStats.
        :rtype: int
        """
        return self._direct_reads

    @direct_reads.setter
    def direct_reads(self, direct_reads):
        """
        Sets the direct_reads of this SqlStats.
        Number of direct reads


        :param direct_reads: The direct_reads of this SqlStats.
        :type: int
        """
        self._direct_reads = direct_reads

    @property
    def direct_writes(self):
        """
        Gets the direct_writes of this SqlStats.
        Number of Direct writes


        :return: The direct_writes of this SqlStats.
        :rtype: int
        """
        return self._direct_writes

    @direct_writes.setter
    def direct_writes(self, direct_writes):
        """
        Sets the direct_writes of this SqlStats.
        Number of Direct writes


        :param direct_writes: The direct_writes of this SqlStats.
        :type: int
        """
        self._direct_writes = direct_writes

    @property
    def buffer_gets(self):
        """
        Gets the buffer_gets of this SqlStats.
        Number of Buffer Gets


        :return: The buffer_gets of this SqlStats.
        :rtype: int
        """
        return self._buffer_gets

    @buffer_gets.setter
    def buffer_gets(self, buffer_gets):
        """
        Sets the buffer_gets of this SqlStats.
        Number of Buffer Gets


        :param buffer_gets: The buffer_gets of this SqlStats.
        :type: int
        """
        self._buffer_gets = buffer_gets

    @property
    def rows_processed(self):
        """
        Gets the rows_processed of this SqlStats.
        Number of row processed


        :return: The rows_processed of this SqlStats.
        :rtype: int
        """
        return self._rows_processed

    @rows_processed.setter
    def rows_processed(self, rows_processed):
        """
        Sets the rows_processed of this SqlStats.
        Number of row processed


        :param rows_processed: The rows_processed of this SqlStats.
        :type: int
        """
        self._rows_processed = rows_processed

    @property
    def serializable_aborts(self):
        """
        Gets the serializable_aborts of this SqlStats.
        Number of serializable aborts


        :return: The serializable_aborts of this SqlStats.
        :rtype: int
        """
        return self._serializable_aborts

    @serializable_aborts.setter
    def serializable_aborts(self, serializable_aborts):
        """
        Sets the serializable_aborts of this SqlStats.
        Number of serializable aborts


        :param serializable_aborts: The serializable_aborts of this SqlStats.
        :type: int
        """
        self._serializable_aborts = serializable_aborts

    @property
    def fetches(self):
        """
        Gets the fetches of this SqlStats.
        Number of fetches


        :return: The fetches of this SqlStats.
        :rtype: int
        """
        return self._fetches

    @fetches.setter
    def fetches(self, fetches):
        """
        Sets the fetches of this SqlStats.
        Number of fetches


        :param fetches: The fetches of this SqlStats.
        :type: int
        """
        self._fetches = fetches

    @property
    def executions(self):
        """
        Gets the executions of this SqlStats.
        Number of executions


        :return: The executions of this SqlStats.
        :rtype: int
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        """
        Sets the executions of this SqlStats.
        Number of executions


        :param executions: The executions of this SqlStats.
        :type: int
        """
        self._executions = executions

    @property
    def avoided_executions(self):
        """
        Gets the avoided_executions of this SqlStats.
        Number of executions attempted on this object, but prevented due to the SQL statement being in quarantine


        :return: The avoided_executions of this SqlStats.
        :rtype: int
        """
        return self._avoided_executions

    @avoided_executions.setter
    def avoided_executions(self, avoided_executions):
        """
        Sets the avoided_executions of this SqlStats.
        Number of executions attempted on this object, but prevented due to the SQL statement being in quarantine


        :param avoided_executions: The avoided_executions of this SqlStats.
        :type: int
        """
        self._avoided_executions = avoided_executions

    @property
    def end_of_fetch_count(self):
        """
        Gets the end_of_fetch_count of this SqlStats.
        Number of times this cursor was fully executed since the cursor was brought into the library cache


        :return: The end_of_fetch_count of this SqlStats.
        :rtype: int
        """
        return self._end_of_fetch_count

    @end_of_fetch_count.setter
    def end_of_fetch_count(self, end_of_fetch_count):
        """
        Sets the end_of_fetch_count of this SqlStats.
        Number of times this cursor was fully executed since the cursor was brought into the library cache


        :param end_of_fetch_count: The end_of_fetch_count of this SqlStats.
        :type: int
        """
        self._end_of_fetch_count = end_of_fetch_count

    @property
    def loads(self):
        """
        Gets the loads of this SqlStats.
        Number of times the object was either loaded or reloaded


        :return: The loads of this SqlStats.
        :rtype: int
        """
        return self._loads

    @loads.setter
    def loads(self, loads):
        """
        Sets the loads of this SqlStats.
        Number of times the object was either loaded or reloaded


        :param loads: The loads of this SqlStats.
        :type: int
        """
        self._loads = loads

    @property
    def version_count(self):
        """
        Gets the version_count of this SqlStats.
        Number of cursors present in the cache with this SQL text and plan


        :return: The version_count of this SqlStats.
        :rtype: int
        """
        return self._version_count

    @version_count.setter
    def version_count(self, version_count):
        """
        Sets the version_count of this SqlStats.
        Number of cursors present in the cache with this SQL text and plan


        :param version_count: The version_count of this SqlStats.
        :type: int
        """
        self._version_count = version_count

    @property
    def invalidations(self):
        """
        Gets the invalidations of this SqlStats.
        Number of times this child cursor has been invalidated


        :return: The invalidations of this SqlStats.
        :rtype: int
        """
        return self._invalidations

    @invalidations.setter
    def invalidations(self, invalidations):
        """
        Sets the invalidations of this SqlStats.
        Number of times this child cursor has been invalidated


        :param invalidations: The invalidations of this SqlStats.
        :type: int
        """
        self._invalidations = invalidations

    @property
    def obsolete_count(self):
        """
        Gets the obsolete_count of this SqlStats.
        Number of times that a parent cursor became obsolete


        :return: The obsolete_count of this SqlStats.
        :rtype: int
        """
        return self._obsolete_count

    @obsolete_count.setter
    def obsolete_count(self, obsolete_count):
        """
        Sets the obsolete_count of this SqlStats.
        Number of times that a parent cursor became obsolete


        :param obsolete_count: The obsolete_count of this SqlStats.
        :type: int
        """
        self._obsolete_count = obsolete_count

    @property
    def px_servers_executions(self):
        """
        Gets the px_servers_executions of this SqlStats.
        Total number of executions performed by parallel execution servers (0 when the statement has never been executed in parallel)


        :return: The px_servers_executions of this SqlStats.
        :rtype: int
        """
        return self._px_servers_executions

    @px_servers_executions.setter
    def px_servers_executions(self, px_servers_executions):
        """
        Sets the px_servers_executions of this SqlStats.
        Total number of executions performed by parallel execution servers (0 when the statement has never been executed in parallel)


        :param px_servers_executions: The px_servers_executions of this SqlStats.
        :type: int
        """
        self._px_servers_executions = px_servers_executions

    @property
    def cpu_time_in_us(self):
        """
        Gets the cpu_time_in_us of this SqlStats.
        CPU time (in microseconds) used by this cursor for parsing, executing, and fetching


        :return: The cpu_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._cpu_time_in_us

    @cpu_time_in_us.setter
    def cpu_time_in_us(self, cpu_time_in_us):
        """
        Sets the cpu_time_in_us of this SqlStats.
        CPU time (in microseconds) used by this cursor for parsing, executing, and fetching


        :param cpu_time_in_us: The cpu_time_in_us of this SqlStats.
        :type: int
        """
        self._cpu_time_in_us = cpu_time_in_us

    @property
    def elapsed_time_in_us(self):
        """
        Gets the elapsed_time_in_us of this SqlStats.
        Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching.


        :return: The elapsed_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._elapsed_time_in_us

    @elapsed_time_in_us.setter
    def elapsed_time_in_us(self, elapsed_time_in_us):
        """
        Sets the elapsed_time_in_us of this SqlStats.
        Elapsed time (in microseconds) used by this cursor for parsing, executing, and fetching.


        :param elapsed_time_in_us: The elapsed_time_in_us of this SqlStats.
        :type: int
        """
        self._elapsed_time_in_us = elapsed_time_in_us

    @property
    def avg_hard_parse_time_in_us(self):
        """
        Gets the avg_hard_parse_time_in_us of this SqlStats.
        Average hard parse time (in microseconds) used by this cursor


        :return: The avg_hard_parse_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._avg_hard_parse_time_in_us

    @avg_hard_parse_time_in_us.setter
    def avg_hard_parse_time_in_us(self, avg_hard_parse_time_in_us):
        """
        Sets the avg_hard_parse_time_in_us of this SqlStats.
        Average hard parse time (in microseconds) used by this cursor


        :param avg_hard_parse_time_in_us: The avg_hard_parse_time_in_us of this SqlStats.
        :type: int
        """
        self._avg_hard_parse_time_in_us = avg_hard_parse_time_in_us

    @property
    def concurrency_wait_time_in_us(self):
        """
        Gets the concurrency_wait_time_in_us of this SqlStats.
        Concurrency wait time (in microseconds)


        :return: The concurrency_wait_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._concurrency_wait_time_in_us

    @concurrency_wait_time_in_us.setter
    def concurrency_wait_time_in_us(self, concurrency_wait_time_in_us):
        """
        Sets the concurrency_wait_time_in_us of this SqlStats.
        Concurrency wait time (in microseconds)


        :param concurrency_wait_time_in_us: The concurrency_wait_time_in_us of this SqlStats.
        :type: int
        """
        self._concurrency_wait_time_in_us = concurrency_wait_time_in_us

    @property
    def application_wait_time_in_us(self):
        """
        Gets the application_wait_time_in_us of this SqlStats.
        Application wait time (in microseconds)


        :return: The application_wait_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._application_wait_time_in_us

    @application_wait_time_in_us.setter
    def application_wait_time_in_us(self, application_wait_time_in_us):
        """
        Sets the application_wait_time_in_us of this SqlStats.
        Application wait time (in microseconds)


        :param application_wait_time_in_us: The application_wait_time_in_us of this SqlStats.
        :type: int
        """
        self._application_wait_time_in_us = application_wait_time_in_us

    @property
    def cluster_wait_time_in_us(self):
        """
        Gets the cluster_wait_time_in_us of this SqlStats.
        Cluster wait time (in microseconds). This value is specific to Oracle RAC


        :return: The cluster_wait_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._cluster_wait_time_in_us

    @cluster_wait_time_in_us.setter
    def cluster_wait_time_in_us(self, cluster_wait_time_in_us):
        """
        Sets the cluster_wait_time_in_us of this SqlStats.
        Cluster wait time (in microseconds). This value is specific to Oracle RAC


        :param cluster_wait_time_in_us: The cluster_wait_time_in_us of this SqlStats.
        :type: int
        """
        self._cluster_wait_time_in_us = cluster_wait_time_in_us

    @property
    def user_io_wait_time_in_us(self):
        """
        Gets the user_io_wait_time_in_us of this SqlStats.
        User I/O wait time (in microseconds)


        :return: The user_io_wait_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._user_io_wait_time_in_us

    @user_io_wait_time_in_us.setter
    def user_io_wait_time_in_us(self, user_io_wait_time_in_us):
        """
        Sets the user_io_wait_time_in_us of this SqlStats.
        User I/O wait time (in microseconds)


        :param user_io_wait_time_in_us: The user_io_wait_time_in_us of this SqlStats.
        :type: int
        """
        self._user_io_wait_time_in_us = user_io_wait_time_in_us

    @property
    def plsql_exec_time_in_us(self):
        """
        Gets the plsql_exec_time_in_us of this SqlStats.
        PL/SQL execution time (in microseconds)


        :return: The plsql_exec_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._plsql_exec_time_in_us

    @plsql_exec_time_in_us.setter
    def plsql_exec_time_in_us(self, plsql_exec_time_in_us):
        """
        Sets the plsql_exec_time_in_us of this SqlStats.
        PL/SQL execution time (in microseconds)


        :param plsql_exec_time_in_us: The plsql_exec_time_in_us of this SqlStats.
        :type: int
        """
        self._plsql_exec_time_in_us = plsql_exec_time_in_us

    @property
    def java_exec_time_in_us(self):
        """
        Gets the java_exec_time_in_us of this SqlStats.
        Java execution time (in microseconds)


        :return: The java_exec_time_in_us of this SqlStats.
        :rtype: int
        """
        return self._java_exec_time_in_us

    @java_exec_time_in_us.setter
    def java_exec_time_in_us(self, java_exec_time_in_us):
        """
        Sets the java_exec_time_in_us of this SqlStats.
        Java execution time (in microseconds)


        :param java_exec_time_in_us: The java_exec_time_in_us of this SqlStats.
        :type: int
        """
        self._java_exec_time_in_us = java_exec_time_in_us

    @property
    def sorts(self):
        """
        Gets the sorts of this SqlStats.
        Number of sorts that were done for the child cursor


        :return: The sorts of this SqlStats.
        :rtype: int
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        """
        Sets the sorts of this SqlStats.
        Number of sorts that were done for the child cursor


        :param sorts: The sorts of this SqlStats.
        :type: int
        """
        self._sorts = sorts

    @property
    def sharable_mem(self):
        """
        Gets the sharable_mem of this SqlStats.
        Total shared memory (in bytes) currently occupied by all cursors with this SQL text and plan


        :return: The sharable_mem of this SqlStats.
        :rtype: int
        """
        return self._sharable_mem

    @sharable_mem.setter
    def sharable_mem(self, sharable_mem):
        """
        Sets the sharable_mem of this SqlStats.
        Total shared memory (in bytes) currently occupied by all cursors with this SQL text and plan


        :param sharable_mem: The sharable_mem of this SqlStats.
        :type: int
        """
        self._sharable_mem = sharable_mem

    @property
    def total_sharable_mem(self):
        """
        Gets the total_sharable_mem of this SqlStats.
        Total shared memory (in bytes) occupied by all cursors with this SQL text and plan if they were to be fully loaded in the shared pool (that is, cursor size)


        :return: The total_sharable_mem of this SqlStats.
        :rtype: int
        """
        return self._total_sharable_mem

    @total_sharable_mem.setter
    def total_sharable_mem(self, total_sharable_mem):
        """
        Sets the total_sharable_mem of this SqlStats.
        Total shared memory (in bytes) occupied by all cursors with this SQL text and plan if they were to be fully loaded in the shared pool (that is, cursor size)


        :param total_sharable_mem: The total_sharable_mem of this SqlStats.
        :type: int
        """
        self._total_sharable_mem = total_sharable_mem

    @property
    def type_check_mem(self):
        """
        Gets the type_check_mem of this SqlStats.
        Typecheck memory


        :return: The type_check_mem of this SqlStats.
        :rtype: int
        """
        return self._type_check_mem

    @type_check_mem.setter
    def type_check_mem(self, type_check_mem):
        """
        Sets the type_check_mem of this SqlStats.
        Typecheck memory


        :param type_check_mem: The type_check_mem of this SqlStats.
        :type: int
        """
        self._type_check_mem = type_check_mem

    @property
    def io_cell_offload_eligible_bytes(self):
        """
        Gets the io_cell_offload_eligible_bytes of this SqlStats.
        Number of I/O bytes which can be filtered by the Exadata storage system


        :return: The io_cell_offload_eligible_bytes of this SqlStats.
        :rtype: int
        """
        return self._io_cell_offload_eligible_bytes

    @io_cell_offload_eligible_bytes.setter
    def io_cell_offload_eligible_bytes(self, io_cell_offload_eligible_bytes):
        """
        Sets the io_cell_offload_eligible_bytes of this SqlStats.
        Number of I/O bytes which can be filtered by the Exadata storage system


        :param io_cell_offload_eligible_bytes: The io_cell_offload_eligible_bytes of this SqlStats.
        :type: int
        """
        self._io_cell_offload_eligible_bytes = io_cell_offload_eligible_bytes

    @property
    def io_interconnect_bytes(self):
        """
        Gets the io_interconnect_bytes of this SqlStats.
        Number of I/O bytes exchanged between Oracle Database and the storage system. Typically used for Cache Fusion or parallel queries


        :return: The io_interconnect_bytes of this SqlStats.
        :rtype: int
        """
        return self._io_interconnect_bytes

    @io_interconnect_bytes.setter
    def io_interconnect_bytes(self, io_interconnect_bytes):
        """
        Sets the io_interconnect_bytes of this SqlStats.
        Number of I/O bytes exchanged between Oracle Database and the storage system. Typically used for Cache Fusion or parallel queries


        :param io_interconnect_bytes: The io_interconnect_bytes of this SqlStats.
        :type: int
        """
        self._io_interconnect_bytes = io_interconnect_bytes

    @property
    def physical_read_requests(self):
        """
        Gets the physical_read_requests of this SqlStats.
        Number of physical read I/O requests issued by the monitored SQL. The requests may not be disk reads


        :return: The physical_read_requests of this SqlStats.
        :rtype: int
        """
        return self._physical_read_requests

    @physical_read_requests.setter
    def physical_read_requests(self, physical_read_requests):
        """
        Sets the physical_read_requests of this SqlStats.
        Number of physical read I/O requests issued by the monitored SQL. The requests may not be disk reads


        :param physical_read_requests: The physical_read_requests of this SqlStats.
        :type: int
        """
        self._physical_read_requests = physical_read_requests

    @property
    def physical_read_bytes(self):
        """
        Gets the physical_read_bytes of this SqlStats.
        Number of bytes read from disks by the monitored SQL


        :return: The physical_read_bytes of this SqlStats.
        :rtype: int
        """
        return self._physical_read_bytes

    @physical_read_bytes.setter
    def physical_read_bytes(self, physical_read_bytes):
        """
        Sets the physical_read_bytes of this SqlStats.
        Number of bytes read from disks by the monitored SQL


        :param physical_read_bytes: The physical_read_bytes of this SqlStats.
        :type: int
        """
        self._physical_read_bytes = physical_read_bytes

    @property
    def physical_write_requests(self):
        """
        Gets the physical_write_requests of this SqlStats.
        Number of physical write I/O requests issued by the monitored SQL


        :return: The physical_write_requests of this SqlStats.
        :rtype: int
        """
        return self._physical_write_requests

    @physical_write_requests.setter
    def physical_write_requests(self, physical_write_requests):
        """
        Sets the physical_write_requests of this SqlStats.
        Number of physical write I/O requests issued by the monitored SQL


        :param physical_write_requests: The physical_write_requests of this SqlStats.
        :type: int
        """
        self._physical_write_requests = physical_write_requests

    @property
    def physical_write_bytes(self):
        """
        Gets the physical_write_bytes of this SqlStats.
        Number of bytes written to disks by the monitored SQL


        :return: The physical_write_bytes of this SqlStats.
        :rtype: int
        """
        return self._physical_write_bytes

    @physical_write_bytes.setter
    def physical_write_bytes(self, physical_write_bytes):
        """
        Sets the physical_write_bytes of this SqlStats.
        Number of bytes written to disks by the monitored SQL


        :param physical_write_bytes: The physical_write_bytes of this SqlStats.
        :type: int
        """
        self._physical_write_bytes = physical_write_bytes

    @property
    def exact_matching_signature(self):
        """
        Gets the exact_matching_signature of this SqlStats.
        exact_matching_signature
        Example: `\"18067345456756876713\"`


        :return: The exact_matching_signature of this SqlStats.
        :rtype: str
        """
        return self._exact_matching_signature

    @exact_matching_signature.setter
    def exact_matching_signature(self, exact_matching_signature):
        """
        Sets the exact_matching_signature of this SqlStats.
        exact_matching_signature
        Example: `\"18067345456756876713\"`


        :param exact_matching_signature: The exact_matching_signature of this SqlStats.
        :type: str
        """
        self._exact_matching_signature = exact_matching_signature

    @property
    def force_matching_signature(self):
        """
        Gets the force_matching_signature of this SqlStats.
        force_matching_signature
        Example: `\"18067345456756876713\"`


        :return: The force_matching_signature of this SqlStats.
        :rtype: str
        """
        return self._force_matching_signature

    @force_matching_signature.setter
    def force_matching_signature(self, force_matching_signature):
        """
        Sets the force_matching_signature of this SqlStats.
        force_matching_signature
        Example: `\"18067345456756876713\"`


        :param force_matching_signature: The force_matching_signature of this SqlStats.
        :type: str
        """
        self._force_matching_signature = force_matching_signature

    @property
    def io_cell_uncompressed_bytes(self):
        """
        Gets the io_cell_uncompressed_bytes of this SqlStats.
        Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells


        :return: The io_cell_uncompressed_bytes of this SqlStats.
        :rtype: int
        """
        return self._io_cell_uncompressed_bytes

    @io_cell_uncompressed_bytes.setter
    def io_cell_uncompressed_bytes(self, io_cell_uncompressed_bytes):
        """
        Sets the io_cell_uncompressed_bytes of this SqlStats.
        Number of uncompressed bytes (that is, size after decompression) that are offloaded to the Exadata cells


        :param io_cell_uncompressed_bytes: The io_cell_uncompressed_bytes of this SqlStats.
        :type: int
        """
        self._io_cell_uncompressed_bytes = io_cell_uncompressed_bytes

    @property
    def io_cell_offload_returned_bytes(self):
        """
        Gets the io_cell_offload_returned_bytes of this SqlStats.
        Number of bytes that are returned by Exadata cell through the regular I/O path


        :return: The io_cell_offload_returned_bytes of this SqlStats.
        :rtype: int
        """
        return self._io_cell_offload_returned_bytes

    @io_cell_offload_returned_bytes.setter
    def io_cell_offload_returned_bytes(self, io_cell_offload_returned_bytes):
        """
        Sets the io_cell_offload_returned_bytes of this SqlStats.
        Number of bytes that are returned by Exadata cell through the regular I/O path


        :param io_cell_offload_returned_bytes: The io_cell_offload_returned_bytes of this SqlStats.
        :type: int
        """
        self._io_cell_offload_returned_bytes = io_cell_offload_returned_bytes

    @property
    def child_number(self):
        """
        Gets the child_number of this SqlStats.
        Number of this child cursor


        :return: The child_number of this SqlStats.
        :rtype: int
        """
        return self._child_number

    @child_number.setter
    def child_number(self, child_number):
        """
        Sets the child_number of this SqlStats.
        Number of this child cursor


        :param child_number: The child_number of this SqlStats.
        :type: int
        """
        self._child_number = child_number

    @property
    def command_type(self):
        """
        Gets the command_type of this SqlStats.
        Oracle command type definition


        :return: The command_type of this SqlStats.
        :rtype: int
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """
        Sets the command_type of this SqlStats.
        Oracle command type definition


        :param command_type: The command_type of this SqlStats.
        :type: int
        """
        self._command_type = command_type

    @property
    def users_opening(self):
        """
        Gets the users_opening of this SqlStats.
        Number of users that have any of the child cursors open


        :return: The users_opening of this SqlStats.
        :rtype: int
        """
        return self._users_opening

    @users_opening.setter
    def users_opening(self, users_opening):
        """
        Sets the users_opening of this SqlStats.
        Number of users that have any of the child cursors open


        :param users_opening: The users_opening of this SqlStats.
        :type: int
        """
        self._users_opening = users_opening

    @property
    def users_executing(self):
        """
        Gets the users_executing of this SqlStats.
        Number of users executing the statement


        :return: The users_executing of this SqlStats.
        :rtype: int
        """
        return self._users_executing

    @users_executing.setter
    def users_executing(self, users_executing):
        """
        Sets the users_executing of this SqlStats.
        Number of users executing the statement


        :param users_executing: The users_executing of this SqlStats.
        :type: int
        """
        self._users_executing = users_executing

    @property
    def optimizer_cost(self):
        """
        Gets the optimizer_cost of this SqlStats.
        Cost of this query given by the optimizer


        :return: The optimizer_cost of this SqlStats.
        :rtype: int
        """
        return self._optimizer_cost

    @optimizer_cost.setter
    def optimizer_cost(self, optimizer_cost):
        """
        Sets the optimizer_cost of this SqlStats.
        Cost of this query given by the optimizer


        :param optimizer_cost: The optimizer_cost of this SqlStats.
        :type: int
        """
        self._optimizer_cost = optimizer_cost

    @property
    def full_plan_hash_value(self):
        """
        Gets the full_plan_hash_value of this SqlStats.
        Total Number of rows in SQLStats table


        :return: The full_plan_hash_value of this SqlStats.
        :rtype: str
        """
        return self._full_plan_hash_value

    @full_plan_hash_value.setter
    def full_plan_hash_value(self, full_plan_hash_value):
        """
        Sets the full_plan_hash_value of this SqlStats.
        Total Number of rows in SQLStats table


        :param full_plan_hash_value: The full_plan_hash_value of this SqlStats.
        :type: str
        """
        self._full_plan_hash_value = full_plan_hash_value

    @property
    def module(self):
        """
        Gets the module of this SqlStats.
        Module name


        :return: The module of this SqlStats.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """
        Sets the module of this SqlStats.
        Module name


        :param module: The module of this SqlStats.
        :type: str
        """
        self._module = module

    @property
    def service(self):
        """
        Gets the service of this SqlStats.
        Service name


        :return: The service of this SqlStats.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this SqlStats.
        Service name


        :param service: The service of this SqlStats.
        :type: str
        """
        self._service = service

    @property
    def action(self):
        """
        Gets the action of this SqlStats.
        Contains the name of the action that was executing when the SQL statement was first parsed, which is set by calling DBMS_APPLICATION_INFO.SET_ACTION


        :return: The action of this SqlStats.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this SqlStats.
        Contains the name of the action that was executing when the SQL statement was first parsed, which is set by calling DBMS_APPLICATION_INFO.SET_ACTION


        :param action: The action of this SqlStats.
        :type: str
        """
        self._action = action

    @property
    def sql_profile(self):
        """
        Gets the sql_profile of this SqlStats.
        SQL profile used for this statement, if any


        :return: The sql_profile of this SqlStats.
        :rtype: str
        """
        return self._sql_profile

    @sql_profile.setter
    def sql_profile(self, sql_profile):
        """
        Sets the sql_profile of this SqlStats.
        SQL profile used for this statement, if any


        :param sql_profile: The sql_profile of this SqlStats.
        :type: str
        """
        self._sql_profile = sql_profile

    @property
    def sql_patch(self):
        """
        Gets the sql_patch of this SqlStats.
        SQL patch used for this statement, if any


        :return: The sql_patch of this SqlStats.
        :rtype: str
        """
        return self._sql_patch

    @sql_patch.setter
    def sql_patch(self, sql_patch):
        """
        Sets the sql_patch of this SqlStats.
        SQL patch used for this statement, if any


        :param sql_patch: The sql_patch of this SqlStats.
        :type: str
        """
        self._sql_patch = sql_patch

    @property
    def sql_plan_baseline(self):
        """
        Gets the sql_plan_baseline of this SqlStats.
        SQL plan baseline used for this statement, if any


        :return: The sql_plan_baseline of this SqlStats.
        :rtype: str
        """
        return self._sql_plan_baseline

    @sql_plan_baseline.setter
    def sql_plan_baseline(self, sql_plan_baseline):
        """
        Sets the sql_plan_baseline of this SqlStats.
        SQL plan baseline used for this statement, if any


        :param sql_plan_baseline: The sql_plan_baseline of this SqlStats.
        :type: str
        """
        self._sql_plan_baseline = sql_plan_baseline

    @property
    def delta_execution_count(self):
        """
        Gets the delta_execution_count of this SqlStats.
        Number of executions for the cursor since the last AWR snapshot


        :return: The delta_execution_count of this SqlStats.
        :rtype: int
        """
        return self._delta_execution_count

    @delta_execution_count.setter
    def delta_execution_count(self, delta_execution_count):
        """
        Sets the delta_execution_count of this SqlStats.
        Number of executions for the cursor since the last AWR snapshot


        :param delta_execution_count: The delta_execution_count of this SqlStats.
        :type: int
        """
        self._delta_execution_count = delta_execution_count

    @property
    def delta_cpu_time(self):
        """
        Gets the delta_cpu_time of this SqlStats.
        CPU time (in microseconds) for the cursor since the last AWR snapshot


        :return: The delta_cpu_time of this SqlStats.
        :rtype: int
        """
        return self._delta_cpu_time

    @delta_cpu_time.setter
    def delta_cpu_time(self, delta_cpu_time):
        """
        Sets the delta_cpu_time of this SqlStats.
        CPU time (in microseconds) for the cursor since the last AWR snapshot


        :param delta_cpu_time: The delta_cpu_time of this SqlStats.
        :type: int
        """
        self._delta_cpu_time = delta_cpu_time

    @property
    def delta_io_bytes(self):
        """
        Gets the delta_io_bytes of this SqlStats.
        Number of I/O bytes exchanged between the Oracle database and the storage system for the cursor since the last AWR snapshot


        :return: The delta_io_bytes of this SqlStats.
        :rtype: int
        """
        return self._delta_io_bytes

    @delta_io_bytes.setter
    def delta_io_bytes(self, delta_io_bytes):
        """
        Sets the delta_io_bytes of this SqlStats.
        Number of I/O bytes exchanged between the Oracle database and the storage system for the cursor since the last AWR snapshot


        :param delta_io_bytes: The delta_io_bytes of this SqlStats.
        :type: int
        """
        self._delta_io_bytes = delta_io_bytes

    @property
    def delta_cpu_rank(self):
        """
        Gets the delta_cpu_rank of this SqlStats.
        Rank based on CPU Consumption


        :return: The delta_cpu_rank of this SqlStats.
        :rtype: int
        """
        return self._delta_cpu_rank

    @delta_cpu_rank.setter
    def delta_cpu_rank(self, delta_cpu_rank):
        """
        Sets the delta_cpu_rank of this SqlStats.
        Rank based on CPU Consumption


        :param delta_cpu_rank: The delta_cpu_rank of this SqlStats.
        :type: int
        """
        self._delta_cpu_rank = delta_cpu_rank

    @property
    def delta_execs_rank(self):
        """
        Gets the delta_execs_rank of this SqlStats.
        Rank based on number of execution


        :return: The delta_execs_rank of this SqlStats.
        :rtype: int
        """
        return self._delta_execs_rank

    @delta_execs_rank.setter
    def delta_execs_rank(self, delta_execs_rank):
        """
        Sets the delta_execs_rank of this SqlStats.
        Rank based on number of execution


        :param delta_execs_rank: The delta_execs_rank of this SqlStats.
        :type: int
        """
        self._delta_execs_rank = delta_execs_rank

    @property
    def sharable_mem_rank(self):
        """
        Gets the sharable_mem_rank of this SqlStats.
        Rank based on sharable memory


        :return: The sharable_mem_rank of this SqlStats.
        :rtype: int
        """
        return self._sharable_mem_rank

    @sharable_mem_rank.setter
    def sharable_mem_rank(self, sharable_mem_rank):
        """
        Sets the sharable_mem_rank of this SqlStats.
        Rank based on sharable memory


        :param sharable_mem_rank: The sharable_mem_rank of this SqlStats.
        :type: int
        """
        self._sharable_mem_rank = sharable_mem_rank

    @property
    def delta_io_rank(self):
        """
        Gets the delta_io_rank of this SqlStats.
        Rank based on I/O Consumption


        :return: The delta_io_rank of this SqlStats.
        :rtype: int
        """
        return self._delta_io_rank

    @delta_io_rank.setter
    def delta_io_rank(self, delta_io_rank):
        """
        Sets the delta_io_rank of this SqlStats.
        Rank based on I/O Consumption


        :param delta_io_rank: The delta_io_rank of this SqlStats.
        :type: int
        """
        self._delta_io_rank = delta_io_rank

    @property
    def harmonic_sum(self):
        """
        Gets the harmonic_sum of this SqlStats.
        Harmonic sum based on ranking parameters


        :return: The harmonic_sum of this SqlStats.
        :rtype: int
        """
        return self._harmonic_sum

    @harmonic_sum.setter
    def harmonic_sum(self, harmonic_sum):
        """
        Sets the harmonic_sum of this SqlStats.
        Harmonic sum based on ranking parameters


        :param harmonic_sum: The harmonic_sum of this SqlStats.
        :type: int
        """
        self._harmonic_sum = harmonic_sum

    @property
    def wt_harmonic_sum(self):
        """
        Gets the wt_harmonic_sum of this SqlStats.
        Weight based harmonic sum of ranking parameters


        :return: The wt_harmonic_sum of this SqlStats.
        :rtype: int
        """
        return self._wt_harmonic_sum

    @wt_harmonic_sum.setter
    def wt_harmonic_sum(self, wt_harmonic_sum):
        """
        Sets the wt_harmonic_sum of this SqlStats.
        Weight based harmonic sum of ranking parameters


        :param wt_harmonic_sum: The wt_harmonic_sum of this SqlStats.
        :type: int
        """
        self._wt_harmonic_sum = wt_harmonic_sum

    @property
    def total_sql_count(self):
        """
        Gets the total_sql_count of this SqlStats.
        Total number of rows in SQLStats table


        :return: The total_sql_count of this SqlStats.
        :rtype: int
        """
        return self._total_sql_count

    @total_sql_count.setter
    def total_sql_count(self, total_sql_count):
        """
        Sets the total_sql_count of this SqlStats.
        Total number of rows in SQLStats table


        :param total_sql_count: The total_sql_count of this SqlStats.
        :type: int
        """
        self._total_sql_count = total_sql_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
