# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_power_action_details import InstancePowerActionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SoftResetActionDetails(InstancePowerActionDetails):
    """
    Parameters for the softReset :func:`instance_action`. If omitted, default values are used.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SoftResetActionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.SoftResetActionDetails.action_type` attribute
        of this class is ``softreset`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this SoftResetActionDetails.
        :type action_type: str

        :param allow_dense_reboot_migration:
            The value to assign to the allow_dense_reboot_migration property of this SoftResetActionDetails.
        :type allow_dense_reboot_migration: bool

        """
        self.swagger_types = {
            'action_type': 'str',
            'allow_dense_reboot_migration': 'bool'
        }

        self.attribute_map = {
            'action_type': 'actionType',
            'allow_dense_reboot_migration': 'allowDenseRebootMigration'
        }

        self._action_type = None
        self._allow_dense_reboot_migration = None
        self._action_type = 'softreset'

    @property
    def allow_dense_reboot_migration(self):
        """
        Gets the allow_dense_reboot_migration of this SoftResetActionDetails.
        For instances that use a DenseIO shape, the flag denoting whether
        `reboot migration`__
        is performed for the instance. The default value is `false`.

        If the instance has a date in the Maintenance reboot field and you do nothing (or set this flag to `false`), the instance
        will be rebuilt at the scheduled maintenance time. The instance will experience 2-6 hours of downtime during the
        maintenance process. The local NVMe-based SSD will be preserved.

        If you want to minimize downtime and can delete the SSD, you can set this flag to `true` and proactively reboot the
        instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be
        deleted. A short downtime occurs during the migration.

        **Caution:** When `true`, the SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm#reboot


        :return: The allow_dense_reboot_migration of this SoftResetActionDetails.
        :rtype: bool
        """
        return self._allow_dense_reboot_migration

    @allow_dense_reboot_migration.setter
    def allow_dense_reboot_migration(self, allow_dense_reboot_migration):
        """
        Sets the allow_dense_reboot_migration of this SoftResetActionDetails.
        For instances that use a DenseIO shape, the flag denoting whether
        `reboot migration`__
        is performed for the instance. The default value is `false`.

        If the instance has a date in the Maintenance reboot field and you do nothing (or set this flag to `false`), the instance
        will be rebuilt at the scheduled maintenance time. The instance will experience 2-6 hours of downtime during the
        maintenance process. The local NVMe-based SSD will be preserved.

        If you want to minimize downtime and can delete the SSD, you can set this flag to `true` and proactively reboot the
        instance before the scheduled maintenance time. The instance will be reboot migrated to a healthy host and the SSD will be
        deleted. A short downtime occurs during the migration.

        **Caution:** When `true`, the SSD is permanently deleted. We recommend that you create a backup of the SSD before proceeding.

        __ https://docs.cloud.oracle.com/iaas/Content/Compute/References/infrastructure-maintenance.htm#reboot


        :param allow_dense_reboot_migration: The allow_dense_reboot_migration of this SoftResetActionDetails.
        :type: bool
        """
        self._allow_dense_reboot_migration = allow_dense_reboot_migration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
