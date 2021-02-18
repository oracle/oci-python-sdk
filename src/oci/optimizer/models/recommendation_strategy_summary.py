# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecommendationStrategySummary(object):
    """
    The metadata associated with the recommendation strategy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RecommendationStrategySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this RecommendationStrategySummary.
        :type name: str

        :param strategies:
            The value to assign to the strategies property of this RecommendationStrategySummary.
        :type strategies: list[oci.optimizer.models.Strategy]

        """
        self.swagger_types = {
            'name': 'str',
            'strategies': 'list[Strategy]'
        }

        self.attribute_map = {
            'name': 'name',
            'strategies': 'strategies'
        }

        self._name = None
        self._strategies = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this RecommendationStrategySummary.
        The display name of the recommendation.


        :return: The name of this RecommendationStrategySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RecommendationStrategySummary.
        The display name of the recommendation.


        :param name: The name of this RecommendationStrategySummary.
        :type: str
        """
        self._name = name

    @property
    def strategies(self):
        """
        **[Required]** Gets the strategies of this RecommendationStrategySummary.
        The list of strategies used.


        :return: The strategies of this RecommendationStrategySummary.
        :rtype: list[oci.optimizer.models.Strategy]
        """
        return self._strategies

    @strategies.setter
    def strategies(self, strategies):
        """
        Sets the strategies of this RecommendationStrategySummary.
        The list of strategies used.


        :param strategies: The strategies of this RecommendationStrategySummary.
        :type: list[oci.optimizer.models.Strategy]
        """
        self._strategies = strategies

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
