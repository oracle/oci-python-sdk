# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModelDeploymentShapeSummary(object):
    """
    The compute shape used to launch a model deployment compute instance.
    """

    #: A constant which can be used with the shape_series property of a ModelDeploymentShapeSummary.
    #: This constant has a value of "AMD_ROME"
    SHAPE_SERIES_AMD_ROME = "AMD_ROME"

    #: A constant which can be used with the shape_series property of a ModelDeploymentShapeSummary.
    #: This constant has a value of "INTEL_SKYLAKE"
    SHAPE_SERIES_INTEL_SKYLAKE = "INTEL_SKYLAKE"

    def __init__(self, **kwargs):
        """
        Initializes a new ModelDeploymentShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ModelDeploymentShapeSummary.
        :type name: str

        :param core_count:
            The value to assign to the core_count property of this ModelDeploymentShapeSummary.
        :type core_count: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this ModelDeploymentShapeSummary.
        :type memory_in_gbs: int

        :param shape_series:
            The value to assign to the shape_series property of this ModelDeploymentShapeSummary.
            Allowed values for this property are: "AMD_ROME", "INTEL_SKYLAKE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shape_series: str

        """
        self.swagger_types = {
            'name': 'str',
            'core_count': 'int',
            'memory_in_gbs': 'int',
            'shape_series': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'core_count': 'coreCount',
            'memory_in_gbs': 'memoryInGBs',
            'shape_series': 'shapeSeries'
        }

        self._name = None
        self._core_count = None
        self._memory_in_gbs = None
        self._shape_series = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModelDeploymentShapeSummary.
        The name of the model deployment shape.


        :return: The name of this ModelDeploymentShapeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModelDeploymentShapeSummary.
        The name of the model deployment shape.


        :param name: The name of this ModelDeploymentShapeSummary.
        :type: str
        """
        self._name = name

    @property
    def core_count(self):
        """
        **[Required]** Gets the core_count of this ModelDeploymentShapeSummary.
        The number of cores associated with this model deployment shape.


        :return: The core_count of this ModelDeploymentShapeSummary.
        :rtype: int
        """
        return self._core_count

    @core_count.setter
    def core_count(self, core_count):
        """
        Sets the core_count of this ModelDeploymentShapeSummary.
        The number of cores associated with this model deployment shape.


        :param core_count: The core_count of this ModelDeploymentShapeSummary.
        :type: int
        """
        self._core_count = core_count

    @property
    def memory_in_gbs(self):
        """
        **[Required]** Gets the memory_in_gbs of this ModelDeploymentShapeSummary.
        The amount of memory in GBs associated with this model deployment shape.


        :return: The memory_in_gbs of this ModelDeploymentShapeSummary.
        :rtype: int
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this ModelDeploymentShapeSummary.
        The amount of memory in GBs associated with this model deployment shape.


        :param memory_in_gbs: The memory_in_gbs of this ModelDeploymentShapeSummary.
        :type: int
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def shape_series(self):
        """
        **[Required]** Gets the shape_series of this ModelDeploymentShapeSummary.
        The family that the compute shape belongs to.

        Allowed values for this property are: "AMD_ROME", "INTEL_SKYLAKE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shape_series of this ModelDeploymentShapeSummary.
        :rtype: str
        """
        return self._shape_series

    @shape_series.setter
    def shape_series(self, shape_series):
        """
        Sets the shape_series of this ModelDeploymentShapeSummary.
        The family that the compute shape belongs to.


        :param shape_series: The shape_series of this ModelDeploymentShapeSummary.
        :type: str
        """
        allowed_values = ["AMD_ROME", "INTEL_SKYLAKE"]
        if not value_allowed_none_or_none_sentinel(shape_series, allowed_values):
            shape_series = 'UNKNOWN_ENUM_VALUE'
        self._shape_series = shape_series

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
