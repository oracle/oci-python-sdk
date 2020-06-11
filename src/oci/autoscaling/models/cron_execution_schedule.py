# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .execution_schedule import ExecutionSchedule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CronExecutionSchedule(ExecutionSchedule):
    """
    Specifies the execution schedule of CRON type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CronExecutionSchedule object with values from keyword arguments. The default value of the :py:attr:`~oci.autoscaling.models.CronExecutionSchedule.type` attribute
        of this class is ``cron`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CronExecutionSchedule.
        :type type: str

        :param timezone:
            The value to assign to the timezone property of this CronExecutionSchedule.
            Allowed values for this property are: "UTC"
        :type timezone: str

        :param expression:
            The value to assign to the expression property of this CronExecutionSchedule.
        :type expression: str

        """
        self.swagger_types = {
            'type': 'str',
            'timezone': 'str',
            'expression': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'timezone': 'timezone',
            'expression': 'expression'
        }

        self._type = None
        self._timezone = None
        self._expression = None
        self._type = 'cron'

    @property
    def expression(self):
        """
        **[Required]** Gets the expression of this CronExecutionSchedule.
        The value representing the execution schedule, as defined by cron format.


        :return: The expression of this CronExecutionSchedule.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """
        Sets the expression of this CronExecutionSchedule.
        The value representing the execution schedule, as defined by cron format.


        :param expression: The expression of this CronExecutionSchedule.
        :type: str
        """
        self._expression = expression

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
