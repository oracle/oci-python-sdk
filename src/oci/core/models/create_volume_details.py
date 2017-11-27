# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVolumeDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVolumeDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param availability_domain:
            The value to assign to the availability_domain property of this CreateVolumeDetails.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateVolumeDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateVolumeDetails.
        :type display_name: str

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this CreateVolumeDetails.
        :type size_in_gbs: int

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this CreateVolumeDetails.
        :type size_in_mbs: int

        :param source_details:
            The value to assign to the source_details property of this CreateVolumeDetails.
        :type source_details: VolumeSourceDetails

        :param volume_backup_id:
            The value to assign to the volume_backup_id property of this CreateVolumeDetails.
        :type volume_backup_id: str

        """
        self.swagger_types = {
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'size_in_gbs': 'int',
            'size_in_mbs': 'int',
            'source_details': 'VolumeSourceDetails',
            'volume_backup_id': 'str'
        }

        self.attribute_map = {
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'size_in_gbs': 'sizeInGBs',
            'size_in_mbs': 'sizeInMBs',
            'source_details': 'sourceDetails',
            'volume_backup_id': 'volumeBackupId'
        }

        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._size_in_gbs = None
        self._size_in_mbs = None
        self._source_details = None
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
        Avoid entering confidential information.


        :return: The display_name of this CreateVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVolumeDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this CreateVolumeDetails.
        The size of the volume in GBs.


        :return: The size_in_gbs of this CreateVolumeDetails.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this CreateVolumeDetails.
        The size of the volume in GBs.


        :param size_in_gbs: The size_in_gbs of this CreateVolumeDetails.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this CreateVolumeDetails.
        The size of the volume in MBs. The value must be a multiple of 1024.
        This field is deprecated. Use sizeInGBs instead.


        :return: The size_in_mbs of this CreateVolumeDetails.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this CreateVolumeDetails.
        The size of the volume in MBs. The value must be a multiple of 1024.
        This field is deprecated. Use sizeInGBs instead.


        :param size_in_mbs: The size_in_mbs of this CreateVolumeDetails.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def source_details(self):
        """
        Gets the source_details of this CreateVolumeDetails.
        Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same Availability Domain or a Block volume backup.
        This is an optional field. If not specified or set to null, the new Block volume will be empty.
        When specified, the new Block volume will contain data from the source volume or backup.


        :return: The source_details of this CreateVolumeDetails.
        :rtype: VolumeSourceDetails
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this CreateVolumeDetails.
        Specifies the volume source details for a new Block volume. The volume source is either another Block volume in the same Availability Domain or a Block volume backup.
        This is an optional field. If not specified or set to null, the new Block volume will be empty.
        When specified, the new Block volume will contain data from the source volume or backup.


        :param source_details: The source_details of this CreateVolumeDetails.
        :type: VolumeSourceDetails
        """
        self._source_details = source_details

    @property
    def volume_backup_id(self):
        """
        Gets the volume_backup_id of this CreateVolumeDetails.
        The OCID of the volume backup from which the data should be restored on the newly created volume.
        This field is deprecated. Use the sourceDetails field instead to specify the
        backup for the volume.


        :return: The volume_backup_id of this CreateVolumeDetails.
        :rtype: str
        """
        return self._volume_backup_id

    @volume_backup_id.setter
    def volume_backup_id(self, volume_backup_id):
        """
        Sets the volume_backup_id of this CreateVolumeDetails.
        The OCID of the volume backup from which the data should be restored on the newly created volume.
        This field is deprecated. Use the sourceDetails field instead to specify the
        backup for the volume.


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
