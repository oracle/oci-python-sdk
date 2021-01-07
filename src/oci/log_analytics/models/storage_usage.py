# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StorageUsage(object):
    """
    This is the storage usage information of a tenancy in Logan Analytics application
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StorageUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param active_data_size_in_bytes:
            The value to assign to the active_data_size_in_bytes property of this StorageUsage.
        :type active_data_size_in_bytes: int

        :param archived_data_size_in_bytes:
            The value to assign to the archived_data_size_in_bytes property of this StorageUsage.
        :type archived_data_size_in_bytes: int

        :param recalled_archived_data_size_in_bytes:
            The value to assign to the recalled_archived_data_size_in_bytes property of this StorageUsage.
        :type recalled_archived_data_size_in_bytes: int

        """
        self.swagger_types = {
            'active_data_size_in_bytes': 'int',
            'archived_data_size_in_bytes': 'int',
            'recalled_archived_data_size_in_bytes': 'int'
        }

        self.attribute_map = {
            'active_data_size_in_bytes': 'activeDataSizeInBytes',
            'archived_data_size_in_bytes': 'archivedDataSizeInBytes',
            'recalled_archived_data_size_in_bytes': 'recalledArchivedDataSizeInBytes'
        }

        self._active_data_size_in_bytes = None
        self._archived_data_size_in_bytes = None
        self._recalled_archived_data_size_in_bytes = None

    @property
    def active_data_size_in_bytes(self):
        """
        **[Required]** Gets the active_data_size_in_bytes of this StorageUsage.
        This is the number of bytes of active data (non-archived)


        :return: The active_data_size_in_bytes of this StorageUsage.
        :rtype: int
        """
        return self._active_data_size_in_bytes

    @active_data_size_in_bytes.setter
    def active_data_size_in_bytes(self, active_data_size_in_bytes):
        """
        Sets the active_data_size_in_bytes of this StorageUsage.
        This is the number of bytes of active data (non-archived)


        :param active_data_size_in_bytes: The active_data_size_in_bytes of this StorageUsage.
        :type: int
        """
        self._active_data_size_in_bytes = active_data_size_in_bytes

    @property
    def archived_data_size_in_bytes(self):
        """
        **[Required]** Gets the archived_data_size_in_bytes of this StorageUsage.
        This is the number of bytes of archived data in object storage


        :return: The archived_data_size_in_bytes of this StorageUsage.
        :rtype: int
        """
        return self._archived_data_size_in_bytes

    @archived_data_size_in_bytes.setter
    def archived_data_size_in_bytes(self, archived_data_size_in_bytes):
        """
        Sets the archived_data_size_in_bytes of this StorageUsage.
        This is the number of bytes of archived data in object storage


        :param archived_data_size_in_bytes: The archived_data_size_in_bytes of this StorageUsage.
        :type: int
        """
        self._archived_data_size_in_bytes = archived_data_size_in_bytes

    @property
    def recalled_archived_data_size_in_bytes(self):
        """
        **[Required]** Gets the recalled_archived_data_size_in_bytes of this StorageUsage.
        This is the number of bytes of recalled data from archived in object store


        :return: The recalled_archived_data_size_in_bytes of this StorageUsage.
        :rtype: int
        """
        return self._recalled_archived_data_size_in_bytes

    @recalled_archived_data_size_in_bytes.setter
    def recalled_archived_data_size_in_bytes(self, recalled_archived_data_size_in_bytes):
        """
        Sets the recalled_archived_data_size_in_bytes of this StorageUsage.
        This is the number of bytes of recalled data from archived in object store


        :param recalled_archived_data_size_in_bytes: The recalled_archived_data_size_in_bytes of this StorageUsage.
        :type: int
        """
        self._recalled_archived_data_size_in_bytes = recalled_archived_data_size_in_bytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
