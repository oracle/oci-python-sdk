# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Table(object):
    """
    The table extracted from a document.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Table object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param row_count:
            The value to assign to the row_count property of this Table.
        :type row_count: int

        :param column_count:
            The value to assign to the column_count property of this Table.
        :type column_count: int

        :param header_rows:
            The value to assign to the header_rows property of this Table.
        :type header_rows: list[oci.ai_document.models.TableRow]

        :param body_rows:
            The value to assign to the body_rows property of this Table.
        :type body_rows: list[oci.ai_document.models.TableRow]

        :param footer_rows:
            The value to assign to the footer_rows property of this Table.
        :type footer_rows: list[oci.ai_document.models.TableRow]

        :param confidence:
            The value to assign to the confidence property of this Table.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this Table.
        :type bounding_polygon: oci.ai_document.models.BoundingPolygon

        """
        self.swagger_types = {
            'row_count': 'int',
            'column_count': 'int',
            'header_rows': 'list[TableRow]',
            'body_rows': 'list[TableRow]',
            'footer_rows': 'list[TableRow]',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon'
        }

        self.attribute_map = {
            'row_count': 'rowCount',
            'column_count': 'columnCount',
            'header_rows': 'headerRows',
            'body_rows': 'bodyRows',
            'footer_rows': 'footerRows',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon'
        }

        self._row_count = None
        self._column_count = None
        self._header_rows = None
        self._body_rows = None
        self._footer_rows = None
        self._confidence = None
        self._bounding_polygon = None

    @property
    def row_count(self):
        """
        **[Required]** Gets the row_count of this Table.
        The number of rows.


        :return: The row_count of this Table.
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """
        Sets the row_count of this Table.
        The number of rows.


        :param row_count: The row_count of this Table.
        :type: int
        """
        self._row_count = row_count

    @property
    def column_count(self):
        """
        **[Required]** Gets the column_count of this Table.
        The number of columns.


        :return: The column_count of this Table.
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        """
        Sets the column_count of this Table.
        The number of columns.


        :param column_count: The column_count of this Table.
        :type: int
        """
        self._column_count = column_count

    @property
    def header_rows(self):
        """
        **[Required]** Gets the header_rows of this Table.
        The header rows.


        :return: The header_rows of this Table.
        :rtype: list[oci.ai_document.models.TableRow]
        """
        return self._header_rows

    @header_rows.setter
    def header_rows(self, header_rows):
        """
        Sets the header_rows of this Table.
        The header rows.


        :param header_rows: The header_rows of this Table.
        :type: list[oci.ai_document.models.TableRow]
        """
        self._header_rows = header_rows

    @property
    def body_rows(self):
        """
        **[Required]** Gets the body_rows of this Table.
        The body rows.


        :return: The body_rows of this Table.
        :rtype: list[oci.ai_document.models.TableRow]
        """
        return self._body_rows

    @body_rows.setter
    def body_rows(self, body_rows):
        """
        Sets the body_rows of this Table.
        The body rows.


        :param body_rows: The body_rows of this Table.
        :type: list[oci.ai_document.models.TableRow]
        """
        self._body_rows = body_rows

    @property
    def footer_rows(self):
        """
        **[Required]** Gets the footer_rows of this Table.
        the footer rows.


        :return: The footer_rows of this Table.
        :rtype: list[oci.ai_document.models.TableRow]
        """
        return self._footer_rows

    @footer_rows.setter
    def footer_rows(self, footer_rows):
        """
        Sets the footer_rows of this Table.
        the footer rows.


        :param footer_rows: The footer_rows of this Table.
        :type: list[oci.ai_document.models.TableRow]
        """
        self._footer_rows = footer_rows

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this Table.
        The confidence score between 0 and 1.


        :return: The confidence of this Table.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Table.
        The confidence score between 0 and 1.


        :param confidence: The confidence of this Table.
        :type: float
        """
        self._confidence = confidence

    @property
    def bounding_polygon(self):
        """
        **[Required]** Gets the bounding_polygon of this Table.

        :return: The bounding_polygon of this Table.
        :rtype: oci.ai_document.models.BoundingPolygon
        """
        return self._bounding_polygon

    @bounding_polygon.setter
    def bounding_polygon(self, bounding_polygon):
        """
        Sets the bounding_polygon of this Table.

        :param bounding_polygon: The bounding_polygon of this Table.
        :type: oci.ai_document.models.BoundingPolygon
        """
        self._bounding_polygon = bounding_polygon

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
