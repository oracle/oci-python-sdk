# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .push_down_operation import PushDownOperation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Join(PushDownOperation):
    """
    The information about the join operator. The join operator links data from multiple inbound sources.
    """

    #: A constant which can be used with the policy property of a Join.
    #: This constant has a value of "INNER_JOIN"
    POLICY_INNER_JOIN = "INNER_JOIN"

    #: A constant which can be used with the policy property of a Join.
    #: This constant has a value of "LEFT_JOIN"
    POLICY_LEFT_JOIN = "LEFT_JOIN"

    #: A constant which can be used with the policy property of a Join.
    #: This constant has a value of "RIGHT_JOIN"
    POLICY_RIGHT_JOIN = "RIGHT_JOIN"

    #: A constant which can be used with the policy property of a Join.
    #: This constant has a value of "FULL_JOIN"
    POLICY_FULL_JOIN = "FULL_JOIN"

    def __init__(self, **kwargs):
        """
        Initializes a new Join object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Join.model_type` attribute
        of this class is ``JOIN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Join.
            Allowed values for this property are: "FILTER", "JOIN", "SELECT", "SORT", "QUERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param condition:
            The value to assign to the condition property of this Join.
        :type condition: str

        :param policy:
            The value to assign to the policy property of this Join.
            Allowed values for this property are: "INNER_JOIN", "LEFT_JOIN", "RIGHT_JOIN", "FULL_JOIN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type policy: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'condition': 'str',
            'policy': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'condition': 'condition',
            'policy': 'policy'
        }

        self._model_type = None
        self._condition = None
        self._policy = None
        self._model_type = 'JOIN'

    @property
    def condition(self):
        """
        Gets the condition of this Join.
        The join condition.


        :return: The condition of this Join.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this Join.
        The join condition.


        :param condition: The condition of this Join.
        :type: str
        """
        self._condition = condition

    @property
    def policy(self):
        """
        Gets the policy of this Join.
        The type of join.

        Allowed values for this property are: "INNER_JOIN", "LEFT_JOIN", "RIGHT_JOIN", "FULL_JOIN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The policy of this Join.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this Join.
        The type of join.


        :param policy: The policy of this Join.
        :type: str
        """
        allowed_values = ["INNER_JOIN", "LEFT_JOIN", "RIGHT_JOIN", "FULL_JOIN"]
        if not value_allowed_none_or_none_sentinel(policy, allowed_values):
            policy = 'UNKNOWN_ENUM_VALUE'
        self._policy = policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
