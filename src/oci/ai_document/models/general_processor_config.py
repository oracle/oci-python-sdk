# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .processor_config import ProcessorConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GeneralProcessorConfig(ProcessorConfig):
    """
    The configuration of a general processor.
    """

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "INVOICE"
    DOCUMENT_TYPE_INVOICE = "INVOICE"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "RECEIPT"
    DOCUMENT_TYPE_RECEIPT = "RECEIPT"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "RESUME"
    DOCUMENT_TYPE_RESUME = "RESUME"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "TAX_FORM"
    DOCUMENT_TYPE_TAX_FORM = "TAX_FORM"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "DRIVER_LICENSE"
    DOCUMENT_TYPE_DRIVER_LICENSE = "DRIVER_LICENSE"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "PASSPORT"
    DOCUMENT_TYPE_PASSPORT = "PASSPORT"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "BANK_STATEMENT"
    DOCUMENT_TYPE_BANK_STATEMENT = "BANK_STATEMENT"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "CHECK"
    DOCUMENT_TYPE_CHECK = "CHECK"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "PAYSLIP"
    DOCUMENT_TYPE_PAYSLIP = "PAYSLIP"

    #: A constant which can be used with the document_type property of a GeneralProcessorConfig.
    #: This constant has a value of "OTHERS"
    DOCUMENT_TYPE_OTHERS = "OTHERS"

    def __init__(self, **kwargs):
        """
        Initializes a new GeneralProcessorConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_document.models.GeneralProcessorConfig.processor_type` attribute
        of this class is ``GENERAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param processor_type:
            The value to assign to the processor_type property of this GeneralProcessorConfig.
            Allowed values for this property are: "GENERAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type processor_type: str

        :param document_type:
            The value to assign to the document_type property of this GeneralProcessorConfig.
            Allowed values for this property are: "INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type document_type: str

        :param features:
            The value to assign to the features property of this GeneralProcessorConfig.
        :type features: list[oci.ai_document.models.DocumentFeature]

        :param is_zip_output_enabled:
            The value to assign to the is_zip_output_enabled property of this GeneralProcessorConfig.
        :type is_zip_output_enabled: bool

        :param language:
            The value to assign to the language property of this GeneralProcessorConfig.
        :type language: str

        """
        self.swagger_types = {
            'processor_type': 'str',
            'document_type': 'str',
            'features': 'list[DocumentFeature]',
            'is_zip_output_enabled': 'bool',
            'language': 'str'
        }

        self.attribute_map = {
            'processor_type': 'processorType',
            'document_type': 'documentType',
            'features': 'features',
            'is_zip_output_enabled': 'isZipOutputEnabled',
            'language': 'language'
        }

        self._processor_type = None
        self._document_type = None
        self._features = None
        self._is_zip_output_enabled = None
        self._language = None
        self._processor_type = 'GENERAL'

    @property
    def document_type(self):
        """
        Gets the document_type of this GeneralProcessorConfig.
        The document type.

        Allowed values for this property are: "INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The document_type of this GeneralProcessorConfig.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this GeneralProcessorConfig.
        The document type.


        :param document_type: The document_type of this GeneralProcessorConfig.
        :type: str
        """
        allowed_values = ["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]
        if not value_allowed_none_or_none_sentinel(document_type, allowed_values):
            document_type = 'UNKNOWN_ENUM_VALUE'
        self._document_type = document_type

    @property
    def features(self):
        """
        **[Required]** Gets the features of this GeneralProcessorConfig.
        The types of document analysis requested.


        :return: The features of this GeneralProcessorConfig.
        :rtype: list[oci.ai_document.models.DocumentFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this GeneralProcessorConfig.
        The types of document analysis requested.


        :param features: The features of this GeneralProcessorConfig.
        :type: list[oci.ai_document.models.DocumentFeature]
        """
        self._features = features

    @property
    def is_zip_output_enabled(self):
        """
        Gets the is_zip_output_enabled of this GeneralProcessorConfig.
        Whether or not to generate a ZIP file containing the results.


        :return: The is_zip_output_enabled of this GeneralProcessorConfig.
        :rtype: bool
        """
        return self._is_zip_output_enabled

    @is_zip_output_enabled.setter
    def is_zip_output_enabled(self, is_zip_output_enabled):
        """
        Sets the is_zip_output_enabled of this GeneralProcessorConfig.
        Whether or not to generate a ZIP file containing the results.


        :param is_zip_output_enabled: The is_zip_output_enabled of this GeneralProcessorConfig.
        :type: bool
        """
        self._is_zip_output_enabled = is_zip_output_enabled

    @property
    def language(self):
        """
        Gets the language of this GeneralProcessorConfig.
        The document language, abbreviated according to the BCP 47 Language-Tag syntax.


        :return: The language of this GeneralProcessorConfig.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this GeneralProcessorConfig.
        The document language, abbreviated according to the BCP 47 Language-Tag syntax.


        :param language: The language of this GeneralProcessorConfig.
        :type: str
        """
        self._language = language

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
