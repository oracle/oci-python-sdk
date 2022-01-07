# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRegionSubscriptionDetails(object):
    """
    CreateRegionSubscriptionDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRegionSubscriptionDetails object with values from keyword arguments.
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
        **[Required]** Gets the region_key of this CreateRegionSubscriptionDetails.
        The regions's key. See `Regions and Availability Domains`__ for
        the full list of supported 3-letter region codes.

        Example: `PHX`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


        :return: The region_key of this CreateRegionSubscriptionDetails.
        :rtype: str
        """
        return self._region_key

    @region_key.setter
    def region_key(self, region_key):
        """
        Sets the region_key of this CreateRegionSubscriptionDetails.
        The regions's key. See `Regions and Availability Domains`__ for
        the full list of supported 3-letter region codes.

        Example: `PHX`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm


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
