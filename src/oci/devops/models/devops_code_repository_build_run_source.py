# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .build_run_source import BuildRunSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DevopsCodeRepositoryBuildRunSource(BuildRunSource):
    """
    Specifies details of build run through DevOps code repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DevopsCodeRepositoryBuildRunSource object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.DevopsCodeRepositoryBuildRunSource.source_type` attribute
        of this class is ``DEVOPS_CODE_REPOSITORY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this DevopsCodeRepositoryBuildRunSource.
            Allowed values for this property are: "MANUAL", "GITHUB", "GITLAB", "DEVOPS_CODE_REPOSITORY"
        :type source_type: str

        :param trigger_id:
            The value to assign to the trigger_id property of this DevopsCodeRepositoryBuildRunSource.
        :type trigger_id: str

        :param trigger_info:
            The value to assign to the trigger_info property of this DevopsCodeRepositoryBuildRunSource.
        :type trigger_info: oci.devops.models.TriggerInfo

        :param repository_id:
            The value to assign to the repository_id property of this DevopsCodeRepositoryBuildRunSource.
        :type repository_id: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'trigger_id': 'str',
            'trigger_info': 'TriggerInfo',
            'repository_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'trigger_id': 'triggerId',
            'trigger_info': 'triggerInfo',
            'repository_id': 'repositoryId'
        }

        self._source_type = None
        self._trigger_id = None
        self._trigger_info = None
        self._repository_id = None
        self._source_type = 'DEVOPS_CODE_REPOSITORY'

    @property
    def trigger_id(self):
        """
        **[Required]** Gets the trigger_id of this DevopsCodeRepositoryBuildRunSource.
        The trigger that invoked the build run.


        :return: The trigger_id of this DevopsCodeRepositoryBuildRunSource.
        :rtype: str
        """
        return self._trigger_id

    @trigger_id.setter
    def trigger_id(self, trigger_id):
        """
        Sets the trigger_id of this DevopsCodeRepositoryBuildRunSource.
        The trigger that invoked the build run.


        :param trigger_id: The trigger_id of this DevopsCodeRepositoryBuildRunSource.
        :type: str
        """
        self._trigger_id = trigger_id

    @property
    def trigger_info(self):
        """
        **[Required]** Gets the trigger_info of this DevopsCodeRepositoryBuildRunSource.

        :return: The trigger_info of this DevopsCodeRepositoryBuildRunSource.
        :rtype: oci.devops.models.TriggerInfo
        """
        return self._trigger_info

    @trigger_info.setter
    def trigger_info(self, trigger_info):
        """
        Sets the trigger_info of this DevopsCodeRepositoryBuildRunSource.

        :param trigger_info: The trigger_info of this DevopsCodeRepositoryBuildRunSource.
        :type: oci.devops.models.TriggerInfo
        """
        self._trigger_info = trigger_info

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this DevopsCodeRepositoryBuildRunSource.
        The DevOps code repository identifier that invoked the build run.


        :return: The repository_id of this DevopsCodeRepositoryBuildRunSource.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this DevopsCodeRepositoryBuildRunSource.
        The DevOps code repository identifier that invoked the build run.


        :param repository_id: The repository_id of this DevopsCodeRepositoryBuildRunSource.
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
