# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscriptionSku(object):
    """
    SKU information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscriptionSku object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sku:
            The value to assign to the sku property of this SubscriptionSku.
        :type sku: str

        :param quantity:
            The value to assign to the quantity property of this SubscriptionSku.
        :type quantity: int

        :param description:
            The value to assign to the description property of this SubscriptionSku.
        :type description: str

        :param gsi_order_line_id:
            The value to assign to the gsi_order_line_id property of this SubscriptionSku.
        :type gsi_order_line_id: str

        :param license_part_description:
            The value to assign to the license_part_description property of this SubscriptionSku.
        :type license_part_description: str

        :param metric_name:
            The value to assign to the metric_name property of this SubscriptionSku.
        :type metric_name: str

        :param is_base_service_component:
            The value to assign to the is_base_service_component property of this SubscriptionSku.
        :type is_base_service_component: bool

        :param is_additional_instance:
            The value to assign to the is_additional_instance property of this SubscriptionSku.
        :type is_additional_instance: bool

        :param start_date:
            The value to assign to the start_date property of this SubscriptionSku.
        :type start_date: datetime

        :param end_date:
            The value to assign to the end_date property of this SubscriptionSku.
        :type end_date: datetime

        """
        self.swagger_types = {
            'sku': 'str',
            'quantity': 'int',
            'description': 'str',
            'gsi_order_line_id': 'str',
            'license_part_description': 'str',
            'metric_name': 'str',
            'is_base_service_component': 'bool',
            'is_additional_instance': 'bool',
            'start_date': 'datetime',
            'end_date': 'datetime'
        }

        self.attribute_map = {
            'sku': 'sku',
            'quantity': 'quantity',
            'description': 'description',
            'gsi_order_line_id': 'gsiOrderLineId',
            'license_part_description': 'licensePartDescription',
            'metric_name': 'metricName',
            'is_base_service_component': 'isBaseServiceComponent',
            'is_additional_instance': 'isAdditionalInstance',
            'start_date': 'startDate',
            'end_date': 'endDate'
        }

        self._sku = None
        self._quantity = None
        self._description = None
        self._gsi_order_line_id = None
        self._license_part_description = None
        self._metric_name = None
        self._is_base_service_component = None
        self._is_additional_instance = None
        self._start_date = None
        self._end_date = None

    @property
    def sku(self):
        """
        **[Required]** Gets the sku of this SubscriptionSku.
        Stock keeping unit ID.


        :return: The sku of this SubscriptionSku.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this SubscriptionSku.
        Stock keeping unit ID.


        :param sku: The sku of this SubscriptionSku.
        :type: str
        """
        self._sku = sku

    @property
    def quantity(self):
        """
        Gets the quantity of this SubscriptionSku.
        Quantity of the stock units.


        :return: The quantity of this SubscriptionSku.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this SubscriptionSku.
        Quantity of the stock units.


        :param quantity: The quantity of this SubscriptionSku.
        :type: int
        """
        self._quantity = quantity

    @property
    def description(self):
        """
        Gets the description of this SubscriptionSku.
        Description of the stock units.


        :return: The description of this SubscriptionSku.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SubscriptionSku.
        Description of the stock units.


        :param description: The description of this SubscriptionSku.
        :type: str
        """
        self._description = description

    @property
    def gsi_order_line_id(self):
        """
        Gets the gsi_order_line_id of this SubscriptionSku.
        Sales order line identifier.


        :return: The gsi_order_line_id of this SubscriptionSku.
        :rtype: str
        """
        return self._gsi_order_line_id

    @gsi_order_line_id.setter
    def gsi_order_line_id(self, gsi_order_line_id):
        """
        Sets the gsi_order_line_id of this SubscriptionSku.
        Sales order line identifier.


        :param gsi_order_line_id: The gsi_order_line_id of this SubscriptionSku.
        :type: str
        """
        self._gsi_order_line_id = gsi_order_line_id

    @property
    def license_part_description(self):
        """
        Gets the license_part_description of this SubscriptionSku.
        Description of the covered product belonging to this SKU.


        :return: The license_part_description of this SubscriptionSku.
        :rtype: str
        """
        return self._license_part_description

    @license_part_description.setter
    def license_part_description(self, license_part_description):
        """
        Sets the license_part_description of this SubscriptionSku.
        Description of the covered product belonging to this SKU.


        :param license_part_description: The license_part_description of this SubscriptionSku.
        :type: str
        """
        self._license_part_description = license_part_description

    @property
    def metric_name(self):
        """
        Gets the metric_name of this SubscriptionSku.
        Base metric for billing the service.


        :return: The metric_name of this SubscriptionSku.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this SubscriptionSku.
        Base metric for billing the service.


        :param metric_name: The metric_name of this SubscriptionSku.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def is_base_service_component(self):
        """
        Gets the is_base_service_component of this SubscriptionSku.
        Denotes if the SKU is considered as a parent or child.


        :return: The is_base_service_component of this SubscriptionSku.
        :rtype: bool
        """
        return self._is_base_service_component

    @is_base_service_component.setter
    def is_base_service_component(self, is_base_service_component):
        """
        Sets the is_base_service_component of this SubscriptionSku.
        Denotes if the SKU is considered as a parent or child.


        :param is_base_service_component: The is_base_service_component of this SubscriptionSku.
        :type: bool
        """
        self._is_base_service_component = is_base_service_component

    @property
    def is_additional_instance(self):
        """
        Gets the is_additional_instance of this SubscriptionSku.
        Denotes if an additional test instance can be provisioned by the SAAS application.


        :return: The is_additional_instance of this SubscriptionSku.
        :rtype: bool
        """
        return self._is_additional_instance

    @is_additional_instance.setter
    def is_additional_instance(self, is_additional_instance):
        """
        Sets the is_additional_instance of this SubscriptionSku.
        Denotes if an additional test instance can be provisioned by the SAAS application.


        :param is_additional_instance: The is_additional_instance of this SubscriptionSku.
        :type: bool
        """
        self._is_additional_instance = is_additional_instance

    @property
    def start_date(self):
        """
        Gets the start_date of this SubscriptionSku.
        Date-time when the SKU was created.


        :return: The start_date of this SubscriptionSku.
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this SubscriptionSku.
        Date-time when the SKU was created.


        :param start_date: The start_date of this SubscriptionSku.
        :type: datetime
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this SubscriptionSku.
        Date-time when the SKU ended.


        :return: The end_date of this SubscriptionSku.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this SubscriptionSku.
        Date-time when the SKU ended.


        :param end_date: The end_date of this SubscriptionSku.
        :type: datetime
        """
        self._end_date = end_date

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
