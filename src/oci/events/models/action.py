# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Action(object):
    """
    An object that represents an action to trigger for events that match a rule.
    """

    #: A constant which can be used with the action_type property of a Action.
    #: This constant has a value of "ONS"
    ACTION_TYPE_ONS = "ONS"

    #: A constant which can be used with the action_type property of a Action.
    #: This constant has a value of "OSS"
    ACTION_TYPE_OSS = "OSS"

    #: A constant which can be used with the action_type property of a Action.
    #: This constant has a value of "FAAS"
    ACTION_TYPE_FAAS = "FAAS"

    #: A constant which can be used with the lifecycle_state property of a Action.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Action.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Action.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Action.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Action.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Action.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Action.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Action object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.events.models.StreamingServiceAction`
        * :class:`~oci.events.models.NotificationServiceAction`
        * :class:`~oci.events.models.FaaSAction`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this Action.
            Allowed values for this property are: "ONS", "OSS", "FAAS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_type: str

        :param id:
            The value to assign to the id property of this Action.
        :type id: str

        :param lifecycle_message:
            The value to assign to the lifecycle_message property of this Action.
        :type lifecycle_message: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Action.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_enabled:
            The value to assign to the is_enabled property of this Action.
        :type is_enabled: bool

        :param description:
            The value to assign to the description property of this Action.
        :type description: str

        """
        self.swagger_types = {
            'action_type': 'str',
            'id': 'str',
            'lifecycle_message': 'str',
            'lifecycle_state': 'str',
            'is_enabled': 'bool',
            'description': 'str'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'id': 'id',
            'lifecycle_message': 'lifecycleMessage',
            'lifecycle_state': 'lifecycleState',
            'is_enabled': 'isEnabled',
            'description': 'description'
        }

        self._action_type = None
        self._id = None
        self._lifecycle_message = None
        self._lifecycle_state = None
        self._is_enabled = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['actionType']

        if type == 'OSS':
            return 'StreamingServiceAction'

        if type == 'ONS':
            return 'NotificationServiceAction'

        if type == 'FAAS':
            return 'FaaSAction'
        else:
            return 'Action'

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this Action.
        The action to perform if the condition in the rule matches an event.

        * **ONS:** Send to an Oracle Notification Service topic.
        * **OSS:** Send to a stream from Oracle Streaming Service.
        * **FAAS:** Send to an Oracle Functions Service endpoint.

        Allowed values for this property are: "ONS", "OSS", "FAAS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_type of this Action.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this Action.
        The action to perform if the condition in the rule matches an event.

        * **ONS:** Send to an Oracle Notification Service topic.
        * **OSS:** Send to a stream from Oracle Streaming Service.
        * **FAAS:** Send to an Oracle Functions Service endpoint.


        :param action_type: The action_type of this Action.
        :type: str
        """
        allowed_values = ["ONS", "OSS", "FAAS"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            action_type = 'UNKNOWN_ENUM_VALUE'
        self._action_type = action_type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Action.
        The `OCID`__ of the action.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this Action.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Action.
        The `OCID`__ of the action.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this Action.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_message(self):
        """
        **[Required]** Gets the lifecycle_message of this Action.
        A message generated by the Events service about the current state of this action.


        :return: The lifecycle_message of this Action.
        :rtype: str
        """
        return self._lifecycle_message

    @lifecycle_message.setter
    def lifecycle_message(self, lifecycle_message):
        """
        Sets the lifecycle_message of this Action.
        A message generated by the Events service about the current state of this action.


        :param lifecycle_message: The lifecycle_message of this Action.
        :type: str
        """
        self._lifecycle_message = lifecycle_message

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Action.
        The current state of the rule.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Action.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Action.
        The current state of the rule.


        :param lifecycle_state: The lifecycle_state of this Action.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this Action.
        Whether or not this action is currently enabled.

        Example: `true`


        :return: The is_enabled of this Action.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this Action.
        Whether or not this action is currently enabled.

        Example: `true`


        :param is_enabled: The is_enabled of this Action.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def description(self):
        """
        Gets the description of this Action.
        A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :return: The description of this Action.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Action.
        A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering
        confidential information.


        :param description: The description of this Action.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
