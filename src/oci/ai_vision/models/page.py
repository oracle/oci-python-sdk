# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Page(object):
    """
    One page document analysis result.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Page object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param page_number:
            The value to assign to the page_number property of this Page.
        :type page_number: int

        :param dimensions:
            The value to assign to the dimensions property of this Page.
        :type dimensions: oci.ai_vision.models.Dimensions

        :param detected_document_types:
            The value to assign to the detected_document_types property of this Page.
        :type detected_document_types: list[oci.ai_vision.models.DetectedDocumentType]

        :param detected_languages:
            The value to assign to the detected_languages property of this Page.
        :type detected_languages: list[oci.ai_vision.models.DetectedLanguage]

        :param words:
            The value to assign to the words property of this Page.
        :type words: list[oci.ai_vision.models.Word]

        :param lines:
            The value to assign to the lines property of this Page.
        :type lines: list[oci.ai_vision.models.Line]

        :param tables:
            The value to assign to the tables property of this Page.
        :type tables: list[oci.ai_vision.models.Table]

        :param document_fields:
            The value to assign to the document_fields property of this Page.
        :type document_fields: list[oci.ai_vision.models.DocumentField]

        """
        self.swagger_types = {
            'page_number': 'int',
            'dimensions': 'Dimensions',
            'detected_document_types': 'list[DetectedDocumentType]',
            'detected_languages': 'list[DetectedLanguage]',
            'words': 'list[Word]',
            'lines': 'list[Line]',
            'tables': 'list[Table]',
            'document_fields': 'list[DocumentField]'
        }

        self.attribute_map = {
            'page_number': 'pageNumber',
            'dimensions': 'dimensions',
            'detected_document_types': 'detectedDocumentTypes',
            'detected_languages': 'detectedLanguages',
            'words': 'words',
            'lines': 'lines',
            'tables': 'tables',
            'document_fields': 'documentFields'
        }

        self._page_number = None
        self._dimensions = None
        self._detected_document_types = None
        self._detected_languages = None
        self._words = None
        self._lines = None
        self._tables = None
        self._document_fields = None

    @property
    def page_number(self):
        """
        **[Required]** Gets the page_number of this Page.
        Document page number.


        :return: The page_number of this Page.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """
        Sets the page_number of this Page.
        Document page number.


        :param page_number: The page_number of this Page.
        :type: int
        """
        self._page_number = page_number

    @property
    def dimensions(self):
        """
        Gets the dimensions of this Page.

        :return: The dimensions of this Page.
        :rtype: oci.ai_vision.models.Dimensions
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """
        Sets the dimensions of this Page.

        :param dimensions: The dimensions of this Page.
        :type: oci.ai_vision.models.Dimensions
        """
        self._dimensions = dimensions

    @property
    def detected_document_types(self):
        """
        Gets the detected_document_types of this Page.
        An array of detected document types.


        :return: The detected_document_types of this Page.
        :rtype: list[oci.ai_vision.models.DetectedDocumentType]
        """
        return self._detected_document_types

    @detected_document_types.setter
    def detected_document_types(self, detected_document_types):
        """
        Sets the detected_document_types of this Page.
        An array of detected document types.


        :param detected_document_types: The detected_document_types of this Page.
        :type: list[oci.ai_vision.models.DetectedDocumentType]
        """
        self._detected_document_types = detected_document_types

    @property
    def detected_languages(self):
        """
        Gets the detected_languages of this Page.
        An array of detected languages.


        :return: The detected_languages of this Page.
        :rtype: list[oci.ai_vision.models.DetectedLanguage]
        """
        return self._detected_languages

    @detected_languages.setter
    def detected_languages(self, detected_languages):
        """
        Sets the detected_languages of this Page.
        An array of detected languages.


        :param detected_languages: The detected_languages of this Page.
        :type: list[oci.ai_vision.models.DetectedLanguage]
        """
        self._detected_languages = detected_languages

    @property
    def words(self):
        """
        Gets the words of this Page.
        Words detected on the page.


        :return: The words of this Page.
        :rtype: list[oci.ai_vision.models.Word]
        """
        return self._words

    @words.setter
    def words(self, words):
        """
        Sets the words of this Page.
        Words detected on the page.


        :param words: The words of this Page.
        :type: list[oci.ai_vision.models.Word]
        """
        self._words = words

    @property
    def lines(self):
        """
        Gets the lines of this Page.
        Text lines detected on the page.


        :return: The lines of this Page.
        :rtype: list[oci.ai_vision.models.Line]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this Page.
        Text lines detected on the page.


        :param lines: The lines of this Page.
        :type: list[oci.ai_vision.models.Line]
        """
        self._lines = lines

    @property
    def tables(self):
        """
        Gets the tables of this Page.
        Tables detected on the page.


        :return: The tables of this Page.
        :rtype: list[oci.ai_vision.models.Table]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        """
        Sets the tables of this Page.
        Tables detected on the page.


        :param tables: The tables of this Page.
        :type: list[oci.ai_vision.models.Table]
        """
        self._tables = tables

    @property
    def document_fields(self):
        """
        Gets the document_fields of this Page.
        Form fields detected on the page.


        :return: The document_fields of this Page.
        :rtype: list[oci.ai_vision.models.DocumentField]
        """
        return self._document_fields

    @document_fields.setter
    def document_fields(self, document_fields):
        """
        Sets the document_fields of this Page.
        Form fields detected on the page.


        :param document_fields: The document_fields of this Page.
        :type: list[oci.ai_vision.models.DocumentField]
        """
        self._document_fields = document_fields

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
