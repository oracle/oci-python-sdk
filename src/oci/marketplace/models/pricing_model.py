# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PricingModel(object):
    """
    The model for pricing.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PricingModel object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rate:
            The value to assign to the rate property of this PricingModel.
        :type rate: float

        """
        self.swagger_types = {
            'rate': 'float'
        }

        self.attribute_map = {
            'rate': 'rate'
        }

        self._rate = None

    @property
    def rate(self):
        """
        Gets the rate of this PricingModel.
        The pricing rate.


        :return: The rate of this PricingModel.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this PricingModel.
        The pricing rate.


        :param rate: The rate of this PricingModel.
        :type: float
        """
        self._rate = rate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
