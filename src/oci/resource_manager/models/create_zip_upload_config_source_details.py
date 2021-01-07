# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_config_source_details import CreateConfigSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateZipUploadConfigSourceDetails(CreateConfigSourceDetails):
    """
    Property details for uploading the configuration zip file.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateZipUploadConfigSourceDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.CreateZipUploadConfigSourceDetails.config_source_type` attribute
        of this class is ``ZIP_UPLOAD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_source_type:
            The value to assign to the config_source_type property of this CreateZipUploadConfigSourceDetails.
        :type config_source_type: str

        :param working_directory:
            The value to assign to the working_directory property of this CreateZipUploadConfigSourceDetails.
        :type working_directory: str

        :param zip_file_base64_encoded:
            The value to assign to the zip_file_base64_encoded property of this CreateZipUploadConfigSourceDetails.
        :type zip_file_base64_encoded: str

        """
        self.swagger_types = {
            'config_source_type': 'str',
            'working_directory': 'str',
            'zip_file_base64_encoded': 'str'
        }

        self.attribute_map = {
            'config_source_type': 'configSourceType',
            'working_directory': 'workingDirectory',
            'zip_file_base64_encoded': 'zipFileBase64Encoded'
        }

        self._config_source_type = None
        self._working_directory = None
        self._zip_file_base64_encoded = None
        self._config_source_type = 'ZIP_UPLOAD'

    @property
    def zip_file_base64_encoded(self):
        """
        **[Required]** Gets the zip_file_base64_encoded of this CreateZipUploadConfigSourceDetails.

        :return: The zip_file_base64_encoded of this CreateZipUploadConfigSourceDetails.
        :rtype: str
        """
        return self._zip_file_base64_encoded

    @zip_file_base64_encoded.setter
    def zip_file_base64_encoded(self, zip_file_base64_encoded):
        """
        Sets the zip_file_base64_encoded of this CreateZipUploadConfigSourceDetails.

        :param zip_file_base64_encoded: The zip_file_base64_encoded of this CreateZipUploadConfigSourceDetails.
        :type: str
        """
        self._zip_file_base64_encoded = zip_file_base64_encoded

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
