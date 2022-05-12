# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StoragePerformanceDetails(object):
    """
    Representation of storage performance detail parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StoragePerformanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this StoragePerformanceDetails.
        :type size_in_gbs: int

        :param balanced_disk_performance:
            The value to assign to the balanced_disk_performance property of this StoragePerformanceDetails.
        :type balanced_disk_performance: oci.database.models.DiskPerformanceDetails

        :param high_disk_performance:
            The value to assign to the high_disk_performance property of this StoragePerformanceDetails.
        :type high_disk_performance: oci.database.models.DiskPerformanceDetails

        """
        self.swagger_types = {
            'size_in_gbs': 'int',
            'balanced_disk_performance': 'DiskPerformanceDetails',
            'high_disk_performance': 'DiskPerformanceDetails'
        }

        self.attribute_map = {
            'size_in_gbs': 'sizeInGBs',
            'balanced_disk_performance': 'balancedDiskPerformance',
            'high_disk_performance': 'highDiskPerformance'
        }

        self._size_in_gbs = None
        self._balanced_disk_performance = None
        self._high_disk_performance = None

    @property
    def size_in_gbs(self):
        """
        **[Required]** Gets the size_in_gbs of this StoragePerformanceDetails.
        Size in GBs.


        :return: The size_in_gbs of this StoragePerformanceDetails.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this StoragePerformanceDetails.
        Size in GBs.


        :param size_in_gbs: The size_in_gbs of this StoragePerformanceDetails.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def balanced_disk_performance(self):
        """
        **[Required]** Gets the balanced_disk_performance of this StoragePerformanceDetails.

        :return: The balanced_disk_performance of this StoragePerformanceDetails.
        :rtype: oci.database.models.DiskPerformanceDetails
        """
        return self._balanced_disk_performance

    @balanced_disk_performance.setter
    def balanced_disk_performance(self, balanced_disk_performance):
        """
        Sets the balanced_disk_performance of this StoragePerformanceDetails.

        :param balanced_disk_performance: The balanced_disk_performance of this StoragePerformanceDetails.
        :type: oci.database.models.DiskPerformanceDetails
        """
        self._balanced_disk_performance = balanced_disk_performance

    @property
    def high_disk_performance(self):
        """
        **[Required]** Gets the high_disk_performance of this StoragePerformanceDetails.

        :return: The high_disk_performance of this StoragePerformanceDetails.
        :rtype: oci.database.models.DiskPerformanceDetails
        """
        return self._high_disk_performance

    @high_disk_performance.setter
    def high_disk_performance(self, high_disk_performance):
        """
        Sets the high_disk_performance of this StoragePerformanceDetails.

        :param high_disk_performance: The high_disk_performance of this StoragePerformanceDetails.
        :type: oci.database.models.DiskPerformanceDetails
        """
        self._high_disk_performance = high_disk_performance

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
