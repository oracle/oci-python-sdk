# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


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

        """
        self.swagger_types = {
            'file_system_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'name': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'file_system_id': 'fileSystemId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'name': 'name',
            'time_created': 'timeCreated'
        }

        self._file_system_id = None
        self._id = None
        self._lifecycle_state = None
        self._name = None
        self._time_created = None

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this Snapshot.
        The OCID of the file system from which the snapshot
        was created.


        :return: The file_system_id of this Snapshot.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this Snapshot.
        The OCID of the file system from which the snapshot
        was created.


        :param file_system_id: The file_system_id of this Snapshot.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Snapshot.
        The OCID of the snapshot.


        :return: The id of this Snapshot.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Snapshot.
        The OCID of the snapshot.


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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
