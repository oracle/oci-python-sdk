# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class VolumeBackup(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'size_in_mbs': 'int',
            'time_created': 'datetime',
            'time_request_received': 'datetime',
            'unique_size_in_mbs': 'int',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'size_in_mbs': 'sizeInMBs',
            'time_created': 'timeCreated',
            'time_request_received': 'timeRequestReceived',
            'unique_size_in_mbs': 'uniqueSizeInMbs',
            'volume_id': 'volumeId'
        }

        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_state = None
        self._size_in_mbs = None
        self._time_created = None
        self._time_request_received = None
        self._unique_size_in_mbs = None
        self._volume_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VolumeBackup.
        The OCID of the compartment that contains the volume backup.


        :return: The compartment_id of this VolumeBackup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeBackup.
        The OCID of the compartment that contains the volume backup.


        :param compartment_id: The compartment_id of this VolumeBackup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VolumeBackup.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.


        :return: The display_name of this VolumeBackup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeBackup.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.


        :param display_name: The display_name of this VolumeBackup.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this VolumeBackup.
        The OCID of the volume backup.


        :return: The id of this VolumeBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeBackup.
        The OCID of the volume backup.


        :param id: The id of this VolumeBackup.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VolumeBackup.
        The current state of a volume backup.

        Allowed values for this property are: "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VolumeBackup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VolumeBackup.
        The current state of a volume backup.


        :param lifecycle_state: The lifecycle_state of this VolumeBackup.
        :type: str
        """
        allowed_values = ["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this VolumeBackup.
        The size of the volume, in MBs.


        :return: The size_in_mbs of this VolumeBackup.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this VolumeBackup.
        The size of the volume, in MBs.


        :param size_in_mbs: The size_in_mbs of this VolumeBackup.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def time_created(self):
        """
        Gets the time_created of this VolumeBackup.
        The date and time the volume backup was created. This is the time the actual point-in-time image
        of the volume data was taken. Format defined by RFC3339.


        :return: The time_created of this VolumeBackup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeBackup.
        The date and time the volume backup was created. This is the time the actual point-in-time image
        of the volume data was taken. Format defined by RFC3339.


        :param time_created: The time_created of this VolumeBackup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_request_received(self):
        """
        Gets the time_request_received of this VolumeBackup.
        The date and time the request to create the volume backup was received. Format defined by RFC3339.


        :return: The time_request_received of this VolumeBackup.
        :rtype: datetime
        """
        return self._time_request_received

    @time_request_received.setter
    def time_request_received(self, time_request_received):
        """
        Sets the time_request_received of this VolumeBackup.
        The date and time the request to create the volume backup was received. Format defined by RFC3339.


        :param time_request_received: The time_request_received of this VolumeBackup.
        :type: datetime
        """
        self._time_request_received = time_request_received

    @property
    def unique_size_in_mbs(self):
        """
        Gets the unique_size_in_mbs of this VolumeBackup.
        The size used by the backup, in MBs. It is typically smaller than sizeInMBs, depending on the space
        consumed on the volume and whether the backup is full or incremental.


        :return: The unique_size_in_mbs of this VolumeBackup.
        :rtype: int
        """
        return self._unique_size_in_mbs

    @unique_size_in_mbs.setter
    def unique_size_in_mbs(self, unique_size_in_mbs):
        """
        Sets the unique_size_in_mbs of this VolumeBackup.
        The size used by the backup, in MBs. It is typically smaller than sizeInMBs, depending on the space
        consumed on the volume and whether the backup is full or incremental.


        :param unique_size_in_mbs: The unique_size_in_mbs of this VolumeBackup.
        :type: int
        """
        self._unique_size_in_mbs = unique_size_in_mbs

    @property
    def volume_id(self):
        """
        Gets the volume_id of this VolumeBackup.
        The OCID of the volume.


        :return: The volume_id of this VolumeBackup.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this VolumeBackup.
        The OCID of the volume.


        :param volume_id: The volume_id of this VolumeBackup.
        :type: str
        """
        self._volume_id = volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
