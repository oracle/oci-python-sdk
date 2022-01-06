# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScaleStorageDetails(object):
    """
    storage size to increase
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScaleStorageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param storage_size_in_tbs:
            The value to assign to the storage_size_in_tbs property of this ScaleStorageDetails.
        :type storage_size_in_tbs: int

        """
        self.swagger_types = {
            'storage_size_in_tbs': 'int'
        }

        self.attribute_map = {
            'storage_size_in_tbs': 'storageSizeInTBs'
        }

        self._storage_size_in_tbs = None

    @property
    def storage_size_in_tbs(self):
        """
        **[Required]** Gets the storage_size_in_tbs of this ScaleStorageDetails.
        Storage size in TBs


        :return: The storage_size_in_tbs of this ScaleStorageDetails.
        :rtype: int
        """
        return self._storage_size_in_tbs

    @storage_size_in_tbs.setter
    def storage_size_in_tbs(self, storage_size_in_tbs):
        """
        Sets the storage_size_in_tbs of this ScaleStorageDetails.
        Storage size in TBs


        :param storage_size_in_tbs: The storage_size_in_tbs of this ScaleStorageDetails.
        :type: int
        """
        self._storage_size_in_tbs = storage_size_in_tbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
