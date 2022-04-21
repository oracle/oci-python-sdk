# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    Description of the work request status.
    """

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_BDS"
    OPERATION_TYPE_CREATE_BDS = "CREATE_BDS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_BDS"
    OPERATION_TYPE_UPDATE_BDS = "UPDATE_BDS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_BDS"
    OPERATION_TYPE_DELETE_BDS = "DELETE_BDS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ADD_BLOCK_STORAGE"
    OPERATION_TYPE_ADD_BLOCK_STORAGE = "ADD_BLOCK_STORAGE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ADD_WORKER_NODES"
    OPERATION_TYPE_ADD_WORKER_NODES = "ADD_WORKER_NODES"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ADD_CLOUD_SQL"
    OPERATION_TYPE_ADD_CLOUD_SQL = "ADD_CLOUD_SQL"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "REMOVE_CLOUD_SQL"
    OPERATION_TYPE_REMOVE_CLOUD_SQL = "REMOVE_CLOUD_SQL"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CHANGE_COMPARTMENT_FOR_BDS"
    OPERATION_TYPE_CHANGE_COMPARTMENT_FOR_BDS = "CHANGE_COMPARTMENT_FOR_BDS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CHANGE_SHAPE"
    OPERATION_TYPE_CHANGE_SHAPE = "CHANGE_SHAPE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_INFRA"
    OPERATION_TYPE_UPDATE_INFRA = "UPDATE_INFRA"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "RESTART_NODE"
    OPERATION_TYPE_RESTART_NODE = "RESTART_NODE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "REMOVE_NODE"
    OPERATION_TYPE_REMOVE_NODE = "REMOVE_NODE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_AUTOSCALE_CONFIG"
    OPERATION_TYPE_CREATE_AUTOSCALE_CONFIG = "CREATE_AUTOSCALE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_AUTOSCALE_CONFIG"
    OPERATION_TYPE_UPDATE_AUTOSCALE_CONFIG = "UPDATE_AUTOSCALE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_AUTOSCALE_CONFIG"
    OPERATION_TYPE_DELETE_AUTOSCALE_CONFIG = "DELETE_AUTOSCALE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "AUTOSCALE_CONFIG"
    OPERATION_TYPE_AUTOSCALE_CONFIG = "AUTOSCALE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "AUTOSCALE_RUN"
    OPERATION_TYPE_AUTOSCALE_RUN = "AUTOSCALE_RUN"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_API_KEY"
    OPERATION_TYPE_CREATE_API_KEY = "CREATE_API_KEY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_API_KEY"
    OPERATION_TYPE_DELETE_API_KEY = "DELETE_API_KEY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "TEST_OBJECT_STORE_CONNECTION"
    OPERATION_TYPE_TEST_OBJECT_STORE_CONNECTION = "TEST_OBJECT_STORE_CONNECTION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_METASTORE_CONFIG"
    OPERATION_TYPE_CREATE_METASTORE_CONFIG = "CREATE_METASTORE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_METASTORE_CONFIG"
    OPERATION_TYPE_DELETE_METASTORE_CONFIG = "DELETE_METASTORE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_METASTORE_CONFIG"
    OPERATION_TYPE_UPDATE_METASTORE_CONFIG = "UPDATE_METASTORE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ACTIVATE_METASTORE_CONFIG"
    OPERATION_TYPE_ACTIVATE_METASTORE_CONFIG = "ACTIVATE_METASTORE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "TEST_METASTORE_CONFIG"
    OPERATION_TYPE_TEST_METASTORE_CONFIG = "TEST_METASTORE_CONFIG"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "PATCH_BDS"
    OPERATION_TYPE_PATCH_BDS = "PATCH_BDS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "PATCH_ODH"
    OPERATION_TYPE_PATCH_ODH = "PATCH_ODH"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequest.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequest.
        :type compartment_id: str

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequest.
            Allowed values for this property are: "CREATE_BDS", "UPDATE_BDS", "DELETE_BDS", "ADD_BLOCK_STORAGE", "ADD_WORKER_NODES", "ADD_CLOUD_SQL", "REMOVE_CLOUD_SQL", "CHANGE_COMPARTMENT_FOR_BDS", "CHANGE_SHAPE", "UPDATE_INFRA", "RESTART_NODE", "REMOVE_NODE", "CREATE_AUTOSCALE_CONFIG", "UPDATE_AUTOSCALE_CONFIG", "DELETE_AUTOSCALE_CONFIG", "AUTOSCALE_CONFIG", "AUTOSCALE_RUN", "CREATE_API_KEY", "DELETE_API_KEY", "TEST_OBJECT_STORE_CONNECTION", "CREATE_METASTORE_CONFIG", "DELETE_METASTORE_CONFIG", "UPDATE_METASTORE_CONFIG", "ACTIVATE_METASTORE_CONFIG", "TEST_METASTORE_CONFIG", "PATCH_BDS", "PATCH_ODH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param resources:
            The value to assign to the resources property of this WorkRequest.
        :type resources: list[oci.bds.models.WorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequest.
        :type percent_complete: float

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequest.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this WorkRequest.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequest.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'operation_type': 'str',
            'status': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'operation_type': 'operationType',
            'status': 'status',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._id = None
        self._compartment_id = None
        self._operation_type = None
        self._status = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequest.
        The ID of the work request.


        :return: The id of this WorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequest.
        The ID of the work request.


        :param id: The id of this WorkRequest.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequest.
        The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The OCID of the compartment that contains the work request. Work requests should be scoped to the same compartment as the resource the work request affects. If the work request affects multiple resources, and those resources are not in the same compartment, it is up to the service team to pick the primary resource whose compartment should be used.


        :param compartment_id: The compartment_id of this WorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequest.
        The type of this work request.

        Allowed values for this property are: "CREATE_BDS", "UPDATE_BDS", "DELETE_BDS", "ADD_BLOCK_STORAGE", "ADD_WORKER_NODES", "ADD_CLOUD_SQL", "REMOVE_CLOUD_SQL", "CHANGE_COMPARTMENT_FOR_BDS", "CHANGE_SHAPE", "UPDATE_INFRA", "RESTART_NODE", "REMOVE_NODE", "CREATE_AUTOSCALE_CONFIG", "UPDATE_AUTOSCALE_CONFIG", "DELETE_AUTOSCALE_CONFIG", "AUTOSCALE_CONFIG", "AUTOSCALE_RUN", "CREATE_API_KEY", "DELETE_API_KEY", "TEST_OBJECT_STORE_CONNECTION", "CREATE_METASTORE_CONFIG", "DELETE_METASTORE_CONFIG", "UPDATE_METASTORE_CONFIG", "ACTIVATE_METASTORE_CONFIG", "TEST_METASTORE_CONFIG", "PATCH_BDS", "PATCH_ODH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequest.
        The type of this work request.


        :param operation_type: The operation_type of this WorkRequest.
        :type: str
        """
        allowed_values = ["CREATE_BDS", "UPDATE_BDS", "DELETE_BDS", "ADD_BLOCK_STORAGE", "ADD_WORKER_NODES", "ADD_CLOUD_SQL", "REMOVE_CLOUD_SQL", "CHANGE_COMPARTMENT_FOR_BDS", "CHANGE_SHAPE", "UPDATE_INFRA", "RESTART_NODE", "REMOVE_NODE", "CREATE_AUTOSCALE_CONFIG", "UPDATE_AUTOSCALE_CONFIG", "DELETE_AUTOSCALE_CONFIG", "AUTOSCALE_CONFIG", "AUTOSCALE_RUN", "CREATE_API_KEY", "DELETE_API_KEY", "TEST_OBJECT_STORE_CONNECTION", "CREATE_METASTORE_CONFIG", "DELETE_METASTORE_CONFIG", "UPDATE_METASTORE_CONFIG", "ACTIVATE_METASTORE_CONFIG", "TEST_METASTORE_CONFIG", "PATCH_BDS", "PATCH_ODH"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequest.
        The status of this work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequest.
        The status of this work request.


        :param status: The status of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequest.
        The resources affected by this work request.


        :return: The resources of this WorkRequest.
        :rtype: list[oci.bds.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequest.
        The resources affected by this work request.


        :param resources: The resources of this WorkRequest.
        :type: list[oci.bds.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequest.
        Percentage of this work request completed.


        :return: The percent_complete of this WorkRequest.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequest.
        Percentage of this work request completed.


        :param percent_complete: The percent_complete of this WorkRequest.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequest.
        The date and time the request was created, shown as an RFC 3339 formatted datetime string.


        :return: The time_accepted of this WorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequest.
        The date and time the request was created, shown as an RFC 3339 formatted datetime string.


        :param time_accepted: The time_accepted of this WorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequest.
        The time the request was started, shown as an RFC 3339 formatted datetime string.


        :return: The time_started of this WorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequest.
        The time the request was started, shown as an RFC 3339 formatted datetime string.


        :param time_started: The time_started of this WorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequest.
        The time the object was finished, shown as an RFC 3339 formatted datetime string.


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The time the object was finished, shown as an RFC 3339 formatted datetime string.


        :param time_finished: The time_finished of this WorkRequest.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
