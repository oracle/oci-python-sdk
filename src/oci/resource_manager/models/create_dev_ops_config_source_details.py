# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_config_source_details import CreateConfigSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDevOpsConfigSourceDetails(CreateConfigSourceDetails):
    """
    Creation details for a `DevOps`__ configuration source.

    __ https://docs.cloud.oracle.com/iaas/Content/devops/using/home.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDevOpsConfigSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateDevOpsConfigSourceDetails.config_source_type` attribute
        of this class is ``DEVOPS_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this CreateDevOpsConfigSourceDetails.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this CreateDevOpsConfigSourceDetails.
        :type working_directory: str

        :param project_id:
            The value to assign to the project_id property of this CreateDevOpsConfigSourceDetails.
        :type project_id: str

        :param repository_id:
            The value to assign to the repository_id property of this CreateDevOpsConfigSourceDetails.
        :type repository_id: str

        :param branch_name:
            The value to assign to the branch_name property of this CreateDevOpsConfigSourceDetails.
        :type branch_name: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str',
            'project_id': 'str',
            'repository_id': 'str',
            'branch_name': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory',
            'project_id': 'projectId',
            'repository_id': 'repositoryId',
            'branch_name': 'branchName'
        }

        self._config_source_type = None
        self._working_directory = None
        self._project_id = None
        self._repository_id = None
        self._branch_name = None
        self._config_source_type = 'DEVOPS_CONFIG_SOURCE'

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this CreateDevOpsConfigSourceDetails.
        The `OCID`__ of the :class:`Project`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The project_id of this CreateDevOpsConfigSourceDetails.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this CreateDevOpsConfigSourceDetails.
        The `OCID`__ of the :class:`Project`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param project_id: The project_id of this CreateDevOpsConfigSourceDetails.
        :type: str
        """
        self._project_id = project_id

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this CreateDevOpsConfigSourceDetails.
        The `OCID`__ of the :class:`Repository`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The repository_id of this CreateDevOpsConfigSourceDetails.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this CreateDevOpsConfigSourceDetails.
        The `OCID`__ of the :class:`Repository`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param repository_id: The repository_id of this CreateDevOpsConfigSourceDetails.
        :type: str
        """
        self._repository_id = repository_id

    @property
    def branch_name(self):
        """
        Gets the branch_name of this CreateDevOpsConfigSourceDetails.
        The name of the branch that contains the Terraform configuration.


        :return: The branch_name of this CreateDevOpsConfigSourceDetails.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        """
        Sets the branch_name of this CreateDevOpsConfigSourceDetails.
        The name of the branch that contains the Terraform configuration.


        :param branch_name: The branch_name of this CreateDevOpsConfigSourceDetails.
        :type: str
        """
        self._branch_name = branch_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
