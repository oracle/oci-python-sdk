# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_media_workflow_job_details import CreateMediaWorkflowJobDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMediaWorkflowJobByIdDetails(CreateMediaWorkflowJobDetails):
    """
    Information to run a MediaWorkflow identified by its OCID.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMediaWorkflowJobByIdDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.media_services.models.CreateMediaWorkflowJobByIdDetails.workflow_identifier_type` attribute
        of this class is ``ID`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param workflow_identifier_type:
            The value to assign to the workflow_identifier_type property of this CreateMediaWorkflowJobByIdDetails.
            Allowed values for this property are: "ID", "NAME"
        :type workflow_identifier_type: str

        :param media_workflow_configuration_ids:
            The value to assign to the media_workflow_configuration_ids property of this CreateMediaWorkflowJobByIdDetails.
        :type media_workflow_configuration_ids: list[str]

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMediaWorkflowJobByIdDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateMediaWorkflowJobByIdDetails.
        :type display_name: str

        :param parameters:
            The value to assign to the parameters property of this CreateMediaWorkflowJobByIdDetails.
        :type parameters: dict(str, object)

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMediaWorkflowJobByIdDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMediaWorkflowJobByIdDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param media_workflow_id:
            The value to assign to the media_workflow_id property of this CreateMediaWorkflowJobByIdDetails.
        :type media_workflow_id: str

        """
        self.swagger_types = {
            'workflow_identifier_type': 'str',
            'media_workflow_configuration_ids': 'list[str]',
            'compartment_id': 'str',
            'display_name': 'str',
            'parameters': 'dict(str, object)',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'media_workflow_id': 'str'
        }

        self.attribute_map = {
            'workflow_identifier_type': 'workflowIdentifierType',
            'media_workflow_configuration_ids': 'mediaWorkflowConfigurationIds',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'parameters': 'parameters',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'media_workflow_id': 'mediaWorkflowId'
        }

        self._workflow_identifier_type = None
        self._media_workflow_configuration_ids = None
        self._compartment_id = None
        self._display_name = None
        self._parameters = None
        self._freeform_tags = None
        self._defined_tags = None
        self._media_workflow_id = None
        self._workflow_identifier_type = 'ID'

    @property
    def media_workflow_id(self):
        """
        Gets the media_workflow_id of this CreateMediaWorkflowJobByIdDetails.
        OCID of the MediaWorkflow that should be run.


        :return: The media_workflow_id of this CreateMediaWorkflowJobByIdDetails.
        :rtype: str
        """
        return self._media_workflow_id

    @media_workflow_id.setter
    def media_workflow_id(self, media_workflow_id):
        """
        Sets the media_workflow_id of this CreateMediaWorkflowJobByIdDetails.
        OCID of the MediaWorkflow that should be run.


        :param media_workflow_id: The media_workflow_id of this CreateMediaWorkflowJobByIdDetails.
        :type: str
        """
        self._media_workflow_id = media_workflow_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
