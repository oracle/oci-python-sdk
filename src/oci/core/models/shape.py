# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Shape(object):
    """
    A compute instance shape that can be used in :func:`launch_instance`.
    For more information, see `Overview of the Compute Service`__ and
    `Compute Shapes`__.

    __ https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm
    __ https://docs.cloud.oracle.com/Content/Compute/References/computeshapes.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Shape object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this Shape.
        :type shape: str

        :param processor_description:
            The value to assign to the processor_description property of this Shape.
        :type processor_description: str

        :param ocpus:
            The value to assign to the ocpus property of this Shape.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this Shape.
        :type memory_in_gbs: float

        :param networking_bandwidth_in_gbps:
            The value to assign to the networking_bandwidth_in_gbps property of this Shape.
        :type networking_bandwidth_in_gbps: float

        :param max_vnic_attachments:
            The value to assign to the max_vnic_attachments property of this Shape.
        :type max_vnic_attachments: int

        :param gpus:
            The value to assign to the gpus property of this Shape.
        :type gpus: int

        :param gpu_description:
            The value to assign to the gpu_description property of this Shape.
        :type gpu_description: str

        :param local_disks:
            The value to assign to the local_disks property of this Shape.
        :type local_disks: int

        :param local_disks_total_size_in_gbs:
            The value to assign to the local_disks_total_size_in_gbs property of this Shape.
        :type local_disks_total_size_in_gbs: float

        :param local_disk_description:
            The value to assign to the local_disk_description property of this Shape.
        :type local_disk_description: str

        :param ocpu_options:
            The value to assign to the ocpu_options property of this Shape.
        :type ocpu_options: ShapeOcpuOptions

        :param memory_options:
            The value to assign to the memory_options property of this Shape.
        :type memory_options: ShapeMemoryOptions

        :param networking_bandwidth_options:
            The value to assign to the networking_bandwidth_options property of this Shape.
        :type networking_bandwidth_options: ShapeNetworkingBandwidthOptions

        :param max_vnic_attachment_options:
            The value to assign to the max_vnic_attachment_options property of this Shape.
        :type max_vnic_attachment_options: ShapeMaxVnicAttachmentOptions

        """
        self.swagger_types = {
            'shape': 'str',
            'processor_description': 'str',
            'ocpus': 'float',
            'memory_in_gbs': 'float',
            'networking_bandwidth_in_gbps': 'float',
            'max_vnic_attachments': 'int',
            'gpus': 'int',
            'gpu_description': 'str',
            'local_disks': 'int',
            'local_disks_total_size_in_gbs': 'float',
            'local_disk_description': 'str',
            'ocpu_options': 'ShapeOcpuOptions',
            'memory_options': 'ShapeMemoryOptions',
            'networking_bandwidth_options': 'ShapeNetworkingBandwidthOptions',
            'max_vnic_attachment_options': 'ShapeMaxVnicAttachmentOptions'
        }

        self.attribute_map = {
            'shape': 'shape',
            'processor_description': 'processorDescription',
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'networking_bandwidth_in_gbps': 'networkingBandwidthInGbps',
            'max_vnic_attachments': 'maxVnicAttachments',
            'gpus': 'gpus',
            'gpu_description': 'gpuDescription',
            'local_disks': 'localDisks',
            'local_disks_total_size_in_gbs': 'localDisksTotalSizeInGBs',
            'local_disk_description': 'localDiskDescription',
            'ocpu_options': 'ocpuOptions',
            'memory_options': 'memoryOptions',
            'networking_bandwidth_options': 'networkingBandwidthOptions',
            'max_vnic_attachment_options': 'maxVnicAttachmentOptions'
        }

        self._shape = None
        self._processor_description = None
        self._ocpus = None
        self._memory_in_gbs = None
        self._networking_bandwidth_in_gbps = None
        self._max_vnic_attachments = None
        self._gpus = None
        self._gpu_description = None
        self._local_disks = None
        self._local_disks_total_size_in_gbs = None
        self._local_disk_description = None
        self._ocpu_options = None
        self._memory_options = None
        self._networking_bandwidth_options = None
        self._max_vnic_attachment_options = None

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this Shape.
        The name of the shape. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :return: The shape of this Shape.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this Shape.
        The name of the shape. You can enumerate all available shapes by calling
        :func:`list_shapes`.


        :param shape: The shape of this Shape.
        :type: str
        """
        self._shape = shape

    @property
    def processor_description(self):
        """
        Gets the processor_description of this Shape.
        A short description of the shape's processor (CPU).


        :return: The processor_description of this Shape.
        :rtype: str
        """
        return self._processor_description

    @processor_description.setter
    def processor_description(self, processor_description):
        """
        Sets the processor_description of this Shape.
        A short description of the shape's processor (CPU).


        :param processor_description: The processor_description of this Shape.
        :type: str
        """
        self._processor_description = processor_description

    @property
    def ocpus(self):
        """
        Gets the ocpus of this Shape.
        The default number of OCPUs available for this shape.


        :return: The ocpus of this Shape.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this Shape.
        The default number of OCPUs available for this shape.


        :param ocpus: The ocpus of this Shape.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this Shape.
        The default amount of memory available for this shape, in gigabytes.


        :return: The memory_in_gbs of this Shape.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this Shape.
        The default amount of memory available for this shape, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this Shape.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def networking_bandwidth_in_gbps(self):
        """
        Gets the networking_bandwidth_in_gbps of this Shape.
        The networking bandwidth available for this shape, in gigabits per second.


        :return: The networking_bandwidth_in_gbps of this Shape.
        :rtype: float
        """
        return self._networking_bandwidth_in_gbps

    @networking_bandwidth_in_gbps.setter
    def networking_bandwidth_in_gbps(self, networking_bandwidth_in_gbps):
        """
        Sets the networking_bandwidth_in_gbps of this Shape.
        The networking bandwidth available for this shape, in gigabits per second.


        :param networking_bandwidth_in_gbps: The networking_bandwidth_in_gbps of this Shape.
        :type: float
        """
        self._networking_bandwidth_in_gbps = networking_bandwidth_in_gbps

    @property
    def max_vnic_attachments(self):
        """
        Gets the max_vnic_attachments of this Shape.
        The maximum number of VNIC attachments available for this shape.


        :return: The max_vnic_attachments of this Shape.
        :rtype: int
        """
        return self._max_vnic_attachments

    @max_vnic_attachments.setter
    def max_vnic_attachments(self, max_vnic_attachments):
        """
        Sets the max_vnic_attachments of this Shape.
        The maximum number of VNIC attachments available for this shape.


        :param max_vnic_attachments: The max_vnic_attachments of this Shape.
        :type: int
        """
        self._max_vnic_attachments = max_vnic_attachments

    @property
    def gpus(self):
        """
        Gets the gpus of this Shape.
        The number of GPUs available for this shape.


        :return: The gpus of this Shape.
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """
        Sets the gpus of this Shape.
        The number of GPUs available for this shape.


        :param gpus: The gpus of this Shape.
        :type: int
        """
        self._gpus = gpus

    @property
    def gpu_description(self):
        """
        Gets the gpu_description of this Shape.
        A short description of the graphics processing unit (GPU) available for this shape.

        If the shape does not have any GPUs, this field is `null`.


        :return: The gpu_description of this Shape.
        :rtype: str
        """
        return self._gpu_description

    @gpu_description.setter
    def gpu_description(self, gpu_description):
        """
        Sets the gpu_description of this Shape.
        A short description of the graphics processing unit (GPU) available for this shape.

        If the shape does not have any GPUs, this field is `null`.


        :param gpu_description: The gpu_description of this Shape.
        :type: str
        """
        self._gpu_description = gpu_description

    @property
    def local_disks(self):
        """
        Gets the local_disks of this Shape.
        The number of local disks available for this shape.


        :return: The local_disks of this Shape.
        :rtype: int
        """
        return self._local_disks

    @local_disks.setter
    def local_disks(self, local_disks):
        """
        Sets the local_disks of this Shape.
        The number of local disks available for this shape.


        :param local_disks: The local_disks of this Shape.
        :type: int
        """
        self._local_disks = local_disks

    @property
    def local_disks_total_size_in_gbs(self):
        """
        Gets the local_disks_total_size_in_gbs of this Shape.
        The aggregate size of the local disks available for this shape, in gigabytes.

        If the shape does not have any local disks, this field is `null`.


        :return: The local_disks_total_size_in_gbs of this Shape.
        :rtype: float
        """
        return self._local_disks_total_size_in_gbs

    @local_disks_total_size_in_gbs.setter
    def local_disks_total_size_in_gbs(self, local_disks_total_size_in_gbs):
        """
        Sets the local_disks_total_size_in_gbs of this Shape.
        The aggregate size of the local disks available for this shape, in gigabytes.

        If the shape does not have any local disks, this field is `null`.


        :param local_disks_total_size_in_gbs: The local_disks_total_size_in_gbs of this Shape.
        :type: float
        """
        self._local_disks_total_size_in_gbs = local_disks_total_size_in_gbs

    @property
    def local_disk_description(self):
        """
        Gets the local_disk_description of this Shape.
        A short description of the local disks available for this shape.

        If the shape does not have any local disks, this field is `null`.


        :return: The local_disk_description of this Shape.
        :rtype: str
        """
        return self._local_disk_description

    @local_disk_description.setter
    def local_disk_description(self, local_disk_description):
        """
        Sets the local_disk_description of this Shape.
        A short description of the local disks available for this shape.

        If the shape does not have any local disks, this field is `null`.


        :param local_disk_description: The local_disk_description of this Shape.
        :type: str
        """
        self._local_disk_description = local_disk_description

    @property
    def ocpu_options(self):
        """
        Gets the ocpu_options of this Shape.

        :return: The ocpu_options of this Shape.
        :rtype: ShapeOcpuOptions
        """
        return self._ocpu_options

    @ocpu_options.setter
    def ocpu_options(self, ocpu_options):
        """
        Sets the ocpu_options of this Shape.

        :param ocpu_options: The ocpu_options of this Shape.
        :type: ShapeOcpuOptions
        """
        self._ocpu_options = ocpu_options

    @property
    def memory_options(self):
        """
        Gets the memory_options of this Shape.

        :return: The memory_options of this Shape.
        :rtype: ShapeMemoryOptions
        """
        return self._memory_options

    @memory_options.setter
    def memory_options(self, memory_options):
        """
        Sets the memory_options of this Shape.

        :param memory_options: The memory_options of this Shape.
        :type: ShapeMemoryOptions
        """
        self._memory_options = memory_options

    @property
    def networking_bandwidth_options(self):
        """
        Gets the networking_bandwidth_options of this Shape.

        :return: The networking_bandwidth_options of this Shape.
        :rtype: ShapeNetworkingBandwidthOptions
        """
        return self._networking_bandwidth_options

    @networking_bandwidth_options.setter
    def networking_bandwidth_options(self, networking_bandwidth_options):
        """
        Sets the networking_bandwidth_options of this Shape.

        :param networking_bandwidth_options: The networking_bandwidth_options of this Shape.
        :type: ShapeNetworkingBandwidthOptions
        """
        self._networking_bandwidth_options = networking_bandwidth_options

    @property
    def max_vnic_attachment_options(self):
        """
        Gets the max_vnic_attachment_options of this Shape.

        :return: The max_vnic_attachment_options of this Shape.
        :rtype: ShapeMaxVnicAttachmentOptions
        """
        return self._max_vnic_attachment_options

    @max_vnic_attachment_options.setter
    def max_vnic_attachment_options(self, max_vnic_attachment_options):
        """
        Sets the max_vnic_attachment_options of this Shape.

        :param max_vnic_attachment_options: The max_vnic_attachment_options of this Shape.
        :type: ShapeMaxVnicAttachmentOptions
        """
        self._max_vnic_attachment_options = max_vnic_attachment_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
