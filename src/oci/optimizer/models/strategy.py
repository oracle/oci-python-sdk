# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Strategy(object):
    """
    The metadata associated with the strategy. The strategy is the method used to apply the recommendation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Strategy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param strategy_name:
            The value to assign to the strategy_name property of this Strategy.
        :type strategy_name: str

        :param is_default:
            The value to assign to the is_default property of this Strategy.
        :type is_default: bool

        :param parameters_definition:
            The value to assign to the parameters_definition property of this Strategy.
        :type parameters_definition: list[oci.optimizer.models.StrategyParameter]

        """
        self.swagger_types = {
            'strategy_name': 'str',
            'is_default': 'bool',
            'parameters_definition': 'list[StrategyParameter]'
        }

        self.attribute_map = {
            'strategy_name': 'strategyName',
            'is_default': 'isDefault',
            'parameters_definition': 'parametersDefinition'
        }

        self._strategy_name = None
        self._is_default = None
        self._parameters_definition = None

    @property
    def strategy_name(self):
        """
        **[Required]** Gets the strategy_name of this Strategy.
        The name of the strategy.


        :return: The strategy_name of this Strategy.
        :rtype: str
        """
        return self._strategy_name

    @strategy_name.setter
    def strategy_name(self, strategy_name):
        """
        Sets the strategy_name of this Strategy.
        The name of the strategy.


        :param strategy_name: The strategy_name of this Strategy.
        :type: str
        """
        self._strategy_name = strategy_name

    @property
    def is_default(self):
        """
        **[Required]** Gets the is_default of this Strategy.
        Whether this is the default recommendation strategy.


        :return: The is_default of this Strategy.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this Strategy.
        Whether this is the default recommendation strategy.


        :param is_default: The is_default of this Strategy.
        :type: bool
        """
        self._is_default = is_default

    @property
    def parameters_definition(self):
        """
        Gets the parameters_definition of this Strategy.
        The list of strategies for the parameters.


        :return: The parameters_definition of this Strategy.
        :rtype: list[oci.optimizer.models.StrategyParameter]
        """
        return self._parameters_definition

    @parameters_definition.setter
    def parameters_definition(self, parameters_definition):
        """
        Sets the parameters_definition of this Strategy.
        The list of strategies for the parameters.


        :param parameters_definition: The parameters_definition of this Strategy.
        :type: list[oci.optimizer.models.StrategyParameter]
        """
        self._parameters_definition = parameters_definition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
