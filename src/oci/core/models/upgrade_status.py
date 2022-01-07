# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpgradeStatus(object):
    """
    The upgrade status of a DRG.
    """

    #: A constant which can be used with the status property of a UpgradeStatus.
    #: This constant has a value of "NOT_UPGRADED"
    STATUS_NOT_UPGRADED = "NOT_UPGRADED"

    #: A constant which can be used with the status property of a UpgradeStatus.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the status property of a UpgradeStatus.
    #: This constant has a value of "UPGRADED"
    STATUS_UPGRADED = "UPGRADED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpgradeStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param drg_id:
            The value to assign to the drg_id property of this UpgradeStatus.
        :type drg_id: str

        :param status:
            The value to assign to the status property of this UpgradeStatus.
            Allowed values for this property are: "NOT_UPGRADED", "IN_PROGRESS", "UPGRADED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param upgraded_connections:
            The value to assign to the upgraded_connections property of this UpgradeStatus.
        :type upgraded_connections: str

        """
        self.swagger_types = {
            'drg_id': 'str',
            'status': 'str',
            'upgraded_connections': 'str'
        }

        self.attribute_map = {
            'drg_id': 'drgId',
            'status': 'status',
            'upgraded_connections': 'upgradedConnections'
        }

        self._drg_id = None
        self._status = None
        self._upgraded_connections = None

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this UpgradeStatus.
        The `drgId` of the upgraded DRG.


        :return: The drg_id of this UpgradeStatus.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this UpgradeStatus.
        The `drgId` of the upgraded DRG.


        :param drg_id: The drg_id of this UpgradeStatus.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this UpgradeStatus.
        The current upgrade status of the DRG attachment.

        Allowed values for this property are: "NOT_UPGRADED", "IN_PROGRESS", "UPGRADED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this UpgradeStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpgradeStatus.
        The current upgrade status of the DRG attachment.


        :param status: The status of this UpgradeStatus.
        :type: str
        """
        allowed_values = ["NOT_UPGRADED", "IN_PROGRESS", "UPGRADED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def upgraded_connections(self):
        """
        **[Required]** Gets the upgraded_connections of this UpgradeStatus.
        The number of upgraded connections.


        :return: The upgraded_connections of this UpgradeStatus.
        :rtype: str
        """
        return self._upgraded_connections

    @upgraded_connections.setter
    def upgraded_connections(self, upgraded_connections):
        """
        Sets the upgraded_connections of this UpgradeStatus.
        The number of upgraded connections.


        :param upgraded_connections: The upgraded_connections of this UpgradeStatus.
        :type: str
        """
        self._upgraded_connections = upgraded_connections

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
