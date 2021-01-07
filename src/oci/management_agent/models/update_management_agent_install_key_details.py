# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateManagementAgentInstallKeyDetails(object):
    """
    Details required to change Management Agent install key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateManagementAgentInstallKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_key_active:
            The value to assign to the is_key_active property of this UpdateManagementAgentInstallKeyDetails.
        :type is_key_active: bool

        :param display_name:
            The value to assign to the display_name property of this UpdateManagementAgentInstallKeyDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'is_key_active': 'bool',
            'display_name': 'str'
        }

        self.attribute_map = {
            'is_key_active': 'isKeyActive',
            'display_name': 'displayName'
        }

        self._is_key_active = None
        self._display_name = None

    @property
    def is_key_active(self):
        """
        Gets the is_key_active of this UpdateManagementAgentInstallKeyDetails.
        if set to true the install key state would be set to Active and if false to Inactive


        :return: The is_key_active of this UpdateManagementAgentInstallKeyDetails.
        :rtype: bool
        """
        return self._is_key_active

    @is_key_active.setter
    def is_key_active(self, is_key_active):
        """
        Sets the is_key_active of this UpdateManagementAgentInstallKeyDetails.
        if set to true the install key state would be set to Active and if false to Inactive


        :param is_key_active: The is_key_active of this UpdateManagementAgentInstallKeyDetails.
        :type: bool
        """
        self._is_key_active = is_key_active

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateManagementAgentInstallKeyDetails.
        New displayName of Agent install key.


        :return: The display_name of this UpdateManagementAgentInstallKeyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateManagementAgentInstallKeyDetails.
        New displayName of Agent install key.


        :param display_name: The display_name of this UpdateManagementAgentInstallKeyDetails.
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
