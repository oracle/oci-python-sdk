# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeAttachment(object):
    """
    A base object for all types of attachments between a storage volume and an instance.
    For specific details about iSCSI attachments, see
    :class:`IScsiVolumeAttachment`.

    For general information about volume attachments, see
    `Overview of Block Volume Storage`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Block/Concepts/overview.htm
    """

    #: A constant which can be used with the lifecycle_state property of a VolumeAttachment.
    #: This constant has a value of "ATTACHING"
    LIFECYCLE_STATE_ATTACHING = "ATTACHING"

    #: A constant which can be used with the lifecycle_state property of a VolumeAttachment.
    #: This constant has a value of "ATTACHED"
    LIFECYCLE_STATE_ATTACHED = "ATTACHED"

    #: A constant which can be used with the lifecycle_state property of a VolumeAttachment.
    #: This constant has a value of "DETACHING"
    LIFECYCLE_STATE_DETACHING = "DETACHING"

    #: A constant which can be used with the lifecycle_state property of a VolumeAttachment.
    #: This constant has a value of "DETACHED"
    LIFECYCLE_STATE_DETACHED = "DETACHED"

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeAttachment object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.IScsiVolumeAttachment`
        * :class:`~oci.core.models.ParavirtualizedVolumeAttachment`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attachment_type:
            The value to assign to the attachment_type property of this VolumeAttachment.
        :type attachment_type: str

        :param availability_domain:
            The value to assign to the availability_domain property of this VolumeAttachment.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VolumeAttachment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this VolumeAttachment.
        :type display_name: str

        :param id:
            The value to assign to the id property of this VolumeAttachment.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this VolumeAttachment.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this VolumeAttachment.
        :type is_read_only: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VolumeAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this VolumeAttachment.
        :type time_created: datetime

        :param volume_id:
            The value to assign to the volume_id property of this VolumeAttachment.
        :type volume_id: str

        """
        self.swagger_types = {
            'attachment_type': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
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
            'is_read_only': 'isReadOnly',
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
        self._is_read_only = None
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

        if type == 'paravirtualized':
            return 'ParavirtualizedVolumeAttachment'
        else:
            return 'VolumeAttachment'

    @property
    def attachment_type(self):
        """
        **[Required]** Gets the attachment_type of this VolumeAttachment.
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
        **[Required]** Gets the availability_domain of this VolumeAttachment.
        The availability domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :return: The availability_domain of this VolumeAttachment.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this VolumeAttachment.
        The availability domain of an instance.

        Example: `Uocm:PHX-AD-1`


        :param availability_domain: The availability_domain of this VolumeAttachment.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VolumeAttachment.
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
        Avoid entering confidential information.

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
        Avoid entering confidential information.

        Example: `My volume attachment`


        :param display_name: The display_name of this VolumeAttachment.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VolumeAttachment.
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
        **[Required]** Gets the instance_id of this VolumeAttachment.
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
    def is_read_only(self):
        """
        Gets the is_read_only of this VolumeAttachment.
        Whether the attachment was created in read-only mode.


        :return: The is_read_only of this VolumeAttachment.
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """
        Sets the is_read_only of this VolumeAttachment.
        Whether the attachment was created in read-only mode.


        :param is_read_only: The is_read_only of this VolumeAttachment.
        :type: bool
        """
        self._is_read_only = is_read_only

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VolumeAttachment.
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
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VolumeAttachment.
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
        **[Required]** Gets the volume_id of this VolumeAttachment.
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
