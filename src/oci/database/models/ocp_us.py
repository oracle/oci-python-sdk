# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OCPUs(object):
    """
    The details of the available and consumed CPU cores of the Autonomous Exadata Infrastructure instance, including consumption by database workload type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OCPUs object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param total_cpu:
            The value to assign to the total_cpu property of this OCPUs.
        :type total_cpu: float

        :param consumed_cpu:
            The value to assign to the consumed_cpu property of this OCPUs.
        :type consumed_cpu: float

        :param by_workload_type:
            The value to assign to the by_workload_type property of this OCPUs.
        :type by_workload_type: WorkloadType

        """
        self.swagger_types = {
            'total_cpu': 'float',
            'consumed_cpu': 'float',
            'by_workload_type': 'WorkloadType'
        }

        self.attribute_map = {
            'total_cpu': 'totalCpu',
            'consumed_cpu': 'consumedCpu',
            'by_workload_type': 'byWorkloadType'
        }

        self._total_cpu = None
        self._consumed_cpu = None
        self._by_workload_type = None

    @property
    def total_cpu(self):
        """
        Gets the total_cpu of this OCPUs.
        The total number of OCPUs in the Autonomous Exadata Infrastructure instance.


        :return: The total_cpu of this OCPUs.
        :rtype: float
        """
        return self._total_cpu

    @total_cpu.setter
    def total_cpu(self, total_cpu):
        """
        Sets the total_cpu of this OCPUs.
        The total number of OCPUs in the Autonomous Exadata Infrastructure instance.


        :param total_cpu: The total_cpu of this OCPUs.
        :type: float
        """
        self._total_cpu = total_cpu

    @property
    def consumed_cpu(self):
        """
        Gets the consumed_cpu of this OCPUs.
        The total number of consumed OCPUs in the Autonomous Exadata Infrastructure instance.


        :return: The consumed_cpu of this OCPUs.
        :rtype: float
        """
        return self._consumed_cpu

    @consumed_cpu.setter
    def consumed_cpu(self, consumed_cpu):
        """
        Sets the consumed_cpu of this OCPUs.
        The total number of consumed OCPUs in the Autonomous Exadata Infrastructure instance.


        :param consumed_cpu: The consumed_cpu of this OCPUs.
        :type: float
        """
        self._consumed_cpu = consumed_cpu

    @property
    def by_workload_type(self):
        """
        Gets the by_workload_type of this OCPUs.

        :return: The by_workload_type of this OCPUs.
        :rtype: WorkloadType
        """
        return self._by_workload_type

    @by_workload_type.setter
    def by_workload_type(self, by_workload_type):
        """
        Sets the by_workload_type of this OCPUs.

        :param by_workload_type: The by_workload_type of this OCPUs.
        :type: WorkloadType
        """
        self._by_workload_type = by_workload_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
