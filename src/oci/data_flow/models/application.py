# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Application(object):
    """
    A data flow application object.
    """

    #: A constant which can be used with the language property of a Application.
    #: This constant has a value of "SCALA"
    LANGUAGE_SCALA = "SCALA"

    #: A constant which can be used with the language property of a Application.
    #: This constant has a value of "JAVA"
    LANGUAGE_JAVA = "JAVA"

    #: A constant which can be used with the language property of a Application.
    #: This constant has a value of "PYTHON"
    LANGUAGE_PYTHON = "PYTHON"

    #: A constant which can be used with the language property of a Application.
    #: This constant has a value of "SQL"
    LANGUAGE_SQL = "SQL"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Application.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new Application object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param arguments:
            The value to assign to the arguments property of this Application.
        :type arguments: list[str]

        :param class_name:
            The value to assign to the class_name property of this Application.
        :type class_name: str

        :param configuration:
            The value to assign to the configuration property of this Application.
        :type configuration: dict(str, str)

        :param compartment_id:
            The value to assign to the compartment_id property of this Application.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this Application.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this Application.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this Application.
        :type display_name: str

        :param driver_shape:
            The value to assign to the driver_shape property of this Application.
        :type driver_shape: str

        :param executor_shape:
            The value to assign to the executor_shape property of this Application.
        :type executor_shape: str

        :param file_uri:
            The value to assign to the file_uri property of this Application.
        :type file_uri: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Application.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this Application.
        :type id: str

        :param language:
            The value to assign to the language property of this Application.
            Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type language: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Application.
            Allowed values for this property are: "ACTIVE", "DELETED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param logs_bucket_uri:
            The value to assign to the logs_bucket_uri property of this Application.
        :type logs_bucket_uri: str

        :param num_executors:
            The value to assign to the num_executors property of this Application.
        :type num_executors: int

        :param owner_principal_id:
            The value to assign to the owner_principal_id property of this Application.
        :type owner_principal_id: str

        :param owner_user_name:
            The value to assign to the owner_user_name property of this Application.
        :type owner_user_name: str

        :param parameters:
            The value to assign to the parameters property of this Application.
        :type parameters: list[ApplicationParameter]

        :param spark_version:
            The value to assign to the spark_version property of this Application.
        :type spark_version: str

        :param time_created:
            The value to assign to the time_created property of this Application.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Application.
        :type time_updated: datetime

        :param warehouse_bucket_uri:
            The value to assign to the warehouse_bucket_uri property of this Application.
        :type warehouse_bucket_uri: str

        """
        self.swagger_types = {
            'arguments': 'list[str]',
            'class_name': 'str',
            'configuration': 'dict(str, str)',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'driver_shape': 'str',
            'executor_shape': 'str',
            'file_uri': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'language': 'str',
            'lifecycle_state': 'str',
            'logs_bucket_uri': 'str',
            'num_executors': 'int',
            'owner_principal_id': 'str',
            'owner_user_name': 'str',
            'parameters': 'list[ApplicationParameter]',
            'spark_version': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'warehouse_bucket_uri': 'str'
        }

        self.attribute_map = {
            'arguments': 'arguments',
            'class_name': 'className',
            'configuration': 'configuration',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'driver_shape': 'driverShape',
            'executor_shape': 'executorShape',
            'file_uri': 'fileUri',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'language': 'language',
            'lifecycle_state': 'lifecycleState',
            'logs_bucket_uri': 'logsBucketUri',
            'num_executors': 'numExecutors',
            'owner_principal_id': 'ownerPrincipalId',
            'owner_user_name': 'ownerUserName',
            'parameters': 'parameters',
            'spark_version': 'sparkVersion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'warehouse_bucket_uri': 'warehouseBucketUri'
        }

        self._arguments = None
        self._class_name = None
        self._configuration = None
        self._compartment_id = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._driver_shape = None
        self._executor_shape = None
        self._file_uri = None
        self._freeform_tags = None
        self._id = None
        self._language = None
        self._lifecycle_state = None
        self._logs_bucket_uri = None
        self._num_executors = None
        self._owner_principal_id = None
        self._owner_user_name = None
        self._parameters = None
        self._spark_version = None
        self._time_created = None
        self._time_updated = None
        self._warehouse_bucket_uri = None

    @property
    def arguments(self):
        """
        Gets the arguments of this Application.
        The arguments passed to the running application as command line arguments.  An argument is
        either a plain text or a placeholder. Placeholders are replaced using values from the parameters
        map.  Each placeholder specified must be represented in the parameters map else the request
        (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
        `Service Api Spec`, where `name` is the name of the parameter.
        Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]`
        If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to
        `--input mydata.xml --name \"John Doe\"`


        :return: The arguments of this Application.
        :rtype: list[str]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this Application.
        The arguments passed to the running application as command line arguments.  An argument is
        either a plain text or a placeholder. Placeholders are replaced using values from the parameters
        map.  Each placeholder specified must be represented in the parameters map else the request
        (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
        `Service Api Spec`, where `name` is the name of the parameter.
        Example:  `[ \"--input\", \"${input_file}\", \"--name\", \"John Doe\" ]`
        If \"input_file\" has a value of \"mydata.xml\", then the value above will be translated to
        `--input mydata.xml --name \"John Doe\"`


        :param arguments: The arguments of this Application.
        :type: list[str]
        """
        self._arguments = arguments

    @property
    def class_name(self):
        """
        Gets the class_name of this Application.
        The class for the application.


        :return: The class_name of this Application.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """
        Sets the class_name of this Application.
        The class for the application.


        :param class_name: The class_name of this Application.
        :type: str
        """
        self._class_name = class_name

    @property
    def configuration(self):
        """
        Gets the configuration of this Application.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :return: The configuration of this Application.
        :rtype: dict(str, str)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """
        Sets the configuration of this Application.
        The Spark configuration passed to the running process.
        See https://spark.apache.org/docs/latest/configuration.html#available-properties
        Example: { \"spark.app.name\" : \"My App Name\", \"spark.shuffle.io.maxRetries\" : \"4\" }
        Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
        not allowed to be overwritten will cause a 400 status to be returned.


        :param configuration: The configuration of this Application.
        :type: dict(str, str)
        """
        self._configuration = configuration

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Application.
        The OCID of a compartment.


        :return: The compartment_id of this Application.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Application.
        The OCID of a compartment.


        :param compartment_id: The compartment_id of this Application.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Application.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Application.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Application.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Application.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this Application.
        A user-friendly description.


        :return: The description of this Application.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Application.
        A user-friendly description.


        :param description: The description of this Application.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Application.
        A user-friendly name. This name is not necessarily unique.


        :return: The display_name of this Application.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Application.
        A user-friendly name. This name is not necessarily unique.


        :param display_name: The display_name of this Application.
        :type: str
        """
        self._display_name = display_name

    @property
    def driver_shape(self):
        """
        **[Required]** Gets the driver_shape of this Application.
        The VM shape for the driver. Sets the driver cores and memory.


        :return: The driver_shape of this Application.
        :rtype: str
        """
        return self._driver_shape

    @driver_shape.setter
    def driver_shape(self, driver_shape):
        """
        Sets the driver_shape of this Application.
        The VM shape for the driver. Sets the driver cores and memory.


        :param driver_shape: The driver_shape of this Application.
        :type: str
        """
        self._driver_shape = driver_shape

    @property
    def executor_shape(self):
        """
        **[Required]** Gets the executor_shape of this Application.
        The VM shape for the executors. Sets the executor cores and memory.


        :return: The executor_shape of this Application.
        :rtype: str
        """
        return self._executor_shape

    @executor_shape.setter
    def executor_shape(self, executor_shape):
        """
        Sets the executor_shape of this Application.
        The VM shape for the executors. Sets the executor cores and memory.


        :param executor_shape: The executor_shape of this Application.
        :type: str
        """
        self._executor_shape = executor_shape

    @property
    def file_uri(self):
        """
        **[Required]** Gets the file_uri of this Application.
        An Oracle Cloud Infrastructure URI of the file containing the application to execute.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat


        :return: The file_uri of this Application.
        :rtype: str
        """
        return self._file_uri

    @file_uri.setter
    def file_uri(self, file_uri):
        """
        Sets the file_uri of this Application.
        An Oracle Cloud Infrastructure URI of the file containing the application to execute.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat


        :param file_uri: The file_uri of this Application.
        :type: str
        """
        self._file_uri = file_uri

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Application.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Application.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Application.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Application.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Application.
        The application ID.


        :return: The id of this Application.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Application.
        The application ID.


        :param id: The id of this Application.
        :type: str
        """
        self._id = id

    @property
    def language(self):
        """
        **[Required]** Gets the language of this Application.
        The Spark language.

        Allowed values for this property are: "SCALA", "JAVA", "PYTHON", "SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The language of this Application.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Application.
        The Spark language.


        :param language: The language of this Application.
        :type: str
        """
        allowed_values = ["SCALA", "JAVA", "PYTHON", "SQL"]
        if not value_allowed_none_or_none_sentinel(language, allowed_values):
            language = 'UNKNOWN_ENUM_VALUE'
        self._language = language

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Application.
        The current state of this application.

        Allowed values for this property are: "ACTIVE", "DELETED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Application.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Application.
        The current state of this application.


        :param lifecycle_state: The lifecycle_state of this Application.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def logs_bucket_uri(self):
        """
        Gets the logs_bucket_uri of this Application.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat


        :return: The logs_bucket_uri of this Application.
        :rtype: str
        """
        return self._logs_bucket_uri

    @logs_bucket_uri.setter
    def logs_bucket_uri(self, logs_bucket_uri):
        """
        Sets the logs_bucket_uri of this Application.
        An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat


        :param logs_bucket_uri: The logs_bucket_uri of this Application.
        :type: str
        """
        self._logs_bucket_uri = logs_bucket_uri

    @property
    def num_executors(self):
        """
        **[Required]** Gets the num_executors of this Application.
        The number of executor VMs requested.


        :return: The num_executors of this Application.
        :rtype: int
        """
        return self._num_executors

    @num_executors.setter
    def num_executors(self, num_executors):
        """
        Sets the num_executors of this Application.
        The number of executor VMs requested.


        :param num_executors: The num_executors of this Application.
        :type: int
        """
        self._num_executors = num_executors

    @property
    def owner_principal_id(self):
        """
        **[Required]** Gets the owner_principal_id of this Application.
        The OCID of the user who created the resource.


        :return: The owner_principal_id of this Application.
        :rtype: str
        """
        return self._owner_principal_id

    @owner_principal_id.setter
    def owner_principal_id(self, owner_principal_id):
        """
        Sets the owner_principal_id of this Application.
        The OCID of the user who created the resource.


        :param owner_principal_id: The owner_principal_id of this Application.
        :type: str
        """
        self._owner_principal_id = owner_principal_id

    @property
    def owner_user_name(self):
        """
        Gets the owner_user_name of this Application.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :return: The owner_user_name of this Application.
        :rtype: str
        """
        return self._owner_user_name

    @owner_user_name.setter
    def owner_user_name(self, owner_user_name):
        """
        Sets the owner_user_name of this Application.
        The username of the user who created the resource.  If the username of the owner does not exist,
        `null` will be returned and the caller should refer to the ownerPrincipalId value instead.


        :param owner_user_name: The owner_user_name of this Application.
        :type: str
        """
        self._owner_user_name = owner_user_name

    @property
    def parameters(self):
        """
        Gets the parameters of this Application.
        An array of name/value pairs used to fill placeholders found in properties like
        `Application.arguments`.  The name must be a string of one or more word characters
        (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
        Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]


        :return: The parameters of this Application.
        :rtype: list[ApplicationParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this Application.
        An array of name/value pairs used to fill placeholders found in properties like
        `Application.arguments`.  The name must be a string of one or more word characters
        (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
        Example:  [ { name: \"iterations\", value: \"10\"}, { name: \"input_file\", value: \"mydata.xml\" }, { name: \"variable_x\", value: \"${x}\"} ]


        :param parameters: The parameters of this Application.
        :type: list[ApplicationParameter]
        """
        self._parameters = parameters

    @property
    def spark_version(self):
        """
        **[Required]** Gets the spark_version of this Application.
        The Spark version utilized to run the application.


        :return: The spark_version of this Application.
        :rtype: str
        """
        return self._spark_version

    @spark_version.setter
    def spark_version(self, spark_version):
        """
        Sets the spark_version of this Application.
        The Spark version utilized to run the application.


        :param spark_version: The spark_version of this Application.
        :type: str
        """
        self._spark_version = spark_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Application.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Application.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Application.
        The date and time a application was created, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Application.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Application.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Application.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Application.
        The date and time a application was updated, expressed in `RFC 3339`__ timestamp format.
        Example: `2018-04-03T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Application.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def warehouse_bucket_uri(self):
        """
        Gets the warehouse_bucket_uri of this Application.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
        for BATCH SQL runs.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat


        :return: The warehouse_bucket_uri of this Application.
        :rtype: str
        """
        return self._warehouse_bucket_uri

    @warehouse_bucket_uri.setter
    def warehouse_bucket_uri(self, warehouse_bucket_uri):
        """
        Sets the warehouse_bucket_uri of this Application.
        An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
        for BATCH SQL runs.
        See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat


        :param warehouse_bucket_uri: The warehouse_bucket_uri of this Application.
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
