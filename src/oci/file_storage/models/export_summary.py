# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExportSummary(object):
    """
    Summary information for an export.
    """

    #: A constant which can be used with the lifecycle_state property of a ExportSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExportSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExportSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ExportSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExportSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_set_id:
            The value to assign to the export_set_id property of this ExportSummary.
        :type export_set_id: str

        :param file_system_id:
            The value to assign to the file_system_id property of this ExportSummary.
        :type file_system_id: str

        :param id:
            The value to assign to the id property of this ExportSummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExportSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param path:
            The value to assign to the path property of this ExportSummary.
        :type path: str

        :param time_created:
            The value to assign to the time_created property of this ExportSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'export_set_id': 'str',
            'file_system_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'path': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'export_set_id': 'exportSetId',
            'file_system_id': 'fileSystemId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'path': 'path',
            'time_created': 'timeCreated'
        }

        self._export_set_id = None
        self._file_system_id = None
        self._id = None
        self._lifecycle_state = None
        self._path = None
        self._time_created = None

    @property
    def export_set_id(self):
        """
        **[Required]** Gets the export_set_id of this ExportSummary.
        The OCID of this export's export set.


        :return: The export_set_id of this ExportSummary.
        :rtype: str
        """
        return self._export_set_id

    @export_set_id.setter
    def export_set_id(self, export_set_id):
        """
        Sets the export_set_id of this ExportSummary.
        The OCID of this export's export set.


        :param export_set_id: The export_set_id of this ExportSummary.
        :type: str
        """
        self._export_set_id = export_set_id

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this ExportSummary.
        The OCID of this export's file system.


        :return: The file_system_id of this ExportSummary.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this ExportSummary.
        The OCID of this export's file system.


        :param file_system_id: The file_system_id of this ExportSummary.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExportSummary.
        The OCID of this export.


        :return: The id of this ExportSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExportSummary.
        The OCID of this export.


        :param id: The id of this ExportSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExportSummary.
        The current state of this export.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExportSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExportSummary.
        The current state of this export.


        :param lifecycle_state: The lifecycle_state of this ExportSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def path(self):
        """
        **[Required]** Gets the path of this ExportSummary.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/mediafiles`


        :return: The path of this ExportSummary.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ExportSummary.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/mediafiles`


        :param path: The path of this ExportSummary.
        :type: str
        """
        self._path = path

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExportSummary.
        The date and time the export was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this ExportSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExportSummary.
        The date and time the export was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this ExportSummary.
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
