# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SectionStatistics(object):
    """
    Statistics showing the number of findings with a particular risk level for each category.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SectionStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param targets_count:
            The value to assign to the targets_count property of this SectionStatistics.
        :type targets_count: int

        :param auditing_findings_count:
            The value to assign to the auditing_findings_count property of this SectionStatistics.
        :type auditing_findings_count: int

        :param authorization_control_findings_count:
            The value to assign to the authorization_control_findings_count property of this SectionStatistics.
        :type authorization_control_findings_count: int

        :param data_encryption_findings_count:
            The value to assign to the data_encryption_findings_count property of this SectionStatistics.
        :type data_encryption_findings_count: int

        :param db_configuration_findings_count:
            The value to assign to the db_configuration_findings_count property of this SectionStatistics.
        :type db_configuration_findings_count: int

        :param fine_grained_access_control_findings_count:
            The value to assign to the fine_grained_access_control_findings_count property of this SectionStatistics.
        :type fine_grained_access_control_findings_count: int

        :param privileges_and_roles_findings_count:
            The value to assign to the privileges_and_roles_findings_count property of this SectionStatistics.
        :type privileges_and_roles_findings_count: int

        :param user_accounts_findings_count:
            The value to assign to the user_accounts_findings_count property of this SectionStatistics.
        :type user_accounts_findings_count: int

        """
        self.swagger_types = {
            'targets_count': 'int',
            'auditing_findings_count': 'int',
            'authorization_control_findings_count': 'int',
            'data_encryption_findings_count': 'int',
            'db_configuration_findings_count': 'int',
            'fine_grained_access_control_findings_count': 'int',
            'privileges_and_roles_findings_count': 'int',
            'user_accounts_findings_count': 'int'
        }

        self.attribute_map = {
            'targets_count': 'targetsCount',
            'auditing_findings_count': 'auditingFindingsCount',
            'authorization_control_findings_count': 'authorizationControlFindingsCount',
            'data_encryption_findings_count': 'dataEncryptionFindingsCount',
            'db_configuration_findings_count': 'dbConfigurationFindingsCount',
            'fine_grained_access_control_findings_count': 'fineGrainedAccessControlFindingsCount',
            'privileges_and_roles_findings_count': 'privilegesAndRolesFindingsCount',
            'user_accounts_findings_count': 'userAccountsFindingsCount'
        }

        self._targets_count = None
        self._auditing_findings_count = None
        self._authorization_control_findings_count = None
        self._data_encryption_findings_count = None
        self._db_configuration_findings_count = None
        self._fine_grained_access_control_findings_count = None
        self._privileges_and_roles_findings_count = None
        self._user_accounts_findings_count = None

    @property
    def targets_count(self):
        """
        Gets the targets_count of this SectionStatistics.
        The number of targets that contributed to the counts at this risk level.


        :return: The targets_count of this SectionStatistics.
        :rtype: int
        """
        return self._targets_count

    @targets_count.setter
    def targets_count(self, targets_count):
        """
        Sets the targets_count of this SectionStatistics.
        The number of targets that contributed to the counts at this risk level.


        :param targets_count: The targets_count of this SectionStatistics.
        :type: int
        """
        self._targets_count = targets_count

    @property
    def auditing_findings_count(self):
        """
        Gets the auditing_findings_count of this SectionStatistics.
        The number of findings in the Auditing category.


        :return: The auditing_findings_count of this SectionStatistics.
        :rtype: int
        """
        return self._auditing_findings_count

    @auditing_findings_count.setter
    def auditing_findings_count(self, auditing_findings_count):
        """
        Sets the auditing_findings_count of this SectionStatistics.
        The number of findings in the Auditing category.


        :param auditing_findings_count: The auditing_findings_count of this SectionStatistics.
        :type: int
        """
        self._auditing_findings_count = auditing_findings_count

    @property
    def authorization_control_findings_count(self):
        """
        Gets the authorization_control_findings_count of this SectionStatistics.
        The number of findings in the Authorization Control category.


        :return: The authorization_control_findings_count of this SectionStatistics.
        :rtype: int
        """
        return self._authorization_control_findings_count

    @authorization_control_findings_count.setter
    def authorization_control_findings_count(self, authorization_control_findings_count):
        """
        Sets the authorization_control_findings_count of this SectionStatistics.
        The number of findings in the Authorization Control category.


        :param authorization_control_findings_count: The authorization_control_findings_count of this SectionStatistics.
        :type: int
        """
        self._authorization_control_findings_count = authorization_control_findings_count

    @property
    def data_encryption_findings_count(self):
        """
        Gets the data_encryption_findings_count of this SectionStatistics.
        The number of findings in the Data Encryption category.


        :return: The data_encryption_findings_count of this SectionStatistics.
        :rtype: int
        """
        return self._data_encryption_findings_count

    @data_encryption_findings_count.setter
    def data_encryption_findings_count(self, data_encryption_findings_count):
        """
        Sets the data_encryption_findings_count of this SectionStatistics.
        The number of findings in the Data Encryption category.


        :param data_encryption_findings_count: The data_encryption_findings_count of this SectionStatistics.
        :type: int
        """
        self._data_encryption_findings_count = data_encryption_findings_count

    @property
    def db_configuration_findings_count(self):
        """
        Gets the db_configuration_findings_count of this SectionStatistics.
        The number of findings in the Database Configuration category.


        :return: The db_configuration_findings_count of this SectionStatistics.
        :rtype: int
        """
        return self._db_configuration_findings_count

    @db_configuration_findings_count.setter
    def db_configuration_findings_count(self, db_configuration_findings_count):
        """
        Sets the db_configuration_findings_count of this SectionStatistics.
        The number of findings in the Database Configuration category.


        :param db_configuration_findings_count: The db_configuration_findings_count of this SectionStatistics.
        :type: int
        """
        self._db_configuration_findings_count = db_configuration_findings_count

    @property
    def fine_grained_access_control_findings_count(self):
        """
        Gets the fine_grained_access_control_findings_count of this SectionStatistics.
        The number of findings in the Fine-Grained Access Control category.


        :return: The fine_grained_access_control_findings_count of this SectionStatistics.
        :rtype: int
        """
        return self._fine_grained_access_control_findings_count

    @fine_grained_access_control_findings_count.setter
    def fine_grained_access_control_findings_count(self, fine_grained_access_control_findings_count):
        """
        Sets the fine_grained_access_control_findings_count of this SectionStatistics.
        The number of findings in the Fine-Grained Access Control category.


        :param fine_grained_access_control_findings_count: The fine_grained_access_control_findings_count of this SectionStatistics.
        :type: int
        """
        self._fine_grained_access_control_findings_count = fine_grained_access_control_findings_count

    @property
    def privileges_and_roles_findings_count(self):
        """
        Gets the privileges_and_roles_findings_count of this SectionStatistics.
        The number of findings in the Privileges and Roles category.


        :return: The privileges_and_roles_findings_count of this SectionStatistics.
        :rtype: int
        """
        return self._privileges_and_roles_findings_count

    @privileges_and_roles_findings_count.setter
    def privileges_and_roles_findings_count(self, privileges_and_roles_findings_count):
        """
        Sets the privileges_and_roles_findings_count of this SectionStatistics.
        The number of findings in the Privileges and Roles category.


        :param privileges_and_roles_findings_count: The privileges_and_roles_findings_count of this SectionStatistics.
        :type: int
        """
        self._privileges_and_roles_findings_count = privileges_and_roles_findings_count

    @property
    def user_accounts_findings_count(self):
        """
        Gets the user_accounts_findings_count of this SectionStatistics.
        The number of findings in the User Accounts category.


        :return: The user_accounts_findings_count of this SectionStatistics.
        :rtype: int
        """
        return self._user_accounts_findings_count

    @user_accounts_findings_count.setter
    def user_accounts_findings_count(self, user_accounts_findings_count):
        """
        Sets the user_accounts_findings_count of this SectionStatistics.
        The number of findings in the User Accounts category.


        :param user_accounts_findings_count: The user_accounts_findings_count of this SectionStatistics.
        :type: int
        """
        self._user_accounts_findings_count = user_accounts_findings_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
