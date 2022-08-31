# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectivityUsageDetails(object):
    """
    Input details to ConnectivityUsage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectivityUsageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_key:
            The value to assign to the connection_key property of this ConnectivityUsageDetails.
        :type connection_key: str

        :param action:
            The value to assign to the action property of this ConnectivityUsageDetails.
        :type action: str

        :param consuming_service:
            The value to assign to the consuming_service property of this ConnectivityUsageDetails.
        :type consuming_service: str

        """
        self.swagger_types = {
            'connection_key': 'str',
            'action': 'str',
            'consuming_service': 'str'
        }

        self.attribute_map = {
            'connection_key': 'connectionKey',
            'action': 'action',
            'consuming_service': 'consumingService'
        }

        self._connection_key = None
        self._action = None
        self._consuming_service = None

    @property
    def connection_key(self):
        """
        Gets the connection_key of this ConnectivityUsageDetails.
        connection Key.


        :return: The connection_key of this ConnectivityUsageDetails.
        :rtype: str
        """
        return self._connection_key

    @connection_key.setter
    def connection_key(self, connection_key):
        """
        Sets the connection_key of this ConnectivityUsageDetails.
        connection Key.


        :param connection_key: The connection_key of this ConnectivityUsageDetails.
        :type: str
        """
        self._connection_key = connection_key

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ConnectivityUsageDetails.
        Action type where connection used.


        :return: The action of this ConnectivityUsageDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ConnectivityUsageDetails.
        Action type where connection used.


        :param action: The action of this ConnectivityUsageDetails.
        :type: str
        """
        self._action = action

    @property
    def consuming_service(self):
        """
        **[Required]** Gets the consuming_service of this ConnectivityUsageDetails.
        Consuming serviceType where connection used.


        :return: The consuming_service of this ConnectivityUsageDetails.
        :rtype: str
        """
        return self._consuming_service

    @consuming_service.setter
    def consuming_service(self, consuming_service):
        """
        Sets the consuming_service of this ConnectivityUsageDetails.
        Consuming serviceType where connection used.


        :param consuming_service: The consuming_service of this ConnectivityUsageDetails.
        :type: str
        """
        self._consuming_service = consuming_service

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
