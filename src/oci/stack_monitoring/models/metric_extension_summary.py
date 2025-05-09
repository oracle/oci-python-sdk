# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210330


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MetricExtensionSummary(object):
    """
    Summary information about metric extension resources
    """

    #: A constant which can be used with the status property of a MetricExtensionSummary.
    #: This constant has a value of "DRAFT"
    STATUS_DRAFT = "DRAFT"

    #: A constant which can be used with the status property of a MetricExtensionSummary.
    #: This constant has a value of "PUBLISHED"
    STATUS_PUBLISHED = "PUBLISHED"

    #: A constant which can be used with the lifecycle_state property of a MetricExtensionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MetricExtensionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the collection_method property of a MetricExtensionSummary.
    #: This constant has a value of "OS_COMMAND"
    COLLECTION_METHOD_OS_COMMAND = "OS_COMMAND"

    #: A constant which can be used with the collection_method property of a MetricExtensionSummary.
    #: This constant has a value of "SQL"
    COLLECTION_METHOD_SQL = "SQL"

    #: A constant which can be used with the collection_method property of a MetricExtensionSummary.
    #: This constant has a value of "JMX"
    COLLECTION_METHOD_JMX = "JMX"

    #: A constant which can be used with the collection_method property of a MetricExtensionSummary.
    #: This constant has a value of "HTTP"
    COLLECTION_METHOD_HTTP = "HTTP"

    def __init__(self, **kwargs):
        """
        Initializes a new MetricExtensionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MetricExtensionSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this MetricExtensionSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this MetricExtensionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MetricExtensionSummary.
        :type description: str

        :param resource_type:
            The value to assign to the resource_type property of this MetricExtensionSummary.
        :type resource_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MetricExtensionSummary.
        :type compartment_id: str

        :param status:
            The value to assign to the status property of this MetricExtensionSummary.
            Allowed values for this property are: "DRAFT", "PUBLISHED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MetricExtensionSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this MetricExtensionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MetricExtensionSummary.
        :type time_updated: datetime

        :param collection_method:
            The value to assign to the collection_method property of this MetricExtensionSummary.
            Allowed values for this property are: "OS_COMMAND", "SQL", "JMX", "HTTP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type collection_method: str

        :param enabled_on_resources_count:
            The value to assign to the enabled_on_resources_count property of this MetricExtensionSummary.
        :type enabled_on_resources_count: int

        :param resource_uri:
            The value to assign to the resource_uri property of this MetricExtensionSummary.
        :type resource_uri: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'display_name': 'str',
            'description': 'str',
            'resource_type': 'str',
            'compartment_id': 'str',
            'status': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'collection_method': 'str',
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
            'status': 'status',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'collection_method': 'collectionMethod',
            'enabled_on_resources_count': 'enabledOnResourcesCount',
            'resource_uri': 'resourceUri'
        }
        self._id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._resource_type = None
        self._compartment_id = None
        self._status = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None
        self._collection_method = None
        self._enabled_on_resources_count = None
        self._resource_uri = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MetricExtensionSummary.
        The `OCID`__ of metric extension.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this MetricExtensionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MetricExtensionSummary.
        The `OCID`__ of metric extension.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this MetricExtensionSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this MetricExtensionSummary.
        Metric Extension Resource name.


        :return: The name of this MetricExtensionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MetricExtensionSummary.
        Metric Extension Resource name.


        :param name: The name of this MetricExtensionSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this MetricExtensionSummary.
        Metric Extension resource display name.


        :return: The display_name of this MetricExtensionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MetricExtensionSummary.
        Metric Extension resource display name.


        :param display_name: The display_name of this MetricExtensionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this MetricExtensionSummary.
        Description of the metric extension.


        :return: The description of this MetricExtensionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MetricExtensionSummary.
        Description of the metric extension.


        :param description: The description of this MetricExtensionSummary.
        :type: str
        """
        self._description = description

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this MetricExtensionSummary.
        Resource type to which Metric Extension applies


        :return: The resource_type of this MetricExtensionSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this MetricExtensionSummary.
        Resource type to which Metric Extension applies


        :param resource_type: The resource_type of this MetricExtensionSummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MetricExtensionSummary.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MetricExtensionSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MetricExtensionSummary.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MetricExtensionSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this MetricExtensionSummary.
        The current state of the metric extension.

        Allowed values for this property are: "DRAFT", "PUBLISHED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this MetricExtensionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this MetricExtensionSummary.
        The current state of the metric extension.


        :param status: The status of this MetricExtensionSummary.
        :type: str
        """
        allowed_values = ["DRAFT", "PUBLISHED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MetricExtensionSummary.
        The current lifecycle state of the metric extension

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MetricExtensionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MetricExtensionSummary.
        The current lifecycle state of the metric extension


        :param lifecycle_state: The lifecycle_state of this MetricExtensionSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this MetricExtensionSummary.
        Metric Extension creation time. An RFC3339 formatted datetime string


        :return: The time_created of this MetricExtensionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MetricExtensionSummary.
        Metric Extension creation time. An RFC3339 formatted datetime string


        :param time_created: The time_created of this MetricExtensionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MetricExtensionSummary.
        Metric Extension updation time. An RFC3339 formatted datetime string


        :return: The time_updated of this MetricExtensionSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MetricExtensionSummary.
        Metric Extension updation time. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this MetricExtensionSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def collection_method(self):
        """
        Gets the collection_method of this MetricExtensionSummary.
        Type of possible collection methods.

        Allowed values for this property are: "OS_COMMAND", "SQL", "JMX", "HTTP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The collection_method of this MetricExtensionSummary.
        :rtype: str
        """
        return self._collection_method

    @collection_method.setter
    def collection_method(self, collection_method):
        """
        Sets the collection_method of this MetricExtensionSummary.
        Type of possible collection methods.


        :param collection_method: The collection_method of this MetricExtensionSummary.
        :type: str
        """
        allowed_values = ["OS_COMMAND", "SQL", "JMX", "HTTP"]
        if not value_allowed_none_or_none_sentinel(collection_method, allowed_values):
            collection_method = 'UNKNOWN_ENUM_VALUE'
        self._collection_method = collection_method

    @property
    def enabled_on_resources_count(self):
        """
        Gets the enabled_on_resources_count of this MetricExtensionSummary.
        Count of resources on which this metric extension is enabled.


        :return: The enabled_on_resources_count of this MetricExtensionSummary.
        :rtype: int
        """
        return self._enabled_on_resources_count

    @enabled_on_resources_count.setter
    def enabled_on_resources_count(self, enabled_on_resources_count):
        """
        Sets the enabled_on_resources_count of this MetricExtensionSummary.
        Count of resources on which this metric extension is enabled.


        :param enabled_on_resources_count: The enabled_on_resources_count of this MetricExtensionSummary.
        :type: int
        """
        self._enabled_on_resources_count = enabled_on_resources_count

    @property
    def resource_uri(self):
        """
        Gets the resource_uri of this MetricExtensionSummary.
        The URI path that the user can do a GET on to access the metric extension metadata


        :return: The resource_uri of this MetricExtensionSummary.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """
        Sets the resource_uri of this MetricExtensionSummary.
        The URI path that the user can do a GET on to access the metric extension metadata


        :param resource_uri: The resource_uri of this MetricExtensionSummary.
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
