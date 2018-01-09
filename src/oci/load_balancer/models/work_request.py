# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequest(object):

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequest object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param error_details:
            The value to assign to the error_details property of this WorkRequest.
        :type error_details: list[WorkRequestError]

        :param id:
            The value to assign to the id property of this WorkRequest.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WorkRequest.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param load_balancer_id:
            The value to assign to the load_balancer_id property of this WorkRequest.
        :type load_balancer_id: str

        :param message:
            The value to assign to the message property of this WorkRequest.
        :type message: str

        :param time_accepted:
            The value to assign to the time_accepted property of this WorkRequest.
        :type time_accepted: datetime

        :param time_finished:
            The value to assign to the time_finished property of this WorkRequest.
        :type time_finished: datetime

        :param type:
            The value to assign to the type property of this WorkRequest.
        :type type: str

        """
        self.swagger_types = {
            'error_details': 'list[WorkRequestError]',
            'id': 'str',
            'lifecycle_state': 'str',
            'load_balancer_id': 'str',
            'message': 'str',
            'time_accepted': 'datetime',
            'time_finished': 'datetime',
            'type': 'str'
        }

        self.attribute_map = {
            'error_details': 'errorDetails',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'load_balancer_id': 'loadBalancerId',
            'message': 'message',
            'time_accepted': 'timeAccepted',
            'time_finished': 'timeFinished',
            'type': 'type'
        }

        self._error_details = None
        self._id = None
        self._lifecycle_state = None
        self._load_balancer_id = None
        self._message = None
        self._time_accepted = None
        self._time_finished = None
        self._type = None

    @property
    def error_details(self):
        """
        **[Required]** Gets the error_details of this WorkRequest.

        :return: The error_details of this WorkRequest.
        :rtype: list[WorkRequestError]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this WorkRequest.

        :param error_details: The error_details of this WorkRequest.
        :type: list[WorkRequestError]
        """
        self._error_details = error_details

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WorkRequest.
        The `OCID`__ of the work request.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this WorkRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkRequest.
        The `OCID`__ of the work request.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this WorkRequest.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this WorkRequest.
        The current state of the work request.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WorkRequest.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WorkRequest.
        The current state of the work request.


        :param lifecycle_state: The lifecycle_state of this WorkRequest.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def load_balancer_id(self):
        """
        **[Required]** Gets the load_balancer_id of this WorkRequest.
        The `OCID`__ of the load balancer with which the work request
        is associated.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The load_balancer_id of this WorkRequest.
        :rtype: str
        """
        return self._load_balancer_id

    @load_balancer_id.setter
    def load_balancer_id(self, load_balancer_id):
        """
        Sets the load_balancer_id of this WorkRequest.
        The `OCID`__ of the load balancer with which the work request
        is associated.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param load_balancer_id: The load_balancer_id of this WorkRequest.
        :type: str
        """
        self._load_balancer_id = load_balancer_id

    @property
    def message(self):
        """
        **[Required]** Gets the message of this WorkRequest.
        A collection of data, related to the load balancer provisioning process, that helps with debugging in the event of failure.
        Possible data elements include:

        - workflow name
        - event ID
        - work request ID
        - load balancer ID
        - workflow completion message


        :return: The message of this WorkRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this WorkRequest.
        A collection of data, related to the load balancer provisioning process, that helps with debugging in the event of failure.
        Possible data elements include:

        - workflow name
        - event ID
        - work request ID
        - load balancer ID
        - workflow completion message


        :param message: The message of this WorkRequest.
        :type: str
        """
        self._message = message

    @property
    def time_accepted(self):
        """
        **[Required]** Gets the time_accepted of this WorkRequest.
        The date and time the work request was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_accepted of this WorkRequest.
        :rtype: datetime
        """
        return self._time_accepted

    @time_accepted.setter
    def time_accepted(self, time_accepted):
        """
        Sets the time_accepted of this WorkRequest.
        The date and time the work request was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_accepted: The time_accepted of this WorkRequest.
        :type: datetime
        """
        self._time_accepted = time_accepted

    @property
    def time_finished(self):
        """
        Gets the time_finished of this WorkRequest.
        The date and time the work request was completed, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_finished of this WorkRequest.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this WorkRequest.
        The date and time the work request was completed, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_finished: The time_finished of this WorkRequest.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def type(self):
        """
        **[Required]** Gets the type of this WorkRequest.
        The type of action the work request represents.


        :return: The type of this WorkRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WorkRequest.
        The type of action the work request represents.


        :param type: The type of this WorkRequest.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
