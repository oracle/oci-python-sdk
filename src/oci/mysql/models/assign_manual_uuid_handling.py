# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190415

from .anonymous_transactions_handling import AnonymousTransactionsHandling
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssignManualUuidHandling(AnonymousTransactionsHandling):
    """
    Enables assignment of IDs on the target to anonymous transactions coming from the source. A manually defined UUID
    is added as a prefix to the ID.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssignManualUuidHandling object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.AssignManualUuidHandling.policy` attribute
        of this class is ``ASSIGN_MANUAL_UUID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param policy:
            The value to assign to the policy property of this AssignManualUuidHandling.
            Allowed values for this property are: "ERROR_ON_ANONYMOUS", "ASSIGN_TARGET_UUID", "ASSIGN_MANUAL_UUID"
        :type policy: str

        :param last_configured_log_filename:
            The value to assign to the last_configured_log_filename property of this AssignManualUuidHandling.
        :type last_configured_log_filename: str

        :param last_configured_log_offset:
            The value to assign to the last_configured_log_offset property of this AssignManualUuidHandling.
        :type last_configured_log_offset: int

        :param uuid:
            The value to assign to the uuid property of this AssignManualUuidHandling.
        :type uuid: str

        """
        self.swagger_types = {
            'policy': 'str',
            'last_configured_log_filename': 'str',
            'last_configured_log_offset': 'int',
            'uuid': 'str'
        }
        self.attribute_map = {
            'policy': 'policy',
            'last_configured_log_filename': 'lastConfiguredLogFilename',
            'last_configured_log_offset': 'lastConfiguredLogOffset',
            'uuid': 'uuid'
        }
        self._policy = None
        self._last_configured_log_filename = None
        self._last_configured_log_offset = None
        self._uuid = None
        self._policy = 'ASSIGN_MANUAL_UUID'

    @property
    def last_configured_log_filename(self):
        """
        Gets the last_configured_log_filename of this AssignManualUuidHandling.
        Specifies one of the coordinates (file) at which the replica should begin
        reading the source's log. As this value specifies the point where replication
        starts from, it is only used once, when it starts. It is never used again,
        unless a new UpdateChannel operation modifies it.


        :return: The last_configured_log_filename of this AssignManualUuidHandling.
        :rtype: str
        """
        return self._last_configured_log_filename

    @last_configured_log_filename.setter
    def last_configured_log_filename(self, last_configured_log_filename):
        """
        Sets the last_configured_log_filename of this AssignManualUuidHandling.
        Specifies one of the coordinates (file) at which the replica should begin
        reading the source's log. As this value specifies the point where replication
        starts from, it is only used once, when it starts. It is never used again,
        unless a new UpdateChannel operation modifies it.


        :param last_configured_log_filename: The last_configured_log_filename of this AssignManualUuidHandling.
        :type: str
        """
        self._last_configured_log_filename = last_configured_log_filename

    @property
    def last_configured_log_offset(self):
        """
        Gets the last_configured_log_offset of this AssignManualUuidHandling.
        Specifies one of the coordinates (offset) at which the replica should begin
        reading the source's log. As this value specifies the point where replication
        starts from, it is only used once, when it starts. It is never used again,
        unless a new UpdateChannel operation modifies it.


        :return: The last_configured_log_offset of this AssignManualUuidHandling.
        :rtype: int
        """
        return self._last_configured_log_offset

    @last_configured_log_offset.setter
    def last_configured_log_offset(self, last_configured_log_offset):
        """
        Sets the last_configured_log_offset of this AssignManualUuidHandling.
        Specifies one of the coordinates (offset) at which the replica should begin
        reading the source's log. As this value specifies the point where replication
        starts from, it is only used once, when it starts. It is never used again,
        unless a new UpdateChannel operation modifies it.


        :param last_configured_log_offset: The last_configured_log_offset of this AssignManualUuidHandling.
        :type: int
        """
        self._last_configured_log_offset = last_configured_log_offset

    @property
    def uuid(self):
        """
        Gets the uuid of this AssignManualUuidHandling.
        The UUID that is used as a prefix when generating transaction identifiers for anonymous transactions
        coming from the source. You can change the UUID later.


        :return: The uuid of this AssignManualUuidHandling.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this AssignManualUuidHandling.
        The UUID that is used as a prefix when generating transaction identifiers for anonymous transactions
        coming from the source. You can change the UUID later.


        :param uuid: The uuid of this AssignManualUuidHandling.
        :type: str
        """
        self._uuid = uuid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
