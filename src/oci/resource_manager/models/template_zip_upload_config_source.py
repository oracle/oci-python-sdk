# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .template_config_source import TemplateConfigSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TemplateZipUploadConfigSource(TemplateConfigSource):
    """
    Metadata about the user-provided Terraform configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TemplateZipUploadConfigSource object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.TemplateZipUploadConfigSource.template_config_source_type` attribute
        of this class is ``ZIP_UPLOAD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param template_config_source_type:
            The value to assign to the template_config_source_type property of this TemplateZipUploadConfigSource.
            Allowed values for this property are: "ZIP_UPLOAD"
        :type template_config_source_type: str

        """
        self.swagger_types = {
            'template_config_source_type': 'str'
        }

        self.attribute_map = {
            'template_config_source_type': 'templateConfigSourceType'
        }

        self._template_config_source_type = None
        self._template_config_source_type = 'ZIP_UPLOAD'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
