# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dr_protection_group_member import DrProtectionGroupMember
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrProtectionGroupMemberDatabase(DrProtectionGroupMember):
    """
    Properties for a Database (DBCS) member of a DR Protection Group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DrProtectionGroupMemberDatabase object with values from keyword arguments. The default value of the :py:attr:`~oci.disaster_recovery.models.DrProtectionGroupMemberDatabase.member_type` attribute
        of this class is ``DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param member_id:
            The value to assign to the member_id property of this DrProtectionGroupMemberDatabase.
        :type member_id: str

        :param member_type:
            The value to assign to the member_type property of this DrProtectionGroupMemberDatabase.
            Allowed values for this property are: "COMPUTE_INSTANCE", "VOLUME_GROUP", "DATABASE", "AUTONOMOUS_DATABASE"
        :type member_type: str

        :param password_vault_secret_id:
            The value to assign to the password_vault_secret_id property of this DrProtectionGroupMemberDatabase.
        :type password_vault_secret_id: str

        """
        self.swagger_types = {
            'member_id': 'str',
            'member_type': 'str',
            'password_vault_secret_id': 'str'
        }

        self.attribute_map = {
            'member_id': 'memberId',
            'member_type': 'memberType',
            'password_vault_secret_id': 'passwordVaultSecretId'
        }

        self._member_id = None
        self._member_type = None
        self._password_vault_secret_id = None
        self._member_type = 'DATABASE'

    @property
    def password_vault_secret_id(self):
        """
        Gets the password_vault_secret_id of this DrProtectionGroupMemberDatabase.
        The ID of the vault secret where the database password is stored.

        Example: `ocid1.vaultsecret.oc1.phx.exampleocid1`


        :return: The password_vault_secret_id of this DrProtectionGroupMemberDatabase.
        :rtype: str
        """
        return self._password_vault_secret_id

    @password_vault_secret_id.setter
    def password_vault_secret_id(self, password_vault_secret_id):
        """
        Sets the password_vault_secret_id of this DrProtectionGroupMemberDatabase.
        The ID of the vault secret where the database password is stored.

        Example: `ocid1.vaultsecret.oc1.phx.exampleocid1`


        :param password_vault_secret_id: The password_vault_secret_id of this DrProtectionGroupMemberDatabase.
        :type: str
        """
        self._password_vault_secret_id = password_vault_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
