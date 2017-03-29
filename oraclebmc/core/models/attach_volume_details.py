# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class AttachVolumeDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'instance_id': 'str',
            'type': 'str',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'type': 'type',
            'volume_id': 'volumeId'
        }

        self._display_name = None
        self._instance_id = None
        self._type = None
        self._volume_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'iscsi':
            return 'AttachIScsiVolumeDetails'
        else:
            return 'AttachVolumeDetails'

    @property
    def display_name(self):
        """
        Gets the display_name of this AttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it cannot be changed.


        :return: The display_name of this AttachVolumeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AttachVolumeDetails.
        A user-friendly name. Does not have to be unique, and it cannot be changed.


        :param display_name: The display_name of this AttachVolumeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def instance_id(self):
        """
        Gets the instance_id of this AttachVolumeDetails.
        The OCID of the instance.


        :return: The instance_id of this AttachVolumeDetails.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this AttachVolumeDetails.
        The OCID of the instance.


        :param instance_id: The instance_id of this AttachVolumeDetails.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """
        Gets the type of this AttachVolumeDetails.
        The type of volume. The only supported value is \"iscsi\".


        :return: The type of this AttachVolumeDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AttachVolumeDetails.
        The type of volume. The only supported value is \"iscsi\".


        :param type: The type of this AttachVolumeDetails.
        :type: str
        """
        self._type = type

    @property
    def volume_id(self):
        """
        Gets the volume_id of this AttachVolumeDetails.
        The OCID of the volume.


        :return: The volume_id of this AttachVolumeDetails.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this AttachVolumeDetails.
        The OCID of the volume.


        :param volume_id: The volume_id of this AttachVolumeDetails.
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
