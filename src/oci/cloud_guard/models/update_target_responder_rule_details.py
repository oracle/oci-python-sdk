# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetResponderRuleDetails(object):
    """
    Details of ResponderRule.
    """

    #: A constant which can be used with the mode property of a UpdateTargetResponderRuleDetails.
    #: This constant has a value of "AUTOACTION"
    MODE_AUTOACTION = "AUTOACTION"

    #: A constant which can be used with the mode property of a UpdateTargetResponderRuleDetails.
    #: This constant has a value of "USERACTION"
    MODE_USERACTION = "USERACTION"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetResponderRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition:
            The value to assign to the condition property of this UpdateTargetResponderRuleDetails.
        :type condition: oci.cloud_guard.models.Condition

        :param configurations:
            The value to assign to the configurations property of this UpdateTargetResponderRuleDetails.
        :type configurations: list[oci.cloud_guard.models.ResponderConfiguration]

        :param mode:
            The value to assign to the mode property of this UpdateTargetResponderRuleDetails.
            Allowed values for this property are: "AUTOACTION", "USERACTION"
        :type mode: str

        """
        self.swagger_types = {
            'condition': 'Condition',
            'configurations': 'list[ResponderConfiguration]',
            'mode': 'str'
        }

        self.attribute_map = {
            'condition': 'condition',
            'configurations': 'configurations',
            'mode': 'mode'
        }

        self._condition = None
        self._configurations = None
        self._mode = None

    @property
    def condition(self):
        """
        Gets the condition of this UpdateTargetResponderRuleDetails.

        :return: The condition of this UpdateTargetResponderRuleDetails.
        :rtype: oci.cloud_guard.models.Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this UpdateTargetResponderRuleDetails.

        :param condition: The condition of this UpdateTargetResponderRuleDetails.
        :type: oci.cloud_guard.models.Condition
        """
        self._condition = condition

    @property
    def configurations(self):
        """
        Gets the configurations of this UpdateTargetResponderRuleDetails.
        Configurations associated with the ResponderRule


        :return: The configurations of this UpdateTargetResponderRuleDetails.
        :rtype: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this UpdateTargetResponderRuleDetails.
        Configurations associated with the ResponderRule


        :param configurations: The configurations of this UpdateTargetResponderRuleDetails.
        :type: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        self._configurations = configurations

    @property
    def mode(self):
        """
        Gets the mode of this UpdateTargetResponderRuleDetails.
        Execution Mode for ResponderRule

        Allowed values for this property are: "AUTOACTION", "USERACTION"


        :return: The mode of this UpdateTargetResponderRuleDetails.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this UpdateTargetResponderRuleDetails.
        Execution Mode for ResponderRule


        :param mode: The mode of this UpdateTargetResponderRuleDetails.
        :type: str
        """
        allowed_values = ["AUTOACTION", "USERACTION"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            raise ValueError(
                "Invalid value for `mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._mode = mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
