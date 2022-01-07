# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestSummary(object):
    """
    High level summary of control plane job work request.
    """

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "CANCELED"
    STATUS_CANCELED = "CANCELED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequestSummary.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WorkRequestSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WorkRequestSummary.
        :type compartment_id: str

        :param time_started:
            The value to assign to the time_started property of this WorkRequestSummary.
        :type time_started: datetime

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequestSummary.
        :type time_accepted: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequestSummary.
        :type time_finished: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this WorkRequestSummary.
        :type percent_complete: int

        :param status:
            The value to assign to the status property of this WorkRequestSummary.
            Allowed values for this property are: "ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'time_started': 'datetime',
            'time_accepted': 'datetime',
            'time_finished': 'datetime',
            'percent_complete': 'int',
            'status': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'time_started': 'timeStarted',
            'time_accepted': 'timeAccepted',
            'time_finished': 'timeFinished',
            'percent_complete': 'percentComplete',
            'status': 'status'
        }

        self._id = None
        self._compartment_id = None
        self._time_started = None
        self._time_accepted = None
        self._time_finished = None
        self._percent_complete = None
        self._status = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequestSummary.
        Unique OCID identifier to reference this query job work Request.


        :return: The id of this WorkRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequestSummary.
        Unique OCID identifier to reference this query job work Request.


        :param id: The id of this WorkRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this WorkRequestSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WorkRequestSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequestSummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WorkRequestSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this WorkRequestSummary.
        When the work request started.


        :return: The time_started of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequestSummary.
        When the work request started.


        :param time_started: The time_started of this WorkRequestSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_accepted(self):
        """
        Gets the time_accepted of this WorkRequestSummary.
        When the work request was accepted. Should match timeStarted in all cases.


        :return: The time_accepted of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequestSummary.
        When the work request was accepted. Should match timeStarted in all cases.


        :param time_accepted: The time_accepted of this WorkRequestSummary.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequestSummary.
        When the work request finished execution.


        :return: The time_finished of this WorkRequestSummary.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequestSummary.
        When the work request finished execution.


        :param time_finished: The time_finished of this WorkRequestSummary.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this WorkRequestSummary.
        Percentage progress completion of the query.


        :return: The percent_complete of this WorkRequestSummary.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this WorkRequestSummary.
        Percentage progress completion of the query.


        :param percent_complete: The percent_complete of this WorkRequestSummary.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def status(self):
        """
        Gets the status of this WorkRequestSummary.
        Work request status.

        Allowed values for this property are: "ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequestSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequestSummary.
        Work request status.


        :param status: The status of this WorkRequestSummary.
        :type: str
        """
        allowed_values = ["ACCEPTED", "CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
