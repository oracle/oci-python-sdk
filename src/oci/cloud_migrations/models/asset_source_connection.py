# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssetSourceConnection(object):
    """
    Descriptor of a connection to an asset source.
    """

    #: A constant which can be used with the connection_type property of a AssetSourceConnection.
    #: This constant has a value of "DISCOVERY"
    CONNECTION_TYPE_DISCOVERY = "DISCOVERY"

    #: A constant which can be used with the connection_type property of a AssetSourceConnection.
    #: This constant has a value of "REPLICATION"
    CONNECTION_TYPE_REPLICATION = "REPLICATION"

    #: A constant which can be used with the lifecycle_state property of a AssetSourceConnection.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AssetSourceConnection.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AssetSourceConnection.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a AssetSourceConnection.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AssetSourceConnection.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    def __init__(self, **kwargs):
        """
        Initializes a new AssetSourceConnection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this AssetSourceConnection.
            Allowed values for this property are: "DISCOVERY", "REPLICATION"
        :type connection_type: str

        :param connector_id:
            The value to assign to the connector_id property of this AssetSourceConnection.
        :type connector_id: str

        :param asset_source_key:
            The value to assign to the asset_source_key property of this AssetSourceConnection.
        :type asset_source_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AssetSourceConnection.
            Allowed values for this property are: "ACTIVE", "UPDATING", "NEEDS_ATTENTION", "DELETED", "CREATING"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AssetSourceConnection.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'connector_id': 'str',
            'asset_source_key': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'connector_id': 'connectorId',
            'asset_source_key': 'assetSourceKey',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._connection_type = None
        self._connector_id = None
        self._asset_source_key = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this AssetSourceConnection.
        The type of connection for an asset source.

        Allowed values for this property are: "DISCOVERY", "REPLICATION"


        :return: The connection_type of this AssetSourceConnection.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this AssetSourceConnection.
        The type of connection for an asset source.


        :param connection_type: The connection_type of this AssetSourceConnection.
        :type: str
        """
        allowed_values = ["DISCOVERY", "REPLICATION"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            raise ValueError(
                "Invalid value for `connection_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._connection_type = connection_type

    @property
    def connector_id(self):
        """
        **[Required]** Gets the connector_id of this AssetSourceConnection.
        The `OCID`__ of the cloud bridge connector used for migration operations.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The connector_id of this AssetSourceConnection.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """
        Sets the connector_id of this AssetSourceConnection.
        The `OCID`__ of the cloud bridge connector used for migration operations.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param connector_id: The connector_id of this AssetSourceConnection.
        :type: str
        """
        self._connector_id = connector_id

    @property
    def asset_source_key(self):
        """
        **[Required]** Gets the asset_source_key of this AssetSourceConnection.
        Type-specific identifier for an asset source.


        :return: The asset_source_key of this AssetSourceConnection.
        :rtype: str
        """
        return self._asset_source_key

    @asset_source_key.setter
    def asset_source_key(self, asset_source_key):
        """
        Sets the asset_source_key of this AssetSourceConnection.
        Type-specific identifier for an asset source.


        :param asset_source_key: The asset_source_key of this AssetSourceConnection.
        :type: str
        """
        self._asset_source_key = asset_source_key

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AssetSourceConnection.
        The current state of the connection.

        Allowed values for this property are: "ACTIVE", "UPDATING", "NEEDS_ATTENTION", "DELETED", "CREATING"


        :return: The lifecycle_state of this AssetSourceConnection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AssetSourceConnection.
        The current state of the connection.


        :param lifecycle_state: The lifecycle_state of this AssetSourceConnection.
        :type: str
        """
        allowed_values = ["ACTIVE", "UPDATING", "NEEDS_ATTENTION", "DELETED", "CREATING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this AssetSourceConnection.
        The detailed sub-state of the connection.


        :return: The lifecycle_details of this AssetSourceConnection.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AssetSourceConnection.
        The detailed sub-state of the connection.


        :param lifecycle_details: The lifecycle_details of this AssetSourceConnection.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
