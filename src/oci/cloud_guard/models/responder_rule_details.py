# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResponderRuleDetails(object):
    """
    Details of ResponderRule.
    """

    #: A constant which can be used with the mode property of a ResponderRuleDetails.
    #: This constant has a value of "AUTOACTION"
    MODE_AUTOACTION = "AUTOACTION"

    #: A constant which can be used with the mode property of a ResponderRuleDetails.
    #: This constant has a value of "USERACTION"
    MODE_USERACTION = "USERACTION"

    def __init__(self, **kwargs):
        """
        Initializes a new ResponderRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition:
            The value to assign to the condition property of this ResponderRuleDetails.
        :type condition: oci.cloud_guard.models.Condition

        :param configurations:
            The value to assign to the configurations property of this ResponderRuleDetails.
        :type configurations: list[oci.cloud_guard.models.ResponderConfiguration]

        :param is_enabled:
            The value to assign to the is_enabled property of this ResponderRuleDetails.
        :type is_enabled: bool

        :param mode:
            The value to assign to the mode property of this ResponderRuleDetails.
            Allowed values for this property are: "AUTOACTION", "USERACTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        """
        self.swagger_types = {
            'condition': 'Condition',
            'configurations': 'list[ResponderConfiguration]',
            'is_enabled': 'bool',
            'mode': 'str'
        }

        self.attribute_map = {
            'condition': 'condition',
            'configurations': 'configurations',
            'is_enabled': 'isEnabled',
            'mode': 'mode'
        }

        self._condition = None
        self._configurations = None
        self._is_enabled = None
        self._mode = None

    @property
    def condition(self):
        """
        Gets the condition of this ResponderRuleDetails.

        :return: The condition of this ResponderRuleDetails.
        :rtype: oci.cloud_guard.models.Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this ResponderRuleDetails.

        :param condition: The condition of this ResponderRuleDetails.
        :type: oci.cloud_guard.models.Condition
        """
        self._condition = condition

    @property
    def configurations(self):
        """
        Gets the configurations of this ResponderRuleDetails.
        ResponderRule configurations


        :return: The configurations of this ResponderRuleDetails.
        :rtype: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this ResponderRuleDetails.
        ResponderRule configurations


        :param configurations: The configurations of this ResponderRuleDetails.
        :type: list[oci.cloud_guard.models.ResponderConfiguration]
        """
        self._configurations = configurations

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this ResponderRuleDetails.
        Identifies state for ResponderRule


        :return: The is_enabled of this ResponderRuleDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ResponderRuleDetails.
        Identifies state for ResponderRule


        :param is_enabled: The is_enabled of this ResponderRuleDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def mode(self):
        """
        Gets the mode of this ResponderRuleDetails.
        Execution Mode for ResponderRule

        Allowed values for this property are: "AUTOACTION", "USERACTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mode of this ResponderRuleDetails.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this ResponderRuleDetails.
        Execution Mode for ResponderRule


        :param mode: The mode of this ResponderRuleDetails.
        :type: str
        """
        allowed_values = ["AUTOACTION", "USERACTION"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            mode = 'UNKNOWN_ENUM_VALUE'
        self._mode = mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
