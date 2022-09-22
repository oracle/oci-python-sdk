# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceDetails(object):
    """
    Source information for the file system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parent_file_system_id:
            The value to assign to the parent_file_system_id property of this SourceDetails.
        :type parent_file_system_id: str

        :param source_snapshot_id:
            The value to assign to the source_snapshot_id property of this SourceDetails.
        :type source_snapshot_id: str

        """
        self.swagger_types = {
            'parent_file_system_id': 'str',
            'source_snapshot_id': 'str'
        }

        self.attribute_map = {
            'parent_file_system_id': 'parentFileSystemId',
            'source_snapshot_id': 'sourceSnapshotId'
        }

        self._parent_file_system_id = None
        self._source_snapshot_id = None

    @property
    def parent_file_system_id(self):
        """
        Gets the parent_file_system_id of this SourceDetails.
        The `OCID`__ of the file system that contains the source snapshot of a cloned file system.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :return: The parent_file_system_id of this SourceDetails.
        :rtype: str
        """
        return self._parent_file_system_id

    @parent_file_system_id.setter
    def parent_file_system_id(self, parent_file_system_id):
        """
        Sets the parent_file_system_id of this SourceDetails.
        The `OCID`__ of the file system that contains the source snapshot of a cloned file system.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :param parent_file_system_id: The parent_file_system_id of this SourceDetails.
        :type: str
        """
        self._parent_file_system_id = parent_file_system_id

    @property
    def source_snapshot_id(self):
        """
        Gets the source_snapshot_id of this SourceDetails.
        The `OCID`__ of the source snapshot used to create a cloned file system.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :return: The source_snapshot_id of this SourceDetails.
        :rtype: str
        """
        return self._source_snapshot_id

    @source_snapshot_id.setter
    def source_snapshot_id(self, source_snapshot_id):
        """
        Sets the source_snapshot_id of this SourceDetails.
        The `OCID`__ of the source snapshot used to create a cloned file system.
        See `Cloning a File System`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm


        :param source_snapshot_id: The source_snapshot_id of this SourceDetails.
        :type: str
        """
        self._source_snapshot_id = source_snapshot_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
