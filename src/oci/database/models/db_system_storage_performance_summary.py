# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemStoragePerformanceSummary(object):
    """
    Representation of storage performance summary per shapeType .
    """

    #: A constant which can be used with the shape_type property of a DbSystemStoragePerformanceSummary.
    #: This constant has a value of "AMD"
    SHAPE_TYPE_AMD = "AMD"

    #: A constant which can be used with the shape_type property of a DbSystemStoragePerformanceSummary.
    #: This constant has a value of "INTEL"
    SHAPE_TYPE_INTEL = "INTEL"

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemStoragePerformanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape_type:
            The value to assign to the shape_type property of this DbSystemStoragePerformanceSummary.
            Allowed values for this property are: "AMD", "INTEL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shape_type: str

        :param data_storage_performance_list:
            The value to assign to the data_storage_performance_list property of this DbSystemStoragePerformanceSummary.
        :type data_storage_performance_list: list[oci.database.models.StoragePerformanceDetails]

        :param reco_storage_performance_list:
            The value to assign to the reco_storage_performance_list property of this DbSystemStoragePerformanceSummary.
        :type reco_storage_performance_list: list[oci.database.models.StoragePerformanceDetails]

        """
        self.swagger_types = {
            'shape_type': 'str',
            'data_storage_performance_list': 'list[StoragePerformanceDetails]',
            'reco_storage_performance_list': 'list[StoragePerformanceDetails]'
        }

        self.attribute_map = {
            'shape_type': 'shapeType',
            'data_storage_performance_list': 'dataStoragePerformanceList',
            'reco_storage_performance_list': 'recoStoragePerformanceList'
        }

        self._shape_type = None
        self._data_storage_performance_list = None
        self._reco_storage_performance_list = None

    @property
    def shape_type(self):
        """
        **[Required]** Gets the shape_type of this DbSystemStoragePerformanceSummary.
        ShapeType of the DbSystems,INTEL or AMD

        Allowed values for this property are: "AMD", "INTEL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shape_type of this DbSystemStoragePerformanceSummary.
        :rtype: str
        """
        return self._shape_type

    @shape_type.setter
    def shape_type(self, shape_type):
        """
        Sets the shape_type of this DbSystemStoragePerformanceSummary.
        ShapeType of the DbSystems,INTEL or AMD


        :param shape_type: The shape_type of this DbSystemStoragePerformanceSummary.
        :type: str
        """
        allowed_values = ["AMD", "INTEL"]
        if not value_allowed_none_or_none_sentinel(shape_type, allowed_values):
            shape_type = 'UNKNOWN_ENUM_VALUE'
        self._shape_type = shape_type

    @property
    def data_storage_performance_list(self):
        """
        **[Required]** Gets the data_storage_performance_list of this DbSystemStoragePerformanceSummary.
        List of storage performance for the DATA disks


        :return: The data_storage_performance_list of this DbSystemStoragePerformanceSummary.
        :rtype: list[oci.database.models.StoragePerformanceDetails]
        """
        return self._data_storage_performance_list

    @data_storage_performance_list.setter
    def data_storage_performance_list(self, data_storage_performance_list):
        """
        Sets the data_storage_performance_list of this DbSystemStoragePerformanceSummary.
        List of storage performance for the DATA disks


        :param data_storage_performance_list: The data_storage_performance_list of this DbSystemStoragePerformanceSummary.
        :type: list[oci.database.models.StoragePerformanceDetails]
        """
        self._data_storage_performance_list = data_storage_performance_list

    @property
    def reco_storage_performance_list(self):
        """
        **[Required]** Gets the reco_storage_performance_list of this DbSystemStoragePerformanceSummary.
        List of storage performance for the RECO disks


        :return: The reco_storage_performance_list of this DbSystemStoragePerformanceSummary.
        :rtype: list[oci.database.models.StoragePerformanceDetails]
        """
        return self._reco_storage_performance_list

    @reco_storage_performance_list.setter
    def reco_storage_performance_list(self, reco_storage_performance_list):
        """
        Sets the reco_storage_performance_list of this DbSystemStoragePerformanceSummary.
        List of storage performance for the RECO disks


        :param reco_storage_performance_list: The reco_storage_performance_list of this DbSystemStoragePerformanceSummary.
        :type: list[oci.database.models.StoragePerformanceDetails]
        """
        self._reco_storage_performance_list = reco_storage_performance_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
