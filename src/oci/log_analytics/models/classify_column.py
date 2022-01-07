# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_column import AbstractColumn
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ClassifyColumn(AbstractColumn):
    """
    Column containing query results produced by the query language classify command.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ClassifyColumn object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.ClassifyColumn.type` attribute
        of this class is ``CLASSIFY_COLUMN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ClassifyColumn.
            Allowed values for this property are: "COLUMN", "CHART_COLUMN", "CHART_DATA_COLUMN", "TIME_COLUMN", "TREND_COLUMN", "CLASSIFY_COLUMN"
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this ClassifyColumn.
        :type display_name: str

        :param sub_system:
            The value to assign to the sub_system property of this ClassifyColumn.
            Allowed values for this property are: "LOG"
        :type sub_system: str

        :param values:
            The value to assign to the values property of this ClassifyColumn.
        :type values: list[oci.log_analytics.models.FieldValue]

        :param is_list_of_values:
            The value to assign to the is_list_of_values property of this ClassifyColumn.
        :type is_list_of_values: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this ClassifyColumn.
        :type is_multi_valued: bool

        :param is_case_sensitive:
            The value to assign to the is_case_sensitive property of this ClassifyColumn.
        :type is_case_sensitive: bool

        :param is_groupable:
            The value to assign to the is_groupable property of this ClassifyColumn.
        :type is_groupable: bool

        :param is_evaluable:
            The value to assign to the is_evaluable property of this ClassifyColumn.
        :type is_evaluable: bool

        :param value_type:
            The value to assign to the value_type property of this ClassifyColumn.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"
        :type value_type: str

        :param original_display_name:
            The value to assign to the original_display_name property of this ClassifyColumn.
        :type original_display_name: str

        :param internal_name:
            The value to assign to the internal_name property of this ClassifyColumn.
        :type internal_name: str

        :param classify_field_names:
            The value to assign to the classify_field_names property of this ClassifyColumn.
        :type classify_field_names: list[str]

        :param classify_field_null_count:
            The value to assign to the classify_field_null_count property of this ClassifyColumn.
        :type classify_field_null_count: list[int]

        :param classify_anomaly_interval_counts:
            The value to assign to the classify_anomaly_interval_counts property of this ClassifyColumn.
        :type classify_anomaly_interval_counts: list[int]

        :param classify_columns:
            The value to assign to the classify_columns property of this ClassifyColumn.
        :type classify_columns: list[oci.log_analytics.models.AbstractColumn]

        :param classify_result:
            The value to assign to the classify_result property of this ClassifyColumn.
        :type classify_result: list[dict(str, object)]

        :param classify_correlate_columns:
            The value to assign to the classify_correlate_columns property of this ClassifyColumn.
        :type classify_correlate_columns: list[oci.log_analytics.models.AbstractColumn]

        :param classify_correlate_result:
            The value to assign to the classify_correlate_result property of this ClassifyColumn.
        :type classify_correlate_result: list[dict(str, object)]

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
            'internal_name': 'str',
            'classify_field_names': 'list[str]',
            'classify_field_null_count': 'list[int]',
            'classify_anomaly_interval_counts': 'list[int]',
            'classify_columns': 'list[AbstractColumn]',
            'classify_result': 'list[dict(str, object)]',
            'classify_correlate_columns': 'list[AbstractColumn]',
            'classify_correlate_result': 'list[dict(str, object)]'
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
            'internal_name': 'internalName',
            'classify_field_names': 'classifyFieldNames',
            'classify_field_null_count': 'classifyFieldNullCount',
            'classify_anomaly_interval_counts': 'classifyAnomalyIntervalCounts',
            'classify_columns': 'classifyColumns',
            'classify_result': 'classifyResult',
            'classify_correlate_columns': 'classifyCorrelateColumns',
            'classify_correlate_result': 'classifyCorrelateResult'
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
        self._classify_field_names = None
        self._classify_field_null_count = None
        self._classify_anomaly_interval_counts = None
        self._classify_columns = None
        self._classify_result = None
        self._classify_correlate_columns = None
        self._classify_correlate_result = None
        self._type = 'CLASSIFY_COLUMN'

    @property
    def classify_field_names(self):
        """
        Gets the classify_field_names of this ClassifyColumn.
        A list of fields specified in the classify command in the query string.


        :return: The classify_field_names of this ClassifyColumn.
        :rtype: list[str]
        """
        return self._classify_field_names

    @classify_field_names.setter
    def classify_field_names(self, classify_field_names):
        """
        Sets the classify_field_names of this ClassifyColumn.
        A list of fields specified in the classify command in the query string.


        :param classify_field_names: The classify_field_names of this ClassifyColumn.
        :type: list[str]
        """
        self._classify_field_names = classify_field_names

    @property
    def classify_field_null_count(self):
        """
        Gets the classify_field_null_count of this ClassifyColumn.
        Count of nulls found in each of the fields specified in the classify command in the query string.


        :return: The classify_field_null_count of this ClassifyColumn.
        :rtype: list[int]
        """
        return self._classify_field_null_count

    @classify_field_null_count.setter
    def classify_field_null_count(self, classify_field_null_count):
        """
        Sets the classify_field_null_count of this ClassifyColumn.
        Count of nulls found in each of the fields specified in the classify command in the query string.


        :param classify_field_null_count: The classify_field_null_count of this ClassifyColumn.
        :type: list[int]
        """
        self._classify_field_null_count = classify_field_null_count

    @property
    def classify_anomaly_interval_counts(self):
        """
        Gets the classify_anomaly_interval_counts of this ClassifyColumn.
        Count of anomalies for each timeseries datapoint.


        :return: The classify_anomaly_interval_counts of this ClassifyColumn.
        :rtype: list[int]
        """
        return self._classify_anomaly_interval_counts

    @classify_anomaly_interval_counts.setter
    def classify_anomaly_interval_counts(self, classify_anomaly_interval_counts):
        """
        Sets the classify_anomaly_interval_counts of this ClassifyColumn.
        Count of anomalies for each timeseries datapoint.


        :param classify_anomaly_interval_counts: The classify_anomaly_interval_counts of this ClassifyColumn.
        :type: list[int]
        """
        self._classify_anomaly_interval_counts = classify_anomaly_interval_counts

    @property
    def classify_columns(self):
        """
        Gets the classify_columns of this ClassifyColumn.
        Column descriptors for the classify result.


        :return: The classify_columns of this ClassifyColumn.
        :rtype: list[oci.log_analytics.models.AbstractColumn]
        """
        return self._classify_columns

    @classify_columns.setter
    def classify_columns(self, classify_columns):
        """
        Sets the classify_columns of this ClassifyColumn.
        Column descriptors for the classify result.


        :param classify_columns: The classify_columns of this ClassifyColumn.
        :type: list[oci.log_analytics.models.AbstractColumn]
        """
        self._classify_columns = classify_columns

    @property
    def classify_result(self):
        """
        Gets the classify_result of this ClassifyColumn.
        Results of the classify command.


        :return: The classify_result of this ClassifyColumn.
        :rtype: list[dict(str, object)]
        """
        return self._classify_result

    @classify_result.setter
    def classify_result(self, classify_result):
        """
        Sets the classify_result of this ClassifyColumn.
        Results of the classify command.


        :param classify_result: The classify_result of this ClassifyColumn.
        :type: list[dict(str, object)]
        """
        self._classify_result = classify_result

    @property
    def classify_correlate_columns(self):
        """
        Gets the classify_correlate_columns of this ClassifyColumn.
        Column descriptors of fields with strong correlation with the classify fields.


        :return: The classify_correlate_columns of this ClassifyColumn.
        :rtype: list[oci.log_analytics.models.AbstractColumn]
        """
        return self._classify_correlate_columns

    @classify_correlate_columns.setter
    def classify_correlate_columns(self, classify_correlate_columns):
        """
        Sets the classify_correlate_columns of this ClassifyColumn.
        Column descriptors of fields with strong correlation with the classify fields.


        :param classify_correlate_columns: The classify_correlate_columns of this ClassifyColumn.
        :type: list[oci.log_analytics.models.AbstractColumn]
        """
        self._classify_correlate_columns = classify_correlate_columns

    @property
    def classify_correlate_result(self):
        """
        Gets the classify_correlate_result of this ClassifyColumn.
        Correlation results of the classify command.


        :return: The classify_correlate_result of this ClassifyColumn.
        :rtype: list[dict(str, object)]
        """
        return self._classify_correlate_result

    @classify_correlate_result.setter
    def classify_correlate_result(self, classify_correlate_result):
        """
        Sets the classify_correlate_result of this ClassifyColumn.
        Correlation results of the classify command.


        :param classify_correlate_result: The classify_correlate_result of this ClassifyColumn.
        :type: list[dict(str, object)]
        """
        self._classify_correlate_result = classify_correlate_result

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
