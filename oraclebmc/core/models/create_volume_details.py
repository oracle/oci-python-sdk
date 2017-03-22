# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateVolumeDetails(object):

    def __init__(self):

        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'size_in_mbs': 'int',
            'volume_backup_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'size_in_mbs': 'sizeInMBs',
            'volume_backup_id': 'volumeBackupId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._size_in_mbs = None
        self._volume_backup_id = None

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this CreateVolumeDetails.
        The Availability Domain of the volume.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this CreateVolumeDetails.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this CreateVolumeDetails.
        The Availability Domain of the volume.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this CreateVolumeDetails.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateVolumeDetails.
        The OCID of the compartment that contains the volume.


        :return: The compartment_id of this CreateVolumeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateVolumeDetails.
        The OCID of the compartment that contains the volume.


        :param compartment_id: The compartment_id of this CreateVolumeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this CreateVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this CreateVolumeDetails.
        The size of the volume in MBs.


        :return: The size_in_mbs of this CreateVolumeDetails.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this CreateVolumeDetails.
        The size of the volume in MBs.


        :param size_in_mbs: The size_in_mbs of this CreateVolumeDetails.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def volume_backup_id(self):
        """
        Gets the volume_backup_id of this CreateVolumeDetails.
        The OCID of the volume backup from which the data should be restored on the newly created volume.


        :return: The volume_backup_id of this CreateVolumeDetails.
        :rtype: str
        """
        return self._volume_backup_id

    @volume_backup_id.setter
    def volume_backup_id(self, volume_backup_id):
        """
        Sets the volume_backup_id of this CreateVolumeDetails.
        The OCID of the volume backup from which the data should be restored on the newly created volume.


        :param volume_backup_id: The volume_backup_id of this CreateVolumeDetails.
        :type: str
        """
        self._volume_backup_id = volume_backup_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
