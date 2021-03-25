# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UsageSummary(object):
    """
    The usage store result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UsageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this UsageSummary.
        :type tenant_id: str

        :param tenant_name:
            The value to assign to the tenant_name property of this UsageSummary.
        :type tenant_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this UsageSummary.
        :type compartment_id: str

        :param compartment_path:
            The value to assign to the compartment_path property of this UsageSummary.
        :type compartment_path: str

        :param compartment_name:
            The value to assign to the compartment_name property of this UsageSummary.
        :type compartment_name: str

        :param service:
            The value to assign to the service property of this UsageSummary.
        :type service: str

        :param resource_name:
            The value to assign to the resource_name property of this UsageSummary.
        :type resource_name: str

        :param resource_id:
            The value to assign to the resource_id property of this UsageSummary.
        :type resource_id: str

        :param region:
            The value to assign to the region property of this UsageSummary.
        :type region: str

        :param ad:
            The value to assign to the ad property of this UsageSummary.
        :type ad: str

        :param weight:
            The value to assign to the weight property of this UsageSummary.
        :type weight: float

        :param shape:
            The value to assign to the shape property of this UsageSummary.
        :type shape: str

        :param sku_part_number:
            The value to assign to the sku_part_number property of this UsageSummary.
        :type sku_part_number: str

        :param sku_name:
            The value to assign to the sku_name property of this UsageSummary.
        :type sku_name: str

        :param unit:
            The value to assign to the unit property of this UsageSummary.
        :type unit: str

        :param discount:
            The value to assign to the discount property of this UsageSummary.
        :type discount: float

        :param list_rate:
            The value to assign to the list_rate property of this UsageSummary.
        :type list_rate: float

        :param platform:
            The value to assign to the platform property of this UsageSummary.
        :type platform: str

        :param time_usage_started:
            The value to assign to the time_usage_started property of this UsageSummary.
        :type time_usage_started: datetime

        :param time_usage_ended:
            The value to assign to the time_usage_ended property of this UsageSummary.
        :type time_usage_ended: datetime

        :param computed_amount:
            The value to assign to the computed_amount property of this UsageSummary.
        :type computed_amount: float

        :param computed_quantity:
            The value to assign to the computed_quantity property of this UsageSummary.
        :type computed_quantity: float

        :param overages_flag:
            The value to assign to the overages_flag property of this UsageSummary.
        :type overages_flag: str

        :param unit_price:
            The value to assign to the unit_price property of this UsageSummary.
        :type unit_price: float

        :param currency:
            The value to assign to the currency property of this UsageSummary.
        :type currency: str

        :param subscription_id:
            The value to assign to the subscription_id property of this UsageSummary.
        :type subscription_id: str

        :param overage:
            The value to assign to the overage property of this UsageSummary.
        :type overage: str

        :param is_forecast:
            The value to assign to the is_forecast property of this UsageSummary.
        :type is_forecast: bool

        :param tags:
            The value to assign to the tags property of this UsageSummary.
        :type tags: list[oci.usage_api.models.Tag]

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'tenant_name': 'str',
            'compartment_id': 'str',
            'compartment_path': 'str',
            'compartment_name': 'str',
            'service': 'str',
            'resource_name': 'str',
            'resource_id': 'str',
            'region': 'str',
            'ad': 'str',
            'weight': 'float',
            'shape': 'str',
            'sku_part_number': 'str',
            'sku_name': 'str',
            'unit': 'str',
            'discount': 'float',
            'list_rate': 'float',
            'platform': 'str',
            'time_usage_started': 'datetime',
            'time_usage_ended': 'datetime',
            'computed_amount': 'float',
            'computed_quantity': 'float',
            'overages_flag': 'str',
            'unit_price': 'float',
            'currency': 'str',
            'subscription_id': 'str',
            'overage': 'str',
            'is_forecast': 'bool',
            'tags': 'list[Tag]'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'tenant_name': 'tenantName',
            'compartment_id': 'compartmentId',
            'compartment_path': 'compartmentPath',
            'compartment_name': 'compartmentName',
            'service': 'service',
            'resource_name': 'resourceName',
            'resource_id': 'resourceId',
            'region': 'region',
            'ad': 'ad',
            'weight': 'weight',
            'shape': 'shape',
            'sku_part_number': 'skuPartNumber',
            'sku_name': 'skuName',
            'unit': 'unit',
            'discount': 'discount',
            'list_rate': 'listRate',
            'platform': 'platform',
            'time_usage_started': 'timeUsageStarted',
            'time_usage_ended': 'timeUsageEnded',
            'computed_amount': 'computedAmount',
            'computed_quantity': 'computedQuantity',
            'overages_flag': 'overagesFlag',
            'unit_price': 'unitPrice',
            'currency': 'currency',
            'subscription_id': 'subscriptionId',
            'overage': 'overage',
            'is_forecast': 'isForecast',
            'tags': 'tags'
        }

        self._tenant_id = None
        self._tenant_name = None
        self._compartment_id = None
        self._compartment_path = None
        self._compartment_name = None
        self._service = None
        self._resource_name = None
        self._resource_id = None
        self._region = None
        self._ad = None
        self._weight = None
        self._shape = None
        self._sku_part_number = None
        self._sku_name = None
        self._unit = None
        self._discount = None
        self._list_rate = None
        self._platform = None
        self._time_usage_started = None
        self._time_usage_ended = None
        self._computed_amount = None
        self._computed_quantity = None
        self._overages_flag = None
        self._unit_price = None
        self._currency = None
        self._subscription_id = None
        self._overage = None
        self._is_forecast = None
        self._tags = None

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this UsageSummary.
        The tenancy OCID.


        :return: The tenant_id of this UsageSummary.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this UsageSummary.
        The tenancy OCID.


        :param tenant_id: The tenant_id of this UsageSummary.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def tenant_name(self):
        """
        Gets the tenant_name of this UsageSummary.
        The tenancy name.


        :return: The tenant_name of this UsageSummary.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """
        Sets the tenant_name of this UsageSummary.
        The tenancy name.


        :param tenant_name: The tenant_name of this UsageSummary.
        :type: str
        """
        self._tenant_name = tenant_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UsageSummary.
        The compartment OCID.


        :return: The compartment_id of this UsageSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UsageSummary.
        The compartment OCID.


        :param compartment_id: The compartment_id of this UsageSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def compartment_path(self):
        """
        Gets the compartment_path of this UsageSummary.
        The compartment path, starting from root.


        :return: The compartment_path of this UsageSummary.
        :rtype: str
        """
        return self._compartment_path

    @compartment_path.setter
    def compartment_path(self, compartment_path):
        """
        Sets the compartment_path of this UsageSummary.
        The compartment path, starting from root.


        :param compartment_path: The compartment_path of this UsageSummary.
        :type: str
        """
        self._compartment_path = compartment_path

    @property
    def compartment_name(self):
        """
        Gets the compartment_name of this UsageSummary.
        The compartment name.


        :return: The compartment_name of this UsageSummary.
        :rtype: str
        """
        return self._compartment_name

    @compartment_name.setter
    def compartment_name(self, compartment_name):
        """
        Sets the compartment_name of this UsageSummary.
        The compartment name.


        :param compartment_name: The compartment_name of this UsageSummary.
        :type: str
        """
        self._compartment_name = compartment_name

    @property
    def service(self):
        """
        Gets the service of this UsageSummary.
        The service name that is incurring the cost.


        :return: The service of this UsageSummary.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this UsageSummary.
        The service name that is incurring the cost.


        :param service: The service of this UsageSummary.
        :type: str
        """
        self._service = service

    @property
    def resource_name(self):
        """
        Gets the resource_name of this UsageSummary.
        The resource name that is incurring the cost.


        :return: The resource_name of this UsageSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this UsageSummary.
        The resource name that is incurring the cost.


        :param resource_name: The resource_name of this UsageSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        """
        Gets the resource_id of this UsageSummary.
        The resource OCID that is incurring the cost.


        :return: The resource_id of this UsageSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this UsageSummary.
        The resource OCID that is incurring the cost.


        :param resource_id: The resource_id of this UsageSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def region(self):
        """
        Gets the region of this UsageSummary.
        The region of the usage.


        :return: The region of this UsageSummary.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this UsageSummary.
        The region of the usage.


        :param region: The region of this UsageSummary.
        :type: str
        """
        self._region = region

    @property
    def ad(self):
        """
        Gets the ad of this UsageSummary.
        The availability domain of the usage.


        :return: The ad of this UsageSummary.
        :rtype: str
        """
        return self._ad

    @ad.setter
    def ad(self, ad):
        """
        Sets the ad of this UsageSummary.
        The availability domain of the usage.


        :param ad: The ad of this UsageSummary.
        :type: str
        """
        self._ad = ad

    @property
    def weight(self):
        """
        Gets the weight of this UsageSummary.
        The resource size being metered.


        :return: The weight of this UsageSummary.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this UsageSummary.
        The resource size being metered.


        :param weight: The weight of this UsageSummary.
        :type: float
        """
        self._weight = weight

    @property
    def shape(self):
        """
        Gets the shape of this UsageSummary.
        The resource shape.


        :return: The shape of this UsageSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this UsageSummary.
        The resource shape.


        :param shape: The shape of this UsageSummary.
        :type: str
        """
        self._shape = shape

    @property
    def sku_part_number(self):
        """
        Gets the sku_part_number of this UsageSummary.
        The SKU part number.


        :return: The sku_part_number of this UsageSummary.
        :rtype: str
        """
        return self._sku_part_number

    @sku_part_number.setter
    def sku_part_number(self, sku_part_number):
        """
        Sets the sku_part_number of this UsageSummary.
        The SKU part number.


        :param sku_part_number: The sku_part_number of this UsageSummary.
        :type: str
        """
        self._sku_part_number = sku_part_number

    @property
    def sku_name(self):
        """
        Gets the sku_name of this UsageSummary.
        The SKU friendly name.


        :return: The sku_name of this UsageSummary.
        :rtype: str
        """
        return self._sku_name

    @sku_name.setter
    def sku_name(self, sku_name):
        """
        Sets the sku_name of this UsageSummary.
        The SKU friendly name.


        :param sku_name: The sku_name of this UsageSummary.
        :type: str
        """
        self._sku_name = sku_name

    @property
    def unit(self):
        """
        Gets the unit of this UsageSummary.
        The usage unit.


        :return: The unit of this UsageSummary.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this UsageSummary.
        The usage unit.


        :param unit: The unit of this UsageSummary.
        :type: str
        """
        self._unit = unit

    @property
    def discount(self):
        """
        Gets the discount of this UsageSummary.
        The discretionary discount applied to the SKU.


        :return: The discount of this UsageSummary.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """
        Sets the discount of this UsageSummary.
        The discretionary discount applied to the SKU.


        :param discount: The discount of this UsageSummary.
        :type: float
        """
        self._discount = discount

    @property
    def list_rate(self):
        """
        Gets the list_rate of this UsageSummary.
        The SKU list rate (not discount).


        :return: The list_rate of this UsageSummary.
        :rtype: float
        """
        return self._list_rate

    @list_rate.setter
    def list_rate(self, list_rate):
        """
        Sets the list_rate of this UsageSummary.
        The SKU list rate (not discount).


        :param list_rate: The list_rate of this UsageSummary.
        :type: float
        """
        self._list_rate = list_rate

    @property
    def platform(self):
        """
        Gets the platform of this UsageSummary.
        Platform for the cost.


        :return: The platform of this UsageSummary.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this UsageSummary.
        Platform for the cost.


        :param platform: The platform of this UsageSummary.
        :type: str
        """
        self._platform = platform

    @property
    def time_usage_started(self):
        """
        **[Required]** Gets the time_usage_started of this UsageSummary.
        The usage start time.


        :return: The time_usage_started of this UsageSummary.
        :rtype: datetime
        """
        return self._time_usage_started

    @time_usage_started.setter
    def time_usage_started(self, time_usage_started):
        """
        Sets the time_usage_started of this UsageSummary.
        The usage start time.


        :param time_usage_started: The time_usage_started of this UsageSummary.
        :type: datetime
        """
        self._time_usage_started = time_usage_started

    @property
    def time_usage_ended(self):
        """
        **[Required]** Gets the time_usage_ended of this UsageSummary.
        The usage end time.


        :return: The time_usage_ended of this UsageSummary.
        :rtype: datetime
        """
        return self._time_usage_ended

    @time_usage_ended.setter
    def time_usage_ended(self, time_usage_ended):
        """
        Sets the time_usage_ended of this UsageSummary.
        The usage end time.


        :param time_usage_ended: The time_usage_ended of this UsageSummary.
        :type: datetime
        """
        self._time_usage_ended = time_usage_ended

    @property
    def computed_amount(self):
        """
        Gets the computed_amount of this UsageSummary.
        The computed cost.


        :return: The computed_amount of this UsageSummary.
        :rtype: float
        """
        return self._computed_amount

    @computed_amount.setter
    def computed_amount(self, computed_amount):
        """
        Sets the computed_amount of this UsageSummary.
        The computed cost.


        :param computed_amount: The computed_amount of this UsageSummary.
        :type: float
        """
        self._computed_amount = computed_amount

    @property
    def computed_quantity(self):
        """
        Gets the computed_quantity of this UsageSummary.
        The usage number.


        :return: The computed_quantity of this UsageSummary.
        :rtype: float
        """
        return self._computed_quantity

    @computed_quantity.setter
    def computed_quantity(self, computed_quantity):
        """
        Sets the computed_quantity of this UsageSummary.
        The usage number.


        :param computed_quantity: The computed_quantity of this UsageSummary.
        :type: float
        """
        self._computed_quantity = computed_quantity

    @property
    def overages_flag(self):
        """
        Gets the overages_flag of this UsageSummary.
        The SPM OverageFlag.


        :return: The overages_flag of this UsageSummary.
        :rtype: str
        """
        return self._overages_flag

    @overages_flag.setter
    def overages_flag(self, overages_flag):
        """
        Sets the overages_flag of this UsageSummary.
        The SPM OverageFlag.


        :param overages_flag: The overages_flag of this UsageSummary.
        :type: str
        """
        self._overages_flag = overages_flag

    @property
    def unit_price(self):
        """
        Gets the unit_price of this UsageSummary.
        The price per unit.


        :return: The unit_price of this UsageSummary.
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this UsageSummary.
        The price per unit.


        :param unit_price: The unit_price of this UsageSummary.
        :type: float
        """
        self._unit_price = unit_price

    @property
    def currency(self):
        """
        Gets the currency of this UsageSummary.
        The price currency.


        :return: The currency of this UsageSummary.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this UsageSummary.
        The price currency.


        :param currency: The currency of this UsageSummary.
        :type: str
        """
        self._currency = currency

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this UsageSummary.
        The subscription ID.


        :return: The subscription_id of this UsageSummary.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this UsageSummary.
        The subscription ID.


        :param subscription_id: The subscription_id of this UsageSummary.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def overage(self):
        """
        Gets the overage of this UsageSummary.
        The overage usage.


        :return: The overage of this UsageSummary.
        :rtype: str
        """
        return self._overage

    @overage.setter
    def overage(self, overage):
        """
        Sets the overage of this UsageSummary.
        The overage usage.


        :param overage: The overage of this UsageSummary.
        :type: str
        """
        self._overage = overage

    @property
    def is_forecast(self):
        """
        Gets the is_forecast of this UsageSummary.
        is forecasted data


        :return: The is_forecast of this UsageSummary.
        :rtype: bool
        """
        return self._is_forecast

    @is_forecast.setter
    def is_forecast(self, is_forecast):
        """
        Sets the is_forecast of this UsageSummary.
        is forecasted data


        :param is_forecast: The is_forecast of this UsageSummary.
        :type: bool
        """
        self._is_forecast = is_forecast

    @property
    def tags(self):
        """
        Gets the tags of this UsageSummary.
        For grouping, a tag definition. For filtering, a definition and key.


        :return: The tags of this UsageSummary.
        :rtype: list[oci.usage_api.models.Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UsageSummary.
        For grouping, a tag definition. For filtering, a definition and key.


        :param tags: The tags of this UsageSummary.
        :type: list[oci.usage_api.models.Tag]
        """
        self._tags = tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
