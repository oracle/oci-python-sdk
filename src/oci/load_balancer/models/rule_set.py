# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleSet(object):
    """
    A named set of rules associated with a load balancer. Rules are objects that represent actions to apply to a listener,
    such as adding, altering, or removing HTTP headers. For more information, see
    `Managing Rule Sets`__.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RuleSet object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this RuleSet.
        :type name: str

        :param items:
            The value to assign to the items property of this RuleSet.
        :type items: list[Rule]

        """
        self.swagger_types = {
            'name': 'str',
            'items': 'list[Rule]'
        }

        self.attribute_map = {
            'name': 'name',
            'items': 'items'
        }

        self._name = None
        self._items = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this RuleSet.
        The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
        confidential information.

        Example: `example_rule_set`


        :return: The name of this RuleSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RuleSet.
        The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
        confidential information.

        Example: `example_rule_set`


        :param name: The name of this RuleSet.
        :type: str
        """
        self._name = name

    @property
    def items(self):
        """
        **[Required]** Gets the items of this RuleSet.
        An array of rules that compose the rule set.


        :return: The items of this RuleSet.
        :rtype: list[Rule]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this RuleSet.
        An array of rules that compose the rule set.


        :param items: The items of this RuleSet.
        :type: list[Rule]
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
