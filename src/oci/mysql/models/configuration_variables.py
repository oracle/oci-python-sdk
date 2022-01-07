# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationVariables(object):
    """
    User controllable service variables.
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

        :param default_authentication_plugin:
            The value to assign to the default_authentication_plugin property of this ConfigurationVariables.
            Allowed values for this property are: "mysql_native_password", "sha256_password", "caching_sha2_password", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type default_authentication_plugin: str

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

        :param innodb_buffer_pool_instances:
            The value to assign to the innodb_buffer_pool_instances property of this ConfigurationVariables.
        :type innodb_buffer_pool_instances: int

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

        :param parser_max_mem_size:
            The value to assign to the parser_max_mem_size property of this ConfigurationVariables.
        :type parser_max_mem_size: int

        :param query_alloc_block_size:
            The value to assign to the query_alloc_block_size property of this ConfigurationVariables.
        :type query_alloc_block_size: int

        :param query_prealloc_size:
            The value to assign to the query_prealloc_size property of this ConfigurationVariables.
        :type query_prealloc_size: int

        :param sql_mode:
            The value to assign to the sql_mode property of this ConfigurationVariables.
        :type sql_mode: str

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

        """
        self.swagger_types = {
            'completion_type': 'str',
            'default_authentication_plugin': 'str',
            'transaction_isolation': 'str',
            'innodb_ft_server_stopword_table': 'str',
            'mandatory_roles': 'str',
            'autocommit': 'bool',
            'foreign_key_checks': 'bool',
            'group_replication_consistency': 'str',
            'innodb_ft_enable_stopword': 'bool',
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
            'max_connections': 'int',
            'max_prepared_stmt_count': 'int',
            'connect_timeout': 'int',
            'cte_max_recursion_depth': 'int',
            'generated_random_password_length': 'int',
            'information_schema_stats_expiry': 'int',
            'innodb_buffer_pool_instances': 'int',
            'innodb_ft_max_token_size': 'int',
            'innodb_ft_min_token_size': 'int',
            'innodb_ft_num_word_optimize': 'int',
            'innodb_lock_wait_timeout': 'int',
            'innodb_max_purge_lag': 'int',
            'innodb_max_purge_lag_delay': 'int',
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
            'parser_max_mem_size': 'int',
            'query_alloc_block_size': 'int',
            'query_prealloc_size': 'int',
            'sql_mode': 'str',
            'mysqlx_deflate_default_compression_level': 'int',
            'mysqlx_deflate_max_client_compression_level': 'int',
            'mysqlx_lz4_max_client_compression_level': 'int',
            'mysqlx_lz4_default_compression_level': 'int',
            'mysqlx_zstd_max_client_compression_level': 'int',
            'mysqlx_zstd_default_compression_level': 'int',
            'mysql_zstd_default_compression_level': 'int'
        }

        self.attribute_map = {
            'completion_type': 'completionType',
            'default_authentication_plugin': 'defaultAuthenticationPlugin',
            'transaction_isolation': 'transactionIsolation',
            'innodb_ft_server_stopword_table': 'innodbFtServerStopwordTable',
            'mandatory_roles': 'mandatoryRoles',
            'autocommit': 'autocommit',
            'foreign_key_checks': 'foreignKeyChecks',
            'group_replication_consistency': 'groupReplicationConsistency',
            'innodb_ft_enable_stopword': 'innodbFtEnableStopword',
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
            'max_connections': 'maxConnections',
            'max_prepared_stmt_count': 'maxPreparedStmtCount',
            'connect_timeout': 'connectTimeout',
            'cte_max_recursion_depth': 'cteMaxRecursionDepth',
            'generated_random_password_length': 'generatedRandomPasswordLength',
            'information_schema_stats_expiry': 'informationSchemaStatsExpiry',
            'innodb_buffer_pool_instances': 'innodbBufferPoolInstances',
            'innodb_ft_max_token_size': 'innodbFtMaxTokenSize',
            'innodb_ft_min_token_size': 'innodbFtMinTokenSize',
            'innodb_ft_num_word_optimize': 'innodbFtNumWordOptimize',
            'innodb_lock_wait_timeout': 'innodbLockWaitTimeout',
            'innodb_max_purge_lag': 'innodbMaxPurgeLag',
            'innodb_max_purge_lag_delay': 'innodbMaxPurgeLagDelay',
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
            'parser_max_mem_size': 'parserMaxMemSize',
            'query_alloc_block_size': 'queryAllocBlockSize',
            'query_prealloc_size': 'queryPreallocSize',
            'sql_mode': 'sqlMode',
            'mysqlx_deflate_default_compression_level': 'mysqlxDeflateDefaultCompressionLevel',
            'mysqlx_deflate_max_client_compression_level': 'mysqlxDeflateMaxClientCompressionLevel',
            'mysqlx_lz4_max_client_compression_level': 'mysqlxLz4MaxClientCompressionLevel',
            'mysqlx_lz4_default_compression_level': 'mysqlxLz4DefaultCompressionLevel',
            'mysqlx_zstd_max_client_compression_level': 'mysqlxZstdMaxClientCompressionLevel',
            'mysqlx_zstd_default_compression_level': 'mysqlxZstdDefaultCompressionLevel',
            'mysql_zstd_default_compression_level': 'mysqlZstdDefaultCompressionLevel'
        }

        self._completion_type = None
        self._default_authentication_plugin = None
        self._transaction_isolation = None
        self._innodb_ft_server_stopword_table = None
        self._mandatory_roles = None
        self._autocommit = None
        self._foreign_key_checks = None
        self._group_replication_consistency = None
        self._innodb_ft_enable_stopword = None
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
        self._max_connections = None
        self._max_prepared_stmt_count = None
        self._connect_timeout = None
        self._cte_max_recursion_depth = None
        self._generated_random_password_length = None
        self._information_schema_stats_expiry = None
        self._innodb_buffer_pool_instances = None
        self._innodb_ft_max_token_size = None
        self._innodb_ft_min_token_size = None
        self._innodb_ft_num_word_optimize = None
        self._innodb_lock_wait_timeout = None
        self._innodb_max_purge_lag = None
        self._innodb_max_purge_lag_delay = None
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
        self._parser_max_mem_size = None
        self._query_alloc_block_size = None
        self._query_prealloc_size = None
        self._sql_mode = None
        self._mysqlx_deflate_default_compression_level = None
        self._mysqlx_deflate_max_client_compression_level = None
        self._mysqlx_lz4_max_client_compression_level = None
        self._mysqlx_lz4_default_compression_level = None
        self._mysqlx_zstd_max_client_compression_level = None
        self._mysqlx_zstd_default_compression_level = None
        self._mysql_zstd_default_compression_level = None

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
        (\"innodb_buffer_pool_size\")


        :return: The innodb_buffer_pool_size of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_buffer_pool_size

    @innodb_buffer_pool_size.setter
    def innodb_buffer_pool_size(self, innodb_buffer_pool_size):
        """
        Sets the innodb_buffer_pool_size of this ConfigurationVariables.
        (\"innodb_buffer_pool_size\")


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
        (\"connect_timeout\")


        :return: The connect_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """
        Sets the connect_timeout of this ConfigurationVariables.
        (\"connect_timeout\")


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
        (\"innodb_max_purge_lag\")


        :return: The innodb_max_purge_lag of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_max_purge_lag

    @innodb_max_purge_lag.setter
    def innodb_max_purge_lag(self, innodb_max_purge_lag):
        """
        Sets the innodb_max_purge_lag of this ConfigurationVariables.
        (\"innodb_max_purge_lag\")


        :param innodb_max_purge_lag: The innodb_max_purge_lag of this ConfigurationVariables.
        :type: int
        """
        self._innodb_max_purge_lag = innodb_max_purge_lag

    @property
    def innodb_max_purge_lag_delay(self):
        """
        Gets the innodb_max_purge_lag_delay of this ConfigurationVariables.
        (\"innodb_max_purge_lag_delay\")


        :return: The innodb_max_purge_lag_delay of this ConfigurationVariables.
        :rtype: int
        """
        return self._innodb_max_purge_lag_delay

    @innodb_max_purge_lag_delay.setter
    def innodb_max_purge_lag_delay(self, innodb_max_purge_lag_delay):
        """
        Sets the innodb_max_purge_lag_delay of this ConfigurationVariables.
        (\"innodb_max_purge_lag_delay\")


        :param innodb_max_purge_lag_delay: The innodb_max_purge_lag_delay of this ConfigurationVariables.
        :type: int
        """
        self._innodb_max_purge_lag_delay = innodb_max_purge_lag_delay

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
        (\"mysqlx_connect_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_connect_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_connect_timeout

    @mysqlx_connect_timeout.setter
    def mysqlx_connect_timeout(self, mysqlx_connect_timeout):
        """
        Sets the mysqlx_connect_timeout of this ConfigurationVariables.
        (\"mysqlx_connect_timeout\") DEPRECATED -- variable should not be settable and will be ignored


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
        (\"mysqlx_interactive_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_interactive_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_interactive_timeout

    @mysqlx_interactive_timeout.setter
    def mysqlx_interactive_timeout(self, mysqlx_interactive_timeout):
        """
        Sets the mysqlx_interactive_timeout of this ConfigurationVariables.
        (\"mysqlx_interactive_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_interactive_timeout: The mysqlx_interactive_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_interactive_timeout = mysqlx_interactive_timeout

    @property
    def mysqlx_max_allowed_packet(self):
        """
        Gets the mysqlx_max_allowed_packet of this ConfigurationVariables.
        (\"mysqlx_max_allowed_packet\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_max_allowed_packet of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_max_allowed_packet

    @mysqlx_max_allowed_packet.setter
    def mysqlx_max_allowed_packet(self, mysqlx_max_allowed_packet):
        """
        Sets the mysqlx_max_allowed_packet of this ConfigurationVariables.
        (\"mysqlx_max_allowed_packet\") DEPRECATED -- variable should not be settable and will be ignored


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
        (\"mysqlx_read_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_read_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_read_timeout

    @mysqlx_read_timeout.setter
    def mysqlx_read_timeout(self, mysqlx_read_timeout):
        """
        Sets the mysqlx_read_timeout of this ConfigurationVariables.
        (\"mysqlx_read_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_read_timeout: The mysqlx_read_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_read_timeout = mysqlx_read_timeout

    @property
    def mysqlx_wait_timeout(self):
        """
        Gets the mysqlx_wait_timeout of this ConfigurationVariables.
        (\"mysqlx_wait_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_wait_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_wait_timeout

    @mysqlx_wait_timeout.setter
    def mysqlx_wait_timeout(self, mysqlx_wait_timeout):
        """
        Sets the mysqlx_wait_timeout of this ConfigurationVariables.
        (\"mysqlx_wait_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_wait_timeout: The mysqlx_wait_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_wait_timeout = mysqlx_wait_timeout

    @property
    def mysqlx_write_timeout(self):
        """
        Gets the mysqlx_write_timeout of this ConfigurationVariables.
        (\"mysqlx_write_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :return: The mysqlx_write_timeout of this ConfigurationVariables.
        :rtype: int
        """
        return self._mysqlx_write_timeout

    @mysqlx_write_timeout.setter
    def mysqlx_write_timeout(self, mysqlx_write_timeout):
        """
        Sets the mysqlx_write_timeout of this ConfigurationVariables.
        (\"mysqlx_write_timeout\") DEPRECATED -- variable should not be settable and will be ignored


        :param mysqlx_write_timeout: The mysqlx_write_timeout of this ConfigurationVariables.
        :type: int
        """
        self._mysqlx_write_timeout = mysqlx_write_timeout

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
