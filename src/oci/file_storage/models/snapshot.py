# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Snapshot(object):
    """
    A point-in-time snapshot of a specified file system.
    """

    #: A constant which can be used with the lifecycle_state property of a Snapshot.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Snapshot.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Snapshot.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Snapshot.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the snapshot_type property of a Snapshot.
    #: This constant has a value of "USER"
    SNAPSHOT_TYPE_USER = "USER"

    #: A constant which can be used with the snapshot_type property of a Snapshot.
    #: This constant has a value of "POLICY_BASED"
    SNAPSHOT_TYPE_POLICY_BASED = "POLICY_BASED"

    #: A constant which can be used with the snapshot_type property of a Snapshot.
    #: This constant has a value of "REPLICATION"
    SNAPSHOT_TYPE_REPLICATION = "REPLICATION"

    def __init__(self, **kwargs):
        """
        Initializes a new Snapshot object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_system_id:
            The value to assign to the file_system_id property of this Snapshot.
        :type file_system_id: str

        :param id:
            The value to assign to the id property of this Snapshot.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Snapshot.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param name:
            The value to assign to the name property of this Snapshot.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this Snapshot.
        :type time_created: datetime

        :param snapshot_type:
            The value to assign to the snapshot_type property of this Snapshot.
            Allowed values for this property are: "USER", "POLICY_BASED", "REPLICATION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type snapshot_type: str

        :param snapshot_time:
            The value to assign to the snapshot_time property of this Snapshot.
        :type snapshot_time: datetime

        :param provenance_id:
            The value to assign to the provenance_id property of this Snapshot.
        :type provenance_id: str

        :param is_clone_source:
            The value to assign to the is_clone_source property of this Snapshot.
        :type is_clone_source: bool

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Snapshot.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Snapshot.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Snapshot.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'file_system_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'snapshot_type': 'str',
            'snapshot_time': 'datetime',
            'provenance_id': 'str',
            'is_clone_source': 'bool',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'file_system_id': 'fileSystemId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'name': 'name',
            'time_created': 'timeCreated',
            'snapshot_type': 'snapshotType',
            'snapshot_time': 'snapshotTime',
            'provenance_id': 'provenanceId',
            'is_clone_source': 'isCloneSource',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._file_system_id = None
        self._id = None
        self._lifecycle_state = None
        self._name = None
        self._time_created = None
        self._snapshot_type = None
        self._snapshot_time = None
        self._provenance_id = None
        self._is_clone_source = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this Snapshot.
        The `OCID`__ of the file system from which the snapshot
        was created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The file_system_id of this Snapshot.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this Snapshot.
        The `OCID`__ of the file system from which the snapshot
        was created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param file_system_id: The file_system_id of this Snapshot.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Snapshot.
        The `OCID`__ of the snapshot.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Snapshot.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Snapshot.
        The `OCID`__ of the snapshot.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Snapshot.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Snapshot.
        The current state of the snapshot.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Snapshot.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Snapshot.
        The current state of the snapshot.


        :param lifecycle_state: The lifecycle_state of this Snapshot.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def name(self):
        """
        **[Required]** Gets the name of this Snapshot.
        Name of the snapshot. This value is immutable.

        Avoid entering confidential information.

        Example: `Sunday`


        :return: The name of this Snapshot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Snapshot.
        Name of the snapshot. This value is immutable.

        Avoid entering confidential information.

        Example: `Sunday`


        :param name: The name of this Snapshot.
        :type: str
        """
        self._name = name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Snapshot.
        The date and time the snapshot was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this Snapshot.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Snapshot.
        The date and time the snapshot was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this Snapshot.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def snapshot_type(self):
        """
        Gets the snapshot_type of this Snapshot.
        Specifies generation type of the snapshot.

        Allowed values for this property are: "USER", "POLICY_BASED", "REPLICATION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The snapshot_type of this Snapshot.
        :rtype: str
        """
        return self._snapshot_type

    @snapshot_type.setter
    def snapshot_type(self, snapshot_type):
        """
        Sets the snapshot_type of this Snapshot.
        Specifies generation type of the snapshot.


        :param snapshot_type: The snapshot_type of this Snapshot.
        :type: str
        """
        allowed_values = ["USER", "POLICY_BASED", "REPLICATION"]
        if not value_allowed_none_or_none_sentinel(snapshot_type, allowed_values):
            snapshot_type = 'UNKNOWN_ENUM_VALUE'
        self._snapshot_type = snapshot_type

    @property
    def snapshot_time(self):
        """
        Gets the snapshot_time of this Snapshot.
        The date and time the snapshot was taken, expressed
        in `RFC 3339`__ timestamp format.
        This value might be the same or different from `timeCreated` depending
        on the following factors:
        - If the snapshot is created in the original file system directory.
        - If the snapshot is cloned from a file system.
        - If the snapshot is replicated from a file system.

        Example: `2020-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The snapshot_time of this Snapshot.
        :rtype: datetime
        """
        return self._snapshot_time

    @snapshot_time.setter
    def snapshot_time(self, snapshot_time):
        """
        Sets the snapshot_time of this Snapshot.
        The date and time the snapshot was taken, expressed
        in `RFC 3339`__ timestamp format.
        This value might be the same or different from `timeCreated` depending
        on the following factors:
        - If the snapshot is created in the original file system directory.
        - If the snapshot is cloned from a file system.
        - If the snapshot is replicated from a file system.

        Example: `2020-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param snapshot_time: The snapshot_time of this Snapshot.
        :type: datetime
        """
        self._snapshot_time = snapshot_time

    @property
    def provenance_id(self):
        """
        Gets the provenance_id of this Snapshot.
        An `OCID`__ identifying the parent from which this snapshot was cloned.
        If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value.
        If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :return: The provenance_id of this Snapshot.
        :rtype: str
        """
        return self._provenance_id

    @provenance_id.setter
    def provenance_id(self, provenance_id):
        """
        Sets the provenance_id of this Snapshot.
        An `OCID`__ identifying the parent from which this snapshot was cloned.
        If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value.
        If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :param provenance_id: The provenance_id of this Snapshot.
        :type: str
        """
        self._provenance_id = provenance_id

    @property
    def is_clone_source(self):
        """
        Gets the is_clone_source of this Snapshot.
        Specifies whether the snapshot has been cloned.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :return: The is_clone_source of this Snapshot.
        :rtype: bool
        """
        return self._is_clone_source

    @is_clone_source.setter
    def is_clone_source(self, is_clone_source):
        """
        Sets the is_clone_source of this Snapshot.
        Specifies whether the snapshot has been cloned.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :param is_clone_source: The is_clone_source of this Snapshot.
        :type: bool
        """
        self._is_clone_source = is_clone_source

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Snapshot.
        Additional information about the current `lifecycleState`.


        :return: The lifecycle_details of this Snapshot.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Snapshot.
        Additional information about the current `lifecycleState`.


        :param lifecycle_details: The lifecycle_details of this Snapshot.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Snapshot.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Snapshot.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Snapshot.
        Free-form tags for this resource. Each tag is a simple key-value pair
         with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Snapshot.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Snapshot.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Snapshot.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Snapshot.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Snapshot.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
