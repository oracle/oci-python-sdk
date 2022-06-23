# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .security_action import SecurityAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DeniedSecurityAction(SecurityAction):
    """
    Defines the security action taken on denied traffic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DeniedSecurityAction object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.DeniedSecurityAction.action` attribute
        of this class is ``DENIED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this DeniedSecurityAction.
            Allowed values for this property are: "ALLOWED", "DENIED"
        :type action: str

        :param action_type:
            The value to assign to the action_type property of this DeniedSecurityAction.
            Allowed values for this property are: "EXPLICIT", "IMPLICIT"
        :type action_type: str

        :param denied_security_action_details:
            The value to assign to the denied_security_action_details property of this DeniedSecurityAction.
        :type denied_security_action_details: oci.vn_monitoring.models.DeniedSecurityActionDetails

        """
        self.swagger_types = {
            'action': 'str',
            'action_type': 'str',
            'denied_security_action_details': 'DeniedSecurityActionDetails'
        }

        self.attribute_map = {
            'action': 'action',
            'action_type': 'actionType',
            'denied_security_action_details': 'deniedSecurityActionDetails'
        }

        self._action = None
        self._action_type = None
        self._denied_security_action_details = None
        self._action = 'DENIED'

    @property
    def denied_security_action_details(self):
        """
        Gets the denied_security_action_details of this DeniedSecurityAction.

        :return: The denied_security_action_details of this DeniedSecurityAction.
        :rtype: oci.vn_monitoring.models.DeniedSecurityActionDetails
        """
        return self._denied_security_action_details

    @denied_security_action_details.setter
    def denied_security_action_details(self, denied_security_action_details):
        """
        Sets the denied_security_action_details of this DeniedSecurityAction.

        :param denied_security_action_details: The denied_security_action_details of this DeniedSecurityAction.
        :type: oci.vn_monitoring.models.DeniedSecurityActionDetails
        """
        self._denied_security_action_details = denied_security_action_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
