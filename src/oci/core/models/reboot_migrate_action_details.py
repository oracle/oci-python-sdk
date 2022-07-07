# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_power_action_details import InstancePowerActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RebootMigrateActionDetails(InstancePowerActionDetails):
    """
    Parameters for the rebootMigrate :func:`instance_action`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RebootMigrateActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.RebootMigrateActionDetails.action_type` attribute
        of this class is ``rebootMigrate`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this RebootMigrateActionDetails.
        :type action_type: str

        :param delete_local_storage:
            The value to assign to the delete_local_storage property of this RebootMigrateActionDetails.
        :type delete_local_storage: bool

        :param time_scheduled:
            The value to assign to the time_scheduled property of this RebootMigrateActionDetails.
        :type time_scheduled: datetime

        """
        self.swagger_types = {
            'action_type': 'str',
            'delete_local_storage': 'bool',
            'time_scheduled': 'datetime'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'delete_local_storage': 'deleteLocalStorage',
            'time_scheduled': 'timeScheduled'
        }

        self._action_type = None
        self._delete_local_storage = None
        self._time_scheduled = None
        self._action_type = 'rebootMigrate'

    @property
    def delete_local_storage(self):
        """
        Gets the delete_local_storage of this RebootMigrateActionDetails.
        For bare metal instances that have local storage, this must be set to true to verify that the local storage
        will be deleted during the migration.  For instances without, this parameter has no effect.


        :return: The delete_local_storage of this RebootMigrateActionDetails.
        :rtype: bool
        """
        return self._delete_local_storage

    @delete_local_storage.setter
    def delete_local_storage(self, delete_local_storage):
        """
        Sets the delete_local_storage of this RebootMigrateActionDetails.
        For bare metal instances that have local storage, this must be set to true to verify that the local storage
        will be deleted during the migration.  For instances without, this parameter has no effect.


        :param delete_local_storage: The delete_local_storage of this RebootMigrateActionDetails.
        :type: bool
        """
        self._delete_local_storage = delete_local_storage

    @property
    def time_scheduled(self):
        """
        Gets the time_scheduled of this RebootMigrateActionDetails.
        If present, this parameter will set (or re-set) the scheduled time that the instance will be reboot
        migrated in the format defined by `RFC3339`__.  This will also change
        the timeRebootMigrationDue field on the instance.
        If not present, the reboot migration will be triggered immediately.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_scheduled of this RebootMigrateActionDetails.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this RebootMigrateActionDetails.
        If present, this parameter will set (or re-set) the scheduled time that the instance will be reboot
        migrated in the format defined by `RFC3339`__.  This will also change
        the timeRebootMigrationDue field on the instance.
        If not present, the reboot migration will be triggered immediately.

        __ https://tools.ietf.org/html/rfc3339


        :param time_scheduled: The time_scheduled of this RebootMigrateActionDetails.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
