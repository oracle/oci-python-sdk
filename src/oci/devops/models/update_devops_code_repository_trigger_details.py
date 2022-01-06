# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_trigger_details import UpdateTriggerDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDevopsCodeRepositoryTriggerDetails(UpdateTriggerDetails):
    """
    Update trigger specific to OCI DevOps code repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDevopsCodeRepositoryTriggerDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.devops.models.UpdateDevopsCodeRepositoryTriggerDetails.trigger_source` attribute
        of this class is ``DEVOPS_CODE_REPOSITORY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDevopsCodeRepositoryTriggerDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDevopsCodeRepositoryTriggerDetails.
        :type description: str

        :param trigger_source:
            The value to assign to the trigger_source property of this UpdateDevopsCodeRepositoryTriggerDetails.
        :type trigger_source: str

        :param actions:
            The value to assign to the actions property of this UpdateDevopsCodeRepositoryTriggerDetails.
        :type actions: list[oci.devops.models.TriggerAction]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateDevopsCodeRepositoryTriggerDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateDevopsCodeRepositoryTriggerDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param repository_id:
            The value to assign to the repository_id property of this UpdateDevopsCodeRepositoryTriggerDetails.
        :type repository_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'trigger_source': 'str',
            'actions': 'list[TriggerAction]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'repository_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'trigger_source': 'triggerSource',
            'actions': 'actions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'repository_id': 'repositoryId'
        }

        self._display_name = None
        self._description = None
        self._trigger_source = None
        self._actions = None
        self._freeform_tags = None
        self._defined_tags = None
        self._repository_id = None
        self._trigger_source = 'DEVOPS_CODE_REPOSITORY'

    @property
    def repository_id(self):
        """
        Gets the repository_id of this UpdateDevopsCodeRepositoryTriggerDetails.
        The OCID of the DevOps code repository.


        :return: The repository_id of this UpdateDevopsCodeRepositoryTriggerDetails.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        """
        Sets the repository_id of this UpdateDevopsCodeRepositoryTriggerDetails.
        The OCID of the DevOps code repository.


        :param repository_id: The repository_id of this UpdateDevopsCodeRepositoryTriggerDetails.
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
