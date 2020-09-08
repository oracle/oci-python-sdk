# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMaintenanceRunDetails(object):
    """
    Describes the modification parameters for the maintenance run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMaintenanceRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateMaintenanceRunDetails.
        :type is_enabled: bool

        :param time_scheduled:
            The value to assign to the time_scheduled property of this UpdateMaintenanceRunDetails.
        :type time_scheduled: datetime

        :param is_patch_now_enabled:
            The value to assign to the is_patch_now_enabled property of this UpdateMaintenanceRunDetails.
        :type is_patch_now_enabled: bool

        :param patch_id:
            The value to assign to the patch_id property of this UpdateMaintenanceRunDetails.
        :type patch_id: str

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'time_scheduled': 'datetime',
            'is_patch_now_enabled': 'bool',
            'patch_id': 'str'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'time_scheduled': 'timeScheduled',
            'is_patch_now_enabled': 'isPatchNowEnabled',
            'patch_id': 'patchId'
        }

        self._is_enabled = None
        self._time_scheduled = None
        self._is_patch_now_enabled = None
        self._patch_id = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateMaintenanceRunDetails.
        If `FALSE`, skips the maintenance run.


        :return: The is_enabled of this UpdateMaintenanceRunDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateMaintenanceRunDetails.
        If `FALSE`, skips the maintenance run.


        :param is_enabled: The is_enabled of this UpdateMaintenanceRunDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def time_scheduled(self):
        """
        Gets the time_scheduled of this UpdateMaintenanceRunDetails.
        The scheduled date and time of the maintenance run to update.


        :return: The time_scheduled of this UpdateMaintenanceRunDetails.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this UpdateMaintenanceRunDetails.
        The scheduled date and time of the maintenance run to update.


        :param time_scheduled: The time_scheduled of this UpdateMaintenanceRunDetails.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    @property
    def is_patch_now_enabled(self):
        """
        Gets the is_patch_now_enabled of this UpdateMaintenanceRunDetails.
        If set to `TRUE`, starts patching immediately.


        :return: The is_patch_now_enabled of this UpdateMaintenanceRunDetails.
        :rtype: bool
        """
        return self._is_patch_now_enabled

    @is_patch_now_enabled.setter
    def is_patch_now_enabled(self, is_patch_now_enabled):
        """
        Sets the is_patch_now_enabled of this UpdateMaintenanceRunDetails.
        If set to `TRUE`, starts patching immediately.


        :param is_patch_now_enabled: The is_patch_now_enabled of this UpdateMaintenanceRunDetails.
        :type: bool
        """
        self._is_patch_now_enabled = is_patch_now_enabled

    @property
    def patch_id(self):
        """
        Gets the patch_id of this UpdateMaintenanceRunDetails.
        The `OCID`__ of the patch to be applied in the maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The patch_id of this UpdateMaintenanceRunDetails.
        :rtype: str
        """
        return self._patch_id

    @patch_id.setter
    def patch_id(self, patch_id):
        """
        Sets the patch_id of this UpdateMaintenanceRunDetails.
        The `OCID`__ of the patch to be applied in the maintenance run.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param patch_id: The patch_id of this UpdateMaintenanceRunDetails.
        :type: str
        """
        self._patch_id = patch_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
