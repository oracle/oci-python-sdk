# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .trigger import Trigger
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DevopsCodeRepositoryTrigger(Trigger):
    """
    Trigger specific to OCI DevOps Code Repository service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DevopsCodeRepositoryTrigger object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.DevopsCodeRepositoryTrigger.trigger_source` attribute
        of this class is ``DEVOPS_CODE_REPOSITORY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DevopsCodeRepositoryTrigger.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DevopsCodeRepositoryTrigger.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DevopsCodeRepositoryTrigger.
        :type description: str

        :param project_id:
            The value to assign to the project_id property of this DevopsCodeRepositoryTrigger.
        :type project_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DevopsCodeRepositoryTrigger.
        :type compartment_id: str

        :param trigger_source:
            The value to assign to the trigger_source property of this DevopsCodeRepositoryTrigger.
            Allowed values for this property are: "GITHUB", "GITLAB", "GITLAB_SERVER", "BITBUCKET_CLOUD", "BITBUCKET_SERVER", "VBS", "DEVOPS_CODE_REPOSITORY"
        :type trigger_source: str

        :param time_created:
            The value to assign to the time_created property of this DevopsCodeRepositoryTrigger.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DevopsCodeRepositoryTrigger.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DevopsCodeRepositoryTrigger.
            Allowed values for this property are: "ACTIVE"
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DevopsCodeRepositoryTrigger.
        :type lifecycle_details: str

        :param actions:
            The value to assign to the actions property of this DevopsCodeRepositoryTrigger.
        :type actions: list[oci.devops.models.TriggerAction]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DevopsCodeRepositoryTrigger.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DevopsCodeRepositoryTrigger.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this DevopsCodeRepositoryTrigger.
        :type system_tags: dict(str, dict(str, object))

        :param repository_id:
            The value to assign to the repository_id property of this DevopsCodeRepositoryTrigger.
        :type repository_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'project_id': 'str',
            'compartment_id': 'str',
            'trigger_source': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'actions': 'list[TriggerAction]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'repository_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'project_id': 'projectId',
            'compartment_id': 'compartmentId',
            'trigger_source': 'triggerSource',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'actions': 'actions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'repository_id': 'repositoryId'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._project_id = None
        self._compartment_id = None
        self._trigger_source = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._actions = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._repository_id = None
        self._trigger_source = 'DEVOPS_CODE_REPOSITORY'

    @property
    def repository_id(self):
        """
        **[Required]** Gets the repository_id of this DevopsCodeRepositoryTrigger.
        The OCID of the DevOps code repository.


        :return: The repository_id of this DevopsCodeRepositoryTrigger.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this DevopsCodeRepositoryTrigger.
        The OCID of the DevOps code repository.


        :param repository_id: The repository_id of this DevopsCodeRepositoryTrigger.
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
