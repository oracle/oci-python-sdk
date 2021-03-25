# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpsertLogAnalyticsFieldDetails(object):
    """
    Upsert LogAnalytics Field Details
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpsertLogAnalyticsFieldDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_type:
            The value to assign to the data_type property of this UpsertLogAnalyticsFieldDetails.
        :type data_type: str

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this UpsertLogAnalyticsFieldDetails.
        :type is_multi_valued: bool

        :param description:
            The value to assign to the description property of this UpsertLogAnalyticsFieldDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this UpsertLogAnalyticsFieldDetails.
        :type display_name: str

        :param name:
            The value to assign to the name property of this UpsertLogAnalyticsFieldDetails.
        :type name: str

        """
        self.swagger_types = {
            'data_type': 'str',
            'is_multi_valued': 'bool',
            'description': 'str',
            'display_name': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'data_type': 'dataType',
            'is_multi_valued': 'isMultiValued',
            'description': 'description',
            'display_name': 'displayName',
            'name': 'name'
        }

        self._data_type = None
        self._is_multi_valued = None
        self._description = None
        self._display_name = None
        self._name = None

    @property
    def data_type(self):
        """
        Gets the data_type of this UpsertLogAnalyticsFieldDetails.
        The data type.


        :return: The data_type of this UpsertLogAnalyticsFieldDetails.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this UpsertLogAnalyticsFieldDetails.
        The data type.


        :param data_type: The data_type of this UpsertLogAnalyticsFieldDetails.
        :type: str
        """
        self._data_type = data_type

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this UpsertLogAnalyticsFieldDetails.
        A flag indicating whether or not the field is multi-valued.


        :return: The is_multi_valued of this UpsertLogAnalyticsFieldDetails.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this UpsertLogAnalyticsFieldDetails.
        A flag indicating whether or not the field is multi-valued.


        :param is_multi_valued: The is_multi_valued of this UpsertLogAnalyticsFieldDetails.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def description(self):
        """
        Gets the description of this UpsertLogAnalyticsFieldDetails.
        The field description.


        :return: The description of this UpsertLogAnalyticsFieldDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpsertLogAnalyticsFieldDetails.
        The field description.


        :param description: The description of this UpsertLogAnalyticsFieldDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this UpsertLogAnalyticsFieldDetails.
        The field display name.


        :return: The display_name of this UpsertLogAnalyticsFieldDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpsertLogAnalyticsFieldDetails.
        The field display name.


        :param display_name: The display_name of this UpsertLogAnalyticsFieldDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        Gets the name of this UpsertLogAnalyticsFieldDetails.
        The field internal name.


        :return: The name of this UpsertLogAnalyticsFieldDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpsertLogAnalyticsFieldDetails.
        The field internal name.


        :param name: The name of this UpsertLogAnalyticsFieldDetails.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
