# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CommitInfo(object):
    """
    Commit details that need to be used for the build run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CommitInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param repository_url:
            The value to assign to the repository_url property of this CommitInfo.
        :type repository_url: str

        :param repository_branch:
            The value to assign to the repository_branch property of this CommitInfo.
        :type repository_branch: str

        :param commit_hash:
            The value to assign to the commit_hash property of this CommitInfo.
        :type commit_hash: str

        """
        self.swagger_types = {
            'repository_url': 'str',
            'repository_branch': 'str',
            'commit_hash': 'str'
        }

        self.attribute_map = {
            'repository_url': 'repositoryUrl',
            'repository_branch': 'repositoryBranch',
            'commit_hash': 'commitHash'
        }

        self._repository_url = None
        self._repository_branch = None
        self._commit_hash = None

    @property
    def repository_url(self):
        """
        **[Required]** Gets the repository_url of this CommitInfo.
        Repository URL.


        :return: The repository_url of this CommitInfo.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this CommitInfo.
        Repository URL.


        :param repository_url: The repository_url of this CommitInfo.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def repository_branch(self):
        """
        **[Required]** Gets the repository_branch of this CommitInfo.
        Name of the repository branch.


        :return: The repository_branch of this CommitInfo.
        :rtype: str
        """
        return self._repository_branch

    @repository_branch.setter
    def repository_branch(self, repository_branch):
        """
        Sets the repository_branch of this CommitInfo.
        Name of the repository branch.


        :param repository_branch: The repository_branch of this CommitInfo.
        :type: str
        """
        self._repository_branch = repository_branch

    @property
    def commit_hash(self):
        """
        **[Required]** Gets the commit_hash of this CommitInfo.
        Commit hash pertinent to the repository URL and the specified branch.


        :return: The commit_hash of this CommitInfo.
        :rtype: str
        """
        return self._commit_hash

    @commit_hash.setter
    def commit_hash(self, commit_hash):
        """
        Sets the commit_hash of this CommitInfo.
        Commit hash pertinent to the repository URL and the specified branch.


        :param commit_hash: The commit_hash of this CommitInfo.
        :type: str
        """
        self._commit_hash = commit_hash

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
