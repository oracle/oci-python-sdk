# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .security_action import SecurityAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedSecurityAction(SecurityAction):
    """
    Defines the security action taken on allowed traffic.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedSecurityAction object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.AllowedSecurityAction.action` attribute
        of this class is ``ALLOWED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this AllowedSecurityAction.
            Allowed values for this property are: "ALLOWED", "DENIED"
        :type action: str

        :param action_type:
            The value to assign to the action_type property of this AllowedSecurityAction.
            Allowed values for this property are: "EXPLICIT", "IMPLICIT"
        :type action_type: str

        :param allowed_security_action_details:
            The value to assign to the allowed_security_action_details property of this AllowedSecurityAction.
        :type allowed_security_action_details: oci.vn_monitoring.models.AllowedSecurityActionDetails

        """
        self.swagger_types = {
            'action': 'str',
            'action_type': 'str',
            'allowed_security_action_details': 'AllowedSecurityActionDetails'
        }

        self.attribute_map = {
            'action': 'action',
            'action_type': 'actionType',
            'allowed_security_action_details': 'allowedSecurityActionDetails'
        }

        self._action = None
        self._action_type = None
        self._allowed_security_action_details = None
        self._action = 'ALLOWED'

    @property
    def allowed_security_action_details(self):
        """
        Gets the allowed_security_action_details of this AllowedSecurityAction.

        :return: The allowed_security_action_details of this AllowedSecurityAction.
        :rtype: oci.vn_monitoring.models.AllowedSecurityActionDetails
        """
        return self._allowed_security_action_details

    @allowed_security_action_details.setter
    def allowed_security_action_details(self, allowed_security_action_details):
        """
        Sets the allowed_security_action_details of this AllowedSecurityAction.

        :param allowed_security_action_details: The allowed_security_action_details of this AllowedSecurityAction.
        :type: oci.vn_monitoring.models.AllowedSecurityActionDetails
        """
        self._allowed_security_action_details = allowed_security_action_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
