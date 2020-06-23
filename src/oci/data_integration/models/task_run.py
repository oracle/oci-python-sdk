# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskRun(object):
    """
    The information about TaskRun.
    """

    #: A constant which can be used with the status property of a TaskRun.
    #: This constant has a value of "NOT_STARTED"
    STATUS_NOT_STARTED = "NOT_STARTED"

    #: A constant which can be used with the status property of a TaskRun.
    #: This constant has a value of "QUEUED"
    STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the status property of a TaskRun.
    #: This constant has a value of "RUNNING"
    STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the status property of a TaskRun.
    #: This constant has a value of "TERMINATING"
    STATUS_TERMINATING = "TERMINATING"

    #: A constant which can be used with the status property of a TaskRun.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the status property of a TaskRun.
    #: This constant has a value of "SUCCESS"
    STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the status property of a TaskRun.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the task_type property of a TaskRun.
    #: This constant has a value of "INTEGRATION_TASK"
    TASK_TYPE_INTEGRATION_TASK = "INTEGRATION_TASK"

    #: A constant which can be used with the task_type property of a TaskRun.
    #: This constant has a value of "DATA_LOADER_TASK"
    TASK_TYPE_DATA_LOADER_TASK = "DATA_LOADER_TASK"

    def __init__(self, **kwargs):
        """
        Initializes a new TaskRun object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TaskRun.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this TaskRun.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this TaskRun.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskRun.
        :type parent_ref: ParentReference

        :param name:
            The value to assign to the name property of this TaskRun.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskRun.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskRun.
        :type object_version: int

        :param config_provider:
            The value to assign to the config_provider property of this TaskRun.
        :type config_provider: ConfigProvider

        :param status:
            The value to assign to the status property of this TaskRun.
            Allowed values for this property are: "NOT_STARTED", "QUEUED", "RUNNING", "TERMINATING", "TERMINATED", "SUCCESS", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param start_time_millis:
            The value to assign to the start_time_millis property of this TaskRun.
        :type start_time_millis: int

        :param end_time_millis:
            The value to assign to the end_time_millis property of this TaskRun.
        :type end_time_millis: int

        :param last_updated:
            The value to assign to the last_updated property of this TaskRun.
        :type last_updated: int

        :param records_written:
            The value to assign to the records_written property of this TaskRun.
        :type records_written: int

        :param bytes_processed:
            The value to assign to the bytes_processed property of this TaskRun.
        :type bytes_processed: int

        :param error_message:
            The value to assign to the error_message property of this TaskRun.
        :type error_message: str

        :param opc_request_id:
            The value to assign to the opc_request_id property of this TaskRun.
        :type opc_request_id: str

        :param object_status:
            The value to assign to the object_status property of this TaskRun.
        :type object_status: int

        :param task_type:
            The value to assign to the task_type property of this TaskRun.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_type: str

        :param identifier:
            The value to assign to the identifier property of this TaskRun.
        :type identifier: str

        :param metadata:
            The value to assign to the metadata property of this TaskRun.
        :type metadata: ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this TaskRun.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'config_provider': 'ConfigProvider',
            'status': 'str',
            'start_time_millis': 'int',
            'end_time_millis': 'int',
            'last_updated': 'int',
            'records_written': 'int',
            'bytes_processed': 'int',
            'error_message': 'str',
            'opc_request_id': 'str',
            'object_status': 'int',
            'task_type': 'str',
            'identifier': 'str',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'config_provider': 'configProvider',
            'status': 'status',
            'start_time_millis': 'startTimeMillis',
            'end_time_millis': 'endTimeMillis',
            'last_updated': 'lastUpdated',
            'records_written': 'recordsWritten',
            'bytes_processed': 'bytesProcessed',
            'error_message': 'errorMessage',
            'opc_request_id': 'opcRequestId',
            'object_status': 'objectStatus',
            'task_type': 'taskType',
            'identifier': 'identifier',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._config_provider = None
        self._status = None
        self._start_time_millis = None
        self._end_time_millis = None
        self._last_updated = None
        self._records_written = None
        self._bytes_processed = None
        self._error_message = None
        self._opc_request_id = None
        self._object_status = None
        self._task_type = None
        self._identifier = None
        self._metadata = None
        self._key_map = None

    @property
    def key(self):
        """
        Gets the key of this TaskRun.
        The key of the object.


        :return: The key of this TaskRun.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TaskRun.
        The key of the object.


        :param key: The key of this TaskRun.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this TaskRun.
        The type of the object.


        :return: The model_type of this TaskRun.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this TaskRun.
        The type of the object.


        :param model_type: The model_type of this TaskRun.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this TaskRun.
        The model version of an object.


        :return: The model_version of this TaskRun.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this TaskRun.
        The model version of an object.


        :param model_version: The model_version of this TaskRun.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this TaskRun.

        :return: The parent_ref of this TaskRun.
        :rtype: ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this TaskRun.

        :param parent_ref: The parent_ref of this TaskRun.
        :type: ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this TaskRun.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :return: The name of this TaskRun.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaskRun.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :param name: The name of this TaskRun.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TaskRun.
        Detailed description for the object.


        :return: The description of this TaskRun.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TaskRun.
        Detailed description for the object.


        :param description: The description of this TaskRun.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this TaskRun.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this TaskRun.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this TaskRun.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this TaskRun.
        :type: int
        """
        self._object_version = object_version

    @property
    def config_provider(self):
        """
        Gets the config_provider of this TaskRun.

        :return: The config_provider of this TaskRun.
        :rtype: ConfigProvider
        """
        return self._config_provider

    @config_provider.setter
    def config_provider(self, config_provider):
        """
        Sets the config_provider of this TaskRun.

        :param config_provider: The config_provider of this TaskRun.
        :type: ConfigProvider
        """
        self._config_provider = config_provider

    @property
    def status(self):
        """
        Gets the status of this TaskRun.
        status

        Allowed values for this property are: "NOT_STARTED", "QUEUED", "RUNNING", "TERMINATING", "TERMINATED", "SUCCESS", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this TaskRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TaskRun.
        status


        :param status: The status of this TaskRun.
        :type: str
        """
        allowed_values = ["NOT_STARTED", "QUEUED", "RUNNING", "TERMINATING", "TERMINATED", "SUCCESS", "ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def start_time_millis(self):
        """
        Gets the start_time_millis of this TaskRun.
        startTimeMillis


        :return: The start_time_millis of this TaskRun.
        :rtype: int
        """
        return self._start_time_millis

    @start_time_millis.setter
    def start_time_millis(self, start_time_millis):
        """
        Sets the start_time_millis of this TaskRun.
        startTimeMillis


        :param start_time_millis: The start_time_millis of this TaskRun.
        :type: int
        """
        self._start_time_millis = start_time_millis

    @property
    def end_time_millis(self):
        """
        Gets the end_time_millis of this TaskRun.
        endTimeMillis


        :return: The end_time_millis of this TaskRun.
        :rtype: int
        """
        return self._end_time_millis

    @end_time_millis.setter
    def end_time_millis(self, end_time_millis):
        """
        Sets the end_time_millis of this TaskRun.
        endTimeMillis


        :param end_time_millis: The end_time_millis of this TaskRun.
        :type: int
        """
        self._end_time_millis = end_time_millis

    @property
    def last_updated(self):
        """
        Gets the last_updated of this TaskRun.
        lastUpdated


        :return: The last_updated of this TaskRun.
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """
        Sets the last_updated of this TaskRun.
        lastUpdated


        :param last_updated: The last_updated of this TaskRun.
        :type: int
        """
        self._last_updated = last_updated

    @property
    def records_written(self):
        """
        Gets the records_written of this TaskRun.
        Number of records processed in task run.


        :return: The records_written of this TaskRun.
        :rtype: int
        """
        return self._records_written

    @records_written.setter
    def records_written(self, records_written):
        """
        Sets the records_written of this TaskRun.
        Number of records processed in task run.


        :param records_written: The records_written of this TaskRun.
        :type: int
        """
        self._records_written = records_written

    @property
    def bytes_processed(self):
        """
        Gets the bytes_processed of this TaskRun.
        Number of bytes processed in task run.


        :return: The bytes_processed of this TaskRun.
        :rtype: int
        """
        return self._bytes_processed

    @bytes_processed.setter
    def bytes_processed(self, bytes_processed):
        """
        Sets the bytes_processed of this TaskRun.
        Number of bytes processed in task run.


        :param bytes_processed: The bytes_processed of this TaskRun.
        :type: int
        """
        self._bytes_processed = bytes_processed

    @property
    def error_message(self):
        """
        Gets the error_message of this TaskRun.
        Error message if status is ERROR


        :return: The error_message of this TaskRun.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this TaskRun.
        Error message if status is ERROR


        :param error_message: The error_message of this TaskRun.
        :type: str
        """
        self._error_message = error_message

    @property
    def opc_request_id(self):
        """
        Gets the opc_request_id of this TaskRun.
        Opc request id of execution of task run


        :return: The opc_request_id of this TaskRun.
        :rtype: str
        """
        return self._opc_request_id

    @opc_request_id.setter
    def opc_request_id(self, opc_request_id):
        """
        Sets the opc_request_id of this TaskRun.
        Opc request id of execution of task run


        :param opc_request_id: The opc_request_id of this TaskRun.
        :type: str
        """
        self._opc_request_id = opc_request_id

    @property
    def object_status(self):
        """
        Gets the object_status of this TaskRun.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this TaskRun.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this TaskRun.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this TaskRun.
        :type: int
        """
        self._object_status = object_status

    @property
    def task_type(self):
        """
        Gets the task_type of this TaskRun.
        The type of the task for the run.

        Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_type of this TaskRun.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """
        Sets the task_type of this TaskRun.
        The type of the task for the run.


        :param task_type: The task_type of this TaskRun.
        :type: str
        """
        allowed_values = ["INTEGRATION_TASK", "DATA_LOADER_TASK"]
        if not value_allowed_none_or_none_sentinel(task_type, allowed_values):
            task_type = 'UNKNOWN_ENUM_VALUE'
        self._task_type = task_type

    @property
    def identifier(self):
        """
        Gets the identifier of this TaskRun.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :return: The identifier of this TaskRun.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this TaskRun.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :param identifier: The identifier of this TaskRun.
        :type: str
        """
        self._identifier = identifier

    @property
    def metadata(self):
        """
        Gets the metadata of this TaskRun.

        :return: The metadata of this TaskRun.
        :rtype: ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this TaskRun.

        :param metadata: The metadata of this TaskRun.
        :type: ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this TaskRun.
        A map, if provided key is replaced with generated key, this structure provides mapping between user provided key and generated key


        :return: The key_map of this TaskRun.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this TaskRun.
        A map, if provided key is replaced with generated key, this structure provides mapping between user provided key and generated key


        :param key_map: The key_map of this TaskRun.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
