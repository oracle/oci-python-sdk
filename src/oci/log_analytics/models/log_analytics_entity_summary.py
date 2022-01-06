# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsEntitySummary(object):
    """
    Summary of a log analytics entity.
    """

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEntitySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsEntitySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsEntitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogAnalyticsEntitySummary.
        :type id: str

        :param name:
            The value to assign to the name property of this LogAnalyticsEntitySummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsEntitySummary.
        :type compartment_id: str

        :param entity_type_name:
            The value to assign to the entity_type_name property of this LogAnalyticsEntitySummary.
        :type entity_type_name: str

        :param entity_type_internal_name:
            The value to assign to the entity_type_internal_name property of this LogAnalyticsEntitySummary.
        :type entity_type_internal_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogAnalyticsEntitySummary.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this LogAnalyticsEntitySummary.
        :type lifecycle_details: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this LogAnalyticsEntitySummary.
        :type management_agent_id: str

        :param cloud_resource_id:
            The value to assign to the cloud_resource_id property of this LogAnalyticsEntitySummary.
        :type cloud_resource_id: str

        :param timezone_region:
            The value to assign to the timezone_region property of this LogAnalyticsEntitySummary.
        :type timezone_region: str

        :param time_created:
            The value to assign to the time_created property of this LogAnalyticsEntitySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsEntitySummary.
        :type time_updated: datetime

        :param are_logs_collected:
            The value to assign to the are_logs_collected property of this LogAnalyticsEntitySummary.
        :type are_logs_collected: bool

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsEntitySummary.
        :type source_id: str

        :param creation_source:
            The value to assign to the creation_source property of this LogAnalyticsEntitySummary.
        :type creation_source: oci.log_analytics.models.CreationSource

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LogAnalyticsEntitySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this LogAnalyticsEntitySummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'entity_type_name': 'str',
            'entity_type_internal_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'management_agent_id': 'str',
            'cloud_resource_id': 'str',
            'timezone_region': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'are_logs_collected': 'bool',
            'source_id': 'str',
            'creation_source': 'CreationSource',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'entity_type_name': 'entityTypeName',
            'entity_type_internal_name': 'entityTypeInternalName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'management_agent_id': 'managementAgentId',
            'cloud_resource_id': 'cloudResourceId',
            'timezone_region': 'timezoneRegion',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'are_logs_collected': 'areLogsCollected',
            'source_id': 'sourceId',
            'creation_source': 'creationSource',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._entity_type_name = None
        self._entity_type_internal_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._management_agent_id = None
        self._cloud_resource_id = None
        self._timezone_region = None
        self._time_created = None
        self._time_updated = None
        self._are_logs_collected = None
        self._source_id = None
        self._creation_source = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LogAnalyticsEntitySummary.
        The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
        a resource that is provisioned and managed by the customer on their premises or on the cloud.


        :return: The id of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogAnalyticsEntitySummary.
        The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
        a resource that is provisioned and managed by the customer on their premises or on the cloud.


        :param id: The id of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogAnalyticsEntitySummary.
        Log analytics entity name.


        :return: The name of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsEntitySummary.
        Log analytics entity name.


        :param name: The name of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogAnalyticsEntitySummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsEntitySummary.
        Compartment Identifier `OCID]`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def entity_type_name(self):
        """
        **[Required]** Gets the entity_type_name of this LogAnalyticsEntitySummary.
        Log analytics entity type name.


        :return: The entity_type_name of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._entity_type_name

    @entity_type_name.setter
    def entity_type_name(self, entity_type_name):
        """
        Sets the entity_type_name of this LogAnalyticsEntitySummary.
        Log analytics entity type name.


        :param entity_type_name: The entity_type_name of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._entity_type_name = entity_type_name

    @property
    def entity_type_internal_name(self):
        """
        **[Required]** Gets the entity_type_internal_name of this LogAnalyticsEntitySummary.
        Internal name for the log analytics entity type.


        :return: The entity_type_internal_name of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._entity_type_internal_name

    @entity_type_internal_name.setter
    def entity_type_internal_name(self, entity_type_internal_name):
        """
        Sets the entity_type_internal_name of this LogAnalyticsEntitySummary.
        Internal name for the log analytics entity type.


        :param entity_type_internal_name: The entity_type_internal_name of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._entity_type_internal_name = entity_type_internal_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LogAnalyticsEntitySummary.
        The current state of the log analytics entity.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogAnalyticsEntitySummary.
        The current state of the log analytics entity.


        :param lifecycle_state: The lifecycle_state of this LogAnalyticsEntitySummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this LogAnalyticsEntitySummary.
        lifecycleDetails has additional information regarding substeps such as management agent plugin deployment.


        :return: The lifecycle_details of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this LogAnalyticsEntitySummary.
        lifecycleDetails has additional information regarding substeps such as management agent plugin deployment.


        :param lifecycle_details: The lifecycle_details of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this LogAnalyticsEntitySummary.
        The OCID of the Management Agent.


        :return: The management_agent_id of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this LogAnalyticsEntitySummary.
        The OCID of the Management Agent.


        :param management_agent_id: The management_agent_id of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def cloud_resource_id(self):
        """
        Gets the cloud_resource_id of this LogAnalyticsEntitySummary.
        The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity
        represents a non-cloud resource that the customer may have on their premises.


        :return: The cloud_resource_id of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._cloud_resource_id

    @cloud_resource_id.setter
    def cloud_resource_id(self, cloud_resource_id):
        """
        Sets the cloud_resource_id of this LogAnalyticsEntitySummary.
        The OCID of the Cloud resource which this entity is a representation of. This may be blank when the entity
        represents a non-cloud resource that the customer may have on their premises.


        :param cloud_resource_id: The cloud_resource_id of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._cloud_resource_id = cloud_resource_id

    @property
    def timezone_region(self):
        """
        Gets the timezone_region of this LogAnalyticsEntitySummary.
        The timezone region of the log analytics entity.


        :return: The timezone_region of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._timezone_region

    @timezone_region.setter
    def timezone_region(self, timezone_region):
        """
        Sets the timezone_region of this LogAnalyticsEntitySummary.
        The timezone region of the log analytics entity.


        :param timezone_region: The timezone_region of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._timezone_region = timezone_region

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LogAnalyticsEntitySummary.
        The date and time the resource was created, in the format defined by RFC3339.


        :return: The time_created of this LogAnalyticsEntitySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogAnalyticsEntitySummary.
        The date and time the resource was created, in the format defined by RFC3339.


        :param time_created: The time_created of this LogAnalyticsEntitySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this LogAnalyticsEntitySummary.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :return: The time_updated of this LogAnalyticsEntitySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsEntitySummary.
        The date and time the resource was last updated, in the format defined by RFC3339.


        :param time_updated: The time_updated of this LogAnalyticsEntitySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def are_logs_collected(self):
        """
        Gets the are_logs_collected of this LogAnalyticsEntitySummary.
        The Boolean flag to indicate if logs are collected for an entity for log analytics usage.


        :return: The are_logs_collected of this LogAnalyticsEntitySummary.
        :rtype: bool
        """
        return self._are_logs_collected

    @are_logs_collected.setter
    def are_logs_collected(self, are_logs_collected):
        """
        Sets the are_logs_collected of this LogAnalyticsEntitySummary.
        The Boolean flag to indicate if logs are collected for an entity for log analytics usage.


        :param are_logs_collected: The are_logs_collected of this LogAnalyticsEntitySummary.
        :type: bool
        """
        self._are_logs_collected = are_logs_collected

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsEntitySummary.
        This indicates the type of source. It is primarily for Enterprise Manager Repository ID.


        :return: The source_id of this LogAnalyticsEntitySummary.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsEntitySummary.
        This indicates the type of source. It is primarily for Enterprise Manager Repository ID.


        :param source_id: The source_id of this LogAnalyticsEntitySummary.
        :type: str
        """
        self._source_id = source_id

    @property
    def creation_source(self):
        """
        Gets the creation_source of this LogAnalyticsEntitySummary.

        :return: The creation_source of this LogAnalyticsEntitySummary.
        :rtype: oci.log_analytics.models.CreationSource
        """
        return self._creation_source

    @creation_source.setter
    def creation_source(self, creation_source):
        """
        Sets the creation_source of this LogAnalyticsEntitySummary.

        :param creation_source: The creation_source of this LogAnalyticsEntitySummary.
        :type: oci.log_analytics.models.CreationSource
        """
        self._creation_source = creation_source

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LogAnalyticsEntitySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this LogAnalyticsEntitySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LogAnalyticsEntitySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this LogAnalyticsEntitySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LogAnalyticsEntitySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this LogAnalyticsEntitySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LogAnalyticsEntitySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this LogAnalyticsEntitySummary.
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
