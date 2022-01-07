# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskSchedule(object):
    """
    A model that holds Schedule and other information required for scheduling a task.
    """

    #: A constant which can be used with the retry_delay_unit property of a TaskSchedule.
    #: This constant has a value of "SECONDS"
    RETRY_DELAY_UNIT_SECONDS = "SECONDS"

    #: A constant which can be used with the retry_delay_unit property of a TaskSchedule.
    #: This constant has a value of "MINUTES"
    RETRY_DELAY_UNIT_MINUTES = "MINUTES"

    #: A constant which can be used with the retry_delay_unit property of a TaskSchedule.
    #: This constant has a value of "HOURS"
    RETRY_DELAY_UNIT_HOURS = "HOURS"

    #: A constant which can be used with the retry_delay_unit property of a TaskSchedule.
    #: This constant has a value of "DAYS"
    RETRY_DELAY_UNIT_DAYS = "DAYS"

    #: A constant which can be used with the auth_mode property of a TaskSchedule.
    #: This constant has a value of "OBO"
    AUTH_MODE_OBO = "OBO"

    #: A constant which can be used with the auth_mode property of a TaskSchedule.
    #: This constant has a value of "RESOURCE_PRINCIPAL"
    AUTH_MODE_RESOURCE_PRINCIPAL = "RESOURCE_PRINCIPAL"

    #: A constant which can be used with the auth_mode property of a TaskSchedule.
    #: This constant has a value of "USER_CERTIFICATE"
    AUTH_MODE_USER_CERTIFICATE = "USER_CERTIFICATE"

    #: A constant which can be used with the expected_duration_unit property of a TaskSchedule.
    #: This constant has a value of "SECONDS"
    EXPECTED_DURATION_UNIT_SECONDS = "SECONDS"

    #: A constant which can be used with the expected_duration_unit property of a TaskSchedule.
    #: This constant has a value of "MINUTES"
    EXPECTED_DURATION_UNIT_MINUTES = "MINUTES"

    #: A constant which can be used with the expected_duration_unit property of a TaskSchedule.
    #: This constant has a value of "HOURS"
    EXPECTED_DURATION_UNIT_HOURS = "HOURS"

    #: A constant which can be used with the expected_duration_unit property of a TaskSchedule.
    #: This constant has a value of "DAYS"
    EXPECTED_DURATION_UNIT_DAYS = "DAYS"

    def __init__(self, **kwargs):
        """
        Initializes a new TaskSchedule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TaskSchedule.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TaskSchedule.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this TaskSchedule.
        :type model_type: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskSchedule.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TaskSchedule.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskSchedule.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskSchedule.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this TaskSchedule.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this TaskSchedule.
        :type identifier: str

        :param schedule_ref:
            The value to assign to the schedule_ref property of this TaskSchedule.
        :type schedule_ref: oci.data_integration.models.Schedule

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this TaskSchedule.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

        :param is_enabled:
            The value to assign to the is_enabled property of this TaskSchedule.
        :type is_enabled: bool

        :param retry_attempts:
            The value to assign to the retry_attempts property of this TaskSchedule.
        :type retry_attempts: int

        :param retry_delay_unit:
            The value to assign to the retry_delay_unit property of this TaskSchedule.
            Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type retry_delay_unit: str

        :param retry_delay:
            The value to assign to the retry_delay property of this TaskSchedule.
        :type retry_delay: float

        :param start_time_millis:
            The value to assign to the start_time_millis property of this TaskSchedule.
        :type start_time_millis: int

        :param end_time_millis:
            The value to assign to the end_time_millis property of this TaskSchedule.
        :type end_time_millis: int

        :param is_concurrent_allowed:
            The value to assign to the is_concurrent_allowed property of this TaskSchedule.
        :type is_concurrent_allowed: bool

        :param is_backfill_enabled:
            The value to assign to the is_backfill_enabled property of this TaskSchedule.
        :type is_backfill_enabled: bool

        :param auth_mode:
            The value to assign to the auth_mode property of this TaskSchedule.
            Allowed values for this property are: "OBO", "RESOURCE_PRINCIPAL", "USER_CERTIFICATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type auth_mode: str

        :param expected_duration:
            The value to assign to the expected_duration property of this TaskSchedule.
        :type expected_duration: float

        :param expected_duration_unit:
            The value to assign to the expected_duration_unit property of this TaskSchedule.
            Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type expected_duration_unit: str

        :param last_run_details:
            The value to assign to the last_run_details property of this TaskSchedule.
        :type last_run_details: oci.data_integration.models.LastRunDetails

        :param metadata:
            The value to assign to the metadata property of this TaskSchedule.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'schedule_ref': 'Schedule',
            'config_provider_delegate': 'ConfigProvider',
            'is_enabled': 'bool',
            'retry_attempts': 'int',
            'retry_delay_unit': 'str',
            'retry_delay': 'float',
            'start_time_millis': 'int',
            'end_time_millis': 'int',
            'is_concurrent_allowed': 'bool',
            'is_backfill_enabled': 'bool',
            'auth_mode': 'str',
            'expected_duration': 'float',
            'expected_duration_unit': 'str',
            'last_run_details': 'LastRunDetails',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'schedule_ref': 'scheduleRef',
            'config_provider_delegate': 'configProviderDelegate',
            'is_enabled': 'isEnabled',
            'retry_attempts': 'retryAttempts',
            'retry_delay_unit': 'retryDelayUnit',
            'retry_delay': 'retryDelay',
            'start_time_millis': 'startTimeMillis',
            'end_time_millis': 'endTimeMillis',
            'is_concurrent_allowed': 'isConcurrentAllowed',
            'is_backfill_enabled': 'isBackfillEnabled',
            'auth_mode': 'authMode',
            'expected_duration': 'expectedDuration',
            'expected_duration_unit': 'expectedDurationUnit',
            'last_run_details': 'lastRunDetails',
            'metadata': 'metadata'
        }

        self._key = None
        self._model_version = None
        self._model_type = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._schedule_ref = None
        self._config_provider_delegate = None
        self._is_enabled = None
        self._retry_attempts = None
        self._retry_delay_unit = None
        self._retry_delay = None
        self._start_time_millis = None
        self._end_time_millis = None
        self._is_concurrent_allowed = None
        self._is_backfill_enabled = None
        self._auth_mode = None
        self._expected_duration = None
        self._expected_duration_unit = None
        self._last_run_details = None
        self._metadata = None

    @property
    def key(self):
        """
        Gets the key of this TaskSchedule.
        Generated key that can be used in API calls to identify taskSchedule. On scenarios where reference to the taskSchedule is needed, a value can be passed in create.


        :return: The key of this TaskSchedule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TaskSchedule.
        Generated key that can be used in API calls to identify taskSchedule. On scenarios where reference to the taskSchedule is needed, a value can be passed in create.


        :param key: The key of this TaskSchedule.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this TaskSchedule.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :return: The model_version of this TaskSchedule.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this TaskSchedule.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :param model_version: The model_version of this TaskSchedule.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        Gets the model_type of this TaskSchedule.
        The type of the object.


        :return: The model_type of this TaskSchedule.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this TaskSchedule.
        The type of the object.


        :param model_type: The model_type of this TaskSchedule.
        :type: str
        """
        self._model_type = model_type

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this TaskSchedule.

        :return: The parent_ref of this TaskSchedule.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this TaskSchedule.

        :param parent_ref: The parent_ref of this TaskSchedule.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this TaskSchedule.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this TaskSchedule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaskSchedule.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this TaskSchedule.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TaskSchedule.
        Detailed description for the object.


        :return: The description of this TaskSchedule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TaskSchedule.
        Detailed description for the object.


        :param description: The description of this TaskSchedule.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this TaskSchedule.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :return: The object_version of this TaskSchedule.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this TaskSchedule.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :param object_version: The object_version of this TaskSchedule.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this TaskSchedule.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this TaskSchedule.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this TaskSchedule.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this TaskSchedule.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this TaskSchedule.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this TaskSchedule.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this TaskSchedule.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this TaskSchedule.
        :type: str
        """
        self._identifier = identifier

    @property
    def schedule_ref(self):
        """
        Gets the schedule_ref of this TaskSchedule.

        :return: The schedule_ref of this TaskSchedule.
        :rtype: oci.data_integration.models.Schedule
        """
        return self._schedule_ref

    @schedule_ref.setter
    def schedule_ref(self, schedule_ref):
        """
        Sets the schedule_ref of this TaskSchedule.

        :param schedule_ref: The schedule_ref of this TaskSchedule.
        :type: oci.data_integration.models.Schedule
        """
        self._schedule_ref = schedule_ref

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this TaskSchedule.

        :return: The config_provider_delegate of this TaskSchedule.
        :rtype: oci.data_integration.models.ConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this TaskSchedule.

        :param config_provider_delegate: The config_provider_delegate of this TaskSchedule.
        :type: oci.data_integration.models.ConfigProvider
        """
        self._config_provider_delegate = config_provider_delegate

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this TaskSchedule.
        Whether the schedule is enabled.


        :return: The is_enabled of this TaskSchedule.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this TaskSchedule.
        Whether the schedule is enabled.


        :param is_enabled: The is_enabled of this TaskSchedule.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def retry_attempts(self):
        """
        Gets the retry_attempts of this TaskSchedule.
        The number of retry attempts.


        :return: The retry_attempts of this TaskSchedule.
        :rtype: int
        """
        return self._retry_attempts

    @retry_attempts.setter
    def retry_attempts(self, retry_attempts):
        """
        Sets the retry_attempts of this TaskSchedule.
        The number of retry attempts.


        :param retry_attempts: The retry_attempts of this TaskSchedule.
        :type: int
        """
        self._retry_attempts = retry_attempts

    @property
    def retry_delay_unit(self):
        """
        Gets the retry_delay_unit of this TaskSchedule.
        The unit for the retry delay.

        Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The retry_delay_unit of this TaskSchedule.
        :rtype: str
        """
        return self._retry_delay_unit

    @retry_delay_unit.setter
    def retry_delay_unit(self, retry_delay_unit):
        """
        Sets the retry_delay_unit of this TaskSchedule.
        The unit for the retry delay.


        :param retry_delay_unit: The retry_delay_unit of this TaskSchedule.
        :type: str
        """
        allowed_values = ["SECONDS", "MINUTES", "HOURS", "DAYS"]
        if not value_allowed_none_or_none_sentinel(retry_delay_unit, allowed_values):
            retry_delay_unit = 'UNKNOWN_ENUM_VALUE'
        self._retry_delay_unit = retry_delay_unit

    @property
    def retry_delay(self):
        """
        Gets the retry_delay of this TaskSchedule.
        The retry delay, the unit for measurement is in the property retry delay unit.


        :return: The retry_delay of this TaskSchedule.
        :rtype: float
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """
        Sets the retry_delay of this TaskSchedule.
        The retry delay, the unit for measurement is in the property retry delay unit.


        :param retry_delay: The retry_delay of this TaskSchedule.
        :type: float
        """
        self._retry_delay = retry_delay

    @property
    def start_time_millis(self):
        """
        Gets the start_time_millis of this TaskSchedule.
        The start time in milliseconds.


        :return: The start_time_millis of this TaskSchedule.
        :rtype: int
        """
        return self._start_time_millis

    @start_time_millis.setter
    def start_time_millis(self, start_time_millis):
        """
        Sets the start_time_millis of this TaskSchedule.
        The start time in milliseconds.


        :param start_time_millis: The start_time_millis of this TaskSchedule.
        :type: int
        """
        self._start_time_millis = start_time_millis

    @property
    def end_time_millis(self):
        """
        Gets the end_time_millis of this TaskSchedule.
        The end time in milliseconds.


        :return: The end_time_millis of this TaskSchedule.
        :rtype: int
        """
        return self._end_time_millis

    @end_time_millis.setter
    def end_time_millis(self, end_time_millis):
        """
        Sets the end_time_millis of this TaskSchedule.
        The end time in milliseconds.


        :param end_time_millis: The end_time_millis of this TaskSchedule.
        :type: int
        """
        self._end_time_millis = end_time_millis

    @property
    def is_concurrent_allowed(self):
        """
        Gets the is_concurrent_allowed of this TaskSchedule.
        Whether the same task can be executed concurrently.


        :return: The is_concurrent_allowed of this TaskSchedule.
        :rtype: bool
        """
        return self._is_concurrent_allowed

    @is_concurrent_allowed.setter
    def is_concurrent_allowed(self, is_concurrent_allowed):
        """
        Sets the is_concurrent_allowed of this TaskSchedule.
        Whether the same task can be executed concurrently.


        :param is_concurrent_allowed: The is_concurrent_allowed of this TaskSchedule.
        :type: bool
        """
        self._is_concurrent_allowed = is_concurrent_allowed

    @property
    def is_backfill_enabled(self):
        """
        Gets the is_backfill_enabled of this TaskSchedule.
        Whether the backfill is enabled


        :return: The is_backfill_enabled of this TaskSchedule.
        :rtype: bool
        """
        return self._is_backfill_enabled

    @is_backfill_enabled.setter
    def is_backfill_enabled(self, is_backfill_enabled):
        """
        Sets the is_backfill_enabled of this TaskSchedule.
        Whether the backfill is enabled


        :param is_backfill_enabled: The is_backfill_enabled of this TaskSchedule.
        :type: bool
        """
        self._is_backfill_enabled = is_backfill_enabled

    @property
    def auth_mode(self):
        """
        Gets the auth_mode of this TaskSchedule.
        The authorization mode for the task.

        Allowed values for this property are: "OBO", "RESOURCE_PRINCIPAL", "USER_CERTIFICATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The auth_mode of this TaskSchedule.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """
        Sets the auth_mode of this TaskSchedule.
        The authorization mode for the task.


        :param auth_mode: The auth_mode of this TaskSchedule.
        :type: str
        """
        allowed_values = ["OBO", "RESOURCE_PRINCIPAL", "USER_CERTIFICATE"]
        if not value_allowed_none_or_none_sentinel(auth_mode, allowed_values):
            auth_mode = 'UNKNOWN_ENUM_VALUE'
        self._auth_mode = auth_mode

    @property
    def expected_duration(self):
        """
        Gets the expected_duration of this TaskSchedule.
        The expected duration of the task execution.


        :return: The expected_duration of this TaskSchedule.
        :rtype: float
        """
        return self._expected_duration

    @expected_duration.setter
    def expected_duration(self, expected_duration):
        """
        Sets the expected_duration of this TaskSchedule.
        The expected duration of the task execution.


        :param expected_duration: The expected_duration of this TaskSchedule.
        :type: float
        """
        self._expected_duration = expected_duration

    @property
    def expected_duration_unit(self):
        """
        Gets the expected_duration_unit of this TaskSchedule.
        The expected duration unit of the task execution.

        Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The expected_duration_unit of this TaskSchedule.
        :rtype: str
        """
        return self._expected_duration_unit

    @expected_duration_unit.setter
    def expected_duration_unit(self, expected_duration_unit):
        """
        Sets the expected_duration_unit of this TaskSchedule.
        The expected duration unit of the task execution.


        :param expected_duration_unit: The expected_duration_unit of this TaskSchedule.
        :type: str
        """
        allowed_values = ["SECONDS", "MINUTES", "HOURS", "DAYS"]
        if not value_allowed_none_or_none_sentinel(expected_duration_unit, allowed_values):
            expected_duration_unit = 'UNKNOWN_ENUM_VALUE'
        self._expected_duration_unit = expected_duration_unit

    @property
    def last_run_details(self):
        """
        Gets the last_run_details of this TaskSchedule.

        :return: The last_run_details of this TaskSchedule.
        :rtype: oci.data_integration.models.LastRunDetails
        """
        return self._last_run_details

    @last_run_details.setter
    def last_run_details(self, last_run_details):
        """
        Sets the last_run_details of this TaskSchedule.

        :param last_run_details: The last_run_details of this TaskSchedule.
        :type: oci.data_integration.models.LastRunDetails
        """
        self._last_run_details = last_run_details

    @property
    def metadata(self):
        """
        Gets the metadata of this TaskSchedule.

        :return: The metadata of this TaskSchedule.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TaskSchedule.

        :param metadata: The metadata of this TaskSchedule.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
