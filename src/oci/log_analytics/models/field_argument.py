# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .argument import Argument
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FieldArgument(Argument):
    """
    QueryString argument of type field.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FieldArgument object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.FieldArgument.type` attribute
        of this class is ``FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this FieldArgument.
            Allowed values for this property are: "FIELD", "LITERAL"
        :type type: str

        :param value:
            The value to assign to the value property of this FieldArgument.
        :type value: oci.log_analytics.models.AbstractField

        """
        self.swagger_types = {
            'type': 'str',
            'value': 'AbstractField'
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = None
        self._value = None
        self._type = 'FIELD'

    @property
    def value(self):
        """
        Gets the value of this FieldArgument.

        :return: The value of this FieldArgument.
        :rtype: oci.log_analytics.models.AbstractField
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this FieldArgument.

        :param value: The value of this FieldArgument.
        :type: oci.log_analytics.models.AbstractField
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
