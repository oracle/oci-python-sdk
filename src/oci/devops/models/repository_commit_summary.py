# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryCommitSummary(object):
    """
    Commit summary with commit information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryCommitSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param commit_id:
            The value to assign to the commit_id property of this RepositoryCommitSummary.
        :type commit_id: str

        :param commit_message:
            The value to assign to the commit_message property of this RepositoryCommitSummary.
        :type commit_message: str

        :param author_name:
            The value to assign to the author_name property of this RepositoryCommitSummary.
        :type author_name: str

        :param author_email:
            The value to assign to the author_email property of this RepositoryCommitSummary.
        :type author_email: str

        :param committer_name:
            The value to assign to the committer_name property of this RepositoryCommitSummary.
        :type committer_name: str

        :param committer_email:
            The value to assign to the committer_email property of this RepositoryCommitSummary.
        :type committer_email: str

        :param parent_commit_ids:
            The value to assign to the parent_commit_ids property of this RepositoryCommitSummary.
        :type parent_commit_ids: list[str]

        :param time_created:
            The value to assign to the time_created property of this RepositoryCommitSummary.
        :type time_created: datetime

        :param tree_id:
            The value to assign to the tree_id property of this RepositoryCommitSummary.
        :type tree_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RepositoryCommitSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RepositoryCommitSummary.
        :type defined_tags: dict(str, dict(str, object))

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
            'tree_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
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
            'tree_id': 'treeId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
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
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def commit_id(self):
        """
        **[Required]** Gets the commit_id of this RepositoryCommitSummary.
        Commit hash pointed to by reference name.


        :return: The commit_id of this RepositoryCommitSummary.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this RepositoryCommitSummary.
        Commit hash pointed to by reference name.


        :param commit_id: The commit_id of this RepositoryCommitSummary.
        :type: str
        """
        self._commit_id = commit_id

    @property
    def commit_message(self):
        """
        **[Required]** Gets the commit_message of this RepositoryCommitSummary.
        The commit message.


        :return: The commit_message of this RepositoryCommitSummary.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """
        Sets the commit_message of this RepositoryCommitSummary.
        The commit message.


        :param commit_message: The commit_message of this RepositoryCommitSummary.
        :type: str
        """
        self._commit_message = commit_message

    @property
    def author_name(self):
        """
        **[Required]** Gets the author_name of this RepositoryCommitSummary.
        Name of the author of the repository.


        :return: The author_name of this RepositoryCommitSummary.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """
        Sets the author_name of this RepositoryCommitSummary.
        Name of the author of the repository.


        :param author_name: The author_name of this RepositoryCommitSummary.
        :type: str
        """
        self._author_name = author_name

    @property
    def author_email(self):
        """
        **[Required]** Gets the author_email of this RepositoryCommitSummary.
        Email of the author of the repository.


        :return: The author_email of this RepositoryCommitSummary.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """
        Sets the author_email of this RepositoryCommitSummary.
        Email of the author of the repository.


        :param author_email: The author_email of this RepositoryCommitSummary.
        :type: str
        """
        self._author_email = author_email

    @property
    def committer_name(self):
        """
        **[Required]** Gets the committer_name of this RepositoryCommitSummary.
        Name of who creates the commit.


        :return: The committer_name of this RepositoryCommitSummary.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        """
        Sets the committer_name of this RepositoryCommitSummary.
        Name of who creates the commit.


        :param committer_name: The committer_name of this RepositoryCommitSummary.
        :type: str
        """
        self._committer_name = committer_name

    @property
    def committer_email(self):
        """
        **[Required]** Gets the committer_email of this RepositoryCommitSummary.
        Email of who creates the commit.


        :return: The committer_email of this RepositoryCommitSummary.
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        """
        Sets the committer_email of this RepositoryCommitSummary.
        Email of who creates the commit.


        :param committer_email: The committer_email of this RepositoryCommitSummary.
        :type: str
        """
        self._committer_email = committer_email

    @property
    def parent_commit_ids(self):
        """
        **[Required]** Gets the parent_commit_ids of this RepositoryCommitSummary.
        An array of parent commit IDs of created commit.


        :return: The parent_commit_ids of this RepositoryCommitSummary.
        :rtype: list[str]
        """
        return self._parent_commit_ids

    @parent_commit_ids.setter
    def parent_commit_ids(self, parent_commit_ids):
        """
        Sets the parent_commit_ids of this RepositoryCommitSummary.
        An array of parent commit IDs of created commit.


        :param parent_commit_ids: The parent_commit_ids of this RepositoryCommitSummary.
        :type: list[str]
        """
        self._parent_commit_ids = parent_commit_ids

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this RepositoryCommitSummary.
        The time to create the commit.


        :return: The time_created of this RepositoryCommitSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RepositoryCommitSummary.
        The time to create the commit.


        :param time_created: The time_created of this RepositoryCommitSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def tree_id(self):
        """
        **[Required]** Gets the tree_id of this RepositoryCommitSummary.
        Tree information for the specified commit.


        :return: The tree_id of this RepositoryCommitSummary.
        :rtype: str
        """
        return self._tree_id

    @tree_id.setter
    def tree_id(self, tree_id):
        """
        Sets the tree_id of this RepositoryCommitSummary.
        Tree information for the specified commit.


        :param tree_id: The tree_id of this RepositoryCommitSummary.
        :type: str
        """
        self._tree_id = tree_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RepositoryCommitSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RepositoryCommitSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RepositoryCommitSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RepositoryCommitSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RepositoryCommitSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RepositoryCommitSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RepositoryCommitSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RepositoryCommitSummary.
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
