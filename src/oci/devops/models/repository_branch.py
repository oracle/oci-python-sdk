# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .repository_ref import RepositoryRef
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositoryBranch(RepositoryRef):
    """
    Branch related information.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RepositoryBranch object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.RepositoryBranch.ref_type` attribute
        of this class is ``BRANCH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ref_name:
            The value to assign to the ref_name property of this RepositoryBranch.
        :type ref_name: str

        :param ref_type:
            The value to assign to the ref_type property of this RepositoryBranch.
            Allowed values for this property are: "BRANCH", "TAG"
        :type ref_type: str

        :param full_ref_name:
            The value to assign to the full_ref_name property of this RepositoryBranch.
        :type full_ref_name: str

        :param repository_id:
            The value to assign to the repository_id property of this RepositoryBranch.
        :type repository_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RepositoryBranch.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RepositoryBranch.
        :type defined_tags: dict(str, dict(str, object))

        :param commit_id:
            The value to assign to the commit_id property of this RepositoryBranch.
        :type commit_id: str

        """
        self.swagger_types = {
            'ref_name': 'str',
            'ref_type': 'str',
            'full_ref_name': 'str',
            'repository_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'commit_id': 'str'
        }

        self.attribute_map = {
            'ref_name': 'refName',
            'ref_type': 'refType',
            'full_ref_name': 'fullRefName',
            'repository_id': 'repositoryId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'commit_id': 'commitId'
        }

        self._ref_name = None
        self._ref_type = None
        self._full_ref_name = None
        self._repository_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._commit_id = None
        self._ref_type = 'BRANCH'

    @property
    def commit_id(self):
        """
        **[Required]** Gets the commit_id of this RepositoryBranch.
        Commit ID pointed to by the new branch.


        :return: The commit_id of this RepositoryBranch.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this RepositoryBranch.
        Commit ID pointed to by the new branch.


        :param commit_id: The commit_id of this RepositoryBranch.
        :type: str
        """
        self._commit_id = commit_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
