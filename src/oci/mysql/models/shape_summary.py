# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeSummary(object):
    """
    The shape of the DB System. The shape determines resources to allocate
    to the DB System - CPU cores and memory for VM shapes; CPU cores, memory
    and storage for non-VM (or bare metal) shapes.  For a description of
    shapes, see `DB System Shape Options`__.

    __ https://docs.cloud.oracle.com/mysql-database/doc/shapes.htm
    """

    #: A constant which can be used with the is_supported_for property of a ShapeSummary.
    #: This constant has a value of "DBSYSTEM"
    IS_SUPPORTED_FOR_DBSYSTEM = "DBSYSTEM"

    #: A constant which can be used with the is_supported_for property of a ShapeSummary.
    #: This constant has a value of "ANALYTICSCLUSTER"
    IS_SUPPORTED_FOR_ANALYTICSCLUSTER = "ANALYTICSCLUSTER"

    #: A constant which can be used with the is_supported_for property of a ShapeSummary.
    #: This constant has a value of "HEATWAVECLUSTER"
    IS_SUPPORTED_FOR_HEATWAVECLUSTER = "HEATWAVECLUSTER"

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ShapeSummary.
        :type name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this ShapeSummary.
        :type cpu_core_count: int

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this ShapeSummary.
        :type memory_size_in_gbs: int

        :param is_supported_for:
            The value to assign to the is_supported_for property of this ShapeSummary.
            Allowed values for items in this list are: "DBSYSTEM", "ANALYTICSCLUSTER", "HEATWAVECLUSTER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type is_supported_for: list[str]

        """
        self.swagger_types = {
            'name': 'str',
            'cpu_core_count': 'int',
            'memory_size_in_gbs': 'int',
            'is_supported_for': 'list[str]'
        }

        self.attribute_map = {
            'name': 'name',
            'cpu_core_count': 'cpuCoreCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'is_supported_for': 'isSupportedFor'
        }

        self._name = None
        self._cpu_core_count = None
        self._memory_size_in_gbs = None
        self._is_supported_for = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ShapeSummary.
        The name of the shape used for the DB System.


        :return: The name of this ShapeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ShapeSummary.
        The name of the shape used for the DB System.


        :param name: The name of this ShapeSummary.
        :type: str
        """
        self._name = name

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this ShapeSummary.
        The number of CPU Cores the Instance provides. These are \"OCPU\"s.


        :return: The cpu_core_count of this ShapeSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this ShapeSummary.
        The number of CPU Cores the Instance provides. These are \"OCPU\"s.


        :param cpu_core_count: The cpu_core_count of this ShapeSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def memory_size_in_gbs(self):
        """
        **[Required]** Gets the memory_size_in_gbs of this ShapeSummary.
        The amount of RAM the Instance provides. This is an IEC base-2 number.


        :return: The memory_size_in_gbs of this ShapeSummary.
        :rtype: int
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this ShapeSummary.
        The amount of RAM the Instance provides. This is an IEC base-2 number.


        :param memory_size_in_gbs: The memory_size_in_gbs of this ShapeSummary.
        :type: int
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def is_supported_for(self):
        """
        Gets the is_supported_for of this ShapeSummary.
        What service features the shape is supported for.

        Allowed values for items in this list are: "DBSYSTEM", "ANALYTICSCLUSTER", "HEATWAVECLUSTER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The is_supported_for of this ShapeSummary.
        :rtype: list[str]
        """
        return self._is_supported_for

    @is_supported_for.setter
    def is_supported_for(self, is_supported_for):
        """
        Sets the is_supported_for of this ShapeSummary.
        What service features the shape is supported for.


        :param is_supported_for: The is_supported_for of this ShapeSummary.
        :type: list[str]
        """
        allowed_values = ["DBSYSTEM", "ANALYTICSCLUSTER", "HEATWAVECLUSTER"]
        if is_supported_for:
            is_supported_for[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in is_supported_for]
        self._is_supported_for = is_supported_for

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
