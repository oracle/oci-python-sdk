# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_resource_statistics import HostResourceStatistics
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostMemoryStatistics(HostResourceStatistics):
    """
    Contains memory statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostMemoryStatistics object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostMemoryStatistics.resource_name` attribute
        of this class is ``HOST_MEMORY_STATISTICS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param usage:
            The value to assign to the usage property of this HostMemoryStatistics.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this HostMemoryStatistics.
        :type capacity: float

        :param utilization_percent:
            The value to assign to the utilization_percent property of this HostMemoryStatistics.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this HostMemoryStatistics.
        :type usage_change_percent: float

        :param resource_name:
            The value to assign to the resource_name property of this HostMemoryStatistics.
            Allowed values for this property are: "HOST_CPU_STATISTICS", "HOST_MEMORY_STATISTICS"
        :type resource_name: str

        :param free_memory:
            The value to assign to the free_memory property of this HostMemoryStatistics.
        :type free_memory: float

        :param available_memory:
            The value to assign to the available_memory property of this HostMemoryStatistics.
        :type available_memory: float

        :param huge_pages_total:
            The value to assign to the huge_pages_total property of this HostMemoryStatistics.
        :type huge_pages_total: int

        :param huge_page_size_in_mb:
            The value to assign to the huge_page_size_in_mb property of this HostMemoryStatistics.
        :type huge_page_size_in_mb: float

        :param huge_pages_free:
            The value to assign to the huge_pages_free property of this HostMemoryStatistics.
        :type huge_pages_free: int

        :param huge_pages_reserved:
            The value to assign to the huge_pages_reserved property of this HostMemoryStatistics.
        :type huge_pages_reserved: int

        :param load:
            The value to assign to the load property of this HostMemoryStatistics.
        :type load: oci.opsi.models.SummaryStatistics

        """
        self.swagger_types = {
            'usage': 'float',
            'capacity': 'float',
            'utilization_percent': 'float',
            'usage_change_percent': 'float',
            'resource_name': 'str',
            'free_memory': 'float',
            'available_memory': 'float',
            'huge_pages_total': 'int',
            'huge_page_size_in_mb': 'float',
            'huge_pages_free': 'int',
            'huge_pages_reserved': 'int',
            'load': 'SummaryStatistics'
        }

        self.attribute_map = {
            'usage': 'usage',
            'capacity': 'capacity',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent',
            'resource_name': 'resourceName',
            'free_memory': 'freeMemory',
            'available_memory': 'availableMemory',
            'huge_pages_total': 'hugePagesTotal',
            'huge_page_size_in_mb': 'hugePageSizeInMB',
            'huge_pages_free': 'hugePagesFree',
            'huge_pages_reserved': 'hugePagesReserved',
            'load': 'load'
        }

        self._usage = None
        self._capacity = None
        self._utilization_percent = None
        self._usage_change_percent = None
        self._resource_name = None
        self._free_memory = None
        self._available_memory = None
        self._huge_pages_total = None
        self._huge_page_size_in_mb = None
        self._huge_pages_free = None
        self._huge_pages_reserved = None
        self._load = None
        self._resource_name = 'HOST_MEMORY_STATISTICS'

    @property
    def free_memory(self):
        """
        Gets the free_memory of this HostMemoryStatistics.

        :return: The free_memory of this HostMemoryStatistics.
        :rtype: float
        """
        return self._free_memory

    @free_memory.setter
    def free_memory(self, free_memory):
        """
        Sets the free_memory of this HostMemoryStatistics.

        :param free_memory: The free_memory of this HostMemoryStatistics.
        :type: float
        """
        self._free_memory = free_memory

    @property
    def available_memory(self):
        """
        Gets the available_memory of this HostMemoryStatistics.

        :return: The available_memory of this HostMemoryStatistics.
        :rtype: float
        """
        return self._available_memory

    @available_memory.setter
    def available_memory(self, available_memory):
        """
        Sets the available_memory of this HostMemoryStatistics.

        :param available_memory: The available_memory of this HostMemoryStatistics.
        :type: float
        """
        self._available_memory = available_memory

    @property
    def huge_pages_total(self):
        """
        Gets the huge_pages_total of this HostMemoryStatistics.
        Total number of huge pages.


        :return: The huge_pages_total of this HostMemoryStatistics.
        :rtype: int
        """
        return self._huge_pages_total

    @huge_pages_total.setter
    def huge_pages_total(self, huge_pages_total):
        """
        Sets the huge_pages_total of this HostMemoryStatistics.
        Total number of huge pages.


        :param huge_pages_total: The huge_pages_total of this HostMemoryStatistics.
        :type: int
        """
        self._huge_pages_total = huge_pages_total

    @property
    def huge_page_size_in_mb(self):
        """
        Gets the huge_page_size_in_mb of this HostMemoryStatistics.
        Size of huge pages in megabytes.


        :return: The huge_page_size_in_mb of this HostMemoryStatistics.
        :rtype: float
        """
        return self._huge_page_size_in_mb

    @huge_page_size_in_mb.setter
    def huge_page_size_in_mb(self, huge_page_size_in_mb):
        """
        Sets the huge_page_size_in_mb of this HostMemoryStatistics.
        Size of huge pages in megabytes.


        :param huge_page_size_in_mb: The huge_page_size_in_mb of this HostMemoryStatistics.
        :type: float
        """
        self._huge_page_size_in_mb = huge_page_size_in_mb

    @property
    def huge_pages_free(self):
        """
        Gets the huge_pages_free of this HostMemoryStatistics.
        Total number of available huge pages.


        :return: The huge_pages_free of this HostMemoryStatistics.
        :rtype: int
        """
        return self._huge_pages_free

    @huge_pages_free.setter
    def huge_pages_free(self, huge_pages_free):
        """
        Sets the huge_pages_free of this HostMemoryStatistics.
        Total number of available huge pages.


        :param huge_pages_free: The huge_pages_free of this HostMemoryStatistics.
        :type: int
        """
        self._huge_pages_free = huge_pages_free

    @property
    def huge_pages_reserved(self):
        """
        Gets the huge_pages_reserved of this HostMemoryStatistics.
        Total number of huge pages which are used or reserved.


        :return: The huge_pages_reserved of this HostMemoryStatistics.
        :rtype: int
        """
        return self._huge_pages_reserved

    @huge_pages_reserved.setter
    def huge_pages_reserved(self, huge_pages_reserved):
        """
        Sets the huge_pages_reserved of this HostMemoryStatistics.
        Total number of huge pages which are used or reserved.


        :param huge_pages_reserved: The huge_pages_reserved of this HostMemoryStatistics.
        :type: int
        """
        self._huge_pages_reserved = huge_pages_reserved

    @property
    def load(self):
        """
        Gets the load of this HostMemoryStatistics.

        :return: The load of this HostMemoryStatistics.
        :rtype: oci.opsi.models.SummaryStatistics
        """
        return self._load

    @load.setter
    def load(self, load):
        """
        Sets the load of this HostMemoryStatistics.

        :param load: The load of this HostMemoryStatistics.
        :type: oci.opsi.models.SummaryStatistics
        """
        self._load = load

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
