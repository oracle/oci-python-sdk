# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectorDetails(object):
    """
    Details of a Detector Rule
    """

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "CRITICAL"
    RISK_LEVEL_CRITICAL = "CRITICAL"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "HIGH"
    RISK_LEVEL_HIGH = "HIGH"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "MEDIUM"
    RISK_LEVEL_MEDIUM = "MEDIUM"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "LOW"
    RISK_LEVEL_LOW = "LOW"

    #: A constant which can be used with the risk_level property of a DetectorDetails.
    #: This constant has a value of "MINOR"
    RISK_LEVEL_MINOR = "MINOR"

    def __init__(self, **kwargs):
        """
        Initializes a new DetectorDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this DetectorDetails.
        :type is_enabled: bool

        :param risk_level:
            The value to assign to the risk_level property of this DetectorDetails.
            Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type risk_level: str

        :param configurations:
            The value to assign to the configurations property of this DetectorDetails.
        :type configurations: list[DetectorConfiguration]

        :param condition:
            The value to assign to the condition property of this DetectorDetails.
        :type condition: Condition

        :param labels:
            The value to assign to the labels property of this DetectorDetails.
        :type labels: list[str]

        :param is_configuration_allowed:
            The value to assign to the is_configuration_allowed property of this DetectorDetails.
        :type is_configuration_allowed: bool

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'risk_level': 'str',
            'configurations': 'list[DetectorConfiguration]',
            'condition': 'Condition',
            'labels': 'list[str]',
            'is_configuration_allowed': 'bool'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'risk_level': 'riskLevel',
            'configurations': 'configurations',
            'condition': 'condition',
            'labels': 'labels',
            'is_configuration_allowed': 'isConfigurationAllowed'
        }

        self._is_enabled = None
        self._risk_level = None
        self._configurations = None
        self._condition = None
        self._labels = None
        self._is_configuration_allowed = None

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this DetectorDetails.
        Enables the control


        :return: The is_enabled of this DetectorDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DetectorDetails.
        Enables the control


        :param is_enabled: The is_enabled of this DetectorDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def risk_level(self):
        """
        **[Required]** Gets the risk_level of this DetectorDetails.
        The Risk Level

        Allowed values for this property are: "CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The risk_level of this DetectorDetails.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this DetectorDetails.
        The Risk Level


        :param risk_level: The risk_level of this DetectorDetails.
        :type: str
        """
        allowed_values = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]
        if not value_allowed_none_or_none_sentinel(risk_level, allowed_values):
            risk_level = 'UNKNOWN_ENUM_VALUE'
        self._risk_level = risk_level

    @property
    def configurations(self):
        """
        Gets the configurations of this DetectorDetails.
        Configuration details


        :return: The configurations of this DetectorDetails.
        :rtype: list[DetectorConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this DetectorDetails.
        Configuration details


        :param configurations: The configurations of this DetectorDetails.
        :type: list[DetectorConfiguration]
        """
        self._configurations = configurations

    @property
    def condition(self):
        """
        Gets the condition of this DetectorDetails.

        :return: The condition of this DetectorDetails.
        :rtype: Condition
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this DetectorDetails.

        :param condition: The condition of this DetectorDetails.
        :type: Condition
        """
        self._condition = condition

    @property
    def labels(self):
        """
        Gets the labels of this DetectorDetails.
        user defined labels for a detector rule


        :return: The labels of this DetectorDetails.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this DetectorDetails.
        user defined labels for a detector rule


        :param labels: The labels of this DetectorDetails.
        :type: list[str]
        """
        self._labels = labels

    @property
    def is_configuration_allowed(self):
        """
        Gets the is_configuration_allowed of this DetectorDetails.
        configuration allowed or not


        :return: The is_configuration_allowed of this DetectorDetails.
        :rtype: bool
        """
        return self._is_configuration_allowed

    @is_configuration_allowed.setter
    def is_configuration_allowed(self, is_configuration_allowed):
        """
        Sets the is_configuration_allowed of this DetectorDetails.
        configuration allowed or not


        :param is_configuration_allowed: The is_configuration_allowed of this DetectorDetails.
        :type: bool
        """
        self._is_configuration_allowed = is_configuration_allowed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
