# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220915


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDbSystemDbInstanceDetails(object):
    """
    Database instance node update parameters.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDbSystemDbInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateDbSystemDbInstanceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateDbSystemDbInstanceDetails.
        :type description: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description'
        }
        self._display_name = None
        self._description = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDbSystemDbInstanceDetails.
        A user-friendly display name of the database instance node. Avoid entering confidential information.


        :return: The display_name of this UpdateDbSystemDbInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDbSystemDbInstanceDetails.
        A user-friendly display name of the database instance node. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateDbSystemDbInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateDbSystemDbInstanceDetails.
        A user-provided description of the database instance node.


        :return: The description of this UpdateDbSystemDbInstanceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDbSystemDbInstanceDetails.
        A user-provided description of the database instance node.


        :param description: The description of this UpdateDbSystemDbInstanceDetails.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
