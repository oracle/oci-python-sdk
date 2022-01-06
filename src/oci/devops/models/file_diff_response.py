# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FileDiffResponse(object):
    """
    Response object for showing differences for a file between two commits.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FileDiffResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param old_path:
            The value to assign to the old_path property of this FileDiffResponse.
        :type old_path: str

        :param new_path:
            The value to assign to the new_path property of this FileDiffResponse.
        :type new_path: str

        :param old_id:
            The value to assign to the old_id property of this FileDiffResponse.
        :type old_id: str

        :param new_id:
            The value to assign to the new_id property of this FileDiffResponse.
        :type new_id: str

        :param are_conflicts_in_file:
            The value to assign to the are_conflicts_in_file property of this FileDiffResponse.
        :type are_conflicts_in_file: bool

        :param is_large:
            The value to assign to the is_large property of this FileDiffResponse.
        :type is_large: bool

        :param is_binary:
            The value to assign to the is_binary property of this FileDiffResponse.
        :type is_binary: bool

        :param changes:
            The value to assign to the changes property of this FileDiffResponse.
        :type changes: list[oci.devops.models.DiffChunk]

        """
        self.swagger_types = {
            'old_path': 'str',
            'new_path': 'str',
            'old_id': 'str',
            'new_id': 'str',
            'are_conflicts_in_file': 'bool',
            'is_large': 'bool',
            'is_binary': 'bool',
            'changes': 'list[DiffChunk]'
        }

        self.attribute_map = {
            'old_path': 'oldPath',
            'new_path': 'newPath',
            'old_id': 'oldId',
            'new_id': 'newId',
            'are_conflicts_in_file': 'areConflictsInFile',
            'is_large': 'isLarge',
            'is_binary': 'isBinary',
            'changes': 'changes'
        }

        self._old_path = None
        self._new_path = None
        self._old_id = None
        self._new_id = None
        self._are_conflicts_in_file = None
        self._is_large = None
        self._is_binary = None
        self._changes = None

    @property
    def old_path(self):
        """
        Gets the old_path of this FileDiffResponse.
        The path on the base version to the changed object.


        :return: The old_path of this FileDiffResponse.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        """
        Sets the old_path of this FileDiffResponse.
        The path on the base version to the changed object.


        :param old_path: The old_path of this FileDiffResponse.
        :type: str
        """
        self._old_path = old_path

    @property
    def new_path(self):
        """
        Gets the new_path of this FileDiffResponse.
        The path on the target version to the changed object.


        :return: The new_path of this FileDiffResponse.
        :rtype: str
        """
        return self._new_path

    @new_path.setter
    def new_path(self, new_path):
        """
        Sets the new_path of this FileDiffResponse.
        The path on the target version to the changed object.


        :param new_path: The new_path of this FileDiffResponse.
        :type: str
        """
        self._new_path = new_path

    @property
    def old_id(self):
        """
        Gets the old_id of this FileDiffResponse.
        The ID of the changed object on the base version.


        :return: The old_id of this FileDiffResponse.
        :rtype: str
        """
        return self._old_id

    @old_id.setter
    def old_id(self, old_id):
        """
        Sets the old_id of this FileDiffResponse.
        The ID of the changed object on the base version.


        :param old_id: The old_id of this FileDiffResponse.
        :type: str
        """
        self._old_id = old_id

    @property
    def new_id(self):
        """
        Gets the new_id of this FileDiffResponse.
        The ID of the changed object on the target version.


        :return: The new_id of this FileDiffResponse.
        :rtype: str
        """
        return self._new_id

    @new_id.setter
    def new_id(self, new_id):
        """
        Sets the new_id of this FileDiffResponse.
        The ID of the changed object on the target version.


        :param new_id: The new_id of this FileDiffResponse.
        :type: str
        """
        self._new_id = new_id

    @property
    def are_conflicts_in_file(self):
        """
        Gets the are_conflicts_in_file of this FileDiffResponse.
        Indicates whether the changed file contains conflicts.


        :return: The are_conflicts_in_file of this FileDiffResponse.
        :rtype: bool
        """
        return self._are_conflicts_in_file

    @are_conflicts_in_file.setter
    def are_conflicts_in_file(self, are_conflicts_in_file):
        """
        Sets the are_conflicts_in_file of this FileDiffResponse.
        Indicates whether the changed file contains conflicts.


        :param are_conflicts_in_file: The are_conflicts_in_file of this FileDiffResponse.
        :type: bool
        """
        self._are_conflicts_in_file = are_conflicts_in_file

    @property
    def is_large(self):
        """
        Gets the is_large of this FileDiffResponse.
        Indicates whether the file is large.


        :return: The is_large of this FileDiffResponse.
        :rtype: bool
        """
        return self._is_large

    @is_large.setter
    def is_large(self, is_large):
        """
        Sets the is_large of this FileDiffResponse.
        Indicates whether the file is large.


        :param is_large: The is_large of this FileDiffResponse.
        :type: bool
        """
        self._is_large = is_large

    @property
    def is_binary(self):
        """
        Gets the is_binary of this FileDiffResponse.
        Indicates whether the file is binary.


        :return: The is_binary of this FileDiffResponse.
        :rtype: bool
        """
        return self._is_binary

    @is_binary.setter
    def is_binary(self, is_binary):
        """
        Sets the is_binary of this FileDiffResponse.
        Indicates whether the file is binary.


        :param is_binary: The is_binary of this FileDiffResponse.
        :type: bool
        """
        self._is_binary = is_binary

    @property
    def changes(self):
        """
        **[Required]** Gets the changes of this FileDiffResponse.
        List of changed section in the file.


        :return: The changes of this FileDiffResponse.
        :rtype: list[oci.devops.models.DiffChunk]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """
        Sets the changes of this FileDiffResponse.
        List of changed section in the file.


        :param changes: The changes of this FileDiffResponse.
        :type: list[oci.devops.models.DiffChunk]
        """
        self._changes = changes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
