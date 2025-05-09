# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceSummary(object):
    """
    The information about monitored resource.
    """

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the license property of a MonitoredResourceSummary.
    #: This constant has a value of "STANDARD_EDITION"
    LICENSE_STANDARD_EDITION = "STANDARD_EDITION"

    #: A constant which can be used with the license property of a MonitoredResourceSummary.
    #: This constant has a value of "ENTERPRISE_EDITION"
    LICENSE_ENTERPRISE_EDITION = "ENTERPRISE_EDITION"

    #: A constant which can be used with the license property of a MonitoredResourceSummary.
    #: This constant has a value of "ENTERPRISE_EDITION_FOR_GPU_INFRASTRUCTURE"
    LICENSE_ENTERPRISE_EDITION_FOR_GPU_INFRASTRUCTURE = "ENTERPRISE_EDITION_FOR_GPU_INFRASTRUCTURE"

    #: A constant which can be used with the source_type property of a MonitoredResourceSummary.
    #: This constant has a value of "SM_MGMT_AGENT_MONITORED"
    SOURCE_TYPE_SM_MGMT_AGENT_MONITORED = "SM_MGMT_AGENT_MONITORED"

    #: A constant which can be used with the source_type property of a MonitoredResourceSummary.
    #: This constant has a value of "SM_REPO_ONLY"
    SOURCE_TYPE_SM_REPO_ONLY = "SM_REPO_ONLY"

    #: A constant which can be used with the source_type property of a MonitoredResourceSummary.
    #: This constant has a value of "OCI_NATIVE"
    SOURCE_TYPE_OCI_NATIVE = "OCI_NATIVE"

    #: A constant which can be used with the source_type property of a MonitoredResourceSummary.
    #: This constant has a value of "PROMETHEUS"
    SOURCE_TYPE_PROMETHEUS = "PROMETHEUS"

    #: A constant which can be used with the source_type property of a MonitoredResourceSummary.
    #: This constant has a value of "TELEGRAF"
    SOURCE_TYPE_TELEGRAF = "TELEGRAF"

    #: A constant which can be used with the source_type property of a MonitoredResourceSummary.
    #: This constant has a value of "COLLECTD"
    SOURCE_TYPE_COLLECTD = "COLLECTD"

    #: A constant which can be used with the resource_category property of a MonitoredResourceSummary.
    #: This constant has a value of "APPLICATION"
    RESOURCE_CATEGORY_APPLICATION = "APPLICATION"

    #: A constant which can be used with the resource_category property of a MonitoredResourceSummary.
    #: This constant has a value of "DATABASE"
    RESOURCE_CATEGORY_DATABASE = "DATABASE"

    #: A constant which can be used with the resource_category property of a MonitoredResourceSummary.
    #: This constant has a value of "MIDDLEWARE"
    RESOURCE_CATEGORY_MIDDLEWARE = "MIDDLEWARE"

    #: A constant which can be used with the resource_category property of a MonitoredResourceSummary.
    #: This constant has a value of "INFRASTRUCTURE"
    RESOURCE_CATEGORY_INFRASTRUCTURE = "INFRASTRUCTURE"

    #: A constant which can be used with the resource_category property of a MonitoredResourceSummary.
    #: This constant has a value of "UNKNOWN"
    RESOURCE_CATEGORY_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MonitoredResourceSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this MonitoredResourceSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this MonitoredResourceSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this MonitoredResourceSummary.
        :type type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoredResourceSummary.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this MonitoredResourceSummary.
        :type host_name: str

        :param external_id:
            The value to assign to the external_id property of this MonitoredResourceSummary.
        :type external_id: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MonitoredResourceSummary.
        :type management_agent_id: str

        :param time_created:
            The value to assign to the time_created property of this MonitoredResourceSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MonitoredResourceSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoredResourceSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param properties:
            The value to assign to the properties property of this MonitoredResourceSummary.
        :type properties: list[oci.stack_monitoring.models.MonitoredResourceProperty]

        :param license:
            The value to assign to the license property of this MonitoredResourceSummary.
            Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_FOR_GPU_INFRASTRUCTURE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license: str

        :param source_type:
            The value to assign to the source_type property of this MonitoredResourceSummary.
            Allowed values for this property are: "SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param resource_category:
            The value to assign to the resource_category property of this MonitoredResourceSummary.
            Allowed values for this property are: "APPLICATION", "DATABASE", "MIDDLEWARE", "INFRASTRUCTURE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_category: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MonitoredResourceSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MonitoredResourceSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MonitoredResourceSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'type': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'external_id': 'str',
            'management_agent_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'properties': 'list[MonitoredResourceProperty]',
            'license': 'str',
            'source_type': 'str',
            'resource_category': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'type': 'type',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'external_id': 'externalId',
            'management_agent_id': 'managementAgentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'properties': 'properties',
            'license': 'license',
            'source_type': 'sourceType',
            'resource_category': 'resourceCategory',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._name = None
        self._display_name = None
        self._type = None
        self._compartment_id = None
        self._host_name = None
        self._external_id = None
        self._management_agent_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._properties = None
        self._license = None
        self._source_type = None
        self._resource_category = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MonitoredResourceSummary.
        Monitored resource identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MonitoredResourceSummary.
        Monitored resource identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MonitoredResourceSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MonitoredResourceSummary.
        Monitored Resource Name.


        :return: The name of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MonitoredResourceSummary.
        Monitored Resource Name.


        :param name: The name of this MonitoredResourceSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this MonitoredResourceSummary.
        Monitored resource display name.


        :return: The display_name of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MonitoredResourceSummary.
        Monitored resource display name.


        :param display_name: The display_name of this MonitoredResourceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MonitoredResourceSummary.
        Monitored Resource Type.


        :return: The type of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MonitoredResourceSummary.
        Monitored Resource Type.


        :param type: The type of this MonitoredResourceSummary.
        :type: str
        """
        self._type = type

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this MonitoredResourceSummary.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoredResourceSummary.
        Compartment Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoredResourceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def host_name(self):
        """
        Gets the host_name of this MonitoredResourceSummary.
        Monitored Resource Host Name.


        :return: The host_name of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this MonitoredResourceSummary.
        Monitored Resource Host Name.


        :param host_name: The host_name of this MonitoredResourceSummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def external_id(self):
        """
        Gets the external_id of this MonitoredResourceSummary.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_id of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this MonitoredResourceSummary.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_id: The external_id of this MonitoredResourceSummary.
        :type: str
        """
        self._external_id = external_id

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this MonitoredResourceSummary.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MonitoredResourceSummary.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MonitoredResourceSummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def time_created(self):
        """
        Gets the time_created of this MonitoredResourceSummary.
        Monitored resource creation time. An RFC3339 formatted datetime string.


        :return: The time_created of this MonitoredResourceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MonitoredResourceSummary.
        Monitored resource creation time. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MonitoredResourceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MonitoredResourceSummary.
        Monitored resource update time. An RFC3339 formatted datetime string.


        :return: The time_updated of this MonitoredResourceSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MonitoredResourceSummary.
        Monitored resource update time. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MonitoredResourceSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MonitoredResourceSummary.
        The current state of the monitored resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoredResourceSummary.
        The current state of the monitored resource.


        :param lifecycle_state: The lifecycle_state of this MonitoredResourceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def properties(self):
        """
        Gets the properties of this MonitoredResourceSummary.
        List of monitored resource properties.


        :return: The properties of this MonitoredResourceSummary.
        :rtype: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this MonitoredResourceSummary.
        List of monitored resource properties.


        :param properties: The properties of this MonitoredResourceSummary.
        :type: list[oci.stack_monitoring.models.MonitoredResourceProperty]
        """
        self._properties = properties

    @property
    def license(self):
        """
        Gets the license of this MonitoredResourceSummary.
        License edition of the monitored resource.

        Allowed values for this property are: "STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_FOR_GPU_INFRASTRUCTURE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """
        Sets the license of this MonitoredResourceSummary.
        License edition of the monitored resource.


        :param license: The license of this MonitoredResourceSummary.
        :type: str
        """
        allowed_values = ["STANDARD_EDITION", "ENTERPRISE_EDITION", "ENTERPRISE_EDITION_FOR_GPU_INFRASTRUCTURE"]
        if not value_allowed_none_or_none_sentinel(license, allowed_values):
            license = 'UNKNOWN_ENUM_VALUE'
        self._license = license

    @property
    def source_type(self):
        """
        Gets the source_type of this MonitoredResourceSummary.
        Source type to indicate if the resource is stack monitoring discovered, OCI native resource, etc.

        Allowed values for this property are: "SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this MonitoredResourceSummary.
        Source type to indicate if the resource is stack monitoring discovered, OCI native resource, etc.


        :param source_type: The source_type of this MonitoredResourceSummary.
        :type: str
        """
        allowed_values = ["SM_MGMT_AGENT_MONITORED", "SM_REPO_ONLY", "OCI_NATIVE", "PROMETHEUS", "TELEGRAF", "COLLECTD"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def resource_category(self):
        """
        Gets the resource_category of this MonitoredResourceSummary.
        Resource Category to indicate the kind of resource type.

        Allowed values for this property are: "APPLICATION", "DATABASE", "MIDDLEWARE", "INFRASTRUCTURE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_category of this MonitoredResourceSummary.
        :rtype: str
        """
        return self._resource_category

    @resource_category.setter
    def resource_category(self, resource_category):
        """
        Sets the resource_category of this MonitoredResourceSummary.
        Resource Category to indicate the kind of resource type.


        :param resource_category: The resource_category of this MonitoredResourceSummary.
        :type: str
        """
        allowed_values = ["APPLICATION", "DATABASE", "MIDDLEWARE", "INFRASTRUCTURE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(resource_category, allowed_values):
            resource_category = 'UNKNOWN_ENUM_VALUE'
        self._resource_category = resource_category

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MonitoredResourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MonitoredResourceSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MonitoredResourceSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MonitoredResourceSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MonitoredResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MonitoredResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MonitoredResourceSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MonitoredResourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MonitoredResourceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MonitoredResourceSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MonitoredResourceSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MonitoredResourceSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
