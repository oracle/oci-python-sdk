# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EstimatePurgeDataSizeResult(object):
    """
    purge data size in bytes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new EstimatePurgeDataSizeResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param purge_data_size_in_bytes:
            The value to assign to the purge_data_size_in_bytes property of this EstimatePurgeDataSizeResult.
        :type purge_data_size_in_bytes: int

        """
        self.swagger_types = {
            'purge_data_size_in_bytes': 'int'
        }

        self.attribute_map = {
            'purge_data_size_in_bytes': 'purgeDataSizeInBytes'
        }

        self._purge_data_size_in_bytes = None

    @property
    def purge_data_size_in_bytes(self):
        """
        **[Required]** Gets the purge_data_size_in_bytes of this EstimatePurgeDataSizeResult.
        This is the size of data to be purged in bytes


        :return: The purge_data_size_in_bytes of this EstimatePurgeDataSizeResult.
        :rtype: int
        """
        return self._purge_data_size_in_bytes

    @purge_data_size_in_bytes.setter
    def purge_data_size_in_bytes(self, purge_data_size_in_bytes):
        """
        Sets the purge_data_size_in_bytes of this EstimatePurgeDataSizeResult.
        This is the size of data to be purged in bytes


        :param purge_data_size_in_bytes: The purge_data_size_in_bytes of this EstimatePurgeDataSizeResult.
        :type: int
        """
        self._purge_data_size_in_bytes = purge_data_size_in_bytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
