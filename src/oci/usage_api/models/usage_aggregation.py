# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UsageAggregation(object):
    """
    The account (tenant) usage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UsageAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param group_by:
            The value to assign to the group_by property of this UsageAggregation.
        :type group_by: list[str]

        :param items:
            The value to assign to the items property of this UsageAggregation.
        :type items: list[oci.usage_api.models.UsageSummary]

        """
        self.swagger_types = {
            'group_by': 'list[str]',
            'items': 'list[UsageSummary]'
        }

        self.attribute_map = {
            'group_by': 'groupBy',
            'items': 'items'
        }

        self._group_by = None
        self._items = None

    @property
    def group_by(self):
        """
        Gets the group_by of this UsageAggregation.
        Aggregate the result by.


        :return: The group_by of this UsageAggregation.
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """
        Sets the group_by of this UsageAggregation.
        Aggregate the result by.


        :param group_by: The group_by of this UsageAggregation.
        :type: list[str]
        """
        self._group_by = group_by

    @property
    def items(self):
        """
        **[Required]** Gets the items of this UsageAggregation.
        A list of usage items.


        :return: The items of this UsageAggregation.
        :rtype: list[oci.usage_api.models.UsageSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this UsageAggregation.
        A list of usage items.


        :param items: The items of this UsageAggregation.
        :type: list[oci.usage_api.models.UsageSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
