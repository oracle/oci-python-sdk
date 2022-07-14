# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FusionEnvironment(object):
    """
    Description of FusionEnvironment.
    """

    #: A constant which can be used with the fusion_environment_type property of a FusionEnvironment.
    #: This constant has a value of "PRODUCTION"
    FUSION_ENVIRONMENT_TYPE_PRODUCTION = "PRODUCTION"

    #: A constant which can be used with the fusion_environment_type property of a FusionEnvironment.
    #: This constant has a value of "TEST"
    FUSION_ENVIRONMENT_TYPE_TEST = "TEST"

    #: A constant which can be used with the fusion_environment_type property of a FusionEnvironment.
    #: This constant has a value of "DEVELOPMENT"
    FUSION_ENVIRONMENT_TYPE_DEVELOPMENT = "DEVELOPMENT"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironment.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironment.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironment.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironment.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironment.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a FusionEnvironment.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new FusionEnvironment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FusionEnvironment.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this FusionEnvironment.
        :type display_name: str

        :param maintenance_policy:
            The value to assign to the maintenance_policy property of this FusionEnvironment.
        :type maintenance_policy: oci.fusion_apps.models.GetMaintenancePolicyDetails

        :param time_upcoming_maintenance:
            The value to assign to the time_upcoming_maintenance property of this FusionEnvironment.
        :type time_upcoming_maintenance: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this FusionEnvironment.
        :type compartment_id: str

        :param fusion_environment_family_id:
            The value to assign to the fusion_environment_family_id property of this FusionEnvironment.
        :type fusion_environment_family_id: str

        :param subscription_ids:
            The value to assign to the subscription_ids property of this FusionEnvironment.
        :type subscription_ids: list[str]

        :param fusion_environment_type:
            The value to assign to the fusion_environment_type property of this FusionEnvironment.
            Allowed values for this property are: "PRODUCTION", "TEST", "DEVELOPMENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type fusion_environment_type: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this FusionEnvironment.
        :type kms_key_id: str

        :param kms_key_info:
            The value to assign to the kms_key_info property of this FusionEnvironment.
        :type kms_key_info: object

        :param domain_id:
            The value to assign to the domain_id property of this FusionEnvironment.
        :type domain_id: str

        :param idcs_domain_url:
            The value to assign to the idcs_domain_url property of this FusionEnvironment.
        :type idcs_domain_url: str

        :param applied_patch_bundles:
            The value to assign to the applied_patch_bundles property of this FusionEnvironment.
        :type applied_patch_bundles: list[str]

        :param version:
            The value to assign to the version property of this FusionEnvironment.
        :type version: str

        :param public_url:
            The value to assign to the public_url property of this FusionEnvironment.
        :type public_url: str

        :param dns_prefix:
            The value to assign to the dns_prefix property of this FusionEnvironment.
        :type dns_prefix: str

        :param additional_language_packs:
            The value to assign to the additional_language_packs property of this FusionEnvironment.
        :type additional_language_packs: list[str]

        :param refresh:
            The value to assign to the refresh property of this FusionEnvironment.
        :type refresh: oci.fusion_apps.models.RefreshDetails

        :param rules:
            The value to assign to the rules property of this FusionEnvironment.
        :type rules: list[oci.fusion_apps.models.Rule]

        :param time_created:
            The value to assign to the time_created property of this FusionEnvironment.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this FusionEnvironment.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FusionEnvironment.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FusionEnvironment.
        :type lifecycle_details: str

        :param system_name:
            The value to assign to the system_name property of this FusionEnvironment.
        :type system_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FusionEnvironment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FusionEnvironment.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'maintenance_policy': 'GetMaintenancePolicyDetails',
            'time_upcoming_maintenance': 'datetime',
            'compartment_id': 'str',
            'fusion_environment_family_id': 'str',
            'subscription_ids': 'list[str]',
            'fusion_environment_type': 'str',
            'kms_key_id': 'str',
            'kms_key_info': 'object',
            'domain_id': 'str',
            'idcs_domain_url': 'str',
            'applied_patch_bundles': 'list[str]',
            'version': 'str',
            'public_url': 'str',
            'dns_prefix': 'str',
            'additional_language_packs': 'list[str]',
            'refresh': 'RefreshDetails',
            'rules': 'list[Rule]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'system_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'maintenance_policy': 'maintenancePolicy',
            'time_upcoming_maintenance': 'timeUpcomingMaintenance',
            'compartment_id': 'compartmentId',
            'fusion_environment_family_id': 'fusionEnvironmentFamilyId',
            'subscription_ids': 'subscriptionIds',
            'fusion_environment_type': 'fusionEnvironmentType',
            'kms_key_id': 'kmsKeyId',
            'kms_key_info': 'kmsKeyInfo',
            'domain_id': 'domainId',
            'idcs_domain_url': 'idcsDomainUrl',
            'applied_patch_bundles': 'appliedPatchBundles',
            'version': 'version',
            'public_url': 'publicUrl',
            'dns_prefix': 'dnsPrefix',
            'additional_language_packs': 'additionalLanguagePacks',
            'refresh': 'refresh',
            'rules': 'rules',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'system_name': 'systemName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._maintenance_policy = None
        self._time_upcoming_maintenance = None
        self._compartment_id = None
        self._fusion_environment_family_id = None
        self._subscription_ids = None
        self._fusion_environment_type = None
        self._kms_key_id = None
        self._kms_key_info = None
        self._domain_id = None
        self._idcs_domain_url = None
        self._applied_patch_bundles = None
        self._version = None
        self._public_url = None
        self._dns_prefix = None
        self._additional_language_packs = None
        self._refresh = None
        self._rules = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._system_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FusionEnvironment.
        Unique identifier that is immutable on creation


        :return: The id of this FusionEnvironment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FusionEnvironment.
        Unique identifier that is immutable on creation


        :param id: The id of this FusionEnvironment.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FusionEnvironment.
        FusionEnvironment Identifier, can be renamed


        :return: The display_name of this FusionEnvironment.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FusionEnvironment.
        FusionEnvironment Identifier, can be renamed


        :param display_name: The display_name of this FusionEnvironment.
        :type: str
        """
        self._display_name = display_name

    @property
    def maintenance_policy(self):
        """
        Gets the maintenance_policy of this FusionEnvironment.

        :return: The maintenance_policy of this FusionEnvironment.
        :rtype: oci.fusion_apps.models.GetMaintenancePolicyDetails
        """
        return self._maintenance_policy

    @maintenance_policy.setter
    def maintenance_policy(self, maintenance_policy):
        """
        Sets the maintenance_policy of this FusionEnvironment.

        :param maintenance_policy: The maintenance_policy of this FusionEnvironment.
        :type: oci.fusion_apps.models.GetMaintenancePolicyDetails
        """
        self._maintenance_policy = maintenance_policy

    @property
    def time_upcoming_maintenance(self):
        """
        Gets the time_upcoming_maintenance of this FusionEnvironment.
        The next maintenance for this environment


        :return: The time_upcoming_maintenance of this FusionEnvironment.
        :rtype: datetime
        """
        return self._time_upcoming_maintenance

    @time_upcoming_maintenance.setter
    def time_upcoming_maintenance(self, time_upcoming_maintenance):
        """
        Sets the time_upcoming_maintenance of this FusionEnvironment.
        The next maintenance for this environment


        :param time_upcoming_maintenance: The time_upcoming_maintenance of this FusionEnvironment.
        :type: datetime
        """
        self._time_upcoming_maintenance = time_upcoming_maintenance

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FusionEnvironment.
        Compartment Identifier


        :return: The compartment_id of this FusionEnvironment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FusionEnvironment.
        Compartment Identifier


        :param compartment_id: The compartment_id of this FusionEnvironment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fusion_environment_family_id(self):
        """
        Gets the fusion_environment_family_id of this FusionEnvironment.
        FusionEnvironmentFamily Identifier


        :return: The fusion_environment_family_id of this FusionEnvironment.
        :rtype: str
        """
        return self._fusion_environment_family_id

    @fusion_environment_family_id.setter
    def fusion_environment_family_id(self, fusion_environment_family_id):
        """
        Sets the fusion_environment_family_id of this FusionEnvironment.
        FusionEnvironmentFamily Identifier


        :param fusion_environment_family_id: The fusion_environment_family_id of this FusionEnvironment.
        :type: str
        """
        self._fusion_environment_family_id = fusion_environment_family_id

    @property
    def subscription_ids(self):
        """
        Gets the subscription_ids of this FusionEnvironment.
        List of subscription IDs.


        :return: The subscription_ids of this FusionEnvironment.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """
        Sets the subscription_ids of this FusionEnvironment.
        List of subscription IDs.


        :param subscription_ids: The subscription_ids of this FusionEnvironment.
        :type: list[str]
        """
        self._subscription_ids = subscription_ids

    @property
    def fusion_environment_type(self):
        """
        **[Required]** Gets the fusion_environment_type of this FusionEnvironment.
        Type of the FusionEnvironment.

        Allowed values for this property are: "PRODUCTION", "TEST", "DEVELOPMENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The fusion_environment_type of this FusionEnvironment.
        :rtype: str
        """
        return self._fusion_environment_type

    @fusion_environment_type.setter
    def fusion_environment_type(self, fusion_environment_type):
        """
        Sets the fusion_environment_type of this FusionEnvironment.
        Type of the FusionEnvironment.


        :param fusion_environment_type: The fusion_environment_type of this FusionEnvironment.
        :type: str
        """
        allowed_values = ["PRODUCTION", "TEST", "DEVELOPMENT"]
        if not value_allowed_none_or_none_sentinel(fusion_environment_type, allowed_values):
            fusion_environment_type = 'UNKNOWN_ENUM_VALUE'
        self._fusion_environment_type = fusion_environment_type

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this FusionEnvironment.
        BYOK key id


        :return: The kms_key_id of this FusionEnvironment.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this FusionEnvironment.
        BYOK key id


        :param kms_key_id: The kms_key_id of this FusionEnvironment.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def kms_key_info(self):
        """
        Gets the kms_key_info of this FusionEnvironment.
        BYOK key info


        :return: The kms_key_info of this FusionEnvironment.
        :rtype: object
        """
        return self._kms_key_info

    @kms_key_info.setter
    def kms_key_info(self, kms_key_info):
        """
        Sets the kms_key_info of this FusionEnvironment.
        BYOK key info


        :param kms_key_info: The kms_key_info of this FusionEnvironment.
        :type: object
        """
        self._kms_key_info = kms_key_info

    @property
    def domain_id(self):
        """
        Gets the domain_id of this FusionEnvironment.
        The IDCS domain created for the fusion instance


        :return: The domain_id of this FusionEnvironment.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """
        Sets the domain_id of this FusionEnvironment.
        The IDCS domain created for the fusion instance


        :param domain_id: The domain_id of this FusionEnvironment.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def idcs_domain_url(self):
        """
        Gets the idcs_domain_url of this FusionEnvironment.
        The IDCS Domain URL


        :return: The idcs_domain_url of this FusionEnvironment.
        :rtype: str
        """
        return self._idcs_domain_url

    @idcs_domain_url.setter
    def idcs_domain_url(self, idcs_domain_url):
        """
        Sets the idcs_domain_url of this FusionEnvironment.
        The IDCS Domain URL


        :param idcs_domain_url: The idcs_domain_url of this FusionEnvironment.
        :type: str
        """
        self._idcs_domain_url = idcs_domain_url

    @property
    def applied_patch_bundles(self):
        """
        Gets the applied_patch_bundles of this FusionEnvironment.
        Patch bundle names


        :return: The applied_patch_bundles of this FusionEnvironment.
        :rtype: list[str]
        """
        return self._applied_patch_bundles

    @applied_patch_bundles.setter
    def applied_patch_bundles(self, applied_patch_bundles):
        """
        Sets the applied_patch_bundles of this FusionEnvironment.
        Patch bundle names


        :param applied_patch_bundles: The applied_patch_bundles of this FusionEnvironment.
        :type: list[str]
        """
        self._applied_patch_bundles = applied_patch_bundles

    @property
    def version(self):
        """
        Gets the version of this FusionEnvironment.
        Version of Fusion Apps used by this environment


        :return: The version of this FusionEnvironment.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FusionEnvironment.
        Version of Fusion Apps used by this environment


        :param version: The version of this FusionEnvironment.
        :type: str
        """
        self._version = version

    @property
    def public_url(self):
        """
        Gets the public_url of this FusionEnvironment.
        Public URL


        :return: The public_url of this FusionEnvironment.
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """
        Sets the public_url of this FusionEnvironment.
        Public URL


        :param public_url: The public_url of this FusionEnvironment.
        :type: str
        """
        self._public_url = public_url

    @property
    def dns_prefix(self):
        """
        Gets the dns_prefix of this FusionEnvironment.
        DNS prefix


        :return: The dns_prefix of this FusionEnvironment.
        :rtype: str
        """
        return self._dns_prefix

    @dns_prefix.setter
    def dns_prefix(self, dns_prefix):
        """
        Sets the dns_prefix of this FusionEnvironment.
        DNS prefix


        :param dns_prefix: The dns_prefix of this FusionEnvironment.
        :type: str
        """
        self._dns_prefix = dns_prefix

    @property
    def additional_language_packs(self):
        """
        Gets the additional_language_packs of this FusionEnvironment.
        Language packs


        :return: The additional_language_packs of this FusionEnvironment.
        :rtype: list[str]
        """
        return self._additional_language_packs

    @additional_language_packs.setter
    def additional_language_packs(self, additional_language_packs):
        """
        Sets the additional_language_packs of this FusionEnvironment.
        Language packs


        :param additional_language_packs: The additional_language_packs of this FusionEnvironment.
        :type: list[str]
        """
        self._additional_language_packs = additional_language_packs

    @property
    def refresh(self):
        """
        Gets the refresh of this FusionEnvironment.

        :return: The refresh of this FusionEnvironment.
        :rtype: oci.fusion_apps.models.RefreshDetails
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """
        Sets the refresh of this FusionEnvironment.

        :param refresh: The refresh of this FusionEnvironment.
        :type: oci.fusion_apps.models.RefreshDetails
        """
        self._refresh = refresh

    @property
    def rules(self):
        """
        Gets the rules of this FusionEnvironment.
        Network Access Control Rules


        :return: The rules of this FusionEnvironment.
        :rtype: list[oci.fusion_apps.models.Rule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this FusionEnvironment.
        Network Access Control Rules


        :param rules: The rules of this FusionEnvironment.
        :type: list[oci.fusion_apps.models.Rule]
        """
        self._rules = rules

    @property
    def time_created(self):
        """
        Gets the time_created of this FusionEnvironment.
        The time the the FusionEnvironment was created. An RFC3339 formatted datetime string


        :return: The time_created of this FusionEnvironment.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FusionEnvironment.
        The time the the FusionEnvironment was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this FusionEnvironment.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this FusionEnvironment.
        The time the FusionEnvironment was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this FusionEnvironment.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this FusionEnvironment.
        The time the FusionEnvironment was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this FusionEnvironment.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FusionEnvironment.
        The current state of the ServiceInstance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this FusionEnvironment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FusionEnvironment.
        The current state of the ServiceInstance.


        :param lifecycle_state: The lifecycle_state of this FusionEnvironment.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this FusionEnvironment.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this FusionEnvironment.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this FusionEnvironment.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this FusionEnvironment.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def system_name(self):
        """
        Gets the system_name of this FusionEnvironment.
        Environment Specific Guid/ System Name


        :return: The system_name of this FusionEnvironment.
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """
        Sets the system_name of this FusionEnvironment.
        Environment Specific Guid/ System Name


        :param system_name: The system_name of this FusionEnvironment.
        :type: str
        """
        self._system_name = system_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FusionEnvironment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this FusionEnvironment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FusionEnvironment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this FusionEnvironment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FusionEnvironment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this FusionEnvironment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FusionEnvironment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this FusionEnvironment.
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
