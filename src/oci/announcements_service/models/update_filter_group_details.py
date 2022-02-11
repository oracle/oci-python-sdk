# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFilterGroupDetails(object):
    """
    The details for updating a filter group in an announcement subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFilterGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param filters:
            The value to assign to the filters property of this UpdateFilterGroupDetails.
        :type filters: list[oci.announcements_service.models.Filter]

        """
        self.swagger_types = {
            'filters': 'list[Filter]'
        }

        self.attribute_map = {
            'filters': 'filters'
        }

        self._filters = None

    @property
    def filters(self):
        """
        **[Required]** Gets the filters of this UpdateFilterGroupDetails.
        A list of filters against which the Announcements service will match announcements. You cannot have more than one of any given filter type within a filter group.


        :return: The filters of this UpdateFilterGroupDetails.
        :rtype: list[oci.announcements_service.models.Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this UpdateFilterGroupDetails.
        A list of filters against which the Announcements service will match announcements. You cannot have more than one of any given filter type within a filter group.


        :param filters: The filters of this UpdateFilterGroupDetails.
        :type: list[oci.announcements_service.models.Filter]
        """
        self._filters = filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
