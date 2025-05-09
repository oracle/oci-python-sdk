# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrProtectionGroupRoleDetails(object):
    """
    The details for updating the role of a DR protection group.
    """

    #: A constant which can be used with the role property of a UpdateDrProtectionGroupRoleDetails.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a UpdateDrProtectionGroupRoleDetails.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a UpdateDrProtectionGroupRoleDetails.
    #: This constant has a value of "UNCONFIGURED"
    ROLE_UNCONFIGURED = "UNCONFIGURED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrProtectionGroupRoleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param role:
            The value to assign to the role property of this UpdateDrProtectionGroupRoleDetails.
            Allowed values for this property are: "PRIMARY", "STANDBY", "UNCONFIGURED"
        :type role: str

        """
        self.swagger_types = {
            'role': 'str'
        }
        self.attribute_map = {
            'role': 'role'
        }
        self._role = None

    @property
    def role(self):
        """
        **[Required]** Gets the role of this UpdateDrProtectionGroupRoleDetails.
        The new role of the DR protection group.

        Allowed values for this property are: "PRIMARY", "STANDBY", "UNCONFIGURED"


        :return: The role of this UpdateDrProtectionGroupRoleDetails.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this UpdateDrProtectionGroupRoleDetails.
        The new role of the DR protection group.


        :param role: The role of this UpdateDrProtectionGroupRoleDetails.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "UNCONFIGURED"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            raise ValueError(
                f"Invalid value for `role`, must be None or one of {allowed_values}"
            )
        self._role = role

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
