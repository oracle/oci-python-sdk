# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceInsightProjectedUtilizationItem(object):
    """
    Projected utilization object containing dbid and daysToReach value
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceInsightProjectedUtilizationItem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ResourceInsightProjectedUtilizationItem.
        :type id: str

        :param days_to_reach:
            The value to assign to the days_to_reach property of this ResourceInsightProjectedUtilizationItem.
        :type days_to_reach: int

        """
        self.swagger_types = {
            'id': 'str',
            'days_to_reach': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'days_to_reach': 'daysToReach'
        }

        self._id = None
        self._days_to_reach = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ResourceInsightProjectedUtilizationItem.
        Db id


        :return: The id of this ResourceInsightProjectedUtilizationItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ResourceInsightProjectedUtilizationItem.
        Db id


        :param id: The id of this ResourceInsightProjectedUtilizationItem.
        :type: str
        """
        self._id = id

    @property
    def days_to_reach(self):
        """
        **[Required]** Gets the days_to_reach of this ResourceInsightProjectedUtilizationItem.
        Days to reach projected utilization


        :return: The days_to_reach of this ResourceInsightProjectedUtilizationItem.
        :rtype: int
        """
        return self._days_to_reach

    @days_to_reach.setter
    def days_to_reach(self, days_to_reach):
        """
        Sets the days_to_reach of this ResourceInsightProjectedUtilizationItem.
        Days to reach projected utilization


        :param days_to_reach: The days_to_reach of this ResourceInsightProjectedUtilizationItem.
        :type: int
        """
        self._days_to_reach = days_to_reach

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
