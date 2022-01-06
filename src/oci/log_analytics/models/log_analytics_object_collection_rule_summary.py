# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsObjectCollectionRuleSummary(object):
    """
    The summary of an Object Storage based collection rule.
    """

    #: A constant which can be used with the collection_type property of a LogAnalyticsObjectCollectionRuleSummary.
    #: This constant has a value of "LIVE"
    COLLECTION_TYPE_LIVE = "LIVE"

    #: A constant which can be used with the collection_type property of a LogAnalyticsObjectCollectionRuleSummary.
    #: This constant has a value of "HISTORIC"
    COLLECTION_TYPE_HISTORIC = "HISTORIC"

    #: A constant which can be used with the collection_type property of a LogAnalyticsObjectCollectionRuleSummary.
    #: This constant has a value of "HISTORIC_LIVE"
    COLLECTION_TYPE_HISTORIC_LIVE = "HISTORIC_LIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsObjectCollectionRuleSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsObjectCollectionRuleSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsObjectCollectionRuleSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsObjectCollectionRuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogAnalyticsObjectCollectionRuleSummary.
        :type id: str

        :param name:
            The value to assign to the name property of this LogAnalyticsObjectCollectionRuleSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this LogAnalyticsObjectCollectionRuleSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsObjectCollectionRuleSummary.
        :type compartment_id: str

        :param os_namespace:
            The value to assign to the os_namespace property of this LogAnalyticsObjectCollectionRuleSummary.
        :type os_namespace: str

        :param os_bucket_name:
            The value to assign to the os_bucket_name property of this LogAnalyticsObjectCollectionRuleSummary.
        :type os_bucket_name: str

        :param collection_type:
            The value to assign to the collection_type property of this LogAnalyticsObjectCollectionRuleSummary.
            Allowed values for this property are: "LIVE", "HISTORIC", "HISTORIC_LIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type collection_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogAnalyticsObjectCollectionRuleSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this LogAnalyticsObjectCollectionRuleSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this LogAnalyticsObjectCollectionRuleSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsObjectCollectionRuleSummary.
        :type time_updated: datetime

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsObjectCollectionRuleSummary.
        :type is_enabled: bool

        :param object_name_filters:
            The value to assign to the object_name_filters property of this LogAnalyticsObjectCollectionRuleSummary.
        :type object_name_filters: list[str]

        :param defined_tags:
            The value to assign to the defined_tags property of this LogAnalyticsObjectCollectionRuleSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LogAnalyticsObjectCollectionRuleSummary.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'os_namespace': 'str',
            'os_bucket_name': 'str',
            'collection_type': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'is_enabled': 'bool',
            'object_name_filters': 'list[str]',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'os_namespace': 'osNamespace',
            'os_bucket_name': 'osBucketName',
            'collection_type': 'collectionType',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'is_enabled': 'isEnabled',
            'object_name_filters': 'objectNameFilters',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._id = None
        self._name = None
        self._description = None
        self._compartment_id = None
        self._os_namespace = None
        self._os_bucket_name = None
        self._collection_type = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._is_enabled = None
        self._object_name_filters = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LogAnalyticsObjectCollectionRuleSummary.
        The `OCID`__ of this rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogAnalyticsObjectCollectionRuleSummary.
        The `OCID`__ of this rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogAnalyticsObjectCollectionRuleSummary.
        A unique name to the rule. The name must be unique, within the tenancy, and cannot be changed.


        :return: The name of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsObjectCollectionRuleSummary.
        A unique name to the rule. The name must be unique, within the tenancy, and cannot be changed.


        :param name: The name of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsObjectCollectionRuleSummary.
        A unique name given to the rule. The name must be unique within the tenancy, and cannot be modified.
        Avoid entering confidential information.


        :return: The description of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsObjectCollectionRuleSummary.
        A unique name given to the rule. The name must be unique within the tenancy, and cannot be modified.
        Avoid entering confidential information.


        :param description: The description of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogAnalyticsObjectCollectionRuleSummary.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsObjectCollectionRuleSummary.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def os_namespace(self):
        """
        **[Required]** Gets the os_namespace of this LogAnalyticsObjectCollectionRuleSummary.
        Object Storage namespace.


        :return: The os_namespace of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._os_namespace

    @os_namespace.setter
    def os_namespace(self, os_namespace):
        """
        Sets the os_namespace of this LogAnalyticsObjectCollectionRuleSummary.
        Object Storage namespace.


        :param os_namespace: The os_namespace of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        self._os_namespace = os_namespace

    @property
    def os_bucket_name(self):
        """
        **[Required]** Gets the os_bucket_name of this LogAnalyticsObjectCollectionRuleSummary.
        Name of the Object Storage bucket.


        :return: The os_bucket_name of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._os_bucket_name

    @os_bucket_name.setter
    def os_bucket_name(self, os_bucket_name):
        """
        Sets the os_bucket_name of this LogAnalyticsObjectCollectionRuleSummary.
        Name of the Object Storage bucket.


        :param os_bucket_name: The os_bucket_name of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        self._os_bucket_name = os_bucket_name

    @property
    def collection_type(self):
        """
        **[Required]** Gets the collection_type of this LogAnalyticsObjectCollectionRuleSummary.
        The type of log collection.

        Allowed values for this property are: "LIVE", "HISTORIC", "HISTORIC_LIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The collection_type of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._collection_type

    @collection_type.setter
    def collection_type(self, collection_type):
        """
        Sets the collection_type of this LogAnalyticsObjectCollectionRuleSummary.
        The type of log collection.


        :param collection_type: The collection_type of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        allowed_values = ["LIVE", "HISTORIC", "HISTORIC_LIVE"]
        if not value_allowed_none_or_none_sentinel(collection_type, allowed_values):
            collection_type = 'UNKNOWN_ENUM_VALUE'
        self._collection_type = collection_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LogAnalyticsObjectCollectionRuleSummary.
        The current state of the rule.

        Allowed values for this property are: "ACTIVE", "DELETED", "INACTIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogAnalyticsObjectCollectionRuleSummary.
        The current state of the rule.


        :param lifecycle_state: The lifecycle_state of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED", "INACTIVE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this LogAnalyticsObjectCollectionRuleSummary.
        A detailed status of the life cycle state.


        :return: The lifecycle_details of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this LogAnalyticsObjectCollectionRuleSummary.
        A detailed status of the life cycle state.


        :param lifecycle_details: The lifecycle_details of this LogAnalyticsObjectCollectionRuleSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LogAnalyticsObjectCollectionRuleSummary.
        The time when this rule was created. An RFC3339 formatted datetime string.


        :return: The time_created of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogAnalyticsObjectCollectionRuleSummary.
        The time when this rule was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this LogAnalyticsObjectCollectionRuleSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this LogAnalyticsObjectCollectionRuleSummary.
        The time when this rule was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsObjectCollectionRuleSummary.
        The time when this rule was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this LogAnalyticsObjectCollectionRuleSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this LogAnalyticsObjectCollectionRuleSummary.
        Whether or not this rule is currently enabled.


        :return: The is_enabled of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsObjectCollectionRuleSummary.
        Whether or not this rule is currently enabled.


        :param is_enabled: The is_enabled of this LogAnalyticsObjectCollectionRuleSummary.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def object_name_filters(self):
        """
        Gets the object_name_filters of this LogAnalyticsObjectCollectionRuleSummary.
        When the filters are provided, only the objects matching the filters are picked up for processing.
        The matchType supported is exact match and accommodates wildcard \"*\".
        For more information on filters, see `Event Filters`__.

        __ https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm


        :return: The object_name_filters of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: list[str]
        """
        return self._object_name_filters

    @object_name_filters.setter
    def object_name_filters(self, object_name_filters):
        """
        Sets the object_name_filters of this LogAnalyticsObjectCollectionRuleSummary.
        When the filters are provided, only the objects matching the filters are picked up for processing.
        The matchType supported is exact match and accommodates wildcard \"*\".
        For more information on filters, see `Event Filters`__.

        __ https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/filterevents.htm


        :param object_name_filters: The object_name_filters of this LogAnalyticsObjectCollectionRuleSummary.
        :type: list[str]
        """
        self._object_name_filters = object_name_filters

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LogAnalyticsObjectCollectionRuleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LogAnalyticsObjectCollectionRuleSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this LogAnalyticsObjectCollectionRuleSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LogAnalyticsObjectCollectionRuleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this LogAnalyticsObjectCollectionRuleSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LogAnalyticsObjectCollectionRuleSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this LogAnalyticsObjectCollectionRuleSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
