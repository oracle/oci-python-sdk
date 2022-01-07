# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .config_source import ConfigSource
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ZipUploadConfigSource(ConfigSource):
    """
    Metadata about the user-provided Terraform configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ZipUploadConfigSource object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.ZipUploadConfigSource.config_source_type` attribute
        of this class is ``ZIP_UPLOAD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this ZipUploadConfigSource.
            Allowed values for this property are: "ZIP_UPLOAD", "GIT_CONFIG_SOURCE", "COMPARTMENT_CONFIG_SOURCE", "OBJECT_STORAGE_CONFIG_SOURCE"
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this ZipUploadConfigSource.
        :type working_directory: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory'
        }

        self._config_source_type = None
        self._working_directory = None
        self._config_source_type = 'ZIP_UPLOAD'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
