# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .push_down_operation import PushDownOperation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FilterPush(PushDownOperation):
    """
    The information about a filter operator. The filter operator lets you select certain attributes from the inbound port to continue downstream to the outbound port.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FilterPush object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.FilterPush.model_type` attribute
        of this class is ``FILTER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this FilterPush.
            Allowed values for this property are: "FILTER", "JOIN", "SELECT", "SORT", "QUERY"
        :type model_type: str

        :param filter_condition:
            The value to assign to the filter_condition property of this FilterPush.
        :type filter_condition: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'filter_condition': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'filter_condition': 'filterCondition'
        }

        self._model_type = None
        self._filter_condition = None
        self._model_type = 'FILTER'

    @property
    def filter_condition(self):
        """
        Gets the filter_condition of this FilterPush.
        The filter condition.


        :return: The filter_condition of this FilterPush.
        :rtype: str
        """
        return self._filter_condition

    @filter_condition.setter
    def filter_condition(self, filter_condition):
        """
        Sets the filter_condition of this FilterPush.
        The filter condition.


        :param filter_condition: The filter_condition of this FilterPush.
        :type: str
        """
        self._filter_condition = filter_condition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
