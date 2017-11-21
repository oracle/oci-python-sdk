# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRegionSubscriptionDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRegionSubscriptionDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region_key:
            The value to assign to the region_key property of this CreateRegionSubscriptionDetails.
        :type region_key: str

        """
        self.swagger_types = {
            'region_key': 'str'
        }

        self.attribute_map = {
            'region_key': 'regionKey'
        }

        self._region_key = None

    @property
    def region_key(self):
        """
        Gets the region_key of this CreateRegionSubscriptionDetails.
        The regions's key.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`

        Example: `PHX`


        :return: The region_key of this CreateRegionSubscriptionDetails.
        :rtype: str
        """
        return self._region_key

    @region_key.setter
    def region_key(self, region_key):
        """
        Sets the region_key of this CreateRegionSubscriptionDetails.
        The regions's key.

        Allowed values are:
        - `PHX`
        - `IAD`
        - `FRA`

        Example: `PHX`


        :param region_key: The region_key of this CreateRegionSubscriptionDetails.
        :type: str
        """
        self._region_key = region_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
