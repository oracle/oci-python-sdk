# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkConnectivityStatusCollection(object):
    """
    This is a collection of NetworkConnectivityStatus.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkConnectivityStatusCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_connectivity_status_list:
            The value to assign to the network_connectivity_status_list property of this NetworkConnectivityStatusCollection.
        :type network_connectivity_status_list: list[oci.data_connectivity.models.NetworkConnectivityStatus]

        """
        self.swagger_types = {
            'network_connectivity_status_list': 'list[NetworkConnectivityStatus]'
        }

        self.attribute_map = {
            'network_connectivity_status_list': 'networkConnectivityStatusList'
        }

        self._network_connectivity_status_list = None

    @property
    def network_connectivity_status_list(self):
        """
        **[Required]** Gets the network_connectivity_status_list of this NetworkConnectivityStatusCollection.
        The array of NetworkConnectivityStatus.


        :return: The network_connectivity_status_list of this NetworkConnectivityStatusCollection.
        :rtype: list[oci.data_connectivity.models.NetworkConnectivityStatus]
        """
        return self._network_connectivity_status_list

    @network_connectivity_status_list.setter
    def network_connectivity_status_list(self, network_connectivity_status_list):
        """
        Sets the network_connectivity_status_list of this NetworkConnectivityStatusCollection.
        The array of NetworkConnectivityStatus.


        :param network_connectivity_status_list: The network_connectivity_status_list of this NetworkConnectivityStatusCollection.
        :type: list[oci.data_connectivity.models.NetworkConnectivityStatus]
        """
        self._network_connectivity_status_list = network_connectivity_status_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
