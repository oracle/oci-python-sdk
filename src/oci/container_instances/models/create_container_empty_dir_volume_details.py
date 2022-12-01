# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_container_volume_details import CreateContainerVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateContainerEmptyDirVolumeDetails(CreateContainerVolumeDetails):
    """
    The empty directory for container instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateContainerEmptyDirVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_instances.models.CreateContainerEmptyDirVolumeDetails.volume_type` attribute
        of this class is ``EMPTYDIR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateContainerEmptyDirVolumeDetails.
        :type name: str

        :param volume_type:
            The value to assign to the volume_type property of this CreateContainerEmptyDirVolumeDetails.
            Allowed values for this property are: "EMPTYDIR", "CONFIGFILE"
        :type volume_type: str

        :param backing_store:
            The value to assign to the backing_store property of this CreateContainerEmptyDirVolumeDetails.
        :type backing_store: str

        """
        self.swagger_types = {
            'name': 'str',
            'volume_type': 'str',
            'backing_store': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'volume_type': 'volumeType',
            'backing_store': 'backingStore'
        }

        self._name = None
        self._volume_type = None
        self._backing_store = None
        self._volume_type = 'EMPTYDIR'

    @property
    def backing_store(self):
        """
        Gets the backing_store of this CreateContainerEmptyDirVolumeDetails.
        Volume type that we are using for empty dir where it could be either File Storage or Memory


        :return: The backing_store of this CreateContainerEmptyDirVolumeDetails.
        :rtype: str
        """
        return self._backing_store

    @backing_store.setter
    def backing_store(self, backing_store):
        """
        Sets the backing_store of this CreateContainerEmptyDirVolumeDetails.
        Volume type that we are using for empty dir where it could be either File Storage or Memory


        :param backing_store: The backing_store of this CreateContainerEmptyDirVolumeDetails.
        :type: str
        """
        self._backing_store = backing_store

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
