# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20241201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProductSummary(object):
    """
    The model for the product metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProductSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ProductSummary.
        :type name: str

        :param code:
            The value to assign to the code property of this ProductSummary.
        :type code: str

        :param product_group:
            The value to assign to the product_group property of this ProductSummary.
        :type product_group: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ProductSummary.
        :type lifecycle_state: str

        :param additional_filters:
            The value to assign to the additional_filters property of this ProductSummary.
        :type additional_filters: list[oci.marketplace_publisher.models.AdditionalFilter]

        :param time_created:
            The value to assign to the time_created property of this ProductSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ProductSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'name': 'str',
            'code': 'str',
            'product_group': 'str',
            'lifecycle_state': 'str',
            'additional_filters': 'list[AdditionalFilter]',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }
        self.attribute_map = {
            'name': 'name',
            'code': 'code',
            'product_group': 'productGroup',
            'lifecycle_state': 'lifecycleState',
            'additional_filters': 'additionalFilters',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }
        self._name = None
        self._code = None
        self._product_group = None
        self._lifecycle_state = None
        self._additional_filters = None
        self._time_created = None
        self._time_updated = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ProductSummary.
        The name for the product.


        :return: The name of this ProductSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductSummary.
        The name for the product.


        :param name: The name of this ProductSummary.
        :type: str
        """
        self._name = name

    @property
    def code(self):
        """
        Gets the code of this ProductSummary.
        The code for the product.


        :return: The code of this ProductSummary.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ProductSummary.
        The code for the product.


        :param code: The code of this ProductSummary.
        :type: str
        """
        self._code = code

    @property
    def product_group(self):
        """
        Gets the product_group of this ProductSummary.
        The product group for the product.


        :return: The product_group of this ProductSummary.
        :rtype: str
        """
        return self._product_group

    @product_group.setter
    def product_group(self, product_group):
        """
        Sets the product_group of this ProductSummary.
        The product group for the product.


        :param product_group: The product_group of this ProductSummary.
        :type: str
        """
        self._product_group = product_group

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ProductSummary.
        The current state for the product.


        :return: The lifecycle_state of this ProductSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ProductSummary.
        The current state for the product.


        :param lifecycle_state: The lifecycle_state of this ProductSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def additional_filters(self):
        """
        Gets the additional_filters of this ProductSummary.
        Additional filter properties for product


        :return: The additional_filters of this ProductSummary.
        :rtype: list[oci.marketplace_publisher.models.AdditionalFilter]
        """
        return self._additional_filters

    @additional_filters.setter
    def additional_filters(self, additional_filters):
        """
        Sets the additional_filters of this ProductSummary.
        Additional filter properties for product


        :param additional_filters: The additional_filters of this ProductSummary.
        :type: list[oci.marketplace_publisher.models.AdditionalFilter]
        """
        self._additional_filters = additional_filters

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ProductSummary.
        The date and time the product was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ProductSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ProductSummary.
        The date and time the product was created, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ProductSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ProductSummary.
        The date and time the product was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ProductSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ProductSummary.
        The date and time the product was updated, in the format defined by `RFC3339`__.

        Example: `2022-09-15T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ProductSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
