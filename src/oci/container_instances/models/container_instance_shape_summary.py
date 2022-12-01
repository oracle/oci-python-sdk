# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ContainerInstanceShapeSummary(object):
    """
    Details about a shape for a container Instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ContainerInstanceShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ContainerInstanceShapeSummary.
        :type name: str

        :param processor_description:
            The value to assign to the processor_description property of this ContainerInstanceShapeSummary.
        :type processor_description: str

        :param ocpu_options:
            The value to assign to the ocpu_options property of this ContainerInstanceShapeSummary.
        :type ocpu_options: oci.container_instances.models.ShapeOcpuOptions

        :param memory_options:
            The value to assign to the memory_options property of this ContainerInstanceShapeSummary.
        :type memory_options: oci.container_instances.models.ShapeMemoryOptions

        :param networking_bandwidth_options:
            The value to assign to the networking_bandwidth_options property of this ContainerInstanceShapeSummary.
        :type networking_bandwidth_options: oci.container_instances.models.ShapeNetworkingBandwidthOptions

        """
        self.swagger_types = {
            'name': 'str',
            'processor_description': 'str',
            'ocpu_options': 'ShapeOcpuOptions',
            'memory_options': 'ShapeMemoryOptions',
            'networking_bandwidth_options': 'ShapeNetworkingBandwidthOptions'
        }

        self.attribute_map = {
            'name': 'name',
            'processor_description': 'processorDescription',
            'ocpu_options': 'ocpuOptions',
            'memory_options': 'memoryOptions',
            'networking_bandwidth_options': 'networkingBandwidthOptions'
        }

        self._name = None
        self._processor_description = None
        self._ocpu_options = None
        self._memory_options = None
        self._networking_bandwidth_options = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ContainerInstanceShapeSummary.
        The name identifying the shape.


        :return: The name of this ContainerInstanceShapeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ContainerInstanceShapeSummary.
        The name identifying the shape.


        :param name: The name of this ContainerInstanceShapeSummary.
        :type: str
        """
        self._name = name

    @property
    def processor_description(self):
        """
        **[Required]** Gets the processor_description of this ContainerInstanceShapeSummary.
        A short description of the Instance's processor (CPU).


        :return: The processor_description of this ContainerInstanceShapeSummary.
        :rtype: str
        """
        return self._processor_description

    @processor_description.setter
    def processor_description(self, processor_description):
        """
        Sets the processor_description of this ContainerInstanceShapeSummary.
        A short description of the Instance's processor (CPU).


        :param processor_description: The processor_description of this ContainerInstanceShapeSummary.
        :type: str
        """
        self._processor_description = processor_description

    @property
    def ocpu_options(self):
        """
        Gets the ocpu_options of this ContainerInstanceShapeSummary.

        :return: The ocpu_options of this ContainerInstanceShapeSummary.
        :rtype: oci.container_instances.models.ShapeOcpuOptions
        """
        return self._ocpu_options

    @ocpu_options.setter
    def ocpu_options(self, ocpu_options):
        """
        Sets the ocpu_options of this ContainerInstanceShapeSummary.

        :param ocpu_options: The ocpu_options of this ContainerInstanceShapeSummary.
        :type: oci.container_instances.models.ShapeOcpuOptions
        """
        self._ocpu_options = ocpu_options

    @property
    def memory_options(self):
        """
        Gets the memory_options of this ContainerInstanceShapeSummary.

        :return: The memory_options of this ContainerInstanceShapeSummary.
        :rtype: oci.container_instances.models.ShapeMemoryOptions
        """
        return self._memory_options

    @memory_options.setter
    def memory_options(self, memory_options):
        """
        Sets the memory_options of this ContainerInstanceShapeSummary.

        :param memory_options: The memory_options of this ContainerInstanceShapeSummary.
        :type: oci.container_instances.models.ShapeMemoryOptions
        """
        self._memory_options = memory_options

    @property
    def networking_bandwidth_options(self):
        """
        Gets the networking_bandwidth_options of this ContainerInstanceShapeSummary.

        :return: The networking_bandwidth_options of this ContainerInstanceShapeSummary.
        :rtype: oci.container_instances.models.ShapeNetworkingBandwidthOptions
        """
        return self._networking_bandwidth_options

    @networking_bandwidth_options.setter
    def networking_bandwidth_options(self, networking_bandwidth_options):
        """
        Sets the networking_bandwidth_options of this ContainerInstanceShapeSummary.

        :param networking_bandwidth_options: The networking_bandwidth_options of this ContainerInstanceShapeSummary.
        :type: oci.container_instances.models.ShapeNetworkingBandwidthOptions
        """
        self._networking_bandwidth_options = networking_bandwidth_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
