# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .argument import Argument
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LiteralArgument(Argument):
    """
    QueryString argument of type literal.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LiteralArgument object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.LiteralArgument.type` attribute
        of this class is ``LITERAL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this LiteralArgument.
            Allowed values for this property are: "FIELD", "LITERAL"
        :type type: str

        :param data_type:
            The value to assign to the data_type property of this LiteralArgument.
        :type data_type: str

        :param value:
            The value to assign to the value property of this LiteralArgument.
        :type value: object

        """
        self.swagger_types = {
            'type': 'str',
            'data_type': 'str',
            'value': 'object'
        }

        self.attribute_map = {
            'type': 'type',
            'data_type': 'dataType',
            'value': 'value'
        }

        self._type = None
        self._data_type = None
        self._value = None
        self._type = 'LITERAL'

    @property
    def data_type(self):
        """
        Gets the data_type of this LiteralArgument.
        Data type of specified literal in queryString.


        :return: The data_type of this LiteralArgument.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this LiteralArgument.
        Data type of specified literal in queryString.


        :param data_type: The data_type of this LiteralArgument.
        :type: str
        """
        self._data_type = data_type

    @property
    def value(self):
        """
        Gets the value of this LiteralArgument.
        Literal value specified in queryString.


        :return: The value of this LiteralArgument.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this LiteralArgument.
        Literal value specified in queryString.


        :param value: The value of this LiteralArgument.
        :type: object
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
