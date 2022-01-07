# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_source import BuildSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GithubBuildSource(BuildSource):
    """
    GitHub build source for Build stage.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GithubBuildSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.GithubBuildSource.connection_type` attribute
        of this class is ``GITHUB`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this GithubBuildSource.
        :type name: str

        :param connection_type:
            The value to assign to the connection_type property of this GithubBuildSource.
            Allowed values for this property are: "GITHUB", "GITLAB", "DEVOPS_CODE_REPOSITORY"
        :type connection_type: str

        :param repository_url:
            The value to assign to the repository_url property of this GithubBuildSource.
        :type repository_url: str

        :param branch:
            The value to assign to the branch property of this GithubBuildSource.
        :type branch: str

        :param connection_id:
            The value to assign to the connection_id property of this GithubBuildSource.
        :type connection_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'connection_type': 'str',
            'repository_url': 'str',
            'branch': 'str',
            'connection_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'connection_type': 'connectionType',
            'repository_url': 'repositoryUrl',
            'branch': 'branch',
            'connection_id': 'connectionId'
        }

        self._name = None
        self._connection_type = None
        self._repository_url = None
        self._branch = None
        self._connection_id = None
        self._connection_type = 'GITHUB'

    @property
    def connection_id(self):
        """
        **[Required]** Gets the connection_id of this GithubBuildSource.
        Connection identifier pertinent to GitHub source provider.


        :return: The connection_id of this GithubBuildSource.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """
        Sets the connection_id of this GithubBuildSource.
        Connection identifier pertinent to GitHub source provider.


        :param connection_id: The connection_id of this GithubBuildSource.
        :type: str
        """
        self._connection_id = connection_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
