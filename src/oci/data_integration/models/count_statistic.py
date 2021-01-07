# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CountStatistic(object):
    """
    A count statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CountStatistic object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object_type_count_list:
            The value to assign to the object_type_count_list property of this CountStatistic.
        :type object_type_count_list: list[oci.data_integration.models.CountStatisticSummary]

        """
        self.swagger_types = {
            'object_type_count_list': 'list[CountStatisticSummary]'
        }

        self.attribute_map = {
            'object_type_count_list': 'objectTypeCountList'
        }

        self._object_type_count_list = None

    @property
    def object_type_count_list(self):
        """
        **[Required]** Gets the object_type_count_list of this CountStatistic.
        The array of statistics.


        :return: The object_type_count_list of this CountStatistic.
        :rtype: list[oci.data_integration.models.CountStatisticSummary]
        """
        return self._object_type_count_list

    @object_type_count_list.setter
    def object_type_count_list(self, object_type_count_list):
        """
        Sets the object_type_count_list of this CountStatistic.
        The array of statistics.


        :param object_type_count_list: The object_type_count_list of this CountStatistic.
        :type: list[oci.data_integration.models.CountStatisticSummary]
        """
        self._object_type_count_list = object_type_count_list

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
