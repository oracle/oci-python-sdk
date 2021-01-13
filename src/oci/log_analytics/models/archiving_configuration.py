# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ArchivingConfiguration(object):
    """
    This is the configuration for data archiving in object storage
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ArchivingConfiguration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param active_storage_duration:
            The value to assign to the active_storage_duration property of this ArchivingConfiguration.
        :type active_storage_duration: str

        :param archival_storage_duration:
            The value to assign to the archival_storage_duration property of this ArchivingConfiguration.
        :type archival_storage_duration: str

        """
        self.swagger_types = {
            'active_storage_duration': 'str',
            'archival_storage_duration': 'str'
        }

        self.attribute_map = {
            'active_storage_duration': 'activeStorageDuration',
            'archival_storage_duration': 'archivalStorageDuration'
        }

        self._active_storage_duration = None
        self._archival_storage_duration = None

    @property
    def active_storage_duration(self):
        """
        Gets the active_storage_duration of this ArchivingConfiguration.
        This is the duration data in active storage before data is archived, as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).


        :return: The active_storage_duration of this ArchivingConfiguration.
        :rtype: str
        """
        return self._active_storage_duration

    @active_storage_duration.setter
    def active_storage_duration(self, active_storage_duration):
        """
        Sets the active_storage_duration of this ArchivingConfiguration.
        This is the duration data in active storage before data is archived, as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations.
        The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).


        :param active_storage_duration: The active_storage_duration of this ArchivingConfiguration.
        :type: str
        """
        self._active_storage_duration = active_storage_duration

    @property
    def archival_storage_duration(self):
        """
        Gets the archival_storage_duration of this ArchivingConfiguration.
        This is the duration before archived data is deleted from object storage, as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations
        The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).


        :return: The archival_storage_duration of this ArchivingConfiguration.
        :rtype: str
        """
        return self._archival_storage_duration

    @archival_storage_duration.setter
    def archival_storage_duration(self, archival_storage_duration):
        """
        Sets the archival_storage_duration of this ArchivingConfiguration.
        This is the duration before archived data is deleted from object storage, as described in
        https://en.wikipedia.org/wiki/ISO_8601#Durations
        The largest supported unit is D, e.g. P365D (not P1Y) or P14D (not P2W).


        :param archival_storage_duration: The archival_storage_duration of this ArchivingConfiguration.
        :type: str
        """
        self._archival_storage_duration = archival_storage_duration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
