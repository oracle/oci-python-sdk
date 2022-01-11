# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceUsageSummary(object):
    """
    Contains resource usage summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceUsageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param exadata_insight_id:
            The value to assign to the exadata_insight_id property of this ResourceUsageSummary.
        :type exadata_insight_id: str

        :param usage:
            The value to assign to the usage property of this ResourceUsageSummary.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this ResourceUsageSummary.
        :type capacity: float

        :param utilization_percent:
            The value to assign to the utilization_percent property of this ResourceUsageSummary.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this ResourceUsageSummary.
        :type usage_change_percent: float

        """
        self.swagger_types = {
            'exadata_insight_id': 'str',
            'usage': 'float',
            'capacity': 'float',
            'utilization_percent': 'float',
            'usage_change_percent': 'float'
        }

        self.attribute_map = {
            'exadata_insight_id': 'exadataInsightId',
            'usage': 'usage',
            'capacity': 'capacity',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent'
        }

        self._exadata_insight_id = None
        self._usage = None
        self._capacity = None
        self._utilization_percent = None
        self._usage_change_percent = None

    @property
    def exadata_insight_id(self):
        """
        **[Required]** Gets the exadata_insight_id of this ResourceUsageSummary.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The exadata_insight_id of this ResourceUsageSummary.
        :rtype: str
        """
        return self._exadata_insight_id

    @exadata_insight_id.setter
    def exadata_insight_id(self, exadata_insight_id):
        """
        Sets the exadata_insight_id of this ResourceUsageSummary.
        The `OCID`__ of the Exadata insight.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param exadata_insight_id: The exadata_insight_id of this ResourceUsageSummary.
        :type: str
        """
        self._exadata_insight_id = exadata_insight_id

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this ResourceUsageSummary.
        Total amount used of the resource metric type (CPU, STORAGE).


        :return: The usage of this ResourceUsageSummary.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this ResourceUsageSummary.
        Total amount used of the resource metric type (CPU, STORAGE).


        :param usage: The usage of this ResourceUsageSummary.
        :type: float
        """
        self._usage = usage

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this ResourceUsageSummary.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :return: The capacity of this ResourceUsageSummary.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this ResourceUsageSummary.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :param capacity: The capacity of this ResourceUsageSummary.
        :type: float
        """
        self._capacity = capacity

    @property
    def utilization_percent(self):
        """
        **[Required]** Gets the utilization_percent of this ResourceUsageSummary.
        Resource utilization in percentage


        :return: The utilization_percent of this ResourceUsageSummary.
        :rtype: float
        """
        return self._utilization_percent

    @utilization_percent.setter
    def utilization_percent(self, utilization_percent):
        """
        Sets the utilization_percent of this ResourceUsageSummary.
        Resource utilization in percentage


        :param utilization_percent: The utilization_percent of this ResourceUsageSummary.
        :type: float
        """
        self._utilization_percent = utilization_percent

    @property
    def usage_change_percent(self):
        """
        **[Required]** Gets the usage_change_percent of this ResourceUsageSummary.
        Change in resource utilization in percentage


        :return: The usage_change_percent of this ResourceUsageSummary.
        :rtype: float
        """
        return self._usage_change_percent

    @usage_change_percent.setter
    def usage_change_percent(self, usage_change_percent):
        """
        Sets the usage_change_percent of this ResourceUsageSummary.
        Change in resource utilization in percentage


        :param usage_change_percent: The usage_change_percent of this ResourceUsageSummary.
        :type: float
        """
        self._usage_change_percent = usage_change_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
