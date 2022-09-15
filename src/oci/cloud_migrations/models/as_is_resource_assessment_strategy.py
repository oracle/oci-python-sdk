# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .resource_assessment_strategy import ResourceAssessmentStrategy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AsIsResourceAssessmentStrategy(ResourceAssessmentStrategy):
    """
    The 'As-Is' based strategy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AsIsResourceAssessmentStrategy object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_migrations.models.AsIsResourceAssessmentStrategy.strategy_type` attribute
        of this class is ``AS_IS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_type:
            The value to assign to the resource_type property of this AsIsResourceAssessmentStrategy.
            Allowed values for this property are: "CPU", "MEMORY", "ALL"
        :type resource_type: str

        :param strategy_type:
            The value to assign to the strategy_type property of this AsIsResourceAssessmentStrategy.
            Allowed values for this property are: "AS_IS", "AVERAGE", "PEAK", "PERCENTILE"
        :type strategy_type: str

        :param adjustment_multiplier:
            The value to assign to the adjustment_multiplier property of this AsIsResourceAssessmentStrategy.
        :type adjustment_multiplier: float

        """
        self.swagger_types = {
            'resource_type': 'str',
            'strategy_type': 'str',
            'adjustment_multiplier': 'float'
        }

        self.attribute_map = {
            'resource_type': 'resourceType',
            'strategy_type': 'strategyType',
            'adjustment_multiplier': 'adjustmentMultiplier'
        }

        self._resource_type = None
        self._strategy_type = None
        self._adjustment_multiplier = None
        self._strategy_type = 'AS_IS'

    @property
    def adjustment_multiplier(self):
        """
        Gets the adjustment_multiplier of this AsIsResourceAssessmentStrategy.
        The real resource usage is multiplied to this number before making any recommendation.


        :return: The adjustment_multiplier of this AsIsResourceAssessmentStrategy.
        :rtype: float
        """
        return self._adjustment_multiplier

    @adjustment_multiplier.setter
    def adjustment_multiplier(self, adjustment_multiplier):
        """
        Sets the adjustment_multiplier of this AsIsResourceAssessmentStrategy.
        The real resource usage is multiplied to this number before making any recommendation.


        :param adjustment_multiplier: The adjustment_multiplier of this AsIsResourceAssessmentStrategy.
        :type: float
        """
        self._adjustment_multiplier = adjustment_multiplier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
