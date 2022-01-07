# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsLabelOperator(object):
    """
    LogAnalyticsLabelOperator
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsLabelOperator object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsLabelOperator.
        :type display_name: str

        :param name:
            The value to assign to the name property of this LogAnalyticsLabelOperator.
        :type name: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name'
        }

        self._display_name = None
        self._name = None

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsLabelOperator.
        The operator display name.


        :return: The display_name of this LogAnalyticsLabelOperator.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsLabelOperator.
        The operator display name.


        :param display_name: The display_name of this LogAnalyticsLabelOperator.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        Gets the name of this LogAnalyticsLabelOperator.
        The operator internal name.


        :return: The name of this LogAnalyticsLabelOperator.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsLabelOperator.
        The operator internal name.


        :param name: The name of this LogAnalyticsLabelOperator.
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
