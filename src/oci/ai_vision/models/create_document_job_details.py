# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDocumentJobDetails(object):
    """
    The batch document analysis details.
    """

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "ENG"
    LANGUAGE_ENG = "ENG"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "CES"
    LANGUAGE_CES = "CES"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "DAN"
    LANGUAGE_DAN = "DAN"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "NLD"
    LANGUAGE_NLD = "NLD"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "FIN"
    LANGUAGE_FIN = "FIN"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "FRA"
    LANGUAGE_FRA = "FRA"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "DEU"
    LANGUAGE_DEU = "DEU"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "ELL"
    LANGUAGE_ELL = "ELL"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "HUN"
    LANGUAGE_HUN = "HUN"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "ITA"
    LANGUAGE_ITA = "ITA"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "NOR"
    LANGUAGE_NOR = "NOR"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "POL"
    LANGUAGE_POL = "POL"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "POR"
    LANGUAGE_POR = "POR"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "RON"
    LANGUAGE_RON = "RON"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "RUS"
    LANGUAGE_RUS = "RUS"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "SLK"
    LANGUAGE_SLK = "SLK"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "SPA"
    LANGUAGE_SPA = "SPA"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "SWE"
    LANGUAGE_SWE = "SWE"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "TUR"
    LANGUAGE_TUR = "TUR"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "ARA"
    LANGUAGE_ARA = "ARA"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "CHI_SIM"
    LANGUAGE_CHI_SIM = "CHI_SIM"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "HIN"
    LANGUAGE_HIN = "HIN"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "JPN"
    LANGUAGE_JPN = "JPN"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "KOR"
    LANGUAGE_KOR = "KOR"

    #: A constant which can be used with the language property of a CreateDocumentJobDetails.
    #: This constant has a value of "OTHERS"
    LANGUAGE_OTHERS = "OTHERS"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "INVOICE"
    DOCUMENT_TYPE_INVOICE = "INVOICE"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "RECEIPT"
    DOCUMENT_TYPE_RECEIPT = "RECEIPT"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "RESUME"
    DOCUMENT_TYPE_RESUME = "RESUME"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "TAX_FORM"
    DOCUMENT_TYPE_TAX_FORM = "TAX_FORM"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "DRIVER_LICENSE"
    DOCUMENT_TYPE_DRIVER_LICENSE = "DRIVER_LICENSE"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "PASSPORT"
    DOCUMENT_TYPE_PASSPORT = "PASSPORT"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "BANK_STATEMENT"
    DOCUMENT_TYPE_BANK_STATEMENT = "BANK_STATEMENT"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "CHECK"
    DOCUMENT_TYPE_CHECK = "CHECK"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "PAYSLIP"
    DOCUMENT_TYPE_PAYSLIP = "PAYSLIP"

    #: A constant which can be used with the document_type property of a CreateDocumentJobDetails.
    #: This constant has a value of "OTHERS"
    DOCUMENT_TYPE_OTHERS = "OTHERS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDocumentJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_location:
            The value to assign to the input_location property of this CreateDocumentJobDetails.
        :type input_location: oci.ai_vision.models.InputLocation

        :param features:
            The value to assign to the features property of this CreateDocumentJobDetails.
        :type features: list[oci.ai_vision.models.DocumentFeature]

        :param output_location:
            The value to assign to the output_location property of this CreateDocumentJobDetails.
        :type output_location: oci.ai_vision.models.OutputLocation

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDocumentJobDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateDocumentJobDetails.
        :type display_name: str

        :param language:
            The value to assign to the language property of this CreateDocumentJobDetails.
            Allowed values for this property are: "ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"
        :type language: str

        :param document_type:
            The value to assign to the document_type property of this CreateDocumentJobDetails.
            Allowed values for this property are: "INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"
        :type document_type: str

        :param is_zip_output_enabled:
            The value to assign to the is_zip_output_enabled property of this CreateDocumentJobDetails.
        :type is_zip_output_enabled: bool

        """
        self.swagger_types = {
            'input_location': 'InputLocation',
            'features': 'list[DocumentFeature]',
            'output_location': 'OutputLocation',
            'compartment_id': 'str',
            'display_name': 'str',
            'language': 'str',
            'document_type': 'str',
            'is_zip_output_enabled': 'bool'
        }

        self.attribute_map = {
            'input_location': 'inputLocation',
            'features': 'features',
            'output_location': 'outputLocation',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'language': 'language',
            'document_type': 'documentType',
            'is_zip_output_enabled': 'isZipOutputEnabled'
        }

        self._input_location = None
        self._features = None
        self._output_location = None
        self._compartment_id = None
        self._display_name = None
        self._language = None
        self._document_type = None
        self._is_zip_output_enabled = None

    @property
    def input_location(self):
        """
        **[Required]** Gets the input_location of this CreateDocumentJobDetails.

        :return: The input_location of this CreateDocumentJobDetails.
        :rtype: oci.ai_vision.models.InputLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this CreateDocumentJobDetails.

        :param input_location: The input_location of this CreateDocumentJobDetails.
        :type: oci.ai_vision.models.InputLocation
        """
        self._input_location = input_location

    @property
    def features(self):
        """
        **[Required]** Gets the features of this CreateDocumentJobDetails.
        The list of requested document analysis types.


        :return: The features of this CreateDocumentJobDetails.
        :rtype: list[oci.ai_vision.models.DocumentFeature]
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this CreateDocumentJobDetails.
        The list of requested document analysis types.


        :param features: The features of this CreateDocumentJobDetails.
        :type: list[oci.ai_vision.models.DocumentFeature]
        """
        self._features = features

    @property
    def output_location(self):
        """
        **[Required]** Gets the output_location of this CreateDocumentJobDetails.

        :return: The output_location of this CreateDocumentJobDetails.
        :rtype: oci.ai_vision.models.OutputLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this CreateDocumentJobDetails.

        :param output_location: The output_location of this CreateDocumentJobDetails.
        :type: oci.ai_vision.models.OutputLocation
        """
        self._output_location = output_location

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateDocumentJobDetails.
        The compartment identifier from the requester.


        :return: The compartment_id of this CreateDocumentJobDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDocumentJobDetails.
        The compartment identifier from the requester.


        :param compartment_id: The compartment_id of this CreateDocumentJobDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDocumentJobDetails.
        The document job display name.


        :return: The display_name of this CreateDocumentJobDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDocumentJobDetails.
        The document job display name.


        :param display_name: The display_name of this CreateDocumentJobDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def language(self):
        """
        Gets the language of this CreateDocumentJobDetails.
        The language of the document, abbreviated according to ISO 639-2.

        Allowed values for this property are: "ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"


        :return: The language of this CreateDocumentJobDetails.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this CreateDocumentJobDetails.
        The language of the document, abbreviated according to ISO 639-2.


        :param language: The language of this CreateDocumentJobDetails.
        :type: str
        """
        allowed_values = ["ENG", "CES", "DAN", "NLD", "FIN", "FRA", "DEU", "ELL", "HUN", "ITA", "NOR", "POL", "POR", "RON", "RUS", "SLK", "SPA", "SWE", "TUR", "ARA", "CHI_SIM", "HIN", "JPN", "KOR", "OTHERS"]
        if not value_allowed_none_or_none_sentinel(language, allowed_values):
            raise ValueError(
                "Invalid value for `language`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._language = language

    @property
    def document_type(self):
        """
        Gets the document_type of this CreateDocumentJobDetails.
        The type of documents.

        Allowed values for this property are: "INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"


        :return: The document_type of this CreateDocumentJobDetails.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this CreateDocumentJobDetails.
        The type of documents.


        :param document_type: The document_type of this CreateDocumentJobDetails.
        :type: str
        """
        allowed_values = ["INVOICE", "RECEIPT", "RESUME", "TAX_FORM", "DRIVER_LICENSE", "PASSPORT", "BANK_STATEMENT", "CHECK", "PAYSLIP", "OTHERS"]
        if not value_allowed_none_or_none_sentinel(document_type, allowed_values):
            raise ValueError(
                "Invalid value for `document_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._document_type = document_type

    @property
    def is_zip_output_enabled(self):
        """
        Gets the is_zip_output_enabled of this CreateDocumentJobDetails.
        Whether or not to generate a ZIP file containing the results.


        :return: The is_zip_output_enabled of this CreateDocumentJobDetails.
        :rtype: bool
        """
        return self._is_zip_output_enabled

    @is_zip_output_enabled.setter
    def is_zip_output_enabled(self, is_zip_output_enabled):
        """
        Sets the is_zip_output_enabled of this CreateDocumentJobDetails.
        Whether or not to generate a ZIP file containing the results.


        :param is_zip_output_enabled: The is_zip_output_enabled of this CreateDocumentJobDetails.
        :type: bool
        """
        self._is_zip_output_enabled = is_zip_output_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
