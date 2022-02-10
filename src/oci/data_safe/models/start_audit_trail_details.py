# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StartAuditTrailDetails(object):
    """
    The details used to  start an audit trail.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StartAuditTrailDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_collection_start_time:
            The value to assign to the audit_collection_start_time property of this StartAuditTrailDetails.
        :type audit_collection_start_time: datetime

        :param is_auto_purge_enabled:
            The value to assign to the is_auto_purge_enabled property of this StartAuditTrailDetails.
        :type is_auto_purge_enabled: bool

        """
        self.swagger_types = {
            'audit_collection_start_time': 'datetime',
            'is_auto_purge_enabled': 'bool'
        }

        self.attribute_map = {
            'audit_collection_start_time': 'auditCollectionStartTime',
            'is_auto_purge_enabled': 'isAutoPurgeEnabled'
        }

        self._audit_collection_start_time = None
        self._is_auto_purge_enabled = None

    @property
    def audit_collection_start_time(self):
        """
        **[Required]** Gets the audit_collection_start_time of this StartAuditTrailDetails.
        The date from which the audit trail must start collecting data, in the format defined by RFC3339.


        :return: The audit_collection_start_time of this StartAuditTrailDetails.
        :rtype: datetime
        """
        return self._audit_collection_start_time

    @audit_collection_start_time.setter
    def audit_collection_start_time(self, audit_collection_start_time):
        """
        Sets the audit_collection_start_time of this StartAuditTrailDetails.
        The date from which the audit trail must start collecting data, in the format defined by RFC3339.


        :param audit_collection_start_time: The audit_collection_start_time of this StartAuditTrailDetails.
        :type: datetime
        """
        self._audit_collection_start_time = audit_collection_start_time

    @property
    def is_auto_purge_enabled(self):
        """
        Gets the is_auto_purge_enabled of this StartAuditTrailDetails.
        Indicates if auto purge is enabled on the target database, which helps delete audit data in the
        target database every seven days so that the database's audit trail does not become too large.


        :return: The is_auto_purge_enabled of this StartAuditTrailDetails.
        :rtype: bool
        """
        return self._is_auto_purge_enabled

    @is_auto_purge_enabled.setter
    def is_auto_purge_enabled(self, is_auto_purge_enabled):
        """
        Sets the is_auto_purge_enabled of this StartAuditTrailDetails.
        Indicates if auto purge is enabled on the target database, which helps delete audit data in the
        target database every seven days so that the database's audit trail does not become too large.


        :param is_auto_purge_enabled: The is_auto_purge_enabled of this StartAuditTrailDetails.
        :type: bool
        """
        self._is_auto_purge_enabled = is_auto_purge_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
