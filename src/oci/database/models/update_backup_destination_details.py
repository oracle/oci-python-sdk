# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateBackupDestinationDetails(object):
    """
    For a RECOVERY_APPLIANCE backup destination, used to update the connection string and/or the list of VPC users.
    For an NFS backup destination, used to update the NFS location.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateBackupDestinationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vpc_users:
            The value to assign to the vpc_users property of this UpdateBackupDestinationDetails.
        :type vpc_users: list[str]

        :param connection_string:
            The value to assign to the connection_string property of this UpdateBackupDestinationDetails.
        :type connection_string: str

        :param local_mount_point_path:
            The value to assign to the local_mount_point_path property of this UpdateBackupDestinationDetails.
        :type local_mount_point_path: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateBackupDestinationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateBackupDestinationDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'vpc_users': 'list[str]',
            'connection_string': 'str',
            'local_mount_point_path': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'vpc_users': 'vpcUsers',
            'connection_string': 'connectionString',
            'local_mount_point_path': 'localMountPointPath',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._vpc_users = None
        self._connection_string = None
        self._local_mount_point_path = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def vpc_users(self):
        """
        Gets the vpc_users of this UpdateBackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.


        :return: The vpc_users of this UpdateBackupDestinationDetails.
        :rtype: list[str]
        """
        return self._vpc_users

    @vpc_users.setter
    def vpc_users(self, vpc_users):
        """
        Sets the vpc_users of this UpdateBackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) users that are used to access the Recovery Appliance.


        :param vpc_users: The vpc_users of this UpdateBackupDestinationDetails.
        :type: list[str]
        """
        self._vpc_users = vpc_users

    @property
    def connection_string(self):
        """
        Gets the connection_string of this UpdateBackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.


        :return: The connection_string of this UpdateBackupDestinationDetails.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this UpdateBackupDestinationDetails.
        For a RECOVERY_APPLIANCE backup destination, the connection string for connecting to the Recovery Appliance.


        :param connection_string: The connection_string of this UpdateBackupDestinationDetails.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def local_mount_point_path(self):
        """
        Gets the local_mount_point_path of this UpdateBackupDestinationDetails.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :return: The local_mount_point_path of this UpdateBackupDestinationDetails.
        :rtype: str
        """
        return self._local_mount_point_path

    @local_mount_point_path.setter
    def local_mount_point_path(self, local_mount_point_path):
        """
        Sets the local_mount_point_path of this UpdateBackupDestinationDetails.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :param local_mount_point_path: The local_mount_point_path of this UpdateBackupDestinationDetails.
        :type: str
        """
        self._local_mount_point_path = local_mount_point_path

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateBackupDestinationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateBackupDestinationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateBackupDestinationDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateBackupDestinationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateBackupDestinationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateBackupDestinationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateBackupDestinationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateBackupDestinationDetails.
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
