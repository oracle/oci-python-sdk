# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_column import AbstractColumn
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Column(AbstractColumn):
    """
    Default column object representing querylanguage result columns.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Column object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.Column.type` attribute
        of this class is ``COLUMN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this Column.
            Allowed values for this property are: "COLUMN", "CHART_COLUMN", "CHART_DATA_COLUMN", "TIME_STATS_COLUMN", "TIME_STATS_DATA_COLUMN", "TIME_CLUSTER_COLUMN", "TIME_CLUSTER_DATA_COLUMN", "TIME_COLUMN", "TREND_COLUMN", "CLASSIFY_COLUMN"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this Column.
        :type display_name: str

        :param sub_system:
            The value to assign to the sub_system property of this Column.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        :param values:
            The value to assign to the values property of this Column.
        :type values: list[oci.log_analytics.models.FieldValue]

        :param is_list_of_values:
            The value to assign to the is_list_of_values property of this Column.
        :type is_list_of_values: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this Column.
        :type is_multi_valued: bool

        :param is_case_sensitive:
            The value to assign to the is_case_sensitive property of this Column.
        :type is_case_sensitive: bool

        :param is_groupable:
            The value to assign to the is_groupable property of this Column.
        :type is_groupable: bool

        :param is_evaluable:
            The value to assign to the is_evaluable property of this Column.
        :type is_evaluable: bool

        :param value_type:
            The value to assign to the value_type property of this Column.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"
        :type value_type: str

        :param original_display_name:
            The value to assign to the original_display_name property of this Column.
        :type original_display_name: str

        :param internal_name:
            The value to assign to the internal_name property of this Column.
        :type internal_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'sub_system': 'str',
            'values': 'list[FieldValue]',
            'is_list_of_values': 'bool',
            'is_multi_valued': 'bool',
            'is_case_sensitive': 'bool',
            'is_groupable': 'bool',
            'is_evaluable': 'bool',
            'value_type': 'str',
            'original_display_name': 'str',
            'internal_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'sub_system': 'subSystem',
            'values': 'values',
            'is_list_of_values': 'isListOfValues',
            'is_multi_valued': 'isMultiValued',
            'is_case_sensitive': 'isCaseSensitive',
            'is_groupable': 'isGroupable',
            'is_evaluable': 'isEvaluable',
            'value_type': 'valueType',
            'original_display_name': 'originalDisplayName',
            'internal_name': 'internalName'
        }

        self._type = None
        self._display_name = None
        self._sub_system = None
        self._values = None
        self._is_list_of_values = None
        self._is_multi_valued = None
        self._is_case_sensitive = None
        self._is_groupable = None
        self._is_evaluable = None
        self._value_type = None
        self._original_display_name = None
        self._internal_name = None
        self._type = 'COLUMN'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
