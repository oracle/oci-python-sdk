# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EstimatedPatchingTime(object):
    """
    The estimated total time required in minutes for all patching operations (database server, storage server, and network switch patching).
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EstimatedPatchingTime object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_estimated_patching_time:
            The value to assign to the total_estimated_patching_time property of this EstimatedPatchingTime.
        :type total_estimated_patching_time: int

        :param estimated_db_server_patching_time:
            The value to assign to the estimated_db_server_patching_time property of this EstimatedPatchingTime.
        :type estimated_db_server_patching_time: int

        :param estimated_storage_server_patching_time:
            The value to assign to the estimated_storage_server_patching_time property of this EstimatedPatchingTime.
        :type estimated_storage_server_patching_time: int

        :param estimated_network_switches_patching_time:
            The value to assign to the estimated_network_switches_patching_time property of this EstimatedPatchingTime.
        :type estimated_network_switches_patching_time: int

        """
        self.swagger_types = {
            'total_estimated_patching_time': 'int',
            'estimated_db_server_patching_time': 'int',
            'estimated_storage_server_patching_time': 'int',
            'estimated_network_switches_patching_time': 'int'
        }

        self.attribute_map = {
            'total_estimated_patching_time': 'totalEstimatedPatchingTime',
            'estimated_db_server_patching_time': 'estimatedDbServerPatchingTime',
            'estimated_storage_server_patching_time': 'estimatedStorageServerPatchingTime',
            'estimated_network_switches_patching_time': 'estimatedNetworkSwitchesPatchingTime'
        }

        self._total_estimated_patching_time = None
        self._estimated_db_server_patching_time = None
        self._estimated_storage_server_patching_time = None
        self._estimated_network_switches_patching_time = None

    @property
    def total_estimated_patching_time(self):
        """
        Gets the total_estimated_patching_time of this EstimatedPatchingTime.
        The estimated total time required in minutes for all patching operations.


        :return: The total_estimated_patching_time of this EstimatedPatchingTime.
        :rtype: int
        """
        return self._total_estimated_patching_time

    @total_estimated_patching_time.setter
    def total_estimated_patching_time(self, total_estimated_patching_time):
        """
        Sets the total_estimated_patching_time of this EstimatedPatchingTime.
        The estimated total time required in minutes for all patching operations.


        :param total_estimated_patching_time: The total_estimated_patching_time of this EstimatedPatchingTime.
        :type: int
        """
        self._total_estimated_patching_time = total_estimated_patching_time

    @property
    def estimated_db_server_patching_time(self):
        """
        Gets the estimated_db_server_patching_time of this EstimatedPatchingTime.
        The estimated time required in minutes for database server patching.


        :return: The estimated_db_server_patching_time of this EstimatedPatchingTime.
        :rtype: int
        """
        return self._estimated_db_server_patching_time

    @estimated_db_server_patching_time.setter
    def estimated_db_server_patching_time(self, estimated_db_server_patching_time):
        """
        Sets the estimated_db_server_patching_time of this EstimatedPatchingTime.
        The estimated time required in minutes for database server patching.


        :param estimated_db_server_patching_time: The estimated_db_server_patching_time of this EstimatedPatchingTime.
        :type: int
        """
        self._estimated_db_server_patching_time = estimated_db_server_patching_time

    @property
    def estimated_storage_server_patching_time(self):
        """
        Gets the estimated_storage_server_patching_time of this EstimatedPatchingTime.
        The estimated time required in minutes for storage server patching.


        :return: The estimated_storage_server_patching_time of this EstimatedPatchingTime.
        :rtype: int
        """
        return self._estimated_storage_server_patching_time

    @estimated_storage_server_patching_time.setter
    def estimated_storage_server_patching_time(self, estimated_storage_server_patching_time):
        """
        Sets the estimated_storage_server_patching_time of this EstimatedPatchingTime.
        The estimated time required in minutes for storage server patching.


        :param estimated_storage_server_patching_time: The estimated_storage_server_patching_time of this EstimatedPatchingTime.
        :type: int
        """
        self._estimated_storage_server_patching_time = estimated_storage_server_patching_time

    @property
    def estimated_network_switches_patching_time(self):
        """
        Gets the estimated_network_switches_patching_time of this EstimatedPatchingTime.
        The estimated time required in minutes for network switch patching.


        :return: The estimated_network_switches_patching_time of this EstimatedPatchingTime.
        :rtype: int
        """
        return self._estimated_network_switches_patching_time

    @estimated_network_switches_patching_time.setter
    def estimated_network_switches_patching_time(self, estimated_network_switches_patching_time):
        """
        Sets the estimated_network_switches_patching_time of this EstimatedPatchingTime.
        The estimated time required in minutes for network switch patching.


        :param estimated_network_switches_patching_time: The estimated_network_switches_patching_time of this EstimatedPatchingTime.
        :type: int
        """
        self._estimated_network_switches_patching_time = estimated_network_switches_patching_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
