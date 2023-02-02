# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    The API operations that create and configure GoldenGate resources do not take effect
    immediately. In these cases, the operation spawns an asynchronous workflow to fulfill the
    request. Work requests provide visibility into the status of these in-progress, long-running
    asynchronous workflows.
    """

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DATABASE_REGISTRATION_CREATE"
    OPERATION_TYPE_GOLDENGATE_DATABASE_REGISTRATION_CREATE = "GOLDENGATE_DATABASE_REGISTRATION_CREATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DATABASE_REGISTRATION_UPDATE"
    OPERATION_TYPE_GOLDENGATE_DATABASE_REGISTRATION_UPDATE = "GOLDENGATE_DATABASE_REGISTRATION_UPDATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DATABASE_REGISTRATION_DELETE"
    OPERATION_TYPE_GOLDENGATE_DATABASE_REGISTRATION_DELETE = "GOLDENGATE_DATABASE_REGISTRATION_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DATABASE_REGISTRATION_MOVE"
    OPERATION_TYPE_GOLDENGATE_DATABASE_REGISTRATION_MOVE = "GOLDENGATE_DATABASE_REGISTRATION_MOVE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_CREATE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_CREATE = "GOLDENGATE_DEPLOYMENT_CREATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_UPDATE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_UPDATE = "GOLDENGATE_DEPLOYMENT_UPDATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_DELETE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_DELETE = "GOLDENGATE_DEPLOYMENT_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_MOVE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_MOVE = "GOLDENGATE_DEPLOYMENT_MOVE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_RESTORE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_RESTORE = "GOLDENGATE_DEPLOYMENT_RESTORE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_START"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_START = "GOLDENGATE_DEPLOYMENT_START"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_STOP"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_STOP = "GOLDENGATE_DEPLOYMENT_STOP"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_UPGRADE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_UPGRADE = "GOLDENGATE_DEPLOYMENT_UPGRADE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_BACKUP_CREATE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_BACKUP_CREATE = "GOLDENGATE_DEPLOYMENT_BACKUP_CREATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_BACKUP_DELETE"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_BACKUP_DELETE = "GOLDENGATE_DEPLOYMENT_BACKUP_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_BACKUP_CANCEL"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_BACKUP_CANCEL = "GOLDENGATE_DEPLOYMENT_BACKUP_CANCEL"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_CONNECTION_CREATE"
    OPERATION_TYPE_GOLDENGATE_CONNECTION_CREATE = "GOLDENGATE_CONNECTION_CREATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_CONNECTION_UPDATE"
    OPERATION_TYPE_GOLDENGATE_CONNECTION_UPDATE = "GOLDENGATE_CONNECTION_UPDATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_CONNECTION_DELETE"
    OPERATION_TYPE_GOLDENGATE_CONNECTION_DELETE = "GOLDENGATE_CONNECTION_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_CONNECTION_MOVE"
    OPERATION_TYPE_GOLDENGATE_CONNECTION_MOVE = "GOLDENGATE_CONNECTION_MOVE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_CONNECTION_ASSIGNMENT_CREATE"
    OPERATION_TYPE_GOLDENGATE_CONNECTION_ASSIGNMENT_CREATE = "GOLDENGATE_CONNECTION_ASSIGNMENT_CREATE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_CONNECTION_ASSIGMNENT_DELETE"
    OPERATION_TYPE_GOLDENGATE_CONNECTION_ASSIGMNENT_DELETE = "GOLDENGATE_CONNECTION_ASSIGMNENT_DELETE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_DIAGNOSTIC_COLLECT"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_DIAGNOSTIC_COLLECT = "GOLDENGATE_DEPLOYMENT_DIAGNOSTIC_COLLECT"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_WALLET_EXPORT"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_WALLET_EXPORT = "GOLDENGATE_DEPLOYMENT_WALLET_EXPORT"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_WALLET_IMPORT"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_WALLET_IMPORT = "GOLDENGATE_DEPLOYMENT_WALLET_IMPORT"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "GOLDENGATE_DEPLOYMENT_PATCH"
    OPERATION_TYPE_GOLDENGATE_DEPLOYMENT_PATCH = "GOLDENGATE_DEPLOYMENT_PATCH"

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
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequest.
            Allowed values for this property are: "GOLDENGATE_DATABASE_REGISTRATION_CREATE", "GOLDENGATE_DATABASE_REGISTRATION_UPDATE", "GOLDENGATE_DATABASE_REGISTRATION_DELETE", "GOLDENGATE_DATABASE_REGISTRATION_MOVE", "GOLDENGATE_DEPLOYMENT_CREATE", "GOLDENGATE_DEPLOYMENT_UPDATE", "GOLDENGATE_DEPLOYMENT_DELETE", "GOLDENGATE_DEPLOYMENT_MOVE", "GOLDENGATE_DEPLOYMENT_RESTORE", "GOLDENGATE_DEPLOYMENT_START", "GOLDENGATE_DEPLOYMENT_STOP", "GOLDENGATE_DEPLOYMENT_UPGRADE", "GOLDENGATE_DEPLOYMENT_BACKUP_CREATE", "GOLDENGATE_DEPLOYMENT_BACKUP_DELETE", "GOLDENGATE_DEPLOYMENT_BACKUP_CANCEL", "GOLDENGATE_CONNECTION_CREATE", "GOLDENGATE_CONNECTION_UPDATE", "GOLDENGATE_CONNECTION_DELETE", "GOLDENGATE_CONNECTION_MOVE", "GOLDENGATE_CONNECTION_ASSIGNMENT_CREATE", "GOLDENGATE_CONNECTION_ASSIGMNENT_DELETE", "GOLDENGATE_DEPLOYMENT_DIAGNOSTIC_COLLECT", "GOLDENGATE_DEPLOYMENT_WALLET_EXPORT", "GOLDENGATE_DEPLOYMENT_WALLET_IMPORT", "GOLDENGATE_DEPLOYMENT_PATCH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param id:
            The value to assign to the id property of this WorkRequest.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequest.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequest.
        :type resources: list[oci.golden_gate.models.WorkRequestResource]

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
            'operation_type': 'str',
            'status': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'operation_type': 'operationType',
            'status': 'status',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._operation_type = None
        self._status = None
        self._id = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequest.
        The work request's operation type.

        Allowed values for this property are: "GOLDENGATE_DATABASE_REGISTRATION_CREATE", "GOLDENGATE_DATABASE_REGISTRATION_UPDATE", "GOLDENGATE_DATABASE_REGISTRATION_DELETE", "GOLDENGATE_DATABASE_REGISTRATION_MOVE", "GOLDENGATE_DEPLOYMENT_CREATE", "GOLDENGATE_DEPLOYMENT_UPDATE", "GOLDENGATE_DEPLOYMENT_DELETE", "GOLDENGATE_DEPLOYMENT_MOVE", "GOLDENGATE_DEPLOYMENT_RESTORE", "GOLDENGATE_DEPLOYMENT_START", "GOLDENGATE_DEPLOYMENT_STOP", "GOLDENGATE_DEPLOYMENT_UPGRADE", "GOLDENGATE_DEPLOYMENT_BACKUP_CREATE", "GOLDENGATE_DEPLOYMENT_BACKUP_DELETE", "GOLDENGATE_DEPLOYMENT_BACKUP_CANCEL", "GOLDENGATE_CONNECTION_CREATE", "GOLDENGATE_CONNECTION_UPDATE", "GOLDENGATE_CONNECTION_DELETE", "GOLDENGATE_CONNECTION_MOVE", "GOLDENGATE_CONNECTION_ASSIGNMENT_CREATE", "GOLDENGATE_CONNECTION_ASSIGMNENT_DELETE", "GOLDENGATE_DEPLOYMENT_DIAGNOSTIC_COLLECT", "GOLDENGATE_DEPLOYMENT_WALLET_EXPORT", "GOLDENGATE_DEPLOYMENT_WALLET_IMPORT", "GOLDENGATE_DEPLOYMENT_PATCH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequest.
        The work request's operation type.


        :param operation_type: The operation_type of this WorkRequest.
        :type: str
        """
        allowed_values = ["GOLDENGATE_DATABASE_REGISTRATION_CREATE", "GOLDENGATE_DATABASE_REGISTRATION_UPDATE", "GOLDENGATE_DATABASE_REGISTRATION_DELETE", "GOLDENGATE_DATABASE_REGISTRATION_MOVE", "GOLDENGATE_DEPLOYMENT_CREATE", "GOLDENGATE_DEPLOYMENT_UPDATE", "GOLDENGATE_DEPLOYMENT_DELETE", "GOLDENGATE_DEPLOYMENT_MOVE", "GOLDENGATE_DEPLOYMENT_RESTORE", "GOLDENGATE_DEPLOYMENT_START", "GOLDENGATE_DEPLOYMENT_STOP", "GOLDENGATE_DEPLOYMENT_UPGRADE", "GOLDENGATE_DEPLOYMENT_BACKUP_CREATE", "GOLDENGATE_DEPLOYMENT_BACKUP_DELETE", "GOLDENGATE_DEPLOYMENT_BACKUP_CANCEL", "GOLDENGATE_CONNECTION_CREATE", "GOLDENGATE_CONNECTION_UPDATE", "GOLDENGATE_CONNECTION_DELETE", "GOLDENGATE_CONNECTION_MOVE", "GOLDENGATE_CONNECTION_ASSIGNMENT_CREATE", "GOLDENGATE_CONNECTION_ASSIGMNENT_DELETE", "GOLDENGATE_DEPLOYMENT_DIAGNOSTIC_COLLECT", "GOLDENGATE_DEPLOYMENT_WALLET_EXPORT", "GOLDENGATE_DEPLOYMENT_WALLET_IMPORT", "GOLDENGATE_DEPLOYMENT_PATCH"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequest.
        Status of current work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequest.
        Status of current work request.


        :param status: The status of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequest.
        The id of the work request.


        :return: The id of this WorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequest.
        The id of the work request.


        :param id: The id of this WorkRequest.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequest.
        The ocid of the compartment that contains the work request. Work requests should be scoped
        to the same compartment as the resource the work request affects. If the work request
        affects multiple resources, and those resources are not in the same compartment, it is up
        to the service team to pick the primary resource whose compartment should be used.


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The ocid of the compartment that contains the work request. Work requests should be scoped
        to the same compartment as the resource the work request affects. If the work request
        affects multiple resources, and those resources are not in the same compartment, it is up
        to the service team to pick the primary resource whose compartment should be used.


        :param compartment_id: The compartment_id of this WorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequest.
        The resources affected by this work request.


        :return: The resources of this WorkRequest.
        :rtype: list[oci.golden_gate.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequest.
        The resources affected by this work request.


        :param resources: The resources of this WorkRequest.
        :type: list[oci.golden_gate.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequest.
        Percentage of the request completed.


        :return: The percent_complete of this WorkRequest.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequest.
        Percentage of the request completed.


        :param percent_complete: The percent_complete of this WorkRequest.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequest.
        The date and time the request was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_accepted of this WorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequest.
        The date and time the request was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_accepted: The time_accepted of this WorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequest.
        The date and time the request was started. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this WorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequest.
        The date and time the request was started. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this WorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequest.
        The date and time the request was finished. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time the request was finished. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


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
