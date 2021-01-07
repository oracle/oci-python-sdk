# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScopeFilter(object):
    """
    Scope filter to reduce the scope of the query.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScopeFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_name:
            The value to assign to the field_name property of this ScopeFilter.
        :type field_name: str

        :param values:
            The value to assign to the values property of this ScopeFilter.
        :type values: list[object]

        """
        self.swagger_types = {
            'field_name': 'str',
            'values': 'list[object]'
        }

        self.attribute_map = {
            'field_name': 'fieldName',
            'values': 'values'
        }

        self._field_name = None
        self._values = None

    @property
    def field_name(self):
        """
        **[Required]** Gets the field_name of this ScopeFilter.
        Field must be a valid logging-analytics out-of-the-box field.


        :return: The field_name of this ScopeFilter.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this ScopeFilter.
        Field must be a valid logging-analytics out-of-the-box field.


        :param field_name: The field_name of this ScopeFilter.
        :type: str
        """
        self._field_name = field_name

    @property
    def values(self):
        """
        **[Required]** Gets the values of this ScopeFilter.
        Field values that will be used to filter the query scope. Please note all values should reflect the fields data type otherwise the query is subject to fail.


        :return: The values of this ScopeFilter.
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this ScopeFilter.
        Field values that will be used to filter the query scope. Please note all values should reflect the fields data type otherwise the query is subject to fail.


        :param values: The values of this ScopeFilter.
        :type: list[object]
        """
        self._values = values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
