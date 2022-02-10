# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TableRow(object):
    """
    A single row in a table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TableRow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cells:
            The value to assign to the cells property of this TableRow.
        :type cells: list[oci.ai_vision.models.Cell]

        """
        self.swagger_types = {
            'cells': 'list[Cell]'
        }

        self.attribute_map = {
            'cells': 'cells'
        }

        self._cells = None

    @property
    def cells(self):
        """
        **[Required]** Gets the cells of this TableRow.
        Cells in the row.


        :return: The cells of this TableRow.
        :rtype: list[oci.ai_vision.models.Cell]
        """
        return self._cells

    @cells.setter
    def cells(self, cells):
        """
        Sets the cells of this TableRow.
        Cells in the row.


        :param cells: The cells of this TableRow.
        :type: list[oci.ai_vision.models.Cell]
        """
        self._cells = cells

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
