# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricExtension(object):
    """
    Detailed information of the Metric Extension resource
    """

    #: A constant which can be used with the status property of a MetricExtension.
    #: This constant has a value of "DRAFT"
    STATUS_DRAFT = "DRAFT"

    #: A constant which can be used with the status property of a MetricExtension.
    #: This constant has a value of "PUBLISHED"
    STATUS_PUBLISHED = "PUBLISHED"

    #: A constant which can be used with the lifecycle_state property of a MetricExtension.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MetricExtension.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new MetricExtension object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MetricExtension.
        :type id: str

        :param name:
            The value to assign to the name property of this MetricExtension.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this MetricExtension.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MetricExtension.
        :type description: str

        :param resource_type:
            The value to assign to the resource_type property of this MetricExtension.
        :type resource_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MetricExtension.
        :type compartment_id: str

        :param tenant_id:
            The value to assign to the tenant_id property of this MetricExtension.
        :type tenant_id: str

        :param collection_method:
            The value to assign to the collection_method property of this MetricExtension.
        :type collection_method: str

        :param status:
            The value to assign to the status property of this MetricExtension.
            Allowed values for this property are: "DRAFT", "PUBLISHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MetricExtension.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param created_by:
            The value to assign to the created_by property of this MetricExtension.
        :type created_by: str

        :param last_updated_by:
            The value to assign to the last_updated_by property of this MetricExtension.
        :type last_updated_by: str

        :param time_created:
            The value to assign to the time_created property of this MetricExtension.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MetricExtension.
        :type time_updated: datetime

        :param collection_recurrences:
            The value to assign to the collection_recurrences property of this MetricExtension.
        :type collection_recurrences: str

        :param metric_list:
            The value to assign to the metric_list property of this MetricExtension.
        :type metric_list: list[oci.stack_monitoring.models.Metric]

        :param query_properties:
            The value to assign to the query_properties property of this MetricExtension.
        :type query_properties: oci.stack_monitoring.models.MetricExtensionQueryProperties

        :param enabled_on_resources:
            The value to assign to the enabled_on_resources property of this MetricExtension.
        :type enabled_on_resources: list[oci.stack_monitoring.models.EnabledResourceDetails]

        :param enabled_on_resources_count:
            The value to assign to the enabled_on_resources_count property of this MetricExtension.
        :type enabled_on_resources_count: int

        :param resource_uri:
            The value to assign to the resource_uri property of this MetricExtension.
        :type resource_uri: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'description': 'str',
            'resource_type': 'str',
            'compartment_id': 'str',
            'tenant_id': 'str',
            'collection_method': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'created_by': 'str',
            'last_updated_by': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'collection_recurrences': 'str',
            'metric_list': 'list[Metric]',
            'query_properties': 'MetricExtensionQueryProperties',
            'enabled_on_resources': 'list[EnabledResourceDetails]',
            'enabled_on_resources_count': 'int',
            'resource_uri': 'str'
        }
        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'display_name': 'displayName',
            'description': 'description',
            'resource_type': 'resourceType',
            'compartment_id': 'compartmentId',
            'tenant_id': 'tenantId',
            'collection_method': 'collectionMethod',
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'created_by': 'createdBy',
            'last_updated_by': 'lastUpdatedBy',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'collection_recurrences': 'collectionRecurrences',
            'metric_list': 'metricList',
            'query_properties': 'queryProperties',
            'enabled_on_resources': 'enabledOnResources',
            'enabled_on_resources_count': 'enabledOnResourcesCount',
            'resource_uri': 'resourceUri'
        }
        self._id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._resource_type = None
        self._compartment_id = None
        self._tenant_id = None
        self._collection_method = None
        self._status = None
        self._lifecycle_state = None
        self._created_by = None
        self._last_updated_by = None
        self._time_created = None
        self._time_updated = None
        self._collection_recurrences = None
        self._metric_list = None
        self._query_properties = None
        self._enabled_on_resources = None
        self._enabled_on_resources_count = None
        self._resource_uri = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MetricExtension.
        The `OCID`__ of Metric Extension resource

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MetricExtension.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MetricExtension.
        The `OCID`__ of Metric Extension resource

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MetricExtension.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MetricExtension.
        Metric Extension resource name


        :return: The name of this MetricExtension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MetricExtension.
        Metric Extension resource name


        :param name: The name of this MetricExtension.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this MetricExtension.
        Metric Extension resource display name


        :return: The display_name of this MetricExtension.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MetricExtension.
        Metric Extension resource display name


        :param display_name: The display_name of this MetricExtension.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this MetricExtension.
        Description of the metric extension.


        :return: The description of this MetricExtension.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MetricExtension.
        Description of the metric extension.


        :param description: The description of this MetricExtension.
        :type: str
        """
        self._description = description

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this MetricExtension.
        Resource type to which Metric Extension applies


        :return: The resource_type of this MetricExtension.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this MetricExtension.
        Resource type to which Metric Extension applies


        :param resource_type: The resource_type of this MetricExtension.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MetricExtension.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MetricExtension.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MetricExtension.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MetricExtension.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this MetricExtension.
        Tenant Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenant_id of this MetricExtension.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this MetricExtension.
        Tenant Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenant_id: The tenant_id of this MetricExtension.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def collection_method(self):
        """
        **[Required]** Gets the collection_method of this MetricExtension.
        Collection Method  Metric Extension applies


        :return: The collection_method of this MetricExtension.
        :rtype: str
        """
        return self._collection_method

    @collection_method.setter
    def collection_method(self, collection_method):
        """
        Sets the collection_method of this MetricExtension.
        Collection Method  Metric Extension applies


        :param collection_method: The collection_method of this MetricExtension.
        :type: str
        """
        self._collection_method = collection_method

    @property
    def status(self):
        """
        **[Required]** Gets the status of this MetricExtension.
        The current status of the metric extension i.e. whether it is Draft or Published

        Allowed values for this property are: "DRAFT", "PUBLISHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this MetricExtension.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MetricExtension.
        The current status of the metric extension i.e. whether it is Draft or Published


        :param status: The status of this MetricExtension.
        :type: str
        """
        allowed_values = ["DRAFT", "PUBLISHED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MetricExtension.
        The current lifecycle state of the metric extension

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MetricExtension.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MetricExtension.
        The current lifecycle state of the metric extension


        :param lifecycle_state: The lifecycle_state of this MetricExtension.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def created_by(self):
        """
        Gets the created_by of this MetricExtension.
        Created by user


        :return: The created_by of this MetricExtension.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this MetricExtension.
        Created by user


        :param created_by: The created_by of this MetricExtension.
        :type: str
        """
        self._created_by = created_by

    @property
    def last_updated_by(self):
        """
        Gets the last_updated_by of this MetricExtension.
        Last updated by user


        :return: The last_updated_by of this MetricExtension.
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """
        Sets the last_updated_by of this MetricExtension.
        Last updated by user


        :param last_updated_by: The last_updated_by of this MetricExtension.
        :type: str
        """
        self._last_updated_by = last_updated_by

    @property
    def time_created(self):
        """
        Gets the time_created of this MetricExtension.
        Metric Extension creation time. An RFC3339 formatted datetime string.


        :return: The time_created of this MetricExtension.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MetricExtension.
        Metric Extension creation time. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MetricExtension.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MetricExtension.
        Metric Extension update time. An RFC3339 formatted datetime string.


        :return: The time_updated of this MetricExtension.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MetricExtension.
        Metric Extension update time. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MetricExtension.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def collection_recurrences(self):
        """
        **[Required]** Gets the collection_recurrences of this MetricExtension.
        Schedule of metric extension should use RFC 5545 format -> recur-rule-part = \"FREQ\";\"INTERVAL\" where FREQ rule part identifies the type of recurrence rule. Valid values are \"MINUTELY\",\"HOURLY\",\"DAILY\" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1


        :return: The collection_recurrences of this MetricExtension.
        :rtype: str
        """
        return self._collection_recurrences

    @collection_recurrences.setter
    def collection_recurrences(self, collection_recurrences):
        """
        Sets the collection_recurrences of this MetricExtension.
        Schedule of metric extension should use RFC 5545 format -> recur-rule-part = \"FREQ\";\"INTERVAL\" where FREQ rule part identifies the type of recurrence rule. Valid values are \"MINUTELY\",\"HOURLY\",\"DAILY\" to specify repeating events based on an interval of a minute, an hour and a day or more. Example- FREQ=DAILY;INTERVAL=1


        :param collection_recurrences: The collection_recurrences of this MetricExtension.
        :type: str
        """
        self._collection_recurrences = collection_recurrences

    @property
    def metric_list(self):
        """
        **[Required]** Gets the metric_list of this MetricExtension.
        List of metrics which are part of this metric extension


        :return: The metric_list of this MetricExtension.
        :rtype: list[oci.stack_monitoring.models.Metric]
        """
        return self._metric_list

    @metric_list.setter
    def metric_list(self, metric_list):
        """
        Sets the metric_list of this MetricExtension.
        List of metrics which are part of this metric extension


        :param metric_list: The metric_list of this MetricExtension.
        :type: list[oci.stack_monitoring.models.Metric]
        """
        self._metric_list = metric_list

    @property
    def query_properties(self):
        """
        **[Required]** Gets the query_properties of this MetricExtension.

        :return: The query_properties of this MetricExtension.
        :rtype: oci.stack_monitoring.models.MetricExtensionQueryProperties
        """
        return self._query_properties

    @query_properties.setter
    def query_properties(self, query_properties):
        """
        Sets the query_properties of this MetricExtension.

        :param query_properties: The query_properties of this MetricExtension.
        :type: oci.stack_monitoring.models.MetricExtensionQueryProperties
        """
        self._query_properties = query_properties

    @property
    def enabled_on_resources(self):
        """
        Gets the enabled_on_resources of this MetricExtension.
        List of resource details objects having resourceIds on which this metric extension is enabled.


        :return: The enabled_on_resources of this MetricExtension.
        :rtype: list[oci.stack_monitoring.models.EnabledResourceDetails]
        """
        return self._enabled_on_resources

    @enabled_on_resources.setter
    def enabled_on_resources(self, enabled_on_resources):
        """
        Sets the enabled_on_resources of this MetricExtension.
        List of resource details objects having resourceIds on which this metric extension is enabled.


        :param enabled_on_resources: The enabled_on_resources of this MetricExtension.
        :type: list[oci.stack_monitoring.models.EnabledResourceDetails]
        """
        self._enabled_on_resources = enabled_on_resources

    @property
    def enabled_on_resources_count(self):
        """
        Gets the enabled_on_resources_count of this MetricExtension.
        Count of resources on which this metric extension is enabled.


        :return: The enabled_on_resources_count of this MetricExtension.
        :rtype: int
        """
        return self._enabled_on_resources_count

    @enabled_on_resources_count.setter
    def enabled_on_resources_count(self, enabled_on_resources_count):
        """
        Sets the enabled_on_resources_count of this MetricExtension.
        Count of resources on which this metric extension is enabled.


        :param enabled_on_resources_count: The enabled_on_resources_count of this MetricExtension.
        :type: int
        """
        self._enabled_on_resources_count = enabled_on_resources_count

    @property
    def resource_uri(self):
        """
        Gets the resource_uri of this MetricExtension.
        The URI path that the user can do a GET on to access the metric extension metadata


        :return: The resource_uri of this MetricExtension.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """
        Sets the resource_uri of this MetricExtension.
        The URI path that the user can do a GET on to access the metric extension metadata


        :param resource_uri: The resource_uri of this MetricExtension.
        :type: str
        """
        self._resource_uri = resource_uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
