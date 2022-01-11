# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BatchDetectLanguageSentimentsDetails(object):
    """
    The documents details for sentiment call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BatchDetectLanguageSentimentsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param documents:
            The value to assign to the documents property of this BatchDetectLanguageSentimentsDetails.
        :type documents: list[oci.ai_language.models.SentimentsDocument]

        """
        self.swagger_types = {
            'documents': 'list[SentimentsDocument]'
        }

        self.attribute_map = {
            'documents': 'documents'
        }

        self._documents = None

    @property
    def documents(self):
        """
        **[Required]** Gets the documents of this BatchDetectLanguageSentimentsDetails.
        List of Documents for detect sentiments.


        :return: The documents of this BatchDetectLanguageSentimentsDetails.
        :rtype: list[oci.ai_language.models.SentimentsDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this BatchDetectLanguageSentimentsDetails.
        List of Documents for detect sentiments.


        :param documents: The documents of this BatchDetectLanguageSentimentsDetails.
        :type: list[oci.ai_language.models.SentimentsDocument]
        """
        self._documents = documents

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
