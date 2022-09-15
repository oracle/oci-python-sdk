# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_source import BuildSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DevopsCodeRepositoryBuildSource(BuildSource):
    """
    DevOps code repository build source for Build stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DevopsCodeRepositoryBuildSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.DevopsCodeRepositoryBuildSource.connection_type` attribute
        of this class is ``DEVOPS_CODE_REPOSITORY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DevopsCodeRepositoryBuildSource.
        :type name: str

        :param connection_type:
            The value to assign to the connection_type property of this DevopsCodeRepositoryBuildSource.
            Allowed values for this property are: "GITHUB", "GITLAB", "GITLAB_SERVER", "BITBUCKET_CLOUD", "BITBUCKET_SERVER", "DEVOPS_CODE_REPOSITORY", "VBS"
        :type connection_type: str

        :param repository_url:
            The value to assign to the repository_url property of this DevopsCodeRepositoryBuildSource.
        :type repository_url: str

        :param branch:
            The value to assign to the branch property of this DevopsCodeRepositoryBuildSource.
        :type branch: str

        :param repository_id:
            The value to assign to the repository_id property of this DevopsCodeRepositoryBuildSource.
        :type repository_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'connection_type': 'str',
            'repository_url': 'str',
            'branch': 'str',
            'repository_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'connection_type': 'connectionType',
            'repository_url': 'repositoryUrl',
            'branch': 'branch',
            'repository_id': 'repositoryId'
        }

        self._name = None
        self._connection_type = None
        self._repository_url = None
        self._branch = None
        self._repository_id = None
        self._connection_type = 'DEVOPS_CODE_REPOSITORY'

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this DevopsCodeRepositoryBuildSource.
        The DevOps code repository ID.


        :return: The repository_id of this DevopsCodeRepositoryBuildSource.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this DevopsCodeRepositoryBuildSource.
        The DevOps code repository ID.


        :param repository_id: The repository_id of this DevopsCodeRepositoryBuildSource.
        :type: str
        """
        self._repository_id = repository_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
