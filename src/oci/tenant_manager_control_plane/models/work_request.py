# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):
    """
    A description of the work request status.
    """

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_SENDER_INVITATION"
    OPERATION_TYPE_CREATE_SENDER_INVITATION = "CREATE_SENDER_INVITATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ACCEPT_RECIPIENT_INVITATION"
    OPERATION_TYPE_ACCEPT_RECIPIENT_INVITATION = "ACCEPT_RECIPIENT_INVITATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CANCEL_SENDER_INVITATION"
    OPERATION_TYPE_CANCEL_SENDER_INVITATION = "CANCEL_SENDER_INVITATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "COMPLETE_ORDER_ACTIVATION"
    OPERATION_TYPE_COMPLETE_ORDER_ACTIVATION = "COMPLETE_ORDER_ACTIVATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ACTIVATE_ORDER_EXISTING_TENANCY"
    OPERATION_TYPE_ACTIVATE_ORDER_EXISTING_TENANCY = "ACTIVATE_ORDER_EXISTING_TENANCY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "REGISTER_DOMAIN"
    OPERATION_TYPE_REGISTER_DOMAIN = "REGISTER_DOMAIN"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "RELEASE_DOMAIN"
    OPERATION_TYPE_RELEASE_DOMAIN = "RELEASE_DOMAIN"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "CREATE_CHILD_TENANCY"
    OPERATION_TYPE_CREATE_CHILD_TENANCY = "CREATE_CHILD_TENANCY"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "ASSIGN_DEFAULT_SUBSCRIPTION"
    OPERATION_TYPE_ASSIGN_DEFAULT_SUBSCRIPTION = "ASSIGN_DEFAULT_SUBSCRIPTION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "MANUAL_LINK_CREATION"
    OPERATION_TYPE_MANUAL_LINK_CREATION = "MANUAL_LINK_CREATION"

    #: A constant which can be used with the operation_type property of a WorkRequest.
    #: This constant has a value of "TERMINATE_ORGANIZATION_TENANCY"
    OPERATION_TYPE_TERMINATE_ORGANIZATION_TENANCY = "TERMINATE_ORGANIZATION_TENANCY"

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

        :param operation_type:
            The value to assign to the operation_type property of this WorkRequest.
            Allowed values for this property are: "CREATE_SENDER_INVITATION", "ACCEPT_RECIPIENT_INVITATION", "CANCEL_SENDER_INVITATION", "COMPLETE_ORDER_ACTIVATION", "ACTIVATE_ORDER_EXISTING_TENANCY", "REGISTER_DOMAIN", "RELEASE_DOMAIN", "CREATE_CHILD_TENANCY", "ASSIGN_DEFAULT_SUBSCRIPTION", "MANUAL_LINK_CREATION", "TERMINATE_ORGANIZATION_TENANCY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation_type: str

        :param status:
            The value to assign to the status property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
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
        :type resources: list[oci.tenant_manager_control_plane.models.WorkRequestResource]

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
        Type of the work request.

        Allowed values for this property are: "CREATE_SENDER_INVITATION", "ACCEPT_RECIPIENT_INVITATION", "CANCEL_SENDER_INVITATION", "COMPLETE_ORDER_ACTIVATION", "ACTIVATE_ORDER_EXISTING_TENANCY", "REGISTER_DOMAIN", "RELEASE_DOMAIN", "CREATE_CHILD_TENANCY", "ASSIGN_DEFAULT_SUBSCRIPTION", "MANUAL_LINK_CREATION", "TERMINATE_ORGANIZATION_TENANCY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation_type of this WorkRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """
        Sets the operation_type of this WorkRequest.
        Type of the work request.


        :param operation_type: The operation_type of this WorkRequest.
        :type: str
        """
        allowed_values = ["CREATE_SENDER_INVITATION", "ACCEPT_RECIPIENT_INVITATION", "CANCEL_SENDER_INVITATION", "COMPLETE_ORDER_ACTIVATION", "ACTIVATE_ORDER_EXISTING_TENANCY", "REGISTER_DOMAIN", "RELEASE_DOMAIN", "CREATE_CHILD_TENANCY", "ASSIGN_DEFAULT_SUBSCRIPTION", "MANUAL_LINK_CREATION", "TERMINATE_ORGANIZATION_TENANCY"]
        if not value_allowed_none_or_none_sentinel(operation_type, allowed_values):
            operation_type = 'UNKNOWN_ENUM_VALUE'
        self._operation_type = operation_type

    @property
    def status(self):
        """
        **[Required]** Gets the status of this WorkRequest.
        Status of the current work request.

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
        Status of the current work request.


        :param status: The status of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

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
        The OCID of the compartment that contains the work request.


        :return: The compartment_id of this WorkRequest.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WorkRequest.
        The OCID of the compartment that contains the work request.


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
        :rtype: list[oci.tenant_manager_control_plane.models.WorkRequestResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this WorkRequest.
        The resources affected by this work request.


        :param resources: The resources of this WorkRequest.
        :type: list[oci.tenant_manager_control_plane.models.WorkRequestResource]
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
        The date and time the request was created, as described in
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
        The date and time the request was created, as described in
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
        The date and time the request was started, as described in `RFC 3339`__,
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
        The date and time the request was started, as described in `RFC 3339`__,
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
        The date and time the object was finished, as described in `RFC 3339`__.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time the object was finished, as described in `RFC 3339`__.

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
