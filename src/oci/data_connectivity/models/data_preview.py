# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataPreview(object):
    """
    The data preview response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataPreview object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_name:
            The value to assign to the entity_name property of this DataPreview.
        :type entity_name: str

        :param sample_rows_count:
            The value to assign to the sample_rows_count property of this DataPreview.
        :type sample_rows_count: int

        :param columns:
            The value to assign to the columns property of this DataPreview.
        :type columns: list[oci.data_connectivity.models.Column]

        :param rows:
            The value to assign to the rows property of this DataPreview.
        :type rows: list[oci.data_connectivity.models.Row]

        """
        self.swagger_types = {
            'entity_name': 'str',
            'sample_rows_count': 'int',
            'columns': 'list[Column]',
            'rows': 'list[Row]'
        }

        self.attribute_map = {
            'entity_name': 'entityName',
            'sample_rows_count': 'sampleRowsCount',
            'columns': 'columns',
            'rows': 'rows'
        }

        self._entity_name = None
        self._sample_rows_count = None
        self._columns = None
        self._rows = None

    @property
    def entity_name(self):
        """
        **[Required]** Gets the entity_name of this DataPreview.
        Name of the entity for which data preview was requested


        :return: The entity_name of this DataPreview.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this DataPreview.
        Name of the entity for which data preview was requested


        :param entity_name: The entity_name of this DataPreview.
        :type: str
        """
        self._entity_name = entity_name

    @property
    def sample_rows_count(self):
        """
        Gets the sample_rows_count of this DataPreview.
        Total number of rows taken for sampling


        :return: The sample_rows_count of this DataPreview.
        :rtype: int
        """
        return self._sample_rows_count

    @sample_rows_count.setter
    def sample_rows_count(self, sample_rows_count):
        """
        Sets the sample_rows_count of this DataPreview.
        Total number of rows taken for sampling


        :param sample_rows_count: The sample_rows_count of this DataPreview.
        :type: int
        """
        self._sample_rows_count = sample_rows_count

    @property
    def columns(self):
        """
        Gets the columns of this DataPreview.
        Array of column definition for the preview result


        :return: The columns of this DataPreview.
        :rtype: list[oci.data_connectivity.models.Column]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this DataPreview.
        Array of column definition for the preview result


        :param columns: The columns of this DataPreview.
        :type: list[oci.data_connectivity.models.Column]
        """
        self._columns = columns

    @property
    def rows(self):
        """
        Gets the rows of this DataPreview.
        Array of rows values for the preview result


        :return: The rows of this DataPreview.
        :rtype: list[oci.data_connectivity.models.Row]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """
        Sets the rows of this DataPreview.
        Array of rows values for the preview result


        :param rows: The rows of this DataPreview.
        :type: list[oci.data_connectivity.models.Row]
        """
        self._rows = rows

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
