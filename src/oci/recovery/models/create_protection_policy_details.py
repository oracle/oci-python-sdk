# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateProtectionPolicyDetails(object):
    """
    Describes the parameters required to create a custom protection policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateProtectionPolicyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateProtectionPolicyDetails.
        :type display_name: str

        :param backup_retention_period_in_days:
            The value to assign to the backup_retention_period_in_days property of this CreateProtectionPolicyDetails.
        :type backup_retention_period_in_days: int

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateProtectionPolicyDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateProtectionPolicyDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateProtectionPolicyDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'backup_retention_period_in_days': 'int',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'backup_retention_period_in_days': 'backupRetentionPeriodInDays',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._backup_retention_period_in_days = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateProtectionPolicyDetails.
        A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.


        :return: The display_name of this CreateProtectionPolicyDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateProtectionPolicyDetails.
        A user provided name for the protection policy. The 'displayName' does not have to be unique, and it can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this CreateProtectionPolicyDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def backup_retention_period_in_days(self):
        """
        **[Required]** Gets the backup_retention_period_in_days of this CreateProtectionPolicyDetails.
        The maximum number of days to retain backups for a protected database.


        :return: The backup_retention_period_in_days of this CreateProtectionPolicyDetails.
        :rtype: int
        """
        return self._backup_retention_period_in_days

    @backup_retention_period_in_days.setter
    def backup_retention_period_in_days(self, backup_retention_period_in_days):
        """
        Sets the backup_retention_period_in_days of this CreateProtectionPolicyDetails.
        The maximum number of days to retain backups for a protected database.


        :param backup_retention_period_in_days: The backup_retention_period_in_days of this CreateProtectionPolicyDetails.
        :type: int
        """
        self._backup_retention_period_in_days = backup_retention_period_in_days

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateProtectionPolicyDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateProtectionPolicyDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateProtectionPolicyDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateProtectionPolicyDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateProtectionPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateProtectionPolicyDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateProtectionPolicyDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateProtectionPolicyDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateProtectionPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateProtectionPolicyDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateProtectionPolicyDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. For more information, see `Resource Tags`__

        __ https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateProtectionPolicyDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
