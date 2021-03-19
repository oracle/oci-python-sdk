# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeBackup(object):
    """
    A point-in-time copy of a volume that can then be used to create a new block volume
    or recover a block volume. For more information, see
    `Overview of Cloud Volume Storage`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/iaas/Content/Block/Concepts/overview.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a VolumeBackup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a VolumeBackup.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a VolumeBackup.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a VolumeBackup.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a VolumeBackup.
    #: This constant has a value of "FAULTY"
    LIFECYCLE_STATE_FAULTY = "FAULTY"

    #: A constant which can be used with the lifecycle_state property of a VolumeBackup.
    #: This constant has a value of "REQUEST_RECEIVED"
    LIFECYCLE_STATE_REQUEST_RECEIVED = "REQUEST_RECEIVED"

    #: A constant which can be used with the source_type property of a VolumeBackup.
    #: This constant has a value of "MANUAL"
    SOURCE_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the source_type property of a VolumeBackup.
    #: This constant has a value of "SCHEDULED"
    SOURCE_TYPE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the type property of a VolumeBackup.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a VolumeBackup.
    #: This constant has a value of "INCREMENTAL"
    TYPE_INCREMENTAL = "INCREMENTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeBackup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this VolumeBackup.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this VolumeBackup.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VolumeBackup.
        :type system_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this VolumeBackup.
        :type display_name: str

        :param expiration_time:
            The value to assign to the expiration_time property of this VolumeBackup.
        :type expiration_time: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VolumeBackup.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this VolumeBackup.
        :type id: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this VolumeBackup.
        :type kms_key_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VolumeBackup.
            Allowed values for this property are: "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this VolumeBackup.
        :type size_in_gbs: int

        :param size_in_mbs:
            The value to assign to the size_in_mbs property of this VolumeBackup.
        :type size_in_mbs: int

        :param source_type:
            The value to assign to the source_type property of this VolumeBackup.
            Allowed values for this property are: "MANUAL", "SCHEDULED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param source_volume_backup_id:
            The value to assign to the source_volume_backup_id property of this VolumeBackup.
        :type source_volume_backup_id: str

        :param time_created:
            The value to assign to the time_created property of this VolumeBackup.
        :type time_created: datetime

        :param time_request_received:
            The value to assign to the time_request_received property of this VolumeBackup.
        :type time_request_received: datetime

        :param type:
            The value to assign to the type property of this VolumeBackup.
            Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param unique_size_in_gbs:
            The value to assign to the unique_size_in_gbs property of this VolumeBackup.
        :type unique_size_in_gbs: int

        :param unique_size_in_mbs:
            The value to assign to the unique_size_in_mbs property of this VolumeBackup.
        :type unique_size_in_mbs: int

        :param volume_id:
            The value to assign to the volume_id property of this VolumeBackup.
        :type volume_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'expiration_time': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'kms_key_id': 'str',
            'lifecycle_state': 'str',
            'size_in_gbs': 'int',
            'size_in_mbs': 'int',
            'source_type': 'str',
            'source_volume_backup_id': 'str',
            'time_created': 'datetime',
            'time_request_received': 'datetime',
            'type': 'str',
            'unique_size_in_gbs': 'int',
            'unique_size_in_mbs': 'int',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'display_name': 'displayName',
            'expiration_time': 'expirationTime',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'kms_key_id': 'kmsKeyId',
            'lifecycle_state': 'lifecycleState',
            'size_in_gbs': 'sizeInGBs',
            'size_in_mbs': 'sizeInMBs',
            'source_type': 'sourceType',
            'source_volume_backup_id': 'sourceVolumeBackupId',
            'time_created': 'timeCreated',
            'time_request_received': 'timeRequestReceived',
            'type': 'type',
            'unique_size_in_gbs': 'uniqueSizeInGBs',
            'unique_size_in_mbs': 'uniqueSizeInMbs',
            'volume_id': 'volumeId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._system_tags = None
        self._display_name = None
        self._expiration_time = None
        self._freeform_tags = None
        self._id = None
        self._kms_key_id = None
        self._lifecycle_state = None
        self._size_in_gbs = None
        self._size_in_mbs = None
        self._source_type = None
        self._source_volume_backup_id = None
        self._time_created = None
        self._time_request_received = None
        self._type = None
        self._unique_size_in_gbs = None
        self._unique_size_in_mbs = None
        self._volume_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VolumeBackup.
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
    def defined_tags(self):
        """
        Gets the defined_tags of this VolumeBackup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this VolumeBackup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VolumeBackup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this VolumeBackup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this VolumeBackup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The system_tags of this VolumeBackup.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this VolumeBackup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param system_tags: The system_tags of this VolumeBackup.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VolumeBackup.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this VolumeBackup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VolumeBackup.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this VolumeBackup.
        :type: str
        """
        self._display_name = display_name

    @property
    def expiration_time(self):
        """
        Gets the expiration_time of this VolumeBackup.
        The date and time the volume backup will expire and be automatically deleted.
        Format defined by `RFC3339`__. This parameter will always be present for backups that
        were created automatically by a scheduled-backup policy. For manually created backups,
        it will be absent, signifying that there is no expiration time and the backup will
        last forever until manually deleted.

        __ https://tools.ietf.org/html/rfc3339


        :return: The expiration_time of this VolumeBackup.
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """
        Sets the expiration_time of this VolumeBackup.
        The date and time the volume backup will expire and be automatically deleted.
        Format defined by `RFC3339`__. This parameter will always be present for backups that
        were created automatically by a scheduled-backup policy. For manually created backups,
        it will be absent, signifying that there is no expiration time and the backup will
        last forever until manually deleted.

        __ https://tools.ietf.org/html/rfc3339


        :param expiration_time: The expiration_time of this VolumeBackup.
        :type: datetime
        """
        self._expiration_time = expiration_time

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VolumeBackup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this VolumeBackup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VolumeBackup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this VolumeBackup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VolumeBackup.
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
    def kms_key_id(self):
        """
        Gets the kms_key_id of this VolumeBackup.
        The OCID of the Key Management key which is the master encryption key for the volume backup.
        For more information about the Key Management service and encryption keys, see
        `Overview of Key Management`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm


        :return: The kms_key_id of this VolumeBackup.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this VolumeBackup.
        The OCID of the Key Management key which is the master encryption key for the volume backup.
        For more information about the Key Management service and encryption keys, see
        `Overview of Key Management`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/iaas/Content/KeyManagement/Tasks/usingkeys.htm


        :param kms_key_id: The kms_key_id of this VolumeBackup.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VolumeBackup.
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
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this VolumeBackup.
        The size of the volume, in GBs.


        :return: The size_in_gbs of this VolumeBackup.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this VolumeBackup.
        The size of the volume, in GBs.


        :param size_in_gbs: The size_in_gbs of this VolumeBackup.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def size_in_mbs(self):
        """
        Gets the size_in_mbs of this VolumeBackup.
        The size of the volume in MBs. The value must be a multiple of 1024.
        This field is deprecated. Please use sizeInGBs.


        :return: The size_in_mbs of this VolumeBackup.
        :rtype: int
        """
        return self._size_in_mbs

    @size_in_mbs.setter
    def size_in_mbs(self, size_in_mbs):
        """
        Sets the size_in_mbs of this VolumeBackup.
        The size of the volume in MBs. The value must be a multiple of 1024.
        This field is deprecated. Please use sizeInGBs.


        :param size_in_mbs: The size_in_mbs of this VolumeBackup.
        :type: int
        """
        self._size_in_mbs = size_in_mbs

    @property
    def source_type(self):
        """
        Gets the source_type of this VolumeBackup.
        Specifies whether the backup was created manually, or via scheduled backup policy.

        Allowed values for this property are: "MANUAL", "SCHEDULED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this VolumeBackup.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this VolumeBackup.
        Specifies whether the backup was created manually, or via scheduled backup policy.


        :param source_type: The source_type of this VolumeBackup.
        :type: str
        """
        allowed_values = ["MANUAL", "SCHEDULED"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def source_volume_backup_id(self):
        """
        Gets the source_volume_backup_id of this VolumeBackup.
        The OCID of the source volume backup.


        :return: The source_volume_backup_id of this VolumeBackup.
        :rtype: str
        """
        return self._source_volume_backup_id

    @source_volume_backup_id.setter
    def source_volume_backup_id(self, source_volume_backup_id):
        """
        Sets the source_volume_backup_id of this VolumeBackup.
        The OCID of the source volume backup.


        :param source_volume_backup_id: The source_volume_backup_id of this VolumeBackup.
        :type: str
        """
        self._source_volume_backup_id = source_volume_backup_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VolumeBackup.
        The date and time the volume backup was created. This is the time the actual point-in-time image
        of the volume data was taken. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this VolumeBackup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VolumeBackup.
        The date and time the volume backup was created. This is the time the actual point-in-time image
        of the volume data was taken. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this VolumeBackup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_request_received(self):
        """
        Gets the time_request_received of this VolumeBackup.
        The date and time the request to create the volume backup was received. Format defined by [RFC3339]https://tools.ietf.org/html/rfc3339.


        :return: The time_request_received of this VolumeBackup.
        :rtype: datetime
        """
        return self._time_request_received

    @time_request_received.setter
    def time_request_received(self, time_request_received):
        """
        Sets the time_request_received of this VolumeBackup.
        The date and time the request to create the volume backup was received. Format defined by [RFC3339]https://tools.ietf.org/html/rfc3339.


        :param time_request_received: The time_request_received of this VolumeBackup.
        :type: datetime
        """
        self._time_request_received = time_request_received

    @property
    def type(self):
        """
        **[Required]** Gets the type of this VolumeBackup.
        The type of a volume backup.

        Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this VolumeBackup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VolumeBackup.
        The type of a volume backup.


        :param type: The type of this VolumeBackup.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def unique_size_in_gbs(self):
        """
        Gets the unique_size_in_gbs of this VolumeBackup.
        The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space
        consumed on the volume and whether the backup is full or incremental.


        :return: The unique_size_in_gbs of this VolumeBackup.
        :rtype: int
        """
        return self._unique_size_in_gbs

    @unique_size_in_gbs.setter
    def unique_size_in_gbs(self, unique_size_in_gbs):
        """
        Sets the unique_size_in_gbs of this VolumeBackup.
        The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space
        consumed on the volume and whether the backup is full or incremental.


        :param unique_size_in_gbs: The unique_size_in_gbs of this VolumeBackup.
        :type: int
        """
        self._unique_size_in_gbs = unique_size_in_gbs

    @property
    def unique_size_in_mbs(self):
        """
        Gets the unique_size_in_mbs of this VolumeBackup.
        The size used by the backup, in MBs. It is typically smaller than sizeInMBs, depending on the space
        consumed on the volume and whether the backup is full or incremental.
        This field is deprecated. Please use uniqueSizeInGBs.


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
        This field is deprecated. Please use uniqueSizeInGBs.


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
