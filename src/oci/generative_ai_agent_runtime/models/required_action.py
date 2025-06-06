# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequiredAction(object):
    """
    Represents an action that needs to be performed by the user or client.
    """

    #: A constant which can be used with the required_action_type property of a RequiredAction.
    #: This constant has a value of "HUMAN_APPROVAL_REQUIRED_ACTION"
    REQUIRED_ACTION_TYPE_HUMAN_APPROVAL_REQUIRED_ACTION = "HUMAN_APPROVAL_REQUIRED_ACTION"

    #: A constant which can be used with the required_action_type property of a RequiredAction.
    #: This constant has a value of "FUNCTION_CALLING_REQUIRED_ACTION"
    REQUIRED_ACTION_TYPE_FUNCTION_CALLING_REQUIRED_ACTION = "FUNCTION_CALLING_REQUIRED_ACTION"

    def __init__(self, **kwargs):
        """
        Initializes a new RequiredAction object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_agent_runtime.models.HumanApprovalRequiredAction`
        * :class:`~oci.generative_ai_agent_runtime.models.FunctionCallingRequiredAction`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_id:
            The value to assign to the action_id property of this RequiredAction.
        :type action_id: str

        :param required_action_type:
            The value to assign to the required_action_type property of this RequiredAction.
            Allowed values for this property are: "HUMAN_APPROVAL_REQUIRED_ACTION", "FUNCTION_CALLING_REQUIRED_ACTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type required_action_type: str

        """
        self.swagger_types = {
            'action_id': 'str',
            'required_action_type': 'str'
        }
        self.attribute_map = {
            'action_id': 'actionId',
            'required_action_type': 'requiredActionType'
        }
        self._action_id = None
        self._required_action_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['requiredActionType']

        if type == 'HUMAN_APPROVAL_REQUIRED_ACTION':
            return 'HumanApprovalRequiredAction'

        if type == 'FUNCTION_CALLING_REQUIRED_ACTION':
            return 'FunctionCallingRequiredAction'
        else:
            return 'RequiredAction'

    @property
    def action_id(self):
        """
        **[Required]** Gets the action_id of this RequiredAction.
        The unique identifier for the action to be performed.


        :return: The action_id of this RequiredAction.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """
        Sets the action_id of this RequiredAction.
        The unique identifier for the action to be performed.


        :param action_id: The action_id of this RequiredAction.
        :type: str
        """
        self._action_id = action_id

    @property
    def required_action_type(self):
        """
        **[Required]** Gets the required_action_type of this RequiredAction.
        Specifies the type of action. Used for determining the action subtype.

        Allowed values for this property are: "HUMAN_APPROVAL_REQUIRED_ACTION", "FUNCTION_CALLING_REQUIRED_ACTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The required_action_type of this RequiredAction.
        :rtype: str
        """
        return self._required_action_type

    @required_action_type.setter
    def required_action_type(self, required_action_type):
        """
        Sets the required_action_type of this RequiredAction.
        Specifies the type of action. Used for determining the action subtype.


        :param required_action_type: The required_action_type of this RequiredAction.
        :type: str
        """
        allowed_values = ["HUMAN_APPROVAL_REQUIRED_ACTION", "FUNCTION_CALLING_REQUIRED_ACTION"]
        if not value_allowed_none_or_none_sentinel(required_action_type, allowed_values):
            required_action_type = 'UNKNOWN_ENUM_VALUE'
        self._required_action_type = required_action_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
