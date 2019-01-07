# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleSetDetails(object):
    """
    The rules that compose a rule set.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RuleSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this RuleSetDetails.
        :type items: list[Rule]

        """
        self.swagger_types = {
            'items': 'list[Rule]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this RuleSetDetails.
        An array of rules that compose the rule set.


        :return: The items of this RuleSetDetails.
        :rtype: list[Rule]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this RuleSetDetails.
        An array of rules that compose the rule set.


        :param items: The items of this RuleSetDetails.
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
