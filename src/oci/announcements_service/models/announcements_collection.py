# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnnouncementsCollection(object):
    """
    A list of announcements that match filter criteria, if any. Results contain both the announcements and the user-specific status of the announcements.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnnouncementsCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this AnnouncementsCollection.
        :type items: list[AnnouncementSummary]

        :param user_statuses:
            The value to assign to the user_statuses property of this AnnouncementsCollection.
        :type user_statuses: list[AnnouncementUserStatusDetails]

        """
        self.swagger_types = {
            'items': 'list[AnnouncementSummary]',
            'user_statuses': 'list[AnnouncementUserStatusDetails]'
        }

        self.attribute_map = {
            'items': 'items',
            'user_statuses': 'userStatuses'
        }

        self._items = None
        self._user_statuses = None

    @property
    def items(self):
        """
        Gets the items of this AnnouncementsCollection.
        A collection of announcements.


        :return: The items of this AnnouncementsCollection.
        :rtype: list[AnnouncementSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AnnouncementsCollection.
        A collection of announcements.


        :param items: The items of this AnnouncementsCollection.
        :type: list[AnnouncementSummary]
        """
        self._items = items

    @property
    def user_statuses(self):
        """
        Gets the user_statuses of this AnnouncementsCollection.
        The user-specific status for found announcements.


        :return: The user_statuses of this AnnouncementsCollection.
        :rtype: list[AnnouncementUserStatusDetails]
        """
        return self._user_statuses

    @user_statuses.setter
    def user_statuses(self, user_statuses):
        """
        Sets the user_statuses of this AnnouncementsCollection.
        The user-specific status for found announcements.


        :param user_statuses: The user_statuses of this AnnouncementsCollection.
        :type: list[AnnouncementUserStatusDetails]
        """
        self._user_statuses = user_statuses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
