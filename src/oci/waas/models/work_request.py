# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    Many of the API requests you use to create and configure WAAS policies do not take effect immediately. In these cases, the request spawns an asynchronous work flow to fulfill the request. `WorkRequest` objects provide visibility for in-progress work flows. For more information about work requests, see `Viewing the State of a Work Request`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/viewingworkrequest.htm
    """

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_WAAS_POLICY"
    OPERATION_TYPE_CREATE_WAAS_POLICY = "CREATE_WAAS_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_WAAS_POLICY"
    OPERATION_TYPE_UPDATE_WAAS_POLICY = "UPDATE_WAAS_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_WAAS_POLICY"
    OPERATION_TYPE_DELETE_WAAS_POLICY = "DELETE_WAAS_POLICY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_HTTP_REDIRECT"
    OPERATION_TYPE_CREATE_HTTP_REDIRECT = "CREATE_HTTP_REDIRECT"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_HTTP_REDIRECT"
    OPERATION_TYPE_UPDATE_HTTP_REDIRECT = "UPDATE_HTTP_REDIRECT"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_HTTP_REDIRECT"
    OPERATION_TYPE_DELETE_HTTP_REDIRECT = "DELETE_HTTP_REDIRECT"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "PURGE_WAAS_POLICY_CACHE"
    OPERATION_TYPE_PURGE_WAAS_POLICY_CACHE = "PURGE_WAAS_POLICY_CACHE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_CUSTOM_PROTECTION_RULE"
    OPERATION_TYPE_CREATE_CUSTOM_PROTECTION_RULE = "CREATE_CUSTOM_PROTECTION_RULE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_CUSTOM_PROTECTION_RULE"
    OPERATION_TYPE_UPDATE_CUSTOM_PROTECTION_RULE = "UPDATE_CUSTOM_PROTECTION_RULE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_CUSTOM_PROTECTION_RULE"
    OPERATION_TYPE_DELETE_CUSTOM_PROTECTION_RULE = "DELETE_CUSTOM_PROTECTION_RULE"

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

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequest.
            Allowed values for this property are: "CREATE_WAAS_POLICY", "UPDATE_WAAS_POLICY", "DELETE_WAAS_POLICY", "CREATE_HTTP_REDIRECT", "UPDATE_HTTP_REDIRECT", "DELETE_HTTP_REDIRECT", "PURGE_WAAS_POLICY_CACHE", "CREATE_CUSTOM_PROTECTION_RULE", "UPDATE_CUSTOM_PROTECTION_RULE", "DELETE_CUSTOM_PROTECTION_RULE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequest.
        :type compartment_id: str

        :param resources:
            The value to assign to the resources property of this WorkRequest.
        :type resources: list[oci.waas.models.WorkRequestResource]

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequest.
        :type percent_complete: int

        :param logs:
            The value to assign to the logs property of this WorkRequest.
        :type logs: list[oci.waas.models.WorkRequestLogEntry]

        :param errors:
            The value to assign to the errors property of this WorkRequest.
        :type errors: list[oci.waas.models.WorkRequestError]

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
            'operation_type': 'str',
            'status': 'str',
            'compartment_id': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'int',
            'logs': 'list[WorkRequestLogEntry]',
            'errors': 'list[WorkRequestError]',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'operation_type': 'operationType',
            'status': 'status',
            'compartment_id': 'compartmentId',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'logs': 'logs',
            'errors': 'errors',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._id = None
        self._operation_type = None
        self._status = None
        self._compartment_id = None
        self._resources = None
        self._percent_complete = None
        self._logs = None
        self._errors = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequest.
        The `OCID`__ of the work request.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this WorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequest.
        The `OCID`__ of the work request.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this WorkRequest.
        :type: str
        """
        self._id = id

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequest.
        A description of the operation requested by the work request.

        Allowed values for this property are: "CREATE_WAAS_POLICY", "UPDATE_WAAS_POLICY", "DELETE_WAAS_POLICY", "CREATE_HTTP_REDIRECT", "UPDATE_HTTP_REDIRECT", "DELETE_HTTP_REDIRECT", "PURGE_WAAS_POLICY_CACHE", "CREATE_CUSTOM_PROTECTION_RULE", "UPDATE_CUSTOM_PROTECTION_RULE", "DELETE_CUSTOM_PROTECTION_RULE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequest.
        A description of the operation requested by the work request.


        :param operation_type: The operation_type of this WorkRequest.
        :type: str
        """
        allowed_values = ["CREATE_WAAS_POLICY", "UPDATE_WAAS_POLICY", "DELETE_WAAS_POLICY", "CREATE_HTTP_REDIRECT", "UPDATE_HTTP_REDIRECT", "DELETE_HTTP_REDIRECT", "PURGE_WAAS_POLICY_CACHE", "CREATE_CUSTOM_PROTECTION_RULE", "UPDATE_CUSTOM_PROTECTION_RULE", "DELETE_CUSTOM_PROTECTION_RULE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequest.
        The current status of the work request.

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
        The current status of the work request.


        :param status: The status of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequest.
        The `OCID`__ of the compartment that contains the work request.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The `OCID`__ of the compartment that contains the work request.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        Gets the resources of this WorkRequest.
        The resources being used to complete the work request operation.


        :return: The resources of this WorkRequest.
        :rtype: list[oci.waas.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequest.
        The resources being used to complete the work request operation.


        :param resources: The resources of this WorkRequest.
        :type: list[oci.waas.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this WorkRequest.
        The percentage of work completed by the work request.


        :return: The percent_complete of this WorkRequest.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequest.
        The percentage of work completed by the work request.


        :param percent_complete: The percent_complete of this WorkRequest.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def logs(self):
        """
        Gets the logs of this WorkRequest.
        The list of log entries from the work request workflow.


        :return: The logs of this WorkRequest.
        :rtype: list[oci.waas.models.WorkRequestLogEntry]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """
        Sets the logs of this WorkRequest.
        The list of log entries from the work request workflow.


        :param logs: The logs of this WorkRequest.
        :type: list[oci.waas.models.WorkRequestLogEntry]
        """
        self._logs = logs

    @property
    def errors(self):
        """
        Gets the errors of this WorkRequest.
        The list of errors that occurred while fulfilling the work request.


        :return: The errors of this WorkRequest.
        :rtype: list[oci.waas.models.WorkRequestError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this WorkRequest.
        The list of errors that occurred while fulfilling the work request.


        :param errors: The errors of this WorkRequest.
        :type: list[oci.waas.models.WorkRequestError]
        """
        self._errors = errors

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequest.
        The date and time the work request was created, in the format defined by RFC3339.


        :return: The time_accepted of this WorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequest.
        The date and time the work request was created, in the format defined by RFC3339.


        :param time_accepted: The time_accepted of this WorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this WorkRequest.
        The date and time the work request moved from the `ACCEPTED` state to the `IN_PROGRESS` state, expressed in RFC 3339 timestamp format.


        :return: The time_started of this WorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequest.
        The date and time the work request moved from the `ACCEPTED` state to the `IN_PROGRESS` state, expressed in RFC 3339 timestamp format.


        :param time_started: The time_started of this WorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        **[Required]** Gets the time_finished of this WorkRequest.
        The date and time the work request was fulfilled or terminated, expressed in RFC 3339 timestamp format.


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time the work request was fulfilled or terminated, expressed in RFC 3339 timestamp format.


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
