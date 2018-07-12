# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Export(object):
    """
    A file system and the path that you can use to mount it. Each export
    resource belongs to exactly one export set.

    The export's path attribute is not a path in the
    referenced file system, but the value used by clients for the path
    component of the remotetarget argument when mounting the file
    system.

    The path must start with a slash (/) followed by a sequence of zero or more
    slash-separated path elements. For any two export resources associated with
    the same export set, except those in a 'DELETED' state, the path element
    sequence for the first export resource can't contain the
    complete path element sequence of the second export resource.


    For example, the following are acceptable:

    * /example and /path
    * /example1 and /example2
    * /example and /example1

    The following examples are not acceptable:
    * /example and /example/path
    * / and /example

    Paths may not end in a slash (/). No path element can be a period (.)
    or two periods in sequence (..). All path elements must be 255 bytes or less.

    No two non-'DELETED' export resources in the same export set can
    reference the same file system.

    Use `exportOptions` to control access to an export. For more information, see
    `Export Options`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/File/Tasks/exportoptions.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Export.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Export.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Export.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Export.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new Export object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_options:
            The value to assign to the export_options property of this Export.
        :type export_options: list[ClientOptions]

        :param export_set_id:
            The value to assign to the export_set_id property of this Export.
        :type export_set_id: str

        :param file_system_id:
            The value to assign to the file_system_id property of this Export.
        :type file_system_id: str

        :param id:
            The value to assign to the id property of this Export.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Export.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param path:
            The value to assign to the path property of this Export.
        :type path: str

        :param time_created:
            The value to assign to the time_created property of this Export.
        :type time_created: datetime

        """
        self.swagger_types = {
            'export_options': 'list[ClientOptions]',
            'export_set_id': 'str',
            'file_system_id': 'str',
            'id': 'str',
            'lifecycle_state': 'str',
            'path': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'export_options': 'exportOptions',
            'export_set_id': 'exportSetId',
            'file_system_id': 'fileSystemId',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'path': 'path',
            'time_created': 'timeCreated'
        }

        self._export_options = None
        self._export_set_id = None
        self._file_system_id = None
        self._id = None
        self._lifecycle_state = None
        self._path = None
        self._time_created = None

    @property
    def export_options(self):
        """
        **[Required]** Gets the export_options of this Export.
        Policies that apply to NFS requests made through this
        export. `exportOptions` contains a sequential list of
        `ClientOptions`. Each `ClientOptions` item defines the
        export options that are applied to a specified
        set of clients.

        For each NFS request, the first `ClientOptions` option
        in the list whose `source` attribute matches the source
        IP address of the request is applied.

        If a client source IP address does not match the `source`
        property of any `ClientOptions` in the list, then the
        export will be invisible to that client. This export will
        not be returned by `MOUNTPROC_EXPORT` calls made by the client
        and any attempt to mount or access the file system through
        this export will result in an error.

        **Exports without defined `ClientOptions` are invisible to all clients.**

        If one export is invisible to a particular client, associated file
        systems may still be accessible through other exports on the same
        or different mount targets.
        To completely deny client access to a file system, be sure that the client
        source IP address is not included in any export for any mount target
        associated with the file system.


        :return: The export_options of this Export.
        :rtype: list[ClientOptions]
        """
        return self._export_options

    @export_options.setter
    def export_options(self, export_options):
        """
        Sets the export_options of this Export.
        Policies that apply to NFS requests made through this
        export. `exportOptions` contains a sequential list of
        `ClientOptions`. Each `ClientOptions` item defines the
        export options that are applied to a specified
        set of clients.

        For each NFS request, the first `ClientOptions` option
        in the list whose `source` attribute matches the source
        IP address of the request is applied.

        If a client source IP address does not match the `source`
        property of any `ClientOptions` in the list, then the
        export will be invisible to that client. This export will
        not be returned by `MOUNTPROC_EXPORT` calls made by the client
        and any attempt to mount or access the file system through
        this export will result in an error.

        **Exports without defined `ClientOptions` are invisible to all clients.**

        If one export is invisible to a particular client, associated file
        systems may still be accessible through other exports on the same
        or different mount targets.
        To completely deny client access to a file system, be sure that the client
        source IP address is not included in any export for any mount target
        associated with the file system.


        :param export_options: The export_options of this Export.
        :type: list[ClientOptions]
        """
        self._export_options = export_options

    @property
    def export_set_id(self):
        """
        **[Required]** Gets the export_set_id of this Export.
        The OCID of this export's export set.


        :return: The export_set_id of this Export.
        :rtype: str
        """
        return self._export_set_id

    @export_set_id.setter
    def export_set_id(self, export_set_id):
        """
        Sets the export_set_id of this Export.
        The OCID of this export's export set.


        :param export_set_id: The export_set_id of this Export.
        :type: str
        """
        self._export_set_id = export_set_id

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this Export.
        The OCID of this export's file system.


        :return: The file_system_id of this Export.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this Export.
        The OCID of this export's file system.


        :param file_system_id: The file_system_id of this Export.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Export.
        The OCID of this export.


        :return: The id of this Export.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Export.
        The OCID of this export.


        :param id: The id of this Export.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Export.
        The current state of this export.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Export.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Export.
        The current state of this export.


        :param lifecycle_state: The lifecycle_state of this Export.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def path(self):
        """
        **[Required]** Gets the path of this Export.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/accounting`


        :return: The path of this Export.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this Export.
        Path used to access the associated file system.

        Avoid entering confidential information.

        Example: `/accounting`


        :param path: The path of this Export.
        :type: str
        """
        self._path = path

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Export.
        The date and time the export was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this Export.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Export.
        The date and time the export was created, expressed
        in `RFC 3339`__ timestamp format.

        Example: `2016-08-25T21:10:29.600Z`

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this Export.
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
