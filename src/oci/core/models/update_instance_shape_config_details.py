# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInstanceShapeConfigDetails(object):
    """
    The shape configuration requested for the instance. If provided, the instance will be updated
    with the resources specified. In the case where some properties are missing,
    the missing values will be set to the default for the provided `shape`.

    Each shape only supports certain configurable values. If the `shape` is provided
    and the configuration values are invalid for that new `shape`, an error will be returned.
    If no `shape` is provided and the configuration values are invalid for the instance's
    existing shape, an error will be returned.
    """

    #: A constant which can be used with the baseline_ocpu_utilization property of a UpdateInstanceShapeConfigDetails.
    #: This constant has a value of "BASELINE_1_8"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_8 = "BASELINE_1_8"

    #: A constant which can be used with the baseline_ocpu_utilization property of a UpdateInstanceShapeConfigDetails.
    #: This constant has a value of "BASELINE_1_2"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_2 = "BASELINE_1_2"

    #: A constant which can be used with the baseline_ocpu_utilization property of a UpdateInstanceShapeConfigDetails.
    #: This constant has a value of "BASELINE_1_1"
    BASELINE_OCPU_UTILIZATION_BASELINE_1_1 = "BASELINE_1_1"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInstanceShapeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ocpus:
            The value to assign to the ocpus property of this UpdateInstanceShapeConfigDetails.
        :type ocpus: float

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this UpdateInstanceShapeConfigDetails.
        :type memory_in_gbs: float

        :param baseline_ocpu_utilization:
            The value to assign to the baseline_ocpu_utilization property of this UpdateInstanceShapeConfigDetails.
            Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"
        :type baseline_ocpu_utilization: str

        """
        self.swagger_types = {
            'ocpus': 'float',
            'memory_in_gbs': 'float',
            'baseline_ocpu_utilization': 'str'
        }

        self.attribute_map = {
            'ocpus': 'ocpus',
            'memory_in_gbs': 'memoryInGBs',
            'baseline_ocpu_utilization': 'baselineOcpuUtilization'
        }

        self._ocpus = None
        self._memory_in_gbs = None
        self._baseline_ocpu_utilization = None

    @property
    def ocpus(self):
        """
        Gets the ocpus of this UpdateInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :return: The ocpus of this UpdateInstanceShapeConfigDetails.
        :rtype: float
        """
        return self._ocpus

    @ocpus.setter
    def ocpus(self, ocpus):
        """
        Sets the ocpus of this UpdateInstanceShapeConfigDetails.
        The total number of OCPUs available to the instance.


        :param ocpus: The ocpus of this UpdateInstanceShapeConfigDetails.
        :type: float
        """
        self._ocpus = ocpus

    @property
    def memory_in_gbs(self):
        """
        Gets the memory_in_gbs of this UpdateInstanceShapeConfigDetails.
        The total amount of memory available to the instance, in gigabytes.


        :return: The memory_in_gbs of this UpdateInstanceShapeConfigDetails.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this UpdateInstanceShapeConfigDetails.
        The total amount of memory available to the instance, in gigabytes.


        :param memory_in_gbs: The memory_in_gbs of this UpdateInstanceShapeConfigDetails.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def baseline_ocpu_utilization(self):
        """
        Gets the baseline_ocpu_utilization of this UpdateInstanceShapeConfigDetails.
        The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
        non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.

        Allowed values for this property are: "BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"


        :return: The baseline_ocpu_utilization of this UpdateInstanceShapeConfigDetails.
        :rtype: str
        """
        return self._baseline_ocpu_utilization

    @baseline_ocpu_utilization.setter
    def baseline_ocpu_utilization(self, baseline_ocpu_utilization):
        """
        Sets the baseline_ocpu_utilization of this UpdateInstanceShapeConfigDetails.
        The baseline OCPU utilization for a subcore burstable VM instance. Leave this attribute blank for a
        non-burstable instance, or explicitly specify non-burstable with `BASELINE_1_1`.

        The following values are supported:
        - `BASELINE_1_8` - baseline usage is 1/8 of an OCPU.
        - `BASELINE_1_2` - baseline usage is 1/2 of an OCPU.
        - `BASELINE_1_1` - baseline usage is an entire OCPU. This represents a non-burstable instance.


        :param baseline_ocpu_utilization: The baseline_ocpu_utilization of this UpdateInstanceShapeConfigDetails.
        :type: str
        """
        allowed_values = ["BASELINE_1_8", "BASELINE_1_2", "BASELINE_1_1"]
        if not value_allowed_none_or_none_sentinel(baseline_ocpu_utilization, allowed_values):
            raise ValueError(
                "Invalid value for `baseline_ocpu_utilization`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._baseline_ocpu_utilization = baseline_ocpu_utilization

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
