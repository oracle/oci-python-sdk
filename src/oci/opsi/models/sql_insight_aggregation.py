# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlInsightAggregation(object):
    """
    Represents a SQL Insight.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlInsightAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this SqlInsightAggregation.
        :type text: str

        :param values:
            The value to assign to the values property of this SqlInsightAggregation.
        :type values: list[int]

        :param category:
            The value to assign to the category property of this SqlInsightAggregation.
        :type category: str

        """
        self.swagger_types = {
            'text': 'str',
            'values': 'list[int]',
            'category': 'str'
        }

        self.attribute_map = {
            'text': 'text',
            'values': 'values',
            'category': 'category'
        }

        self._text = None
        self._values = None
        self._category = None

    @property
    def text(self):
        """
        **[Required]** Gets the text of this SqlInsightAggregation.
        Insight text.
        For example `Degrading SQLs`, `Variant SQLs`,
          `Inefficient SQLs`, `Improving SQLs`, `SQLs with Plan Changes`,
          `Degrading SQLs have increasing IO Time above 50%`,
          `Degrading SQLs are variant`,
          `2 of the 2 variant SQLs have plan changes`,
          `Inefficient SQLs have increasing CPU Time above 50%


        :return: The text of this SqlInsightAggregation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this SqlInsightAggregation.
        Insight text.
        For example `Degrading SQLs`, `Variant SQLs`,
          `Inefficient SQLs`, `Improving SQLs`, `SQLs with Plan Changes`,
          `Degrading SQLs have increasing IO Time above 50%`,
          `Degrading SQLs are variant`,
          `2 of the 2 variant SQLs have plan changes`,
          `Inefficient SQLs have increasing CPU Time above 50%


        :param text: The text of this SqlInsightAggregation.
        :type: str
        """
        self._text = text

    @property
    def values(self):
        """
        **[Required]** Gets the values of this SqlInsightAggregation.
        SQL counts for a given insight. For example insight text `2 of 10 SQLs have degrading response time` will have values as [2,10]\"


        :return: The values of this SqlInsightAggregation.
        :rtype: list[int]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this SqlInsightAggregation.
        SQL counts for a given insight. For example insight text `2 of 10 SQLs have degrading response time` will have values as [2,10]\"


        :param values: The values of this SqlInsightAggregation.
        :type: list[int]
        """
        self._values = values

    @property
    def category(self):
        """
        **[Required]** Gets the category of this SqlInsightAggregation.
        Insight category. It would be one of the following
        DEGRADING,
        VARIANT,
        INEFFICIENT,
        CHANGING_PLANS,
        IMPROVING,
        DEGRADING_VARIANT,
        DEGRADING_INEFFICIENT,
        DEGRADING_CHANGING_PLANS,
        DEGRADING_INCREASING_IO,
        DEGRADING_INCREASING_CPU,
        DEGRADING_INCREASING_INEFFICIENT_WAIT,
        DEGRADING_CHANGING_PLANS_AND_INCREASING_IO,
        DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU,
        DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT,VARIANT_INEFFICIENT,
        VARIANT_CHANGING_PLANS,
        VARIANT_INCREASING_IO,
        VARIANT_INCREASING_CPU,
        VARIANT_INCREASING_INEFFICIENT_WAIT,
        VARIANT_CHANGING_PLANS_AND_INCREASING_IO,
        VARIANT_CHANGING_PLANS_AND_INCREASING_CPU,
        VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT,
        INEFFICIENT_CHANGING_PLANS,
        INEFFICIENT_INCREASING_INEFFICIENT_WAIT,
        INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT


        :return: The category of this SqlInsightAggregation.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this SqlInsightAggregation.
        Insight category. It would be one of the following
        DEGRADING,
        VARIANT,
        INEFFICIENT,
        CHANGING_PLANS,
        IMPROVING,
        DEGRADING_VARIANT,
        DEGRADING_INEFFICIENT,
        DEGRADING_CHANGING_PLANS,
        DEGRADING_INCREASING_IO,
        DEGRADING_INCREASING_CPU,
        DEGRADING_INCREASING_INEFFICIENT_WAIT,
        DEGRADING_CHANGING_PLANS_AND_INCREASING_IO,
        DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU,
        DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT,VARIANT_INEFFICIENT,
        VARIANT_CHANGING_PLANS,
        VARIANT_INCREASING_IO,
        VARIANT_INCREASING_CPU,
        VARIANT_INCREASING_INEFFICIENT_WAIT,
        VARIANT_CHANGING_PLANS_AND_INCREASING_IO,
        VARIANT_CHANGING_PLANS_AND_INCREASING_CPU,
        VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT,
        INEFFICIENT_CHANGING_PLANS,
        INEFFICIENT_INCREASING_INEFFICIENT_WAIT,
        INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT


        :param category: The category of this SqlInsightAggregation.
        :type: str
        """
        self._category = category

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
