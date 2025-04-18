# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200129


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlEndpoint(object):
    """
    The description of a SQL Endpoint.
    """

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a SqlEndpoint.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SqlEndpoint.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this SqlEndpoint.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SqlEndpoint.
        :type compartment_id: str

        :param jdbc_endpoint_url:
            The value to assign to the jdbc_endpoint_url property of this SqlEndpoint.
        :type jdbc_endpoint_url: str

        :param time_created:
            The value to assign to the time_created property of this SqlEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this SqlEndpoint.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SqlEndpoint.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this SqlEndpoint.
        :type state_message: str

        :param sql_endpoint_version:
            The value to assign to the sql_endpoint_version property of this SqlEndpoint.
        :type sql_endpoint_version: str

        :param driver_shape:
            The value to assign to the driver_shape property of this SqlEndpoint.
        :type driver_shape: str

        :param driver_shape_config:
            The value to assign to the driver_shape_config property of this SqlEndpoint.
        :type driver_shape_config: oci.data_flow.models.ShapeConfig

        :param executor_shape:
            The value to assign to the executor_shape property of this SqlEndpoint.
        :type executor_shape: str

        :param executor_shape_config:
            The value to assign to the executor_shape_config property of this SqlEndpoint.
        :type executor_shape_config: oci.data_flow.models.ShapeConfig

        :param min_executor_count:
            The value to assign to the min_executor_count property of this SqlEndpoint.
        :type min_executor_count: int

        :param max_executor_count:
            The value to assign to the max_executor_count property of this SqlEndpoint.
        :type max_executor_count: int

        :param metastore_id:
            The value to assign to the metastore_id property of this SqlEndpoint.
        :type metastore_id: str

        :param lake_id:
            The value to assign to the lake_id property of this SqlEndpoint.
        :type lake_id: str

        :param warehouse_bucket_uri:
            The value to assign to the warehouse_bucket_uri property of this SqlEndpoint.
        :type warehouse_bucket_uri: str

        :param description:
            The value to assign to the description property of this SqlEndpoint.
        :type description: str

        :param last_accepted_request_token:
            The value to assign to the last_accepted_request_token property of this SqlEndpoint.
        :type last_accepted_request_token: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SqlEndpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SqlEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SqlEndpoint.
        :type system_tags: dict(str, dict(str, object))

        :param spark_advanced_configurations:
            The value to assign to the spark_advanced_configurations property of this SqlEndpoint.
        :type spark_advanced_configurations: dict(str, str)

        :param banner_message:
            The value to assign to the banner_message property of this SqlEndpoint.
        :type banner_message: str

        :param network_configuration:
            The value to assign to the network_configuration property of this SqlEndpoint.
        :type network_configuration: oci.data_flow.models.SqlEndpointNetworkConfiguration

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'jdbc_endpoint_url': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'state_message': 'str',
            'sql_endpoint_version': 'str',
            'driver_shape': 'str',
            'driver_shape_config': 'ShapeConfig',
            'executor_shape': 'str',
            'executor_shape_config': 'ShapeConfig',
            'min_executor_count': 'int',
            'max_executor_count': 'int',
            'metastore_id': 'str',
            'lake_id': 'str',
            'warehouse_bucket_uri': 'str',
            'description': 'str',
            'last_accepted_request_token': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'spark_advanced_configurations': 'dict(str, str)',
            'banner_message': 'str',
            'network_configuration': 'SqlEndpointNetworkConfiguration'
        }
        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'jdbc_endpoint_url': 'jdbcEndpointUrl',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'state_message': 'stateMessage',
            'sql_endpoint_version': 'sqlEndpointVersion',
            'driver_shape': 'driverShape',
            'driver_shape_config': 'driverShapeConfig',
            'executor_shape': 'executorShape',
            'executor_shape_config': 'executorShapeConfig',
            'min_executor_count': 'minExecutorCount',
            'max_executor_count': 'maxExecutorCount',
            'metastore_id': 'metastoreId',
            'lake_id': 'lakeId',
            'warehouse_bucket_uri': 'warehouseBucketUri',
            'description': 'description',
            'last_accepted_request_token': 'lastAcceptedRequestToken',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'spark_advanced_configurations': 'sparkAdvancedConfigurations',
            'banner_message': 'bannerMessage',
            'network_configuration': 'networkConfiguration'
        }
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._jdbc_endpoint_url = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._state_message = None
        self._sql_endpoint_version = None
        self._driver_shape = None
        self._driver_shape_config = None
        self._executor_shape = None
        self._executor_shape_config = None
        self._min_executor_count = None
        self._max_executor_count = None
        self._metastore_id = None
        self._lake_id = None
        self._warehouse_bucket_uri = None
        self._description = None
        self._last_accepted_request_token = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._spark_advanced_configurations = None
        self._banner_message = None
        self._network_configuration = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SqlEndpoint.
        The provision identifier that is immutable on creation.


        :return: The id of this SqlEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SqlEndpoint.
        The provision identifier that is immutable on creation.


        :param id: The id of this SqlEndpoint.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SqlEndpoint.
        The SQL Endpoint name, which can be changed.


        :return: The display_name of this SqlEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SqlEndpoint.
        The SQL Endpoint name, which can be changed.


        :param display_name: The display_name of this SqlEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SqlEndpoint.
        The OCID of a compartment.


        :return: The compartment_id of this SqlEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SqlEndpoint.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this SqlEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def jdbc_endpoint_url(self):
        """
        Gets the jdbc_endpoint_url of this SqlEndpoint.
        The JDBC URL field. For example, jdbc:spark://{serviceFQDN}:443/default;SparkServerType=DFI


        :return: The jdbc_endpoint_url of this SqlEndpoint.
        :rtype: str
        """
        return self._jdbc_endpoint_url

    @jdbc_endpoint_url.setter
    def jdbc_endpoint_url(self, jdbc_endpoint_url):
        """
        Sets the jdbc_endpoint_url of this SqlEndpoint.
        The JDBC URL field. For example, jdbc:spark://{serviceFQDN}:443/default;SparkServerType=DFI


        :param jdbc_endpoint_url: The jdbc_endpoint_url of this SqlEndpoint.
        :type: str
        """
        self._jdbc_endpoint_url = jdbc_endpoint_url

    @property
    def time_created(self):
        """
        Gets the time_created of this SqlEndpoint.
        The time the Sql Endpoint was created. An RFC3339 formatted datetime string.


        :return: The time_created of this SqlEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlEndpoint.
        The time the Sql Endpoint was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this SqlEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this SqlEndpoint.
        The time the Sql Endpoint was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this SqlEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this SqlEndpoint.
        The time the Sql Endpoint was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this SqlEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SqlEndpoint.
        The current state of the Sql Endpoint.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SqlEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SqlEndpoint.
        The current state of the Sql Endpoint.


        :param lifecycle_state: The lifecycle_state of this SqlEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "UPDATING", "NEEDS_ATTENTION", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this SqlEndpoint.
        A message describing the reason why the resource is in it's current state. Helps bubble up errors in state changes. For example, it can be used to provide actionable information for a resource in the Failed state.


        :return: The state_message of this SqlEndpoint.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this SqlEndpoint.
        A message describing the reason why the resource is in it's current state. Helps bubble up errors in state changes. For example, it can be used to provide actionable information for a resource in the Failed state.


        :param state_message: The state_message of this SqlEndpoint.
        :type: str
        """
        self._state_message = state_message

    @property
    def sql_endpoint_version(self):
        """
        **[Required]** Gets the sql_endpoint_version of this SqlEndpoint.
        The version of SQL Endpoint.


        :return: The sql_endpoint_version of this SqlEndpoint.
        :rtype: str
        """
        return self._sql_endpoint_version

    @sql_endpoint_version.setter
    def sql_endpoint_version(self, sql_endpoint_version):
        """
        Sets the sql_endpoint_version of this SqlEndpoint.
        The version of SQL Endpoint.


        :param sql_endpoint_version: The sql_endpoint_version of this SqlEndpoint.
        :type: str
        """
        self._sql_endpoint_version = sql_endpoint_version

    @property
    def driver_shape(self):
        """
        **[Required]** Gets the driver_shape of this SqlEndpoint.
        The shape of the SQL Endpoint driver instance.


        :return: The driver_shape of this SqlEndpoint.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this SqlEndpoint.
        The shape of the SQL Endpoint driver instance.


        :param driver_shape: The driver_shape of this SqlEndpoint.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def driver_shape_config(self):
        """
        Gets the driver_shape_config of this SqlEndpoint.

        :return: The driver_shape_config of this SqlEndpoint.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._driver_shape_config

    @driver_shape_config.setter
    def driver_shape_config(self, driver_shape_config):
        """
        Sets the driver_shape_config of this SqlEndpoint.

        :param driver_shape_config: The driver_shape_config of this SqlEndpoint.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._driver_shape_config = driver_shape_config

    @property
    def executor_shape(self):
        """
        **[Required]** Gets the executor_shape of this SqlEndpoint.
        The shape of the SQL Endpoint executor instance.


        :return: The executor_shape of this SqlEndpoint.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this SqlEndpoint.
        The shape of the SQL Endpoint executor instance.


        :param executor_shape: The executor_shape of this SqlEndpoint.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def executor_shape_config(self):
        """
        Gets the executor_shape_config of this SqlEndpoint.

        :return: The executor_shape_config of this SqlEndpoint.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._executor_shape_config

    @executor_shape_config.setter
    def executor_shape_config(self, executor_shape_config):
        """
        Sets the executor_shape_config of this SqlEndpoint.

        :param executor_shape_config: The executor_shape_config of this SqlEndpoint.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._executor_shape_config = executor_shape_config

    @property
    def min_executor_count(self):
        """
        **[Required]** Gets the min_executor_count of this SqlEndpoint.
        The minimum number of executors.


        :return: The min_executor_count of this SqlEndpoint.
        :rtype: int
        """
        return self._min_executor_count

    @min_executor_count.setter
    def min_executor_count(self, min_executor_count):
        """
        Sets the min_executor_count of this SqlEndpoint.
        The minimum number of executors.


        :param min_executor_count: The min_executor_count of this SqlEndpoint.
        :type: int
        """
        self._min_executor_count = min_executor_count

    @property
    def max_executor_count(self):
        """
        **[Required]** Gets the max_executor_count of this SqlEndpoint.
        The maximum number of executors.


        :return: The max_executor_count of this SqlEndpoint.
        :rtype: int
        """
        return self._max_executor_count

    @max_executor_count.setter
    def max_executor_count(self, max_executor_count):
        """
        Sets the max_executor_count of this SqlEndpoint.
        The maximum number of executors.


        :param max_executor_count: The max_executor_count of this SqlEndpoint.
        :type: int
        """
        self._max_executor_count = max_executor_count

    @property
    def metastore_id(self):
        """
        **[Required]** Gets the metastore_id of this SqlEndpoint.
        The OCID of OCI Hive Metastore.


        :return: The metastore_id of this SqlEndpoint.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        """
        Sets the metastore_id of this SqlEndpoint.
        The OCID of OCI Hive Metastore.


        :param metastore_id: The metastore_id of this SqlEndpoint.
        :type: str
        """
        self._metastore_id = metastore_id

    @property
    def lake_id(self):
        """
        **[Required]** Gets the lake_id of this SqlEndpoint.
        The OCID of OCI Lake.


        :return: The lake_id of this SqlEndpoint.
        :rtype: str
        """
        return self._lake_id

    @lake_id.setter
    def lake_id(self, lake_id):
        """
        Sets the lake_id of this SqlEndpoint.
        The OCID of OCI Lake.


        :param lake_id: The lake_id of this SqlEndpoint.
        :type: str
        """
        self._lake_id = lake_id

    @property
    def warehouse_bucket_uri(self):
        """
        **[Required]** Gets the warehouse_bucket_uri of this SqlEndpoint.
        The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html


        :return: The warehouse_bucket_uri of this SqlEndpoint.
        :rtype: str
        """
        return self._warehouse_bucket_uri

    @warehouse_bucket_uri.setter
    def warehouse_bucket_uri(self, warehouse_bucket_uri):
        """
        Sets the warehouse_bucket_uri of this SqlEndpoint.
        The warehouse bucket URI. It is a Oracle Cloud Infrastructure Object Storage bucket URI as defined here https://docs.oracle.com/en/cloud/paas/atp-cloud/atpud/object-storage-uris.html


        :param warehouse_bucket_uri: The warehouse_bucket_uri of this SqlEndpoint.
        :type: str
        """
        self._warehouse_bucket_uri = warehouse_bucket_uri

    @property
    def description(self):
        """
        **[Required]** Gets the description of this SqlEndpoint.
        The description of the SQL Endpoint.


        :return: The description of this SqlEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlEndpoint.
        The description of the SQL Endpoint.


        :param description: The description of this SqlEndpoint.
        :type: str
        """
        self._description = description

    @property
    def last_accepted_request_token(self):
        """
        Gets the last_accepted_request_token of this SqlEndpoint.
        This token is used by Splat, and indicates that the service accepts the request, and that the request is currently being processed.


        :return: The last_accepted_request_token of this SqlEndpoint.
        :rtype: str
        """
        return self._last_accepted_request_token

    @last_accepted_request_token.setter
    def last_accepted_request_token(self, last_accepted_request_token):
        """
        Sets the last_accepted_request_token of this SqlEndpoint.
        This token is used by Splat, and indicates that the service accepts the request, and that the request is currently being processed.


        :param last_accepted_request_token: The last_accepted_request_token of this SqlEndpoint.
        :type: str
        """
        self._last_accepted_request_token = last_accepted_request_token

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SqlEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SqlEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SqlEndpoint.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SqlEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SqlEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SqlEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SqlEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SqlEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SqlEndpoint.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this SqlEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SqlEndpoint.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this SqlEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def spark_advanced_configurations(self):
        """
        Gets the spark_advanced_configurations of this SqlEndpoint.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :return: The spark_advanced_configurations of this SqlEndpoint.
        :rtype: dict(str, str)
        """
        return self._spark_advanced_configurations

    @spark_advanced_configurations.setter
    def spark_advanced_configurations(self, spark_advanced_configurations):
        """
        Sets the spark_advanced_configurations of this SqlEndpoint.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :param spark_advanced_configurations: The spark_advanced_configurations of this SqlEndpoint.
        :type: dict(str, str)
        """
        self._spark_advanced_configurations = spark_advanced_configurations

    @property
    def banner_message(self):
        """
        Gets the banner_message of this SqlEndpoint.
        The SQL Endpoint message displayed as a banner to provide user with any action items required on the resource.


        :return: The banner_message of this SqlEndpoint.
        :rtype: str
        """
        return self._banner_message

    @banner_message.setter
    def banner_message(self, banner_message):
        """
        Sets the banner_message of this SqlEndpoint.
        The SQL Endpoint message displayed as a banner to provide user with any action items required on the resource.


        :param banner_message: The banner_message of this SqlEndpoint.
        :type: str
        """
        self._banner_message = banner_message

    @property
    def network_configuration(self):
        """
        Gets the network_configuration of this SqlEndpoint.

        :return: The network_configuration of this SqlEndpoint.
        :rtype: oci.data_flow.models.SqlEndpointNetworkConfiguration
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        """
        Sets the network_configuration of this SqlEndpoint.

        :param network_configuration: The network_configuration of this SqlEndpoint.
        :type: oci.data_flow.models.SqlEndpointNetworkConfiguration
        """
        self._network_configuration = network_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
