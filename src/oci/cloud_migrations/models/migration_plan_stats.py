# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MigrationPlanStats(object):
    """
    Status of the migration plan.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MigrationPlanStats object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_estimated_cost:
            The value to assign to the total_estimated_cost property of this MigrationPlanStats.
        :type total_estimated_cost: oci.cloud_migrations.models.CostEstimation

        :param time_updated:
            The value to assign to the time_updated property of this MigrationPlanStats.
        :type time_updated: datetime

        :param vm_count:
            The value to assign to the vm_count property of this MigrationPlanStats.
        :type vm_count: int

        """
        self.swagger_types = {
            'total_estimated_cost': 'CostEstimation',
            'time_updated': 'datetime',
            'vm_count': 'int'
        }

        self.attribute_map = {
            'total_estimated_cost': 'totalEstimatedCost',
            'time_updated': 'timeUpdated',
            'vm_count': 'vmCount'
        }

        self._total_estimated_cost = None
        self._time_updated = None
        self._vm_count = None

    @property
    def total_estimated_cost(self):
        """
        Gets the total_estimated_cost of this MigrationPlanStats.

        :return: The total_estimated_cost of this MigrationPlanStats.
        :rtype: oci.cloud_migrations.models.CostEstimation
        """
        return self._total_estimated_cost

    @total_estimated_cost.setter
    def total_estimated_cost(self, total_estimated_cost):
        """
        Sets the total_estimated_cost of this MigrationPlanStats.

        :param total_estimated_cost: The total_estimated_cost of this MigrationPlanStats.
        :type: oci.cloud_migrations.models.CostEstimation
        """
        self._total_estimated_cost = total_estimated_cost

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MigrationPlanStats.
        The time when the migration plan was calculated. An RFC3339 formatted datetime string.


        :return: The time_updated of this MigrationPlanStats.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MigrationPlanStats.
        The time when the migration plan was calculated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MigrationPlanStats.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def vm_count(self):
        """
        Gets the vm_count of this MigrationPlanStats.
        The total count of VMs in migration


        :return: The vm_count of this MigrationPlanStats.
        :rtype: int
        """
        return self._vm_count

    @vm_count.setter
    def vm_count(self, vm_count):
        """
        Sets the vm_count of this MigrationPlanStats.
        The total count of VMs in migration


        :param vm_count: The vm_count of this MigrationPlanStats.
        :type: int
        """
        self._vm_count = vm_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
