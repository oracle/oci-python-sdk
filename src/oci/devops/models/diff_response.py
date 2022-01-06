# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DiffResponse(object):
    """
    Response object for obtaining list of changed files.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DiffResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param are_all_changes_included:
            The value to assign to the are_all_changes_included property of this DiffResponse.
        :type are_all_changes_included: bool

        :param change_type_count:
            The value to assign to the change_type_count property of this DiffResponse.
        :type change_type_count: dict(str, int)

        :param common_commit:
            The value to assign to the common_commit property of this DiffResponse.
        :type common_commit: str

        :param commits_ahead_count:
            The value to assign to the commits_ahead_count property of this DiffResponse.
        :type commits_ahead_count: int

        :param commits_behind_count:
            The value to assign to the commits_behind_count property of this DiffResponse.
        :type commits_behind_count: int

        :param added_lines_count:
            The value to assign to the added_lines_count property of this DiffResponse.
        :type added_lines_count: int

        :param deleted_lines_count:
            The value to assign to the deleted_lines_count property of this DiffResponse.
        :type deleted_lines_count: int

        :param changes:
            The value to assign to the changes property of this DiffResponse.
        :type changes: list[oci.devops.models.DiffResponseEntry]

        """
        self.swagger_types = {
            'are_all_changes_included': 'bool',
            'change_type_count': 'dict(str, int)',
            'common_commit': 'str',
            'commits_ahead_count': 'int',
            'commits_behind_count': 'int',
            'added_lines_count': 'int',
            'deleted_lines_count': 'int',
            'changes': 'list[DiffResponseEntry]'
        }

        self.attribute_map = {
            'are_all_changes_included': 'areAllChangesIncluded',
            'change_type_count': 'changeTypeCount',
            'common_commit': 'commonCommit',
            'commits_ahead_count': 'commitsAheadCount',
            'commits_behind_count': 'commitsBehindCount',
            'added_lines_count': 'addedLinesCount',
            'deleted_lines_count': 'deletedLinesCount',
            'changes': 'changes'
        }

        self._are_all_changes_included = None
        self._change_type_count = None
        self._common_commit = None
        self._commits_ahead_count = None
        self._commits_behind_count = None
        self._added_lines_count = None
        self._deleted_lines_count = None
        self._changes = None

    @property
    def are_all_changes_included(self):
        """
        Gets the are_all_changes_included of this DiffResponse.
        Boolean value to indicate if all changes are included in the response.


        :return: The are_all_changes_included of this DiffResponse.
        :rtype: bool
        """
        return self._are_all_changes_included

    @are_all_changes_included.setter
    def are_all_changes_included(self, are_all_changes_included):
        """
        Sets the are_all_changes_included of this DiffResponse.
        Boolean value to indicate if all changes are included in the response.


        :param are_all_changes_included: The are_all_changes_included of this DiffResponse.
        :type: bool
        """
        self._are_all_changes_included = are_all_changes_included

    @property
    def change_type_count(self):
        """
        Gets the change_type_count of this DiffResponse.
        Count of each type of change in difference.


        :return: The change_type_count of this DiffResponse.
        :rtype: dict(str, int)
        """
        return self._change_type_count

    @change_type_count.setter
    def change_type_count(self, change_type_count):
        """
        Sets the change_type_count of this DiffResponse.
        Count of each type of change in difference.


        :param change_type_count: The change_type_count of this DiffResponse.
        :type: dict(str, int)
        """
        self._change_type_count = change_type_count

    @property
    def common_commit(self):
        """
        Gets the common_commit of this DiffResponse.
        The ID of the common commit between source and target.


        :return: The common_commit of this DiffResponse.
        :rtype: str
        """
        return self._common_commit

    @common_commit.setter
    def common_commit(self, common_commit):
        """
        Sets the common_commit of this DiffResponse.
        The ID of the common commit between source and target.


        :param common_commit: The common_commit of this DiffResponse.
        :type: str
        """
        self._common_commit = common_commit

    @property
    def commits_ahead_count(self):
        """
        Gets the commits_ahead_count of this DiffResponse.
        The number of commits source is ahead of target by.


        :return: The commits_ahead_count of this DiffResponse.
        :rtype: int
        """
        return self._commits_ahead_count

    @commits_ahead_count.setter
    def commits_ahead_count(self, commits_ahead_count):
        """
        Sets the commits_ahead_count of this DiffResponse.
        The number of commits source is ahead of target by.


        :param commits_ahead_count: The commits_ahead_count of this DiffResponse.
        :type: int
        """
        self._commits_ahead_count = commits_ahead_count

    @property
    def commits_behind_count(self):
        """
        Gets the commits_behind_count of this DiffResponse.
        The number of commits source is behind target by.


        :return: The commits_behind_count of this DiffResponse.
        :rtype: int
        """
        return self._commits_behind_count

    @commits_behind_count.setter
    def commits_behind_count(self, commits_behind_count):
        """
        Sets the commits_behind_count of this DiffResponse.
        The number of commits source is behind target by.


        :param commits_behind_count: The commits_behind_count of this DiffResponse.
        :type: int
        """
        self._commits_behind_count = commits_behind_count

    @property
    def added_lines_count(self):
        """
        Gets the added_lines_count of this DiffResponse.
        The number of lines added in whole difference.


        :return: The added_lines_count of this DiffResponse.
        :rtype: int
        """
        return self._added_lines_count

    @added_lines_count.setter
    def added_lines_count(self, added_lines_count):
        """
        Sets the added_lines_count of this DiffResponse.
        The number of lines added in whole difference.


        :param added_lines_count: The added_lines_count of this DiffResponse.
        :type: int
        """
        self._added_lines_count = added_lines_count

    @property
    def deleted_lines_count(self):
        """
        Gets the deleted_lines_count of this DiffResponse.
        The number of lines deleted in whole difference.


        :return: The deleted_lines_count of this DiffResponse.
        :rtype: int
        """
        return self._deleted_lines_count

    @deleted_lines_count.setter
    def deleted_lines_count(self, deleted_lines_count):
        """
        Sets the deleted_lines_count of this DiffResponse.
        The number of lines deleted in whole difference.


        :param deleted_lines_count: The deleted_lines_count of this DiffResponse.
        :type: int
        """
        self._deleted_lines_count = deleted_lines_count

    @property
    def changes(self):
        """
        **[Required]** Gets the changes of this DiffResponse.
        List of changes in the difference.


        :return: The changes of this DiffResponse.
        :rtype: list[oci.devops.models.DiffResponseEntry]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """
        Sets the changes of this DiffResponse.
        List of changes in the difference.


        :param changes: The changes of this DiffResponse.
        :type: list[oci.devops.models.DiffResponseEntry]
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
