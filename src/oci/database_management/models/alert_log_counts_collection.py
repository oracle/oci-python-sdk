# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertLogCountsCollection(object):
    """
    The collection of the counts of different level or type of alert logs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AlertLogCountsCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param managed_database_id:
            The value to assign to the managed_database_id property of this AlertLogCountsCollection.
        :type managed_database_id: str

        :param items:
            The value to assign to the items property of this AlertLogCountsCollection.
        :type items: list[oci.database_management.models.AlertLogCountSummary]

        """
        self.swagger_types = {
            'managed_database_id': 'str',
            'items': 'list[AlertLogCountSummary]'
        }

        self.attribute_map = {
            'managed_database_id': 'managedDatabaseId',
            'items': 'items'
        }

        self._managed_database_id = None
        self._items = None

    @property
    def managed_database_id(self):
        """
        **[Required]** Gets the managed_database_id of this AlertLogCountsCollection.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this AlertLogCountsCollection.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this AlertLogCountsCollection.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this AlertLogCountsCollection.
        :type: str
        """
        self._managed_database_id = managed_database_id

    @property
    def items(self):
        """
        **[Required]** Gets the items of this AlertLogCountsCollection.
        An array of the counts of different urgency or type of alert logs.


        :return: The items of this AlertLogCountsCollection.
        :rtype: list[oci.database_management.models.AlertLogCountSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AlertLogCountsCollection.
        An array of the counts of different urgency or type of alert logs.


        :param items: The items of this AlertLogCountsCollection.
        :type: list[oci.database_management.models.AlertLogCountSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
