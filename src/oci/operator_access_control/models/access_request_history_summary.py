# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessRequestHistorySummary(object):
    """
    Summary of access request status.
    """

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "APPROVALWAITING"
    LIFECYCLE_STATE_APPROVALWAITING = "APPROVALWAITING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "PREAPPROVED"
    LIFECYCLE_STATE_PREAPPROVED = "PREAPPROVED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "APPROVED"
    LIFECYCLE_STATE_APPROVED = "APPROVED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "REJECTED"
    LIFECYCLE_STATE_REJECTED = "REJECTED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "DEPLOYED"
    LIFECYCLE_STATE_DEPLOYED = "DEPLOYED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "DEPLOYFAILED"
    LIFECYCLE_STATE_DEPLOYFAILED = "DEPLOYFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "UNDEPLOYED"
    LIFECYCLE_STATE_UNDEPLOYED = "UNDEPLOYED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "UNDEPLOYFAILED"
    LIFECYCLE_STATE_UNDEPLOYFAILED = "UNDEPLOYFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "CLOSEFAILED"
    LIFECYCLE_STATE_CLOSEFAILED = "CLOSEFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "REVOKEFAILED"
    LIFECYCLE_STATE_REVOKEFAILED = "REVOKEFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "EXPIRYFAILED"
    LIFECYCLE_STATE_EXPIRYFAILED = "EXPIRYFAILED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "REVOKING"
    LIFECYCLE_STATE_REVOKING = "REVOKING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "REVOKED"
    LIFECYCLE_STATE_REVOKED = "REVOKED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "EXTENDING"
    LIFECYCLE_STATE_EXTENDING = "EXTENDING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "EXTENDED"
    LIFECYCLE_STATE_EXTENDED = "EXTENDED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "EXTENSIONREJECTED"
    LIFECYCLE_STATE_EXTENSIONREJECTED = "EXTENSIONREJECTED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "COMPLETING"
    LIFECYCLE_STATE_COMPLETING = "COMPLETING"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "COMPLETED"
    LIFECYCLE_STATE_COMPLETED = "COMPLETED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "EXPIRED"
    LIFECYCLE_STATE_EXPIRED = "EXPIRED"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "APPROVEDFORFUTURE"
    LIFECYCLE_STATE_APPROVEDFORFUTURE = "APPROVEDFORFUTURE"

    #: A constant which can be used with the lifecycle_state property of a AccessRequestHistorySummary.
    #: This constant has a value of "INREVIEW"
    LIFECYCLE_STATE_INREVIEW = "INREVIEW"

    def __init__(self, **kwargs):
        """
        Initializes a new AccessRequestHistorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AccessRequestHistorySummary.
            Allowed values for this property are: "CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param user_id:
            The value to assign to the user_id property of this AccessRequestHistorySummary.
        :type user_id: str

        :param description:
            The value to assign to the description property of this AccessRequestHistorySummary.
        :type description: str

        :param duration:
            The value to assign to the duration property of this AccessRequestHistorySummary.
        :type duration: int

        :param is_auto_approved:
            The value to assign to the is_auto_approved property of this AccessRequestHistorySummary.
        :type is_auto_approved: bool

        :param actions_list:
            The value to assign to the actions_list property of this AccessRequestHistorySummary.
        :type actions_list: list[str]

        :param time_of_action:
            The value to assign to the time_of_action property of this AccessRequestHistorySummary.
        :type time_of_action: datetime

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'user_id': 'str',
            'description': 'str',
            'duration': 'int',
            'is_auto_approved': 'bool',
            'actions_list': 'list[str]',
            'time_of_action': 'datetime'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'user_id': 'userId',
            'description': 'description',
            'duration': 'duration',
            'is_auto_approved': 'isAutoApproved',
            'actions_list': 'actionsList',
            'time_of_action': 'timeOfAction'
        }

        self._lifecycle_state = None
        self._user_id = None
        self._description = None
        self._duration = None
        self._is_auto_approved = None
        self._actions_list = None
        self._time_of_action = None

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AccessRequestHistorySummary.
        The current state of the AccessRequest.

        Allowed values for this property are: "CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AccessRequestHistorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AccessRequestHistorySummary.
        The current state of the AccessRequest.


        :param lifecycle_state: The lifecycle_state of this AccessRequestHistorySummary.
        :type: str
        """
        allowed_values = ["CREATED", "APPROVALWAITING", "PREAPPROVED", "APPROVED", "REJECTED", "DEPLOYED", "DEPLOYFAILED", "UNDEPLOYED", "UNDEPLOYFAILED", "CLOSEFAILED", "REVOKEFAILED", "EXPIRYFAILED", "REVOKING", "REVOKED", "EXTENDING", "EXTENDED", "EXTENSIONREJECTED", "COMPLETING", "COMPLETED", "EXPIRED", "APPROVEDFORFUTURE", "INREVIEW"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def user_id(self):
        """
        Gets the user_id of this AccessRequestHistorySummary.
        Approver who modified the access request.


        :return: The user_id of this AccessRequestHistorySummary.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AccessRequestHistorySummary.
        Approver who modified the access request.


        :param user_id: The user_id of this AccessRequestHistorySummary.
        :type: str
        """
        self._user_id = user_id

    @property
    def description(self):
        """
        Gets the description of this AccessRequestHistorySummary.
        Reason or description about the cause of change.


        :return: The description of this AccessRequestHistorySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AccessRequestHistorySummary.
        Reason or description about the cause of change.


        :param description: The description of this AccessRequestHistorySummary.
        :type: str
        """
        self._description = description

    @property
    def duration(self):
        """
        Gets the duration of this AccessRequestHistorySummary.
        Duration for approval of request or extension depending on the type of action.


        :return: The duration of this AccessRequestHistorySummary.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this AccessRequestHistorySummary.
        Duration for approval of request or extension depending on the type of action.


        :param duration: The duration of this AccessRequestHistorySummary.
        :type: int
        """
        self._duration = duration

    @property
    def is_auto_approved(self):
        """
        Gets the is_auto_approved of this AccessRequestHistorySummary.
        Whether the access request was automatically approved.


        :return: The is_auto_approved of this AccessRequestHistorySummary.
        :rtype: bool
        """
        return self._is_auto_approved

    @is_auto_approved.setter
    def is_auto_approved(self, is_auto_approved):
        """
        Sets the is_auto_approved of this AccessRequestHistorySummary.
        Whether the access request was automatically approved.


        :param is_auto_approved: The is_auto_approved of this AccessRequestHistorySummary.
        :type: bool
        """
        self._is_auto_approved = is_auto_approved

    @property
    def actions_list(self):
        """
        Gets the actions_list of this AccessRequestHistorySummary.
        List of operator actions for which approvals were requested by the operator.


        :return: The actions_list of this AccessRequestHistorySummary.
        :rtype: list[str]
        """
        return self._actions_list

    @actions_list.setter
    def actions_list(self, actions_list):
        """
        Sets the actions_list of this AccessRequestHistorySummary.
        List of operator actions for which approvals were requested by the operator.


        :param actions_list: The actions_list of this AccessRequestHistorySummary.
        :type: list[str]
        """
        self._actions_list = actions_list

    @property
    def time_of_action(self):
        """
        Gets the time_of_action of this AccessRequestHistorySummary.
        Time when the respective action happened in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_action of this AccessRequestHistorySummary.
        :rtype: datetime
        """
        return self._time_of_action

    @time_of_action.setter
    def time_of_action(self, time_of_action):
        """
        Sets the time_of_action of this AccessRequestHistorySummary.
        Time when the respective action happened in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_action: The time_of_action of this AccessRequestHistorySummary.
        :type: datetime
        """
        self._time_of_action = time_of_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
