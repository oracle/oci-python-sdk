# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    An asynchronous work request. See `Work Requests`__.

    __ https://docs.cloud.oracle.com/Content/General/Concepts/workrequestoverview.htm
    """

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_FLEET"
    OPERATION_TYPE_CREATE_FLEET = "CREATE_FLEET"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_FLEET"
    OPERATION_TYPE_DELETE_FLEET = "DELETE_FLEET"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "MOVE_FLEET"
    OPERATION_TYPE_MOVE_FLEET = "MOVE_FLEET"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_FLEET"
    OPERATION_TYPE_UPDATE_FLEET = "UPDATE_FLEET"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "UPDATE_FLEET_AGENT_CONFIGURATION"
    OPERATION_TYPE_UPDATE_FLEET_AGENT_CONFIGURATION = "UPDATE_FLEET_AGENT_CONFIGURATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "DELETE_JAVA_INSTALLATION"
    OPERATION_TYPE_DELETE_JAVA_INSTALLATION = "DELETE_JAVA_INSTALLATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_JAVA_INSTALLATION"
    OPERATION_TYPE_CREATE_JAVA_INSTALLATION = "CREATE_JAVA_INSTALLATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "COLLECT_JFR"
    OPERATION_TYPE_COLLECT_JFR = "COLLECT_JFR"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "REQUEST_CRYPTO_EVENT_ANALYSIS"
    OPERATION_TYPE_REQUEST_CRYPTO_EVENT_ANALYSIS = "REQUEST_CRYPTO_EVENT_ANALYSIS"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "SCAN_JAVA_SERVER_USAGE"
    OPERATION_TYPE_SCAN_JAVA_SERVER_USAGE = "SCAN_JAVA_SERVER_USAGE"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "SCAN_LIBRARY_USAGE"
    OPERATION_TYPE_SCAN_LIBRARY_USAGE = "SCAN_LIBRARY_USAGE"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequest.
            Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
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
        :type resources: list[oci.jms.models.WorkRequestResource]

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

        :param created_by:
            The value to assign to the created_by property of this WorkRequest.
        :type created_by: oci.jms.models.Principal

        :param time_last_updated:
            The value to assign to the time_last_updated property of this WorkRequest.
        :type time_last_updated: datetime

        :param total_task_count:
            The value to assign to the total_task_count property of this WorkRequest.
        :type total_task_count: int

        :param completed_task_count:
            The value to assign to the completed_task_count property of this WorkRequest.
        :type completed_task_count: int

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
            'time_finished': 'datetime',
            'created_by': 'Principal',
            'time_last_updated': 'datetime',
            'total_task_count': 'int',
            'completed_task_count': 'int'
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
            'time_finished': 'timeFinished',
            'created_by': 'createdBy',
            'time_last_updated': 'timeLastUpdated',
            'total_task_count': 'totalTaskCount',
            'completed_task_count': 'completedTaskCount'
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
        self._created_by = None
        self._time_last_updated = None
        self._total_task_count = None
        self._completed_task_count = None

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this WorkRequest.
        The asynchronous operation tracked by this work request.

        Allowed values for this property are: "CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequest.
        The asynchronous operation tracked by this work request.


        :param operation_type: The operation_type of this WorkRequest.
        :type: str
        """
        allowed_values = ["CREATE_FLEET", "DELETE_FLEET", "MOVE_FLEET", "UPDATE_FLEET", "UPDATE_FLEET_AGENT_CONFIGURATION", "DELETE_JAVA_INSTALLATION", "CREATE_JAVA_INSTALLATION", "COLLECT_JFR", "REQUEST_CRYPTO_EVENT_ANALYSIS", "SCAN_JAVA_SERVER_USAGE", "SCAN_LIBRARY_USAGE"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequest.
        The status of the work request.

        Allowed values for this property are: "ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequest.
        The status of the work request.


        :param status: The status of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "CANCELED", "CANCELING", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

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
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequest.
        The `OCID`__ of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The `OCID`__ of the compartment that contains the work request. Work requests should be scoped to
        the same compartment as the resource the work request affects. If the work request affects multiple resources,
        and those resources are not in the same compartment, it is up to the service team to pick the primary
        resource whose compartment should be used.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequest.
        The resources that are affected by this work request.


        :return: The resources of this WorkRequest.
        :rtype: list[oci.jms.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequest.
        The resources that are affected by this work request.


        :param resources: The resources of this WorkRequest.
        :type: list[oci.jms.models.WorkRequestResource]
        """
        self._resources = resources

    @property
    def percent_complete(self):
        """
        **[Required]** Gets the percent_complete of this WorkRequest.
        The percentage complete of the operation tracked by this work request.


        :return: The percent_complete of this WorkRequest.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequest.
        The percentage complete of the operation tracked by this work request.


        :param percent_complete: The percent_complete of this WorkRequest.
        :type: float
        """
        self._percent_complete = percent_complete

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequest.
        The date and time the request was created (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_accepted of this WorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequest.
        The date and time the request was created (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_accepted: The time_accepted of this WorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequest.
        The date and time the work request transitioned from _ACCEPTED_ to _IN_PROGRESS_ (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_started of this WorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequest.
        The date and time the work request transitioned from _ACCEPTED_ to _IN_PROGRESS_ (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_started: The time_started of this WorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequest.
        The date and time the work request reached a terminal state, either _FAILED_ or _SUCCEEDED_ (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time the work request reached a terminal state, either _FAILED_ or _SUCCEEDED_ (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_finished: The time_finished of this WorkRequest.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def created_by(self):
        """
        Gets the created_by of this WorkRequest.

        :return: The created_by of this WorkRequest.
        :rtype: oci.jms.models.Principal
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this WorkRequest.

        :param created_by: The created_by of this WorkRequest.
        :type: oci.jms.models.Principal
        """
        self._created_by = created_by

    @property
    def time_last_updated(self):
        """
        Gets the time_last_updated of this WorkRequest.
        The date and time the work request percentage was last updated. (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_last_updated of this WorkRequest.
        :rtype: datetime
        """
        return self._time_last_updated

    @time_last_updated.setter
    def time_last_updated(self, time_last_updated):
        """
        Sets the time_last_updated of this WorkRequest.
        The date and time the work request percentage was last updated. (formatted according to `RFC3339`__).

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_last_updated: The time_last_updated of this WorkRequest.
        :type: datetime
        """
        self._time_last_updated = time_last_updated

    @property
    def total_task_count(self):
        """
        Gets the total_task_count of this WorkRequest.
        The total number of tasks to be executed for this work request.


        :return: The total_task_count of this WorkRequest.
        :rtype: int
        """
        return self._total_task_count

    @total_task_count.setter
    def total_task_count(self, total_task_count):
        """
        Sets the total_task_count of this WorkRequest.
        The total number of tasks to be executed for this work request.


        :param total_task_count: The total_task_count of this WorkRequest.
        :type: int
        """
        self._total_task_count = total_task_count

    @property
    def completed_task_count(self):
        """
        Gets the completed_task_count of this WorkRequest.
        The number of tasks had been executed to a terminal state.


        :return: The completed_task_count of this WorkRequest.
        :rtype: int
        """
        return self._completed_task_count

    @completed_task_count.setter
    def completed_task_count(self, completed_task_count):
        """
        Sets the completed_task_count of this WorkRequest.
        The number of tasks had been executed to a terminal state.


        :param completed_task_count: The completed_task_count of this WorkRequest.
        :type: int
        """
        self._completed_task_count = completed_task_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
