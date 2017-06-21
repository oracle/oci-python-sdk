# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class RegionSubscription(object):

    def __init__(self):

        self.swagger_types = {
            'region_key': 'str',
            'region_name': 'str',
            'status': 'str',
            'is_home_region': 'bool'
        }

        self.attribute_map = {
            'region_key': 'regionKey',
            'region_name': 'regionName',
            'status': 'status',
            'is_home_region': 'isHomeRegion'
        }

        self._region_key = None
        self._region_name = None
        self._status = None
        self._is_home_region = None

    @property
    def region_key(self):
        """
        Gets the region_key of this RegionSubscription.
        The region's key.

        Allowed values are:
        - `PHX`
        - `IAD`


        :return: The region_key of this RegionSubscription.
        :rtype: str
        """
        return self._region_key

    @region_key.setter
    def region_key(self, region_key):
        """
        Sets the region_key of this RegionSubscription.
        The region's key.

        Allowed values are:
        - `PHX`
        - `IAD`


        :param region_key: The region_key of this RegionSubscription.
        :type: str
        """
        self._region_key = region_key

    @property
    def region_name(self):
        """
        Gets the region_name of this RegionSubscription.
        The region's name.

        Allowed values are:
        - `us-phoenix-1`
        - `us-ashburn-1`


        :return: The region_name of this RegionSubscription.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """
        Sets the region_name of this RegionSubscription.
        The region's name.

        Allowed values are:
        - `us-phoenix-1`
        - `us-ashburn-1`


        :param region_name: The region_name of this RegionSubscription.
        :type: str
        """
        self._region_name = region_name

    @property
    def status(self):
        """
        Gets the status of this RegionSubscription.
        The region subscription status.

        Allowed values for this property are: "READY", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RegionSubscription.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RegionSubscription.
        The region subscription status.


        :param status: The status of this RegionSubscription.
        :type: str
        """
        allowed_values = ["READY", "IN_PROGRESS"]
        if status not in allowed_values:
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def is_home_region(self):
        """
        Gets the is_home_region of this RegionSubscription.
        Indicates if the region is the home region or not.


        :return: The is_home_region of this RegionSubscription.
        :rtype: bool
        """
        return self._is_home_region

    @is_home_region.setter
    def is_home_region(self, is_home_region):
        """
        Sets the is_home_region of this RegionSubscription.
        Indicates if the region is the home region or not.


        :param is_home_region: The is_home_region of this RegionSubscription.
        :type: bool
        """
        self._is_home_region = is_home_region

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
