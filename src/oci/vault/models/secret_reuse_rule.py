# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .secret_rule import SecretRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SecretReuseRule(SecretRule):
    """
    A rule that disallows reuse of previously used secret content by the specified secret.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SecretReuseRule object with values from keyword arguments. The default value of the :py:attr:`~oci.vault.models.SecretReuseRule.rule_type` attribute
        of this class is ``SECRET_REUSE_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rule_type:
            The value to assign to the rule_type property of this SecretReuseRule.
            Allowed values for this property are: "SECRET_EXPIRY_RULE", "SECRET_REUSE_RULE"
        :type rule_type: str

        :param is_enforced_on_deleted_secret_versions:
            The value to assign to the is_enforced_on_deleted_secret_versions property of this SecretReuseRule.
        :type is_enforced_on_deleted_secret_versions: bool

        """
        self.swagger_types = {
            'rule_type': 'str',
            'is_enforced_on_deleted_secret_versions': 'bool'
        }

        self.attribute_map = {
            'rule_type': 'ruleType',
            'is_enforced_on_deleted_secret_versions': 'isEnforcedOnDeletedSecretVersions'
        }

        self._rule_type = None
        self._is_enforced_on_deleted_secret_versions = None
        self._rule_type = 'SECRET_REUSE_RULE'

    @property
    def is_enforced_on_deleted_secret_versions(self):
        """
        Gets the is_enforced_on_deleted_secret_versions of this SecretReuseRule.
        A property indicating whether the rule is applied even if the secret version with the content you are trying to reuse was deleted.


        :return: The is_enforced_on_deleted_secret_versions of this SecretReuseRule.
        :rtype: bool
        """
        return self._is_enforced_on_deleted_secret_versions

    @is_enforced_on_deleted_secret_versions.setter
    def is_enforced_on_deleted_secret_versions(self, is_enforced_on_deleted_secret_versions):
        """
        Sets the is_enforced_on_deleted_secret_versions of this SecretReuseRule.
        A property indicating whether the rule is applied even if the secret version with the content you are trying to reuse was deleted.


        :param is_enforced_on_deleted_secret_versions: The is_enforced_on_deleted_secret_versions of this SecretReuseRule.
        :type: bool
        """
        self._is_enforced_on_deleted_secret_versions = is_enforced_on_deleted_secret_versions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
