# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualCircuitBandwidthShape(object):
    """
    An individual bandwidth level for virtual circuits.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualCircuitBandwidthShape object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param bandwidth_in_mbps:
            The value to assign to the bandwidth_in_mbps property of this VirtualCircuitBandwidthShape.
        :type bandwidth_in_mbps: int

        :param name:
            The value to assign to the name property of this VirtualCircuitBandwidthShape.
        :type name: str

        """
        self.swagger_types = {
            'bandwidth_in_mbps': 'int',
            'name': 'str'
        }

        self.attribute_map = {
            'bandwidth_in_mbps': 'bandwidthInMbps',
            'name': 'name'
        }

        self._bandwidth_in_mbps = None
        self._name = None

    @property
    def bandwidth_in_mbps(self):
        """
        Gets the bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        The bandwidth in Mbps.

        Example: `10000`


        :return: The bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        :rtype: int
        """
        return self._bandwidth_in_mbps

    @bandwidth_in_mbps.setter
    def bandwidth_in_mbps(self, bandwidth_in_mbps):
        """
        Sets the bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        The bandwidth in Mbps.

        Example: `10000`


        :param bandwidth_in_mbps: The bandwidth_in_mbps of this VirtualCircuitBandwidthShape.
        :type: int
        """
        self._bandwidth_in_mbps = bandwidth_in_mbps

    @property
    def name(self):
        """
        **[Required]** Gets the name of this VirtualCircuitBandwidthShape.
        The name of the bandwidth shape.

        Example: `10 Gbps`


        :return: The name of this VirtualCircuitBandwidthShape.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VirtualCircuitBandwidthShape.
        The name of the bandwidth shape.

        Example: `10 Gbps`


        :param name: The name of this VirtualCircuitBandwidthShape.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
