# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Schedule(object):
    """
    Schedule for scheduled task.
    """

    #: A constant which can be used with the type property of a Schedule.
    #: This constant has a value of "FIXED_FREQUENCY"
    TYPE_FIXED_FREQUENCY = "FIXED_FREQUENCY"

    #: A constant which can be used with the type property of a Schedule.
    #: This constant has a value of "CRON"
    TYPE_CRON = "CRON"

    #: A constant which can be used with the misfire_policy property of a Schedule.
    #: This constant has a value of "RETRY_ONCE"
    MISFIRE_POLICY_RETRY_ONCE = "RETRY_ONCE"

    #: A constant which can be used with the misfire_policy property of a Schedule.
    #: This constant has a value of "RETRY_INDEFINITELY"
    MISFIRE_POLICY_RETRY_INDEFINITELY = "RETRY_INDEFINITELY"

    #: A constant which can be used with the misfire_policy property of a Schedule.
    #: This constant has a value of "SKIP"
    MISFIRE_POLICY_SKIP = "SKIP"

    def __init__(self, **kwargs):
        """
        Initializes a new Schedule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.log_analytics.models.CronSchedule`
        * :class:`~oci.log_analytics.models.FixedFrequencySchedule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Schedule.
            Allowed values for this property are: "FIXED_FREQUENCY", "CRON", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param misfire_policy:
            The value to assign to the misfire_policy property of this Schedule.
            Allowed values for this property are: "RETRY_ONCE", "RETRY_INDEFINITELY", "SKIP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type misfire_policy: str

        """
        self.swagger_types = {
            'type': 'str',
            'misfire_policy': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'misfire_policy': 'misfirePolicy'
        }

        self._type = None
        self._misfire_policy = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'CRON':
            return 'CronSchedule'

        if type == 'FIXED_FREQUENCY':
            return 'FixedFrequencySchedule'
        else:
            return 'Schedule'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Schedule.
        Schedule type discriminator.

        Allowed values for this property are: "FIXED_FREQUENCY", "CRON", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Schedule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Schedule.
        Schedule type discriminator.


        :param type: The type of this Schedule.
        :type: str
        """
        allowed_values = ["FIXED_FREQUENCY", "CRON"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def misfire_policy(self):
        """
        Gets the misfire_policy of this Schedule.
        Schedule misfire retry policy.

        Allowed values for this property are: "RETRY_ONCE", "RETRY_INDEFINITELY", "SKIP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The misfire_policy of this Schedule.
        :rtype: str
        """
        return self._misfire_policy

    @misfire_policy.setter
    def misfire_policy(self, misfire_policy):
        """
        Sets the misfire_policy of this Schedule.
        Schedule misfire retry policy.


        :param misfire_policy: The misfire_policy of this Schedule.
        :type: str
        """
        allowed_values = ["RETRY_ONCE", "RETRY_INDEFINITELY", "SKIP"]
        if not value_allowed_none_or_none_sentinel(misfire_policy, allowed_values):
            misfire_policy = 'UNKNOWN_ENUM_VALUE'
        self._misfire_policy = misfire_policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
