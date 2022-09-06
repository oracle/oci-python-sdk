# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkConnectivityStatus(object):
    """
    The network validation status for a Private Endpoint - Data Asset pair.
    """

    #: A constant which can be used with the network_validation_status_enum property of a NetworkConnectivityStatus.
    #: This constant has a value of "REACHABLE"
    NETWORK_VALIDATION_STATUS_ENUM_REACHABLE = "REACHABLE"

    #: A constant which can be used with the network_validation_status_enum property of a NetworkConnectivityStatus.
    #: This constant has a value of "NOT_REACHABLE"
    NETWORK_VALIDATION_STATUS_ENUM_NOT_REACHABLE = "NOT_REACHABLE"

    #: A constant which can be used with the network_validation_status_enum property of a NetworkConnectivityStatus.
    #: This constant has a value of "ERROR"
    NETWORK_VALIDATION_STATUS_ENUM_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkConnectivityStatus object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_asset_key:
            The value to assign to the data_asset_key property of this NetworkConnectivityStatus.
        :type data_asset_key: str

        :param private_end_point_key:
            The value to assign to the private_end_point_key property of this NetworkConnectivityStatus.
        :type private_end_point_key: str

        :param error_message:
            The value to assign to the error_message property of this NetworkConnectivityStatus.
        :type error_message: str

        :param time_last_updated:
            The value to assign to the time_last_updated property of this NetworkConnectivityStatus.
        :type time_last_updated: datetime

        :param network_validation_status_enum:
            The value to assign to the network_validation_status_enum property of this NetworkConnectivityStatus.
            Allowed values for this property are: "REACHABLE", "NOT_REACHABLE", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type network_validation_status_enum: str

        """
        self.swagger_types = {
            'data_asset_key': 'str',
            'private_end_point_key': 'str',
            'error_message': 'str',
            'time_last_updated': 'datetime',
            'network_validation_status_enum': 'str'
        }

        self.attribute_map = {
            'data_asset_key': 'dataAssetKey',
            'private_end_point_key': 'privateEndPointKey',
            'error_message': 'errorMessage',
            'time_last_updated': 'timeLastUpdated',
            'network_validation_status_enum': 'networkValidationStatusEnum'
        }

        self._data_asset_key = None
        self._private_end_point_key = None
        self._error_message = None
        self._time_last_updated = None
        self._network_validation_status_enum = None

    @property
    def data_asset_key(self):
        """
        **[Required]** Gets the data_asset_key of this NetworkConnectivityStatus.
        DataAsset key to which the NetworkValidationStatus belongs to.


        :return: The data_asset_key of this NetworkConnectivityStatus.
        :rtype: str
        """
        return self._data_asset_key

    @data_asset_key.setter
    def data_asset_key(self, data_asset_key):
        """
        Sets the data_asset_key of this NetworkConnectivityStatus.
        DataAsset key to which the NetworkValidationStatus belongs to.


        :param data_asset_key: The data_asset_key of this NetworkConnectivityStatus.
        :type: str
        """
        self._data_asset_key = data_asset_key

    @property
    def private_end_point_key(self):
        """
        Gets the private_end_point_key of this NetworkConnectivityStatus.
        PrivateEndpoint key, if any, to which the NetworkValidationStatus belongs to.


        :return: The private_end_point_key of this NetworkConnectivityStatus.
        :rtype: str
        """
        return self._private_end_point_key

    @private_end_point_key.setter
    def private_end_point_key(self, private_end_point_key):
        """
        Sets the private_end_point_key of this NetworkConnectivityStatus.
        PrivateEndpoint key, if any, to which the NetworkValidationStatus belongs to.


        :param private_end_point_key: The private_end_point_key of this NetworkConnectivityStatus.
        :type: str
        """
        self._private_end_point_key = private_end_point_key

    @property
    def error_message(self):
        """
        Gets the error_message of this NetworkConnectivityStatus.
        Exception or error message encountered while testing network reachability for the data asset.


        :return: The error_message of this NetworkConnectivityStatus.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this NetworkConnectivityStatus.
        Exception or error message encountered while testing network reachability for the data asset.


        :param error_message: The error_message of this NetworkConnectivityStatus.
        :type: str
        """
        self._error_message = error_message

    @property
    def time_last_updated(self):
        """
        Gets the time_last_updated of this NetworkConnectivityStatus.
        The timestamp when the network validation was last updated for the given DataAsset-PrivateEndpoint pair.


        :return: The time_last_updated of this NetworkConnectivityStatus.
        :rtype: datetime
        """
        return self._time_last_updated

    @time_last_updated.setter
    def time_last_updated(self, time_last_updated):
        """
        Sets the time_last_updated of this NetworkConnectivityStatus.
        The timestamp when the network validation was last updated for the given DataAsset-PrivateEndpoint pair.


        :param time_last_updated: The time_last_updated of this NetworkConnectivityStatus.
        :type: datetime
        """
        self._time_last_updated = time_last_updated

    @property
    def network_validation_status_enum(self):
        """
        Gets the network_validation_status_enum of this NetworkConnectivityStatus.
        Exception or error message encountered while testing network reachability for the data asset.

        Allowed values for this property are: "REACHABLE", "NOT_REACHABLE", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The network_validation_status_enum of this NetworkConnectivityStatus.
        :rtype: str
        """
        return self._network_validation_status_enum

    @network_validation_status_enum.setter
    def network_validation_status_enum(self, network_validation_status_enum):
        """
        Sets the network_validation_status_enum of this NetworkConnectivityStatus.
        Exception or error message encountered while testing network reachability for the data asset.


        :param network_validation_status_enum: The network_validation_status_enum of this NetworkConnectivityStatus.
        :type: str
        """
        allowed_values = ["REACHABLE", "NOT_REACHABLE", "ERROR"]
        if not value_allowed_none_or_none_sentinel(network_validation_status_enum, allowed_values):
            network_validation_status_enum = 'UNKNOWN_ENUM_VALUE'
        self._network_validation_status_enum = network_validation_status_enum

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
