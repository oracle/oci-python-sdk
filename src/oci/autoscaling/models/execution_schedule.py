# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecutionSchedule(object):
    """
    An execution schedule for an autoscaling policy.
    """

    #: A constant which can be used with the timezone property of a ExecutionSchedule.
    #: This constant has a value of "UTC"
    TIMEZONE_UTC = "UTC"

    def __init__(self, **kwargs):
        """
        Initializes a new ExecutionSchedule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.autoscaling.models.CronExecutionSchedule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ExecutionSchedule.
        :type type: str

        :param timezone:
            The value to assign to the timezone property of this ExecutionSchedule.
            Allowed values for this property are: "UTC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type timezone: str

        """
        self.swagger_types = {
            'type': 'str',
            'timezone': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'timezone': 'timezone'
        }

        self._type = None
        self._timezone = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'cron':
            return 'CronExecutionSchedule'
        else:
            return 'ExecutionSchedule'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ExecutionSchedule.
        The type of execution schedule.


        :return: The type of this ExecutionSchedule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ExecutionSchedule.
        The type of execution schedule.


        :param type: The type of this ExecutionSchedule.
        :type: str
        """
        self._type = type

    @property
    def timezone(self):
        """
        **[Required]** Gets the timezone of this ExecutionSchedule.
        The time zone for the execution schedule.

        Allowed values for this property are: "UTC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The timezone of this ExecutionSchedule.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this ExecutionSchedule.
        The time zone for the execution schedule.


        :param timezone: The timezone of this ExecutionSchedule.
        :type: str
        """
        allowed_values = ["UTC"]
        if not value_allowed_none_or_none_sentinel(timezone, allowed_values):
            timezone = 'UNKNOWN_ENUM_VALUE'
        self._timezone = timezone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
