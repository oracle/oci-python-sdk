# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .autotune_policy import AutotunePolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PerformanceBasedAutotunePolicy(AutotunePolicy):
    """
    If a volume is being throttled at the current setting for a certain period of time, auto-tune will
    gradually increase the volume\u2019s performance limited up to Maximum VPUs/GB. After the volume has been idle at the
    current setting for a certain period of time, auto-tune will gradually decrease the volume\u2019s performance limited
    down to Default/Minimum VPUs/GB.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PerformanceBasedAutotunePolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.PerformanceBasedAutotunePolicy.autotune_type` attribute
        of this class is ``PERFORMANCE_BASED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param autotune_type:
            The value to assign to the autotune_type property of this PerformanceBasedAutotunePolicy.
            Allowed values for this property are: "DETACHED_VOLUME", "PERFORMANCE_BASED"
        :type autotune_type: str

        :param max_vpus_per_gb:
            The value to assign to the max_vpus_per_gb property of this PerformanceBasedAutotunePolicy.
        :type max_vpus_per_gb: int

        """
        self.swagger_types = {
            'autotune_type': 'str',
            'max_vpus_per_gb': 'int'
        }

        self.attribute_map = {
            'autotune_type': 'autotuneType',
            'max_vpus_per_gb': 'maxVpusPerGB'
        }

        self._autotune_type = None
        self._max_vpus_per_gb = None
        self._autotune_type = 'PERFORMANCE_BASED'

    @property
    def max_vpus_per_gb(self):
        """
        **[Required]** Gets the max_vpus_per_gb of this PerformanceBasedAutotunePolicy.
        This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
        temporarily based on performance monitoring.


        :return: The max_vpus_per_gb of this PerformanceBasedAutotunePolicy.
        :rtype: int
        """
        return self._max_vpus_per_gb

    @max_vpus_per_gb.setter
    def max_vpus_per_gb(self, max_vpus_per_gb):
        """
        Sets the max_vpus_per_gb of this PerformanceBasedAutotunePolicy.
        This will be the maximum VPUs/GB performance level that the volume will be auto-tuned
        temporarily based on performance monitoring.


        :param max_vpus_per_gb: The max_vpus_per_gb of this PerformanceBasedAutotunePolicy.
        :type: int
        """
        self._max_vpus_per_gb = max_vpus_per_gb

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
