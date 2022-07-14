# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFusionEnvironmentDetails(object):
    """
    The configuration details of the FusionEnvironment. For more information about these fields, see `Managing Environments`__.

    __ https://docs.cloud.oracle.com/iaas/Content/fusion-applications/manage-environment.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFusionEnvironmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateFusionEnvironmentDetails.
        :type display_name: str

        :param maintenance_policy:
            The value to assign to the maintenance_policy property of this CreateFusionEnvironmentDetails.
        :type maintenance_policy: oci.fusion_apps.models.MaintenancePolicy

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateFusionEnvironmentDetails.
        :type compartment_id: str

        :param fusion_environment_family_id:
            The value to assign to the fusion_environment_family_id property of this CreateFusionEnvironmentDetails.
        :type fusion_environment_family_id: str

        :param fusion_environment_type:
            The value to assign to the fusion_environment_type property of this CreateFusionEnvironmentDetails.
        :type fusion_environment_type: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateFusionEnvironmentDetails.
        :type kms_key_id: str

        :param dns_prefix:
            The value to assign to the dns_prefix property of this CreateFusionEnvironmentDetails.
        :type dns_prefix: str

        :param additional_language_packs:
            The value to assign to the additional_language_packs property of this CreateFusionEnvironmentDetails.
        :type additional_language_packs: list[str]

        :param rules:
            The value to assign to the rules property of this CreateFusionEnvironmentDetails.
        :type rules: list[oci.fusion_apps.models.Rule]

        :param create_fusion_environment_admin_user_details:
            The value to assign to the create_fusion_environment_admin_user_details property of this CreateFusionEnvironmentDetails.
        :type create_fusion_environment_admin_user_details: oci.fusion_apps.models.CreateFusionEnvironmentAdminUserDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateFusionEnvironmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateFusionEnvironmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'maintenance_policy': 'MaintenancePolicy',
            'compartment_id': 'str',
            'fusion_environment_family_id': 'str',
            'fusion_environment_type': 'str',
            'kms_key_id': 'str',
            'dns_prefix': 'str',
            'additional_language_packs': 'list[str]',
            'rules': 'list[Rule]',
            'create_fusion_environment_admin_user_details': 'CreateFusionEnvironmentAdminUserDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'maintenance_policy': 'maintenancePolicy',
            'compartment_id': 'compartmentId',
            'fusion_environment_family_id': 'fusionEnvironmentFamilyId',
            'fusion_environment_type': 'fusionEnvironmentType',
            'kms_key_id': 'kmsKeyId',
            'dns_prefix': 'dnsPrefix',
            'additional_language_packs': 'additionalLanguagePacks',
            'rules': 'rules',
            'create_fusion_environment_admin_user_details': 'createFusionEnvironmentAdminUserDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._maintenance_policy = None
        self._compartment_id = None
        self._fusion_environment_family_id = None
        self._fusion_environment_type = None
        self._kms_key_id = None
        self._dns_prefix = None
        self._additional_language_packs = None
        self._rules = None
        self._create_fusion_environment_admin_user_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateFusionEnvironmentDetails.
        FusionEnvironment Identifier can be renamed.


        :return: The display_name of this CreateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateFusionEnvironmentDetails.
        FusionEnvironment Identifier can be renamed.


        :param display_name: The display_name of this CreateFusionEnvironmentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def maintenance_policy(self):
        """
        Gets the maintenance_policy of this CreateFusionEnvironmentDetails.

        :return: The maintenance_policy of this CreateFusionEnvironmentDetails.
        :rtype: oci.fusion_apps.models.MaintenancePolicy
        """
        return self._maintenance_policy

    @maintenance_policy.setter
    def maintenance_policy(self, maintenance_policy):
        """
        Sets the maintenance_policy of this CreateFusionEnvironmentDetails.

        :param maintenance_policy: The maintenance_policy of this CreateFusionEnvironmentDetails.
        :type: oci.fusion_apps.models.MaintenancePolicy
        """
        self._maintenance_policy = maintenance_policy

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateFusionEnvironmentDetails.
        The unique identifier (OCID) of the compartment where the Fusion Environment is located.


        :return: The compartment_id of this CreateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateFusionEnvironmentDetails.
        The unique identifier (OCID) of the compartment where the Fusion Environment is located.


        :param compartment_id: The compartment_id of this CreateFusionEnvironmentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fusion_environment_family_id(self):
        """
        **[Required]** Gets the fusion_environment_family_id of this CreateFusionEnvironmentDetails.
        The unique identifier (OCID) of the Fusion Environment Family that the Fusion Environment belongs to.


        :return: The fusion_environment_family_id of this CreateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._fusion_environment_family_id

    @fusion_environment_family_id.setter
    def fusion_environment_family_id(self, fusion_environment_family_id):
        """
        Sets the fusion_environment_family_id of this CreateFusionEnvironmentDetails.
        The unique identifier (OCID) of the Fusion Environment Family that the Fusion Environment belongs to.


        :param fusion_environment_family_id: The fusion_environment_family_id of this CreateFusionEnvironmentDetails.
        :type: str
        """
        self._fusion_environment_family_id = fusion_environment_family_id

    @property
    def fusion_environment_type(self):
        """
        **[Required]** Gets the fusion_environment_type of this CreateFusionEnvironmentDetails.
        The type of environment. Valid values are Production, Test, or Development.


        :return: The fusion_environment_type of this CreateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._fusion_environment_type

    @fusion_environment_type.setter
    def fusion_environment_type(self, fusion_environment_type):
        """
        Sets the fusion_environment_type of this CreateFusionEnvironmentDetails.
        The type of environment. Valid values are Production, Test, or Development.


        :param fusion_environment_type: The fusion_environment_type of this CreateFusionEnvironmentDetails.
        :type: str
        """
        self._fusion_environment_type = fusion_environment_type

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CreateFusionEnvironmentDetails.
        byok kms keyId


        :return: The kms_key_id of this CreateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateFusionEnvironmentDetails.
        byok kms keyId


        :param kms_key_id: The kms_key_id of this CreateFusionEnvironmentDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def dns_prefix(self):
        """
        Gets the dns_prefix of this CreateFusionEnvironmentDetails.
        DNS prefix.


        :return: The dns_prefix of this CreateFusionEnvironmentDetails.
        :rtype: str
        """
        return self._dns_prefix

    @dns_prefix.setter
    def dns_prefix(self, dns_prefix):
        """
        Sets the dns_prefix of this CreateFusionEnvironmentDetails.
        DNS prefix.


        :param dns_prefix: The dns_prefix of this CreateFusionEnvironmentDetails.
        :type: str
        """
        self._dns_prefix = dns_prefix

    @property
    def additional_language_packs(self):
        """
        Gets the additional_language_packs of this CreateFusionEnvironmentDetails.
        Language packs.


        :return: The additional_language_packs of this CreateFusionEnvironmentDetails.
        :rtype: list[str]
        """
        return self._additional_language_packs

    @additional_language_packs.setter
    def additional_language_packs(self, additional_language_packs):
        """
        Sets the additional_language_packs of this CreateFusionEnvironmentDetails.
        Language packs.


        :param additional_language_packs: The additional_language_packs of this CreateFusionEnvironmentDetails.
        :type: list[str]
        """
        self._additional_language_packs = additional_language_packs

    @property
    def rules(self):
        """
        Gets the rules of this CreateFusionEnvironmentDetails.
        Rules.


        :return: The rules of this CreateFusionEnvironmentDetails.
        :rtype: list[oci.fusion_apps.models.Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this CreateFusionEnvironmentDetails.
        Rules.


        :param rules: The rules of this CreateFusionEnvironmentDetails.
        :type: list[oci.fusion_apps.models.Rule]
        """
        self._rules = rules

    @property
    def create_fusion_environment_admin_user_details(self):
        """
        **[Required]** Gets the create_fusion_environment_admin_user_details of this CreateFusionEnvironmentDetails.

        :return: The create_fusion_environment_admin_user_details of this CreateFusionEnvironmentDetails.
        :rtype: oci.fusion_apps.models.CreateFusionEnvironmentAdminUserDetails
        """
        return self._create_fusion_environment_admin_user_details

    @create_fusion_environment_admin_user_details.setter
    def create_fusion_environment_admin_user_details(self, create_fusion_environment_admin_user_details):
        """
        Sets the create_fusion_environment_admin_user_details of this CreateFusionEnvironmentDetails.

        :param create_fusion_environment_admin_user_details: The create_fusion_environment_admin_user_details of this CreateFusionEnvironmentDetails.
        :type: oci.fusion_apps.models.CreateFusionEnvironmentAdminUserDetails
        """
        self._create_fusion_environment_admin_user_details = create_fusion_environment_admin_user_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateFusionEnvironmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateFusionEnvironmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateFusionEnvironmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateFusionEnvironmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateFusionEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateFusionEnvironmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateFusionEnvironmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateFusionEnvironmentDetails.
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
