# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InclusionCriterionCollection(object):
    """
    Results of a inclusion criterion search. Contains inclusion criterion summary items.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InclusionCriterionCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this InclusionCriterionCollection.
        :type items: list[oci.governance_rules_control_plane.models.InclusionCriterionSummary]

        """
        self.swagger_types = {
            'items': 'list[InclusionCriterionSummary]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this InclusionCriterionCollection.
        List of inclusionCriteria.


        :return: The items of this InclusionCriterionCollection.
        :rtype: list[oci.governance_rules_control_plane.models.InclusionCriterionSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this InclusionCriterionCollection.
        List of inclusionCriteria.


        :param items: The items of this InclusionCriterionCollection.
        :type: list[oci.governance_rules_control_plane.models.InclusionCriterionSummary]
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
