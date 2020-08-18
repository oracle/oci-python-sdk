# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAvailabilityConfig(object):
    """
    Options for customers to define the general policy of how compute service perform maintenance on VM instances.
    """

    #: A constant which can be used with the recovery_action property of a InstanceAvailabilityConfig.
    #: This constant has a value of "RESTORE_INSTANCE"
    RECOVERY_ACTION_RESTORE_INSTANCE = "RESTORE_INSTANCE"

    #: A constant which can be used with the recovery_action property of a InstanceAvailabilityConfig.
    #: This constant has a value of "STOP_INSTANCE"
    RECOVERY_ACTION_STOP_INSTANCE = "STOP_INSTANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAvailabilityConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param recovery_action:
            The value to assign to the recovery_action property of this InstanceAvailabilityConfig.
            Allowed values for this property are: "RESTORE_INSTANCE", "STOP_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type recovery_action: str

        """
        self.swagger_types = {
            'recovery_action': 'str'
        }

        self.attribute_map = {
            'recovery_action': 'recoveryAction'
        }

        self._recovery_action = None

    @property
    def recovery_action(self):
        """
        Gets the recovery_action of this InstanceAvailabilityConfig.
        Actions customers can specify that would be applied to their instances after scheduled or unexpected host maintenance.
        * `RESTORE_INSTANCE` - This would be the default action if recoveryAction is not set. VM instances
        will be restored to the power state it was in before maintenance.
        * `STOP_INSTANCE` - This action allow customers to have their VM instances be stopped after maintenance.

        Allowed values for this property are: "RESTORE_INSTANCE", "STOP_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The recovery_action of this InstanceAvailabilityConfig.
        :rtype: str
        """
        return self._recovery_action

    @recovery_action.setter
    def recovery_action(self, recovery_action):
        """
        Sets the recovery_action of this InstanceAvailabilityConfig.
        Actions customers can specify that would be applied to their instances after scheduled or unexpected host maintenance.
        * `RESTORE_INSTANCE` - This would be the default action if recoveryAction is not set. VM instances
        will be restored to the power state it was in before maintenance.
        * `STOP_INSTANCE` - This action allow customers to have their VM instances be stopped after maintenance.


        :param recovery_action: The recovery_action of this InstanceAvailabilityConfig.
        :type: str
        """
        allowed_values = ["RESTORE_INSTANCE", "STOP_INSTANCE"]
        if not value_allowed_none_or_none_sentinel(recovery_action, allowed_values):
            recovery_action = 'UNKNOWN_ENUM_VALUE'
        self._recovery_action = recovery_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
