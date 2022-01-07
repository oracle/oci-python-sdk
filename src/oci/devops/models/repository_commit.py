# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryCommit(object):
    """
    Commit object with commit information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryCommit object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param commit_id:
            The value to assign to the commit_id property of this RepositoryCommit.
        :type commit_id: str

        :param commit_message:
            The value to assign to the commit_message property of this RepositoryCommit.
        :type commit_message: str

        :param author_name:
            The value to assign to the author_name property of this RepositoryCommit.
        :type author_name: str

        :param author_email:
            The value to assign to the author_email property of this RepositoryCommit.
        :type author_email: str

        :param committer_name:
            The value to assign to the committer_name property of this RepositoryCommit.
        :type committer_name: str

        :param committer_email:
            The value to assign to the committer_email property of this RepositoryCommit.
        :type committer_email: str

        :param parent_commit_ids:
            The value to assign to the parent_commit_ids property of this RepositoryCommit.
        :type parent_commit_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this RepositoryCommit.
        :type time_created: datetime

        :param tree_id:
            The value to assign to the tree_id property of this RepositoryCommit.
        :type tree_id: str

        """
        self.swagger_types = {
            'commit_id': 'str',
            'commit_message': 'str',
            'author_name': 'str',
            'author_email': 'str',
            'committer_name': 'str',
            'committer_email': 'str',
            'parent_commit_ids': 'list[str]',
            'time_created': 'datetime',
            'tree_id': 'str'
        }

        self.attribute_map = {
            'commit_id': 'commitId',
            'commit_message': 'commitMessage',
            'author_name': 'authorName',
            'author_email': 'authorEmail',
            'committer_name': 'committerName',
            'committer_email': 'committerEmail',
            'parent_commit_ids': 'parentCommitIds',
            'time_created': 'timeCreated',
            'tree_id': 'treeId'
        }

        self._commit_id = None
        self._commit_message = None
        self._author_name = None
        self._author_email = None
        self._committer_name = None
        self._committer_email = None
        self._parent_commit_ids = None
        self._time_created = None
        self._tree_id = None

    @property
    def commit_id(self):
        """
        **[Required]** Gets the commit_id of this RepositoryCommit.
        Commit hash pointed to by reference name.


        :return: The commit_id of this RepositoryCommit.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this RepositoryCommit.
        Commit hash pointed to by reference name.


        :param commit_id: The commit_id of this RepositoryCommit.
        :type: str
        """
        self._commit_id = commit_id

    @property
    def commit_message(self):
        """
        **[Required]** Gets the commit_message of this RepositoryCommit.
        The commit message.


        :return: The commit_message of this RepositoryCommit.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """
        Sets the commit_message of this RepositoryCommit.
        The commit message.


        :param commit_message: The commit_message of this RepositoryCommit.
        :type: str
        """
        self._commit_message = commit_message

    @property
    def author_name(self):
        """
        Gets the author_name of this RepositoryCommit.
        Name of the author of the repository.


        :return: The author_name of this RepositoryCommit.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """
        Sets the author_name of this RepositoryCommit.
        Name of the author of the repository.


        :param author_name: The author_name of this RepositoryCommit.
        :type: str
        """
        self._author_name = author_name

    @property
    def author_email(self):
        """
        Gets the author_email of this RepositoryCommit.
        Email of the author of the repository.


        :return: The author_email of this RepositoryCommit.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """
        Sets the author_email of this RepositoryCommit.
        Email of the author of the repository.


        :param author_email: The author_email of this RepositoryCommit.
        :type: str
        """
        self._author_email = author_email

    @property
    def committer_name(self):
        """
        Gets the committer_name of this RepositoryCommit.
        Name of who creates the commit.


        :return: The committer_name of this RepositoryCommit.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        """
        Sets the committer_name of this RepositoryCommit.
        Name of who creates the commit.


        :param committer_name: The committer_name of this RepositoryCommit.
        :type: str
        """
        self._committer_name = committer_name

    @property
    def committer_email(self):
        """
        Gets the committer_email of this RepositoryCommit.
        Email of who creates the commit.


        :return: The committer_email of this RepositoryCommit.
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        """
        Sets the committer_email of this RepositoryCommit.
        Email of who creates the commit.


        :param committer_email: The committer_email of this RepositoryCommit.
        :type: str
        """
        self._committer_email = committer_email

    @property
    def parent_commit_ids(self):
        """
        Gets the parent_commit_ids of this RepositoryCommit.
        An array of parent commit IDs of created commit.


        :return: The parent_commit_ids of this RepositoryCommit.
        :rtype: list[str]
        """
        return self._parent_commit_ids

    @parent_commit_ids.setter
    def parent_commit_ids(self, parent_commit_ids):
        """
        Sets the parent_commit_ids of this RepositoryCommit.
        An array of parent commit IDs of created commit.


        :param parent_commit_ids: The parent_commit_ids of this RepositoryCommit.
        :type: list[str]
        """
        self._parent_commit_ids = parent_commit_ids

    @property
    def time_created(self):
        """
        Gets the time_created of this RepositoryCommit.
        The time at which commit was created.


        :return: The time_created of this RepositoryCommit.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RepositoryCommit.
        The time at which commit was created.


        :param time_created: The time_created of this RepositoryCommit.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def tree_id(self):
        """
        Gets the tree_id of this RepositoryCommit.
        Tree information for the specified commit.


        :return: The tree_id of this RepositoryCommit.
        :rtype: str
        """
        return self._tree_id

    @tree_id.setter
    def tree_id(self, tree_id):
        """
        Sets the tree_id of this RepositoryCommit.
        Tree information for the specified commit.


        :param tree_id: The tree_id of this RepositoryCommit.
        :type: str
        """
        self._tree_id = tree_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
