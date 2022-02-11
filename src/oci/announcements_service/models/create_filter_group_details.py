# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFilterGroupDetails(object):
    """
    The details for creating a new filter group for an announcement subscription.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFilterGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateFilterGroupDetails.
        :type name: str

        :param filters:
            The value to assign to the filters property of this CreateFilterGroupDetails.
        :type filters: list[oci.announcements_service.models.Filter]

        """
        self.swagger_types = {
            'name': 'str',
            'filters': 'list[Filter]'
        }

        self.attribute_map = {
            'name': 'name',
            'filters': 'filters'
        }

        self._name = None
        self._filters = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateFilterGroupDetails.
        The name of the filter group. The name must be unique and it cannot be changed. Avoid entering confidential information.


        :return: The name of this CreateFilterGroupDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateFilterGroupDetails.
        The name of the filter group. The name must be unique and it cannot be changed. Avoid entering confidential information.


        :param name: The name of this CreateFilterGroupDetails.
        :type: str
        """
        self._name = name

    @property
    def filters(self):
        """
        **[Required]** Gets the filters of this CreateFilterGroupDetails.
        A list of filters against which the Announcements service will match announcements. You cannot have more than one of any given filter type within a filter group.


        :return: The filters of this CreateFilterGroupDetails.
        :rtype: list[oci.announcements_service.models.Filter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this CreateFilterGroupDetails.
        A list of filters against which the Announcements service will match announcements. You cannot have more than one of any given filter type within a filter group.


        :param filters: The filters of this CreateFilterGroupDetails.
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
