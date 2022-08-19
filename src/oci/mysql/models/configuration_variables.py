# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationVariables(object):
    """
    User-defined service variables.
    """

    #: A constant which can be used with the completion_type property of a ConfigurationVariables.
    #: This constant has a value of "NO_CHAIN"
    COMPLETION_TYPE_NO_CHAIN = "NO_CHAIN"

    #: A constant which can be used with the completion_type property of a ConfigurationVariables.
    #: This constant has a value of "CHAIN"
    COMPLETION_TYPE_CHAIN = "CHAIN"

    #: A constant which can be used with the completion_type property of a ConfigurationVariables.
    #: This constant has a value of "RELEASE"
    COMPLETION_TYPE_RELEASE = "RELEASE"

    #: A constant which can be used with the default_authentication_plugin property of a ConfigurationVariables.
    #: This constant has a value of "mysql_native_password"
    DEFAULT_AUTHENTICATION_PLUGIN_MYSQL_NATIVE_PASSWORD = "mysql_native_password"

    #: A constant which can be used with the default_authentication_plugin property of a ConfigurationVariables.
    #: This constant has a value of "sha256_password"
    DEFAULT_AUTHENTICATION_PLUGIN_SHA256_PASSWORD = "sha256_password"

    #: A constant which can be used with the default_authentication_plugin property of a ConfigurationVariables.
    #: This constant has a value of "caching_sha2_password"
    DEFAULT_AUTHENTICATION_PLUGIN_CACHING_SHA2_PASSWORD = "caching_sha2_password"

    #: A constant which can be used with the transaction_isolation property of a ConfigurationVariables.
    #: This constant has a value of "READ-UNCOMMITTED"
    TRANSACTION_ISOLATION_READ_UNCOMMITTED = "READ-UNCOMMITTED"

    #: A constant which can be used with the transaction_isolation property of a ConfigurationVariables.
    #: This constant has a value of "READ-COMMITED"
    TRANSACTION_ISOLATION_READ_COMMITED = "READ-COMMITED"

    #: A constant which can be used with the transaction_isolation property of a ConfigurationVariables.
    #: This constant has a value of "READ-COMMITTED"
    TRANSACTION_ISOLATION_READ_COMMITTED = "READ-COMMITTED"

    #: A constant which can be used with the transaction_isolation property of a ConfigurationVariables.
    #: This constant has a value of "REPEATABLE-READ"
    TRANSACTION_ISOLATION_REPEATABLE_READ = "REPEATABLE-READ"

    #: A constant which can be used with the transaction_isolation property of a ConfigurationVariables.
    #: This constant has a value of "SERIALIZABLE"
    TRANSACTION_ISOLATION_SERIALIZABLE = "SERIALIZABLE"

    #: A constant which can be used with the group_replication_consistency property of a ConfigurationVariables.
    #: This constant has a value of "EVENTUAL"
    GROUP_REPLICATION_CONSISTENCY_EVENTUAL = "EVENTUAL"

    #: A constant which can be used with the group_replication_consistency property of a ConfigurationVariables.
    #: This constant has a value of "BEFORE_ON_PRIMARY_FAILOVER"
    GROUP_REPLICATION_CONSISTENCY_BEFORE_ON_PRIMARY_FAILOVER = "BEFORE_ON_PRIMARY_FAILOVER"

    #: A constant which can be used with the group_replication_consistency property of a ConfigurationVariables.
    #: This constant has a value of "BEFORE"
    GROUP_REPLICATION_CONSISTENCY_BEFORE = "BEFORE"

    #: A constant which can be used with the group_replication_consistency property of a ConfigurationVariables.
    #: This constant has a value of "AFTER"
    GROUP_REPLICATION_CONSISTENCY_AFTER = "AFTER"

    #: A constant which can be used with the group_replication_consistency property of a ConfigurationVariables.
    #: This constant has a value of "BEFORE_AND_AFTER"
    GROUP_REPLICATION_CONSISTENCY_BEFORE_AND_AFTER = "BEFORE_AND_AFTER"

    #: A constant which can be used with the binlog_row_metadata property of a ConfigurationVariables.
    #: This constant has a value of "FULL"
    BINLOG_ROW_METADATA_FULL = "FULL"

    #: A constant which can be used with the binlog_row_metadata property of a ConfigurationVariables.
    #: This constant has a value of "MINIMAL"
    BINLOG_ROW_METADATA_MINIMAL = "MINIMAL"

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationVariables object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param completion_type:
            The value to assign to the completion_type property of this ConfigurationVariables.
            Allowed values for this property are: "NO_CHAIN", "CHAIN", "RELEASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type completion_type: str

        :param big_tables:
            The value to assign to the big_tables property of this ConfigurationVariables.
        :type big_tables: bool

        :param connection_memory_chunk_size:
            The value to assign to the connection_memory_chunk_size property of this ConfigurationVariables.
        :type connection_memory_chunk_size: int

        :param connection_memory_limit:
            The value to assign to the connection_memory_limit property of this ConfigurationVariables.
        :type connection_memory_limit: int

        :param default_authentication_plugin:
            The value to assign to the default_authentication_plugin property of this ConfigurationVariables.
            Allowed values for this property are: "mysql_native_password", "sha256_password", "caching_sha2_password", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type default_authentication_plugin: str

        :param global_connection_memory_limit:
            The value to assign to the global_connection_memory_limit property of this ConfigurationVariables.
        :type global_connection_memory_limit: int

        :param global_connection_memory_tracking:
            The value to assign to the global_connection_memory_tracking property of this ConfigurationVariables.
        :type global_connection_memory_tracking: bool

        :param transaction_isolation:
            The value to assign to the transaction_isolation property of this ConfigurationVariables.
            Allowed values for this property are: "READ-UNCOMMITTED", "READ-COMMITED", "READ-COMMITTED", "REPEATABLE-READ", "SERIALIZABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type transaction_isolation: str

        :param innodb_ft_server_stopword_table:
            The value to assign to the innodb_ft_server_stopword_table property of this ConfigurationVariables.
        :type innodb_ft_server_stopword_table: str

        :param mandatory_roles:
            The value to assign to the mandatory_roles property of this ConfigurationVariables.
        :type mandatory_roles: str

        :param autocommit:
            The value to assign to the autocommit property of this ConfigurationVariables.
        :type autocommit: bool

        :param foreign_key_checks:
            The value to assign to the foreign_key_checks property of this ConfigurationVariables.
        :type foreign_key_checks: bool

        :param group_replication_consistency:
            The value to assign to the group_replication_consistency property of this ConfigurationVariables.
            Allowed values for this property are: "EVENTUAL", "BEFORE_ON_PRIMARY_FAILOVER", "BEFORE", "AFTER", "BEFORE_AND_AFTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type group_replication_consistency: str

        :param innodb_ft_enable_stopword:
            The value to assign to the innodb_ft_enable_stopword property of this ConfigurationVariables.
        :type innodb_ft_enable_stopword: bool

        :param innodb_log_writer_threads:
            The value to assign to the innodb_log_writer_threads property of this ConfigurationVariables.
        :type innodb_log_writer_threads: bool

        :param local_infile:
            The value to assign to the local_infile property of this ConfigurationVariables.
        :type local_infile: bool

        :param mysql_firewall_mode:
            The value to assign to the mysql_firewall_mode property of this ConfigurationVariables.
        :type mysql_firewall_mode: bool

        :param mysqlx_enable_hello_notice:
            The value to assign to the mysqlx_enable_hello_notice property of this ConfigurationVariables.
        :type mysqlx_enable_hello_notice: bool

        :param sql_require_primary_key:
            The value to assign to the sql_require_primary_key property of this ConfigurationVariables.
        :type sql_require_primary_key: bool

        :param sql_warnings:
            The value to assign to the sql_warnings property of this ConfigurationVariables.
        :type sql_warnings: bool

        :param binlog_expire_logs_seconds:
            The value to assign to the binlog_expire_logs_seconds property of this ConfigurationVariables.
        :type binlog_expire_logs_seconds: int

        :param binlog_row_metadata:
            The value to assign to the binlog_row_metadata property of this ConfigurationVariables.
            Allowed values for this property are: "FULL", "MINIMAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type binlog_row_metadata: str

        :param binlog_row_value_options:
            The value to assign to the binlog_row_value_options property of this ConfigurationVariables.
        :type binlog_row_value_options: str

        :param binlog_transaction_compression:
            The value to assign to the binlog_transaction_compression property of this ConfigurationVariables.
        :type binlog_transaction_compression: bool

        :param innodb_buffer_pool_size:
            The value to assign to the innodb_buffer_pool_size property of this ConfigurationVariables.
        :type innodb_buffer_pool_size: int

        :param innodb_ft_result_cache_limit:
            The value to assign to the innodb_ft_result_cache_limit property of this ConfigurationVariables.
        :type innodb_ft_result_cache_limit: int

        :param max_binlog_cache_size:
            The value to assign to the max_binlog_cache_size property of this ConfigurationVariables.
        :type max_binlog_cache_size: int

        :param max_connect_errors:
            The value to assign to the max_connect_errors property of this ConfigurationVariables.
        :type max_connect_errors: int

        :param max_heap_table_size:
            The value to assign to the max_heap_table_size property of this ConfigurationVariables.
        :type max_heap_table_size: int

        :param max_connections:
            The value to assign to the max_connections property of this ConfigurationVariables.
        :type max_connections: int

        :param max_prepared_stmt_count:
            The value to assign to the max_prepared_stmt_count property of this ConfigurationVariables.
        :type max_prepared_stmt_count: int

        :param connect_timeout:
            The value to assign to the connect_timeout property of this ConfigurationVariables.
        :type connect_timeout: int

        :param cte_max_recursion_depth:
            The value to assign to the cte_max_recursion_depth property of this ConfigurationVariables.
        :type cte_max_recursion_depth: int

        :param generated_random_password_length:
            The value to assign to the generated_random_password_length property of this ConfigurationVariables.
        :type generated_random_password_length: int

        :param information_schema_stats_expiry:
            The value to assign to the information_schema_stats_expiry property of this ConfigurationVariables.
        :type information_schema_stats_expiry: int

        :param innodb_buffer_pool_dump_pct:
            The value to assign to the innodb_buffer_pool_dump_pct property of this ConfigurationVariables.
        :type innodb_buffer_pool_dump_pct: int

        :param innodb_buffer_pool_instances:
            The value to assign to the innodb_buffer_pool_instances property of this ConfigurationVariables.
        :type innodb_buffer_pool_instances: int

        :param innodb_ddl_buffer_size:
            The value to assign to the innodb_ddl_buffer_size property of this ConfigurationVariables.
        :type innodb_ddl_buffer_size: int

        :param innodb_ddl_threads:
            The value to assign to the innodb_ddl_threads property of this ConfigurationVariables.
        :type innodb_ddl_threads: int

        :param innodb_ft_max_token_size:
            The value to assign to the innodb_ft_max_token_size property of this ConfigurationVariables.
        :type innodb_ft_max_token_size: int

        :param innodb_ft_min_token_size:
            The value to assign to the innodb_ft_min_token_size property of this ConfigurationVariables.
        :type innodb_ft_min_token_size: int

        :param innodb_ft_num_word_optimize:
            The value to assign to the innodb_ft_num_word_optimize property of this ConfigurationVariables.
        :type innodb_ft_num_word_optimize: int

        :param innodb_lock_wait_timeout:
            The value to assign to the innodb_lock_wait_timeout property of this ConfigurationVariables.
        :type innodb_lock_wait_timeout: int

        :param innodb_max_purge_lag:
            The value to assign to the innodb_max_purge_lag property of this ConfigurationVariables.
        :type innodb_max_purge_lag: int

        :param innodb_max_purge_lag_delay:
            The value to assign to the innodb_max_purge_lag_delay property of this ConfigurationVariables.
        :type innodb_max_purge_lag_delay: int

        :param interactive_timeout:
            The value to assign to the interactive_timeout property of this ConfigurationVariables.
        :type interactive_timeout: int

        :param innodb_stats_persistent_sample_pages:
            The value to assign to the innodb_stats_persistent_sample_pages property of this ConfigurationVariables.
        :type innodb_stats_persistent_sample_pages: int

        :param innodb_stats_transient_sample_pages:
            The value to assign to the innodb_stats_transient_sample_pages property of this ConfigurationVariables.
        :type innodb_stats_transient_sample_pages: int

        :param max_allowed_packet:
            The value to assign to the max_allowed_packet property of this ConfigurationVariables.
        :type max_allowed_packet: int

        :param max_execution_time:
            The value to assign to the max_execution_time property of this ConfigurationVariables.
        :type max_execution_time: int

        :param mysqlx_connect_timeout:
            The value to assign to the mysqlx_connect_timeout property of this ConfigurationVariables.
        :type mysqlx_connect_timeout: int

        :param mysqlx_document_id_unique_prefix:
            The value to assign to the mysqlx_document_id_unique_prefix property of this ConfigurationVariables.
        :type mysqlx_document_id_unique_prefix: int

        :param mysqlx_idle_worker_thread_timeout:
            The value to assign to the mysqlx_idle_worker_thread_timeout property of this ConfigurationVariables.
        :type mysqlx_idle_worker_thread_timeout: int

        :param mysqlx_interactive_timeout:
            The value to assign to the mysqlx_interactive_timeout property of this ConfigurationVariables.
        :type mysqlx_interactive_timeout: int

        :param mysqlx_max_allowed_packet:
            The value to assign to the mysqlx_max_allowed_packet property of this ConfigurationVariables.
        :type mysqlx_max_allowed_packet: int

        :param mysqlx_min_worker_threads:
            The value to assign to the mysqlx_min_worker_threads property of this ConfigurationVariables.
        :type mysqlx_min_worker_threads: int

        :param mysqlx_read_timeout:
            The value to assign to the mysqlx_read_timeout property of this ConfigurationVariables.
        :type mysqlx_read_timeout: int

        :param mysqlx_wait_timeout:
            The value to assign to the mysqlx_wait_timeout property of this ConfigurationVariables.
        :type mysqlx_wait_timeout: int

        :param mysqlx_write_timeout:
            The value to assign to the mysqlx_write_timeout property of this ConfigurationVariables.
        :type mysqlx_write_timeout: int

        :param net_read_timeout:
            The value to assign to the net_read_timeout property of this ConfigurationVariables.
        :type net_read_timeout: int

        :param net_write_timeout:
            The value to assign to the net_write_timeout property of this ConfigurationVariables.
        :type net_write_timeout: int

        :param parser_max_mem_size:
            The value to assign to the parser_max_mem_size property of this ConfigurationVariables.
        :type parser_max_mem_size: int

        :param query_alloc_block_size:
            The value to assign to the query_alloc_block_size property of this ConfigurationVariables.
        :type query_alloc_block_size: int

        :param query_prealloc_size:
            The value to assign to the query_prealloc_size property of this ConfigurationVariables.
        :type query_prealloc_size: int

        :param regexp_time_limit:
            The value to assign to the regexp_time_limit property of this ConfigurationVariables.
        :type regexp_time_limit: int

        :param sql_mode:
            The value to assign to the sql_mode property of this ConfigurationVariables.
        :type sql_mode: str

        :param tmp_table_size:
            The value to assign to the tmp_table_size property of this ConfigurationVariables.
        :type tmp_table_size: int

        :param mysqlx_deflate_default_compression_level:
            The value to assign to the mysqlx_deflate_default_compression_level property of this ConfigurationVariables.
        :type mysqlx_deflate_default_compression_level: int

        :param mysqlx_deflate_max_client_compression_level:
            The value to assign to the mysqlx_deflate_max_client_compression_level property of this ConfigurationVariables.
        :type mysqlx_deflate_max_client_compression_level: int

        :param mysqlx_lz4_max_client_compression_level:
            The value to assign to the mysqlx_lz4_max_client_compression_level property of this ConfigurationVariables.
        :type mysqlx_lz4_max_client_compression_level: int

        :param mysqlx_lz4_default_compression_level:
            The value to assign to the mysqlx_lz4_default_compression_level property of this ConfigurationVariables.
        :type mysqlx_lz4_default_compression_level: int

        :param mysqlx_zstd_max_client_compression_level:
            The value to assign to the mysqlx_zstd_max_client_compression_level property of this ConfigurationVariables.
        :type mysqlx_zstd_max_client_compression_level: int

        :param mysqlx_zstd_default_compression_level:
            The value to assign to the mysqlx_zstd_default_compression_level property of this ConfigurationVariables.
        :type mysqlx_zstd_default_compression_level: int

        :param mysql_zstd_default_compression_level:
            The value to assign to the mysql_zstd_default_compression_level property of this ConfigurationVariables.
        :type mysql_zstd_default_compression_level: int

        :param sort_buffer_size:
            The value to assign to the sort_buffer_size property of this ConfigurationVariables.
        :type sort_buffer_size: int

        :param wait_timeout:
            The value to assign to the wait_timeout property of this ConfigurationVariables.
        :type wait_timeout: int

        :param thread_pool_dedicated_listeners:
            The value to assign to the thread_pool_dedicated_listeners property of this ConfigurationVariables.
        :type thread_pool_dedicated_listeners: bool

        :param thread_pool_max_transactions_limit:
            The value to assign to the thread_pool_max_transactions_limit property of this ConfigurationVariables.
        :type thread_pool_max_transactions_limit: int

        :param time_zone:
            The value to assign to the time_zone property of this ConfigurationVariables.
        :type time_zone: str

        """
        self.swagger_types = {
            'completion_type': 'str',
            'big_tables': 'bool',
            'connection_memory_chunk_size': 'int',
            'connection_memory_limit': 'int',
            'default_authentication_plugin': 'str',
            'global_connection_memory_limit': 'int',
            'global_connection_memory_tracking': 'bool',
            'transaction_isolation': 'str',
            'innodb_ft_server_stopword_table': 'str',
            'mandatory_roles': 'str',
            'autocommit': 'bool',
            'foreign_key_checks': 'bool',
            'group_replication_consistency': 'str',
            'innodb_ft_enable_stopword': 'bool',
            'innodb_log_writer_threads': 'bool',
            'local_infile': 'bool',
            'mysql_firewall_mode': 'bool',
            'mysqlx_enable_hello_notice': 'bool',
            'sql_require_primary_key': 'bool',
            'sql_warnings': 'bool',
            'binlog_expire_logs_seconds': 'int',
            'binlog_row_metadata': 'str',
            'binlog_row_value_options': 'str',
            'binlog_transaction_compression': 'bool',
            'innodb_buffer_pool_size': 'int',
            'innodb_ft_result_cache_limit': 'int',
            'max_binlog_cache_size': 'int',
            'max_connect_errors': 'int',
            'max_heap_table_size': 'int',
            'max_connections': 'int',
            'max_prepared_stmt_count': 'int',
            'connect_timeout': 'int',
            'cte_max_recursion_depth': 'int',
            'generated_random_password_length': 'int',
            'information_schema_stats_expiry': 'int',
            'innodb_buffer_pool_dump_pct': 'int',
            'innodb_buffer_pool_instances': 'int',
            'innodb_ddl_buffer_size': 'int',
            'innodb_ddl_threads': 'int',
            'innodb_ft_max_token_size': 'int',
            'innodb_ft_min_token_size': 'int',
            'innodb_ft_num_word_optimize': 'int',
            'innodb_lock_wait_timeout': 'int',
            'innodb_max_purge_lag': 'int',
            'innodb_max_purge_lag_delay': 'int',
            'interactive_timeout': 'int',
            'innodb_stats_persistent_sample_pages': 'int',
            'innodb_stats_transient_sample_pages': 'int',
            'max_allowed_packet': 'int',
            'max_execution_time': 'int',
            'mysqlx_connect_timeout': 'int',
            'mysqlx_document_id_unique_prefix': 'int',
            'mysqlx_idle_worker_thread_timeout': 'int',
            'mysqlx_interactive_timeout': 'int',
            'mysqlx_max_allowed_packet': 'int',
            'mysqlx_min_worker_threads': 'int',
            'mysqlx_read_timeout': 'int',
            'mysqlx_wait_timeout': 'int',
            'mysqlx_write_timeout': 'int',
            'net_read_timeout': 'int',
            'net_write_timeout': 'int',
            'parser_max_mem_size': 'int',
            'query_alloc_block_size': 'int',
            'query_prealloc_size': 'int',
            'regexp_time_limit': 'int',
            'sql_mode': 'str',
            'tmp_table_size': 'int',
            'mysqlx_deflate_default_compression_level': 'int',
            'mysqlx_deflate_max_client_compression_level': 'int',
            'mysqlx_lz4_max_client_compression_level': 'int',
            'mysqlx_lz4_default_compression_level': 'int',
            'mysqlx_zstd_max_client_compression_level': 'int',
            'mysqlx_zstd_default_compression_level': 'int',
            'mysql_zstd_default_compression_level': 'int',
            'sort_buffer_size': 'int',
            'wait_timeout': 'int',
            'thread_pool_dedicated_listeners': 'bool',
            'thread_pool_max_transactions_limit': 'int',
            'time_zone': 'str'
        }

        self.attribute_map = {
            'completion_type': 'completionType',
            'big_tables': 'bigTables',
            'connection_memory_chunk_size': 'connectionMemoryChunkSize',
            'connection_memory_limit': 'connectionMemoryLimit',
            'default_authentication_plugin': 'defaultAuthenticationPlugin',
            'global_connection_memory_limit': 'globalConnectionMemoryLimit',
            'global_connection_memory_tracking': 'globalConnectionMemoryTracking',
            'transaction_isolation': 'transactionIsolation',
            'innodb_ft_server_stopword_table': 'innodbFtServerStopwordTable',
            'mandatory_roles': 'mandatoryRoles',
            'autocommit': 'autocommit',
            'foreign_key_checks': 'foreignKeyChecks',
            'group_replication_consistency': 'groupReplicationConsistency',
            'innodb_ft_enable_stopword': 'innodbFtEnableStopword',
            'innodb_log_writer_threads': 'innodbLogWriterThreads',
            'local_infile': 'localInfile',
            'mysql_firewall_mode': 'mysqlFirewallMode',
            'mysqlx_enable_hello_notice': 'mysqlxEnableHelloNotice',
            'sql_require_primary_key': 'sqlRequirePrimaryKey',
            'sql_warnings': 'sqlWarnings',
            'binlog_expire_logs_seconds': 'binlogExpireLogsSeconds',
            'binlog_row_metadata': 'binlogRowMetadata',
            'binlog_row_value_options': 'binlogRowValueOptions',
            'binlog_transaction_compression': 'binlogTransactionCompression',
            'innodb_buffer_pool_size': 'innodbBufferPoolSize',
            'innodb_ft_result_cache_limit': 'innodbFtResultCacheLimit',
            'max_binlog_cache_size': 'maxBinlogCacheSize',
            'max_connect_errors': 'maxConnectErrors',
            'max_heap_table_size': 'maxHeapTableSize',
            'max_connections': 'maxConnections',
            'max_prepared_stmt_count': 'maxPreparedStmtCount',
            'connect_timeout': 'connectTimeout',
            'cte_max_recursion_depth': 'cteMaxRecursionDepth',
            'generated_random_password_length': 'generatedRandomPasswordLength',
            'information_schema_stats_expiry': 'informationSchemaStatsExpiry',
            'innodb_buffer_pool_dump_pct': 'innodbBufferPoolDumpPct',
            'innodb_buffer_pool_instances': 'innodbBufferPoolInstances',
            'innodb_ddl_buffer_size': 'innodbDdlBufferSize',
            'innodb_ddl_threads': 'innodbDdlThreads',
            'innodb_ft_max_token_size': 'innodbFtMaxTokenSize',
            'innodb_ft_min_token_size': 'innodbFtMinTokenSize',
            'innodb_ft_num_word_optimize': 'innodbFtNumWordOptimize',
            'innodb_lock_wait_timeout': 'innodbLockWaitTimeout',
            'innodb_max_purge_lag': 'innodbMaxPurgeLag',
            'innodb_max_purge_lag_delay': 'innodbMaxPurgeLagDelay',
            'interactive_timeout': 'interactiveTimeout',
            'innodb_stats_persistent_sample_pages': 'innodbStatsPersistentSamplePages',
            'innodb_stats_transient_sample_pages': 'innodbStatsTransientSamplePages',
            'max_allowed_packet': 'maxAllowedPacket',
            'max_execution_time': 'maxExecutionTime',
            'mysqlx_connect_timeout': 'mysqlxConnectTimeout',
            'mysqlx_document_id_unique_prefix': 'mysqlxDocumentIdUniquePrefix',
            'mysqlx_idle_worker_thread_timeout': 'mysqlxIdleWorkerThreadTimeout',
            'mysqlx_interactive_timeout': 'mysqlxInteractiveTimeout',
            'mysqlx_max_allowed_packet': 'mysqlxMaxAllowedPacket',
            'mysqlx_min_worker_threads': 'mysqlxMinWorkerThreads',
            'mysqlx_read_timeout': 'mysqlxReadTimeout',
            'mysqlx_wait_timeout': 'mysqlxWaitTimeout',
            'mysqlx_write_timeout': 'mysqlxWriteTimeout',
            'net_read_timeout': 'netReadTimeout',
            'net_write_timeout': 'netWriteTimeout',
            'parser_max_mem_size': 'parserMaxMemSize',
            'query_alloc_block_size': 'queryAllocBlockSize',
            'query_prealloc_size': 'queryPreallocSize',
            'regexp_time_limit': 'regexpTimeLimit',
            'sql_mode': 'sqlMode',
            'tmp_table_size': 'tmpTableSize',
            'mysqlx_deflate_default_compression_level': 'mysqlxDeflateDefaultCompressionLevel',
            'mysqlx_deflate_max_client_compression_level': 'mysqlxDeflateMaxClientCompressionLevel',
            'mysqlx_lz4_max_client_compression_level': 'mysqlxLz4MaxClientCompressionLevel',
            'mysqlx_lz4_default_compression_level': 'mysqlxLz4DefaultCompressionLevel',
            'mysqlx_zstd_max_client_compression_level': 'mysqlxZstdMaxClientCompressionLevel',
            'mysqlx_zstd_default_compression_level': 'mysqlxZstdDefaultCompressionLevel',
            'mysql_zstd_default_compression_level': 'mysqlZstdDefaultCompressionLevel',
            'sort_buffer_size': 'sortBufferSize',
            'wait_timeout': 'waitTimeout',
            'thread_pool_dedicated_listeners': 'threadPoolDedicatedListeners',
            'thread_pool_max_transactions_limit': 'threadPoolMaxTransactionsLimit',
            'time_zone': 'timeZone'
        }

        self._completion_type = None
        self._big_tables = None
        self._connection_memory_chunk_size = None
        self._connection_memory_limit = None
        self._default_authentication_plugin = None
        self._global_connection_memory_limit = None
        self._global_connection_memory_tracking = None
        self._transaction_isolation = None
        self._innodb_ft_server_stopword_table = None
        self._mandatory_roles = None
        self._autocommit = None
        self._foreign_key_checks = None
        self._group_replication_consistency = None
        self._innodb_ft_enable_stopword = None
        self._innodb_log_writer_threads = None
        self._local_infile = None
        self._mysql_firewall_mode = None
        self._mysqlx_enable_hello_notice = None
        self._sql_require_primary_key = None
        self._sql_warnings = None
        self._binlog_expire_logs_seconds = None
        self._binlog_row_metadata = None
        self._binlog_row_value_options = None
        self._binlog_transaction_compression = None
        self._innodb_buffer_pool_size = None
        self._innodb_ft_result_cache_limit = None
        self._max_binlog_cache_size = None
        self._max_connect_errors = None
        self._max_heap_table_size = None
        self._max_connections = None
        self._max_prepared_stmt_count = None
        self._connect_timeout = None
        self._cte_max_recursion_depth = None
        self._generated_random_password_length = None
        self._information_schema_stats_expiry = None
        self._innodb_buffer_pool_dump_pct = None
        self._innodb_buffer_pool_instances = None
        self._innodb_ddl_buffer_size = None
        self._innodb_ddl_threads = None
        self._innodb_ft_max_token_size = None
        self._innodb_ft_min_token_size = None
        self._innodb_ft_num_word_optimize = None
        self._innodb_lock_wait_timeout = None
        self._innodb_max_purge_lag = None
        self._innodb_max_purge_lag_delay = None
        self._interactive_timeout = None
        self._innodb_stats_persistent_sample_pages = None
        self._innodb_stats_transient_sample_pages = None
        self._max_allowed_packet = None
        self._max_execution_time = None
        self._mysqlx_connect_timeout = None
        self._mysqlx_document_id_unique_prefix = None
        self._mysqlx_idle_worker_thread_timeout = None
        self._mysqlx_interactive_timeout = None
        self._mysqlx_max_allowed_packet = None
        self._mysqlx_min_worker_threads = None
        self._mysqlx_read_timeout = None
        self._mysqlx_wait_timeout = None
        self._mysqlx_write_timeout = None
        self._net_read_timeout = None
        self._net_write_timeout = None
        self._parser_max_mem_size = None
        self._query_alloc_block_size = None
        self._query_prealloc_size = None
        self._regexp_time_limit = None
        self._sql_mode = None
        self._tmp_table_size = None
        self._mysqlx_deflate_default_compression_level = None
        self._mysqlx_deflate_max_client_compression_level = None
        self._mysqlx_lz4_max_client_compression_level = None
        self._mysqlx_lz4_default_compression_level = None
        self._mysqlx_zstd_max_client_compression_level = None
        self._mysqlx_zstd_default_compression_level = None
        self._mysql_zstd_default_compression_level = None
        self._sort_buffer_size = None
        self._wait_timeout = None
        self._thread_pool_dedicated_listeners = None
        self._thread_pool_max_transactions_limit = None
        self._time_zone = None

    @property
    def completion_type(self):
        """
        Gets the completion_type of this ConfigurationVariables.
        (\"completion_type\")

        Allowed values for this property are: "NO_CHAIN", "CHAIN", "RELEASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The completion_type of this ConfigurationVariables.
        :rtype: str
        """
        return self._completion_type

    @completion_type.setter
    def completion_type(self, completion_type):
        """
        Sets the completion_type of this ConfigurationVariables.
        (\"completion_type\")


        :param completion_type: The completion_type of this ConfigurationVariables.
        :type: str
        """
        allowed_values = ["NO_CHAIN", "CHAIN", "RELEASE"]
        if not value_allowed_none_or_none_sentinel(completion_type, allowed_values):
            completion_type = 'UNKNOWN_ENUM_VALUE'
        self._completion_type = completion_type

    @property
    def big_tables(self):
        """
        Gets the big_tables of this ConfigurationVariables.
        If enabled, the server stores all temporary tables on disk rather than in memory.

        bigTables corresponds to the MySQL server variable `big_tables`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_big_tables


        :return: The big_tables of this ConfigurationVariables.
        :rtype: bool
        """
        return self._big_tables

    @big_tables.setter
    def big_tables(self, big_tables):
        """
        Sets the big_tables of this ConfigurationVariables.
        If enabled, the server stores all temporary tables on disk rather than in memory.

        bigTables corresponds to the MySQL server variable `big_tables`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_big_tables


        :param big_tables: The big_tables of this ConfigurationVariables.
        :type: bool
        """
        self._big_tables = big_tables

    @property
    def connection_memory_chunk_size(self):
        """
        Gets the connection_memory_chunk_size of this ConfigurationVariables.
        Set the chunking size for updates to the global memory usage counter Global_connection_memory.

        connectionMemoryChunkSize corresponds to the MySQL system variable `connection_memory_chunk_size`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_connection_memory_chunk_size


        :return: The connection_memory_chunk_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._connection_memory_chunk_size

    @connection_memory_chunk_size.setter
    def connection_memory_chunk_size(self, connection_memory_chunk_size):
        """
        Sets the connection_memory_chunk_size of this ConfigurationVariables.
        Set the chunking size for updates to the global memory usage counter Global_connection_memory.

        connectionMemoryChunkSize corresponds to the MySQL system variable `connection_memory_chunk_size`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_connection_memory_chunk_size


        :param connection_memory_chunk_size: The connection_memory_chunk_size of this ConfigurationVariables.
        :type: int
        """
        self._connection_memory_chunk_size = connection_memory_chunk_size

    @property
    def connection_memory_limit(self):
        """
        Gets the connection_memory_limit of this ConfigurationVariables.
        Set the maximum amount of memory that can be used by a single user connection.

        connectionMemoryLimit corresponds to the MySQL system variable `connection_memory_limit`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_connection_memory_limit


        :return: The connection_memory_limit of this ConfigurationVariables.
        :rtype: int
        """
        return self._connection_memory_limit

    @connection_memory_limit.setter
    def connection_memory_limit(self, connection_memory_limit):
        """
        Sets the connection_memory_limit of this ConfigurationVariables.
        Set the maximum amount of memory that can be used by a single user connection.

        connectionMemoryLimit corresponds to the MySQL system variable `connection_memory_limit`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_connection_memory_limit


        :param connection_memory_limit: The connection_memory_limit of this ConfigurationVariables.
        :type: int
        """
        self._connection_memory_limit = connection_memory_limit

    @property
    def default_authentication_plugin(self):
        """
        Gets the default_authentication_plugin of this ConfigurationVariables.
        (\"default_authentication_plugin\")

        Allowed values for this property are: "mysql_native_password", "sha256_password", "caching_sha2_password", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The default_authentication_plugin of this ConfigurationVariables.
        :rtype: str
        """
        return self._default_authentication_plugin

    @default_authentication_plugin.setter
    def default_authentication_plugin(self, default_authentication_plugin):
        """
        Sets the default_authentication_plugin of this ConfigurationVariables.
        (\"default_authentication_plugin\")


        :param default_authentication_plugin: The default_authentication_plugin of this ConfigurationVariables.
        :type: str
        """
        allowed_values = ["mysql_native_password", "sha256_password", "caching_sha2_password"]
        if not value_allowed_none_or_none_sentinel(default_authentication_plugin, allowed_values):
            default_authentication_plugin = 'UNKNOWN_ENUM_VALUE'
        self._default_authentication_plugin = default_authentication_plugin

    @property
    def global_connection_memory_limit(self):
        """
        Gets the global_connection_memory_limit of this ConfigurationVariables.
        Set the total amount of memory that can be used by all user connections.

        globalConnectionMemoryLimit corresponds to the MySQL system variable `global_connection_memory_limit`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_global_connection_memory_limit


        :return: The global_connection_memory_limit of this ConfigurationVariables.
        :rtype: int
        """
        return self._global_connection_memory_limit

    @global_connection_memory_limit.setter
    def global_connection_memory_limit(self, global_connection_memory_limit):
        """
        Sets the global_connection_memory_limit of this ConfigurationVariables.
        Set the total amount of memory that can be used by all user connections.

        globalConnectionMemoryLimit corresponds to the MySQL system variable `global_connection_memory_limit`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_global_connection_memory_limit


        :param global_connection_memory_limit: The global_connection_memory_limit of this ConfigurationVariables.
        :type: int
        """
        self._global_connection_memory_limit = global_connection_memory_limit

    @property
    def global_connection_memory_tracking(self):
        """
        Gets the global_connection_memory_tracking of this ConfigurationVariables.
        Determines whether the MySQL server calculates Global_connection_memory.

        globalConnectionMemoryTracking corresponds to the MySQL system variable `global_connection_memory_tracking`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_global_connection_memory_tracking


        :return: The global_connection_memory_tracking of this ConfigurationVariables.
        :rtype: bool
        """
        return self._global_connection_memory_tracking

    @global_connection_memory_tracking.setter
    def global_connection_memory_tracking(self, global_connection_memory_tracking):
        """
        Sets the global_connection_memory_tracking of this ConfigurationVariables.
        Determines whether the MySQL server calculates Global_connection_memory.

        globalConnectionMemoryTracking corresponds to the MySQL system variable `global_connection_memory_tracking`__.

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_global_connection_memory_tracking


        :param global_connection_memory_tracking: The global_connection_memory_tracking of this ConfigurationVariables.
        :type: bool
        """
        self._global_connection_memory_tracking = global_connection_memory_tracking

    @property
    def transaction_isolation(self):
        """
        Gets the transaction_isolation of this ConfigurationVariables.
        (\"transaction_isolation\")

        Allowed values for this property are: "READ-UNCOMMITTED", "READ-COMMITED", "READ-COMMITTED", "REPEATABLE-READ", "SERIALIZABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The transaction_isolation of this ConfigurationVariables.
        :rtype: str
        """
        return self._transaction_isolation

    @transaction_isolation.setter
    def transaction_isolation(self, transaction_isolation):
        """
        Sets the transaction_isolation of this ConfigurationVariables.
        (\"transaction_isolation\")


        :param transaction_isolation: The transaction_isolation of this ConfigurationVariables.
        :type: str
        """
        allowed_values = ["READ-UNCOMMITTED", "READ-COMMITED", "READ-COMMITTED", "REPEATABLE-READ", "SERIALIZABLE"]
        if not value_allowed_none_or_none_sentinel(transaction_isolation, allowed_values):
            transaction_isolation = 'UNKNOWN_ENUM_VALUE'
        self._transaction_isolation = transaction_isolation

    @property
    def innodb_ft_server_stopword_table(self):
        """
        Gets the innodb_ft_server_stopword_table of this ConfigurationVariables.
        (\"innodb_ft_server_stopword_table\")


        :return: The innodb_ft_server_stopword_table of this ConfigurationVariables.
        :rtype: str
        """
        return self._innodb_ft_server_stopword_table

    @innodb_ft_server_stopword_table.setter
    def innodb_ft_server_stopword_table(self, innodb_ft_server_stopword_table):
        """
        Sets the innodb_ft_server_stopword_table of this ConfigurationVariables.
        (\"innodb_ft_server_stopword_table\")


        :param innodb_ft_server_stopword_table: The innodb_ft_server_stopword_table of this ConfigurationVariables.
        :type: str
        """
        self._innodb_ft_server_stopword_table = innodb_ft_server_stopword_table

    @property
    def mandatory_roles(self):
        """
        Gets the mandatory_roles of this ConfigurationVariables.
        (\"mandatory_roles\")


        :return: The mandatory_roles of this ConfigurationVariables.
        :rtype: str
        """
        return self._mandatory_roles

    @mandatory_roles.setter
    def mandatory_roles(self, mandatory_roles):
        """
        Sets the mandatory_roles of this ConfigurationVariables.
        (\"mandatory_roles\")


        :param mandatory_roles: The mandatory_roles of this ConfigurationVariables.
        :type: str
        """
        self._mandatory_roles = mandatory_roles

    @property
    def autocommit(self):
        """
        Gets the autocommit of this ConfigurationVariables.
        (\"autocommit\")


        :return: The autocommit of this ConfigurationVariables.
        :rtype: bool
        """
        return self._autocommit

    @autocommit.setter
    def autocommit(self, autocommit):
        """
        Sets the autocommit of this ConfigurationVariables.
        (\"autocommit\")


        :param autocommit: The autocommit of this ConfigurationVariables.
        :type: bool
        """
        self._autocommit = autocommit

    @property
    def foreign_key_checks(self):
        """
        Gets the foreign_key_checks of this ConfigurationVariables.
        (\"foreign_key_checks\")


        :return: The foreign_key_checks of this ConfigurationVariables.
        :rtype: bool
        """
        return self._foreign_key_checks

    @foreign_key_checks.setter
    def foreign_key_checks(self, foreign_key_checks):
        """
        Sets the foreign_key_checks of this ConfigurationVariables.
        (\"foreign_key_checks\")


        :param foreign_key_checks: The foreign_key_checks of this ConfigurationVariables.
        :type: bool
        """
        self._foreign_key_checks = foreign_key_checks

    @property
    def group_replication_consistency(self):
        """
        Gets the group_replication_consistency of this ConfigurationVariables.
        - EVENTUAL:
            Both RO and RW transactions do not wait for preceding transactions to be applied before executing.
            A RW transaction does not wait for other members to apply a transaction. This means that a transaction
            could be externalized on one member before the others. This also means that in the event of a primary failover,
            the new primary can accept new RO and RW transactions before the previous primary transactions are all applied.
            RO transactions could result in outdated values, RW transactions could result in a rollback due to conflicts.
        - BEFORE_ON_PRIMARY_FAILOVER:
            New RO or RW transactions with a newly elected primary that is applying backlog from the old
            primary are held (not applied) until any backlog has been applied. This ensures that when a primary failover happens,
            intentionally or not, clients always see the latest value on the primary. This guarantees consistency, but means that
            clients must be able to handle the delay in the event that a backlog is being applied. Usually this delay should be minimal,
            but does depend on the size of the backlog.
        - BEFORE:
            A RW transaction waits for all preceding transactions to complete before being applied. A RO transaction waits for all preceding
            transactions to complete before being executed. This ensures that this transaction reads the latest value by only affecting the
            latency of the transaction. This reduces the overhead of synchronization on every RW transaction, by ensuring synchronization is
            used only on RO transactions. This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER.
        - AFTER:
            A RW transaction waits until its changes have been applied to all of the other members. This value has no effect on RO transactions.
            This mode ensures that when a transaction is committed on the local member, any subsequent transaction reads the written value or
            a more recent value on any group member. Use this mode with a group that is used for predominantly RO operations to ensure that
            applied RW transactions are applied everywhere once they commit. This could be used by your application to ensure that subsequent
            reads fetch the latest data which includes the latest writes. This reduces the overhead of synchronization on every RO transaction,
            by ensuring synchronization is used only on RW transactions. This consistency level also includes the consistency guarantees
            provided by BEFORE_ON_PRIMARY_FAILOVER.
        - BEFORE_AND_AFTER:
            A RW transaction waits for 1) all preceding transactions to complete before being applied and 2) until its changes have been
            applied on other members. A RO transaction waits for all preceding transactions to complete before execution takes place.
            This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER.

        Allowed values for this property are: "EVENTUAL", "BEFORE_ON_PRIMARY_FAILOVER", "BEFORE", "AFTER", "BEFORE_AND_AFTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The group_replication_consistency of this ConfigurationVariables.
        :rtype: str
        """
        return self._group_replication_consistency

    @group_replication_consistency.setter
    def group_replication_consistency(self, group_replication_consistency):
        """
        Sets the group_replication_consistency of this ConfigurationVariables.
        - EVENTUAL:
            Both RO and RW transactions do not wait for preceding transactions to be applied before executing.
            A RW transaction does not wait for other members to apply a transaction. This means that a transaction
            could be externalized on one member before the others. This also means that in the event of a primary failover,
            the new primary can accept new RO and RW transactions before the previous primary transactions are all applied.
            RO transactions could result in outdated values, RW transactions could result in a rollback due to conflicts.
        - BEFORE_ON_PRIMARY_FAILOVER:
            New RO or RW transactions with a newly elected primary that is applying backlog from the old
            primary are held (not applied) until any backlog has been applied. This ensures that when a primary failover happens,
            intentionally or not, clients always see the latest value on the primary. This guarantees consistency, but means that
            clients must be able to handle the delay in the event that a backlog is being applied. Usually this delay should be minimal,
            but does depend on the size of the backlog.
        - BEFORE:
            A RW transaction waits for all preceding transactions to complete before being applied. A RO transaction waits for all preceding
            transactions to complete before being executed. This ensures that this transaction reads the latest value by only affecting the
            latency of the transaction. This reduces the overhead of synchronization on every RW transaction, by ensuring synchronization is
            used only on RO transactions. This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER.
        - AFTER:
            A RW transaction waits until its changes have been applied to all of the other members. This value has no effect on RO transactions.
            This mode ensures that when a transaction is committed on the local member, any subsequent transaction reads the written value or
            a more recent value on any group member. Use this mode with a group that is used for predominantly RO operations to ensure that
            applied RW transactions are applied everywhere once they commit. This could be used by your application to ensure that subsequent
            reads fetch the latest data which includes the latest writes. This reduces the overhead of synchronization on every RO transaction,
            by ensuring synchronization is used only on RW transactions. This consistency level also includes the consistency guarantees
            provided by BEFORE_ON_PRIMARY_FAILOVER.
        - BEFORE_AND_AFTER:
            A RW transaction waits for 1) all preceding transactions to complete before being applied and 2) until its changes have been
            applied on other members. A RO transaction waits for all preceding transactions to complete before execution takes place.
            This consistency level also includes the consistency guarantees provided by BEFORE_ON_PRIMARY_FAILOVER.


        :param group_replication_consistency: The group_replication_consistency of this ConfigurationVariables.
        :type: str
        """
        allowed_values = ["EVENTUAL", "BEFORE_ON_PRIMARY_FAILOVER", "BEFORE", "AFTER", "BEFORE_AND_AFTER"]
        if not value_allowed_none_or_none_sentinel(group_replication_consistency, allowed_values):
            group_replication_consistency = 'UNKNOWN_ENUM_VALUE'
        self._group_replication_consistency = group_replication_consistency

    @property
    def innodb_ft_enable_stopword(self):
        """
        Gets the innodb_ft_enable_stopword of this ConfigurationVariables.
        (\"innodb_ft_enable_stopword\")


        :return: The innodb_ft_enable_stopword of this ConfigurationVariables.
        :rtype: bool
        """
        return self._innodb_ft_enable_stopword

    @innodb_ft_enable_stopword.setter
    def innodb_ft_enable_stopword(self, innodb_ft_enable_stopword):
        """
        Sets the innodb_ft_enable_stopword of this ConfigurationVariables.
        (\"innodb_ft_enable_stopword\")


        :param innodb_ft_enable_stopword: The innodb_ft_enable_stopword of this ConfigurationVariables.
        :type: bool
        """
        self._innodb_ft_enable_stopword = innodb_ft_enable_stopword

    @property
    def innodb_log_writer_threads(self):
        """
        Gets the innodb_log_writer_threads of this ConfigurationVariables.
        Enables dedicated log writer threads for writing redo log records from the log buffer to the system buffers and flushing the system buffers to the redo log files.

        This is the MySQL variable \"innodb_log_writer_threads\". For more information, please see the `MySQL documentation`__

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_writer_threads


        :return: The innodb_log_writer_threads of this ConfigurationVariables.
        :rtype: bool
        """
        return self._innodb_log_writer_threads

    @innodb_log_writer_threads.setter
    def innodb_log_writer_threads(self, innodb_log_writer_threads):
        """
        Sets the innodb_log_writer_threads of this ConfigurationVariables.
        Enables dedicated log writer threads for writing redo log records from the log buffer to the system buffers and flushing the system buffers to the redo log files.

        This is the MySQL variable \"innodb_log_writer_threads\". For more information, please see the `MySQL documentation`__

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_writer_threads


        :param innodb_log_writer_threads: The innodb_log_writer_threads of this ConfigurationVariables.
        :type: bool
        """
        self._innodb_log_writer_threads = innodb_log_writer_threads

    @property
    def local_infile(self):
        """
        Gets the local_infile of this ConfigurationVariables.
        (\"local_infile\")


        :return: The local_infile of this ConfigurationVariables.
        :rtype: bool
        """
        return self._local_infile

    @local_infile.setter
    def local_infile(self, local_infile):
        """
        Sets the local_infile of this ConfigurationVariables.
        (\"local_infile\")


        :param local_infile: The local_infile of this ConfigurationVariables.
        :type: bool
        """
        self._local_infile = local_infile

    @property
    def mysql_firewall_mode(self):
        """
        Gets the mysql_firewall_mode of this ConfigurationVariables.
        (\"mysql_firewall_mode\")


        :return: The mysql_firewall_mode of this ConfigurationVariables.
        :rtype: bool
        """
        return self._mysql_firewall_mode

    @mysql_firewall_mode.setter
    def mysql_firewall_mode(self, mysql_firewall_mode):
        """
        Sets the mysql_firewall_mode of this ConfigurationVariables.
        (\"mysql_firewall_mode\")


        :param mysql_firewall_mode: The mysql_firewall_mode of this ConfigurationVariables.
        :type: bool
        """
        self._mysql_firewall_mode = mysql_firewall_mode

    @property
    def mysqlx_enable_hello_notice(self):
        """
        Gets the mysqlx_enable_hello_notice of this ConfigurationVariables.
        (\"mysqlx_enable_hello_notice\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_enable_hello_notice of this ConfigurationVariables.
        :rtype: bool
        """
        return self._mysqlx_enable_hello_notice

    @mysqlx_enable_hello_notice.setter
    def mysqlx_enable_hello_notice(self, mysqlx_enable_hello_notice):
        """
        Sets the mysqlx_enable_hello_notice of this ConfigurationVariables.
        (\"mysqlx_enable_hello_notice\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_enable_hello_notice: The mysqlx_enable_hello_notice of this ConfigurationVariables.
        :type: bool
        """
        self._mysqlx_enable_hello_notice = mysqlx_enable_hello_notice

    @property
    def sql_require_primary_key(self):
        """
        Gets the sql_require_primary_key of this ConfigurationVariables.
        (\"sql_require_primary_key\")


        :return: The sql_require_primary_key of this ConfigurationVariables.
        :rtype: bool
        """
        return self._sql_require_primary_key

    @sql_require_primary_key.setter
    def sql_require_primary_key(self, sql_require_primary_key):
        """
        Sets the sql_require_primary_key of this ConfigurationVariables.
        (\"sql_require_primary_key\")


        :param sql_require_primary_key: The sql_require_primary_key of this ConfigurationVariables.
        :type: bool
        """
        self._sql_require_primary_key = sql_require_primary_key

    @property
    def sql_warnings(self):
        """
        Gets the sql_warnings of this ConfigurationVariables.
        (\"sql_warnings\")


        :return: The sql_warnings of this ConfigurationVariables.
        :rtype: bool
        """
        return self._sql_warnings

    @sql_warnings.setter
    def sql_warnings(self, sql_warnings):
        """
        Sets the sql_warnings of this ConfigurationVariables.
        (\"sql_warnings\")


        :param sql_warnings: The sql_warnings of this ConfigurationVariables.
        :type: bool
        """
        self._sql_warnings = sql_warnings

    @property
    def binlog_expire_logs_seconds(self):
        """
        Gets the binlog_expire_logs_seconds of this ConfigurationVariables.
        Sets the binary log expiration period in seconds.
        binlogExpireLogsSeconds corresponds to the MySQL binary logging system variable `binlog_expire_logs_seconds`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds


        :return: The binlog_expire_logs_seconds of this ConfigurationVariables.
        :rtype: int
        """
        return self._binlog_expire_logs_seconds

    @binlog_expire_logs_seconds.setter
    def binlog_expire_logs_seconds(self, binlog_expire_logs_seconds):
        """
        Sets the binlog_expire_logs_seconds of this ConfigurationVariables.
        Sets the binary log expiration period in seconds.
        binlogExpireLogsSeconds corresponds to the MySQL binary logging system variable `binlog_expire_logs_seconds`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_expire_logs_seconds


        :param binlog_expire_logs_seconds: The binlog_expire_logs_seconds of this ConfigurationVariables.
        :type: int
        """
        self._binlog_expire_logs_seconds = binlog_expire_logs_seconds

    @property
    def binlog_row_metadata(self):
        """
        Gets the binlog_row_metadata of this ConfigurationVariables.
        Configures the amount of table metadata added to the binary log when using row-based logging.
        binlogRowMetadata corresponds to the MySQL binary logging system variable `binlog_row_metadata`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_metadata

        Allowed values for this property are: "FULL", "MINIMAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The binlog_row_metadata of this ConfigurationVariables.
        :rtype: str
        """
        return self._binlog_row_metadata

    @binlog_row_metadata.setter
    def binlog_row_metadata(self, binlog_row_metadata):
        """
        Sets the binlog_row_metadata of this ConfigurationVariables.
        Configures the amount of table metadata added to the binary log when using row-based logging.
        binlogRowMetadata corresponds to the MySQL binary logging system variable `binlog_row_metadata`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_metadata


        :param binlog_row_metadata: The binlog_row_metadata of this ConfigurationVariables.
        :type: str
        """
        allowed_values = ["FULL", "MINIMAL"]
        if not value_allowed_none_or_none_sentinel(binlog_row_metadata, allowed_values):
            binlog_row_metadata = 'UNKNOWN_ENUM_VALUE'
        self._binlog_row_metadata = binlog_row_metadata

    @property
    def binlog_row_value_options(self):
        """
        Gets the binlog_row_value_options of this ConfigurationVariables.
        When set to PARTIAL_JSON, this enables use of a space-efficient binary log format for updates that modify only a small portion of a JSON document.
        binlogRowValueOptions corresponds to the MySQL binary logging system variable `binlog_row_value_options`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_value_options


        :return: The binlog_row_value_options of this ConfigurationVariables.
        :rtype: str
        """
        return self._binlog_row_value_options

    @binlog_row_value_options.setter
    def binlog_row_value_options(self, binlog_row_value_options):
        """
        Sets the binlog_row_value_options of this ConfigurationVariables.
        When set to PARTIAL_JSON, this enables use of a space-efficient binary log format for updates that modify only a small portion of a JSON document.
        binlogRowValueOptions corresponds to the MySQL binary logging system variable `binlog_row_value_options`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_row_value_options


        :param binlog_row_value_options: The binlog_row_value_options of this ConfigurationVariables.
        :type: str
        """
        self._binlog_row_value_options = binlog_row_value_options

    @property
    def binlog_transaction_compression(self):
        """
        Gets the binlog_transaction_compression of this ConfigurationVariables.
        Enables compression for transactions that are written to binary log files on this server.
        binlogTransactionCompression corresponds to the MySQL binary logging system variable `binlog_transaction_compression`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_transaction_compression


        :return: The binlog_transaction_compression of this ConfigurationVariables.
        :rtype: bool
        """
        return self._binlog_transaction_compression

    @binlog_transaction_compression.setter
    def binlog_transaction_compression(self, binlog_transaction_compression):
        """
        Sets the binlog_transaction_compression of this ConfigurationVariables.
        Enables compression for transactions that are written to binary log files on this server.
        binlogTransactionCompression corresponds to the MySQL binary logging system variable `binlog_transaction_compression`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_transaction_compression


        :param binlog_transaction_compression: The binlog_transaction_compression of this ConfigurationVariables.
        :type: bool
        """
        self._binlog_transaction_compression = binlog_transaction_compression

    @property
    def innodb_buffer_pool_size(self):
        """
        Gets the innodb_buffer_pool_size of this ConfigurationVariables.
        The size (in bytes) of the buffer pool, that is, the memory area where InnoDB caches table and index data.

        innodbBufferPoolSize corresponds to the MySQL server system variable
        `innodb_buffer_pool_size`__.

        The default and maximum values depend on the amount of RAM provisioned by the shape.
        See `Default User Variables`__.

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size
        __ https://docs.cloud.oracle.com/mysql-database/doc/configuring-db-system.html#GUID-B5504C19-F6F4-4DAB-8506-189A4E8F4A6A


        :return: The innodb_buffer_pool_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_buffer_pool_size

    @innodb_buffer_pool_size.setter
    def innodb_buffer_pool_size(self, innodb_buffer_pool_size):
        """
        Sets the innodb_buffer_pool_size of this ConfigurationVariables.
        The size (in bytes) of the buffer pool, that is, the memory area where InnoDB caches table and index data.

        innodbBufferPoolSize corresponds to the MySQL server system variable
        `innodb_buffer_pool_size`__.

        The default and maximum values depend on the amount of RAM provisioned by the shape.
        See `Default User Variables`__.

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size
        __ https://docs.cloud.oracle.com/mysql-database/doc/configuring-db-system.html#GUID-B5504C19-F6F4-4DAB-8506-189A4E8F4A6A


        :param innodb_buffer_pool_size: The innodb_buffer_pool_size of this ConfigurationVariables.
        :type: int
        """
        self._innodb_buffer_pool_size = innodb_buffer_pool_size

    @property
    def innodb_ft_result_cache_limit(self):
        """
        Gets the innodb_ft_result_cache_limit of this ConfigurationVariables.
        (\"innodb_ft_result_cache_limit\")


        :return: The innodb_ft_result_cache_limit of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_ft_result_cache_limit

    @innodb_ft_result_cache_limit.setter
    def innodb_ft_result_cache_limit(self, innodb_ft_result_cache_limit):
        """
        Sets the innodb_ft_result_cache_limit of this ConfigurationVariables.
        (\"innodb_ft_result_cache_limit\")


        :param innodb_ft_result_cache_limit: The innodb_ft_result_cache_limit of this ConfigurationVariables.
        :type: int
        """
        self._innodb_ft_result_cache_limit = innodb_ft_result_cache_limit

    @property
    def max_binlog_cache_size(self):
        """
        Gets the max_binlog_cache_size of this ConfigurationVariables.
        Sets the size of the transaction cache.

        maxBinlogCacheSize corresponds to the MySQL server system variable `max_binlog_cache_size`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_max_binlog_cache_size


        :return: The max_binlog_cache_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._max_binlog_cache_size

    @max_binlog_cache_size.setter
    def max_binlog_cache_size(self, max_binlog_cache_size):
        """
        Sets the max_binlog_cache_size of this ConfigurationVariables.
        Sets the size of the transaction cache.

        maxBinlogCacheSize corresponds to the MySQL server system variable `max_binlog_cache_size`__.

        __ https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_max_binlog_cache_size


        :param max_binlog_cache_size: The max_binlog_cache_size of this ConfigurationVariables.
        :type: int
        """
        self._max_binlog_cache_size = max_binlog_cache_size

    @property
    def max_connect_errors(self):
        """
        Gets the max_connect_errors of this ConfigurationVariables.
        (\"max_connect_errors\")


        :return: The max_connect_errors of this ConfigurationVariables.
        :rtype: int
        """
        return self._max_connect_errors

    @max_connect_errors.setter
    def max_connect_errors(self, max_connect_errors):
        """
        Sets the max_connect_errors of this ConfigurationVariables.
        (\"max_connect_errors\")


        :param max_connect_errors: The max_connect_errors of this ConfigurationVariables.
        :type: int
        """
        self._max_connect_errors = max_connect_errors

    @property
    def max_heap_table_size(self):
        """
        Gets the max_heap_table_size of this ConfigurationVariables.
        This variable sets the maximum size to which user-created MEMORY tables are permitted to grow.

        maxHeapTableSize corresponds to the MySQL system variable
        `max_heap_table_size`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_heap_table_size


        :return: The max_heap_table_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._max_heap_table_size

    @max_heap_table_size.setter
    def max_heap_table_size(self, max_heap_table_size):
        """
        Sets the max_heap_table_size of this ConfigurationVariables.
        This variable sets the maximum size to which user-created MEMORY tables are permitted to grow.

        maxHeapTableSize corresponds to the MySQL system variable
        `max_heap_table_size`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_max_heap_table_size


        :param max_heap_table_size: The max_heap_table_size of this ConfigurationVariables.
        :type: int
        """
        self._max_heap_table_size = max_heap_table_size

    @property
    def max_connections(self):
        """
        Gets the max_connections of this ConfigurationVariables.
        (\"max_connections\")


        :return: The max_connections of this ConfigurationVariables.
        :rtype: int
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """
        Sets the max_connections of this ConfigurationVariables.
        (\"max_connections\")


        :param max_connections: The max_connections of this ConfigurationVariables.
        :type: int
        """
        self._max_connections = max_connections

    @property
    def max_prepared_stmt_count(self):
        """
        Gets the max_prepared_stmt_count of this ConfigurationVariables.
        (\"max_prepared_stmt_count\")


        :return: The max_prepared_stmt_count of this ConfigurationVariables.
        :rtype: int
        """
        return self._max_prepared_stmt_count

    @max_prepared_stmt_count.setter
    def max_prepared_stmt_count(self, max_prepared_stmt_count):
        """
        Sets the max_prepared_stmt_count of this ConfigurationVariables.
        (\"max_prepared_stmt_count\")


        :param max_prepared_stmt_count: The max_prepared_stmt_count of this ConfigurationVariables.
        :type: int
        """
        self._max_prepared_stmt_count = max_prepared_stmt_count

    @property
    def connect_timeout(self):
        """
        Gets the connect_timeout of this ConfigurationVariables.
        The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake.

        connectTimeout corresponds to the MySQL system variable
        `connect_timeout`__

        Increasing the connect_timeout value might help if clients frequently encounter errors of the form
        \"Lost connection to MySQL server at 'XXX', system error: errno\".

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_connect_timeout


        :return: The connect_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """
        Sets the connect_timeout of this ConfigurationVariables.
        The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake.

        connectTimeout corresponds to the MySQL system variable
        `connect_timeout`__

        Increasing the connect_timeout value might help if clients frequently encounter errors of the form
        \"Lost connection to MySQL server at 'XXX', system error: errno\".

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_connect_timeout


        :param connect_timeout: The connect_timeout of this ConfigurationVariables.
        :type: int
        """
        self._connect_timeout = connect_timeout

    @property
    def cte_max_recursion_depth(self):
        """
        Gets the cte_max_recursion_depth of this ConfigurationVariables.
        (\"cte_max_recursion_depth\")


        :return: The cte_max_recursion_depth of this ConfigurationVariables.
        :rtype: int
        """
        return self._cte_max_recursion_depth

    @cte_max_recursion_depth.setter
    def cte_max_recursion_depth(self, cte_max_recursion_depth):
        """
        Sets the cte_max_recursion_depth of this ConfigurationVariables.
        (\"cte_max_recursion_depth\")


        :param cte_max_recursion_depth: The cte_max_recursion_depth of this ConfigurationVariables.
        :type: int
        """
        self._cte_max_recursion_depth = cte_max_recursion_depth

    @property
    def generated_random_password_length(self):
        """
        Gets the generated_random_password_length of this ConfigurationVariables.
        (\"generated_random_password_length\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The generated_random_password_length of this ConfigurationVariables.
        :rtype: int
        """
        return self._generated_random_password_length

    @generated_random_password_length.setter
    def generated_random_password_length(self, generated_random_password_length):
        """
        Sets the generated_random_password_length of this ConfigurationVariables.
        (\"generated_random_password_length\") DEPRECATED -- variable should not be settable and will be ignored


        :param generated_random_password_length: The generated_random_password_length of this ConfigurationVariables.
        :type: int
        """
        self._generated_random_password_length = generated_random_password_length

    @property
    def information_schema_stats_expiry(self):
        """
        Gets the information_schema_stats_expiry of this ConfigurationVariables.
        (\"information_schema_stats_expiry\")


        :return: The information_schema_stats_expiry of this ConfigurationVariables.
        :rtype: int
        """
        return self._information_schema_stats_expiry

    @information_schema_stats_expiry.setter
    def information_schema_stats_expiry(self, information_schema_stats_expiry):
        """
        Sets the information_schema_stats_expiry of this ConfigurationVariables.
        (\"information_schema_stats_expiry\")


        :param information_schema_stats_expiry: The information_schema_stats_expiry of this ConfigurationVariables.
        :type: int
        """
        self._information_schema_stats_expiry = information_schema_stats_expiry

    @property
    def innodb_buffer_pool_dump_pct(self):
        """
        Gets the innodb_buffer_pool_dump_pct of this ConfigurationVariables.
        Specifies the percentage of the most recently used pages for each buffer pool to read out and dump.

        innodbBufferPoolDumpPct corresponds to the MySQL InnoDB system variable
        `innodb_buffer_pool_dump_pct`__.

        The range is 1 to 100. The default value is 25.

        For example, if there are 4 buffer pools with 100 pages each, and innodb_buffer_pool_dump_pct is set to 25,
        the 25 most recently used pages from each buffer pool are dumped.

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_dump_pct


        :return: The innodb_buffer_pool_dump_pct of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_buffer_pool_dump_pct

    @innodb_buffer_pool_dump_pct.setter
    def innodb_buffer_pool_dump_pct(self, innodb_buffer_pool_dump_pct):
        """
        Sets the innodb_buffer_pool_dump_pct of this ConfigurationVariables.
        Specifies the percentage of the most recently used pages for each buffer pool to read out and dump.

        innodbBufferPoolDumpPct corresponds to the MySQL InnoDB system variable
        `innodb_buffer_pool_dump_pct`__.

        The range is 1 to 100. The default value is 25.

        For example, if there are 4 buffer pools with 100 pages each, and innodb_buffer_pool_dump_pct is set to 25,
        the 25 most recently used pages from each buffer pool are dumped.

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_dump_pct


        :param innodb_buffer_pool_dump_pct: The innodb_buffer_pool_dump_pct of this ConfigurationVariables.
        :type: int
        """
        self._innodb_buffer_pool_dump_pct = innodb_buffer_pool_dump_pct

    @property
    def innodb_buffer_pool_instances(self):
        """
        Gets the innodb_buffer_pool_instances of this ConfigurationVariables.
        (\"innodb_buffer_pool_instances\")


        :return: The innodb_buffer_pool_instances of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_buffer_pool_instances

    @innodb_buffer_pool_instances.setter
    def innodb_buffer_pool_instances(self, innodb_buffer_pool_instances):
        """
        Sets the innodb_buffer_pool_instances of this ConfigurationVariables.
        (\"innodb_buffer_pool_instances\")


        :param innodb_buffer_pool_instances: The innodb_buffer_pool_instances of this ConfigurationVariables.
        :type: int
        """
        self._innodb_buffer_pool_instances = innodb_buffer_pool_instances

    @property
    def innodb_ddl_buffer_size(self):
        """
        Gets the innodb_ddl_buffer_size of this ConfigurationVariables.
        innodbDdlBufferSize corresponds to the MySQL system variable `innodb_ddl_buffer_size]`__

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_ddl_buffer_size


        :return: The innodb_ddl_buffer_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_ddl_buffer_size

    @innodb_ddl_buffer_size.setter
    def innodb_ddl_buffer_size(self, innodb_ddl_buffer_size):
        """
        Sets the innodb_ddl_buffer_size of this ConfigurationVariables.
        innodbDdlBufferSize corresponds to the MySQL system variable `innodb_ddl_buffer_size]`__

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_ddl_buffer_size


        :param innodb_ddl_buffer_size: The innodb_ddl_buffer_size of this ConfigurationVariables.
        :type: int
        """
        self._innodb_ddl_buffer_size = innodb_ddl_buffer_size

    @property
    def innodb_ddl_threads(self):
        """
        Gets the innodb_ddl_threads of this ConfigurationVariables.
        innodbDdlThreads corresponds to the MySQL system variable `innodb_ddl_threads]`__

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_ddl_threads


        :return: The innodb_ddl_threads of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_ddl_threads

    @innodb_ddl_threads.setter
    def innodb_ddl_threads(self, innodb_ddl_threads):
        """
        Sets the innodb_ddl_threads of this ConfigurationVariables.
        innodbDdlThreads corresponds to the MySQL system variable `innodb_ddl_threads]`__

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_ddl_threads


        :param innodb_ddl_threads: The innodb_ddl_threads of this ConfigurationVariables.
        :type: int
        """
        self._innodb_ddl_threads = innodb_ddl_threads

    @property
    def innodb_ft_max_token_size(self):
        """
        Gets the innodb_ft_max_token_size of this ConfigurationVariables.
        (\"innodb_ft_max_token_size\")


        :return: The innodb_ft_max_token_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_ft_max_token_size

    @innodb_ft_max_token_size.setter
    def innodb_ft_max_token_size(self, innodb_ft_max_token_size):
        """
        Sets the innodb_ft_max_token_size of this ConfigurationVariables.
        (\"innodb_ft_max_token_size\")


        :param innodb_ft_max_token_size: The innodb_ft_max_token_size of this ConfigurationVariables.
        :type: int
        """
        self._innodb_ft_max_token_size = innodb_ft_max_token_size

    @property
    def innodb_ft_min_token_size(self):
        """
        Gets the innodb_ft_min_token_size of this ConfigurationVariables.
        (\"innodb_ft_min_token_size\")


        :return: The innodb_ft_min_token_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_ft_min_token_size

    @innodb_ft_min_token_size.setter
    def innodb_ft_min_token_size(self, innodb_ft_min_token_size):
        """
        Sets the innodb_ft_min_token_size of this ConfigurationVariables.
        (\"innodb_ft_min_token_size\")


        :param innodb_ft_min_token_size: The innodb_ft_min_token_size of this ConfigurationVariables.
        :type: int
        """
        self._innodb_ft_min_token_size = innodb_ft_min_token_size

    @property
    def innodb_ft_num_word_optimize(self):
        """
        Gets the innodb_ft_num_word_optimize of this ConfigurationVariables.
        (\"innodb_ft_num_word_optimize\")


        :return: The innodb_ft_num_word_optimize of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_ft_num_word_optimize

    @innodb_ft_num_word_optimize.setter
    def innodb_ft_num_word_optimize(self, innodb_ft_num_word_optimize):
        """
        Sets the innodb_ft_num_word_optimize of this ConfigurationVariables.
        (\"innodb_ft_num_word_optimize\")


        :param innodb_ft_num_word_optimize: The innodb_ft_num_word_optimize of this ConfigurationVariables.
        :type: int
        """
        self._innodb_ft_num_word_optimize = innodb_ft_num_word_optimize

    @property
    def innodb_lock_wait_timeout(self):
        """
        Gets the innodb_lock_wait_timeout of this ConfigurationVariables.
        (\"innodb_lock_wait_timeout\")


        :return: The innodb_lock_wait_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_lock_wait_timeout

    @innodb_lock_wait_timeout.setter
    def innodb_lock_wait_timeout(self, innodb_lock_wait_timeout):
        """
        Sets the innodb_lock_wait_timeout of this ConfigurationVariables.
        (\"innodb_lock_wait_timeout\")


        :param innodb_lock_wait_timeout: The innodb_lock_wait_timeout of this ConfigurationVariables.
        :type: int
        """
        self._innodb_lock_wait_timeout = innodb_lock_wait_timeout

    @property
    def innodb_max_purge_lag(self):
        """
        Gets the innodb_max_purge_lag of this ConfigurationVariables.
        The desired maximum purge lag in terms of transactions.

        InnoDB maintains a list of transactions that have index records delete-marked by UPDATE or DELETE operations. The length of the list is the purge lag.

        If this value is exceeded, a delay is imposed on INSERT, UPDATE, and DELETE operations to allow time for purge to catch up.

        The default value is 0, which means there is no maximum purge lag and no delay.

        innodbMaxPurgeLag corresponds to the MySQL server system variable
        `innodb_max_purge_lag`__.

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag


        :return: The innodb_max_purge_lag of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_max_purge_lag

    @innodb_max_purge_lag.setter
    def innodb_max_purge_lag(self, innodb_max_purge_lag):
        """
        Sets the innodb_max_purge_lag of this ConfigurationVariables.
        The desired maximum purge lag in terms of transactions.

        InnoDB maintains a list of transactions that have index records delete-marked by UPDATE or DELETE operations. The length of the list is the purge lag.

        If this value is exceeded, a delay is imposed on INSERT, UPDATE, and DELETE operations to allow time for purge to catch up.

        The default value is 0, which means there is no maximum purge lag and no delay.

        innodbMaxPurgeLag corresponds to the MySQL server system variable
        `innodb_max_purge_lag`__.

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag


        :param innodb_max_purge_lag: The innodb_max_purge_lag of this ConfigurationVariables.
        :type: int
        """
        self._innodb_max_purge_lag = innodb_max_purge_lag

    @property
    def innodb_max_purge_lag_delay(self):
        """
        Gets the innodb_max_purge_lag_delay of this ConfigurationVariables.
        The maximum delay in microseconds for the delay imposed when the innodb_max_purge_lag threshold is exceeded.

        The specified innodb_max_purge_lag_delay value is an upper limit on the delay period.

        innodbMaxPurgeLagDelay corresponds to the MySQL server system variable
        `innodb_max_purge_lag_delay`__.

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag_delay


        :return: The innodb_max_purge_lag_delay of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_max_purge_lag_delay

    @innodb_max_purge_lag_delay.setter
    def innodb_max_purge_lag_delay(self, innodb_max_purge_lag_delay):
        """
        Sets the innodb_max_purge_lag_delay of this ConfigurationVariables.
        The maximum delay in microseconds for the delay imposed when the innodb_max_purge_lag threshold is exceeded.

        The specified innodb_max_purge_lag_delay value is an upper limit on the delay period.

        innodbMaxPurgeLagDelay corresponds to the MySQL server system variable
        `innodb_max_purge_lag_delay`__.

        __ https://dev.mysql.com/doc/refman/en/innodb-parameters.html#sysvar_innodb_max_purge_lag_delay


        :param innodb_max_purge_lag_delay: The innodb_max_purge_lag_delay of this ConfigurationVariables.
        :type: int
        """
        self._innodb_max_purge_lag_delay = innodb_max_purge_lag_delay

    @property
    def interactive_timeout(self):
        """
        Gets the interactive_timeout of this ConfigurationVariables.
        The number of seconds the server waits for activity on an interactive connection before closing it.

        interactiveTimeout corresponds to the MySQL system variable.
        `interactive_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_interactive_timeout


        :return: The interactive_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._interactive_timeout

    @interactive_timeout.setter
    def interactive_timeout(self, interactive_timeout):
        """
        Sets the interactive_timeout of this ConfigurationVariables.
        The number of seconds the server waits for activity on an interactive connection before closing it.

        interactiveTimeout corresponds to the MySQL system variable.
        `interactive_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_interactive_timeout


        :param interactive_timeout: The interactive_timeout of this ConfigurationVariables.
        :type: int
        """
        self._interactive_timeout = interactive_timeout

    @property
    def innodb_stats_persistent_sample_pages(self):
        """
        Gets the innodb_stats_persistent_sample_pages of this ConfigurationVariables.
        The number of index pages to sample when estimating cardinality and other statistics for an indexed column,
        such as those calculated by ANALYZE TABLE.

        innodbStatsPersistentSamplePages corresponds to the MySQL InnoDB system variable
        `innodb_stats_persistent_sample_pages`__

        innodb_stats_persistent_sample_pages only applies when innodb_stats_persistent is enabled for a table;
        when innodb_stats_persistent is disabled, innodb_stats_transient_sample_pages applies instead.

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_stats_persistent_sample_pages


        :return: The innodb_stats_persistent_sample_pages of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_stats_persistent_sample_pages

    @innodb_stats_persistent_sample_pages.setter
    def innodb_stats_persistent_sample_pages(self, innodb_stats_persistent_sample_pages):
        """
        Sets the innodb_stats_persistent_sample_pages of this ConfigurationVariables.
        The number of index pages to sample when estimating cardinality and other statistics for an indexed column,
        such as those calculated by ANALYZE TABLE.

        innodbStatsPersistentSamplePages corresponds to the MySQL InnoDB system variable
        `innodb_stats_persistent_sample_pages`__

        innodb_stats_persistent_sample_pages only applies when innodb_stats_persistent is enabled for a table;
        when innodb_stats_persistent is disabled, innodb_stats_transient_sample_pages applies instead.

        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_stats_persistent_sample_pages


        :param innodb_stats_persistent_sample_pages: The innodb_stats_persistent_sample_pages of this ConfigurationVariables.
        :type: int
        """
        self._innodb_stats_persistent_sample_pages = innodb_stats_persistent_sample_pages

    @property
    def innodb_stats_transient_sample_pages(self):
        """
        Gets the innodb_stats_transient_sample_pages of this ConfigurationVariables.
        The number of index pages to sample when estimating cardinality and other statistics for an indexed column,
        such as those calculated by `ANALYZE TABLE`__.

        innodbStatsTransientSamplePages corresponds to the MySQL InnoDB system variable
        `innodb_stats_transient_sample_pages`__

        innodb_stats_transient_sample_pages only applies when innodb_stats_persistent is disabled for a table;
        when innodb_stats_persistent is enabled, innodb_stats_persistent_sample_pages applies instead.

        innodb_stats_persistent is ON by default and cannot be changed. It is possible to override it using the
        STATS_PERSISTENT clause of the `CREATE TABLE`__ and
        `ALTER TABLE`__ statements.

        __ https://dev.mysql.com/doc/refman/8.0/en/analyze-table.html
        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_stats_transient_sample_pages
        __ https://dev.mysql.com/doc/refman/8.0/en/create-table.html
        __ https://dev.mysql.com/doc/refman/8.0/en/alter-table.html


        :return: The innodb_stats_transient_sample_pages of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_stats_transient_sample_pages

    @innodb_stats_transient_sample_pages.setter
    def innodb_stats_transient_sample_pages(self, innodb_stats_transient_sample_pages):
        """
        Sets the innodb_stats_transient_sample_pages of this ConfigurationVariables.
        The number of index pages to sample when estimating cardinality and other statistics for an indexed column,
        such as those calculated by `ANALYZE TABLE`__.

        innodbStatsTransientSamplePages corresponds to the MySQL InnoDB system variable
        `innodb_stats_transient_sample_pages`__

        innodb_stats_transient_sample_pages only applies when innodb_stats_persistent is disabled for a table;
        when innodb_stats_persistent is enabled, innodb_stats_persistent_sample_pages applies instead.

        innodb_stats_persistent is ON by default and cannot be changed. It is possible to override it using the
        STATS_PERSISTENT clause of the `CREATE TABLE`__ and
        `ALTER TABLE`__ statements.

        __ https://dev.mysql.com/doc/refman/8.0/en/analyze-table.html
        __ https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_stats_transient_sample_pages
        __ https://dev.mysql.com/doc/refman/8.0/en/create-table.html
        __ https://dev.mysql.com/doc/refman/8.0/en/alter-table.html


        :param innodb_stats_transient_sample_pages: The innodb_stats_transient_sample_pages of this ConfigurationVariables.
        :type: int
        """
        self._innodb_stats_transient_sample_pages = innodb_stats_transient_sample_pages

    @property
    def max_allowed_packet(self):
        """
        Gets the max_allowed_packet of this ConfigurationVariables.
        The maximum size of one packet or any generated/intermediate string.

        This is the mysql variable \"max_allowed_packet\".


        :return: The max_allowed_packet of this ConfigurationVariables.
        :rtype: int
        """
        return self._max_allowed_packet

    @max_allowed_packet.setter
    def max_allowed_packet(self, max_allowed_packet):
        """
        Sets the max_allowed_packet of this ConfigurationVariables.
        The maximum size of one packet or any generated/intermediate string.

        This is the mysql variable \"max_allowed_packet\".


        :param max_allowed_packet: The max_allowed_packet of this ConfigurationVariables.
        :type: int
        """
        self._max_allowed_packet = max_allowed_packet

    @property
    def max_execution_time(self):
        """
        Gets the max_execution_time of this ConfigurationVariables.
        (\"max_execution_time\")


        :return: The max_execution_time of this ConfigurationVariables.
        :rtype: int
        """
        return self._max_execution_time

    @max_execution_time.setter
    def max_execution_time(self, max_execution_time):
        """
        Sets the max_execution_time of this ConfigurationVariables.
        (\"max_execution_time\")


        :param max_execution_time: The max_execution_time of this ConfigurationVariables.
        :type: int
        """
        self._max_execution_time = max_execution_time

    @property
    def mysqlx_connect_timeout(self):
        """
        Gets the mysqlx_connect_timeout of this ConfigurationVariables.
        The number of seconds X Plugin waits for the first packet to be received from newly connected clients.

        mysqlxConnectTimeout corresponds to the MySQL X Plugin system variable
        `mysqlx_connect_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_connect_timeout


        :return: The mysqlx_connect_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_connect_timeout

    @mysqlx_connect_timeout.setter
    def mysqlx_connect_timeout(self, mysqlx_connect_timeout):
        """
        Sets the mysqlx_connect_timeout of this ConfigurationVariables.
        The number of seconds X Plugin waits for the first packet to be received from newly connected clients.

        mysqlxConnectTimeout corresponds to the MySQL X Plugin system variable
        `mysqlx_connect_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_connect_timeout


        :param mysqlx_connect_timeout: The mysqlx_connect_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_connect_timeout = mysqlx_connect_timeout

    @property
    def mysqlx_document_id_unique_prefix(self):
        """
        Gets the mysqlx_document_id_unique_prefix of this ConfigurationVariables.
        (\"mysqlx_document_id_unique_prefix\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_document_id_unique_prefix of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_document_id_unique_prefix

    @mysqlx_document_id_unique_prefix.setter
    def mysqlx_document_id_unique_prefix(self, mysqlx_document_id_unique_prefix):
        """
        Sets the mysqlx_document_id_unique_prefix of this ConfigurationVariables.
        (\"mysqlx_document_id_unique_prefix\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_document_id_unique_prefix: The mysqlx_document_id_unique_prefix of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_document_id_unique_prefix = mysqlx_document_id_unique_prefix

    @property
    def mysqlx_idle_worker_thread_timeout(self):
        """
        Gets the mysqlx_idle_worker_thread_timeout of this ConfigurationVariables.
        (\"mysqlx_idle_worker_thread_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_idle_worker_thread_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_idle_worker_thread_timeout

    @mysqlx_idle_worker_thread_timeout.setter
    def mysqlx_idle_worker_thread_timeout(self, mysqlx_idle_worker_thread_timeout):
        """
        Sets the mysqlx_idle_worker_thread_timeout of this ConfigurationVariables.
        (\"mysqlx_idle_worker_thread_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_idle_worker_thread_timeout: The mysqlx_idle_worker_thread_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_idle_worker_thread_timeout = mysqlx_idle_worker_thread_timeout

    @property
    def mysqlx_interactive_timeout(self):
        """
        Gets the mysqlx_interactive_timeout of this ConfigurationVariables.
        The number of seconds to wait for interactive clients to timeout.

        mysqlxInteractiveTimeout corresponds to the MySQL X Plugin system variable.
        `mysqlx_interactive_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_interactive_timeout


        :return: The mysqlx_interactive_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_interactive_timeout

    @mysqlx_interactive_timeout.setter
    def mysqlx_interactive_timeout(self, mysqlx_interactive_timeout):
        """
        Sets the mysqlx_interactive_timeout of this ConfigurationVariables.
        The number of seconds to wait for interactive clients to timeout.

        mysqlxInteractiveTimeout corresponds to the MySQL X Plugin system variable.
        `mysqlx_interactive_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_interactive_timeout


        :param mysqlx_interactive_timeout: The mysqlx_interactive_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_interactive_timeout = mysqlx_interactive_timeout

    @property
    def mysqlx_max_allowed_packet(self):
        """
        Gets the mysqlx_max_allowed_packet of this ConfigurationVariables.
        The maximum size of network packets that can be received by X Plugin.

        This is the mysql variable \"mysqlx_max_allowed_packet\".


        :return: The mysqlx_max_allowed_packet of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_max_allowed_packet

    @mysqlx_max_allowed_packet.setter
    def mysqlx_max_allowed_packet(self, mysqlx_max_allowed_packet):
        """
        Sets the mysqlx_max_allowed_packet of this ConfigurationVariables.
        The maximum size of network packets that can be received by X Plugin.

        This is the mysql variable \"mysqlx_max_allowed_packet\".


        :param mysqlx_max_allowed_packet: The mysqlx_max_allowed_packet of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_max_allowed_packet = mysqlx_max_allowed_packet

    @property
    def mysqlx_min_worker_threads(self):
        """
        Gets the mysqlx_min_worker_threads of this ConfigurationVariables.
        (\"mysqlx_min_worker_threads\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_min_worker_threads of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_min_worker_threads

    @mysqlx_min_worker_threads.setter
    def mysqlx_min_worker_threads(self, mysqlx_min_worker_threads):
        """
        Sets the mysqlx_min_worker_threads of this ConfigurationVariables.
        (\"mysqlx_min_worker_threads\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_min_worker_threads: The mysqlx_min_worker_threads of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_min_worker_threads = mysqlx_min_worker_threads

    @property
    def mysqlx_read_timeout(self):
        """
        Gets the mysqlx_read_timeout of this ConfigurationVariables.
        The number of seconds that X Plugin waits for blocking read operations to complete. After this time, if the
        read operation is not successful, X Plugin closes the connection and returns a warning notice with the error
        code ER_IO_READ_ERROR to the client application.

        mysqlxReadTimeout corresponds to the MySQL X Plugin system variable
        `mysqlx_read_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_read_timeout


        :return: The mysqlx_read_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_read_timeout

    @mysqlx_read_timeout.setter
    def mysqlx_read_timeout(self, mysqlx_read_timeout):
        """
        Sets the mysqlx_read_timeout of this ConfigurationVariables.
        The number of seconds that X Plugin waits for blocking read operations to complete. After this time, if the
        read operation is not successful, X Plugin closes the connection and returns a warning notice with the error
        code ER_IO_READ_ERROR to the client application.

        mysqlxReadTimeout corresponds to the MySQL X Plugin system variable
        `mysqlx_read_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_read_timeout


        :param mysqlx_read_timeout: The mysqlx_read_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_read_timeout = mysqlx_read_timeout

    @property
    def mysqlx_wait_timeout(self):
        """
        Gets the mysqlx_wait_timeout of this ConfigurationVariables.
        The number of seconds that X Plugin waits for activity on a connection.

        mysqlxWaitTimeout corresponds to the MySQL X Plugin system variable.
        `mysqlx_wait_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_wait_timeout


        :return: The mysqlx_wait_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_wait_timeout

    @mysqlx_wait_timeout.setter
    def mysqlx_wait_timeout(self, mysqlx_wait_timeout):
        """
        Sets the mysqlx_wait_timeout of this ConfigurationVariables.
        The number of seconds that X Plugin waits for activity on a connection.

        mysqlxWaitTimeout corresponds to the MySQL X Plugin system variable.
        `mysqlx_wait_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_wait_timeout


        :param mysqlx_wait_timeout: The mysqlx_wait_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_wait_timeout = mysqlx_wait_timeout

    @property
    def mysqlx_write_timeout(self):
        """
        Gets the mysqlx_write_timeout of this ConfigurationVariables.
        The number of seconds that X Plugin waits for blocking write operations to complete. After this time, if the
        write operation is not successful, X Plugin closes the connection.

        mysqlxReadmysqlxWriteTimeoutTimeout corresponds to the MySQL X Plugin system variable
        `mysqlx_write_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_write_timeout


        :return: The mysqlx_write_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_write_timeout

    @mysqlx_write_timeout.setter
    def mysqlx_write_timeout(self, mysqlx_write_timeout):
        """
        Sets the mysqlx_write_timeout of this ConfigurationVariables.
        The number of seconds that X Plugin waits for blocking write operations to complete. After this time, if the
        write operation is not successful, X Plugin closes the connection.

        mysqlxReadmysqlxWriteTimeoutTimeout corresponds to the MySQL X Plugin system variable
        `mysqlx_write_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/x-plugin-options-system-variables.html#sysvar_mysqlx_write_timeout


        :param mysqlx_write_timeout: The mysqlx_write_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_write_timeout = mysqlx_write_timeout

    @property
    def net_read_timeout(self):
        """
        Gets the net_read_timeout of this ConfigurationVariables.
        The number of seconds to wait for more data from a connection before aborting the read.

        netReadTimeout corresponds to the MySQL system variable
        `net_read_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_read_timeout


        :return: The net_read_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._net_read_timeout

    @net_read_timeout.setter
    def net_read_timeout(self, net_read_timeout):
        """
        Sets the net_read_timeout of this ConfigurationVariables.
        The number of seconds to wait for more data from a connection before aborting the read.

        netReadTimeout corresponds to the MySQL system variable
        `net_read_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_read_timeout


        :param net_read_timeout: The net_read_timeout of this ConfigurationVariables.
        :type: int
        """
        self._net_read_timeout = net_read_timeout

    @property
    def net_write_timeout(self):
        """
        Gets the net_write_timeout of this ConfigurationVariables.
        The number of seconds to wait for a block to be written to a connection before aborting the write.

        netWriteTimeout corresponds to the MySQL system variable
        `net_write_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_write_timeout


        :return: The net_write_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._net_write_timeout

    @net_write_timeout.setter
    def net_write_timeout(self, net_write_timeout):
        """
        Sets the net_write_timeout of this ConfigurationVariables.
        The number of seconds to wait for a block to be written to a connection before aborting the write.

        netWriteTimeout corresponds to the MySQL system variable
        `net_write_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_net_write_timeout


        :param net_write_timeout: The net_write_timeout of this ConfigurationVariables.
        :type: int
        """
        self._net_write_timeout = net_write_timeout

    @property
    def parser_max_mem_size(self):
        """
        Gets the parser_max_mem_size of this ConfigurationVariables.
        (\"parser_max_mem_size\")


        :return: The parser_max_mem_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._parser_max_mem_size

    @parser_max_mem_size.setter
    def parser_max_mem_size(self, parser_max_mem_size):
        """
        Sets the parser_max_mem_size of this ConfigurationVariables.
        (\"parser_max_mem_size\")


        :param parser_max_mem_size: The parser_max_mem_size of this ConfigurationVariables.
        :type: int
        """
        self._parser_max_mem_size = parser_max_mem_size

    @property
    def query_alloc_block_size(self):
        """
        Gets the query_alloc_block_size of this ConfigurationVariables.
        (\"query_alloc_block_size\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The query_alloc_block_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._query_alloc_block_size

    @query_alloc_block_size.setter
    def query_alloc_block_size(self, query_alloc_block_size):
        """
        Sets the query_alloc_block_size of this ConfigurationVariables.
        (\"query_alloc_block_size\") DEPRECATED -- variable should not be settable and will be ignored


        :param query_alloc_block_size: The query_alloc_block_size of this ConfigurationVariables.
        :type: int
        """
        self._query_alloc_block_size = query_alloc_block_size

    @property
    def query_prealloc_size(self):
        """
        Gets the query_prealloc_size of this ConfigurationVariables.
        (\"query_prealloc_size\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The query_prealloc_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._query_prealloc_size

    @query_prealloc_size.setter
    def query_prealloc_size(self, query_prealloc_size):
        """
        Sets the query_prealloc_size of this ConfigurationVariables.
        (\"query_prealloc_size\") DEPRECATED -- variable should not be settable and will be ignored


        :param query_prealloc_size: The query_prealloc_size of this ConfigurationVariables.
        :type: int
        """
        self._query_prealloc_size = query_prealloc_size

    @property
    def regexp_time_limit(self):
        """
        Gets the regexp_time_limit of this ConfigurationVariables.
        regexpTimeLimit corresponds to the MySQL system variable `regexp_time_limit]`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_regexp_time_limit


        :return: The regexp_time_limit of this ConfigurationVariables.
        :rtype: int
        """
        return self._regexp_time_limit

    @regexp_time_limit.setter
    def regexp_time_limit(self, regexp_time_limit):
        """
        Sets the regexp_time_limit of this ConfigurationVariables.
        regexpTimeLimit corresponds to the MySQL system variable `regexp_time_limit]`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_regexp_time_limit


        :param regexp_time_limit: The regexp_time_limit of this ConfigurationVariables.
        :type: int
        """
        self._regexp_time_limit = regexp_time_limit

    @property
    def sql_mode(self):
        """
        Gets the sql_mode of this ConfigurationVariables.
        (\"sql_mode\")


        :return: The sql_mode of this ConfigurationVariables.
        :rtype: str
        """
        return self._sql_mode

    @sql_mode.setter
    def sql_mode(self, sql_mode):
        """
        Sets the sql_mode of this ConfigurationVariables.
        (\"sql_mode\")


        :param sql_mode: The sql_mode of this ConfigurationVariables.
        :type: str
        """
        self._sql_mode = sql_mode

    @property
    def tmp_table_size(self):
        """
        Gets the tmp_table_size of this ConfigurationVariables.
        The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables.

        tmp_table_size corresponds to the MySQL system variable
        `tmp_table_size`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size


        :return: The tmp_table_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._tmp_table_size

    @tmp_table_size.setter
    def tmp_table_size(self, tmp_table_size):
        """
        Sets the tmp_table_size of this ConfigurationVariables.
        The maximum size of internal in-memory temporary tables. This variable does not apply to user-created MEMORY tables.

        tmp_table_size corresponds to the MySQL system variable
        `tmp_table_size`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_tmp_table_size


        :param tmp_table_size: The tmp_table_size of this ConfigurationVariables.
        :type: int
        """
        self._tmp_table_size = tmp_table_size

    @property
    def mysqlx_deflate_default_compression_level(self):
        """
        Gets the mysqlx_deflate_default_compression_level of this ConfigurationVariables.
        Set the default compression level for the deflate algorithm. (\"mysqlx_deflate_default_compression_level\")


        :return: The mysqlx_deflate_default_compression_level of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_deflate_default_compression_level

    @mysqlx_deflate_default_compression_level.setter
    def mysqlx_deflate_default_compression_level(self, mysqlx_deflate_default_compression_level):
        """
        Sets the mysqlx_deflate_default_compression_level of this ConfigurationVariables.
        Set the default compression level for the deflate algorithm. (\"mysqlx_deflate_default_compression_level\")


        :param mysqlx_deflate_default_compression_level: The mysqlx_deflate_default_compression_level of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_deflate_default_compression_level = mysqlx_deflate_default_compression_level

    @property
    def mysqlx_deflate_max_client_compression_level(self):
        """
        Gets the mysqlx_deflate_max_client_compression_level of this ConfigurationVariables.
        Limit the upper bound of accepted compression levels for the deflate algorithm. (\"mysqlx_deflate_max_client_compression_level\")


        :return: The mysqlx_deflate_max_client_compression_level of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_deflate_max_client_compression_level

    @mysqlx_deflate_max_client_compression_level.setter
    def mysqlx_deflate_max_client_compression_level(self, mysqlx_deflate_max_client_compression_level):
        """
        Sets the mysqlx_deflate_max_client_compression_level of this ConfigurationVariables.
        Limit the upper bound of accepted compression levels for the deflate algorithm. (\"mysqlx_deflate_max_client_compression_level\")


        :param mysqlx_deflate_max_client_compression_level: The mysqlx_deflate_max_client_compression_level of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_deflate_max_client_compression_level = mysqlx_deflate_max_client_compression_level

    @property
    def mysqlx_lz4_max_client_compression_level(self):
        """
        Gets the mysqlx_lz4_max_client_compression_level of this ConfigurationVariables.
        Limit the upper bound of accepted compression levels for the lz4 algorithm. (\"mysqlx_lz4_max_client_compression_level\")


        :return: The mysqlx_lz4_max_client_compression_level of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_lz4_max_client_compression_level

    @mysqlx_lz4_max_client_compression_level.setter
    def mysqlx_lz4_max_client_compression_level(self, mysqlx_lz4_max_client_compression_level):
        """
        Sets the mysqlx_lz4_max_client_compression_level of this ConfigurationVariables.
        Limit the upper bound of accepted compression levels for the lz4 algorithm. (\"mysqlx_lz4_max_client_compression_level\")


        :param mysqlx_lz4_max_client_compression_level: The mysqlx_lz4_max_client_compression_level of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_lz4_max_client_compression_level = mysqlx_lz4_max_client_compression_level

    @property
    def mysqlx_lz4_default_compression_level(self):
        """
        Gets the mysqlx_lz4_default_compression_level of this ConfigurationVariables.
        Set the default compression level for the lz4 algorithm. (\"mysqlx_lz4_default_compression_level\")


        :return: The mysqlx_lz4_default_compression_level of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_lz4_default_compression_level

    @mysqlx_lz4_default_compression_level.setter
    def mysqlx_lz4_default_compression_level(self, mysqlx_lz4_default_compression_level):
        """
        Sets the mysqlx_lz4_default_compression_level of this ConfigurationVariables.
        Set the default compression level for the lz4 algorithm. (\"mysqlx_lz4_default_compression_level\")


        :param mysqlx_lz4_default_compression_level: The mysqlx_lz4_default_compression_level of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_lz4_default_compression_level = mysqlx_lz4_default_compression_level

    @property
    def mysqlx_zstd_max_client_compression_level(self):
        """
        Gets the mysqlx_zstd_max_client_compression_level of this ConfigurationVariables.
        Limit the upper bound of accepted compression levels for the zstd algorithm. (\"mysqlx_zstd_max_client_compression_level\")


        :return: The mysqlx_zstd_max_client_compression_level of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_zstd_max_client_compression_level

    @mysqlx_zstd_max_client_compression_level.setter
    def mysqlx_zstd_max_client_compression_level(self, mysqlx_zstd_max_client_compression_level):
        """
        Sets the mysqlx_zstd_max_client_compression_level of this ConfigurationVariables.
        Limit the upper bound of accepted compression levels for the zstd algorithm. (\"mysqlx_zstd_max_client_compression_level\")


        :param mysqlx_zstd_max_client_compression_level: The mysqlx_zstd_max_client_compression_level of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_zstd_max_client_compression_level = mysqlx_zstd_max_client_compression_level

    @property
    def mysqlx_zstd_default_compression_level(self):
        """
        Gets the mysqlx_zstd_default_compression_level of this ConfigurationVariables.
        Set the default compression level for the zstd algorithm. (\"mysqlx_zstd_default_compression_level\")


        :return: The mysqlx_zstd_default_compression_level of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_zstd_default_compression_level

    @mysqlx_zstd_default_compression_level.setter
    def mysqlx_zstd_default_compression_level(self, mysqlx_zstd_default_compression_level):
        """
        Sets the mysqlx_zstd_default_compression_level of this ConfigurationVariables.
        Set the default compression level for the zstd algorithm. (\"mysqlx_zstd_default_compression_level\")


        :param mysqlx_zstd_default_compression_level: The mysqlx_zstd_default_compression_level of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_zstd_default_compression_level = mysqlx_zstd_default_compression_level

    @property
    def mysql_zstd_default_compression_level(self):
        """
        Gets the mysql_zstd_default_compression_level of this ConfigurationVariables.
        DEPRECATED -- typo of mysqlx_zstd_default_compression_level. variable will be ignored.


        :return: The mysql_zstd_default_compression_level of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysql_zstd_default_compression_level

    @mysql_zstd_default_compression_level.setter
    def mysql_zstd_default_compression_level(self, mysql_zstd_default_compression_level):
        """
        Sets the mysql_zstd_default_compression_level of this ConfigurationVariables.
        DEPRECATED -- typo of mysqlx_zstd_default_compression_level. variable will be ignored.


        :param mysql_zstd_default_compression_level: The mysql_zstd_default_compression_level of this ConfigurationVariables.
        :type: int
        """
        self._mysql_zstd_default_compression_level = mysql_zstd_default_compression_level

    @property
    def sort_buffer_size(self):
        """
        Gets the sort_buffer_size of this ConfigurationVariables.
        Each session that must perform a sort allocates a buffer of this size.

        sortBufferSize corresponds to the MySQL system variable `sort_buffer_size`__

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_sort_buffer_size


        :return: The sort_buffer_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._sort_buffer_size

    @sort_buffer_size.setter
    def sort_buffer_size(self, sort_buffer_size):
        """
        Sets the sort_buffer_size of this ConfigurationVariables.
        Each session that must perform a sort allocates a buffer of this size.

        sortBufferSize corresponds to the MySQL system variable `sort_buffer_size`__

        __ https://dev.mysql.com/doc/refman/en/server-system-variables.html#sysvar_sort_buffer_size


        :param sort_buffer_size: The sort_buffer_size of this ConfigurationVariables.
        :type: int
        """
        self._sort_buffer_size = sort_buffer_size

    @property
    def wait_timeout(self):
        """
        Gets the wait_timeout of this ConfigurationVariables.
        The number of seconds the server waits for activity on a noninteractive connection before closing it.

        waitTimeout corresponds to the MySQL system variable.
        `wait_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout


        :return: The wait_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._wait_timeout

    @wait_timeout.setter
    def wait_timeout(self, wait_timeout):
        """
        Sets the wait_timeout of this ConfigurationVariables.
        The number of seconds the server waits for activity on a noninteractive connection before closing it.

        waitTimeout corresponds to the MySQL system variable.
        `wait_timeout`__

        __ https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_wait_timeout


        :param wait_timeout: The wait_timeout of this ConfigurationVariables.
        :type: int
        """
        self._wait_timeout = wait_timeout

    @property
    def thread_pool_dedicated_listeners(self):
        """
        Gets the thread_pool_dedicated_listeners of this ConfigurationVariables.
        Controls whether the thread pool uses dedicated listener threads. If enabled, a listener thread in each thread group is dedicated to the task of listening
        for network events from clients, ensuring that the maximum number of query worker threads is no more than the value specified by threadPoolMaxTransactionsLimit.
        threadPoolDedicatedListeners corresponds to the MySQL Database Service-specific system variable thread_pool_dedicated_listeners.


        :return: The thread_pool_dedicated_listeners of this ConfigurationVariables.
        :rtype: bool
        """
        return self._thread_pool_dedicated_listeners

    @thread_pool_dedicated_listeners.setter
    def thread_pool_dedicated_listeners(self, thread_pool_dedicated_listeners):
        """
        Sets the thread_pool_dedicated_listeners of this ConfigurationVariables.
        Controls whether the thread pool uses dedicated listener threads. If enabled, a listener thread in each thread group is dedicated to the task of listening
        for network events from clients, ensuring that the maximum number of query worker threads is no more than the value specified by threadPoolMaxTransactionsLimit.
        threadPoolDedicatedListeners corresponds to the MySQL Database Service-specific system variable thread_pool_dedicated_listeners.


        :param thread_pool_dedicated_listeners: The thread_pool_dedicated_listeners of this ConfigurationVariables.
        :type: bool
        """
        self._thread_pool_dedicated_listeners = thread_pool_dedicated_listeners

    @property
    def thread_pool_max_transactions_limit(self):
        """
        Gets the thread_pool_max_transactions_limit of this ConfigurationVariables.
        Limits the maximum number of open transactions to the defined value. The default value is 0, which enforces no limit.
        threadPoolMaxTransactionsLimit corresponds to the MySQL Database Service-specific system variable thread_pool_max_transactions_limit.


        :return: The thread_pool_max_transactions_limit of this ConfigurationVariables.
        :rtype: int
        """
        return self._thread_pool_max_transactions_limit

    @thread_pool_max_transactions_limit.setter
    def thread_pool_max_transactions_limit(self, thread_pool_max_transactions_limit):
        """
        Sets the thread_pool_max_transactions_limit of this ConfigurationVariables.
        Limits the maximum number of open transactions to the defined value. The default value is 0, which enforces no limit.
        threadPoolMaxTransactionsLimit corresponds to the MySQL Database Service-specific system variable thread_pool_max_transactions_limit.


        :param thread_pool_max_transactions_limit: The thread_pool_max_transactions_limit of this ConfigurationVariables.
        :type: int
        """
        self._thread_pool_max_transactions_limit = thread_pool_max_transactions_limit

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ConfigurationVariables.
        Initializes the time zone for each client that connects.

        This corresponds to the MySQL System Variable \"time_zone\".

        The values can be given in one of the following formats, none of which are case-sensitive:

        - As a string indicating an offset from UTC of the form [H]H:MM, prefixed with a + or -, such as '+10:00', '-6:00', or '+05:30'. The permitted range is '-13:59' to '+14:00', inclusive.
        - As a named time zone, as defined by the \"IANA Time Zone database\", such as 'Europe/Helsinki', 'US/Eastern', 'MET', or 'UTC'.


        :return: The time_zone of this ConfigurationVariables.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ConfigurationVariables.
        Initializes the time zone for each client that connects.

        This corresponds to the MySQL System Variable \"time_zone\".

        The values can be given in one of the following formats, none of which are case-sensitive:

        - As a string indicating an offset from UTC of the form [H]H:MM, prefixed with a + or -, such as '+10:00', '-6:00', or '+05:30'. The permitted range is '-13:59' to '+14:00', inclusive.
        - As a named time zone, as defined by the \"IANA Time Zone database\", such as 'Europe/Helsinki', 'US/Eastern', 'MET', or 'UTC'.


        :param time_zone: The time_zone of this ConfigurationVariables.
        :type: str
        """
        self._time_zone = time_zone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
