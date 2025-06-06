# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DefinedAlarmCondition(object):
    """
    Defined Alarm Condition.
    """

    #: A constant which can be used with the condition_type property of a DefinedAlarmCondition.
    #: This constant has a value of "FIXED"
    CONDITION_TYPE_FIXED = "FIXED"

    #: A constant which can be used with the condition_type property of a DefinedAlarmCondition.
    #: This constant has a value of "AVAILABILITY"
    CONDITION_TYPE_AVAILABILITY = "AVAILABILITY"

    def __init__(self, **kwargs):
        """
        Initializes a new DefinedAlarmCondition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this DefinedAlarmCondition.
        :type metric_name: str

        :param condition_type:
            The value to assign to the condition_type property of this DefinedAlarmCondition.
            Allowed values for this property are: "FIXED", "AVAILABILITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type condition_type: str

        :param conditions:
            The value to assign to the conditions property of this DefinedAlarmCondition.
        :type conditions: list[oci.stack_monitoring.models.Condition]

        """
        self.swagger_types = {
            'metric_name': 'str',
            'condition_type': 'str',
            'conditions': 'list[Condition]'
        }
        self.attribute_map = {
            'metric_name': 'metricName',
            'condition_type': 'conditionType',
            'conditions': 'conditions'
        }
        self._metric_name = None
        self._condition_type = None
        self._conditions = None

    @property
    def metric_name(self):
        """
        **[Required]** Gets the metric_name of this DefinedAlarmCondition.
        The metric name.


        :return: The metric_name of this DefinedAlarmCondition.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this DefinedAlarmCondition.
        The metric name.


        :param metric_name: The metric_name of this DefinedAlarmCondition.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def condition_type(self):
        """
        **[Required]** Gets the condition_type of this DefinedAlarmCondition.
        Type of defined monitoring template.

        Allowed values for this property are: "FIXED", "AVAILABILITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The condition_type of this DefinedAlarmCondition.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """
        Sets the condition_type of this DefinedAlarmCondition.
        Type of defined monitoring template.


        :param condition_type: The condition_type of this DefinedAlarmCondition.
        :type: str
        """
        allowed_values = ["FIXED", "AVAILABILITY"]
        if not value_allowed_none_or_none_sentinel(condition_type, allowed_values):
            condition_type = 'UNKNOWN_ENUM_VALUE'
        self._condition_type = condition_type

    @property
    def conditions(self):
        """
        **[Required]** Gets the conditions of this DefinedAlarmCondition.
        Monitoring template conditions.


        :return: The conditions of this DefinedAlarmCondition.
        :rtype: list[oci.stack_monitoring.models.Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this DefinedAlarmCondition.
        Monitoring template conditions.


        :param conditions: The conditions of this DefinedAlarmCondition.
        :type: list[oci.stack_monitoring.models.Condition]
        """
        self._conditions = conditions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
