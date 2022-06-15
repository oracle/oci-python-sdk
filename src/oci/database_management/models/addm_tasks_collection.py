# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddmTasksCollection(object):
    """
    The list of ADDM task metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddmTasksCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this AddmTasksCollection.
        :type items: list[oci.database_management.models.AddmTaskSummary]

        :param managed_database_id:
            The value to assign to the managed_database_id property of this AddmTasksCollection.
        :type managed_database_id: str

        """
        self.swagger_types = {
            'items': 'list[AddmTaskSummary]',
            'managed_database_id': 'str'
        }

        self.attribute_map = {
            'items': 'items',
            'managed_database_id': 'managedDatabaseId'
        }

        self._items = None
        self._managed_database_id = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this AddmTasksCollection.
        The list of ADDM task metadata.


        :return: The items of this AddmTasksCollection.
        :rtype: list[oci.database_management.models.AddmTaskSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AddmTasksCollection.
        The list of ADDM task metadata.


        :param items: The items of this AddmTasksCollection.
        :type: list[oci.database_management.models.AddmTaskSummary]
        """
        self._items = items

    @property
    def managed_database_id(self):
        """
        **[Required]** Gets the managed_database_id of this AddmTasksCollection.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this AddmTasksCollection.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this AddmTasksCollection.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this AddmTasksCollection.
        :type: str
        """
        self._managed_database_id = managed_database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
