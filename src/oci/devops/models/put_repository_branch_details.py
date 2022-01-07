# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .put_repository_ref_details import PutRepositoryRefDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PutRepositoryBranchDetails(PutRepositoryRefDetails):
    """
    The information needed to create a branch.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PutRepositoryBranchDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.PutRepositoryBranchDetails.ref_type` attribute
        of this class is ``BRANCH`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ref_type:
            The value to assign to the ref_type property of this PutRepositoryBranchDetails.
            Allowed values for this property are: "BRANCH", "TAG"
        :type ref_type: str

        :param commit_id:
            The value to assign to the commit_id property of this PutRepositoryBranchDetails.
        :type commit_id: str

        """
        self.swagger_types = {
            'ref_type': 'str',
            'commit_id': 'str'
        }

        self.attribute_map = {
            'ref_type': 'refType',
            'commit_id': 'commitId'
        }

        self._ref_type = None
        self._commit_id = None
        self._ref_type = 'BRANCH'

    @property
    def commit_id(self):
        """
        **[Required]** Gets the commit_id of this PutRepositoryBranchDetails.
        Commit ID pointed to by the new branch.


        :return: The commit_id of this PutRepositoryBranchDetails.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this PutRepositoryBranchDetails.
        Commit ID pointed to by the new branch.


        :param commit_id: The commit_id of this PutRepositoryBranchDetails.
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
