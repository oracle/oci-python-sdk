# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaggingWorkRequestSummary(object):
    """
    The work request summary. Tracks the status of the asynchronous operation.
    """

    #: A constant which can be used with the operation_type property of a TaggingWorkRequestSummary.
    #: This constant has a value of "DELETE_TAG_DEFINITION"
    OPERATION_TYPE_DELETE_TAG_DEFINITION = "DELETE_TAG_DEFINITION"

    #: A constant which can be used with the status property of a TaggingWorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a TaggingWorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a TaggingWorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a TaggingWorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a TaggingWorkRequestSummary.
    #: This constant has a value of "CANCELING"
    STATUS_CANCELING = "CANCELING"

    #: A constant which can be used with the status property of a TaggingWorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new TaggingWorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TaggingWorkRequestSummary.
        :type id: str

        :param operation_type:
            The value to assign to the operation_type property of this TaggingWorkRequestSummary.
            Allowed values for this property are: "DELETE_TAG_DEFINITION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TaggingWorkRequestSummary.
        :type compartment_id: str

        :param status:
            The value to assign to the status property of this TaggingWorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param resources:
            The value to assign to the resources property of this TaggingWorkRequestSummary.
        :type resources: list[WorkRequestResource]

        :param time_accepted:
            The value to assign to the time_accepted property of this TaggingWorkRequestSummary.
        :type time_accepted: datetime

        :param time_started:
            The value to assign to the time_started property of this TaggingWorkRequestSummary.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this TaggingWorkRequestSummary.
        :type time_finished: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this TaggingWorkRequestSummary.
        :type percent_complete: float

        """
        self.swagger_types = {
            'id': 'str',
            'operation_type': 'str',
            'compartment_id': 'str',
            'status': 'str',
            'resources': 'list[WorkRequestResource]',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'percent_complete': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'operation_type': 'operationType',
            'compartment_id': 'compartmentId',
            'status': 'status',
            'resources': 'resources',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'percent_complete': 'percentComplete'
        }

        self._id = None
        self._operation_type = None
        self._compartment_id = None
        self._status = None
        self._resources = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None
        self._percent_complete = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TaggingWorkRequestSummary.
        The OCID of the work request.


        :return: The id of this TaggingWorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TaggingWorkRequestSummary.
        The OCID of the work request.


        :param id: The id of this TaggingWorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def operation_type(self):
        """
        **[Required]** Gets the operation_type of this TaggingWorkRequestSummary.
        An enum-like description of the type of work the work request is doing.

        Allowed values for this property are: "DELETE_TAG_DEFINITION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this TaggingWorkRequestSummary.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this TaggingWorkRequestSummary.
        An enum-like description of the type of work the work request is doing.


        :param operation_type: The operation_type of this TaggingWorkRequestSummary.
        :type: str
        """
        allowed_values = ["DELETE_TAG_DEFINITION"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this TaggingWorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :return: The compartment_id of this TaggingWorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TaggingWorkRequestSummary.
        The OCID of the compartment that contains the work request.


        :param compartment_id: The compartment_id of this TaggingWorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this TaggingWorkRequestSummary.
        The current status of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this TaggingWorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this TaggingWorkRequestSummary.
        The current status of the work request.


        :param status: The status of this TaggingWorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def resources(self):
        """
        Gets the resources of this TaggingWorkRequestSummary.
        The resources this work request affects.


        :return: The resources of this TaggingWorkRequestSummary.
        :rtype: list[WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this TaggingWorkRequestSummary.
        The resources this work request affects.


        :param resources: The resources of this TaggingWorkRequestSummary.
        :type: list[WorkRequestResource]
        """
        self._resources = resources

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this TaggingWorkRequestSummary.
        Date and time the work was accepted, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_accepted of this TaggingWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this TaggingWorkRequestSummary.
        Date and time the work was accepted, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_accepted: The time_accepted of this TaggingWorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this TaggingWorkRequestSummary.
        Date and time the work started, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_started of this TaggingWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this TaggingWorkRequestSummary.
        Date and time the work started, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_started: The time_started of this TaggingWorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this TaggingWorkRequestSummary.
        Date and time the work completed, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_finished of this TaggingWorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this TaggingWorkRequestSummary.
        Date and time the work completed, in the format defined by RFC3339.
        Example: `2016-08-25T21:10:29.600Z`


        :param time_finished: The time_finished of this TaggingWorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this TaggingWorkRequestSummary.
        How much progress the operation has made.


        :return: The percent_complete of this TaggingWorkRequestSummary.
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this TaggingWorkRequestSummary.
        How much progress the operation has made.


        :param percent_complete: The percent_complete of this TaggingWorkRequestSummary.
        :type: float
        """
        self._percent_complete = percent_complete

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
