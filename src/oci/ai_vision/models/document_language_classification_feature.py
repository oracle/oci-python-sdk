# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .document_feature import DocumentFeature
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DocumentLanguageClassificationFeature(DocumentFeature):
    """
    Detecting the language of the document.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DocumentLanguageClassificationFeature object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.DocumentLanguageClassificationFeature.feature_type` attribute
        of this class is ``LANGUAGE_CLASSIFICATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature_type:
            The value to assign to the feature_type property of this DocumentLanguageClassificationFeature.
            Allowed values for this property are: "LANGUAGE_CLASSIFICATION", "TEXT_DETECTION", "TABLE_DETECTION", "KEY_VALUE_DETECTION", "DOCUMENT_CLASSIFICATION"
        :type feature_type: str

        :param max_results:
            The value to assign to the max_results property of this DocumentLanguageClassificationFeature.
        :type max_results: int

        """
        self.swagger_types = {
            'feature_type': 'str',
            'max_results': 'int'
        }

        self.attribute_map = {
            'feature_type': 'featureType',
            'max_results': 'maxResults'
        }

        self._feature_type = None
        self._max_results = None
        self._feature_type = 'LANGUAGE_CLASSIFICATION'

    @property
    def max_results(self):
        """
        Gets the max_results of this DocumentLanguageClassificationFeature.
        The maximum number of results to return.


        :return: The max_results of this DocumentLanguageClassificationFeature.
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """
        Sets the max_results of this DocumentLanguageClassificationFeature.
        The maximum number of results to return.


        :param max_results: The max_results of this DocumentLanguageClassificationFeature.
        :type: int
        """
        self._max_results = max_results

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
