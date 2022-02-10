# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AlertsAggregationDimension(object):
    """
    Details of aggregation dimension summarizing alerts.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AlertsAggregationDimension object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param group_by:
            The value to assign to the group_by property of this AlertsAggregationDimension.
        :type group_by: dict(str, str)

        """
        self.swagger_types = {
            'group_by': 'dict(str, str)'
        }

        self.attribute_map = {
            'group_by': 'groupBy'
        }

        self._group_by = None

    @property
    def group_by(self):
        """
        **[Required]** Gets the group_by of this AlertsAggregationDimension.
        GroupBy value used in aggregation.


        :return: The group_by of this AlertsAggregationDimension.
        :rtype: dict(str, str)
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """
        Sets the group_by of this AlertsAggregationDimension.
        GroupBy value used in aggregation.


        :param group_by: The group_by of this AlertsAggregationDimension.
        :type: dict(str, str)
        """
        self._group_by = group_by

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
