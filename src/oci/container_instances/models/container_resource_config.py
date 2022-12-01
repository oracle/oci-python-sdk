# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerResourceConfig(object):
    """
    The resource configuration for a Container. The resource configuration determines
    the guaranteed resources allocated to the container and the maximum allowed resources for a container.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerResourceConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcpus_limit:
            The value to assign to the vcpus_limit property of this ContainerResourceConfig.
        :type vcpus_limit: float

        :param memory_limit_in_gbs:
            The value to assign to the memory_limit_in_gbs property of this ContainerResourceConfig.
        :type memory_limit_in_gbs: float

        """
        self.swagger_types = {
            'vcpus_limit': 'float',
            'memory_limit_in_gbs': 'float'
        }

        self.attribute_map = {
            'vcpus_limit': 'vcpusLimit',
            'memory_limit_in_gbs': 'memoryLimitInGBs'
        }

        self._vcpus_limit = None
        self._memory_limit_in_gbs = None

    @property
    def vcpus_limit(self):
        """
        Gets the vcpus_limit of this ContainerResourceConfig.
        The maximum amount of CPU utilization which may be consumed by the Container's
        process. If no value is provided, then the process may consume
        all CPU resources on the Instance.
        CPU usage is defined in terms of logical CPUs. This means that the
        maximum possible value on an E3 ContainerInstance with 1 OCPU is 2.0.


        :return: The vcpus_limit of this ContainerResourceConfig.
        :rtype: float
        """
        return self._vcpus_limit

    @vcpus_limit.setter
    def vcpus_limit(self, vcpus_limit):
        """
        Sets the vcpus_limit of this ContainerResourceConfig.
        The maximum amount of CPU utilization which may be consumed by the Container's
        process. If no value is provided, then the process may consume
        all CPU resources on the Instance.
        CPU usage is defined in terms of logical CPUs. This means that the
        maximum possible value on an E3 ContainerInstance with 1 OCPU is 2.0.


        :param vcpus_limit: The vcpus_limit of this ContainerResourceConfig.
        :type: float
        """
        self._vcpus_limit = vcpus_limit

    @property
    def memory_limit_in_gbs(self):
        """
        Gets the memory_limit_in_gbs of this ContainerResourceConfig.
        The maximum amount of memory which may be consumed by the Container's
        process. If no value is provided, then the process
        may use all available memory on the Instance.


        :return: The memory_limit_in_gbs of this ContainerResourceConfig.
        :rtype: float
        """
        return self._memory_limit_in_gbs

    @memory_limit_in_gbs.setter
    def memory_limit_in_gbs(self, memory_limit_in_gbs):
        """
        Sets the memory_limit_in_gbs of this ContainerResourceConfig.
        The maximum amount of memory which may be consumed by the Container's
        process. If no value is provided, then the process
        may use all available memory on the Instance.


        :param memory_limit_in_gbs: The memory_limit_in_gbs of this ContainerResourceConfig.
        :type: float
        """
        self._memory_limit_in_gbs = memory_limit_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
