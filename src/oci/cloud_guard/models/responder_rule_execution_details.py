# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponderRuleExecutionDetails(object):
    """
    Details of ResponderRuleExecution. A Responder Rule Execution is the entity that captures the execution of a Responder Rule for a given Problem.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResponderRuleExecutionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition:
            The value to assign to the condition property of this ResponderRuleExecutionDetails.
        :type condition: oci.cloud_guard.models.Condition

        :param configurations:
            The value to assign to the configurations property of this ResponderRuleExecutionDetails.
        :type configurations: list[oci.cloud_guard.models.ResponderConfiguration]

        """
        self.swagger_types = {
            'condition': 'Condition',
            'configurations': 'list[ResponderConfiguration]'
        }

        self.attribute_map = {
            'condition': 'condition',
            'configurations': 'configurations'
        }

        self._condition = None
        self._configurations = None

    @property
    def condition(self):
        """
        Gets the condition of this ResponderRuleExecutionDetails.

        :return: The condition of this ResponderRuleExecutionDetails.
        :rtype: oci.cloud_guard.models.Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this ResponderRuleExecutionDetails.

        :param condition: The condition of this ResponderRuleExecutionDetails.
        :type: oci.cloud_guard.models.Condition
        """
        self._condition = condition

    @property
    def configurations(self):
        """
        Gets the configurations of this ResponderRuleExecutionDetails.
        ResponderRule configurations


        :return: The configurations of this ResponderRuleExecutionDetails.
        :rtype: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this ResponderRuleExecutionDetails.
        ResponderRule configurations


        :param configurations: The configurations of this ResponderRuleExecutionDetails.
        :type: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        self._configurations = configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
