# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .entity_discovered import EntityDiscovered
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalExadataInfrastructureDiscoverySummary(EntityDiscovered):
    """
    The discovery result for the Exadata system infrastructure.
    """

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscoverySummary.
    #: This constant has a value of "FULL"
    RACK_SIZE_FULL = "FULL"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscoverySummary.
    #: This constant has a value of "HALF"
    RACK_SIZE_HALF = "HALF"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscoverySummary.
    #: This constant has a value of "QUARTER"
    RACK_SIZE_QUARTER = "QUARTER"

    #: A constant which can be used with the rack_size property of a ExternalExadataInfrastructureDiscoverySummary.
    #: This constant has a value of "EIGHTH"
    RACK_SIZE_EIGHTH = "EIGHTH"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalExadataInfrastructureDiscoverySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.ExternalExadataInfrastructureDiscoverySummary.entity_type` attribute
        of this class is ``INFRASTRUCTURE_DISCOVER_SUMMARY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalExadataInfrastructureDiscoverySummary.
        :type id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalExadataInfrastructureDiscoverySummary.
        :type agent_id: str

        :param connector_id:
            The value to assign to the connector_id property of this ExternalExadataInfrastructureDiscoverySummary.
        :type connector_id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalExadataInfrastructureDiscoverySummary.
        :type display_name: str

        :param version:
            The value to assign to the version property of this ExternalExadataInfrastructureDiscoverySummary.
        :type version: str

        :param internal_id:
            The value to assign to the internal_id property of this ExternalExadataInfrastructureDiscoverySummary.
        :type internal_id: str

        :param status:
            The value to assign to the status property of this ExternalExadataInfrastructureDiscoverySummary.
        :type status: str

        :param discover_status:
            The value to assign to the discover_status property of this ExternalExadataInfrastructureDiscoverySummary.
            Allowed values for this property are: "PREV_DISCOVERED", "NEW_DISCOVERED", "NOT_FOUND", "DISCOVERING"
        :type discover_status: str

        :param discover_error_code:
            The value to assign to the discover_error_code property of this ExternalExadataInfrastructureDiscoverySummary.
        :type discover_error_code: str

        :param discover_error_msg:
            The value to assign to the discover_error_msg property of this ExternalExadataInfrastructureDiscoverySummary.
        :type discover_error_msg: str

        :param entity_type:
            The value to assign to the entity_type property of this ExternalExadataInfrastructureDiscoverySummary.
            Allowed values for this property are: "STORAGE_SERVER_DISCOVER_SUMMARY", "STORAGE_GRID_DISCOVER_SUMMARY", "DATABASE_SYSTEM_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER_SUMMARY", "INFRASTRUCTURE_DISCOVER"
        :type entity_type: str

        :param rack_size:
            The value to assign to the rack_size property of this ExternalExadataInfrastructureDiscoverySummary.
            Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH"
        :type rack_size: str

        """
        self.swagger_types = {
            'id': 'str',
            'agent_id': 'str',
            'connector_id': 'str',
            'display_name': 'str',
            'version': 'str',
            'internal_id': 'str',
            'status': 'str',
            'discover_status': 'str',
            'discover_error_code': 'str',
            'discover_error_msg': 'str',
            'entity_type': 'str',
            'rack_size': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'agent_id': 'agentId',
            'connector_id': 'connectorId',
            'display_name': 'displayName',
            'version': 'version',
            'internal_id': 'internalId',
            'status': 'status',
            'discover_status': 'discoverStatus',
            'discover_error_code': 'discoverErrorCode',
            'discover_error_msg': 'discoverErrorMsg',
            'entity_type': 'entityType',
            'rack_size': 'rackSize'
        }

        self._id = None
        self._agent_id = None
        self._connector_id = None
        self._display_name = None
        self._version = None
        self._internal_id = None
        self._status = None
        self._discover_status = None
        self._discover_error_code = None
        self._discover_error_msg = None
        self._entity_type = None
        self._rack_size = None
        self._entity_type = 'INFRASTRUCTURE_DISCOVER_SUMMARY'

    @property
    def rack_size(self):
        """
        Gets the rack_size of this ExternalExadataInfrastructureDiscoverySummary.
        The size of the Exadata infrastructure.

        Allowed values for this property are: "FULL", "HALF", "QUARTER", "EIGHTH"


        :return: The rack_size of this ExternalExadataInfrastructureDiscoverySummary.
        :rtype: str
        """
        return self._rack_size

    @rack_size.setter
    def rack_size(self, rack_size):
        """
        Sets the rack_size of this ExternalExadataInfrastructureDiscoverySummary.
        The size of the Exadata infrastructure.


        :param rack_size: The rack_size of this ExternalExadataInfrastructureDiscoverySummary.
        :type: str
        """
        allowed_values = ["FULL", "HALF", "QUARTER", "EIGHTH"]
        if not value_allowed_none_or_none_sentinel(rack_size, allowed_values):
            raise ValueError(
                "Invalid value for `rack_size`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._rack_size = rack_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
