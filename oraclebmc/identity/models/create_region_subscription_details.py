# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateRegionSubscriptionDetails(object):

    def __init__(self):

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
