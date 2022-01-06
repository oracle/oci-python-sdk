# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .mount_type_details import MountTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutomatedMountDetails(MountTypeDetails):
    """
    Used for creating NFS Auto Mount backup destinations for autonomous on ExaCC.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutomatedMountDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.AutomatedMountDetails.mount_type` attribute
        of this class is ``AUTOMATED_MOUNT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mount_type:
            The value to assign to the mount_type property of this AutomatedMountDetails.
            Allowed values for this property are: "SELF_MOUNT", "AUTOMATED_MOUNT"
        :type mount_type: str

        :param nfs_server:
            The value to assign to the nfs_server property of this AutomatedMountDetails.
        :type nfs_server: list[str]

        :param nfs_server_export:
            The value to assign to the nfs_server_export property of this AutomatedMountDetails.
        :type nfs_server_export: str

        """
        self.swagger_types = {
            'mount_type': 'str',
            'nfs_server': 'list[str]',
            'nfs_server_export': 'str'
        }

        self.attribute_map = {
            'mount_type': 'mountType',
            'nfs_server': 'nfsServer',
            'nfs_server_export': 'nfsServerExport'
        }

        self._mount_type = None
        self._nfs_server = None
        self._nfs_server_export = None
        self._mount_type = 'AUTOMATED_MOUNT'

    @property
    def nfs_server(self):
        """
        **[Required]** Gets the nfs_server of this AutomatedMountDetails.
        IP addresses for NFS Auto mount.


        :return: The nfs_server of this AutomatedMountDetails.
        :rtype: list[str]
        """
        return self._nfs_server

    @nfs_server.setter
    def nfs_server(self, nfs_server):
        """
        Sets the nfs_server of this AutomatedMountDetails.
        IP addresses for NFS Auto mount.


        :param nfs_server: The nfs_server of this AutomatedMountDetails.
        :type: list[str]
        """
        self._nfs_server = nfs_server

    @property
    def nfs_server_export(self):
        """
        **[Required]** Gets the nfs_server_export of this AutomatedMountDetails.
        Specifies the directory on which to mount the file system


        :return: The nfs_server_export of this AutomatedMountDetails.
        :rtype: str
        """
        return self._nfs_server_export

    @nfs_server_export.setter
    def nfs_server_export(self, nfs_server_export):
        """
        Sets the nfs_server_export of this AutomatedMountDetails.
        Specifies the directory on which to mount the file system


        :param nfs_server_export: The nfs_server_export of this AutomatedMountDetails.
        :type: str
        """
        self._nfs_server_export = nfs_server_export

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
