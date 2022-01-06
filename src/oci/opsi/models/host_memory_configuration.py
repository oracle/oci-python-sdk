# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostMemoryConfiguration(HostConfigurationMetricGroup):
    """
    Memory Configuration metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostMemoryConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostMemoryConfiguration.metric_name` attribute
        of this class is ``HOST_MEMORY_CONFIGURATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostMemoryConfiguration.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostMemoryConfiguration.
        :type time_collected: datetime

        :param page_size_in_kb:
            The value to assign to the page_size_in_kb property of this HostMemoryConfiguration.
        :type page_size_in_kb: float

        :param page_tables_in_kb:
            The value to assign to the page_tables_in_kb property of this HostMemoryConfiguration.
        :type page_tables_in_kb: float

        :param swap_total_in_kb:
            The value to assign to the swap_total_in_kb property of this HostMemoryConfiguration.
        :type swap_total_in_kb: float

        :param huge_page_size_in_kb:
            The value to assign to the huge_page_size_in_kb property of this HostMemoryConfiguration.
        :type huge_page_size_in_kb: float

        :param huge_pages_total:
            The value to assign to the huge_pages_total property of this HostMemoryConfiguration.
        :type huge_pages_total: int

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'page_size_in_kb': 'float',
            'page_tables_in_kb': 'float',
            'swap_total_in_kb': 'float',
            'huge_page_size_in_kb': 'float',
            'huge_pages_total': 'int'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'page_size_in_kb': 'pageSizeInKB',
            'page_tables_in_kb': 'pageTablesInKB',
            'swap_total_in_kb': 'swapTotalInKB',
            'huge_page_size_in_kb': 'hugePageSizeInKB',
            'huge_pages_total': 'hugePagesTotal'
        }

        self._metric_name = None
        self._time_collected = None
        self._page_size_in_kb = None
        self._page_tables_in_kb = None
        self._swap_total_in_kb = None
        self._huge_page_size_in_kb = None
        self._huge_pages_total = None
        self._metric_name = 'HOST_MEMORY_CONFIGURATION'

    @property
    def page_size_in_kb(self):
        """
        Gets the page_size_in_kb of this HostMemoryConfiguration.
        Page size in kilobytes


        :return: The page_size_in_kb of this HostMemoryConfiguration.
        :rtype: float
        """
        return self._page_size_in_kb

    @page_size_in_kb.setter
    def page_size_in_kb(self, page_size_in_kb):
        """
        Sets the page_size_in_kb of this HostMemoryConfiguration.
        Page size in kilobytes


        :param page_size_in_kb: The page_size_in_kb of this HostMemoryConfiguration.
        :type: float
        """
        self._page_size_in_kb = page_size_in_kb

    @property
    def page_tables_in_kb(self):
        """
        Gets the page_tables_in_kb of this HostMemoryConfiguration.
        Amount of memory used for page tables in kilobytes


        :return: The page_tables_in_kb of this HostMemoryConfiguration.
        :rtype: float
        """
        return self._page_tables_in_kb

    @page_tables_in_kb.setter
    def page_tables_in_kb(self, page_tables_in_kb):
        """
        Sets the page_tables_in_kb of this HostMemoryConfiguration.
        Amount of memory used for page tables in kilobytes


        :param page_tables_in_kb: The page_tables_in_kb of this HostMemoryConfiguration.
        :type: float
        """
        self._page_tables_in_kb = page_tables_in_kb

    @property
    def swap_total_in_kb(self):
        """
        Gets the swap_total_in_kb of this HostMemoryConfiguration.
        Amount of total swap space in kilobytes


        :return: The swap_total_in_kb of this HostMemoryConfiguration.
        :rtype: float
        """
        return self._swap_total_in_kb

    @swap_total_in_kb.setter
    def swap_total_in_kb(self, swap_total_in_kb):
        """
        Sets the swap_total_in_kb of this HostMemoryConfiguration.
        Amount of total swap space in kilobytes


        :param swap_total_in_kb: The swap_total_in_kb of this HostMemoryConfiguration.
        :type: float
        """
        self._swap_total_in_kb = swap_total_in_kb

    @property
    def huge_page_size_in_kb(self):
        """
        Gets the huge_page_size_in_kb of this HostMemoryConfiguration.
        Size of huge pages in kilobytes


        :return: The huge_page_size_in_kb of this HostMemoryConfiguration.
        :rtype: float
        """
        return self._huge_page_size_in_kb

    @huge_page_size_in_kb.setter
    def huge_page_size_in_kb(self, huge_page_size_in_kb):
        """
        Sets the huge_page_size_in_kb of this HostMemoryConfiguration.
        Size of huge pages in kilobytes


        :param huge_page_size_in_kb: The huge_page_size_in_kb of this HostMemoryConfiguration.
        :type: float
        """
        self._huge_page_size_in_kb = huge_page_size_in_kb

    @property
    def huge_pages_total(self):
        """
        Gets the huge_pages_total of this HostMemoryConfiguration.
        Total number of huge pages


        :return: The huge_pages_total of this HostMemoryConfiguration.
        :rtype: int
        """
        return self._huge_pages_total

    @huge_pages_total.setter
    def huge_pages_total(self, huge_pages_total):
        """
        Sets the huge_pages_total of this HostMemoryConfiguration.
        Total number of huge pages


        :param huge_pages_total: The huge_pages_total of this HostMemoryConfiguration.
        :type: int
        """
        self._huge_pages_total = huge_pages_total

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
