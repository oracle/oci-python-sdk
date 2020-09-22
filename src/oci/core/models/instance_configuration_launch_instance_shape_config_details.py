# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationLaunchInstanceShapeConfigDetails(object):
    """
    The shape configuration requested for the instance.

    If the parameter is provided, the instance is created
    with the resources that you specify. If some properties are missing or
    the entire parameter is not provided, the instance is created with the default
    configuration values for the `shape` that you specify.

    Each shape only supports certain configurable values. If the values that you provid are not valid for the
    specified `shape`, an error is returned.

    For more information about customizing the resources that are allocated to a flexible shapes, see
    `Flexible Shapes`__.

    __ https://docs.cloud.oracle.com/Content/Compute/References/computeshapes.htm#flexible
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationLaunchInstanceShapeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :type memory_in_gbs: float

        """
        self.swagger_types = {
            'ocpus': 'float',
            'memory_in_gbs': 'float'
        }

        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs'
        }

        self._ocpus = None
        self._memory_in_gbs = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :return: The ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :param ocpus: The ocpus of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        The total amount of memory available to the instance, in gigabytes.


        :return: The memory_in_gbs of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        The total amount of memory available to the instance, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this InstanceConfigurationLaunchInstanceShapeConfigDetails.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
