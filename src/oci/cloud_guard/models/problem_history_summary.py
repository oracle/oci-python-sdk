# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProblemHistorySummary(object):
    """
    Problem History Definition.
    """

    #: A constant which can be used with the actor_type property of a ProblemHistorySummary.
    #: This constant has a value of "CLOUD_GUARD_SERVICE"
    ACTOR_TYPE_CLOUD_GUARD_SERVICE = "CLOUD_GUARD_SERVICE"

    #: A constant which can be used with the actor_type property of a ProblemHistorySummary.
    #: This constant has a value of "CORRELATION"
    ACTOR_TYPE_CORRELATION = "CORRELATION"

    #: A constant which can be used with the actor_type property of a ProblemHistorySummary.
    #: This constant has a value of "RESPONDER"
    ACTOR_TYPE_RESPONDER = "RESPONDER"

    #: A constant which can be used with the actor_type property of a ProblemHistorySummary.
    #: This constant has a value of "USER"
    ACTOR_TYPE_USER = "USER"

    #: A constant which can be used with the lifecycle_detail property of a ProblemHistorySummary.
    #: This constant has a value of "OPEN"
    LIFECYCLE_DETAIL_OPEN = "OPEN"

    #: A constant which can be used with the lifecycle_detail property of a ProblemHistorySummary.
    #: This constant has a value of "RESOLVED"
    LIFECYCLE_DETAIL_RESOLVED = "RESOLVED"

    #: A constant which can be used with the lifecycle_detail property of a ProblemHistorySummary.
    #: This constant has a value of "DISMISSED"
    LIFECYCLE_DETAIL_DISMISSED = "DISMISSED"

    #: A constant which can be used with the lifecycle_detail property of a ProblemHistorySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_DETAIL_DELETED = "DELETED"

    #: A constant which can be used with the event_status property of a ProblemHistorySummary.
    #: This constant has a value of "REOPEN"
    EVENT_STATUS_REOPEN = "REOPEN"

    #: A constant which can be used with the event_status property of a ProblemHistorySummary.
    #: This constant has a value of "OPEN"
    EVENT_STATUS_OPEN = "OPEN"

    #: A constant which can be used with the event_status property of a ProblemHistorySummary.
    #: This constant has a value of "UPDATE"
    EVENT_STATUS_UPDATE = "UPDATE"

    #: A constant which can be used with the event_status property of a ProblemHistorySummary.
    #: This constant has a value of "RESOLVE"
    EVENT_STATUS_RESOLVE = "RESOLVE"

    #: A constant which can be used with the event_status property of a ProblemHistorySummary.
    #: This constant has a value of "DISMISS"
    EVENT_STATUS_DISMISS = "DISMISS"

    #: A constant which can be used with the event_status property of a ProblemHistorySummary.
    #: This constant has a value of "DELETE"
    EVENT_STATUS_DELETE = "DELETE"

    def __init__(self, **kwargs):
        """
        Initializes a new ProblemHistorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ProblemHistorySummary.
        :type id: str

        :param problem_id:
            The value to assign to the problem_id property of this ProblemHistorySummary.
        :type problem_id: str

        :param actor_type:
            The value to assign to the actor_type property of this ProblemHistorySummary.
            Allowed values for this property are: "CLOUD_GUARD_SERVICE", "CORRELATION", "RESPONDER", "USER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type actor_type: str

        :param actor_name:
            The value to assign to the actor_name property of this ProblemHistorySummary.
        :type actor_name: str

        :param explanation:
            The value to assign to the explanation property of this ProblemHistorySummary.
        :type explanation: str

        :param lifecycle_detail:
            The value to assign to the lifecycle_detail property of this ProblemHistorySummary.
            Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_detail: str

        :param event_status:
            The value to assign to the event_status property of this ProblemHistorySummary.
            Allowed values for this property are: "REOPEN", "OPEN", "UPDATE", "RESOLVE", "DISMISS", "DELETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type event_status: str

        :param time_created:
            The value to assign to the time_created property of this ProblemHistorySummary.
        :type time_created: datetime

        :param delta:
            The value to assign to the delta property of this ProblemHistorySummary.
        :type delta: str

        :param comment:
            The value to assign to the comment property of this ProblemHistorySummary.
        :type comment: str

        """
        self.swagger_types = {
            'id': 'str',
            'problem_id': 'str',
            'actor_type': 'str',
            'actor_name': 'str',
            'explanation': 'str',
            'lifecycle_detail': 'str',
            'event_status': 'str',
            'time_created': 'datetime',
            'delta': 'str',
            'comment': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'problem_id': 'problemId',
            'actor_type': 'actorType',
            'actor_name': 'actorName',
            'explanation': 'explanation',
            'lifecycle_detail': 'lifecycleDetail',
            'event_status': 'eventStatus',
            'time_created': 'timeCreated',
            'delta': 'delta',
            'comment': 'comment'
        }

        self._id = None
        self._problem_id = None
        self._actor_type = None
        self._actor_name = None
        self._explanation = None
        self._lifecycle_detail = None
        self._event_status = None
        self._time_created = None
        self._delta = None
        self._comment = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ProblemHistorySummary.
        Unique identifier for the history record


        :return: The id of this ProblemHistorySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProblemHistorySummary.
        Unique identifier for the history record


        :param id: The id of this ProblemHistorySummary.
        :type: str
        """
        self._id = id

    @property
    def problem_id(self):
        """
        **[Required]** Gets the problem_id of this ProblemHistorySummary.
        problemId for which history is associated to.


        :return: The problem_id of this ProblemHistorySummary.
        :rtype: str
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id):
        """
        Sets the problem_id of this ProblemHistorySummary.
        problemId for which history is associated to.


        :param problem_id: The problem_id of this ProblemHistorySummary.
        :type: str
        """
        self._problem_id = problem_id

    @property
    def actor_type(self):
        """
        **[Required]** Gets the actor_type of this ProblemHistorySummary.
        Actor type who performed the operation

        Allowed values for this property are: "CLOUD_GUARD_SERVICE", "CORRELATION", "RESPONDER", "USER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The actor_type of this ProblemHistorySummary.
        :rtype: str
        """
        return self._actor_type

    @actor_type.setter
    def actor_type(self, actor_type):
        """
        Sets the actor_type of this ProblemHistorySummary.
        Actor type who performed the operation


        :param actor_type: The actor_type of this ProblemHistorySummary.
        :type: str
        """
        allowed_values = ["CLOUD_GUARD_SERVICE", "CORRELATION", "RESPONDER", "USER"]
        if not value_allowed_none_or_none_sentinel(actor_type, allowed_values):
            actor_type = 'UNKNOWN_ENUM_VALUE'
        self._actor_type = actor_type

    @property
    def actor_name(self):
        """
        **[Required]** Gets the actor_name of this ProblemHistorySummary.
        Resource Name who performed activity


        :return: The actor_name of this ProblemHistorySummary.
        :rtype: str
        """
        return self._actor_name

    @actor_name.setter
    def actor_name(self, actor_name):
        """
        Sets the actor_name of this ProblemHistorySummary.
        Resource Name who performed activity


        :param actor_name: The actor_name of this ProblemHistorySummary.
        :type: str
        """
        self._actor_name = actor_name

    @property
    def explanation(self):
        """
        **[Required]** Gets the explanation of this ProblemHistorySummary.
        Activity explanation details


        :return: The explanation of this ProblemHistorySummary.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """
        Sets the explanation of this ProblemHistorySummary.
        Activity explanation details


        :param explanation: The explanation of this ProblemHistorySummary.
        :type: str
        """
        self._explanation = explanation

    @property
    def lifecycle_detail(self):
        """
        **[Required]** Gets the lifecycle_detail of this ProblemHistorySummary.
        Problem Lifecycle Detail Status

        Allowed values for this property are: "OPEN", "RESOLVED", "DISMISSED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_detail of this ProblemHistorySummary.
        :rtype: str
        """
        return self._lifecycle_detail

    @lifecycle_detail.setter
    def lifecycle_detail(self, lifecycle_detail):
        """
        Sets the lifecycle_detail of this ProblemHistorySummary.
        Problem Lifecycle Detail Status


        :param lifecycle_detail: The lifecycle_detail of this ProblemHistorySummary.
        :type: str
        """
        allowed_values = ["OPEN", "RESOLVED", "DISMISSED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_detail, allowed_values):
            lifecycle_detail = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_detail = lifecycle_detail

    @property
    def event_status(self):
        """
        Gets the event_status of this ProblemHistorySummary.
        Event status

        Allowed values for this property are: "REOPEN", "OPEN", "UPDATE", "RESOLVE", "DISMISS", "DELETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The event_status of this ProblemHistorySummary.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """
        Sets the event_status of this ProblemHistorySummary.
        Event status


        :param event_status: The event_status of this ProblemHistorySummary.
        :type: str
        """
        allowed_values = ["REOPEN", "OPEN", "UPDATE", "RESOLVE", "DISMISS", "DELETE"]
        if not value_allowed_none_or_none_sentinel(event_status, allowed_values):
            event_status = 'UNKNOWN_ENUM_VALUE'
        self._event_status = event_status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ProblemHistorySummary.
        Type of the Entity


        :return: The time_created of this ProblemHistorySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProblemHistorySummary.
        Type of the Entity


        :param time_created: The time_created of this ProblemHistorySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def delta(self):
        """
        **[Required]** Gets the delta of this ProblemHistorySummary.
        Impacted Resource Names in a comma-separated string.


        :return: The delta of this ProblemHistorySummary.
        :rtype: str
        """
        return self._delta

    @delta.setter
    def delta(self, delta):
        """
        Sets the delta of this ProblemHistorySummary.
        Impacted Resource Names in a comma-separated string.


        :param delta: The delta of this ProblemHistorySummary.
        :type: str
        """
        self._delta = delta

    @property
    def comment(self):
        """
        Gets the comment of this ProblemHistorySummary.
        User Defined Comments


        :return: The comment of this ProblemHistorySummary.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this ProblemHistorySummary.
        User Defined Comments


        :param comment: The comment of this ProblemHistorySummary.
        :type: str
        """
        self._comment = comment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
