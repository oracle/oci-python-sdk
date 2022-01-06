# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config_source_record import ConfigSourceRecord
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GitConfigSourceRecord(ConfigSourceRecord):
    """
    Metadata about the Git configuration source.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GitConfigSourceRecord object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.GitConfigSourceRecord.config_source_record_type` attribute
        of this class is ``GIT_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_record_type:
            The value to assign to the config_source_record_type property of this GitConfigSourceRecord.
            Allowed values for this property are: "ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE"
        :type config_source_record_type: str

        :param configuration_source_provider_id:
            The value to assign to the configuration_source_provider_id property of this GitConfigSourceRecord.
        :type configuration_source_provider_id: str

        :param repository_url:
            The value to assign to the repository_url property of this GitConfigSourceRecord.
        :type repository_url: str

        :param branch_name:
            The value to assign to the branch_name property of this GitConfigSourceRecord.
        :type branch_name: str

        :param commit_id:
            The value to assign to the commit_id property of this GitConfigSourceRecord.
        :type commit_id: str

        """
        self.swagger_types = {
            'config_source_record_type': 'str',
            'configuration_source_provider_id': 'str',
            'repository_url': 'str',
            'branch_name': 'str',
            'commit_id': 'str'
        }

        self.attribute_map = {
            'config_source_record_type': 'configSourceRecordType',
            'configuration_source_provider_id': 'configurationSourceProviderId',
            'repository_url': 'repositoryUrl',
            'branch_name': 'branchName',
            'commit_id': 'commitId'
        }

        self._config_source_record_type = None
        self._configuration_source_provider_id = None
        self._repository_url = None
        self._branch_name = None
        self._commit_id = None
        self._config_source_record_type = 'GIT_CONFIG_SOURCE'

    @property
    def configuration_source_provider_id(self):
        """
        **[Required]** Gets the configuration_source_provider_id of this GitConfigSourceRecord.
        Unique identifier (`OCID`__)
        for the Git configuration source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The configuration_source_provider_id of this GitConfigSourceRecord.
        :rtype: str
        """
        return self._configuration_source_provider_id

    @configuration_source_provider_id.setter
    def configuration_source_provider_id(self, configuration_source_provider_id):
        """
        Sets the configuration_source_provider_id of this GitConfigSourceRecord.
        Unique identifier (`OCID`__)
        for the Git configuration source.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param configuration_source_provider_id: The configuration_source_provider_id of this GitConfigSourceRecord.
        :type: str
        """
        self._configuration_source_provider_id = configuration_source_provider_id

    @property
    def repository_url(self):
        """
        Gets the repository_url of this GitConfigSourceRecord.
        The URL of the Git repository.


        :return: The repository_url of this GitConfigSourceRecord.
        :rtype: str
        """
        return self._repository_url

    @repository_url.setter
    def repository_url(self, repository_url):
        """
        Sets the repository_url of this GitConfigSourceRecord.
        The URL of the Git repository.


        :param repository_url: The repository_url of this GitConfigSourceRecord.
        :type: str
        """
        self._repository_url = repository_url

    @property
    def branch_name(self):
        """
        Gets the branch_name of this GitConfigSourceRecord.
        The name of the branch within the Git repository.


        :return: The branch_name of this GitConfigSourceRecord.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """
        Sets the branch_name of this GitConfigSourceRecord.
        The name of the branch within the Git repository.


        :param branch_name: The branch_name of this GitConfigSourceRecord.
        :type: str
        """
        self._branch_name = branch_name

    @property
    def commit_id(self):
        """
        Gets the commit_id of this GitConfigSourceRecord.
        The unique identifier (SHA-1 hash) of the individual change to the Git repository.


        :return: The commit_id of this GitConfigSourceRecord.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """
        Sets the commit_id of this GitConfigSourceRecord.
        The unique identifier (SHA-1 hash) of the individual change to the Git repository.


        :param commit_id: The commit_id of this GitConfigSourceRecord.
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
