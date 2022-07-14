# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FamilyMaintenancePolicy(object):
    """
    The policy that specifies the maintenance and upgrade preferences for an environment. For more information about the options, see `Understanding Environment Maintenance`__.

    __ https://docs.cloud.oracle.com/iaas/Content/fusion-applications/plan-environment-family.htm#about-env-maintenance
    """

    #: A constant which can be used with the concurrent_maintenance property of a FamilyMaintenancePolicy.
    #: This constant has a value of "PROD"
    CONCURRENT_MAINTENANCE_PROD = "PROD"

    #: A constant which can be used with the concurrent_maintenance property of a FamilyMaintenancePolicy.
    #: This constant has a value of "NON_PROD"
    CONCURRENT_MAINTENANCE_NON_PROD = "NON_PROD"

    #: A constant which can be used with the concurrent_maintenance property of a FamilyMaintenancePolicy.
    #: This constant has a value of "DISABLED"
    CONCURRENT_MAINTENANCE_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new FamilyMaintenancePolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param quarterly_upgrade_begin_times:
            The value to assign to the quarterly_upgrade_begin_times property of this FamilyMaintenancePolicy.
        :type quarterly_upgrade_begin_times: str

        :param is_monthly_patching_enabled:
            The value to assign to the is_monthly_patching_enabled property of this FamilyMaintenancePolicy.
        :type is_monthly_patching_enabled: bool

        :param concurrent_maintenance:
            The value to assign to the concurrent_maintenance property of this FamilyMaintenancePolicy.
            Allowed values for this property are: "PROD", "NON_PROD", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type concurrent_maintenance: str

        """
        self.swagger_types = {
            'quarterly_upgrade_begin_times': 'str',
            'is_monthly_patching_enabled': 'bool',
            'concurrent_maintenance': 'str'
        }

        self.attribute_map = {
            'quarterly_upgrade_begin_times': 'quarterlyUpgradeBeginTimes',
            'is_monthly_patching_enabled': 'isMonthlyPatchingEnabled',
            'concurrent_maintenance': 'concurrentMaintenance'
        }

        self._quarterly_upgrade_begin_times = None
        self._is_monthly_patching_enabled = None
        self._concurrent_maintenance = None

    @property
    def quarterly_upgrade_begin_times(self):
        """
        Gets the quarterly_upgrade_begin_times of this FamilyMaintenancePolicy.
        The quarterly maintenance month group schedule of the Fusion environment family.


        :return: The quarterly_upgrade_begin_times of this FamilyMaintenancePolicy.
        :rtype: str
        """
        return self._quarterly_upgrade_begin_times

    @quarterly_upgrade_begin_times.setter
    def quarterly_upgrade_begin_times(self, quarterly_upgrade_begin_times):
        """
        Sets the quarterly_upgrade_begin_times of this FamilyMaintenancePolicy.
        The quarterly maintenance month group schedule of the Fusion environment family.


        :param quarterly_upgrade_begin_times: The quarterly_upgrade_begin_times of this FamilyMaintenancePolicy.
        :type: str
        """
        self._quarterly_upgrade_begin_times = quarterly_upgrade_begin_times

    @property
    def is_monthly_patching_enabled(self):
        """
        Gets the is_monthly_patching_enabled of this FamilyMaintenancePolicy.
        When True, monthly patching is enabled for the environment family.


        :return: The is_monthly_patching_enabled of this FamilyMaintenancePolicy.
        :rtype: bool
        """
        return self._is_monthly_patching_enabled

    @is_monthly_patching_enabled.setter
    def is_monthly_patching_enabled(self, is_monthly_patching_enabled):
        """
        Sets the is_monthly_patching_enabled of this FamilyMaintenancePolicy.
        When True, monthly patching is enabled for the environment family.


        :param is_monthly_patching_enabled: The is_monthly_patching_enabled of this FamilyMaintenancePolicy.
        :type: bool
        """
        self._is_monthly_patching_enabled = is_monthly_patching_enabled

    @property
    def concurrent_maintenance(self):
        """
        Gets the concurrent_maintenance of this FamilyMaintenancePolicy.
        Option to upgrade both production and non-production environments at the same time. When set to PROD both types of environnments are upgraded on the production schedule. When set to NON_PROD both types of environments are upgraded on the non-production schedule.

        Allowed values for this property are: "PROD", "NON_PROD", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The concurrent_maintenance of this FamilyMaintenancePolicy.
        :rtype: str
        """
        return self._concurrent_maintenance

    @concurrent_maintenance.setter
    def concurrent_maintenance(self, concurrent_maintenance):
        """
        Sets the concurrent_maintenance of this FamilyMaintenancePolicy.
        Option to upgrade both production and non-production environments at the same time. When set to PROD both types of environnments are upgraded on the production schedule. When set to NON_PROD both types of environments are upgraded on the non-production schedule.


        :param concurrent_maintenance: The concurrent_maintenance of this FamilyMaintenancePolicy.
        :type: str
        """
        allowed_values = ["PROD", "NON_PROD", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(concurrent_maintenance, allowed_values):
            concurrent_maintenance = 'UNKNOWN_ENUM_VALUE'
        self._concurrent_maintenance = concurrent_maintenance

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
