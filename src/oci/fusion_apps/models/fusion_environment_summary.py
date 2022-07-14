# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FusionEnvironmentSummary(object):
    """
    Summary of the internal FA Environment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FusionEnvironmentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this FusionEnvironmentSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this FusionEnvironmentSummary.
        :type display_name: str

        :param time_upcoming_maintenance:
            The value to assign to the time_upcoming_maintenance property of this FusionEnvironmentSummary.
        :type time_upcoming_maintenance: datetime

        :param maintenance_policy:
            The value to assign to the maintenance_policy property of this FusionEnvironmentSummary.
        :type maintenance_policy: oci.fusion_apps.models.GetMaintenancePolicyDetails

        :param compartment_id:
            The value to assign to the compartment_id property of this FusionEnvironmentSummary.
        :type compartment_id: str

        :param fusion_environment_family_id:
            The value to assign to the fusion_environment_family_id property of this FusionEnvironmentSummary.
        :type fusion_environment_family_id: str

        :param subscription_ids:
            The value to assign to the subscription_ids property of this FusionEnvironmentSummary.
        :type subscription_ids: list[str]

        :param applied_patch_bundles:
            The value to assign to the applied_patch_bundles property of this FusionEnvironmentSummary.
        :type applied_patch_bundles: list[str]

        :param fusion_environment_type:
            The value to assign to the fusion_environment_type property of this FusionEnvironmentSummary.
        :type fusion_environment_type: str

        :param version:
            The value to assign to the version property of this FusionEnvironmentSummary.
        :type version: str

        :param public_url:
            The value to assign to the public_url property of this FusionEnvironmentSummary.
        :type public_url: str

        :param dns_prefix:
            The value to assign to the dns_prefix property of this FusionEnvironmentSummary.
        :type dns_prefix: str

        :param additional_language_packs:
            The value to assign to the additional_language_packs property of this FusionEnvironmentSummary.
        :type additional_language_packs: list[str]

        :param time_created:
            The value to assign to the time_created property of this FusionEnvironmentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this FusionEnvironmentSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this FusionEnvironmentSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this FusionEnvironmentSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this FusionEnvironmentSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this FusionEnvironmentSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'time_upcoming_maintenance': 'datetime',
            'maintenance_policy': 'GetMaintenancePolicyDetails',
            'compartment_id': 'str',
            'fusion_environment_family_id': 'str',
            'subscription_ids': 'list[str]',
            'applied_patch_bundles': 'list[str]',
            'fusion_environment_type': 'str',
            'version': 'str',
            'public_url': 'str',
            'dns_prefix': 'str',
            'additional_language_packs': 'list[str]',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'time_upcoming_maintenance': 'timeUpcomingMaintenance',
            'maintenance_policy': 'maintenancePolicy',
            'compartment_id': 'compartmentId',
            'fusion_environment_family_id': 'fusionEnvironmentFamilyId',
            'subscription_ids': 'subscriptionIds',
            'applied_patch_bundles': 'appliedPatchBundles',
            'fusion_environment_type': 'fusionEnvironmentType',
            'version': 'version',
            'public_url': 'publicUrl',
            'dns_prefix': 'dnsPrefix',
            'additional_language_packs': 'additionalLanguagePacks',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._time_upcoming_maintenance = None
        self._maintenance_policy = None
        self._compartment_id = None
        self._fusion_environment_family_id = None
        self._subscription_ids = None
        self._applied_patch_bundles = None
        self._fusion_environment_type = None
        self._version = None
        self._public_url = None
        self._dns_prefix = None
        self._additional_language_packs = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this FusionEnvironmentSummary.
        Unique identifier that is immutable on creation


        :return: The id of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FusionEnvironmentSummary.
        Unique identifier that is immutable on creation


        :param id: The id of this FusionEnvironmentSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this FusionEnvironmentSummary.
        FusionEnvironment Identifier, can be renamed


        :return: The display_name of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this FusionEnvironmentSummary.
        FusionEnvironment Identifier, can be renamed


        :param display_name: The display_name of this FusionEnvironmentSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_upcoming_maintenance(self):
        """
        Gets the time_upcoming_maintenance of this FusionEnvironmentSummary.
        The next maintenance for this environment


        :return: The time_upcoming_maintenance of this FusionEnvironmentSummary.
        :rtype: datetime
        """
        return self._time_upcoming_maintenance

    @time_upcoming_maintenance.setter
    def time_upcoming_maintenance(self, time_upcoming_maintenance):
        """
        Sets the time_upcoming_maintenance of this FusionEnvironmentSummary.
        The next maintenance for this environment


        :param time_upcoming_maintenance: The time_upcoming_maintenance of this FusionEnvironmentSummary.
        :type: datetime
        """
        self._time_upcoming_maintenance = time_upcoming_maintenance

    @property
    def maintenance_policy(self):
        """
        Gets the maintenance_policy of this FusionEnvironmentSummary.

        :return: The maintenance_policy of this FusionEnvironmentSummary.
        :rtype: oci.fusion_apps.models.GetMaintenancePolicyDetails
        """
        return self._maintenance_policy

    @maintenance_policy.setter
    def maintenance_policy(self, maintenance_policy):
        """
        Sets the maintenance_policy of this FusionEnvironmentSummary.

        :param maintenance_policy: The maintenance_policy of this FusionEnvironmentSummary.
        :type: oci.fusion_apps.models.GetMaintenancePolicyDetails
        """
        self._maintenance_policy = maintenance_policy

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this FusionEnvironmentSummary.
        Compartment Identifier


        :return: The compartment_id of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this FusionEnvironmentSummary.
        Compartment Identifier


        :param compartment_id: The compartment_id of this FusionEnvironmentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fusion_environment_family_id(self):
        """
        Gets the fusion_environment_family_id of this FusionEnvironmentSummary.
        FusionEnvironmentFamily Identifier


        :return: The fusion_environment_family_id of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._fusion_environment_family_id

    @fusion_environment_family_id.setter
    def fusion_environment_family_id(self, fusion_environment_family_id):
        """
        Sets the fusion_environment_family_id of this FusionEnvironmentSummary.
        FusionEnvironmentFamily Identifier


        :param fusion_environment_family_id: The fusion_environment_family_id of this FusionEnvironmentSummary.
        :type: str
        """
        self._fusion_environment_family_id = fusion_environment_family_id

    @property
    def subscription_ids(self):
        """
        Gets the subscription_ids of this FusionEnvironmentSummary.
        List of subscription IDs.


        :return: The subscription_ids of this FusionEnvironmentSummary.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        """
        Sets the subscription_ids of this FusionEnvironmentSummary.
        List of subscription IDs.


        :param subscription_ids: The subscription_ids of this FusionEnvironmentSummary.
        :type: list[str]
        """
        self._subscription_ids = subscription_ids

    @property
    def applied_patch_bundles(self):
        """
        Gets the applied_patch_bundles of this FusionEnvironmentSummary.
        Patch bundle names


        :return: The applied_patch_bundles of this FusionEnvironmentSummary.
        :rtype: list[str]
        """
        return self._applied_patch_bundles

    @applied_patch_bundles.setter
    def applied_patch_bundles(self, applied_patch_bundles):
        """
        Sets the applied_patch_bundles of this FusionEnvironmentSummary.
        Patch bundle names


        :param applied_patch_bundles: The applied_patch_bundles of this FusionEnvironmentSummary.
        :type: list[str]
        """
        self._applied_patch_bundles = applied_patch_bundles

    @property
    def fusion_environment_type(self):
        """
        **[Required]** Gets the fusion_environment_type of this FusionEnvironmentSummary.
        Type of the FusionEnvironment.


        :return: The fusion_environment_type of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._fusion_environment_type

    @fusion_environment_type.setter
    def fusion_environment_type(self, fusion_environment_type):
        """
        Sets the fusion_environment_type of this FusionEnvironmentSummary.
        Type of the FusionEnvironment.


        :param fusion_environment_type: The fusion_environment_type of this FusionEnvironmentSummary.
        :type: str
        """
        self._fusion_environment_type = fusion_environment_type

    @property
    def version(self):
        """
        Gets the version of this FusionEnvironmentSummary.
        Version of Fusion Apps used by this environment


        :return: The version of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FusionEnvironmentSummary.
        Version of Fusion Apps used by this environment


        :param version: The version of this FusionEnvironmentSummary.
        :type: str
        """
        self._version = version

    @property
    def public_url(self):
        """
        Gets the public_url of this FusionEnvironmentSummary.
        Public URL


        :return: The public_url of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """
        Sets the public_url of this FusionEnvironmentSummary.
        Public URL


        :param public_url: The public_url of this FusionEnvironmentSummary.
        :type: str
        """
        self._public_url = public_url

    @property
    def dns_prefix(self):
        """
        Gets the dns_prefix of this FusionEnvironmentSummary.
        DNS prefix


        :return: The dns_prefix of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._dns_prefix

    @dns_prefix.setter
    def dns_prefix(self, dns_prefix):
        """
        Sets the dns_prefix of this FusionEnvironmentSummary.
        DNS prefix


        :param dns_prefix: The dns_prefix of this FusionEnvironmentSummary.
        :type: str
        """
        self._dns_prefix = dns_prefix

    @property
    def additional_language_packs(self):
        """
        Gets the additional_language_packs of this FusionEnvironmentSummary.
        Language packs


        :return: The additional_language_packs of this FusionEnvironmentSummary.
        :rtype: list[str]
        """
        return self._additional_language_packs

    @additional_language_packs.setter
    def additional_language_packs(self, additional_language_packs):
        """
        Sets the additional_language_packs of this FusionEnvironmentSummary.
        Language packs


        :param additional_language_packs: The additional_language_packs of this FusionEnvironmentSummary.
        :type: list[str]
        """
        self._additional_language_packs = additional_language_packs

    @property
    def time_created(self):
        """
        Gets the time_created of this FusionEnvironmentSummary.
        The time the the FusionEnvironment was created. An RFC3339 formatted datetime string


        :return: The time_created of this FusionEnvironmentSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this FusionEnvironmentSummary.
        The time the the FusionEnvironment was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this FusionEnvironmentSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this FusionEnvironmentSummary.
        The time the FusionEnvironment was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this FusionEnvironmentSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this FusionEnvironmentSummary.
        The time the FusionEnvironment was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this FusionEnvironmentSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this FusionEnvironmentSummary.
        The current state of the FusionEnvironment.


        :return: The lifecycle_state of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this FusionEnvironmentSummary.
        The current state of the FusionEnvironment.


        :param lifecycle_state: The lifecycle_state of this FusionEnvironmentSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this FusionEnvironmentSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this FusionEnvironmentSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this FusionEnvironmentSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this FusionEnvironmentSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this FusionEnvironmentSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this FusionEnvironmentSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this FusionEnvironmentSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this FusionEnvironmentSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this FusionEnvironmentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this FusionEnvironmentSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this FusionEnvironmentSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this FusionEnvironmentSummary.
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
