# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateResourceDetails(object):
    """
    Details about updates to the resource.

    **Caution:** Avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateResourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param item:
            The value to assign to the item property of this UpdateResourceDetails.
        :type item: UpdateItemDetails

        """
        self.swagger_types = {
            'item': 'UpdateItemDetails'
        }

        self.attribute_map = {
            'item': 'item'
        }

        self._item = None

    @property
    def item(self):
        """
        Gets the item of this UpdateResourceDetails.

        :return: The item of this UpdateResourceDetails.
        :rtype: UpdateItemDetails
        """
        return self._item

    @item.setter
    def item(self, item):
        """
        Sets the item of this UpdateResourceDetails.

        :param item: The item of this UpdateResourceDetails.
        :type: UpdateItemDetails
        """
        self._item = item

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
