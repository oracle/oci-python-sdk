# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    The description of work request, including its status.
    """

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "CREATE_ODA_INSTANCE"
    REQUEST_ACTION_CREATE_ODA_INSTANCE = "CREATE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "UPGRADE_ODA_INSTANCE"
    REQUEST_ACTION_UPGRADE_ODA_INSTANCE = "UPGRADE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "DELETE_ODA_INSTANCE"
    REQUEST_ACTION_DELETE_ODA_INSTANCE = "DELETE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "PURGE_ODA_INSTANCE"
    REQUEST_ACTION_PURGE_ODA_INSTANCE = "PURGE_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "RECOVER_ODA_INSTANCE"
    REQUEST_ACTION_RECOVER_ODA_INSTANCE = "RECOVER_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "STOP_ODA_INSTANCE"
    REQUEST_ACTION_STOP_ODA_INSTANCE = "STOP_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "START_ODA_INSTANCE"
    REQUEST_ACTION_START_ODA_INSTANCE = "START_ODA_INSTANCE"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "CHANGE_ODA_INSTANCE_COMPARTMENT"
    REQUEST_ACTION_CHANGE_ODA_INSTANCE_COMPARTMENT = "CHANGE_ODA_INSTANCE_COMPARTMENT"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "CREATE_ASSOCIATION"
    REQUEST_ACTION_CREATE_ASSOCIATION = "CREATE_ASSOCIATION"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "DELETE_ASSOCIATION"
    REQUEST_ACTION_DELETE_ASSOCIATION = "DELETE_ASSOCIATION"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "UPDATE_ENTITLEMENTS_FOR_CACCT"
    REQUEST_ACTION_UPDATE_ENTITLEMENTS_FOR_CACCT = "UPDATE_ENTITLEMENTS_FOR_CACCT"

    #: A constant which can be used with the request_action property of a WorkRequest.
    #: This constant has a value of "LOOKUP_ODA_INSTANCES_FOR_CACCT"
    REQUEST_ACTION_LOOKUP_ODA_INSTANCES_FOR_CACCT = "LOOKUP_ODA_INSTANCES_FOR_CACCT"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "ACCEPTED"
    STATUS_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a WorkRequest.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

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

        :param oda_instance_id:
            The value to assign to the oda_instance_id property of this WorkRequest.
        :type oda_instance_id: str

        :param request_action:
            The value to assign to the request_action property of this WorkRequest.
            Allowed values for this property are: "CREATE_ODA_INSTANCE", "UPGRADE_ODA_INSTANCE", "DELETE_ODA_INSTANCE", "PURGE_ODA_INSTANCE", "RECOVER_ODA_INSTANCE", "STOP_ODA_INSTANCE", "START_ODA_INSTANCE", "CHANGE_ODA_INSTANCE_COMPARTMENT", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", "LOOKUP_ODA_INSTANCES_FOR_CACCT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type request_action: str

        :param status:
            The value to assign to the status property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param status_message:
            The value to assign to the status_message property of this WorkRequest.
        :type status_message: str

        :param resources:
            The value to assign to the resources property of this WorkRequest.
        :type resources: list[oci.oda.models.WorkRequestResource]

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
            'oda_instance_id': 'str',
            'request_action': 'str',
            'status': 'str',
            'status_message': 'str',
            'resources': 'list[WorkRequestResource]',
            'percent_complete': 'float',
            'time_accepted': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'oda_instance_id': 'odaInstanceId',
            'request_action': 'requestAction',
            'status': 'status',
            'status_message': 'statusMessage',
            'resources': 'resources',
            'percent_complete': 'percentComplete',
            'time_accepted': 'timeAccepted',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._id = None
        self._compartment_id = None
        self._oda_instance_id = None
        self._request_action = None
        self._status = None
        self._status_message = None
        self._resources = None
        self._percent_complete = None
        self._time_accepted = None
        self._time_started = None
        self._time_finished = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequest.
        The identifier of the work request.


        :return: The id of this WorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequest.
        The identifier of the work request.


        :param id: The id of this WorkRequest.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WorkRequest.
        The identifier of the compartment that contains the work request.


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The identifier of the compartment that contains the work request.


        :param compartment_id: The compartment_id of this WorkRequest.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def oda_instance_id(self):
        """
        **[Required]** Gets the oda_instance_id of this WorkRequest.
        The identifier of the Digital Assistant instance to which this work request pertains.


        :return: The oda_instance_id of this WorkRequest.
        :rtype: str
        """
        return self._oda_instance_id

    @oda_instance_id.setter
    def oda_instance_id(self, oda_instance_id):
        """
        Sets the oda_instance_id of this WorkRequest.
        The identifier of the Digital Assistant instance to which this work request pertains.


        :param oda_instance_id: The oda_instance_id of this WorkRequest.
        :type: str
        """
        self._oda_instance_id = oda_instance_id

    @property
    def request_action(self):
        """
        **[Required]** Gets the request_action of this WorkRequest.
        The type of the operation that's associated with the work request.

        Allowed values for this property are: "CREATE_ODA_INSTANCE", "UPGRADE_ODA_INSTANCE", "DELETE_ODA_INSTANCE", "PURGE_ODA_INSTANCE", "RECOVER_ODA_INSTANCE", "STOP_ODA_INSTANCE", "START_ODA_INSTANCE", "CHANGE_ODA_INSTANCE_COMPARTMENT", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", "LOOKUP_ODA_INSTANCES_FOR_CACCT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The request_action of this WorkRequest.
        :rtype: str
        """
        return self._request_action

    @request_action.setter
    def request_action(self, request_action):
        """
        Sets the request_action of this WorkRequest.
        The type of the operation that's associated with the work request.


        :param request_action: The request_action of this WorkRequest.
        :type: str
        """
        allowed_values = ["CREATE_ODA_INSTANCE", "UPGRADE_ODA_INSTANCE", "DELETE_ODA_INSTANCE", "PURGE_ODA_INSTANCE", "RECOVER_ODA_INSTANCE", "STOP_ODA_INSTANCE", "START_ODA_INSTANCE", "CHANGE_ODA_INSTANCE_COMPARTMENT", "CREATE_ASSOCIATION", "DELETE_ASSOCIATION", "UPDATE_ENTITLEMENTS_FOR_CACCT", "LOOKUP_ODA_INSTANCES_FOR_CACCT"]
        if not value_allowed_none_or_none_sentinel(request_action, allowed_values):
            request_action = 'UNKNOWN_ENUM_VALUE'
        self._request_action = request_action

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequest.
        The status of current work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this WorkRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkRequest.
        The status of current work request.


        :param status: The status of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def status_message(self):
        """
        Gets the status_message of this WorkRequest.
        A short message that provides more detail about the current status.
        For example, if a work request fails, then this may include information
        about why it failed.


        :return: The status_message of this WorkRequest.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this WorkRequest.
        A short message that provides more detail about the current status.
        For example, if a work request fails, then this may include information
        about why it failed.


        :param status_message: The status_message of this WorkRequest.
        :type: str
        """
        self._status_message = status_message

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this WorkRequest.
        The resources that this work request affects.


        :return: The resources of this WorkRequest.
        :rtype: list[oci.oda.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequest.
        The resources that this work request affects.


        :param resources: The resources of this WorkRequest.
        :type: list[oci.oda.models.WorkRequestResource]
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
        The date and time that the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_accepted of this WorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequest.
        The date and time that the request was created, as described in
        `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_accepted: The time_accepted of this WorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_started(self):
        """
        Gets the time_started of this WorkRequest.
        The date and time that the request was started, as described in `RFC 3339`__, CKQ
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_started of this WorkRequest.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this WorkRequest.
        The date and time that the request was started, as described in `RFC 3339`__, CKQ
        section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_started: The time_started of this WorkRequest.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequest.
        The date and time that the object finished, as described in `RFC 3339`__. CKQ

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time that the object finished, as described in `RFC 3339`__. CKQ

        __ https://tools.ietf.org/rfc/rfc3339


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
