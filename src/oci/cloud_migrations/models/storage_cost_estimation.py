# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StorageCostEstimation(object):
    """
    Cost estimation for storage
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StorageCostEstimation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param volumes:
            The value to assign to the volumes property of this StorageCostEstimation.
        :type volumes: list[oci.cloud_migrations.models.VolumeCostEstimation]

        :param total_gb_per_month:
            The value to assign to the total_gb_per_month property of this StorageCostEstimation.
        :type total_gb_per_month: float

        :param total_gb_per_month_by_subscription:
            The value to assign to the total_gb_per_month_by_subscription property of this StorageCostEstimation.
        :type total_gb_per_month_by_subscription: float

        """
        self.swagger_types = {
            'volumes': 'list[VolumeCostEstimation]',
            'total_gb_per_month': 'float',
            'total_gb_per_month_by_subscription': 'float'
        }

        self.attribute_map = {
            'volumes': 'volumes',
            'total_gb_per_month': 'totalGbPerMonth',
            'total_gb_per_month_by_subscription': 'totalGbPerMonthBySubscription'
        }

        self._volumes = None
        self._total_gb_per_month = None
        self._total_gb_per_month_by_subscription = None

    @property
    def volumes(self):
        """
        **[Required]** Gets the volumes of this StorageCostEstimation.
        Volume estimation


        :return: The volumes of this StorageCostEstimation.
        :rtype: list[oci.cloud_migrations.models.VolumeCostEstimation]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this StorageCostEstimation.
        Volume estimation


        :param volumes: The volumes of this StorageCostEstimation.
        :type: list[oci.cloud_migrations.models.VolumeCostEstimation]
        """
        self._volumes = volumes

    @property
    def total_gb_per_month(self):
        """
        **[Required]** Gets the total_gb_per_month of this StorageCostEstimation.
        Gigabyte storage capacity per month.


        :return: The total_gb_per_month of this StorageCostEstimation.
        :rtype: float
        """
        return self._total_gb_per_month

    @total_gb_per_month.setter
    def total_gb_per_month(self, total_gb_per_month):
        """
        Sets the total_gb_per_month of this StorageCostEstimation.
        Gigabyte storage capacity per month.


        :param total_gb_per_month: The total_gb_per_month of this StorageCostEstimation.
        :type: float
        """
        self._total_gb_per_month = total_gb_per_month

    @property
    def total_gb_per_month_by_subscription(self):
        """
        Gets the total_gb_per_month_by_subscription of this StorageCostEstimation.
        Gigabyte storage capacity per month by subscription.


        :return: The total_gb_per_month_by_subscription of this StorageCostEstimation.
        :rtype: float
        """
        return self._total_gb_per_month_by_subscription

    @total_gb_per_month_by_subscription.setter
    def total_gb_per_month_by_subscription(self, total_gb_per_month_by_subscription):
        """
        Sets the total_gb_per_month_by_subscription of this StorageCostEstimation.
        Gigabyte storage capacity per month by subscription.


        :param total_gb_per_month_by_subscription: The total_gb_per_month_by_subscription of this StorageCostEstimation.
        :type: float
        """
        self._total_gb_per_month_by_subscription = total_gb_per_month_by_subscription

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
