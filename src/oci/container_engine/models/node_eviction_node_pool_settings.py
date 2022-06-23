# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodeEvictionNodePoolSettings(object):
    """
    Node Eviction Details configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodeEvictionNodePoolSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param eviction_grace_duration:
            The value to assign to the eviction_grace_duration property of this NodeEvictionNodePoolSettings.
        :type eviction_grace_duration: str

        :param is_force_delete_after_grace_duration:
            The value to assign to the is_force_delete_after_grace_duration property of this NodeEvictionNodePoolSettings.
        :type is_force_delete_after_grace_duration: bool

        """
        self.swagger_types = {
            'eviction_grace_duration': 'str',
            'is_force_delete_after_grace_duration': 'bool'
        }

        self.attribute_map = {
            'eviction_grace_duration': 'evictionGraceDuration',
            'is_force_delete_after_grace_duration': 'isForceDeleteAfterGraceDuration'
        }

        self._eviction_grace_duration = None
        self._is_force_delete_after_grace_duration = None

    @property
    def eviction_grace_duration(self):
        """
        Gets the eviction_grace_duration of this NodeEvictionNodePoolSettings.
        Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon and drain.
        Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M


        :return: The eviction_grace_duration of this NodeEvictionNodePoolSettings.
        :rtype: str
        """
        return self._eviction_grace_duration

    @eviction_grace_duration.setter
    def eviction_grace_duration(self, eviction_grace_duration):
        """
        Sets the eviction_grace_duration of this NodeEvictionNodePoolSettings.
        Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon and drain.
        Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M


        :param eviction_grace_duration: The eviction_grace_duration of this NodeEvictionNodePoolSettings.
        :type: str
        """
        self._eviction_grace_duration = eviction_grace_duration

    @property
    def is_force_delete_after_grace_duration(self):
        """
        Gets the is_force_delete_after_grace_duration of this NodeEvictionNodePoolSettings.
        If the underlying compute instance should be deleted if you cannot evict all the pods in grace period


        :return: The is_force_delete_after_grace_duration of this NodeEvictionNodePoolSettings.
        :rtype: bool
        """
        return self._is_force_delete_after_grace_duration

    @is_force_delete_after_grace_duration.setter
    def is_force_delete_after_grace_duration(self, is_force_delete_after_grace_duration):
        """
        Sets the is_force_delete_after_grace_duration of this NodeEvictionNodePoolSettings.
        If the underlying compute instance should be deleted if you cannot evict all the pods in grace period


        :param is_force_delete_after_grace_duration: The is_force_delete_after_grace_duration of this NodeEvictionNodePoolSettings.
        :type: bool
        """
        self._is_force_delete_after_grace_duration = is_force_delete_after_grace_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
