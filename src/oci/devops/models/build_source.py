# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BuildSource(object):
    """
    Build source required for the Build stage.
    """

    #: A constant which can be used with the connection_type property of a BuildSource.
    #: This constant has a value of "GITHUB"
    CONNECTION_TYPE_GITHUB = "GITHUB"

    #: A constant which can be used with the connection_type property of a BuildSource.
    #: This constant has a value of "GITLAB"
    CONNECTION_TYPE_GITLAB = "GITLAB"

    #: A constant which can be used with the connection_type property of a BuildSource.
    #: This constant has a value of "GITLAB_SERVER"
    CONNECTION_TYPE_GITLAB_SERVER = "GITLAB_SERVER"

    #: A constant which can be used with the connection_type property of a BuildSource.
    #: This constant has a value of "BITBUCKET_CLOUD"
    CONNECTION_TYPE_BITBUCKET_CLOUD = "BITBUCKET_CLOUD"

    #: A constant which can be used with the connection_type property of a BuildSource.
    #: This constant has a value of "BITBUCKET_SERVER"
    CONNECTION_TYPE_BITBUCKET_SERVER = "BITBUCKET_SERVER"

    #: A constant which can be used with the connection_type property of a BuildSource.
    #: This constant has a value of "DEVOPS_CODE_REPOSITORY"
    CONNECTION_TYPE_DEVOPS_CODE_REPOSITORY = "DEVOPS_CODE_REPOSITORY"

    #: A constant which can be used with the connection_type property of a BuildSource.
    #: This constant has a value of "VBS"
    CONNECTION_TYPE_VBS = "VBS"

    def __init__(self, **kwargs):
        """
        Initializes a new BuildSource object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.devops.models.VbsBuildSource`
        * :class:`~oci.devops.models.BitbucketServerBuildSource`
        * :class:`~oci.devops.models.GithubBuildSource`
        * :class:`~oci.devops.models.BitbucketCloudBuildSource`
        * :class:`~oci.devops.models.GitlabServerBuildSource`
        * :class:`~oci.devops.models.DevopsCodeRepositoryBuildSource`
        * :class:`~oci.devops.models.GitlabBuildSource`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this BuildSource.
        :type name: str

        :param connection_type:
            The value to assign to the connection_type property of this BuildSource.
            Allowed values for this property are: "GITHUB", "GITLAB", "GITLAB_SERVER", "BITBUCKET_CLOUD", "BITBUCKET_SERVER", "DEVOPS_CODE_REPOSITORY", "VBS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param repository_url:
            The value to assign to the repository_url property of this BuildSource.
        :type repository_url: str

        :param branch:
            The value to assign to the branch property of this BuildSource.
        :type branch: str

        """
        self.swagger_types = {
            'name': 'str',
            'connection_type': 'str',
            'repository_url': 'str',
            'branch': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'connection_type': 'connectionType',
            'repository_url': 'repositoryUrl',
            'branch': 'branch'
        }

        self._name = None
        self._connection_type = None
        self._repository_url = None
        self._branch = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'VBS':
            return 'VbsBuildSource'

        if type == 'BITBUCKET_SERVER':
            return 'BitbucketServerBuildSource'

        if type == 'GITHUB':
            return 'GithubBuildSource'

        if type == 'BITBUCKET_CLOUD':
            return 'BitbucketCloudBuildSource'

        if type == 'GITLAB_SERVER':
            return 'GitlabServerBuildSource'

        if type == 'DEVOPS_CODE_REPOSITORY':
            return 'DevopsCodeRepositoryBuildSource'

        if type == 'GITLAB':
            return 'GitlabBuildSource'
        else:
            return 'BuildSource'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this BuildSource.
        Name of the build source. This must be unique within a build source collection. The name can be used by customers to locate the working directory pertinent to this repository.


        :return: The name of this BuildSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildSource.
        Name of the build source. This must be unique within a build source collection. The name can be used by customers to locate the working directory pertinent to this repository.


        :param name: The name of this BuildSource.
        :type: str
        """
        self._name = name

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this BuildSource.
        The type of source provider.

        Allowed values for this property are: "GITHUB", "GITLAB", "GITLAB_SERVER", "BITBUCKET_CLOUD", "BITBUCKET_SERVER", "DEVOPS_CODE_REPOSITORY", "VBS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_type of this BuildSource.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this BuildSource.
        The type of source provider.


        :param connection_type: The connection_type of this BuildSource.
        :type: str
        """
        allowed_values = ["GITHUB", "GITLAB", "GITLAB_SERVER", "BITBUCKET_CLOUD", "BITBUCKET_SERVER", "DEVOPS_CODE_REPOSITORY", "VBS"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            connection_type = 'UNKNOWN_ENUM_VALUE'
        self._connection_type = connection_type

    @property
    def repository_url(self):
        """
        **[Required]** Gets the repository_url of this BuildSource.
        URL for the repository.


        :return: The repository_url of this BuildSource.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this BuildSource.
        URL for the repository.


        :param repository_url: The repository_url of this BuildSource.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def branch(self):
        """
        **[Required]** Gets the branch of this BuildSource.
        Branch name.


        :return: The branch of this BuildSource.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """
        Sets the branch of this BuildSource.
        Branch name.


        :param branch: The branch of this BuildSource.
        :type: str
        """
        self._branch = branch

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
