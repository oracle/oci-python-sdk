# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProvisionAuditPolicyDetails(object):
    """
    Details for audit policy provisioning.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProvisionAuditPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_data_safe_service_account_excluded:
            The value to assign to the is_data_safe_service_account_excluded property of this ProvisionAuditPolicyDetails.
        :type is_data_safe_service_account_excluded: bool

        :param provision_audit_conditions:
            The value to assign to the provision_audit_conditions property of this ProvisionAuditPolicyDetails.
        :type provision_audit_conditions: list[oci.data_safe.models.ProvisionAuditConditions]

        """
        self.swagger_types = {
            'is_data_safe_service_account_excluded': 'bool',
            'provision_audit_conditions': 'list[ProvisionAuditConditions]'
        }

        self.attribute_map = {
            'is_data_safe_service_account_excluded': 'isDataSafeServiceAccountExcluded',
            'provision_audit_conditions': 'provisionAuditConditions'
        }

        self._is_data_safe_service_account_excluded = None
        self._provision_audit_conditions = None

    @property
    def is_data_safe_service_account_excluded(self):
        """
        Gets the is_data_safe_service_account_excluded of this ProvisionAuditPolicyDetails.
        Option provided to users at the target to indicate whether the Data Safe service account has to be excluded while provisioning the audit policies.


        :return: The is_data_safe_service_account_excluded of this ProvisionAuditPolicyDetails.
        :rtype: bool
        """
        return self._is_data_safe_service_account_excluded

    @is_data_safe_service_account_excluded.setter
    def is_data_safe_service_account_excluded(self, is_data_safe_service_account_excluded):
        """
        Sets the is_data_safe_service_account_excluded of this ProvisionAuditPolicyDetails.
        Option provided to users at the target to indicate whether the Data Safe service account has to be excluded while provisioning the audit policies.


        :param is_data_safe_service_account_excluded: The is_data_safe_service_account_excluded of this ProvisionAuditPolicyDetails.
        :type: bool
        """
        self._is_data_safe_service_account_excluded = is_data_safe_service_account_excluded

    @property
    def provision_audit_conditions(self):
        """
        **[Required]** Gets the provision_audit_conditions of this ProvisionAuditPolicyDetails.
        The audit policy details for provisioning.


        :return: The provision_audit_conditions of this ProvisionAuditPolicyDetails.
        :rtype: list[oci.data_safe.models.ProvisionAuditConditions]
        """
        return self._provision_audit_conditions

    @provision_audit_conditions.setter
    def provision_audit_conditions(self, provision_audit_conditions):
        """
        Sets the provision_audit_conditions of this ProvisionAuditPolicyDetails.
        The audit policy details for provisioning.


        :param provision_audit_conditions: The provision_audit_conditions of this ProvisionAuditPolicyDetails.
        :type: list[oci.data_safe.models.ProvisionAuditConditions]
        """
        self._provision_audit_conditions = provision_audit_conditions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
