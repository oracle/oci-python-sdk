# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StorageServerDetails(object):
    """
    Partial information about a storage server which includes name and displayName.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StorageServerDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param storage_server_name:
            The value to assign to the storage_server_name property of this StorageServerDetails.
        :type storage_server_name: str

        :param storage_server_display_name:
            The value to assign to the storage_server_display_name property of this StorageServerDetails.
        :type storage_server_display_name: str

        """
        self.swagger_types = {
            'storage_server_name': 'str',
            'storage_server_display_name': 'str'
        }

        self.attribute_map = {
            'storage_server_name': 'storageServerName',
            'storage_server_display_name': 'storageServerDisplayName'
        }

        self._storage_server_name = None
        self._storage_server_display_name = None

    @property
    def storage_server_name(self):
        """
        **[Required]** Gets the storage_server_name of this StorageServerDetails.
        The storage server name.


        :return: The storage_server_name of this StorageServerDetails.
        :rtype: str
        """
        return self._storage_server_name

    @storage_server_name.setter
    def storage_server_name(self, storage_server_name):
        """
        Sets the storage_server_name of this StorageServerDetails.
        The storage server name.


        :param storage_server_name: The storage_server_name of this StorageServerDetails.
        :type: str
        """
        self._storage_server_name = storage_server_name

    @property
    def storage_server_display_name(self):
        """
        **[Required]** Gets the storage_server_display_name of this StorageServerDetails.
        The user-friendly name for the storage server. The name does not have to be unique.


        :return: The storage_server_display_name of this StorageServerDetails.
        :rtype: str
        """
        return self._storage_server_display_name

    @storage_server_display_name.setter
    def storage_server_display_name(self, storage_server_display_name):
        """
        Sets the storage_server_display_name of this StorageServerDetails.
        The user-friendly name for the storage server. The name does not have to be unique.


        :param storage_server_display_name: The storage_server_display_name of this StorageServerDetails.
        :type: str
        """
        self._storage_server_display_name = storage_server_display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
