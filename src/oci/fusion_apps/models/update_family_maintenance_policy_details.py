# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFamilyMaintenancePolicyDetails(object):
    """
    The editable settings of the policy that specifies the maintenance and upgrade preferences for an environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFamilyMaintenancePolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_monthly_patching_enabled:
            The value to assign to the is_monthly_patching_enabled property of this UpdateFamilyMaintenancePolicyDetails.
        :type is_monthly_patching_enabled: bool

        :param concurrent_maintenance:
            The value to assign to the concurrent_maintenance property of this UpdateFamilyMaintenancePolicyDetails.
        :type concurrent_maintenance: str

        """
        self.swagger_types = {
            'is_monthly_patching_enabled': 'bool',
            'concurrent_maintenance': 'str'
        }

        self.attribute_map = {
            'is_monthly_patching_enabled': 'isMonthlyPatchingEnabled',
            'concurrent_maintenance': 'concurrentMaintenance'
        }

        self._is_monthly_patching_enabled = None
        self._concurrent_maintenance = None

    @property
    def is_monthly_patching_enabled(self):
        """
        Gets the is_monthly_patching_enabled of this UpdateFamilyMaintenancePolicyDetails.
        Whether the Fusion environment receives monthly patching.


        :return: The is_monthly_patching_enabled of this UpdateFamilyMaintenancePolicyDetails.
        :rtype: bool
        """
        return self._is_monthly_patching_enabled

    @is_monthly_patching_enabled.setter
    def is_monthly_patching_enabled(self, is_monthly_patching_enabled):
        """
        Sets the is_monthly_patching_enabled of this UpdateFamilyMaintenancePolicyDetails.
        Whether the Fusion environment receives monthly patching.


        :param is_monthly_patching_enabled: The is_monthly_patching_enabled of this UpdateFamilyMaintenancePolicyDetails.
        :type: bool
        """
        self._is_monthly_patching_enabled = is_monthly_patching_enabled

    @property
    def concurrent_maintenance(self):
        """
        Gets the concurrent_maintenance of this UpdateFamilyMaintenancePolicyDetails.
        Whether production and non-production environments are upgraded concurrently.


        :return: The concurrent_maintenance of this UpdateFamilyMaintenancePolicyDetails.
        :rtype: str
        """
        return self._concurrent_maintenance

    @concurrent_maintenance.setter
    def concurrent_maintenance(self, concurrent_maintenance):
        """
        Sets the concurrent_maintenance of this UpdateFamilyMaintenancePolicyDetails.
        Whether production and non-production environments are upgraded concurrently.


        :param concurrent_maintenance: The concurrent_maintenance of this UpdateFamilyMaintenancePolicyDetails.
        :type: str
        """
        self._concurrent_maintenance = concurrent_maintenance

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
