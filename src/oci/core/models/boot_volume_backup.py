# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BootVolumeBackup(object):
    """
    A point-in-time copy of a boot volume that can then be used to create
    a new boot volume or recover a boot volume. For more information, see `Overview
    of Boot Volume Backups`__
    To use any of the API operations, you must be authorized in an IAM policy.
    If you're not authorized, talk to an administrator. If you're an administrator
    who needs to write policies to give users access, see `Getting Started with
    Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Block/Concepts/bootvolumebackups.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a BootVolumeBackup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeBackup.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeBackup.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeBackup.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeBackup.
    #: This constant has a value of "FAULTY"
    LIFECYCLE_STATE_FAULTY = "FAULTY"

    #: A constant which can be used with the lifecycle_state property of a BootVolumeBackup.
    #: This constant has a value of "REQUEST_RECEIVED"
    LIFECYCLE_STATE_REQUEST_RECEIVED = "REQUEST_RECEIVED"

    #: A constant which can be used with the source_type property of a BootVolumeBackup.
    #: This constant has a value of "MANUAL"
    SOURCE_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the source_type property of a BootVolumeBackup.
    #: This constant has a value of "SCHEDULED"
    SOURCE_TYPE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the type property of a BootVolumeBackup.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the type property of a BootVolumeBackup.
    #: This constant has a value of "INCREMENTAL"
    TYPE_INCREMENTAL = "INCREMENTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new BootVolumeBackup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param boot_volume_id:
            The value to assign to the boot_volume_id property of this BootVolumeBackup.
        :type boot_volume_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BootVolumeBackup.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this BootVolumeBackup.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this BootVolumeBackup.
        :type system_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this BootVolumeBackup.
        :type display_name: str

        :param expiration_time:
            The value to assign to the expiration_time property of this BootVolumeBackup.
        :type expiration_time: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BootVolumeBackup.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this BootVolumeBackup.
        :type id: str

        :param image_id:
            The value to assign to the image_id property of this BootVolumeBackup.
        :type image_id: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this BootVolumeBackup.
        :type kms_key_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BootVolumeBackup.
            Allowed values for this property are: "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param size_in_gbs:
            The value to assign to the size_in_gbs property of this BootVolumeBackup.
        :type size_in_gbs: int

        :param source_boot_volume_backup_id:
            The value to assign to the source_boot_volume_backup_id property of this BootVolumeBackup.
        :type source_boot_volume_backup_id: str

        :param source_type:
            The value to assign to the source_type property of this BootVolumeBackup.
            Allowed values for this property are: "MANUAL", "SCHEDULED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param time_created:
            The value to assign to the time_created property of this BootVolumeBackup.
        :type time_created: datetime

        :param time_request_received:
            The value to assign to the time_request_received property of this BootVolumeBackup.
        :type time_request_received: datetime

        :param type:
            The value to assign to the type property of this BootVolumeBackup.
            Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param unique_size_in_gbs:
            The value to assign to the unique_size_in_gbs property of this BootVolumeBackup.
        :type unique_size_in_gbs: int

        """
        self.swagger_types = {
            'boot_volume_id': 'str',
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'expiration_time': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'image_id': 'str',
            'kms_key_id': 'str',
            'lifecycle_state': 'str',
            'size_in_gbs': 'int',
            'source_boot_volume_backup_id': 'str',
            'source_type': 'str',
            'time_created': 'datetime',
            'time_request_received': 'datetime',
            'type': 'str',
            'unique_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'boot_volume_id': 'bootVolumeId',
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'display_name': 'displayName',
            'expiration_time': 'expirationTime',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'image_id': 'imageId',
            'kms_key_id': 'kmsKeyId',
            'lifecycle_state': 'lifecycleState',
            'size_in_gbs': 'sizeInGBs',
            'source_boot_volume_backup_id': 'sourceBootVolumeBackupId',
            'source_type': 'sourceType',
            'time_created': 'timeCreated',
            'time_request_received': 'timeRequestReceived',
            'type': 'type',
            'unique_size_in_gbs': 'uniqueSizeInGBs'
        }

        self._boot_volume_id = None
        self._compartment_id = None
        self._defined_tags = None
        self._system_tags = None
        self._display_name = None
        self._expiration_time = None
        self._freeform_tags = None
        self._id = None
        self._image_id = None
        self._kms_key_id = None
        self._lifecycle_state = None
        self._size_in_gbs = None
        self._source_boot_volume_backup_id = None
        self._source_type = None
        self._time_created = None
        self._time_request_received = None
        self._type = None
        self._unique_size_in_gbs = None

    @property
    def boot_volume_id(self):
        """
        Gets the boot_volume_id of this BootVolumeBackup.
        The OCID of the boot volume.


        :return: The boot_volume_id of this BootVolumeBackup.
        :rtype: str
        """
        return self._boot_volume_id

    @boot_volume_id.setter
    def boot_volume_id(self, boot_volume_id):
        """
        Sets the boot_volume_id of this BootVolumeBackup.
        The OCID of the boot volume.


        :param boot_volume_id: The boot_volume_id of this BootVolumeBackup.
        :type: str
        """
        self._boot_volume_id = boot_volume_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BootVolumeBackup.
        The OCID of the compartment that contains the boot volume backup.


        :return: The compartment_id of this BootVolumeBackup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BootVolumeBackup.
        The OCID of the compartment that contains the boot volume backup.


        :param compartment_id: The compartment_id of this BootVolumeBackup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BootVolumeBackup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this BootVolumeBackup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BootVolumeBackup.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this BootVolumeBackup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this BootVolumeBackup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The system_tags of this BootVolumeBackup.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this BootVolumeBackup.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param system_tags: The system_tags of this BootVolumeBackup.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BootVolumeBackup.
        A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this BootVolumeBackup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BootVolumeBackup.
        A user-friendly name for the boot volume backup. Does not have to be unique and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this BootVolumeBackup.
        :type: str
        """
        self._display_name = display_name

    @property
    def expiration_time(self):
        """
        Gets the expiration_time of this BootVolumeBackup.
        The date and time the volume backup will expire and be automatically deleted.
        Format defined by `RFC3339`__. This parameter will always be present for backups that
        were created automatically by a scheduled-backup policy. For manually created backups,
        it will be absent, signifying that there is no expiration time and the backup will
        last forever until manually deleted.

        __ https://tools.ietf.org/html/rfc3339


        :return: The expiration_time of this BootVolumeBackup.
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """
        Sets the expiration_time of this BootVolumeBackup.
        The date and time the volume backup will expire and be automatically deleted.
        Format defined by `RFC3339`__. This parameter will always be present for backups that
        were created automatically by a scheduled-backup policy. For manually created backups,
        it will be absent, signifying that there is no expiration time and the backup will
        last forever until manually deleted.

        __ https://tools.ietf.org/html/rfc3339


        :param expiration_time: The expiration_time of this BootVolumeBackup.
        :type: datetime
        """
        self._expiration_time = expiration_time

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BootVolumeBackup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this BootVolumeBackup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BootVolumeBackup.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this BootVolumeBackup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BootVolumeBackup.
        The OCID of the boot volume backup.


        :return: The id of this BootVolumeBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BootVolumeBackup.
        The OCID of the boot volume backup.


        :param id: The id of this BootVolumeBackup.
        :type: str
        """
        self._id = id

    @property
    def image_id(self):
        """
        Gets the image_id of this BootVolumeBackup.
        The image OCID used to create the boot volume the backup is taken from.


        :return: The image_id of this BootVolumeBackup.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this BootVolumeBackup.
        The image OCID used to create the boot volume the backup is taken from.


        :param image_id: The image_id of this BootVolumeBackup.
        :type: str
        """
        self._image_id = image_id

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this BootVolumeBackup.
        The OCID of the Key Management master encryption assigned to the boot volume backup.
        For more information about the Key Management service and encryption keys, see
        `Overview of Key Management`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Tasks/usingkeys.htm


        :return: The kms_key_id of this BootVolumeBackup.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this BootVolumeBackup.
        The OCID of the Key Management master encryption assigned to the boot volume backup.
        For more information about the Key Management service and encryption keys, see
        `Overview of Key Management`__ and
        `Using Keys`__.

        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Tasks/usingkeys.htm


        :param kms_key_id: The kms_key_id of this BootVolumeBackup.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BootVolumeBackup.
        The current state of a boot volume backup.

        Allowed values for this property are: "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BootVolumeBackup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BootVolumeBackup.
        The current state of a boot volume backup.


        :param lifecycle_state: The lifecycle_state of this BootVolumeBackup.
        :type: str
        """
        allowed_values = ["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def size_in_gbs(self):
        """
        Gets the size_in_gbs of this BootVolumeBackup.
        The size of the boot volume, in GBs.


        :return: The size_in_gbs of this BootVolumeBackup.
        :rtype: int
        """
        return self._size_in_gbs

    @size_in_gbs.setter
    def size_in_gbs(self, size_in_gbs):
        """
        Sets the size_in_gbs of this BootVolumeBackup.
        The size of the boot volume, in GBs.


        :param size_in_gbs: The size_in_gbs of this BootVolumeBackup.
        :type: int
        """
        self._size_in_gbs = size_in_gbs

    @property
    def source_boot_volume_backup_id(self):
        """
        Gets the source_boot_volume_backup_id of this BootVolumeBackup.
        The OCID of the source boot volume backup.


        :return: The source_boot_volume_backup_id of this BootVolumeBackup.
        :rtype: str
        """
        return self._source_boot_volume_backup_id

    @source_boot_volume_backup_id.setter
    def source_boot_volume_backup_id(self, source_boot_volume_backup_id):
        """
        Sets the source_boot_volume_backup_id of this BootVolumeBackup.
        The OCID of the source boot volume backup.


        :param source_boot_volume_backup_id: The source_boot_volume_backup_id of this BootVolumeBackup.
        :type: str
        """
        self._source_boot_volume_backup_id = source_boot_volume_backup_id

    @property
    def source_type(self):
        """
        Gets the source_type of this BootVolumeBackup.
        Specifies whether the backup was created manually, or via scheduled backup policy.

        Allowed values for this property are: "MANUAL", "SCHEDULED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this BootVolumeBackup.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this BootVolumeBackup.
        Specifies whether the backup was created manually, or via scheduled backup policy.


        :param source_type: The source_type of this BootVolumeBackup.
        :type: str
        """
        allowed_values = ["MANUAL", "SCHEDULED"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BootVolumeBackup.
        The date and time the boot volume backup was created. This is the time the actual point-in-time image
        of the volume data was taken. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this BootVolumeBackup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BootVolumeBackup.
        The date and time the boot volume backup was created. This is the time the actual point-in-time image
        of the volume data was taken. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this BootVolumeBackup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_request_received(self):
        """
        Gets the time_request_received of this BootVolumeBackup.
        The date and time the request to create the boot volume backup was received. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_request_received of this BootVolumeBackup.
        :rtype: datetime
        """
        return self._time_request_received

    @time_request_received.setter
    def time_request_received(self, time_request_received):
        """
        Sets the time_request_received of this BootVolumeBackup.
        The date and time the request to create the boot volume backup was received. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_request_received: The time_request_received of this BootVolumeBackup.
        :type: datetime
        """
        self._time_request_received = time_request_received

    @property
    def type(self):
        """
        Gets the type of this BootVolumeBackup.
        The type of a volume backup.

        Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this BootVolumeBackup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BootVolumeBackup.
        The type of a volume backup.


        :param type: The type of this BootVolumeBackup.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def unique_size_in_gbs(self):
        """
        Gets the unique_size_in_gbs of this BootVolumeBackup.
        The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space
        consumed on the boot volume and whether the backup is full or incremental.


        :return: The unique_size_in_gbs of this BootVolumeBackup.
        :rtype: int
        """
        return self._unique_size_in_gbs

    @unique_size_in_gbs.setter
    def unique_size_in_gbs(self, unique_size_in_gbs):
        """
        Sets the unique_size_in_gbs of this BootVolumeBackup.
        The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the space
        consumed on the boot volume and whether the backup is full or incremental.


        :param unique_size_in_gbs: The unique_size_in_gbs of this BootVolumeBackup.
        :type: int
        """
        self._unique_size_in_gbs = unique_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
