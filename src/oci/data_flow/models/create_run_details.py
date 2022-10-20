# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRunDetails(object):
    """
    The create run details. The following properties are optional and override the default values
    set in the associated application:
    - applicationId
    - archiveUri
    - applicationLogConfig
    - arguments
    - configuration
    - definedTags
    - displayName
    - driverShape
    - execute
    - executorShape
    - freeformTags
    - logsBucketUri
    - metastoreId
    - numExecutors
    - parameters
    - sparkVersion
    - warehouseBucketUri
    It is expected that either the applicationId or the execute parameter is specified; but not both.
    If both or none are set, a Bad Request (HTTP 400) status will be sent as the response.
    If an appicationId is not specified, then a value for the execute parameter is expected.
    Using data parsed from the value, a new application will be created and assicated with the new run.
    See information on the execute parameter for details on the format of this parameter.

    The optional parameter spark version can only be specified when using the execute parameter.  If it
    is not specified when using the execute parameter, the latest version will be used as default.
    If the execute parameter is not used, the spark version will be taken from the associated application.

    If displayName is not specified, it will be derived from the displayName of associated application or
    set by API using fileUri's application file name.
    Once a run is created, its properties (except for definedTags and freeformTags) cannot be changed.
    If the parent application's properties (including definedTags and freeformTags) are updated,
    the corresponding properties of the run will not update.
    """

    #: A constant which can be used with the type property of a CreateRunDetails.
    #: This constant has a value of "BATCH"
    TYPE_BATCH = "BATCH"

    #: A constant which can be used with the type property of a CreateRunDetails.
    #: This constant has a value of "STREAMING"
    TYPE_STREAMING = "STREAMING"

    #: A constant which can be used with the type property of a CreateRunDetails.
    #: This constant has a value of "SESSION"
    TYPE_SESSION = "SESSION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param application_log_config:
            The value to assign to the application_log_config property of this CreateRunDetails.
        :type application_log_config: oci.data_flow.models.ApplicationLogConfig

        :param application_id:
            The value to assign to the application_id property of this CreateRunDetails.
        :type application_id: str

        :param archive_uri:
            The value to assign to the archive_uri property of this CreateRunDetails.
        :type archive_uri: str

        :param arguments:
            The value to assign to the arguments property of this CreateRunDetails.
        :type arguments: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRunDetails.
        :type compartment_id: str

        :param configuration:
            The value to assign to the configuration property of this CreateRunDetails.
        :type configuration: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateRunDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateRunDetails.
        :type display_name: str

        :param driver_shape:
            The value to assign to the driver_shape property of this CreateRunDetails.
        :type driver_shape: str

        :param driver_shape_config:
            The value to assign to the driver_shape_config property of this CreateRunDetails.
        :type driver_shape_config: oci.data_flow.models.ShapeConfig

        :param execute:
            The value to assign to the execute property of this CreateRunDetails.
        :type execute: str

        :param executor_shape:
            The value to assign to the executor_shape property of this CreateRunDetails.
        :type executor_shape: str

        :param executor_shape_config:
            The value to assign to the executor_shape_config property of this CreateRunDetails.
        :type executor_shape_config: oci.data_flow.models.ShapeConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateRunDetails.
        :type freeform_tags: dict(str, str)

        :param logs_bucket_uri:
            The value to assign to the logs_bucket_uri property of this CreateRunDetails.
        :type logs_bucket_uri: str

        :param metastore_id:
            The value to assign to the metastore_id property of this CreateRunDetails.
        :type metastore_id: str

        :param num_executors:
            The value to assign to the num_executors property of this CreateRunDetails.
        :type num_executors: int

        :param parameters:
            The value to assign to the parameters property of this CreateRunDetails.
        :type parameters: list[oci.data_flow.models.ApplicationParameter]

        :param spark_version:
            The value to assign to the spark_version property of this CreateRunDetails.
        :type spark_version: str

        :param type:
            The value to assign to the type property of this CreateRunDetails.
            Allowed values for this property are: "BATCH", "STREAMING", "SESSION"
        :type type: str

        :param warehouse_bucket_uri:
            The value to assign to the warehouse_bucket_uri property of this CreateRunDetails.
        :type warehouse_bucket_uri: str

        :param max_duration_in_minutes:
            The value to assign to the max_duration_in_minutes property of this CreateRunDetails.
        :type max_duration_in_minutes: int

        :param idle_timeout_in_minutes:
            The value to assign to the idle_timeout_in_minutes property of this CreateRunDetails.
        :type idle_timeout_in_minutes: int

        """
        self.swagger_types = {
            'application_log_config': 'ApplicationLogConfig',
            'application_id': 'str',
            'archive_uri': 'str',
            'arguments': 'list[str]',
            'compartment_id': 'str',
            'configuration': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'driver_shape': 'str',
            'driver_shape_config': 'ShapeConfig',
            'execute': 'str',
            'executor_shape': 'str',
            'executor_shape_config': 'ShapeConfig',
            'freeform_tags': 'dict(str, str)',
            'logs_bucket_uri': 'str',
            'metastore_id': 'str',
            'num_executors': 'int',
            'parameters': 'list[ApplicationParameter]',
            'spark_version': 'str',
            'type': 'str',
            'warehouse_bucket_uri': 'str',
            'max_duration_in_minutes': 'int',
            'idle_timeout_in_minutes': 'int'
        }

        self.attribute_map = {
            'application_log_config': 'applicationLogConfig',
            'application_id': 'applicationId',
            'archive_uri': 'archiveUri',
            'arguments': 'arguments',
            'compartment_id': 'compartmentId',
            'configuration': 'configuration',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'driver_shape': 'driverShape',
            'driver_shape_config': 'driverShapeConfig',
            'execute': 'execute',
            'executor_shape': 'executorShape',
            'executor_shape_config': 'executorShapeConfig',
            'freeform_tags': 'freeformTags',
            'logs_bucket_uri': 'logsBucketUri',
            'metastore_id': 'metastoreId',
            'num_executors': 'numExecutors',
            'parameters': 'parameters',
            'spark_version': 'sparkVersion',
            'type': 'type',
            'warehouse_bucket_uri': 'warehouseBucketUri',
            'max_duration_in_minutes': 'maxDurationInMinutes',
            'idle_timeout_in_minutes': 'idleTimeoutInMinutes'
        }

        self._application_log_config = None
        self._application_id = None
        self._archive_uri = None
        self._arguments = None
        self._compartment_id = None
        self._configuration = None
        self._defined_tags = None
        self._display_name = None
        self._driver_shape = None
        self._driver_shape_config = None
        self._execute = None
        self._executor_shape = None
        self._executor_shape_config = None
        self._freeform_tags = None
        self._logs_bucket_uri = None
        self._metastore_id = None
        self._num_executors = None
        self._parameters = None
        self._spark_version = None
        self._type = None
        self._warehouse_bucket_uri = None
        self._max_duration_in_minutes = None
        self._idle_timeout_in_minutes = None

    @property
    def application_log_config(self):
        """
        Gets the application_log_config of this CreateRunDetails.

        :return: The application_log_config of this CreateRunDetails.
        :rtype: oci.data_flow.models.ApplicationLogConfig
        """
        return self._application_log_config

    @application_log_config.setter
    def application_log_config(self, application_log_config):
        """
        Sets the application_log_config of this CreateRunDetails.

        :param application_log_config: The application_log_config of this CreateRunDetails.
        :type: oci.data_flow.models.ApplicationLogConfig
        """
        self._application_log_config = application_log_config

    @property
    def application_id(self):
        """
        Gets the application_id of this CreateRunDetails.
        The OCID of the associated application. If this value is set, then no value for the execute parameter is required. If this value is not set, then a value for the execute parameter is required, and a new application is created and associated with the new run.


        :return: The application_id of this CreateRunDetails.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this CreateRunDetails.
        The OCID of the associated application. If this value is set, then no value for the execute parameter is required. If this value is not set, then a value for the execute parameter is required, and a new application is created and associated with the new run.


        :param application_id: The application_id of this CreateRunDetails.
        :type: str
        """
        self._application_id = application_id

    @property
    def archive_uri(self):
        """
        Gets the archive_uri of this CreateRunDetails.
        A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python, Java, or Scala application.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :return: The archive_uri of this CreateRunDetails.
        :rtype: str
        """
        return self._archive_uri

    @archive_uri.setter
    def archive_uri(self, archive_uri):
        """
        Sets the archive_uri of this CreateRunDetails.
        A comma separated list of one or more archive files as Oracle Cloud Infrastructure URIs. For example, ``oci://path/to/a.zip,oci://path/to/b.zip``. An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution of a Python, Java, or Scala application.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :param archive_uri: The archive_uri of this CreateRunDetails.
        :type: str
        """
        self._archive_uri = archive_uri

    @property
    def arguments(self):
        """
        Gets the arguments of this CreateRunDetails.
        The arguments passed to the running application as command line arguments.  An argument is
        either a plain text or a placeholder. Placeholders are replaced using values from the parameters
        map.  Each placeholder specified must be represented in the parameters map else the request
        (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
        `Service Api Spec`, where `name` is the name of the parameter.
        Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]`
        If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to
        `--input mydata.xml --name \"John Doe\"`


        :return: The arguments of this CreateRunDetails.
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this CreateRunDetails.
        The arguments passed to the running application as command line arguments.  An argument is
        either a plain text or a placeholder. Placeholders are replaced using values from the parameters
        map.  Each placeholder specified must be represented in the parameters map else the request
        (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
        `Service Api Spec`, where `name` is the name of the parameter.
        Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]`
        If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to
        `--input mydata.xml --name \"John Doe\"`


        :param arguments: The arguments of this CreateRunDetails.
        :type: list[str]
        """
        self._arguments = arguments

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateRunDetails.
        The OCID of a compartment.


        :return: The compartment_id of this CreateRunDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRunDetails.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this CreateRunDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def configuration(self):
        """
        Gets the configuration of this CreateRunDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :return: The configuration of this CreateRunDetails.
        :rtype: dict(str, str)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this CreateRunDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :param configuration: The configuration of this CreateRunDetails.
        :type: dict(str, str)
        """
        self._configuration = configuration

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateRunDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateRunDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateRunDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRunDetails.
        A user-friendly name that does not have to be unique. Avoid entering confidential information. If this value is not specified, it will be derived from the associated application's displayName or set by API using fileUri's application file name.


        :return: The display_name of this CreateRunDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRunDetails.
        A user-friendly name that does not have to be unique. Avoid entering confidential information. If this value is not specified, it will be derived from the associated application's displayName or set by API using fileUri's application file name.


        :param display_name: The display_name of this CreateRunDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def driver_shape(self):
        """
        Gets the driver_shape of this CreateRunDetails.
        The VM shape for the driver. Sets the driver cores and memory.


        :return: The driver_shape of this CreateRunDetails.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this CreateRunDetails.
        The VM shape for the driver. Sets the driver cores and memory.


        :param driver_shape: The driver_shape of this CreateRunDetails.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def driver_shape_config(self):
        """
        Gets the driver_shape_config of this CreateRunDetails.

        :return: The driver_shape_config of this CreateRunDetails.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._driver_shape_config

    @driver_shape_config.setter
    def driver_shape_config(self, driver_shape_config):
        """
        Sets the driver_shape_config of this CreateRunDetails.

        :param driver_shape_config: The driver_shape_config of this CreateRunDetails.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._driver_shape_config = driver_shape_config

    @property
    def execute(self):
        """
        Gets the execute of this CreateRunDetails.
        The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit.
        Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments.
        Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10``
        Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit,
        Data Flow service will use derived information from execute input only.


        :return: The execute of this CreateRunDetails.
        :rtype: str
        """
        return self._execute

    @execute.setter
    def execute(self, execute):
        """
        Sets the execute of this CreateRunDetails.
        The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-applications-with-spark-submit.
        Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments.
        Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar 10``
        Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application create/update, or run create/submit,
        Data Flow service will use derived information from execute input only.


        :param execute: The execute of this CreateRunDetails.
        :type: str
        """
        self._execute = execute

    @property
    def executor_shape(self):
        """
        Gets the executor_shape of this CreateRunDetails.
        The VM shape for the executors. Sets the executor cores and memory.


        :return: The executor_shape of this CreateRunDetails.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this CreateRunDetails.
        The VM shape for the executors. Sets the executor cores and memory.


        :param executor_shape: The executor_shape of this CreateRunDetails.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def executor_shape_config(self):
        """
        Gets the executor_shape_config of this CreateRunDetails.

        :return: The executor_shape_config of this CreateRunDetails.
        :rtype: oci.data_flow.models.ShapeConfig
        """
        return self._executor_shape_config

    @executor_shape_config.setter
    def executor_shape_config(self, executor_shape_config):
        """
        Sets the executor_shape_config of this CreateRunDetails.

        :param executor_shape_config: The executor_shape_config of this CreateRunDetails.
        :type: oci.data_flow.models.ShapeConfig
        """
        self._executor_shape_config = executor_shape_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateRunDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateRunDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateRunDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def logs_bucket_uri(self):
        """
        Gets the logs_bucket_uri of this CreateRunDetails.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :return: The logs_bucket_uri of this CreateRunDetails.
        :rtype: str
        """
        return self._logs_bucket_uri

    @logs_bucket_uri.setter
    def logs_bucket_uri(self, logs_bucket_uri):
        """
        Sets the logs_bucket_uri of this CreateRunDetails.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :param logs_bucket_uri: The logs_bucket_uri of this CreateRunDetails.
        :type: str
        """
        self._logs_bucket_uri = logs_bucket_uri

    @property
    def metastore_id(self):
        """
        Gets the metastore_id of this CreateRunDetails.
        The OCID of OCI Hive Metastore.


        :return: The metastore_id of this CreateRunDetails.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        """
        Sets the metastore_id of this CreateRunDetails.
        The OCID of OCI Hive Metastore.


        :param metastore_id: The metastore_id of this CreateRunDetails.
        :type: str
        """
        self._metastore_id = metastore_id

    @property
    def num_executors(self):
        """
        Gets the num_executors of this CreateRunDetails.
        The number of executor VMs requested.


        :return: The num_executors of this CreateRunDetails.
        :rtype: int
        """
        return self._num_executors

    @num_executors.setter
    def num_executors(self, num_executors):
        """
        Sets the num_executors of this CreateRunDetails.
        The number of executor VMs requested.


        :param num_executors: The num_executors of this CreateRunDetails.
        :type: int
        """
        self._num_executors = num_executors

    @property
    def parameters(self):
        """
        Gets the parameters of this CreateRunDetails.
        An array of name/value pairs used to fill placeholders found in properties like
        `Application.arguments`.  The name must be a string of one or more word characters
        (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
        Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]


        :return: The parameters of this CreateRunDetails.
        :rtype: list[oci.data_flow.models.ApplicationParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateRunDetails.
        An array of name/value pairs used to fill placeholders found in properties like
        `Application.arguments`.  The name must be a string of one or more word characters
        (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
        Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]


        :param parameters: The parameters of this CreateRunDetails.
        :type: list[oci.data_flow.models.ApplicationParameter]
        """
        self._parameters = parameters

    @property
    def spark_version(self):
        """
        Gets the spark_version of this CreateRunDetails.
        The Spark version utilized to run the application. This value may be set if applicationId is not since the Spark version will be taken from the associated application.


        :return: The spark_version of this CreateRunDetails.
        :rtype: str
        """
        return self._spark_version

    @spark_version.setter
    def spark_version(self, spark_version):
        """
        Sets the spark_version of this CreateRunDetails.
        The Spark version utilized to run the application. This value may be set if applicationId is not since the Spark version will be taken from the associated application.


        :param spark_version: The spark_version of this CreateRunDetails.
        :type: str
        """
        self._spark_version = spark_version

    @property
    def type(self):
        """
        Gets the type of this CreateRunDetails.
        The Spark application processing type.

        Allowed values for this property are: "BATCH", "STREAMING", "SESSION"


        :return: The type of this CreateRunDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateRunDetails.
        The Spark application processing type.


        :param type: The type of this CreateRunDetails.
        :type: str
        """
        allowed_values = ["BATCH", "STREAMING", "SESSION"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def warehouse_bucket_uri(self):
        """
        Gets the warehouse_bucket_uri of this CreateRunDetails.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
        for BATCH SQL runs.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :return: The warehouse_bucket_uri of this CreateRunDetails.
        :rtype: str
        """
        return self._warehouse_bucket_uri

    @warehouse_bucket_uri.setter
    def warehouse_bucket_uri(self, warehouse_bucket_uri):
        """
        Sets the warehouse_bucket_uri of this CreateRunDetails.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
        for BATCH SQL runs.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :param warehouse_bucket_uri: The warehouse_bucket_uri of this CreateRunDetails.
        :type: str
        """
        self._warehouse_bucket_uri = warehouse_bucket_uri

    @property
    def max_duration_in_minutes(self):
        """
        Gets the max_duration_in_minutes of this CreateRunDetails.
        The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated
        once it reaches this duration from the time it transitions to `IN_PROGRESS` state.


        :return: The max_duration_in_minutes of this CreateRunDetails.
        :rtype: int
        """
        return self._max_duration_in_minutes

    @max_duration_in_minutes.setter
    def max_duration_in_minutes(self, max_duration_in_minutes):
        """
        Sets the max_duration_in_minutes of this CreateRunDetails.
        The maximum duration in minutes for which an Application should run. Data Flow Run would be terminated
        once it reaches this duration from the time it transitions to `IN_PROGRESS` state.


        :param max_duration_in_minutes: The max_duration_in_minutes of this CreateRunDetails.
        :type: int
        """
        self._max_duration_in_minutes = max_duration_in_minutes

    @property
    def idle_timeout_in_minutes(self):
        """
        Gets the idle_timeout_in_minutes of this CreateRunDetails.
        The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period.
        Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)


        :return: The idle_timeout_in_minutes of this CreateRunDetails.
        :rtype: int
        """
        return self._idle_timeout_in_minutes

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, idle_timeout_in_minutes):
        """
        Sets the idle_timeout_in_minutes of this CreateRunDetails.
        The timeout value in minutes used to manage Runs. A Run would be stopped after inactivity for this amount of time period.
        Note: This parameter is currently only applicable for Runs of type `SESSION`. Default value is 2880 minutes (2 days)


        :param idle_timeout_in_minutes: The idle_timeout_in_minutes of this CreateRunDetails.
        :type: int
        """
        self._idle_timeout_in_minutes = idle_timeout_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
