# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuditSpecification(object):
    """
    Represents an audit policy relevant for the target database.The audit policy could be in any one of the following 3 states in the target database
    1) Created and enabled
    2) Created but not enabled
    3) Not created
    For more details on relevant audit policies for the target database, refer to `documentation`__.

    __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/audit-policies.html#GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827
    """

    #: A constant which can be used with the audit_policy_category property of a AuditSpecification.
    #: This constant has a value of "BASIC_ACTIVITY"
    AUDIT_POLICY_CATEGORY_BASIC_ACTIVITY = "BASIC_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditSpecification.
    #: This constant has a value of "ADMIN_USER_ACTIVITY"
    AUDIT_POLICY_CATEGORY_ADMIN_USER_ACTIVITY = "ADMIN_USER_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditSpecification.
    #: This constant has a value of "USER_ACTIVITY"
    AUDIT_POLICY_CATEGORY_USER_ACTIVITY = "USER_ACTIVITY"

    #: A constant which can be used with the audit_policy_category property of a AuditSpecification.
    #: This constant has a value of "ORACLE_PREDEFINED"
    AUDIT_POLICY_CATEGORY_ORACLE_PREDEFINED = "ORACLE_PREDEFINED"

    #: A constant which can be used with the audit_policy_category property of a AuditSpecification.
    #: This constant has a value of "COMPLIANCE_STANDARD"
    AUDIT_POLICY_CATEGORY_COMPLIANCE_STANDARD = "COMPLIANCE_STANDARD"

    #: A constant which can be used with the audit_policy_category property of a AuditSpecification.
    #: This constant has a value of "CUSTOM"
    AUDIT_POLICY_CATEGORY_CUSTOM = "CUSTOM"

    #: A constant which can be used with the enable_status property of a AuditSpecification.
    #: This constant has a value of "ENABLED"
    ENABLE_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the enable_status property of a AuditSpecification.
    #: This constant has a value of "DISABLED"
    ENABLE_STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the enable_status property of a AuditSpecification.
    #: This constant has a value of "PARTIALLY_ENABLED"
    ENABLE_STATUS_PARTIALLY_ENABLED = "PARTIALLY_ENABLED"

    #: A constant which can be used with the enabled_entities property of a AuditSpecification.
    #: This constant has a value of "ALL_USERS"
    ENABLED_ENTITIES_ALL_USERS = "ALL_USERS"

    #: A constant which can be used with the enabled_entities property of a AuditSpecification.
    #: This constant has a value of "INCLUDE_USERS"
    ENABLED_ENTITIES_INCLUDE_USERS = "INCLUDE_USERS"

    #: A constant which can be used with the enabled_entities property of a AuditSpecification.
    #: This constant has a value of "INCLUDE_ROLES"
    ENABLED_ENTITIES_INCLUDE_ROLES = "INCLUDE_ROLES"

    #: A constant which can be used with the enabled_entities property of a AuditSpecification.
    #: This constant has a value of "EXCLUDE_USERS"
    ENABLED_ENTITIES_EXCLUDE_USERS = "EXCLUDE_USERS"

    #: A constant which can be used with the enabled_entities property of a AuditSpecification.
    #: This constant has a value of "INCLUDE_USERS_ROLES"
    ENABLED_ENTITIES_INCLUDE_USERS_ROLES = "INCLUDE_USERS_ROLES"

    #: A constant which can be used with the enabled_entities property of a AuditSpecification.
    #: This constant has a value of "DISABLED"
    ENABLED_ENTITIES_DISABLED = "DISABLED"

    def __init__(self, **kwargs):
        """
        Initializes a new AuditSpecification object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audit_policy_name:
            The value to assign to the audit_policy_name property of this AuditSpecification.
        :type audit_policy_name: str

        :param database_policy_names:
            The value to assign to the database_policy_names property of this AuditSpecification.
        :type database_policy_names: list[str]

        :param audit_policy_category:
            The value to assign to the audit_policy_category property of this AuditSpecification.
            Allowed values for this property are: "BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type audit_policy_category: str

        :param enable_status:
            The value to assign to the enable_status property of this AuditSpecification.
            Allowed values for this property are: "ENABLED", "DISABLED", "PARTIALLY_ENABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type enable_status: str

        :param partially_enabled_msg:
            The value to assign to the partially_enabled_msg property of this AuditSpecification.
        :type partially_enabled_msg: str

        :param is_enabled_for_all_users:
            The value to assign to the is_enabled_for_all_users property of this AuditSpecification.
        :type is_enabled_for_all_users: bool

        :param is_view_only:
            The value to assign to the is_view_only property of this AuditSpecification.
        :type is_view_only: bool

        :param is_seeded_in_target:
            The value to assign to the is_seeded_in_target property of this AuditSpecification.
        :type is_seeded_in_target: bool

        :param is_seeded_in_data_safe:
            The value to assign to the is_seeded_in_data_safe property of this AuditSpecification.
        :type is_seeded_in_data_safe: bool

        :param is_created:
            The value to assign to the is_created property of this AuditSpecification.
        :type is_created: bool

        :param enabled_entities:
            The value to assign to the enabled_entities property of this AuditSpecification.
            Allowed values for this property are: "ALL_USERS", "INCLUDE_USERS", "INCLUDE_ROLES", "EXCLUDE_USERS", "INCLUDE_USERS_ROLES", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type enabled_entities: str

        """
        self.swagger_types = {
            'audit_policy_name': 'str',
            'database_policy_names': 'list[str]',
            'audit_policy_category': 'str',
            'enable_status': 'str',
            'partially_enabled_msg': 'str',
            'is_enabled_for_all_users': 'bool',
            'is_view_only': 'bool',
            'is_seeded_in_target': 'bool',
            'is_seeded_in_data_safe': 'bool',
            'is_created': 'bool',
            'enabled_entities': 'str'
        }

        self.attribute_map = {
            'audit_policy_name': 'auditPolicyName',
            'database_policy_names': 'databasePolicyNames',
            'audit_policy_category': 'auditPolicyCategory',
            'enable_status': 'enableStatus',
            'partially_enabled_msg': 'partiallyEnabledMsg',
            'is_enabled_for_all_users': 'isEnabledForAllUsers',
            'is_view_only': 'isViewOnly',
            'is_seeded_in_target': 'isSeededInTarget',
            'is_seeded_in_data_safe': 'isSeededInDataSafe',
            'is_created': 'isCreated',
            'enabled_entities': 'enabledEntities'
        }

        self._audit_policy_name = None
        self._database_policy_names = None
        self._audit_policy_category = None
        self._enable_status = None
        self._partially_enabled_msg = None
        self._is_enabled_for_all_users = None
        self._is_view_only = None
        self._is_seeded_in_target = None
        self._is_seeded_in_data_safe = None
        self._is_created = None
        self._enabled_entities = None

    @property
    def audit_policy_name(self):
        """
        **[Required]** Gets the audit_policy_name of this AuditSpecification.
        Indicates the audit policy name. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/audit-policies.html#GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :return: The audit_policy_name of this AuditSpecification.
        :rtype: str
        """
        return self._audit_policy_name

    @audit_policy_name.setter
    def audit_policy_name(self, audit_policy_name):
        """
        Sets the audit_policy_name of this AuditSpecification.
        Indicates the audit policy name. Refer to the `documentation`__ for seeded audit policy names. For custom policies, refer to the user-defined policy name created in the target database.

        __ https://docs.oracle.com/en/cloud/paas/data-safe/udscs/audit-policies.html#GUID-361A9A9A-7C21-4F5A-8945-9B3A0C472827


        :param audit_policy_name: The audit_policy_name of this AuditSpecification.
        :type: str
        """
        self._audit_policy_name = audit_policy_name

    @property
    def database_policy_names(self):
        """
        **[Required]** Gets the database_policy_names of this AuditSpecification.
        Indicates the names of corresponding database policy ( or policies) in the target database.


        :return: The database_policy_names of this AuditSpecification.
        :rtype: list[str]
        """
        return self._database_policy_names

    @database_policy_names.setter
    def database_policy_names(self, database_policy_names):
        """
        Sets the database_policy_names of this AuditSpecification.
        Indicates the names of corresponding database policy ( or policies) in the target database.


        :param database_policy_names: The database_policy_names of this AuditSpecification.
        :type: list[str]
        """
        self._database_policy_names = database_policy_names

    @property
    def audit_policy_category(self):
        """
        **[Required]** Gets the audit_policy_category of this AuditSpecification.
        The category to which the audit policy belongs.

        Allowed values for this property are: "BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The audit_policy_category of this AuditSpecification.
        :rtype: str
        """
        return self._audit_policy_category

    @audit_policy_category.setter
    def audit_policy_category(self, audit_policy_category):
        """
        Sets the audit_policy_category of this AuditSpecification.
        The category to which the audit policy belongs.


        :param audit_policy_category: The audit_policy_category of this AuditSpecification.
        :type: str
        """
        allowed_values = ["BASIC_ACTIVITY", "ADMIN_USER_ACTIVITY", "USER_ACTIVITY", "ORACLE_PREDEFINED", "COMPLIANCE_STANDARD", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(audit_policy_category, allowed_values):
            audit_policy_category = 'UNKNOWN_ENUM_VALUE'
        self._audit_policy_category = audit_policy_category

    @property
    def enable_status(self):
        """
        **[Required]** Gets the enable_status of this AuditSpecification.
        Indicates whether the policy has been enabled, disabled or partially enabled in the target database. The status is PARTIALLY_ENABLED if any of the constituent database audit policies is not enabled.

        Allowed values for this property are: "ENABLED", "DISABLED", "PARTIALLY_ENABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The enable_status of this AuditSpecification.
        :rtype: str
        """
        return self._enable_status

    @enable_status.setter
    def enable_status(self, enable_status):
        """
        Sets the enable_status of this AuditSpecification.
        Indicates whether the policy has been enabled, disabled or partially enabled in the target database. The status is PARTIALLY_ENABLED if any of the constituent database audit policies is not enabled.


        :param enable_status: The enable_status of this AuditSpecification.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "PARTIALLY_ENABLED"]
        if not value_allowed_none_or_none_sentinel(enable_status, allowed_values):
            enable_status = 'UNKNOWN_ENUM_VALUE'
        self._enable_status = enable_status

    @property
    def partially_enabled_msg(self):
        """
        Gets the partially_enabled_msg of this AuditSpecification.
        Provides information about the policy that has been only partially enabled.


        :return: The partially_enabled_msg of this AuditSpecification.
        :rtype: str
        """
        return self._partially_enabled_msg

    @partially_enabled_msg.setter
    def partially_enabled_msg(self, partially_enabled_msg):
        """
        Sets the partially_enabled_msg of this AuditSpecification.
        Provides information about the policy that has been only partially enabled.


        :param partially_enabled_msg: The partially_enabled_msg of this AuditSpecification.
        :type: str
        """
        self._partially_enabled_msg = partially_enabled_msg

    @property
    def is_enabled_for_all_users(self):
        """
        **[Required]** Gets the is_enabled_for_all_users of this AuditSpecification.
        Indicates whether the policy by default is enabled for all users with no flexibility to alter the enablement conditions.


        :return: The is_enabled_for_all_users of this AuditSpecification.
        :rtype: bool
        """
        return self._is_enabled_for_all_users

    @is_enabled_for_all_users.setter
    def is_enabled_for_all_users(self, is_enabled_for_all_users):
        """
        Sets the is_enabled_for_all_users of this AuditSpecification.
        Indicates whether the policy by default is enabled for all users with no flexibility to alter the enablement conditions.


        :param is_enabled_for_all_users: The is_enabled_for_all_users of this AuditSpecification.
        :type: bool
        """
        self._is_enabled_for_all_users = is_enabled_for_all_users

    @property
    def is_view_only(self):
        """
        **[Required]** Gets the is_view_only of this AuditSpecification.
        Indicates whether the audit policy is available for provisioning/ de-provisioning from Oracle Data Safe, or is only available for displaying the current provisioning status from the target.


        :return: The is_view_only of this AuditSpecification.
        :rtype: bool
        """
        return self._is_view_only

    @is_view_only.setter
    def is_view_only(self, is_view_only):
        """
        Sets the is_view_only of this AuditSpecification.
        Indicates whether the audit policy is available for provisioning/ de-provisioning from Oracle Data Safe, or is only available for displaying the current provisioning status from the target.


        :param is_view_only: The is_view_only of this AuditSpecification.
        :type: bool
        """
        self._is_view_only = is_view_only

    @property
    def is_seeded_in_target(self):
        """
        **[Required]** Gets the is_seeded_in_target of this AuditSpecification.
        Indicates whether the audit policy is one of the predefined policies provided by Oracle Database.


        :return: The is_seeded_in_target of this AuditSpecification.
        :rtype: bool
        """
        return self._is_seeded_in_target

    @is_seeded_in_target.setter
    def is_seeded_in_target(self, is_seeded_in_target):
        """
        Sets the is_seeded_in_target of this AuditSpecification.
        Indicates whether the audit policy is one of the predefined policies provided by Oracle Database.


        :param is_seeded_in_target: The is_seeded_in_target of this AuditSpecification.
        :type: bool
        """
        self._is_seeded_in_target = is_seeded_in_target

    @property
    def is_seeded_in_data_safe(self):
        """
        **[Required]** Gets the is_seeded_in_data_safe of this AuditSpecification.
        Indicates whether the audit policy is one of the seeded policies provided by Oracle Data Safe.


        :return: The is_seeded_in_data_safe of this AuditSpecification.
        :rtype: bool
        """
        return self._is_seeded_in_data_safe

    @is_seeded_in_data_safe.setter
    def is_seeded_in_data_safe(self, is_seeded_in_data_safe):
        """
        Sets the is_seeded_in_data_safe of this AuditSpecification.
        Indicates whether the audit policy is one of the seeded policies provided by Oracle Data Safe.


        :param is_seeded_in_data_safe: The is_seeded_in_data_safe of this AuditSpecification.
        :type: bool
        """
        self._is_seeded_in_data_safe = is_seeded_in_data_safe

    @property
    def is_created(self):
        """
        **[Required]** Gets the is_created of this AuditSpecification.
        Indicates whether the policy is already created on the target database.


        :return: The is_created of this AuditSpecification.
        :rtype: bool
        """
        return self._is_created

    @is_created.setter
    def is_created(self, is_created):
        """
        Sets the is_created of this AuditSpecification.
        Indicates whether the policy is already created on the target database.


        :param is_created: The is_created of this AuditSpecification.
        :type: bool
        """
        self._is_created = is_created

    @property
    def enabled_entities(self):
        """
        **[Required]** Gets the enabled_entities of this AuditSpecification.
        Indicates on whom the audit policy is enabled.

        Allowed values for this property are: "ALL_USERS", "INCLUDE_USERS", "INCLUDE_ROLES", "EXCLUDE_USERS", "INCLUDE_USERS_ROLES", "DISABLED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The enabled_entities of this AuditSpecification.
        :rtype: str
        """
        return self._enabled_entities

    @enabled_entities.setter
    def enabled_entities(self, enabled_entities):
        """
        Sets the enabled_entities of this AuditSpecification.
        Indicates on whom the audit policy is enabled.


        :param enabled_entities: The enabled_entities of this AuditSpecification.
        :type: str
        """
        allowed_values = ["ALL_USERS", "INCLUDE_USERS", "INCLUDE_ROLES", "EXCLUDE_USERS", "INCLUDE_USERS_ROLES", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(enabled_entities, allowed_values):
            enabled_entities = 'UNKNOWN_ENUM_VALUE'
        self._enabled_entities = enabled_entities

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
