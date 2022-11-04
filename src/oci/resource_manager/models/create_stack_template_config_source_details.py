# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_config_source_details import CreateConfigSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateStackTemplateConfigSourceDetails(CreateConfigSourceDetails):
    """
    Creation details for a template to use as the source of the Terraform configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateStackTemplateConfigSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateStackTemplateConfigSourceDetails.config_source_type` attribute
        of this class is ``TEMPLATE_CONFIG_SOURCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this CreateStackTemplateConfigSourceDetails.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this CreateStackTemplateConfigSourceDetails.
        :type working_directory: str

        :param template_id:
            The value to assign to the template_id property of this CreateStackTemplateConfigSourceDetails.
        :type template_id: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str',
            'template_id': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory',
            'template_id': 'templateId'
        }

        self._config_source_type = None
        self._working_directory = None
        self._template_id = None
        self._config_source_type = 'TEMPLATE_CONFIG_SOURCE'

    @property
    def template_id(self):
        """
        **[Required]** Gets the template_id of this CreateStackTemplateConfigSourceDetails.

        :return: The template_id of this CreateStackTemplateConfigSourceDetails.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this CreateStackTemplateConfigSourceDetails.

        :param template_id: The template_id of this CreateStackTemplateConfigSourceDetails.
        :type: str
        """
        self._template_id = template_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
