# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponderActivitySummary(object):
    """
    Responder Activity summary Definition.
    """

    #: A constant which can be used with the responder_type property of a ResponderActivitySummary.
    #: This constant has a value of "REMEDIATION"
    RESPONDER_TYPE_REMEDIATION = "REMEDIATION"

    #: A constant which can be used with the responder_type property of a ResponderActivitySummary.
    #: This constant has a value of "NOTIFICATION"
    RESPONDER_TYPE_NOTIFICATION = "NOTIFICATION"

    #: A constant which can be used with the responder_activity_type property of a ResponderActivitySummary.
    #: This constant has a value of "STARTED"
    RESPONDER_ACTIVITY_TYPE_STARTED = "STARTED"

    #: A constant which can be used with the responder_activity_type property of a ResponderActivitySummary.
    #: This constant has a value of "COMPLETED"
    RESPONDER_ACTIVITY_TYPE_COMPLETED = "COMPLETED"

    #: A constant which can be used with the responder_execution_status property of a ResponderActivitySummary.
    #: This constant has a value of "STARTED"
    RESPONDER_EXECUTION_STATUS_STARTED = "STARTED"

    #: A constant which can be used with the responder_execution_status property of a ResponderActivitySummary.
    #: This constant has a value of "AWAITING_CONFIRMATION"
    RESPONDER_EXECUTION_STATUS_AWAITING_CONFIRMATION = "AWAITING_CONFIRMATION"

    #: A constant which can be used with the responder_execution_status property of a ResponderActivitySummary.
    #: This constant has a value of "AWAITING_INPUT"
    RESPONDER_EXECUTION_STATUS_AWAITING_INPUT = "AWAITING_INPUT"

    #: A constant which can be used with the responder_execution_status property of a ResponderActivitySummary.
    #: This constant has a value of "SUCCEEDED"
    RESPONDER_EXECUTION_STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the responder_execution_status property of a ResponderActivitySummary.
    #: This constant has a value of "FAILED"
    RESPONDER_EXECUTION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the responder_execution_status property of a ResponderActivitySummary.
    #: This constant has a value of "SKIPPED"
    RESPONDER_EXECUTION_STATUS_SKIPPED = "SKIPPED"

    #: A constant which can be used with the responder_execution_status property of a ResponderActivitySummary.
    #: This constant has a value of "ALL"
    RESPONDER_EXECUTION_STATUS_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new ResponderActivitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ResponderActivitySummary.
        :type id: str

        :param problem_id:
            The value to assign to the problem_id property of this ResponderActivitySummary.
        :type problem_id: str

        :param responder_rule_id:
            The value to assign to the responder_rule_id property of this ResponderActivitySummary.
        :type responder_rule_id: str

        :param responder_type:
            The value to assign to the responder_type property of this ResponderActivitySummary.
            Allowed values for this property are: "REMEDIATION", "NOTIFICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type responder_type: str

        :param responder_rule_name:
            The value to assign to the responder_rule_name property of this ResponderActivitySummary.
        :type responder_rule_name: str

        :param responder_activity_type:
            The value to assign to the responder_activity_type property of this ResponderActivitySummary.
            Allowed values for this property are: "STARTED", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type responder_activity_type: str

        :param responder_execution_status:
            The value to assign to the responder_execution_status property of this ResponderActivitySummary.
            Allowed values for this property are: "STARTED", "AWAITING_CONFIRMATION", "AWAITING_INPUT", "SUCCEEDED", "FAILED", "SKIPPED", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type responder_execution_status: str

        :param time_created:
            The value to assign to the time_created property of this ResponderActivitySummary.
        :type time_created: datetime

        :param message:
            The value to assign to the message property of this ResponderActivitySummary.
        :type message: str

        """
        self.swagger_types = {
            'id': 'str',
            'problem_id': 'str',
            'responder_rule_id': 'str',
            'responder_type': 'str',
            'responder_rule_name': 'str',
            'responder_activity_type': 'str',
            'responder_execution_status': 'str',
            'time_created': 'datetime',
            'message': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'problem_id': 'problemId',
            'responder_rule_id': 'responderRuleId',
            'responder_type': 'responderType',
            'responder_rule_name': 'responderRuleName',
            'responder_activity_type': 'responderActivityType',
            'responder_execution_status': 'responderExecutionStatus',
            'time_created': 'timeCreated',
            'message': 'message'
        }

        self._id = None
        self._problem_id = None
        self._responder_rule_id = None
        self._responder_type = None
        self._responder_rule_name = None
        self._responder_activity_type = None
        self._responder_execution_status = None
        self._time_created = None
        self._message = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResponderActivitySummary.
        Unique id for Responder activity.


        :return: The id of this ResponderActivitySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResponderActivitySummary.
        Unique id for Responder activity.


        :param id: The id of this ResponderActivitySummary.
        :type: str
        """
        self._id = id

    @property
    def problem_id(self):
        """
        **[Required]** Gets the problem_id of this ResponderActivitySummary.
        problemId for which Responder activity is associated to.


        :return: The problem_id of this ResponderActivitySummary.
        :rtype: str
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id):
        """
        Sets the problem_id of this ResponderActivitySummary.
        problemId for which Responder activity is associated to.


        :param problem_id: The problem_id of this ResponderActivitySummary.
        :type: str
        """
        self._problem_id = problem_id

    @property
    def responder_rule_id(self):
        """
        **[Required]** Gets the responder_rule_id of this ResponderActivitySummary.
        Id of the responder rule for the problem


        :return: The responder_rule_id of this ResponderActivitySummary.
        :rtype: str
        """
        return self._responder_rule_id

    @responder_rule_id.setter
    def responder_rule_id(self, responder_rule_id):
        """
        Sets the responder_rule_id of this ResponderActivitySummary.
        Id of the responder rule for the problem


        :param responder_rule_id: The responder_rule_id of this ResponderActivitySummary.
        :type: str
        """
        self._responder_rule_id = responder_rule_id

    @property
    def responder_type(self):
        """
        **[Required]** Gets the responder_type of this ResponderActivitySummary.
        responder rule type for performing the operation

        Allowed values for this property are: "REMEDIATION", "NOTIFICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The responder_type of this ResponderActivitySummary.
        :rtype: str
        """
        return self._responder_type

    @responder_type.setter
    def responder_type(self, responder_type):
        """
        Sets the responder_type of this ResponderActivitySummary.
        responder rule type for performing the operation


        :param responder_type: The responder_type of this ResponderActivitySummary.
        :type: str
        """
        allowed_values = ["REMEDIATION", "NOTIFICATION"]
        if not value_allowed_none_or_none_sentinel(responder_type, allowed_values):
            responder_type = 'UNKNOWN_ENUM_VALUE'
        self._responder_type = responder_type

    @property
    def responder_rule_name(self):
        """
        **[Required]** Gets the responder_rule_name of this ResponderActivitySummary.
        responder rule name


        :return: The responder_rule_name of this ResponderActivitySummary.
        :rtype: str
        """
        return self._responder_rule_name

    @responder_rule_name.setter
    def responder_rule_name(self, responder_rule_name):
        """
        Sets the responder_rule_name of this ResponderActivitySummary.
        responder rule name


        :param responder_rule_name: The responder_rule_name of this ResponderActivitySummary.
        :type: str
        """
        self._responder_rule_name = responder_rule_name

    @property
    def responder_activity_type(self):
        """
        **[Required]** Gets the responder_activity_type of this ResponderActivitySummary.
        Responder activity types

        Allowed values for this property are: "STARTED", "COMPLETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The responder_activity_type of this ResponderActivitySummary.
        :rtype: str
        """
        return self._responder_activity_type

    @responder_activity_type.setter
    def responder_activity_type(self, responder_activity_type):
        """
        Sets the responder_activity_type of this ResponderActivitySummary.
        Responder activity types


        :param responder_activity_type: The responder_activity_type of this ResponderActivitySummary.
        :type: str
        """
        allowed_values = ["STARTED", "COMPLETED"]
        if not value_allowed_none_or_none_sentinel(responder_activity_type, allowed_values):
            responder_activity_type = 'UNKNOWN_ENUM_VALUE'
        self._responder_activity_type = responder_activity_type

    @property
    def responder_execution_status(self):
        """
        **[Required]** Gets the responder_execution_status of this ResponderActivitySummary.
        the responder execution status

        Allowed values for this property are: "STARTED", "AWAITING_CONFIRMATION", "AWAITING_INPUT", "SUCCEEDED", "FAILED", "SKIPPED", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The responder_execution_status of this ResponderActivitySummary.
        :rtype: str
        """
        return self._responder_execution_status

    @responder_execution_status.setter
    def responder_execution_status(self, responder_execution_status):
        """
        Sets the responder_execution_status of this ResponderActivitySummary.
        the responder execution status


        :param responder_execution_status: The responder_execution_status of this ResponderActivitySummary.
        :type: str
        """
        allowed_values = ["STARTED", "AWAITING_CONFIRMATION", "AWAITING_INPUT", "SUCCEEDED", "FAILED", "SKIPPED", "ALL"]
        if not value_allowed_none_or_none_sentinel(responder_execution_status, allowed_values):
            responder_execution_status = 'UNKNOWN_ENUM_VALUE'
        self._responder_execution_status = responder_execution_status

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ResponderActivitySummary.
        responder activity starting time


        :return: The time_created of this ResponderActivitySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ResponderActivitySummary.
        responder activity starting time


        :param time_created: The time_created of this ResponderActivitySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def message(self):
        """
        **[Required]** Gets the message of this ResponderActivitySummary.
        additional message related to this operation


        :return: The message of this ResponderActivitySummary.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ResponderActivitySummary.
        additional message related to this operation


        :param message: The message of this ResponderActivitySummary.
        :type: str
        """
        self._message = message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
