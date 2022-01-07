# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryWorkRequestSummary(object):
    """
    High level summary of query job work request.
    """

    #: A constant which can be used with the mode property of a QueryWorkRequestSummary.
    #: This constant has a value of "FOREGROUND"
    MODE_FOREGROUND = "FOREGROUND"

    #: A constant which can be used with the mode property of a QueryWorkRequestSummary.
    #: This constant has a value of "BACKGROUND"
    MODE_BACKGROUND = "BACKGROUND"

    #: A constant which can be used with the status property of a QueryWorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a QueryWorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a QueryWorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a QueryWorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a QueryWorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the operation_type property of a QueryWorkRequestSummary.
    #: This constant has a value of "EXECUTE_QUERY_JOB"
    OPERATION_TYPE_EXECUTE_QUERY_JOB = "EXECUTE_QUERY_JOB"

    #: A constant which can be used with the operation_type property of a QueryWorkRequestSummary.
    #: This constant has a value of "EXECUTE_PURGE_JOB"
    OPERATION_TYPE_EXECUTE_PURGE_JOB = "EXECUTE_PURGE_JOB"

    def __init__(self, **kwargs):
        """
        Initializes a new QueryWorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this QueryWorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this QueryWorkRequestSummary.
        :type compartment_id: str

        :param time_started:
            The value to assign to the time_started property of this QueryWorkRequestSummary.
        :type time_started: datetime

        :param time_accepted:
            The value to assign to the time_accepted property of this QueryWorkRequestSummary.
        :type time_accepted: datetime

        :param time_finished:
            The value to assign to the time_finished property of this QueryWorkRequestSummary.
        :type time_finished: datetime

        :param time_expires:
            The value to assign to the time_expires property of this QueryWorkRequestSummary.
        :type time_expires: datetime

        :param mode:
            The value to assign to the mode property of this QueryWorkRequestSummary.
            Allowed values for this property are: "FOREGROUND", "BACKGROUND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        :param percent_complete:
            The value to assign to the percent_complete property of this QueryWorkRequestSummary.
        :type percent_complete: int

        :param status:
            The value to assign to the status property of this QueryWorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param operation_type:
            The value to assign to the operation_type property of this QueryWorkRequestSummary.
            Allowed values for this property are: "EXECUTE_QUERY_JOB", "EXECUTE_PURGE_JOB", 'UNKNOWN_ENUM_VALUE'.
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
            'mode': 'str',
            'percent_complete': 'int',
            'status': 'str',
            'operation_type': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'time_started': 'timeStarted',
            'time_accepted': 'timeAccepted',
            'time_finished': 'timeFinished',
            'time_expires': 'timeExpires',
            'mode': 'mode',
            'percent_complete': 'percentComplete',
            'status': 'status',
            'operation_type': 'operationType'
        }

        self._id = None
        self._compartment_id = None
        self._time_started = None
        self._time_accepted = None
        self._time_finished = None
        self._time_expires = None
        self._mode = None
        self._percent_complete = None
        self._status = None
        self._operation_type = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this QueryWorkRequestSummary.
        Unique OCID identifier to reference this query job work Request with.


        :return: The id of this QueryWorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueryWorkRequestSummary.
        Unique OCID identifier to reference this query job work Request with.


        :param id: The id of this QueryWorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this QueryWorkRequestSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this QueryWorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this QueryWorkRequestSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this QueryWorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this QueryWorkRequestSummary.
        When the work request started.


        :return: The time_started of this QueryWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this QueryWorkRequestSummary.
        When the work request started.


        :param time_started: The time_started of this QueryWorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this QueryWorkRequestSummary.
        When the work request was accepted. Should match timeStarted in all cases.


        :return: The time_accepted of this QueryWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this QueryWorkRequestSummary.
        When the work request was accepted. Should match timeStarted in all cases.


        :param time_accepted: The time_accepted of this QueryWorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_finished(self):
        """
        Gets the time_finished of this QueryWorkRequestSummary.
        When the work request finished execution.


        :return: The time_finished of this QueryWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this QueryWorkRequestSummary.
        When the work request finished execution.


        :param time_finished: The time_finished of this QueryWorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def time_expires(self):
        """
        Gets the time_expires of this QueryWorkRequestSummary.
        When the work request will expire.


        :return: The time_expires of this QueryWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this QueryWorkRequestSummary.
        When the work request will expire.


        :param time_expires: The time_expires of this QueryWorkRequestSummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def mode(self):
        """
        **[Required]** Gets the mode of this QueryWorkRequestSummary.
        Current execution mode for the job.

        Allowed values for this property are: "FOREGROUND", "BACKGROUND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mode of this QueryWorkRequestSummary.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this QueryWorkRequestSummary.
        Current execution mode for the job.


        :param mode: The mode of this QueryWorkRequestSummary.
        :type: str
        """
        allowed_values = ["FOREGROUND", "BACKGROUND"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            mode = 'UNKNOWN_ENUM_VALUE'
        self._mode = mode

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this QueryWorkRequestSummary.
        Percentage progress completion of the query.


        :return: The percent_complete of this QueryWorkRequestSummary.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this QueryWorkRequestSummary.
        Percentage progress completion of the query.


        :param percent_complete: The percent_complete of this QueryWorkRequestSummary.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def status(self):
        """
        Gets the status of this QueryWorkRequestSummary.
        Work request status.

        Allowed values for this property are: "ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this QueryWorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this QueryWorkRequestSummary.
        Work request status.


        :param status: The status of this QueryWorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def operation_type(self):
        """
        Gets the operation_type of this QueryWorkRequestSummary.
        Asynchronous action name.

        Allowed values for this property are: "EXECUTE_QUERY_JOB", "EXECUTE_PURGE_JOB", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this QueryWorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this QueryWorkRequestSummary.
        Asynchronous action name.


        :param operation_type: The operation_type of this QueryWorkRequestSummary.
        :type: str
        """
        allowed_values = ["EXECUTE_QUERY_JOB", "EXECUTE_PURGE_JOB"]
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
