# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class VolumeAttachment(object):

    def __init__(self):

        self.swagger_types = {
            'attachment_type': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'attachment_type': 'attachmentType',
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'volume_id': 'volumeId'
        }

        self._attachment_type = None
        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._volume_id = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['attachmentType']

        if type == 'iscsi':
            return 'IScsiVolumeAttachment'
        else:
            return 'VolumeAttachment'

    @property
    def attachment_type(self):
        """
        Gets the attachment_type of this VolumeAttachment.
        The type of volume attachment.


        :return: The attachment_type of this VolumeAttachment.
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """
        Sets the attachment_type of this VolumeAttachment.
        The type of volume attachment.


        :param attachment_type: The attachment_type of this VolumeAttachment.
        :type: str
        """
        self._attachment_type = attachment_type

    @property
    def availability_domain(self):
        """
        Gets the availability_domain of this VolumeAttachment.
        The Availability Domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this VolumeAttachment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VolumeAttachment.
        The Availability Domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this VolumeAttachment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this VolumeAttachment.
        The OCID of the compartment.


        :return: The compartment_id of this VolumeAttachment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeAttachment.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this VolumeAttachment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this VolumeAttachment.
        A user-friendly name. Does not have to be unique, and it cannot be changed.

        Example: `My volume attachment`


        :return: The display_name of this VolumeAttachment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeAttachment.
        A user-friendly name. Does not have to be unique, and it cannot be changed.

        Example: `My volume attachment`


        :param display_name: The display_name of this VolumeAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this VolumeAttachment.
        The OCID of the volume attachment.


        :return: The id of this VolumeAttachment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeAttachment.
        The OCID of the volume attachment.


        :param id: The id of this VolumeAttachment.
        :type: str
        """
        self._id = id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this VolumeAttachment.
        The OCID of the instance the volume is attached to.


        :return: The instance_id of this VolumeAttachment.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this VolumeAttachment.
        The OCID of the instance the volume is attached to.


        :param instance_id: The instance_id of this VolumeAttachment.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this VolumeAttachment.
        The current state of the volume attachment.

        Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VolumeAttachment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VolumeAttachment.
        The current state of the volume attachment.


        :param lifecycle_state: The lifecycle_state of this VolumeAttachment.
        :type: str
        """
        allowed_values = ["ATTACHING", "ATTACHED", "DETACHING", "DETACHED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this VolumeAttachment.
        The date and time the volume was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this VolumeAttachment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeAttachment.
        The date and time the volume was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this VolumeAttachment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def volume_id(self):
        """
        Gets the volume_id of this VolumeAttachment.
        The OCID of the volume.


        :return: The volume_id of this VolumeAttachment.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this VolumeAttachment.
        The OCID of the volume.


        :param volume_id: The volume_id of this VolumeAttachment.
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
