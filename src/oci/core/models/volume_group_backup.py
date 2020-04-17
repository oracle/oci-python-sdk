# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroupBackup(object):
    """
    A point-in-time copy of a volume group that can then be used to create a new volume group
    or restore a volume group. For more information, see `Volume Groups`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Block/Concepts/volumegroups.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupBackup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupBackup.
    #: This constant has a value of "COMMITTED"
    LIFECYCLE_STATE_COMMITTED = "COMMITTED"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupBackup.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupBackup.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupBackup.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupBackup.
    #: This constant has a value of "FAULTY"
    LIFECYCLE_STATE_FAULTY = "FAULTY"

    #: A constant which can be used with the lifecycle_state property of a VolumeGroupBackup.
    #: This constant has a value of "REQUEST_RECEIVED"
    LIFECYCLE_STATE_REQUEST_RECEIVED = "REQUEST_RECEIVED"

    #: A constant which can be used with the type property of a VolumeGroupBackup.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a VolumeGroupBackup.
    #: This constant has a value of "INCREMENTAL"
    TYPE_INCREMENTAL = "INCREMENTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroupBackup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this VolumeGroupBackup.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this VolumeGroupBackup.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this VolumeGroupBackup.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VolumeGroupBackup.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this VolumeGroupBackup.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VolumeGroupBackup.
            Allowed values for this property are: "CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this VolumeGroupBackup.
        :type size_in_mbs: int

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this VolumeGroupBackup.
        :type size_in_gbs: int

        :param time_created:
            The value to assign to the time_created property of this VolumeGroupBackup.
        :type time_created: datetime

        :param time_request_received:
            The value to assign to the time_request_received property of this VolumeGroupBackup.
        :type time_request_received: datetime

        :param type:
            The value to assign to the type property of this VolumeGroupBackup.
            Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param unique_size_in_mbs:
            The value to assign to the unique_size_in_mbs property of this VolumeGroupBackup.
        :type unique_size_in_mbs: int

        :param unique_size_in_gbs:
            The value to assign to the unique_size_in_gbs property of this VolumeGroupBackup.
        :type unique_size_in_gbs: int

        :param volume_backup_ids:
            The value to assign to the volume_backup_ids property of this VolumeGroupBackup.
        :type volume_backup_ids: list[str]

        :param volume_group_id:
            The value to assign to the volume_group_id property of this VolumeGroupBackup.
        :type volume_group_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'size_in_mbs': 'int',
            'size_in_gbs': 'int',
            'time_created': 'datetime',
            'time_request_received': 'datetime',
            'type': 'str',
            'unique_size_in_mbs': 'int',
            'unique_size_in_gbs': 'int',
            'volume_backup_ids': 'list[str]',
            'volume_group_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'size_in_mbs': 'sizeInMBs',
            'size_in_gbs': 'sizeInGBs',
            'time_created': 'timeCreated',
            'time_request_received': 'timeRequestReceived',
            'type': 'type',
            'unique_size_in_mbs': 'uniqueSizeInMbs',
            'unique_size_in_gbs': 'uniqueSizeInGbs',
            'volume_backup_ids': 'volumeBackupIds',
            'volume_group_id': 'volumeGroupId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._size_in_mbs = None
        self._size_in_gbs = None
        self._time_created = None
        self._time_request_received = None
        self._type = None
        self._unique_size_in_mbs = None
        self._unique_size_in_gbs = None
        self._volume_backup_ids = None
        self._volume_group_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VolumeGroupBackup.
        The OCID of the compartment that contains the volume group backup.


        :return: The compartment_id of this VolumeGroupBackup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VolumeGroupBackup.
        The OCID of the compartment that contains the volume group backup.


        :param compartment_id: The compartment_id of this VolumeGroupBackup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VolumeGroupBackup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VolumeGroupBackup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VolumeGroupBackup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VolumeGroupBackup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VolumeGroupBackup.
        A user-friendly name for the volume group backup. Does not have to be unique and it's changeable. Avoid entering confidential information.


        :return: The display_name of this VolumeGroupBackup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeGroupBackup.
        A user-friendly name for the volume group backup. Does not have to be unique and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this VolumeGroupBackup.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VolumeGroupBackup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VolumeGroupBackup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VolumeGroupBackup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VolumeGroupBackup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VolumeGroupBackup.
        The OCID of the volume group backup.


        :return: The id of this VolumeGroupBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeGroupBackup.
        The OCID of the volume group backup.


        :param id: The id of this VolumeGroupBackup.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VolumeGroupBackup.
        The current state of a volume group backup.

        Allowed values for this property are: "CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VolumeGroupBackup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VolumeGroupBackup.
        The current state of a volume group backup.


        :param lifecycle_state: The lifecycle_state of this VolumeGroupBackup.
        :type: str
        """
        allowed_values = ["CREATING", "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this VolumeGroupBackup.
        The aggregate size of the volume group backup, in MBs.


        :return: The size_in_mbs of this VolumeGroupBackup.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this VolumeGroupBackup.
        The aggregate size of the volume group backup, in MBs.


        :param size_in_mbs: The size_in_mbs of this VolumeGroupBackup.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this VolumeGroupBackup.
        The aggregate size of the volume group backup, in GBs.


        :return: The size_in_gbs of this VolumeGroupBackup.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this VolumeGroupBackup.
        The aggregate size of the volume group backup, in GBs.


        :param size_in_gbs: The size_in_gbs of this VolumeGroupBackup.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VolumeGroupBackup.
        The date and time the volume group backup was created. This is the time the actual point-in-time image
        of the volume group data was taken. Format defined by RFC3339.


        :return: The time_created of this VolumeGroupBackup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeGroupBackup.
        The date and time the volume group backup was created. This is the time the actual point-in-time image
        of the volume group data was taken. Format defined by RFC3339.


        :param time_created: The time_created of this VolumeGroupBackup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_request_received(self):
        """
        Gets the time_request_received of this VolumeGroupBackup.
        The date and time the request to create the volume group backup was received. Format defined by RFC3339.


        :return: The time_request_received of this VolumeGroupBackup.
        :rtype: datetime
        """
        return self._time_request_received

    @time_request_received.setter
    def time_request_received(self, time_request_received):
        """
        Sets the time_request_received of this VolumeGroupBackup.
        The date and time the request to create the volume group backup was received. Format defined by RFC3339.


        :param time_request_received: The time_request_received of this VolumeGroupBackup.
        :type: datetime
        """
        self._time_request_received = time_request_received

    @property
    def type(self):
        """
        **[Required]** Gets the type of this VolumeGroupBackup.
        The type of backup.

        Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this VolumeGroupBackup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VolumeGroupBackup.
        The type of backup.


        :param type: The type of this VolumeGroupBackup.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def unique_size_in_mbs(self):
        """
        Gets the unique_size_in_mbs of this VolumeGroupBackup.
        The aggregate size used by the volume group backup, in MBs.
        It is typically smaller than sizeInMBs, depending on the space
        consumed on the volume group and whether the volume backup is full or incremental.


        :return: The unique_size_in_mbs of this VolumeGroupBackup.
        :rtype: int
        """
        return self._unique_size_in_mbs

    @unique_size_in_mbs.setter
    def unique_size_in_mbs(self, unique_size_in_mbs):
        """
        Sets the unique_size_in_mbs of this VolumeGroupBackup.
        The aggregate size used by the volume group backup, in MBs.
        It is typically smaller than sizeInMBs, depending on the space
        consumed on the volume group and whether the volume backup is full or incremental.


        :param unique_size_in_mbs: The unique_size_in_mbs of this VolumeGroupBackup.
        :type: int
        """
        self._unique_size_in_mbs = unique_size_in_mbs

    @property
    def unique_size_in_gbs(self):
        """
        Gets the unique_size_in_gbs of this VolumeGroupBackup.
        The aggregate size used by the volume group backup, in GBs.
        It is typically smaller than sizeInGBs, depending on the space
        consumed on the volume group and whether the volume backup is full or incremental.


        :return: The unique_size_in_gbs of this VolumeGroupBackup.
        :rtype: int
        """
        return self._unique_size_in_gbs

    @unique_size_in_gbs.setter
    def unique_size_in_gbs(self, unique_size_in_gbs):
        """
        Sets the unique_size_in_gbs of this VolumeGroupBackup.
        The aggregate size used by the volume group backup, in GBs.
        It is typically smaller than sizeInGBs, depending on the space
        consumed on the volume group and whether the volume backup is full or incremental.


        :param unique_size_in_gbs: The unique_size_in_gbs of this VolumeGroupBackup.
        :type: int
        """
        self._unique_size_in_gbs = unique_size_in_gbs

    @property
    def volume_backup_ids(self):
        """
        **[Required]** Gets the volume_backup_ids of this VolumeGroupBackup.
        OCIDs for the volume backups in this volume group backup.


        :return: The volume_backup_ids of this VolumeGroupBackup.
        :rtype: list[str]
        """
        return self._volume_backup_ids

    @volume_backup_ids.setter
    def volume_backup_ids(self, volume_backup_ids):
        """
        Sets the volume_backup_ids of this VolumeGroupBackup.
        OCIDs for the volume backups in this volume group backup.


        :param volume_backup_ids: The volume_backup_ids of this VolumeGroupBackup.
        :type: list[str]
        """
        self._volume_backup_ids = volume_backup_ids

    @property
    def volume_group_id(self):
        """
        Gets the volume_group_id of this VolumeGroupBackup.
        The OCID of the source volume group.


        :return: The volume_group_id of this VolumeGroupBackup.
        :rtype: str
        """
        return self._volume_group_id

    @volume_group_id.setter
    def volume_group_id(self, volume_group_id):
        """
        Sets the volume_group_id of this VolumeGroupBackup.
        The OCID of the source volume group.


        :param volume_group_id: The volume_group_id of this VolumeGroupBackup.
        :type: str
        """
        self._volume_group_id = volume_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
