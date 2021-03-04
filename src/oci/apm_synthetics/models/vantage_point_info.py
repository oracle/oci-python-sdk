# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VantagePointInfo(object):
    """
    Details of the vantage point.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VantagePointInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this VantagePointInfo.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this VantagePointInfo.
        :type display_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName'
        }

        self._name = None
        self._display_name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this VantagePointInfo.
        Name of the vantage point.


        :return: The name of this VantagePointInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VantagePointInfo.
        Name of the vantage point.


        :param name: The name of this VantagePointInfo.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this VantagePointInfo.
        Unique name that can be edited. The name should not contain any confidential information.


        :return: The display_name of this VantagePointInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this VantagePointInfo.
        Unique name that can be edited. The name should not contain any confidential information.


        :param display_name: The display_name of this VantagePointInfo.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
