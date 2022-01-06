# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsResourceCategoryCollection(object):
    """
    A collection of resources and their category assignments.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsResourceCategoryCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param categories:
            The value to assign to the categories property of this LogAnalyticsResourceCategoryCollection.
        :type categories: list[oci.log_analytics.models.LogAnalyticsCategory]

        :param items:
            The value to assign to the items property of this LogAnalyticsResourceCategoryCollection.
        :type items: list[oci.log_analytics.models.LogAnalyticsResourceCategory]

        """
        self.swagger_types = {
            'categories': 'list[LogAnalyticsCategory]',
            'items': 'list[LogAnalyticsResourceCategory]'
        }

        self.attribute_map = {
            'categories': 'categories',
            'items': 'items'
        }

        self._categories = None
        self._items = None

    @property
    def categories(self):
        """
        Gets the categories of this LogAnalyticsResourceCategoryCollection.
        An array of categories. The array contents include detailed information about
        the distinct set of categories assigned to all the listed resources under items.


        :return: The categories of this LogAnalyticsResourceCategoryCollection.
        :rtype: list[oci.log_analytics.models.LogAnalyticsCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this LogAnalyticsResourceCategoryCollection.
        An array of categories. The array contents include detailed information about
        the distinct set of categories assigned to all the listed resources under items.


        :param categories: The categories of this LogAnalyticsResourceCategoryCollection.
        :type: list[oci.log_analytics.models.LogAnalyticsCategory]
        """
        self._categories = categories

    @property
    def items(self):
        """
        Gets the items of this LogAnalyticsResourceCategoryCollection.
        A list of resources and their category assignments


        :return: The items of this LogAnalyticsResourceCategoryCollection.
        :rtype: list[oci.log_analytics.models.LogAnalyticsResourceCategory]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this LogAnalyticsResourceCategoryCollection.
        A list of resources and their category assignments


        :param items: The items of this LogAnalyticsResourceCategoryCollection.
        :type: list[oci.log_analytics.models.LogAnalyticsResourceCategory]
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
