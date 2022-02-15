# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailableAuditVolumeSummary(object):
    """
    Represents the audit data volume collected by Data Safe from the target database for the specified audit profile.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailableAuditVolumeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_profile_id:
            The value to assign to the audit_profile_id property of this AvailableAuditVolumeSummary.
        :type audit_profile_id: str

        :param trail_location:
            The value to assign to the trail_location property of this AvailableAuditVolumeSummary.
        :type trail_location: str

        :param month_in_consideration:
            The value to assign to the month_in_consideration property of this AvailableAuditVolumeSummary.
        :type month_in_consideration: datetime

        :param volume:
            The value to assign to the volume property of this AvailableAuditVolumeSummary.
        :type volume: int

        """
        self.swagger_types = {
            'audit_profile_id': 'str',
            'trail_location': 'str',
            'month_in_consideration': 'datetime',
            'volume': 'int'
        }

        self.attribute_map = {
            'audit_profile_id': 'auditProfileId',
            'trail_location': 'trailLocation',
            'month_in_consideration': 'monthInConsideration',
            'volume': 'volume'
        }

        self._audit_profile_id = None
        self._trail_location = None
        self._month_in_consideration = None
        self._volume = None

    @property
    def audit_profile_id(self):
        """
        **[Required]** Gets the audit_profile_id of this AvailableAuditVolumeSummary.
        The OCID of the audit profile resource.


        :return: The audit_profile_id of this AvailableAuditVolumeSummary.
        :rtype: str
        """
        return self._audit_profile_id

    @audit_profile_id.setter
    def audit_profile_id(self, audit_profile_id):
        """
        Sets the audit_profile_id of this AvailableAuditVolumeSummary.
        The OCID of the audit profile resource.


        :param audit_profile_id: The audit_profile_id of this AvailableAuditVolumeSummary.
        :type: str
        """
        self._audit_profile_id = audit_profile_id

    @property
    def trail_location(self):
        """
        **[Required]** Gets the trail_location of this AvailableAuditVolumeSummary.
        Audit trail location on the target database from where the audit data is being collected by Data Safe.


        :return: The trail_location of this AvailableAuditVolumeSummary.
        :rtype: str
        """
        return self._trail_location

    @trail_location.setter
    def trail_location(self, trail_location):
        """
        Sets the trail_location of this AvailableAuditVolumeSummary.
        Audit trail location on the target database from where the audit data is being collected by Data Safe.


        :param trail_location: The trail_location of this AvailableAuditVolumeSummary.
        :type: str
        """
        self._trail_location = trail_location

    @property
    def month_in_consideration(self):
        """
        **[Required]** Gets the month_in_consideration of this AvailableAuditVolumeSummary.
        Represents the month under consideration for which aggregated audit data volume available at the target is computed.
        This field will be the UTC start of the day of the first day of the month for which the aggregate count corresponds to, in the format defined by RFC3339..
        For instance, the value of 01-01-2021T00:00:00Z represents Jan 2021.


        :return: The month_in_consideration of this AvailableAuditVolumeSummary.
        :rtype: datetime
        """
        return self._month_in_consideration

    @month_in_consideration.setter
    def month_in_consideration(self, month_in_consideration):
        """
        Sets the month_in_consideration of this AvailableAuditVolumeSummary.
        Represents the month under consideration for which aggregated audit data volume available at the target is computed.
        This field will be the UTC start of the day of the first day of the month for which the aggregate count corresponds to, in the format defined by RFC3339..
        For instance, the value of 01-01-2021T00:00:00Z represents Jan 2021.


        :param month_in_consideration: The month_in_consideration of this AvailableAuditVolumeSummary.
        :type: datetime
        """
        self._month_in_consideration = month_in_consideration

    @property
    def volume(self):
        """
        **[Required]** Gets the volume of this AvailableAuditVolumeSummary.
        Represents the aggregated audit data volume available in the audit trails on the target database which is yet to be collected by Data Safe for the specified month.


        :return: The volume of this AvailableAuditVolumeSummary.
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """
        Sets the volume of this AvailableAuditVolumeSummary.
        Represents the aggregated audit data volume available in the audit trails on the target database which is yet to be collected by Data Safe for the specified month.


        :param volume: The volume of this AvailableAuditVolumeSummary.
        :type: int
        """
        self._volume = volume

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
