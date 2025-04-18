# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExascaleDbStorageVaultSummary(object):
    """
    Details of the Exadata Database Storage Vault.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExascaleDbStorageVaultSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExascaleDbStorageVaultSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExascaleDbStorageVaultSummary.
        :type compartment_id: str

        :param availability_domain:
            The value to assign to the availability_domain property of this ExascaleDbStorageVaultSummary.
        :type availability_domain: str

        :param time_zone:
            The value to assign to the time_zone property of this ExascaleDbStorageVaultSummary.
        :type time_zone: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExascaleDbStorageVaultSummary.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this ExascaleDbStorageVaultSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ExascaleDbStorageVaultSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this ExascaleDbStorageVaultSummary.
        :type time_created: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExascaleDbStorageVaultSummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ExascaleDbStorageVaultSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ExascaleDbStorageVaultSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this ExascaleDbStorageVaultSummary.
        :type system_tags: dict(str, dict(str, object))

        :param high_capacity_database_storage:
            The value to assign to the high_capacity_database_storage property of this ExascaleDbStorageVaultSummary.
        :type high_capacity_database_storage: oci.database.models.ExascaleDbStorageDetails

        :param additional_flash_cache_in_percent:
            The value to assign to the additional_flash_cache_in_percent property of this ExascaleDbStorageVaultSummary.
        :type additional_flash_cache_in_percent: int

        :param vm_cluster_count:
            The value to assign to the vm_cluster_count property of this ExascaleDbStorageVaultSummary.
        :type vm_cluster_count: int

        :param exadata_infrastructure_id:
            The value to assign to the exadata_infrastructure_id property of this ExascaleDbStorageVaultSummary.
        :type exadata_infrastructure_id: str

        :param cluster_placement_group_id:
            The value to assign to the cluster_placement_group_id property of this ExascaleDbStorageVaultSummary.
        :type cluster_placement_group_id: str

        :param subscription_id:
            The value to assign to the subscription_id property of this ExascaleDbStorageVaultSummary.
        :type subscription_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'availability_domain': 'str',
            'time_zone': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'high_capacity_database_storage': 'ExascaleDbStorageDetails',
            'additional_flash_cache_in_percent': 'int',
            'vm_cluster_count': 'int',
            'exadata_infrastructure_id': 'str',
            'cluster_placement_group_id': 'str',
            'subscription_id': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'availability_domain': 'availabilityDomain',
            'time_zone': 'timeZone',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'high_capacity_database_storage': 'highCapacityDatabaseStorage',
            'additional_flash_cache_in_percent': 'additionalFlashCacheInPercent',
            'vm_cluster_count': 'vmClusterCount',
            'exadata_infrastructure_id': 'exadataInfrastructureId',
            'cluster_placement_group_id': 'clusterPlacementGroupId',
            'subscription_id': 'subscriptionId'
        }
        self._id = None
        self._compartment_id = None
        self._availability_domain = None
        self._time_zone = None
        self._lifecycle_state = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._high_capacity_database_storage = None
        self._additional_flash_cache_in_percent = None
        self._vm_cluster_count = None
        self._exadata_infrastructure_id = None
        self._cluster_placement_group_id = None
        self._subscription_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the Exadata Database Storage Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the Exadata Database Storage Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def availability_domain(self):
        """
        **[Required]** Gets the availability_domain of this ExascaleDbStorageVaultSummary.
        The name of the availability domain in which the Exadata Database Storage Vault is located.


        :return: The availability_domain of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._availability_domain

    @availability_domain.setter
    def availability_domain(self, availability_domain):
        """
        Sets the availability_domain of this ExascaleDbStorageVaultSummary.
        The name of the availability domain in which the Exadata Database Storage Vault is located.


        :param availability_domain: The availability_domain of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._availability_domain = availability_domain

    @property
    def time_zone(self):
        """
        Gets the time_zone of this ExascaleDbStorageVaultSummary.
        The time zone that you want to use for the Exadata Database Storage Vault. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :return: The time_zone of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this ExascaleDbStorageVaultSummary.
        The time zone that you want to use for the Exadata Database Storage Vault. For details, see `Time Zones`__.

        __ https://docs.cloud.oracle.com/Content/Database/References/timezones.htm


        :param time_zone: The time_zone of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._time_zone = time_zone

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExascaleDbStorageVaultSummary.
        The current state of the Exadata Database Storage Vault.


        :return: The lifecycle_state of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExascaleDbStorageVaultSummary.
        The current state of the Exadata Database Storage Vault.


        :param lifecycle_state: The lifecycle_state of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExascaleDbStorageVaultSummary.
        The user-friendly name for the Exadata Database Storage Vault. The name does not need to be unique.


        :return: The display_name of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExascaleDbStorageVaultSummary.
        The user-friendly name for the Exadata Database Storage Vault. The name does not need to be unique.


        :param display_name: The display_name of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ExascaleDbStorageVaultSummary.
        Exadata Database Storage Vault description.


        :return: The description of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ExascaleDbStorageVaultSummary.
        Exadata Database Storage Vault description.


        :param description: The description of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this ExascaleDbStorageVaultSummary.
        The date and time that the Exadata Database Storage Vault was created.


        :return: The time_created of this ExascaleDbStorageVaultSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExascaleDbStorageVaultSummary.
        The date and time that the Exadata Database Storage Vault was created.


        :param time_created: The time_created of this ExascaleDbStorageVaultSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExascaleDbStorageVaultSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExascaleDbStorageVaultSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ExascaleDbStorageVaultSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ExascaleDbStorageVaultSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ExascaleDbStorageVaultSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ExascaleDbStorageVaultSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ExascaleDbStorageVaultSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ExascaleDbStorageVaultSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ExascaleDbStorageVaultSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ExascaleDbStorageVaultSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this ExascaleDbStorageVaultSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this ExascaleDbStorageVaultSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this ExascaleDbStorageVaultSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this ExascaleDbStorageVaultSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def high_capacity_database_storage(self):
        """
        **[Required]** Gets the high_capacity_database_storage of this ExascaleDbStorageVaultSummary.

        :return: The high_capacity_database_storage of this ExascaleDbStorageVaultSummary.
        :rtype: oci.database.models.ExascaleDbStorageDetails
        """
        return self._high_capacity_database_storage

    @high_capacity_database_storage.setter
    def high_capacity_database_storage(self, high_capacity_database_storage):
        """
        Sets the high_capacity_database_storage of this ExascaleDbStorageVaultSummary.

        :param high_capacity_database_storage: The high_capacity_database_storage of this ExascaleDbStorageVaultSummary.
        :type: oci.database.models.ExascaleDbStorageDetails
        """
        self._high_capacity_database_storage = high_capacity_database_storage

    @property
    def additional_flash_cache_in_percent(self):
        """
        Gets the additional_flash_cache_in_percent of this ExascaleDbStorageVaultSummary.
        The size of additional Flash Cache in percentage of High Capacity database storage.


        :return: The additional_flash_cache_in_percent of this ExascaleDbStorageVaultSummary.
        :rtype: int
        """
        return self._additional_flash_cache_in_percent

    @additional_flash_cache_in_percent.setter
    def additional_flash_cache_in_percent(self, additional_flash_cache_in_percent):
        """
        Sets the additional_flash_cache_in_percent of this ExascaleDbStorageVaultSummary.
        The size of additional Flash Cache in percentage of High Capacity database storage.


        :param additional_flash_cache_in_percent: The additional_flash_cache_in_percent of this ExascaleDbStorageVaultSummary.
        :type: int
        """
        self._additional_flash_cache_in_percent = additional_flash_cache_in_percent

    @property
    def vm_cluster_count(self):
        """
        Gets the vm_cluster_count of this ExascaleDbStorageVaultSummary.
        The number of Exadata VM clusters used the Exadata Database Storage Vault.


        :return: The vm_cluster_count of this ExascaleDbStorageVaultSummary.
        :rtype: int
        """
        return self._vm_cluster_count

    @vm_cluster_count.setter
    def vm_cluster_count(self, vm_cluster_count):
        """
        Sets the vm_cluster_count of this ExascaleDbStorageVaultSummary.
        The number of Exadata VM clusters used the Exadata Database Storage Vault.


        :param vm_cluster_count: The vm_cluster_count of this ExascaleDbStorageVaultSummary.
        :type: int
        """
        self._vm_cluster_count = vm_cluster_count

    @property
    def exadata_infrastructure_id(self):
        """
        Gets the exadata_infrastructure_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The exadata_infrastructure_id of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._exadata_infrastructure_id

    @exadata_infrastructure_id.setter
    def exadata_infrastructure_id(self, exadata_infrastructure_id):
        """
        Sets the exadata_infrastructure_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the Exadata infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param exadata_infrastructure_id: The exadata_infrastructure_id of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._exadata_infrastructure_id = exadata_infrastructure_id

    @property
    def cluster_placement_group_id(self):
        """
        Gets the cluster_placement_group_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the cluster placement group of the Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cluster_placement_group_id of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._cluster_placement_group_id

    @cluster_placement_group_id.setter
    def cluster_placement_group_id(self, cluster_placement_group_id):
        """
        Sets the cluster_placement_group_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the cluster placement group of the Exadata Infrastructure.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cluster_placement_group_id: The cluster_placement_group_id of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._cluster_placement_group_id = cluster_placement_group_id

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the subscription with which resource needs to be associated with.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subscription_id of this ExascaleDbStorageVaultSummary.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this ExascaleDbStorageVaultSummary.
        The `OCID`__ of the subscription with which resource needs to be associated with.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subscription_id: The subscription_id of this ExascaleDbStorageVaultSummary.
        :type: str
        """
        self._subscription_id = subscription_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
