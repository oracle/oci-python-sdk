# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dataset_format_details import DatasetFormatDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentDatasetFormatDetails(DatasetFormatDetails):
    """
    It indicates the dataset is comprised of document files.  It is open for further configurability.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentDatasetFormatDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_labeling_service.models.DocumentDatasetFormatDetails.format_type` attribute
        of this class is ``DOCUMENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format_type:
            The value to assign to the format_type property of this DocumentDatasetFormatDetails.
            Allowed values for this property are: "DOCUMENT", "IMAGE", "TEXT"
        :type format_type: str

        """
        self.swagger_types = {
            'format_type': 'str'
        }

        self.attribute_map = {
            'format_type': 'formatType'
        }

        self._format_type = None
        self._format_type = 'DOCUMENT'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
