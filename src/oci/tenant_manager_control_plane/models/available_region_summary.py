# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailableRegionSummary(object):
    """
    The summary of region availability for a subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailableRegionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param region_name:
            The value to assign to the region_name property of this AvailableRegionSummary.
        :type region_name: str

        """
        self.swagger_types = {
            'region_name': 'str'
        }

        self.attribute_map = {
            'region_name': 'regionName'
        }

        self._region_name = None

    @property
    def region_name(self):
        """
        **[Required]** Gets the region_name of this AvailableRegionSummary.
        Region availability for the subscription.


        :return: The region_name of this AvailableRegionSummary.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """
        Sets the region_name of this AvailableRegionSummary.
        Region availability for the subscription.


        :param region_name: The region_name of this AvailableRegionSummary.
        :type: str
        """
        self._region_name = region_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
