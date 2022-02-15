# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CalculateAuditVolumeAvailableDetails(object):
    """
    The details for calculating audit data volume on target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CalculateAuditVolumeAvailableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_collection_start_time:
            The value to assign to the audit_collection_start_time property of this CalculateAuditVolumeAvailableDetails.
        :type audit_collection_start_time: datetime

        :param trail_locations:
            The value to assign to the trail_locations property of this CalculateAuditVolumeAvailableDetails.
        :type trail_locations: list[str]

        """
        self.swagger_types = {
            'audit_collection_start_time': 'datetime',
            'trail_locations': 'list[str]'
        }

        self.attribute_map = {
            'audit_collection_start_time': 'auditCollectionStartTime',
            'trail_locations': 'trailLocations'
        }

        self._audit_collection_start_time = None
        self._trail_locations = None

    @property
    def audit_collection_start_time(self):
        """
        Gets the audit_collection_start_time of this CalculateAuditVolumeAvailableDetails.
        The date from which the audit trail must start collecting data in UTC, in the format defined by RFC3339. If not specified, this will default to the date based on the retention period.


        :return: The audit_collection_start_time of this CalculateAuditVolumeAvailableDetails.
        :rtype: datetime
        """
        return self._audit_collection_start_time

    @audit_collection_start_time.setter
    def audit_collection_start_time(self, audit_collection_start_time):
        """
        Sets the audit_collection_start_time of this CalculateAuditVolumeAvailableDetails.
        The date from which the audit trail must start collecting data in UTC, in the format defined by RFC3339. If not specified, this will default to the date based on the retention period.


        :param audit_collection_start_time: The audit_collection_start_time of this CalculateAuditVolumeAvailableDetails.
        :type: datetime
        """
        self._audit_collection_start_time = audit_collection_start_time

    @property
    def trail_locations(self):
        """
        **[Required]** Gets the trail_locations of this CalculateAuditVolumeAvailableDetails.
        The trail locations for which the audit data volume has to be calculated.


        :return: The trail_locations of this CalculateAuditVolumeAvailableDetails.
        :rtype: list[str]
        """
        return self._trail_locations

    @trail_locations.setter
    def trail_locations(self, trail_locations):
        """
        Sets the trail_locations of this CalculateAuditVolumeAvailableDetails.
        The trail locations for which the audit data volume has to be calculated.


        :param trail_locations: The trail_locations of this CalculateAuditVolumeAvailableDetails.
        :type: list[str]
        """
        self._trail_locations = trail_locations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
