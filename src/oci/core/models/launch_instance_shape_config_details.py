# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LaunchInstanceShapeConfigDetails(object):
    """
    The shape configuration requested for the instance.

    If the parameter is provided, the instance is created with the resources that you specify. If some
    properties are missing or the entire parameter is not provided, the instance is created
    with the default configuration values for the `shape` that you specify.

    Each shape only supports certain configurable values. If the values that you provide are not valid for the
    specified `shape`, an error is returned.
    """

    #: A constant which can be used with the baseline_ocpu_utilization property of a LaunchInstanceShapeConfigDetails.
    #: This constant has a value of "BASELINE_1_8"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_8 = "BASELINE_1_8"

    #: A constant which can be used with the baseline_ocpu_utilization property of a LaunchInstanceShapeConfigDetails.
    #: This constant has a value of "BASELINE_1_2"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_2 = "BASELINE_1_2"

    #: A constant which can be used with the baseline_ocpu_utilization property of a LaunchInstanceShapeConfigDetails.
    #: This constant has a value of "BASELINE_1_1"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_1 = "BASELINE_1_1"

    def __init__(self, **kwargs):
        """
        Initializes a new LaunchInstanceShapeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this LaunchInstanceShapeConfigDetails.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this LaunchInstanceShapeConfigDetails.
        :type memory_in_gbs: float

        :param baseline_ocpu_utilization:
            The value to assign to the baseline_ocpu_utilization property of this LaunchInstanceShapeConfigDetails.
            Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"
        :type baseline_ocpu_utilization: str

        :param nvmes:
            The value to assign to the nvmes property of this LaunchInstanceShapeConfigDetails.
        :type nvmes: int

        """
        self.swagger_types = {
            'ocpus': 'float',
            'memory_in_gbs': 'float',
            'baseline_ocpu_utilization': 'str',
            'nvmes': 'int'
        }

        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'baseline_ocpu_utilization': 'baselineOcpuUtilization',
            'nvmes': 'nvmes'
        }

        self._ocpus = None
        self._memory_in_gbs = None
        self._baseline_ocpu_utilization = None
        self._nvmes = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this LaunchInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :return: The ocpus of this LaunchInstanceShapeConfigDetails.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this LaunchInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :param ocpus: The ocpus of this LaunchInstanceShapeConfigDetails.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this LaunchInstanceShapeConfigDetails.
        The total amount of memory available to the instance, in gigabytes.


        :return: The memory_in_gbs of this LaunchInstanceShapeConfigDetails.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this LaunchInstanceShapeConfigDetails.
        The total amount of memory available to the instance, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this LaunchInstanceShapeConfigDetails.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def baseline_ocpu_utilization(self):
        """
        Gets the baseline_ocpu_utilization of this LaunchInstanceShapeConfigDetails.
        The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
        non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.

        Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"


        :return: The baseline_ocpu_utilization of this LaunchInstanceShapeConfigDetails.
        :rtype: str
        """
        return self._baseline_ocpu_utilization

    @baseline_ocpu_utilization.setter
    def baseline_ocpu_utilization(self, baseline_ocpu_utilization):
        """
        Sets the baseline_ocpu_utilization of this LaunchInstanceShapeConfigDetails.
        The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
        non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.


        :param baseline_ocpu_utilization: The baseline_ocpu_utilization of this LaunchInstanceShapeConfigDetails.
        :type: str
        """
        allowed_values = ["BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"]
        if not value_allowed_none_or_none_sentinel(baseline_ocpu_utilization, allowed_values):
            raise ValueError(
                "Invalid value for `baseline_ocpu_utilization`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._baseline_ocpu_utilization = baseline_ocpu_utilization

    @property
    def nvmes(self):
        """
        Gets the nvmes of this LaunchInstanceShapeConfigDetails.
        The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.


        :return: The nvmes of this LaunchInstanceShapeConfigDetails.
        :rtype: int
        """
        return self._nvmes

    @nvmes.setter
    def nvmes(self, nvmes):
        """
        Sets the nvmes of this LaunchInstanceShapeConfigDetails.
        The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.


        :param nvmes: The nvmes of this LaunchInstanceShapeConfigDetails.
        :type: int
        """
        self._nvmes = nvmes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
