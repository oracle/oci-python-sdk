# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UploadFileSummary(object):
    """
    Details of Upload File.
    """

    #: A constant which can be used with the status property of a UploadFileSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a UploadFileSummary.
    #: This constant has a value of "SUCCESSFUL"
    STATUS_SUCCESSFUL = "SUCCESSFUL"

    #: A constant which can be used with the status property of a UploadFileSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new UploadFileSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference:
            The value to assign to the reference property of this UploadFileSummary.
        :type reference: str

        :param name:
            The value to assign to the name property of this UploadFileSummary.
        :type name: str

        :param status:
            The value to assign to the status property of this UploadFileSummary.
            Allowed values for this property are: "IN_PROGRESS", "SUCCESSFUL", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param total_chunks:
            The value to assign to the total_chunks property of this UploadFileSummary.
        :type total_chunks: float

        :param chunks_consumed:
            The value to assign to the chunks_consumed property of this UploadFileSummary.
        :type chunks_consumed: float

        :param chunks_success:
            The value to assign to the chunks_success property of this UploadFileSummary.
        :type chunks_success: float

        :param chunks_fail:
            The value to assign to the chunks_fail property of this UploadFileSummary.
        :type chunks_fail: float

        :param time_started:
            The value to assign to the time_started property of this UploadFileSummary.
        :type time_started: datetime

        :param source_name:
            The value to assign to the source_name property of this UploadFileSummary.
        :type source_name: str

        :param entity_type:
            The value to assign to the entity_type property of this UploadFileSummary.
        :type entity_type: str

        :param entity_name:
            The value to assign to the entity_name property of this UploadFileSummary.
        :type entity_name: str

        :param log_namespace:
            The value to assign to the log_namespace property of this UploadFileSummary.
        :type log_namespace: str

        :param log_group_id:
            The value to assign to the log_group_id property of this UploadFileSummary.
        :type log_group_id: str

        :param log_group_name:
            The value to assign to the log_group_name property of this UploadFileSummary.
        :type log_group_name: str

        :param failure_details:
            The value to assign to the failure_details property of this UploadFileSummary.
        :type failure_details: str

        """
        self.swagger_types = {
            'reference': 'str',
            'name': 'str',
            'status': 'str',
            'total_chunks': 'float',
            'chunks_consumed': 'float',
            'chunks_success': 'float',
            'chunks_fail': 'float',
            'time_started': 'datetime',
            'source_name': 'str',
            'entity_type': 'str',
            'entity_name': 'str',
            'log_namespace': 'str',
            'log_group_id': 'str',
            'log_group_name': 'str',
            'failure_details': 'str'
        }

        self.attribute_map = {
            'reference': 'reference',
            'name': 'name',
            'status': 'status',
            'total_chunks': 'totalChunks',
            'chunks_consumed': 'chunksConsumed',
            'chunks_success': 'chunksSuccess',
            'chunks_fail': 'chunksFail',
            'time_started': 'timeStarted',
            'source_name': 'sourceName',
            'entity_type': 'entityType',
            'entity_name': 'entityName',
            'log_namespace': 'logNamespace',
            'log_group_id': 'logGroupId',
            'log_group_name': 'logGroupName',
            'failure_details': 'failureDetails'
        }

        self._reference = None
        self._name = None
        self._status = None
        self._total_chunks = None
        self._chunks_consumed = None
        self._chunks_success = None
        self._chunks_fail = None
        self._time_started = None
        self._source_name = None
        self._entity_type = None
        self._entity_name = None
        self._log_namespace = None
        self._log_group_id = None
        self._log_group_name = None
        self._failure_details = None

    @property
    def reference(self):
        """
        **[Required]** Gets the reference of this UploadFileSummary.
        Unique internal identifier to refer upload file.


        :return: The reference of this UploadFileSummary.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this UploadFileSummary.
        Unique internal identifier to refer upload file.


        :param reference: The reference of this UploadFileSummary.
        :type: str
        """
        self._reference = reference

    @property
    def name(self):
        """
        **[Required]** Gets the name of this UploadFileSummary.
        Name of the file


        :return: The name of this UploadFileSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UploadFileSummary.
        Name of the file


        :param name: The name of this UploadFileSummary.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """
        Gets the status of this UploadFileSummary.
        Processing status of the file.

        Allowed values for this property are: "IN_PROGRESS", "SUCCESSFUL", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this UploadFileSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UploadFileSummary.
        Processing status of the file.


        :param status: The status of this UploadFileSummary.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SUCCESSFUL", "FAILED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def total_chunks(self):
        """
        Gets the total_chunks of this UploadFileSummary.
        Number of estimated chunks for this file. A chunk is a portion of the log file used for the processing.


        :return: The total_chunks of this UploadFileSummary.
        :rtype: float
        """
        return self._total_chunks

    @total_chunks.setter
    def total_chunks(self, total_chunks):
        """
        Sets the total_chunks of this UploadFileSummary.
        Number of estimated chunks for this file. A chunk is a portion of the log file used for the processing.


        :param total_chunks: The total_chunks of this UploadFileSummary.
        :type: float
        """
        self._total_chunks = total_chunks

    @property
    def chunks_consumed(self):
        """
        Gets the chunks_consumed of this UploadFileSummary.
        Number of chunks processed.


        :return: The chunks_consumed of this UploadFileSummary.
        :rtype: float
        """
        return self._chunks_consumed

    @chunks_consumed.setter
    def chunks_consumed(self, chunks_consumed):
        """
        Sets the chunks_consumed of this UploadFileSummary.
        Number of chunks processed.


        :param chunks_consumed: The chunks_consumed of this UploadFileSummary.
        :type: float
        """
        self._chunks_consumed = chunks_consumed

    @property
    def chunks_success(self):
        """
        Gets the chunks_success of this UploadFileSummary.
        Number of chunks processed successfully.


        :return: The chunks_success of this UploadFileSummary.
        :rtype: float
        """
        return self._chunks_success

    @chunks_success.setter
    def chunks_success(self, chunks_success):
        """
        Sets the chunks_success of this UploadFileSummary.
        Number of chunks processed successfully.


        :param chunks_success: The chunks_success of this UploadFileSummary.
        :type: float
        """
        self._chunks_success = chunks_success

    @property
    def chunks_fail(self):
        """
        Gets the chunks_fail of this UploadFileSummary.
        Number of chunks failed processing.


        :return: The chunks_fail of this UploadFileSummary.
        :rtype: float
        """
        return self._chunks_fail

    @chunks_fail.setter
    def chunks_fail(self, chunks_fail):
        """
        Sets the chunks_fail of this UploadFileSummary.
        Number of chunks failed processing.


        :param chunks_fail: The chunks_fail of this UploadFileSummary.
        :type: float
        """
        self._chunks_fail = chunks_fail

    @property
    def time_started(self):
        """
        Gets the time_started of this UploadFileSummary.
        The time when this file processing started.


        :return: The time_started of this UploadFileSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this UploadFileSummary.
        The time when this file processing started.


        :param time_started: The time_started of this UploadFileSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def source_name(self):
        """
        Gets the source_name of this UploadFileSummary.
        Name of the log source used for processing this file.


        :return: The source_name of this UploadFileSummary.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this UploadFileSummary.
        Name of the log source used for processing this file.


        :param source_name: The source_name of this UploadFileSummary.
        :type: str
        """
        self._source_name = source_name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this UploadFileSummary.
        Name of the entity type.


        :return: The entity_type of this UploadFileSummary.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this UploadFileSummary.
        Name of the entity type.


        :param entity_type: The entity_type of this UploadFileSummary.
        :type: str
        """
        self._entity_type = entity_type

    @property
    def entity_name(self):
        """
        Gets the entity_name of this UploadFileSummary.
        Name of the entity associated with the file.


        :return: The entity_name of this UploadFileSummary.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this UploadFileSummary.
        Name of the entity associated with the file.


        :param entity_name: The entity_name of this UploadFileSummary.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def log_namespace(self):
        """
        Gets the log_namespace of this UploadFileSummary.
        (Deprecated) Name of the log namespace associated with the file.


        :return: The log_namespace of this UploadFileSummary.
        :rtype: str
        """
        return self._log_namespace

    @log_namespace.setter
    def log_namespace(self, log_namespace):
        """
        Sets the log_namespace of this UploadFileSummary.
        (Deprecated) Name of the log namespace associated with the file.


        :param log_namespace: The log_namespace of this UploadFileSummary.
        :type: str
        """
        self._log_namespace = log_namespace

    @property
    def log_group_id(self):
        """
        Gets the log_group_id of this UploadFileSummary.
        Log group OCID associated with the file.


        :return: The log_group_id of this UploadFileSummary.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this UploadFileSummary.
        Log group OCID associated with the file.


        :param log_group_id: The log_group_id of this UploadFileSummary.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        """
        Gets the log_group_name of this UploadFileSummary.
        Name of the log group associated with the file.


        :return: The log_group_name of this UploadFileSummary.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """
        Sets the log_group_name of this UploadFileSummary.
        Name of the log group associated with the file.


        :param log_group_name: The log_group_name of this UploadFileSummary.
        :type: str
        """
        self._log_group_name = log_group_name

    @property
    def failure_details(self):
        """
        Gets the failure_details of this UploadFileSummary.
        The details about upload processing failure.


        :return: The failure_details of this UploadFileSummary.
        :rtype: str
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details):
        """
        Sets the failure_details of this UploadFileSummary.
        The details about upload processing failure.


        :param failure_details: The failure_details of this UploadFileSummary.
        :type: str
        """
        self._failure_details = failure_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
