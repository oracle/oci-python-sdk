# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequestLogEntryCollection(object):
    """
    The collection of work request log entries. These result from a
    workRequestLog search. Contains both workRequestLog items and
    other information, such as metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequestLogEntryCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this WorkRequestLogEntryCollection.
        :type items: list[oci.cloud_guard.models.WorkRequestLogEntry]

        :param locks:
            The value to assign to the locks property of this WorkRequestLogEntryCollection.
        :type locks: list[oci.cloud_guard.models.ResourceLock]

        """
        self.swagger_types = {
            'items': 'list[WorkRequestLogEntry]',
            'locks': 'list[ResourceLock]'
        }
        self.attribute_map = {
            'items': 'items',
            'locks': 'locks'
        }
        self._items = None
        self._locks = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this WorkRequestLogEntryCollection.
        List of workRequestLogEntry resources


        :return: The items of this WorkRequestLogEntryCollection.
        :rtype: list[oci.cloud_guard.models.WorkRequestLogEntry]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this WorkRequestLogEntryCollection.
        List of workRequestLogEntry resources


        :param items: The items of this WorkRequestLogEntryCollection.
        :type: list[oci.cloud_guard.models.WorkRequestLogEntry]
        """
        self._items = items

    @property
    def locks(self):
        """
        Gets the locks of this WorkRequestLogEntryCollection.
        Locks associated with this resource.


        :return: The locks of this WorkRequestLogEntryCollection.
        :rtype: list[oci.cloud_guard.models.ResourceLock]
        """
        return self._locks

    @locks.setter
    def locks(self, locks):
        """
        Sets the locks of this WorkRequestLogEntryCollection.
        Locks associated with this resource.


        :param locks: The locks of this WorkRequestLogEntryCollection.
        :type: list[oci.cloud_guard.models.ResourceLock]
        """
        self._locks = locks

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
