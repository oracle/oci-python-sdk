# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StorageWorkRequest(object):
    """
    Storage work request details.
    """

    #: A constant which can be used with the status property of a StorageWorkRequest.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a StorageWorkRequest.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a StorageWorkRequest.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a StorageWorkRequest.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a StorageWorkRequest.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the data_type property of a StorageWorkRequest.
    #: This constant has a value of "LOG"
    DATA_TYPE_LOG = "LOG"

    #: A constant which can be used with the data_type property of a StorageWorkRequest.
    #: This constant has a value of "LOOKUP"
    DATA_TYPE_LOOKUP = "LOOKUP"

    #: A constant which can be used with the operation_type property of a StorageWorkRequest.
    #: This constant has a value of "OFFBOARD_TENANCY"
    OPERATION_TYPE_OFFBOARD_TENANCY = "OFFBOARD_TENANCY"

    #: A constant which can be used with the operation_type property of a StorageWorkRequest.
    #: This constant has a value of "PURGE_STORAGE_DATA"
    OPERATION_TYPE_PURGE_STORAGE_DATA = "PURGE_STORAGE_DATA"

    #: A constant which can be used with the operation_type property of a StorageWorkRequest.
    #: This constant has a value of "RECALL_ARCHIVED_STORAGE_DATA"
    OPERATION_TYPE_RECALL_ARCHIVED_STORAGE_DATA = "RECALL_ARCHIVED_STORAGE_DATA"

    #: A constant which can be used with the operation_type property of a StorageWorkRequest.
    #: This constant has a value of "RELEASE_RECALLED_STORAGE_DATA"
    OPERATION_TYPE_RELEASE_RECALLED_STORAGE_DATA = "RELEASE_RECALLED_STORAGE_DATA"

    #: A constant which can be used with the operation_type property of a StorageWorkRequest.
    #: This constant has a value of "ARCHIVE_STORAGE_DATA"
    OPERATION_TYPE_ARCHIVE_STORAGE_DATA = "ARCHIVE_STORAGE_DATA"

    #: A constant which can be used with the operation_type property of a StorageWorkRequest.
    #: This constant has a value of "CLEANUP_ARCHIVAL_STORAGE_DATA"
    OPERATION_TYPE_CLEANUP_ARCHIVAL_STORAGE_DATA = "CLEANUP_ARCHIVAL_STORAGE_DATA"

    def __init__(self, **kwargs):
        """
        Initializes a new StorageWorkRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this StorageWorkRequest.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this StorageWorkRequest.
        :type compartment_id: str

        :param time_started:
            The value to assign to the time_started property of this StorageWorkRequest.
        :type time_started: datetime

        :param time_accepted:
            The value to assign to the time_accepted property of this StorageWorkRequest.
        :type time_accepted: datetime

        :param time_finished:
            The value to assign to the time_finished property of this StorageWorkRequest.
        :type time_finished: datetime

        :param time_expires:
            The value to assign to the time_expires property of this StorageWorkRequest.
        :type time_expires: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this StorageWorkRequest.
        :type percent_complete: int

        :param status:
            The value to assign to the status property of this StorageWorkRequest.
            Allowed values for this property are: "ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_data_started:
            The value to assign to the time_data_started property of this StorageWorkRequest.
        :type time_data_started: datetime

        :param time_data_ended:
            The value to assign to the time_data_ended property of this StorageWorkRequest.
        :type time_data_ended: datetime

        :param purge_query_string:
            The value to assign to the purge_query_string property of this StorageWorkRequest.
        :type purge_query_string: str

        :param data_type:
            The value to assign to the data_type property of this StorageWorkRequest.
            Allowed values for this property are: "LOG", "LOOKUP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        :param status_details:
            The value to assign to the status_details property of this StorageWorkRequest.
        :type status_details: str

        :param operation_details:
            The value to assign to the operation_details property of this StorageWorkRequest.
        :type operation_details: str

        :param policy_name:
            The value to assign to the policy_name property of this StorageWorkRequest.
        :type policy_name: str

        :param policy_id:
            The value to assign to the policy_id property of this StorageWorkRequest.
        :type policy_id: str

        :param storage_usage_in_bytes:
            The value to assign to the storage_usage_in_bytes property of this StorageWorkRequest.
        :type storage_usage_in_bytes: int

        :param compartment_id_in_subtree:
            The value to assign to the compartment_id_in_subtree property of this StorageWorkRequest.
        :type compartment_id_in_subtree: bool

        :param operation_type:
            The value to assign to the operation_type property of this StorageWorkRequest.
            Allowed values for this property are: "OFFBOARD_TENANCY", "PURGE_STORAGE_DATA", "RECALL_ARCHIVED_STORAGE_DATA", "RELEASE_RECALLED_STORAGE_DATA", "ARCHIVE_STORAGE_DATA", "CLEANUP_ARCHIVAL_STORAGE_DATA", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'time_started': 'datetime',
            'time_accepted': 'datetime',
            'time_finished': 'datetime',
            'time_expires': 'datetime',
            'percent_complete': 'int',
            'status': 'str',
            'time_data_started': 'datetime',
            'time_data_ended': 'datetime',
            'purge_query_string': 'str',
            'data_type': 'str',
            'status_details': 'str',
            'operation_details': 'str',
            'policy_name': 'str',
            'policy_id': 'str',
            'storage_usage_in_bytes': 'int',
            'compartment_id_in_subtree': 'bool',
            'operation_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'time_started': 'timeStarted',
            'time_accepted': 'timeAccepted',
            'time_finished': 'timeFinished',
            'time_expires': 'timeExpires',
            'percent_complete': 'percentComplete',
            'status': 'status',
            'time_data_started': 'timeDataStarted',
            'time_data_ended': 'timeDataEnded',
            'purge_query_string': 'purgeQueryString',
            'data_type': 'dataType',
            'status_details': 'statusDetails',
            'operation_details': 'operationDetails',
            'policy_name': 'policyName',
            'policy_id': 'policyId',
            'storage_usage_in_bytes': 'storageUsageInBytes',
            'compartment_id_in_subtree': 'compartmentIdInSubtree',
            'operation_type': 'operationType'
        }

        self._id = None
        self._compartment_id = None
        self._time_started = None
        self._time_accepted = None
        self._time_finished = None
        self._time_expires = None
        self._percent_complete = None
        self._status = None
        self._time_data_started = None
        self._time_data_ended = None
        self._purge_query_string = None
        self._data_type = None
        self._status_details = None
        self._operation_details = None
        self._policy_name = None
        self._policy_id = None
        self._storage_usage_in_bytes = None
        self._compartment_id_in_subtree = None
        self._operation_type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this StorageWorkRequest.
        Unique OCID identifier to reference this storage work Request with.


        :return: The id of this StorageWorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StorageWorkRequest.
        Unique OCID identifier to reference this storage work Request with.


        :param id: The id of this StorageWorkRequest.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this StorageWorkRequest.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this StorageWorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this StorageWorkRequest.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this StorageWorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_started(self):
        """
        Gets the time_started of this StorageWorkRequest.
        When the work request started.


        :return: The time_started of this StorageWorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this StorageWorkRequest.
        When the work request started.


        :param time_started: The time_started of this StorageWorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this StorageWorkRequest.
        When the work request was accepted. Should match timeStarted in all cases.


        :return: The time_accepted of this StorageWorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this StorageWorkRequest.
        When the work request was accepted. Should match timeStarted in all cases.


        :param time_accepted: The time_accepted of this StorageWorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_finished(self):
        """
        Gets the time_finished of this StorageWorkRequest.
        When the work request finished execution.


        :return: The time_finished of this StorageWorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this StorageWorkRequest.
        When the work request finished execution.


        :param time_finished: The time_finished of this StorageWorkRequest.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def time_expires(self):
        """
        Gets the time_expires of this StorageWorkRequest.
        When the work request will expire.


        :return: The time_expires of this StorageWorkRequest.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this StorageWorkRequest.
        When the work request will expire.


        :param time_expires: The time_expires of this StorageWorkRequest.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this StorageWorkRequest.
        Percentage progress completion of the work request.


        :return: The percent_complete of this StorageWorkRequest.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this StorageWorkRequest.
        Percentage progress completion of the work request.


        :param percent_complete: The percent_complete of this StorageWorkRequest.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def status(self):
        """
        **[Required]** Gets the status of this StorageWorkRequest.
        Work request status.

        Allowed values for this property are: "ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this StorageWorkRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StorageWorkRequest.
        Work request status.


        :param status: The status of this StorageWorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_data_started(self):
        """
        Gets the time_data_started of this StorageWorkRequest.
        the start of the time interval


        :return: The time_data_started of this StorageWorkRequest.
        :rtype: datetime
        """
        return self._time_data_started

    @time_data_started.setter
    def time_data_started(self, time_data_started):
        """
        Sets the time_data_started of this StorageWorkRequest.
        the start of the time interval


        :param time_data_started: The time_data_started of this StorageWorkRequest.
        :type: datetime
        """
        self._time_data_started = time_data_started

    @property
    def time_data_ended(self):
        """
        **[Required]** Gets the time_data_ended of this StorageWorkRequest.
        the end of the time interval


        :return: The time_data_ended of this StorageWorkRequest.
        :rtype: datetime
        """
        return self._time_data_ended

    @time_data_ended.setter
    def time_data_ended(self, time_data_ended):
        """
        Sets the time_data_ended of this StorageWorkRequest.
        the end of the time interval


        :param time_data_ended: The time_data_ended of this StorageWorkRequest.
        :type: datetime
        """
        self._time_data_ended = time_data_ended

    @property
    def purge_query_string(self):
        """
        Gets the purge_query_string of this StorageWorkRequest.
        the solr data filter query, '*' means all


        :return: The purge_query_string of this StorageWorkRequest.
        :rtype: str
        """
        return self._purge_query_string

    @purge_query_string.setter
    def purge_query_string(self, purge_query_string):
        """
        Sets the purge_query_string of this StorageWorkRequest.
        the solr data filter query, '*' means all


        :param purge_query_string: The purge_query_string of this StorageWorkRequest.
        :type: str
        """
        self._purge_query_string = purge_query_string

    @property
    def data_type(self):
        """
        **[Required]** Gets the data_type of this StorageWorkRequest.
        the type of the log data to be purged

        Allowed values for this property are: "LOG", "LOOKUP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this StorageWorkRequest.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this StorageWorkRequest.
        the type of the log data to be purged


        :param data_type: The data_type of this StorageWorkRequest.
        :type: str
        """
        allowed_values = ["LOG", "LOOKUP"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    @property
    def status_details(self):
        """
        Gets the status_details of this StorageWorkRequest.
        more detailed status if applicable


        :return: The status_details of this StorageWorkRequest.
        :rtype: str
        """
        return self._status_details

    @status_details.setter
    def status_details(self, status_details):
        """
        Sets the status_details of this StorageWorkRequest.
        more detailed status if applicable


        :param status_details: The status_details of this StorageWorkRequest.
        :type: str
        """
        self._status_details = status_details

    @property
    def operation_details(self):
        """
        Gets the operation_details of this StorageWorkRequest.
        more detailed info about this operation if applicable


        :return: The operation_details of this StorageWorkRequest.
        :rtype: str
        """
        return self._operation_details

    @operation_details.setter
    def operation_details(self, operation_details):
        """
        Sets the operation_details of this StorageWorkRequest.
        more detailed info about this operation if applicable


        :param operation_details: The operation_details of this StorageWorkRequest.
        :type: str
        """
        self._operation_details = operation_details

    @property
    def policy_name(self):
        """
        Gets the policy_name of this StorageWorkRequest.
        policy name if applicable (e.g. purge policy)


        :return: The policy_name of this StorageWorkRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """
        Sets the policy_name of this StorageWorkRequest.
        policy name if applicable (e.g. purge policy)


        :param policy_name: The policy_name of this StorageWorkRequest.
        :type: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        """
        Gets the policy_id of this StorageWorkRequest.
        purge policy ID


        :return: The policy_id of this StorageWorkRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """
        Sets the policy_id of this StorageWorkRequest.
        purge policy ID


        :param policy_id: The policy_id of this StorageWorkRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def storage_usage_in_bytes(self):
        """
        Gets the storage_usage_in_bytes of this StorageWorkRequest.
        storage usage in bytes if applicable


        :return: The storage_usage_in_bytes of this StorageWorkRequest.
        :rtype: int
        """
        return self._storage_usage_in_bytes

    @storage_usage_in_bytes.setter
    def storage_usage_in_bytes(self, storage_usage_in_bytes):
        """
        Sets the storage_usage_in_bytes of this StorageWorkRequest.
        storage usage in bytes if applicable


        :param storage_usage_in_bytes: The storage_usage_in_bytes of this StorageWorkRequest.
        :type: int
        """
        self._storage_usage_in_bytes = storage_usage_in_bytes

    @property
    def compartment_id_in_subtree(self):
        """
        Gets the compartment_id_in_subtree of this StorageWorkRequest.
        if true, purge child compartments data, only applicable to purge request


        :return: The compartment_id_in_subtree of this StorageWorkRequest.
        :rtype: bool
        """
        return self._compartment_id_in_subtree

    @compartment_id_in_subtree.setter
    def compartment_id_in_subtree(self, compartment_id_in_subtree):
        """
        Sets the compartment_id_in_subtree of this StorageWorkRequest.
        if true, purge child compartments data, only applicable to purge request


        :param compartment_id_in_subtree: The compartment_id_in_subtree of this StorageWorkRequest.
        :type: bool
        """
        self._compartment_id_in_subtree = compartment_id_in_subtree

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this StorageWorkRequest.
        Asynchronous storage request name.

        Allowed values for this property are: "OFFBOARD_TENANCY", "PURGE_STORAGE_DATA", "RECALL_ARCHIVED_STORAGE_DATA", "RELEASE_RECALLED_STORAGE_DATA", "ARCHIVE_STORAGE_DATA", "CLEANUP_ARCHIVAL_STORAGE_DATA", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this StorageWorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this StorageWorkRequest.
        Asynchronous storage request name.


        :param operation_type: The operation_type of this StorageWorkRequest.
        :type: str
        """
        allowed_values = ["OFFBOARD_TENANCY", "PURGE_STORAGE_DATA", "RECALL_ARCHIVED_STORAGE_DATA", "RELEASE_RECALLED_STORAGE_DATA", "ARCHIVE_STORAGE_DATA", "CLEANUP_ARCHIVAL_STORAGE_DATA"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
