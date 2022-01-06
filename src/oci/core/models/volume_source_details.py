# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeSourceDetails(object):
    """
    Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same Availability Domain or a Block volume backup.
    This is an optional field. If not specified or set to null, the new Block volume will be empty.
    When specified, the new Block volume will contain data from the source volume or backup.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.VolumeSourceFromBlockVolumeReplicaDetails`
        * :class:`~oci.core.models.VolumeSourceFromVolumeDetails`
        * :class:`~oci.core.models.VolumeSourceFromVolumeBackupDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VolumeSourceDetails.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'blockVolumeReplica':
            return 'VolumeSourceFromBlockVolumeReplicaDetails'

        if type == 'volume':
            return 'VolumeSourceFromVolumeDetails'

        if type == 'volumeBackup':
            return 'VolumeSourceFromVolumeBackupDetails'
        else:
            return 'VolumeSourceDetails'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this VolumeSourceDetails.

        :return: The type of this VolumeSourceDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VolumeSourceDetails.

        :param type: The type of this VolumeSourceDetails.
        :type: str
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
