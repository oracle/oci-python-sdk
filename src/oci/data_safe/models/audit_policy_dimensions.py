# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditPolicyDimensions(object):
    """
    Details of aggregation dimensions used for summarizing audit policies.
    """

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "BASIC_ACTIVITY"
    AUDIT_POLICY_CATEGORY_BASIC_ACTIVITY = "BASIC_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "ADMIN_USER_ACTIVITY"
    AUDIT_POLICY_CATEGORY_ADMIN_USER_ACTIVITY = "ADMIN_USER_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "USER_ACTIVITY"
    AUDIT_POLICY_CATEGORY_USER_ACTIVITY = "USER_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "ORACLE_PREDEFINED"
    AUDIT_POLICY_CATEGORY_ORACLE_PREDEFINED = "ORACLE_PREDEFINED"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "COMPLIANCE_STANDARD"
    AUDIT_POLICY_CATEGORY_COMPLIANCE_STANDARD = "COMPLIANCE_STANDARD"

    #: A constant which can be used with the audit_policy_category property of a AuditPolicyDimensions.
    #: This constant has a value of "CUSTOM"
    AUDIT_POLICY_CATEGORY_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditPolicyDimensions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_policy_category:
            The value to assign to the audit_policy_category property of this AuditPolicyDimensions.
            Allowed values for this property are: "BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM"
        :type audit_policy_category: str

        :param audit_policy_name:
            The value to assign to the audit_policy_name property of this AuditPolicyDimensions.
        :type audit_policy_name: str

        """
        self.swagger_types = {
            'audit_policy_category': 'str',
            'audit_policy_name': 'str'
        }

        self.attribute_map = {
            'audit_policy_category': 'auditPolicyCategory',
            'audit_policy_name': 'auditPolicyName'
        }

        self._audit_policy_category = None
        self._audit_policy_name = None

    @property
    def audit_policy_category(self):
        """
        Gets the audit_policy_category of this AuditPolicyDimensions.
        The category to which the audit policy belongs.

        Allowed values for this property are: "BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM"


        :return: The audit_policy_category of this AuditPolicyDimensions.
        :rtype: str
        """
        return self._audit_policy_category

    @audit_policy_category.setter
    def audit_policy_category(self, audit_policy_category):
        """
        Sets the audit_policy_category of this AuditPolicyDimensions.
        The category to which the audit policy belongs.


        :param audit_policy_category: The audit_policy_category of this AuditPolicyDimensions.
        :type: str
        """
        allowed_values = ["BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(audit_policy_category, allowed_values):
            raise ValueError(
                "Invalid value for `audit_policy_category`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._audit_policy_category = audit_policy_category

    @property
    def audit_policy_name(self):
        """
        Gets the audit_policy_name of this AuditPolicyDimensions.
        Indicates the audit policy name. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/audit-policies.html#GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :return: The audit_policy_name of this AuditPolicyDimensions.
        :rtype: str
        """
        return self._audit_policy_name

    @audit_policy_name.setter
    def audit_policy_name(self, audit_policy_name):
        """
        Sets the audit_policy_name of this AuditPolicyDimensions.
        Indicates the audit policy name. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/audit-policies.html#GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :param audit_policy_name: The audit_policy_name of this AuditPolicyDimensions.
        :type: str
        """
        self._audit_policy_name = audit_policy_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
