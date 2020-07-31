# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApplicationDetails(object):
    """
    The create application details.
    """

    #: A constant which can be used with the language property of a CreateApplicationDetails.
    #: This constant has a value of "SCALA"
    LANGUAGE_SCALA = "SCALA"

    #: A constant which can be used with the language property of a CreateApplicationDetails.
    #: This constant has a value of "JAVA"
    LANGUAGE_JAVA = "JAVA"

    #: A constant which can be used with the language property of a CreateApplicationDetails.
    #: This constant has a value of "PYTHON"
    LANGUAGE_PYTHON = "PYTHON"

    #: A constant which can be used with the language property of a CreateApplicationDetails.
    #: This constant has a value of "SQL"
    LANGUAGE_SQL = "SQL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param archive_uri:
            The value to assign to the archive_uri property of this CreateApplicationDetails.
        :type archive_uri: str

        :param arguments:
            The value to assign to the arguments property of this CreateApplicationDetails.
        :type arguments: list[str]

        :param class_name:
            The value to assign to the class_name property of this CreateApplicationDetails.
        :type class_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateApplicationDetails.
        :type compartment_id: str

        :param configuration:
            The value to assign to the configuration property of this CreateApplicationDetails.
        :type configuration: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateApplicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this CreateApplicationDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateApplicationDetails.
        :type display_name: str

        :param driver_shape:
            The value to assign to the driver_shape property of this CreateApplicationDetails.
        :type driver_shape: str

        :param executor_shape:
            The value to assign to the executor_shape property of this CreateApplicationDetails.
        :type executor_shape: str

        :param file_uri:
            The value to assign to the file_uri property of this CreateApplicationDetails.
        :type file_uri: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateApplicationDetails.
        :type freeform_tags: dict(str, str)

        :param language:
            The value to assign to the language property of this CreateApplicationDetails.
            Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL"
        :type language: str

        :param logs_bucket_uri:
            The value to assign to the logs_bucket_uri property of this CreateApplicationDetails.
        :type logs_bucket_uri: str

        :param num_executors:
            The value to assign to the num_executors property of this CreateApplicationDetails.
        :type num_executors: int

        :param parameters:
            The value to assign to the parameters property of this CreateApplicationDetails.
        :type parameters: list[ApplicationParameter]

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this CreateApplicationDetails.
        :type private_endpoint_id: str

        :param spark_version:
            The value to assign to the spark_version property of this CreateApplicationDetails.
        :type spark_version: str

        :param warehouse_bucket_uri:
            The value to assign to the warehouse_bucket_uri property of this CreateApplicationDetails.
        :type warehouse_bucket_uri: str

        """
        self.swagger_types = {
            'archive_uri': 'str',
            'arguments': 'list[str]',
            'class_name': 'str',
            'compartment_id': 'str',
            'configuration': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'driver_shape': 'str',
            'executor_shape': 'str',
            'file_uri': 'str',
            'freeform_tags': 'dict(str, str)',
            'language': 'str',
            'logs_bucket_uri': 'str',
            'num_executors': 'int',
            'parameters': 'list[ApplicationParameter]',
            'private_endpoint_id': 'str',
            'spark_version': 'str',
            'warehouse_bucket_uri': 'str'
        }

        self.attribute_map = {
            'archive_uri': 'archiveUri',
            'arguments': 'arguments',
            'class_name': 'className',
            'compartment_id': 'compartmentId',
            'configuration': 'configuration',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'driver_shape': 'driverShape',
            'executor_shape': 'executorShape',
            'file_uri': 'fileUri',
            'freeform_tags': 'freeformTags',
            'language': 'language',
            'logs_bucket_uri': 'logsBucketUri',
            'num_executors': 'numExecutors',
            'parameters': 'parameters',
            'private_endpoint_id': 'privateEndpointId',
            'spark_version': 'sparkVersion',
            'warehouse_bucket_uri': 'warehouseBucketUri'
        }

        self._archive_uri = None
        self._arguments = None
        self._class_name = None
        self._compartment_id = None
        self._configuration = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._driver_shape = None
        self._executor_shape = None
        self._file_uri = None
        self._freeform_tags = None
        self._language = None
        self._logs_bucket_uri = None
        self._num_executors = None
        self._parameters = None
        self._private_endpoint_id = None
        self._spark_version = None
        self._warehouse_bucket_uri = None

    @property
    def archive_uri(self):
        """
        Gets the archive_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution a Python, Java, or Scala application.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :return: The archive_uri of this CreateApplicationDetails.
        :rtype: str
        """
        return self._archive_uri

    @archive_uri.setter
    def archive_uri(self, archive_uri):
        """
        Sets the archive_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution a Python, Java, or Scala application.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :param archive_uri: The archive_uri of this CreateApplicationDetails.
        :type: str
        """
        self._archive_uri = archive_uri

    @property
    def arguments(self):
        """
        Gets the arguments of this CreateApplicationDetails.
        The arguments passed to the running application as command line arguments.  An argument is
        either a plain text or a placeholder. Placeholders are replaced using values from the parameters
        map.  Each placeholder specified must be represented in the parameters map else the request
        (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
        `Service Api Spec`, where `name` is the name of the parameter.
        Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]`
        If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to
        `--input mydata.xml --name \"John Doe\"`


        :return: The arguments of this CreateApplicationDetails.
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this CreateApplicationDetails.
        The arguments passed to the running application as command line arguments.  An argument is
        either a plain text or a placeholder. Placeholders are replaced using values from the parameters
        map.  Each placeholder specified must be represented in the parameters map else the request
        (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
        `Service Api Spec`, where `name` is the name of the parameter.
        Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]`
        If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to
        `--input mydata.xml --name \"John Doe\"`


        :param arguments: The arguments of this CreateApplicationDetails.
        :type: list[str]
        """
        self._arguments = arguments

    @property
    def class_name(self):
        """
        Gets the class_name of this CreateApplicationDetails.
        The class for the application.


        :return: The class_name of this CreateApplicationDetails.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """
        Sets the class_name of this CreateApplicationDetails.
        The class for the application.


        :param class_name: The class_name of this CreateApplicationDetails.
        :type: str
        """
        self._class_name = class_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateApplicationDetails.
        The OCID of a compartment.


        :return: The compartment_id of this CreateApplicationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateApplicationDetails.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this CreateApplicationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def configuration(self):
        """
        Gets the configuration of this CreateApplicationDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :return: The configuration of this CreateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this CreateApplicationDetails.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties.
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :param configuration: The configuration of this CreateApplicationDetails.
        :type: dict(str, str)
        """
        self._configuration = configuration

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateApplicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateApplicationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateApplicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this CreateApplicationDetails.
        A user-friendly description. Avoid entering confidential information.


        :return: The description of this CreateApplicationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateApplicationDetails.
        A user-friendly description. Avoid entering confidential information.


        :param description: The description of this CreateApplicationDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateApplicationDetails.
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.


        :return: The display_name of this CreateApplicationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateApplicationDetails.
        A user-friendly name. It does not have to be unique. Avoid entering confidential information.


        :param display_name: The display_name of this CreateApplicationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def driver_shape(self):
        """
        **[Required]** Gets the driver_shape of this CreateApplicationDetails.
        The VM shape for the driver. Sets the driver cores and memory.


        :return: The driver_shape of this CreateApplicationDetails.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this CreateApplicationDetails.
        The VM shape for the driver. Sets the driver cores and memory.


        :param driver_shape: The driver_shape of this CreateApplicationDetails.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def executor_shape(self):
        """
        **[Required]** Gets the executor_shape of this CreateApplicationDetails.
        The VM shape for the executors. Sets the executor cores and memory.


        :return: The executor_shape of this CreateApplicationDetails.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this CreateApplicationDetails.
        The VM shape for the executors. Sets the executor cores and memory.


        :param executor_shape: The executor_shape of this CreateApplicationDetails.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def file_uri(self):
        """
        **[Required]** Gets the file_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of the file containing the application to execute.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :return: The file_uri of this CreateApplicationDetails.
        :rtype: str
        """
        return self._file_uri

    @file_uri.setter
    def file_uri(self, file_uri):
        """
        Sets the file_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of the file containing the application to execute.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :param file_uri: The file_uri of this CreateApplicationDetails.
        :type: str
        """
        self._file_uri = file_uri

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateApplicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateApplicationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateApplicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def language(self):
        """
        **[Required]** Gets the language of this CreateApplicationDetails.
        The Spark language.

        Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL"


        :return: The language of this CreateApplicationDetails.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this CreateApplicationDetails.
        The Spark language.


        :param language: The language of this CreateApplicationDetails.
        :type: str
        """
        allowed_values = ["SCALA", "JAVA", "PYTHON", "SQL"]
        if not value_allowed_none_or_none_sentinel(language, allowed_values):
            raise ValueError(
                "Invalid value for `language`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._language = language

    @property
    def logs_bucket_uri(self):
        """
        Gets the logs_bucket_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :return: The logs_bucket_uri of this CreateApplicationDetails.
        :rtype: str
        """
        return self._logs_bucket_uri

    @logs_bucket_uri.setter
    def logs_bucket_uri(self, logs_bucket_uri):
        """
        Sets the logs_bucket_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :param logs_bucket_uri: The logs_bucket_uri of this CreateApplicationDetails.
        :type: str
        """
        self._logs_bucket_uri = logs_bucket_uri

    @property
    def num_executors(self):
        """
        **[Required]** Gets the num_executors of this CreateApplicationDetails.
        The number of executor VMs requested.


        :return: The num_executors of this CreateApplicationDetails.
        :rtype: int
        """
        return self._num_executors

    @num_executors.setter
    def num_executors(self, num_executors):
        """
        Sets the num_executors of this CreateApplicationDetails.
        The number of executor VMs requested.


        :param num_executors: The num_executors of this CreateApplicationDetails.
        :type: int
        """
        self._num_executors = num_executors

    @property
    def parameters(self):
        """
        Gets the parameters of this CreateApplicationDetails.
        An array of name/value pairs used to fill placeholders found in properties like
        `Application.arguments`.  The name must be a string of one or more word characters
        (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
        Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]


        :return: The parameters of this CreateApplicationDetails.
        :rtype: list[ApplicationParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this CreateApplicationDetails.
        An array of name/value pairs used to fill placeholders found in properties like
        `Application.arguments`.  The name must be a string of one or more word characters
        (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
        Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]


        :param parameters: The parameters of this CreateApplicationDetails.
        :type: list[ApplicationParameter]
        """
        self._parameters = parameters

    @property
    def private_endpoint_id(self):
        """
        Gets the private_endpoint_id of this CreateApplicationDetails.
        The OCID of a private endpoint.


        :return: The private_endpoint_id of this CreateApplicationDetails.
        :rtype: str
        """
        return self._private_endpoint_id

    @private_endpoint_id.setter
    def private_endpoint_id(self, private_endpoint_id):
        """
        Sets the private_endpoint_id of this CreateApplicationDetails.
        The OCID of a private endpoint.


        :param private_endpoint_id: The private_endpoint_id of this CreateApplicationDetails.
        :type: str
        """
        self._private_endpoint_id = private_endpoint_id

    @property
    def spark_version(self):
        """
        **[Required]** Gets the spark_version of this CreateApplicationDetails.
        The Spark version utilized to run the application.


        :return: The spark_version of this CreateApplicationDetails.
        :rtype: str
        """
        return self._spark_version

    @spark_version.setter
    def spark_version(self, spark_version):
        """
        Sets the spark_version of this CreateApplicationDetails.
        The Spark version utilized to run the application.


        :param spark_version: The spark_version of this CreateApplicationDetails.
        :type: str
        """
        self._spark_version = spark_version

    @property
    def warehouse_bucket_uri(self):
        """
        Gets the warehouse_bucket_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
        for BATCH SQL runs.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :return: The warehouse_bucket_uri of this CreateApplicationDetails.
        :rtype: str
        """
        return self._warehouse_bucket_uri

    @warehouse_bucket_uri.setter
    def warehouse_bucket_uri(self, warehouse_bucket_uri):
        """
        Sets the warehouse_bucket_uri of this CreateApplicationDetails.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
        for BATCH SQL runs.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.


        :param warehouse_bucket_uri: The warehouse_bucket_uri of this CreateApplicationDetails.
        :type: str
        """
        self._warehouse_bucket_uri = warehouse_bucket_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
