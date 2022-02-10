# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProvisionAuditConditions(object):
    """
    Represents audit policies with corresponding audit provisioning conditions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProvisionAuditConditions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_policy_name:
            The value to assign to the audit_policy_name property of this ProvisionAuditConditions.
        :type audit_policy_name: str

        :param is_priv_users_managed_by_data_safe:
            The value to assign to the is_priv_users_managed_by_data_safe property of this ProvisionAuditConditions.
        :type is_priv_users_managed_by_data_safe: bool

        :param is_enabled:
            The value to assign to the is_enabled property of this ProvisionAuditConditions.
        :type is_enabled: bool

        :param enable_conditions:
            The value to assign to the enable_conditions property of this ProvisionAuditConditions.
        :type enable_conditions: list[oci.data_safe.models.EnableConditions]

        """
        self.swagger_types = {
            'audit_policy_name': 'str',
            'is_priv_users_managed_by_data_safe': 'bool',
            'is_enabled': 'bool',
            'enable_conditions': 'list[EnableConditions]'
        }

        self.attribute_map = {
            'audit_policy_name': 'auditPolicyName',
            'is_priv_users_managed_by_data_safe': 'isPrivUsersManagedByDataSafe',
            'is_enabled': 'isEnabled',
            'enable_conditions': 'enableConditions'
        }

        self._audit_policy_name = None
        self._is_priv_users_managed_by_data_safe = None
        self._is_enabled = None
        self._enable_conditions = None

    @property
    def audit_policy_name(self):
        """
        **[Required]** Gets the audit_policy_name of this ProvisionAuditConditions.
        Indicates the audit policy name available for provisioning from Data Safe. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/audit-policies.html#GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :return: The audit_policy_name of this ProvisionAuditConditions.
        :rtype: str
        """
        return self._audit_policy_name

    @audit_policy_name.setter
    def audit_policy_name(self, audit_policy_name):
        """
        Sets the audit_policy_name of this ProvisionAuditConditions.
        Indicates the audit policy name available for provisioning from Data Safe. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/audit-policies.html#GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :param audit_policy_name: The audit_policy_name of this ProvisionAuditConditions.
        :type: str
        """
        self._audit_policy_name = audit_policy_name

    @property
    def is_priv_users_managed_by_data_safe(self):
        """
        **[Required]** Gets the is_priv_users_managed_by_data_safe of this ProvisionAuditConditions.
        Indicates whether the privileged user list is managed by Data Safe.


        :return: The is_priv_users_managed_by_data_safe of this ProvisionAuditConditions.
        :rtype: bool
        """
        return self._is_priv_users_managed_by_data_safe

    @is_priv_users_managed_by_data_safe.setter
    def is_priv_users_managed_by_data_safe(self, is_priv_users_managed_by_data_safe):
        """
        Sets the is_priv_users_managed_by_data_safe of this ProvisionAuditConditions.
        Indicates whether the privileged user list is managed by Data Safe.


        :param is_priv_users_managed_by_data_safe: The is_priv_users_managed_by_data_safe of this ProvisionAuditConditions.
        :type: bool
        """
        self._is_priv_users_managed_by_data_safe = is_priv_users_managed_by_data_safe

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this ProvisionAuditConditions.
        Indicates whether the policy has to be enabled or disabled in the target database. Set this to true if you want the audit policy to be enabled in the target database. If the seeded audit policy is not already created in the database, the provisioning creates and enables them. If this is set to false, the policy will be disabled in the target database.


        :return: The is_enabled of this ProvisionAuditConditions.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ProvisionAuditConditions.
        Indicates whether the policy has to be enabled or disabled in the target database. Set this to true if you want the audit policy to be enabled in the target database. If the seeded audit policy is not already created in the database, the provisioning creates and enables them. If this is set to false, the policy will be disabled in the target database.


        :param is_enabled: The is_enabled of this ProvisionAuditConditions.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def enable_conditions(self):
        """
        Gets the enable_conditions of this ProvisionAuditConditions.
        Indicates the users/roles in the target database for which the audit policy will be enforced, and the success/failure event condition to generate the audit event.


        :return: The enable_conditions of this ProvisionAuditConditions.
        :rtype: list[oci.data_safe.models.EnableConditions]
        """
        return self._enable_conditions

    @enable_conditions.setter
    def enable_conditions(self, enable_conditions):
        """
        Sets the enable_conditions of this ProvisionAuditConditions.
        Indicates the users/roles in the target database for which the audit policy will be enforced, and the success/failure event condition to generate the audit event.


        :param enable_conditions: The enable_conditions of this ProvisionAuditConditions.
        :type: list[oci.data_safe.models.EnableConditions]
        """
        self._enable_conditions = enable_conditions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
