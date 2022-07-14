# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFusionEnvironmentDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFusionEnvironmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateFusionEnvironmentDetails.
        :type display_name: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this UpdateFusionEnvironmentDetails.
        :type kms_key_id: str

        :param maintenance_policy:
            The value to assign to the maintenance_policy property of this UpdateFusionEnvironmentDetails.
        :type maintenance_policy: oci.fusion_apps.models.MaintenancePolicy

        :param additional_language_packs:
            The value to assign to the additional_language_packs property of this UpdateFusionEnvironmentDetails.
        :type additional_language_packs: list[str]

        :param rules:
            The value to assign to the rules property of this UpdateFusionEnvironmentDetails.
        :type rules: list[oci.fusion_apps.models.Rule]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateFusionEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateFusionEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'kms_key_id': 'str',
            'maintenance_policy': 'MaintenancePolicy',
            'additional_language_packs': 'list[str]',
            'rules': 'list[Rule]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'kms_key_id': 'kmsKeyId',
            'maintenance_policy': 'maintenancePolicy',
            'additional_language_packs': 'additionalLanguagePacks',
            'rules': 'rules',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._kms_key_id = None
        self._maintenance_policy = None
        self._additional_language_packs = None
        self._rules = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateFusionEnvironmentDetails.
        FusionEnvironment Identifier, can be renamed


        :return: The display_name of this UpdateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateFusionEnvironmentDetails.
        FusionEnvironment Identifier, can be renamed


        :param display_name: The display_name of this UpdateFusionEnvironmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this UpdateFusionEnvironmentDetails.
        byok kms keyId


        :return: The kms_key_id of this UpdateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this UpdateFusionEnvironmentDetails.
        byok kms keyId


        :param kms_key_id: The kms_key_id of this UpdateFusionEnvironmentDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def maintenance_policy(self):
        """
        Gets the maintenance_policy of this UpdateFusionEnvironmentDetails.

        :return: The maintenance_policy of this UpdateFusionEnvironmentDetails.
        :rtype: oci.fusion_apps.models.MaintenancePolicy
        """
        return self._maintenance_policy

    @maintenance_policy.setter
    def maintenance_policy(self, maintenance_policy):
        """
        Sets the maintenance_policy of this UpdateFusionEnvironmentDetails.

        :param maintenance_policy: The maintenance_policy of this UpdateFusionEnvironmentDetails.
        :type: oci.fusion_apps.models.MaintenancePolicy
        """
        self._maintenance_policy = maintenance_policy

    @property
    def additional_language_packs(self):
        """
        Gets the additional_language_packs of this UpdateFusionEnvironmentDetails.
        Language packs


        :return: The additional_language_packs of this UpdateFusionEnvironmentDetails.
        :rtype: list[str]
        """
        return self._additional_language_packs

    @additional_language_packs.setter
    def additional_language_packs(self, additional_language_packs):
        """
        Sets the additional_language_packs of this UpdateFusionEnvironmentDetails.
        Language packs


        :param additional_language_packs: The additional_language_packs of this UpdateFusionEnvironmentDetails.
        :type: list[str]
        """
        self._additional_language_packs = additional_language_packs

    @property
    def rules(self):
        """
        Gets the rules of this UpdateFusionEnvironmentDetails.
        Network access control rules to limit internet traffic that can access the environment. For more information, see :func:`allow_rule`.


        :return: The rules of this UpdateFusionEnvironmentDetails.
        :rtype: list[oci.fusion_apps.models.Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this UpdateFusionEnvironmentDetails.
        Network access control rules to limit internet traffic that can access the environment. For more information, see :func:`allow_rule`.


        :param rules: The rules of this UpdateFusionEnvironmentDetails.
        :type: list[oci.fusion_apps.models.Rule]
        """
        self._rules = rules

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateFusionEnvironmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateFusionEnvironmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateFusionEnvironmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateFusionEnvironmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateFusionEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateFusionEnvironmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateFusionEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateFusionEnvironmentDetails.
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
