# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSnapshotDetails(object):
    """
    CreateSnapshotDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSnapshotDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param file_system_id:
            The value to assign to the file_system_id property of this CreateSnapshotDetails.
        :type file_system_id: str

        :param name:
            The value to assign to the name property of this CreateSnapshotDetails.
        :type name: str

        """
        self.swagger_types = {
            'file_system_id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'file_system_id': 'fileSystemId',
            'name': 'name'
        }

        self._file_system_id = None
        self._name = None

    @property
    def file_system_id(self):
        """
        **[Required]** Gets the file_system_id of this CreateSnapshotDetails.
        The OCID of the file system to take a snapshot of.


        :return: The file_system_id of this CreateSnapshotDetails.
        :rtype: str
        """
        return self._file_system_id

    @file_system_id.setter
    def file_system_id(self, file_system_id):
        """
        Sets the file_system_id of this CreateSnapshotDetails.
        The OCID of the file system to take a snapshot of.


        :param file_system_id: The file_system_id of this CreateSnapshotDetails.
        :type: str
        """
        self._file_system_id = file_system_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateSnapshotDetails.
        Name of the snapshot. This value is immutable. It must also be unique with respect
        to all other non-DELETED snapshots on the associated file
        system.

        Avoid entering confidential information.

        Example: `Sunday`


        :return: The name of this CreateSnapshotDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateSnapshotDetails.
        Name of the snapshot. This value is immutable. It must also be unique with respect
        to all other non-DELETED snapshots on the associated file
        system.

        Avoid entering confidential information.

        Example: `Sunday`


        :param name: The name of this CreateSnapshotDetails.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
