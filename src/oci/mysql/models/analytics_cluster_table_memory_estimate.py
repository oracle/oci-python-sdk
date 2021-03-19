# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnalyticsClusterTableMemoryEstimate(object):
    """
    DEPRECATED -- please use HeatWave API instead.
    Estimated memory footprint for a MySQL user table
    when loaded to the Analytics Cluster memory.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnalyticsClusterTableMemoryEstimate object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param table_name:
            The value to assign to the table_name property of this AnalyticsClusterTableMemoryEstimate.
        :type table_name: str

        :param to_load_column_count:
            The value to assign to the to_load_column_count property of this AnalyticsClusterTableMemoryEstimate.
        :type to_load_column_count: int

        :param varlen_column_count:
            The value to assign to the varlen_column_count property of this AnalyticsClusterTableMemoryEstimate.
        :type varlen_column_count: int

        :param estimated_row_count:
            The value to assign to the estimated_row_count property of this AnalyticsClusterTableMemoryEstimate.
        :type estimated_row_count: int

        :param analytical_footprint_in_mbs:
            The value to assign to the analytical_footprint_in_mbs property of this AnalyticsClusterTableMemoryEstimate.
        :type analytical_footprint_in_mbs: int

        :param error_comment:
            The value to assign to the error_comment property of this AnalyticsClusterTableMemoryEstimate.
        :type error_comment: str

        """
        self.swagger_types = {
            'table_name': 'str',
            'to_load_column_count': 'int',
            'varlen_column_count': 'int',
            'estimated_row_count': 'int',
            'analytical_footprint_in_mbs': 'int',
            'error_comment': 'str'
        }

        self.attribute_map = {
            'table_name': 'tableName',
            'to_load_column_count': 'toLoadColumnCount',
            'varlen_column_count': 'varlenColumnCount',
            'estimated_row_count': 'estimatedRowCount',
            'analytical_footprint_in_mbs': 'analyticalFootprintInMbs',
            'error_comment': 'errorComment'
        }

        self._table_name = None
        self._to_load_column_count = None
        self._varlen_column_count = None
        self._estimated_row_count = None
        self._analytical_footprint_in_mbs = None
        self._error_comment = None

    @property
    def table_name(self):
        """
        **[Required]** Gets the table_name of this AnalyticsClusterTableMemoryEstimate.
        The table name.


        :return: The table_name of this AnalyticsClusterTableMemoryEstimate.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """
        Sets the table_name of this AnalyticsClusterTableMemoryEstimate.
        The table name.


        :param table_name: The table_name of this AnalyticsClusterTableMemoryEstimate.
        :type: str
        """
        self._table_name = table_name

    @property
    def to_load_column_count(self):
        """
        **[Required]** Gets the to_load_column_count of this AnalyticsClusterTableMemoryEstimate.
        The number of columns to be loaded to Analytics Cluster memory.
        These columns contribute to the analytical memory footprint.


        :return: The to_load_column_count of this AnalyticsClusterTableMemoryEstimate.
        :rtype: int
        """
        return self._to_load_column_count

    @to_load_column_count.setter
    def to_load_column_count(self, to_load_column_count):
        """
        Sets the to_load_column_count of this AnalyticsClusterTableMemoryEstimate.
        The number of columns to be loaded to Analytics Cluster memory.
        These columns contribute to the analytical memory footprint.


        :param to_load_column_count: The to_load_column_count of this AnalyticsClusterTableMemoryEstimate.
        :type: int
        """
        self._to_load_column_count = to_load_column_count

    @property
    def varlen_column_count(self):
        """
        **[Required]** Gets the varlen_column_count of this AnalyticsClusterTableMemoryEstimate.
        The number of variable-length columns to be loaded to Analytics Cluster memory.
        These columns contribute to the analytical memory footprint.


        :return: The varlen_column_count of this AnalyticsClusterTableMemoryEstimate.
        :rtype: int
        """
        return self._varlen_column_count

    @varlen_column_count.setter
    def varlen_column_count(self, varlen_column_count):
        """
        Sets the varlen_column_count of this AnalyticsClusterTableMemoryEstimate.
        The number of variable-length columns to be loaded to Analytics Cluster memory.
        These columns contribute to the analytical memory footprint.


        :param varlen_column_count: The varlen_column_count of this AnalyticsClusterTableMemoryEstimate.
        :type: int
        """
        self._varlen_column_count = varlen_column_count

    @property
    def estimated_row_count(self):
        """
        **[Required]** Gets the estimated_row_count of this AnalyticsClusterTableMemoryEstimate.
        The estimated number of rows in the table. This number was used to
        derive the analytical memory footprint.


        :return: The estimated_row_count of this AnalyticsClusterTableMemoryEstimate.
        :rtype: int
        """
        return self._estimated_row_count

    @estimated_row_count.setter
    def estimated_row_count(self, estimated_row_count):
        """
        Sets the estimated_row_count of this AnalyticsClusterTableMemoryEstimate.
        The estimated number of rows in the table. This number was used to
        derive the analytical memory footprint.


        :param estimated_row_count: The estimated_row_count of this AnalyticsClusterTableMemoryEstimate.
        :type: int
        """
        self._estimated_row_count = estimated_row_count

    @property
    def analytical_footprint_in_mbs(self):
        """
        **[Required]** Gets the analytical_footprint_in_mbs of this AnalyticsClusterTableMemoryEstimate.
        The estimated memory footprint of the table in MBs when loaded to
        Analytics Cluster memory (null if the table cannot be loaded to the
        Analytics Cluster).


        :return: The analytical_footprint_in_mbs of this AnalyticsClusterTableMemoryEstimate.
        :rtype: int
        """
        return self._analytical_footprint_in_mbs

    @analytical_footprint_in_mbs.setter
    def analytical_footprint_in_mbs(self, analytical_footprint_in_mbs):
        """
        Sets the analytical_footprint_in_mbs of this AnalyticsClusterTableMemoryEstimate.
        The estimated memory footprint of the table in MBs when loaded to
        Analytics Cluster memory (null if the table cannot be loaded to the
        Analytics Cluster).


        :param analytical_footprint_in_mbs: The analytical_footprint_in_mbs of this AnalyticsClusterTableMemoryEstimate.
        :type: int
        """
        self._analytical_footprint_in_mbs = analytical_footprint_in_mbs

    @property
    def error_comment(self):
        """
        **[Required]** Gets the error_comment of this AnalyticsClusterTableMemoryEstimate.
        Error comment (empty string if no errors occured).


        :return: The error_comment of this AnalyticsClusterTableMemoryEstimate.
        :rtype: str
        """
        return self._error_comment

    @error_comment.setter
    def error_comment(self, error_comment):
        """
        Sets the error_comment of this AnalyticsClusterTableMemoryEstimate.
        Error comment (empty string if no errors occured).


        :param error_comment: The error_comment of this AnalyticsClusterTableMemoryEstimate.
        :type: str
        """
        self._error_comment = error_comment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
