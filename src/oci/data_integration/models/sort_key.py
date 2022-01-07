# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SortKey(object):
    """
    Sort key contains a set of sort key rules defining sorting algorithm.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SortKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sort_rules:
            The value to assign to the sort_rules property of this SortKey.
        :type sort_rules: list[oci.data_integration.models.SortKeyRule]

        """
        self.swagger_types = {
            'sort_rules': 'list[SortKeyRule]'
        }

        self.attribute_map = {
            'sort_rules': 'sortRules'
        }

        self._sort_rules = None

    @property
    def sort_rules(self):
        """
        Gets the sort_rules of this SortKey.
        The list of sort key rules.


        :return: The sort_rules of this SortKey.
        :rtype: list[oci.data_integration.models.SortKeyRule]
        """
        return self._sort_rules

    @sort_rules.setter
    def sort_rules(self, sort_rules):
        """
        Sets the sort_rules of this SortKey.
        The list of sort key rules.


        :param sort_rules: The sort_rules of this SortKey.
        :type: list[oci.data_integration.models.SortKeyRule]
        """
        self._sort_rules = sort_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
