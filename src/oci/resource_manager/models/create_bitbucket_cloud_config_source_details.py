# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_config_source_details import CreateConfigSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBitbucketCloudConfigSourceDetails(CreateConfigSourceDetails):
    """
    Creation details for a Bitbucket Cloud configuration source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBitbucketCloudConfigSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateBitbucketCloudConfigSourceDetails.config_source_type` attribute
        of this class is ``BITBUCKET_CLOUD_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this CreateBitbucketCloudConfigSourceDetails.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this CreateBitbucketCloudConfigSourceDetails.
        :type working_directory: str

        :param configuration_source_provider_id:
            The value to assign to the configuration_source_provider_id property of this CreateBitbucketCloudConfigSourceDetails.
        :type configuration_source_provider_id: str

        :param repository_url:
            The value to assign to the repository_url property of this CreateBitbucketCloudConfigSourceDetails.
        :type repository_url: str

        :param branch_name:
            The value to assign to the branch_name property of this CreateBitbucketCloudConfigSourceDetails.
        :type branch_name: str

        :param workspace_id:
            The value to assign to the workspace_id property of this CreateBitbucketCloudConfigSourceDetails.
        :type workspace_id: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str',
            'configuration_source_provider_id': 'str',
            'repository_url': 'str',
            'branch_name': 'str',
            'workspace_id': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory',
            'configuration_source_provider_id': 'configurationSourceProviderId',
            'repository_url': 'repositoryUrl',
            'branch_name': 'branchName',
            'workspace_id': 'workspaceId'
        }

        self._config_source_type = None
        self._working_directory = None
        self._configuration_source_provider_id = None
        self._repository_url = None
        self._branch_name = None
        self._workspace_id = None
        self._config_source_type = 'BITBUCKET_CLOUD_CONFIG_SOURCE'

    @property
    def configuration_source_provider_id(self):
        """
        **[Required]** Gets the configuration_source_provider_id of this CreateBitbucketCloudConfigSourceDetails.
        The `OCID`__ of the Bitbucket Cloud configuration source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The configuration_source_provider_id of this CreateBitbucketCloudConfigSourceDetails.
        :rtype: str
        """
        return self._configuration_source_provider_id

    @configuration_source_provider_id.setter
    def configuration_source_provider_id(self, configuration_source_provider_id):
        """
        Sets the configuration_source_provider_id of this CreateBitbucketCloudConfigSourceDetails.
        The `OCID`__ of the Bitbucket Cloud configuration source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param configuration_source_provider_id: The configuration_source_provider_id of this CreateBitbucketCloudConfigSourceDetails.
        :type: str
        """
        self._configuration_source_provider_id = configuration_source_provider_id

    @property
    def repository_url(self):
        """
        **[Required]** Gets the repository_url of this CreateBitbucketCloudConfigSourceDetails.
        The URL of the Bitbucket Cloud repository for the configuration source.


        :return: The repository_url of this CreateBitbucketCloudConfigSourceDetails.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this CreateBitbucketCloudConfigSourceDetails.
        The URL of the Bitbucket Cloud repository for the configuration source.


        :param repository_url: The repository_url of this CreateBitbucketCloudConfigSourceDetails.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def branch_name(self):
        """
        Gets the branch_name of this CreateBitbucketCloudConfigSourceDetails.
        The name of the branch in the Bitbucket Cloud repository for the configuration source.


        :return: The branch_name of this CreateBitbucketCloudConfigSourceDetails.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """
        Sets the branch_name of this CreateBitbucketCloudConfigSourceDetails.
        The name of the branch in the Bitbucket Cloud repository for the configuration source.


        :param branch_name: The branch_name of this CreateBitbucketCloudConfigSourceDetails.
        :type: str
        """
        self._branch_name = branch_name

    @property
    def workspace_id(self):
        """
        **[Required]** Gets the workspace_id of this CreateBitbucketCloudConfigSourceDetails.
        The id of the workspace in Bitbucket Cloud for the configuration source


        :return: The workspace_id of this CreateBitbucketCloudConfigSourceDetails.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """
        Sets the workspace_id of this CreateBitbucketCloudConfigSourceDetails.
        The id of the workspace in Bitbucket Cloud for the configuration source


        :param workspace_id: The workspace_id of this CreateBitbucketCloudConfigSourceDetails.
        :type: str
        """
        self._workspace_id = workspace_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
