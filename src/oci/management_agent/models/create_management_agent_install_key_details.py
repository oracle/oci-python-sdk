# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateManagementAgentInstallKeyDetails(object):
    """
    The information about new Management Agent install Key.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateManagementAgentInstallKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateManagementAgentInstallKeyDetails.
        :type display_name: str

        :param allowed_key_install_count:
            The value to assign to the allowed_key_install_count property of this CreateManagementAgentInstallKeyDetails.
        :type allowed_key_install_count: int

        :param time_expires:
            The value to assign to the time_expires property of this CreateManagementAgentInstallKeyDetails.
        :type time_expires: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateManagementAgentInstallKeyDetails.
        :type compartment_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'allowed_key_install_count': 'int',
            'time_expires': 'datetime',
            'compartment_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'allowed_key_install_count': 'allowedKeyInstallCount',
            'time_expires': 'timeExpires',
            'compartment_id': 'compartmentId'
        }

        self._display_name = None
        self._allowed_key_install_count = None
        self._time_expires = None
        self._compartment_id = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateManagementAgentInstallKeyDetails.
        Management Agent install Key Name


        :return: The display_name of this CreateManagementAgentInstallKeyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateManagementAgentInstallKeyDetails.
        Management Agent install Key Name


        :param display_name: The display_name of this CreateManagementAgentInstallKeyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def allowed_key_install_count(self):
        """
        Gets the allowed_key_install_count of this CreateManagementAgentInstallKeyDetails.
        Total number of install for this keys


        :return: The allowed_key_install_count of this CreateManagementAgentInstallKeyDetails.
        :rtype: int
        """
        return self._allowed_key_install_count

    @allowed_key_install_count.setter
    def allowed_key_install_count(self, allowed_key_install_count):
        """
        Sets the allowed_key_install_count of this CreateManagementAgentInstallKeyDetails.
        Total number of install for this keys


        :param allowed_key_install_count: The allowed_key_install_count of this CreateManagementAgentInstallKeyDetails.
        :type: int
        """
        self._allowed_key_install_count = allowed_key_install_count

    @property
    def time_expires(self):
        """
        Gets the time_expires of this CreateManagementAgentInstallKeyDetails.
        date after which key would expire after creation


        :return: The time_expires of this CreateManagementAgentInstallKeyDetails.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this CreateManagementAgentInstallKeyDetails.
        date after which key would expire after creation


        :param time_expires: The time_expires of this CreateManagementAgentInstallKeyDetails.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateManagementAgentInstallKeyDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateManagementAgentInstallKeyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateManagementAgentInstallKeyDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateManagementAgentInstallKeyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
