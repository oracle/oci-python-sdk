# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dataset_format_details import DatasetFormatDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextDatasetFormatDetails(DatasetFormatDetails):
    """
    It indicates the dataset is comprised of TXT files.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextDatasetFormatDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service.models.TextDatasetFormatDetails.format_type` attribute
        of this class is ``TEXT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format_type:
            The value to assign to the format_type property of this TextDatasetFormatDetails.
            Allowed values for this property are: "DOCUMENT", "IMAGE", "TEXT"
        :type format_type: str

        :param text_file_type_metadata:
            The value to assign to the text_file_type_metadata property of this TextDatasetFormatDetails.
        :type text_file_type_metadata: oci.data_labeling_service.models.TextFileTypeMetadata

        """
        self.swagger_types = {
            'format_type': 'str',
            'text_file_type_metadata': 'TextFileTypeMetadata'
        }

        self.attribute_map = {
            'format_type': 'formatType',
            'text_file_type_metadata': 'textFileTypeMetadata'
        }

        self._format_type = None
        self._text_file_type_metadata = None
        self._format_type = 'TEXT'

    @property
    def text_file_type_metadata(self):
        """
        Gets the text_file_type_metadata of this TextDatasetFormatDetails.

        :return: The text_file_type_metadata of this TextDatasetFormatDetails.
        :rtype: oci.data_labeling_service.models.TextFileTypeMetadata
        """
        return self._text_file_type_metadata

    @text_file_type_metadata.setter
    def text_file_type_metadata(self, text_file_type_metadata):
        """
        Sets the text_file_type_metadata of this TextDatasetFormatDetails.

        :param text_file_type_metadata: The text_file_type_metadata of this TextDatasetFormatDetails.
        :type: oci.data_labeling_service.models.TextFileTypeMetadata
        """
        self._text_file_type_metadata = text_file_type_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
