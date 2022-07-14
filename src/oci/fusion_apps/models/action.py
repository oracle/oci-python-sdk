# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Action(object):
    """
    Action details
    """

    #: A constant which can be used with the action_type property of a Action.
    #: This constant has a value of "QUARTERLY_UPGRADE"
    ACTION_TYPE_QUARTERLY_UPGRADE = "QUARTERLY_UPGRADE"

    #: A constant which can be used with the action_type property of a Action.
    #: This constant has a value of "PATCH"
    ACTION_TYPE_PATCH = "PATCH"

    #: A constant which can be used with the action_type property of a Action.
    #: This constant has a value of "VERTEX"
    ACTION_TYPE_VERTEX = "VERTEX"

    #: A constant which can be used with the state property of a Action.
    #: This constant has a value of "ACCEPTED"
    STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the state property of a Action.
    #: This constant has a value of "IN_PROGRESS"
    STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the state property of a Action.
    #: This constant has a value of "SUCCEEDED"
    STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the state property of a Action.
    #: This constant has a value of "FAILED"
    STATE_FAILED = "FAILED"

    #: A constant which can be used with the state property of a Action.
    #: This constant has a value of "CANCELED"
    STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new Action object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.fusion_apps.models.PatchAction`
        * :class:`~oci.fusion_apps.models.UpgradeAction`
        * :class:`~oci.fusion_apps.models.VertexAction`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param reference_key:
            The value to assign to the reference_key property of this Action.
        :type reference_key: str

        :param action_type:
            The value to assign to the action_type property of this Action.
            Allowed values for this property are: "QUARTERLY_UPGRADE", "PATCH", "VERTEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action_type: str

        :param state:
            The value to assign to the state property of this Action.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type state: str

        :param description:
            The value to assign to the description property of this Action.
        :type description: str

        """
        self.swagger_types = {
            'reference_key': 'str',
            'action_type': 'str',
            'state': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'reference_key': 'referenceKey',
            'action_type': 'actionType',
            'state': 'state',
            'description': 'description'
        }

        self._reference_key = None
        self._action_type = None
        self._state = None
        self._description = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['actionType']

        if type == 'PATCH':
            return 'PatchAction'

        if type == 'QUARTERLY_UPGRADE':
            return 'UpgradeAction'

        if type == 'VERTEX':
            return 'VertexAction'
        else:
            return 'Action'

    @property
    def reference_key(self):
        """
        Gets the reference_key of this Action.
        Unique identifier of the object that represents the action


        :return: The reference_key of this Action.
        :rtype: str
        """
        return self._reference_key

    @reference_key.setter
    def reference_key(self, reference_key):
        """
        Sets the reference_key of this Action.
        Unique identifier of the object that represents the action


        :param reference_key: The reference_key of this Action.
        :type: str
        """
        self._reference_key = reference_key

    @property
    def action_type(self):
        """
        **[Required]** Gets the action_type of this Action.
        Type of action

        Allowed values for this property are: "QUARTERLY_UPGRADE", "PATCH", "VERTEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action_type of this Action.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this Action.
        Type of action


        :param action_type: The action_type of this Action.
        :type: str
        """
        allowed_values = ["QUARTERLY_UPGRADE", "PATCH", "VERTEX"]
        if not value_allowed_none_or_none_sentinel(action_type, allowed_values):
            action_type = 'UNKNOWN_ENUM_VALUE'
        self._action_type = action_type

    @property
    def state(self):
        """
        Gets the state of this Action.
        A string that describes whether the change is applied hot or cold

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The state of this Action.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Action.
        A string that describes whether the change is applied hot or cold


        :param state: The state of this Action.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(state, allowed_values):
            state = 'UNKNOWN_ENUM_VALUE'
        self._state = state

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Action.
        A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering confidential information.


        :return: The description of this Action.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Action.
        A string that describes the details of the action. It does not have to be unique, and you can change it. Avoid entering confidential information.


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
