# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CostEstimation(object):
    """
    Cost estimation description
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CostEstimation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compute:
            The value to assign to the compute property of this CostEstimation.
        :type compute: oci.cloud_migrations.models.ComputeCostEstimation

        :param storage:
            The value to assign to the storage property of this CostEstimation.
        :type storage: oci.cloud_migrations.models.StorageCostEstimation

        :param os_image:
            The value to assign to the os_image property of this CostEstimation.
        :type os_image: oci.cloud_migrations.models.OsImageEstimation

        :param currency_code:
            The value to assign to the currency_code property of this CostEstimation.
        :type currency_code: str

        :param total_estimation_per_month:
            The value to assign to the total_estimation_per_month property of this CostEstimation.
        :type total_estimation_per_month: float

        :param total_estimation_per_month_by_subscription:
            The value to assign to the total_estimation_per_month_by_subscription property of this CostEstimation.
        :type total_estimation_per_month_by_subscription: float

        :param subscription_id:
            The value to assign to the subscription_id property of this CostEstimation.
        :type subscription_id: str

        """
        self.swagger_types = {
            'compute': 'ComputeCostEstimation',
            'storage': 'StorageCostEstimation',
            'os_image': 'OsImageEstimation',
            'currency_code': 'str',
            'total_estimation_per_month': 'float',
            'total_estimation_per_month_by_subscription': 'float',
            'subscription_id': 'str'
        }

        self.attribute_map = {
            'compute': 'compute',
            'storage': 'storage',
            'os_image': 'osImage',
            'currency_code': 'currencyCode',
            'total_estimation_per_month': 'totalEstimationPerMonth',
            'total_estimation_per_month_by_subscription': 'totalEstimationPerMonthBySubscription',
            'subscription_id': 'subscriptionId'
        }

        self._compute = None
        self._storage = None
        self._os_image = None
        self._currency_code = None
        self._total_estimation_per_month = None
        self._total_estimation_per_month_by_subscription = None
        self._subscription_id = None

    @property
    def compute(self):
        """
        **[Required]** Gets the compute of this CostEstimation.

        :return: The compute of this CostEstimation.
        :rtype: oci.cloud_migrations.models.ComputeCostEstimation
        """
        return self._compute

    @compute.setter
    def compute(self, compute):
        """
        Sets the compute of this CostEstimation.

        :param compute: The compute of this CostEstimation.
        :type: oci.cloud_migrations.models.ComputeCostEstimation
        """
        self._compute = compute

    @property
    def storage(self):
        """
        **[Required]** Gets the storage of this CostEstimation.

        :return: The storage of this CostEstimation.
        :rtype: oci.cloud_migrations.models.StorageCostEstimation
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """
        Sets the storage of this CostEstimation.

        :param storage: The storage of this CostEstimation.
        :type: oci.cloud_migrations.models.StorageCostEstimation
        """
        self._storage = storage

    @property
    def os_image(self):
        """
        **[Required]** Gets the os_image of this CostEstimation.

        :return: The os_image of this CostEstimation.
        :rtype: oci.cloud_migrations.models.OsImageEstimation
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        """
        Sets the os_image of this CostEstimation.

        :param os_image: The os_image of this CostEstimation.
        :type: oci.cloud_migrations.models.OsImageEstimation
        """
        self._os_image = os_image

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CostEstimation.
        Currency code in the ISO format.


        :return: The currency_code of this CostEstimation.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CostEstimation.
        Currency code in the ISO format.


        :param currency_code: The currency_code of this CostEstimation.
        :type: str
        """
        self._currency_code = currency_code

    @property
    def total_estimation_per_month(self):
        """
        **[Required]** Gets the total_estimation_per_month of this CostEstimation.
        Total estimation per month


        :return: The total_estimation_per_month of this CostEstimation.
        :rtype: float
        """
        return self._total_estimation_per_month

    @total_estimation_per_month.setter
    def total_estimation_per_month(self, total_estimation_per_month):
        """
        Sets the total_estimation_per_month of this CostEstimation.
        Total estimation per month


        :param total_estimation_per_month: The total_estimation_per_month of this CostEstimation.
        :type: float
        """
        self._total_estimation_per_month = total_estimation_per_month

    @property
    def total_estimation_per_month_by_subscription(self):
        """
        Gets the total_estimation_per_month_by_subscription of this CostEstimation.
        Total estimation per month by subscription.


        :return: The total_estimation_per_month_by_subscription of this CostEstimation.
        :rtype: float
        """
        return self._total_estimation_per_month_by_subscription

    @total_estimation_per_month_by_subscription.setter
    def total_estimation_per_month_by_subscription(self, total_estimation_per_month_by_subscription):
        """
        Sets the total_estimation_per_month_by_subscription of this CostEstimation.
        Total estimation per month by subscription.


        :param total_estimation_per_month_by_subscription: The total_estimation_per_month_by_subscription of this CostEstimation.
        :type: float
        """
        self._total_estimation_per_month_by_subscription = total_estimation_per_month_by_subscription

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this CostEstimation.
        Subscription ID


        :return: The subscription_id of this CostEstimation.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this CostEstimation.
        Subscription ID


        :param subscription_id: The subscription_id of this CostEstimation.
        :type: str
        """
        self._subscription_id = subscription_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
