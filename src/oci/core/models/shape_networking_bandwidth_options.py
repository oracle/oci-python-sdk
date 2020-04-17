# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeNetworkingBandwidthOptions(object):
    """
    The possible configurations for the amount of networking bandwidth available to an instance of this shape. If this field is null, then all instances of this shape have a fixed amount of bandwidth equivalent to `networkingBandwidthInGbps`.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeNetworkingBandwidthOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param min_in_gbps:
            The value to assign to the min_in_gbps property of this ShapeNetworkingBandwidthOptions.
        :type min_in_gbps: float

        :param max_in_gbps:
            The value to assign to the max_in_gbps property of this ShapeNetworkingBandwidthOptions.
        :type max_in_gbps: float

        :param default_per_ocpu_in_gbps:
            The value to assign to the default_per_ocpu_in_gbps property of this ShapeNetworkingBandwidthOptions.
        :type default_per_ocpu_in_gbps: float

        """
        self.swagger_types = {
            'min_in_gbps': 'float',
            'max_in_gbps': 'float',
            'default_per_ocpu_in_gbps': 'float'
        }

        self.attribute_map = {
            'min_in_gbps': 'minInGbps',
            'max_in_gbps': 'maxInGbps',
            'default_per_ocpu_in_gbps': 'defaultPerOcpuInGbps'
        }

        self._min_in_gbps = None
        self._max_in_gbps = None
        self._default_per_ocpu_in_gbps = None

    @property
    def min_in_gbps(self):
        """
        Gets the min_in_gbps of this ShapeNetworkingBandwidthOptions.
        The minimum amount of networking bandwidth, in gigabits per second.


        :return: The min_in_gbps of this ShapeNetworkingBandwidthOptions.
        :rtype: float
        """
        return self._min_in_gbps

    @min_in_gbps.setter
    def min_in_gbps(self, min_in_gbps):
        """
        Sets the min_in_gbps of this ShapeNetworkingBandwidthOptions.
        The minimum amount of networking bandwidth, in gigabits per second.


        :param min_in_gbps: The min_in_gbps of this ShapeNetworkingBandwidthOptions.
        :type: float
        """
        self._min_in_gbps = min_in_gbps

    @property
    def max_in_gbps(self):
        """
        Gets the max_in_gbps of this ShapeNetworkingBandwidthOptions.
        The maximum amount of networking bandwidth, in gigabits per second.


        :return: The max_in_gbps of this ShapeNetworkingBandwidthOptions.
        :rtype: float
        """
        return self._max_in_gbps

    @max_in_gbps.setter
    def max_in_gbps(self, max_in_gbps):
        """
        Sets the max_in_gbps of this ShapeNetworkingBandwidthOptions.
        The maximum amount of networking bandwidth, in gigabits per second.


        :param max_in_gbps: The max_in_gbps of this ShapeNetworkingBandwidthOptions.
        :type: float
        """
        self._max_in_gbps = max_in_gbps

    @property
    def default_per_ocpu_in_gbps(self):
        """
        Gets the default_per_ocpu_in_gbps of this ShapeNetworkingBandwidthOptions.
        The default amount of networking bandwidth, in gigabits per second,
        per OCPU.


        :return: The default_per_ocpu_in_gbps of this ShapeNetworkingBandwidthOptions.
        :rtype: float
        """
        return self._default_per_ocpu_in_gbps

    @default_per_ocpu_in_gbps.setter
    def default_per_ocpu_in_gbps(self, default_per_ocpu_in_gbps):
        """
        Sets the default_per_ocpu_in_gbps of this ShapeNetworkingBandwidthOptions.
        The default amount of networking bandwidth, in gigabits per second,
        per OCPU.


        :param default_per_ocpu_in_gbps: The default_per_ocpu_in_gbps of this ShapeNetworkingBandwidthOptions.
        :type: float
        """
        self._default_per_ocpu_in_gbps = default_per_ocpu_in_gbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
