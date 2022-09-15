# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GpuDevice(object):
    """
    GPU device details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GpuDevice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this GpuDevice.
        :type name: str

        :param description:
            The value to assign to the description property of this GpuDevice.
        :type description: str

        :param cores_count:
            The value to assign to the cores_count property of this GpuDevice.
        :type cores_count: int

        :param memory_in_mbs:
            The value to assign to the memory_in_mbs property of this GpuDevice.
        :type memory_in_mbs: int

        :param manufacturer:
            The value to assign to the manufacturer property of this GpuDevice.
        :type manufacturer: str

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'cores_count': 'int',
            'memory_in_mbs': 'int',
            'manufacturer': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'cores_count': 'coresCount',
            'memory_in_mbs': 'memoryInMBs',
            'manufacturer': 'manufacturer'
        }

        self._name = None
        self._description = None
        self._cores_count = None
        self._memory_in_mbs = None
        self._manufacturer = None

    @property
    def name(self):
        """
        Gets the name of this GpuDevice.
        GPU device name.


        :return: The name of this GpuDevice.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GpuDevice.
        GPU device name.


        :param name: The name of this GpuDevice.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this GpuDevice.
        GPU device description.


        :return: The description of this GpuDevice.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GpuDevice.
        GPU device description.


        :param description: The description of this GpuDevice.
        :type: str
        """
        self._description = description

    @property
    def cores_count(self):
        """
        Gets the cores_count of this GpuDevice.
        Number of GPU cores.


        :return: The cores_count of this GpuDevice.
        :rtype: int
        """
        return self._cores_count

    @cores_count.setter
    def cores_count(self, cores_count):
        """
        Sets the cores_count of this GpuDevice.
        Number of GPU cores.


        :param cores_count: The cores_count of this GpuDevice.
        :type: int
        """
        self._cores_count = cores_count

    @property
    def memory_in_mbs(self):
        """
        Gets the memory_in_mbs of this GpuDevice.
        GPU memory size in MBs.


        :return: The memory_in_mbs of this GpuDevice.
        :rtype: int
        """
        return self._memory_in_mbs

    @memory_in_mbs.setter
    def memory_in_mbs(self, memory_in_mbs):
        """
        Sets the memory_in_mbs of this GpuDevice.
        GPU memory size in MBs.


        :param memory_in_mbs: The memory_in_mbs of this GpuDevice.
        :type: int
        """
        self._memory_in_mbs = memory_in_mbs

    @property
    def manufacturer(self):
        """
        Gets the manufacturer of this GpuDevice.
        The manufacturer of GPU.


        :return: The manufacturer of this GpuDevice.
        :rtype: str
        """
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        """
        Sets the manufacturer of this GpuDevice.
        The manufacturer of GPU.


        :param manufacturer: The manufacturer of this GpuDevice.
        :type: str
        """
        self._manufacturer = manufacturer

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
