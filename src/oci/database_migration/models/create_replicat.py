# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateReplicat(object):
    """
    Parameters for GoldenGate Replicat processes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateReplicat object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param map_parallelism:
            The value to assign to the map_parallelism property of this CreateReplicat.
        :type map_parallelism: int

        :param min_apply_parallelism:
            The value to assign to the min_apply_parallelism property of this CreateReplicat.
        :type min_apply_parallelism: int

        :param max_apply_parallelism:
            The value to assign to the max_apply_parallelism property of this CreateReplicat.
        :type max_apply_parallelism: int

        """
        self.swagger_types = {
            'map_parallelism': 'int',
            'min_apply_parallelism': 'int',
            'max_apply_parallelism': 'int'
        }

        self.attribute_map = {
            'map_parallelism': 'mapParallelism',
            'min_apply_parallelism': 'minApplyParallelism',
            'max_apply_parallelism': 'maxApplyParallelism'
        }

        self._map_parallelism = None
        self._min_apply_parallelism = None
        self._max_apply_parallelism = None

    @property
    def map_parallelism(self):
        """
        Gets the map_parallelism of this CreateReplicat.
        Number of threads used to read trail files (valid for Parallel Replicat)


        :return: The map_parallelism of this CreateReplicat.
        :rtype: int
        """
        return self._map_parallelism

    @map_parallelism.setter
    def map_parallelism(self, map_parallelism):
        """
        Sets the map_parallelism of this CreateReplicat.
        Number of threads used to read trail files (valid for Parallel Replicat)


        :param map_parallelism: The map_parallelism of this CreateReplicat.
        :type: int
        """
        self._map_parallelism = map_parallelism

    @property
    def min_apply_parallelism(self):
        """
        Gets the min_apply_parallelism of this CreateReplicat.
        Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :return: The min_apply_parallelism of this CreateReplicat.
        :rtype: int
        """
        return self._min_apply_parallelism

    @min_apply_parallelism.setter
    def min_apply_parallelism(self, min_apply_parallelism):
        """
        Sets the min_apply_parallelism of this CreateReplicat.
        Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :param min_apply_parallelism: The min_apply_parallelism of this CreateReplicat.
        :type: int
        """
        self._min_apply_parallelism = min_apply_parallelism

    @property
    def max_apply_parallelism(self):
        """
        Gets the max_apply_parallelism of this CreateReplicat.
        Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :return: The max_apply_parallelism of this CreateReplicat.
        :rtype: int
        """
        return self._max_apply_parallelism

    @max_apply_parallelism.setter
    def max_apply_parallelism(self, max_apply_parallelism):
        """
        Sets the max_apply_parallelism of this CreateReplicat.
        Defines the range in which the Replicat automatically adjusts its apply parallelism (valid for Parallel Replicat)


        :param max_apply_parallelism: The max_apply_parallelism of this CreateReplicat.
        :type: int
        """
        self._max_apply_parallelism = max_apply_parallelism

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
