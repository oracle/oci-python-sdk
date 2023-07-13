# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerResourceConfigDetails(object):
    """
    The size and amount of resources available to the container.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerResourceConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcpus_limit:
            The value to assign to the vcpus_limit property of this CreateContainerResourceConfigDetails.
        :type vcpus_limit: float

        :param memory_limit_in_gbs:
            The value to assign to the memory_limit_in_gbs property of this CreateContainerResourceConfigDetails.
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
        Gets the vcpus_limit of this CreateContainerResourceConfigDetails.
        The maximum amount of CPUs that can be consumed by the container's process.

        If you do not set a value, then the process
        can use all available CPU resources on the instance.

        CPU usage is defined in terms of logical CPUs. This means that the maximum possible value on
        an E3 ContainerInstance with 1 OCPU is 2.0.

        A container with a 2.0 vcpusLimit could consume up to 100% of the CPU resources available on the container instance.
        Values can be fractional. A value of \"1.5\" means that the container
        can consume at most the equivalent of 1 and a half logical CPUs worth of CPU capacity.


        :return: The vcpus_limit of this CreateContainerResourceConfigDetails.
        :rtype: float
        """
        return self._vcpus_limit

    @vcpus_limit.setter
    def vcpus_limit(self, vcpus_limit):
        """
        Sets the vcpus_limit of this CreateContainerResourceConfigDetails.
        The maximum amount of CPUs that can be consumed by the container's process.

        If you do not set a value, then the process
        can use all available CPU resources on the instance.

        CPU usage is defined in terms of logical CPUs. This means that the maximum possible value on
        an E3 ContainerInstance with 1 OCPU is 2.0.

        A container with a 2.0 vcpusLimit could consume up to 100% of the CPU resources available on the container instance.
        Values can be fractional. A value of \"1.5\" means that the container
        can consume at most the equivalent of 1 and a half logical CPUs worth of CPU capacity.


        :param vcpus_limit: The vcpus_limit of this CreateContainerResourceConfigDetails.
        :type: float
        """
        self._vcpus_limit = vcpus_limit

    @property
    def memory_limit_in_gbs(self):
        """
        Gets the memory_limit_in_gbs of this CreateContainerResourceConfigDetails.
        The maximum amount of memory that can be consumed by the container's
        process.

        If you do not set a value, then the process
        may use all available memory on the instance.


        :return: The memory_limit_in_gbs of this CreateContainerResourceConfigDetails.
        :rtype: float
        """
        return self._memory_limit_in_gbs

    @memory_limit_in_gbs.setter
    def memory_limit_in_gbs(self, memory_limit_in_gbs):
        """
        Sets the memory_limit_in_gbs of this CreateContainerResourceConfigDetails.
        The maximum amount of memory that can be consumed by the container's
        process.

        If you do not set a value, then the process
        may use all available memory on the instance.


        :param memory_limit_in_gbs: The memory_limit_in_gbs of this CreateContainerResourceConfigDetails.
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
