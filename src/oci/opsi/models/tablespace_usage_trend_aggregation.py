# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TablespaceUsageTrendAggregation(object):
    """
    Usage data per tablespace for a Pluggable database
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TablespaceUsageTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tablespace_name:
            The value to assign to the tablespace_name property of this TablespaceUsageTrendAggregation.
        :type tablespace_name: str

        :param tablespace_type:
            The value to assign to the tablespace_type property of this TablespaceUsageTrendAggregation.
        :type tablespace_type: str

        :param usage_data:
            The value to assign to the usage_data property of this TablespaceUsageTrendAggregation.
        :type usage_data: list[oci.opsi.models.TablespaceUsageTrend]

        """
        self.swagger_types = {
            'tablespace_name': 'str',
            'tablespace_type': 'str',
            'usage_data': 'list[TablespaceUsageTrend]'
        }
        self.attribute_map = {
            'tablespace_name': 'tablespaceName',
            'tablespace_type': 'tablespaceType',
            'usage_data': 'usageData'
        }
        self._tablespace_name = None
        self._tablespace_type = None
        self._usage_data = None

    @property
    def tablespace_name(self):
        """
        **[Required]** Gets the tablespace_name of this TablespaceUsageTrendAggregation.
        The name of tablespace.


        :return: The tablespace_name of this TablespaceUsageTrendAggregation.
        :rtype: str
        """
        return self._tablespace_name

    @tablespace_name.setter
    def tablespace_name(self, tablespace_name):
        """
        Sets the tablespace_name of this TablespaceUsageTrendAggregation.
        The name of tablespace.


        :param tablespace_name: The tablespace_name of this TablespaceUsageTrendAggregation.
        :type: str
        """
        self._tablespace_name = tablespace_name

    @property
    def tablespace_type(self):
        """
        **[Required]** Gets the tablespace_type of this TablespaceUsageTrendAggregation.
        Type of tablespace


        :return: The tablespace_type of this TablespaceUsageTrendAggregation.
        :rtype: str
        """
        return self._tablespace_type

    @tablespace_type.setter
    def tablespace_type(self, tablespace_type):
        """
        Sets the tablespace_type of this TablespaceUsageTrendAggregation.
        Type of tablespace


        :param tablespace_type: The tablespace_type of this TablespaceUsageTrendAggregation.
        :type: str
        """
        self._tablespace_type = tablespace_type

    @property
    def usage_data(self):
        """
        **[Required]** Gets the usage_data of this TablespaceUsageTrendAggregation.
        List of usage data samples for a tablespace


        :return: The usage_data of this TablespaceUsageTrendAggregation.
        :rtype: list[oci.opsi.models.TablespaceUsageTrend]
        """
        return self._usage_data

    @usage_data.setter
    def usage_data(self, usage_data):
        """
        Sets the usage_data of this TablespaceUsageTrendAggregation.
        List of usage data samples for a tablespace


        :param usage_data: The usage_data of this TablespaceUsageTrendAggregation.
        :type: list[oci.opsi.models.TablespaceUsageTrend]
        """
        self._usage_data = usage_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
