# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SortClause(object):
    """
    The information about the sort object.
    """

    #: A constant which can be used with the order property of a SortClause.
    #: This constant has a value of "ASC"
    ORDER_ASC = "ASC"

    #: A constant which can be used with the order property of a SortClause.
    #: This constant has a value of "DESC"
    ORDER_DESC = "DESC"

    def __init__(self, **kwargs):
        """
        Initializes a new SortClause object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field:
            The value to assign to the field property of this SortClause.
        :type field: oci.data_connectivity.models.ShapeField

        :param order:
            The value to assign to the order property of this SortClause.
            Allowed values for this property are: "ASC", "DESC"
        :type order: str

        """
        self.swagger_types = {
            'field': 'ShapeField',
            'order': 'str'
        }

        self.attribute_map = {
            'field': 'field',
            'order': 'order'
        }

        self._field = None
        self._order = None

    @property
    def field(self):
        """
        Gets the field of this SortClause.

        :return: The field of this SortClause.
        :rtype: oci.data_connectivity.models.ShapeField
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this SortClause.

        :param field: The field of this SortClause.
        :type: oci.data_connectivity.models.ShapeField
        """
        self._field = field

    @property
    def order(self):
        """
        Gets the order of this SortClause.
        The sort order.

        Allowed values for this property are: "ASC", "DESC"


        :return: The order of this SortClause.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this SortClause.
        The sort order.


        :param order: The order of this SortClause.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if not value_allowed_none_or_none_sentinel(order, allowed_values):
            raise ValueError(
                "Invalid value for `order`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._order = order

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
