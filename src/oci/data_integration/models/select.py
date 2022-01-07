# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .push_down_operation import PushDownOperation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Select(PushDownOperation):
    """
    The information about the select object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Select object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Select.model_type` attribute
        of this class is ``SELECT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Select.
            Allowed values for this property are: "FILTER", "JOIN", "SELECT", "SORT", "QUERY"
        :type model_type: str

        :param is_distinct:
            The value to assign to the is_distinct property of this Select.
        :type is_distinct: bool

        :param select_columns:
            The value to assign to the select_columns property of this Select.
        :type select_columns: list[oci.data_integration.models.ShapeField]

        """
        self.swagger_types = {
            'model_type': 'str',
            'is_distinct': 'bool',
            'select_columns': 'list[ShapeField]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'is_distinct': 'isDistinct',
            'select_columns': 'selectColumns'
        }

        self._model_type = None
        self._is_distinct = None
        self._select_columns = None
        self._model_type = 'SELECT'

    @property
    def is_distinct(self):
        """
        Gets the is_distinct of this Select.
        Specifies whether the object is distinct.


        :return: The is_distinct of this Select.
        :rtype: bool
        """
        return self._is_distinct

    @is_distinct.setter
    def is_distinct(self, is_distinct):
        """
        Sets the is_distinct of this Select.
        Specifies whether the object is distinct.


        :param is_distinct: The is_distinct of this Select.
        :type: bool
        """
        self._is_distinct = is_distinct

    @property
    def select_columns(self):
        """
        Gets the select_columns of this Select.
        An array of selected columns.


        :return: The select_columns of this Select.
        :rtype: list[oci.data_integration.models.ShapeField]
        """
        return self._select_columns

    @select_columns.setter
    def select_columns(self, select_columns):
        """
        Sets the select_columns of this Select.
        An array of selected columns.


        :param select_columns: The select_columns of this Select.
        :type: list[oci.data_integration.models.ShapeField]
        """
        self._select_columns = select_columns

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
