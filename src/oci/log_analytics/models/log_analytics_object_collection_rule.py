# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsObjectCollectionRule(object):
    """
    The configuration details of an Object Storage based collection rule.
    """

    #: A constant which can be used with the collection_type property of a LogAnalyticsObjectCollectionRule.
    #: This constant has a value of "LIVE"
    COLLECTION_TYPE_LIVE = "LIVE"

    #: A constant which can be used with the collection_type property of a LogAnalyticsObjectCollectionRule.
    #: This constant has a value of "HISTORIC"
    COLLECTION_TYPE_HISTORIC = "HISTORIC"

    #: A constant which can be used with the collection_type property of a LogAnalyticsObjectCollectionRule.
    #: This constant has a value of "HISTORIC_LIVE"
    COLLECTION_TYPE_HISTORIC_LIVE = "HISTORIC_LIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsObjectCollectionRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a LogAnalyticsObjectCollectionRule.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsObjectCollectionRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this LogAnalyticsObjectCollectionRule.
        :type id: str

        :param name:
            The value to assign to the name property of this LogAnalyticsObjectCollectionRule.
        :type name: str

        :param description:
            The value to assign to the description property of this LogAnalyticsObjectCollectionRule.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this LogAnalyticsObjectCollectionRule.
        :type compartment_id: str

        :param os_namespace:
            The value to assign to the os_namespace property of this LogAnalyticsObjectCollectionRule.
        :type os_namespace: str

        :param os_bucket_name:
            The value to assign to the os_bucket_name property of this LogAnalyticsObjectCollectionRule.
        :type os_bucket_name: str

        :param collection_type:
            The value to assign to the collection_type property of this LogAnalyticsObjectCollectionRule.
            Allowed values for this property are: "LIVE", "HISTORIC", "HISTORIC_LIVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type collection_type: str

        :param poll_since:
            The value to assign to the poll_since property of this LogAnalyticsObjectCollectionRule.
        :type poll_since: str

        :param poll_till:
            The value to assign to the poll_till property of this LogAnalyticsObjectCollectionRule.
        :type poll_till: str

        :param log_group_id:
            The value to assign to the log_group_id property of this LogAnalyticsObjectCollectionRule.
        :type log_group_id: str

        :param log_source_name:
            The value to assign to the log_source_name property of this LogAnalyticsObjectCollectionRule.
        :type log_source_name: str

        :param entity_id:
            The value to assign to the entity_id property of this LogAnalyticsObjectCollectionRule.
        :type entity_id: str

        :param char_encoding:
            The value to assign to the char_encoding property of this LogAnalyticsObjectCollectionRule.
        :type char_encoding: str

        :param overrides:
            The value to assign to the overrides property of this LogAnalyticsObjectCollectionRule.
        :type overrides: dict(str, list[PropertyOverride])

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this LogAnalyticsObjectCollectionRule.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this LogAnalyticsObjectCollectionRule.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this LogAnalyticsObjectCollectionRule.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsObjectCollectionRule.
        :type time_updated: datetime

        :param defined_tags:
            The value to assign to the defined_tags property of this LogAnalyticsObjectCollectionRule.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this LogAnalyticsObjectCollectionRule.
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
            'poll_since': 'str',
            'poll_till': 'str',
            'log_group_id': 'str',
            'log_source_name': 'str',
            'entity_id': 'str',
            'char_encoding': 'str',
            'overrides': 'dict(str, list[PropertyOverride])',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
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
            'poll_since': 'pollSince',
            'poll_till': 'pollTill',
            'log_group_id': 'logGroupId',
            'log_source_name': 'logSourceName',
            'entity_id': 'entityId',
            'char_encoding': 'charEncoding',
            'overrides': 'overrides',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
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
        self._poll_since = None
        self._poll_till = None
        self._log_group_id = None
        self._log_source_name = None
        self._entity_id = None
        self._char_encoding = None
        self._overrides = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this LogAnalyticsObjectCollectionRule.
        The `OCID`__ of this rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LogAnalyticsObjectCollectionRule.
        The `OCID`__ of this rule.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this LogAnalyticsObjectCollectionRule.
        A unique name to the rule. The name must be unique, within the tenancy, and cannot be changed.


        :return: The name of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LogAnalyticsObjectCollectionRule.
        A unique name to the rule. The name must be unique, within the tenancy, and cannot be changed.


        :param name: The name of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsObjectCollectionRule.
        A string that describes the details of the rule. It does not have to be unique, and can be changed.
        Avoid entering confidential information.


        :return: The description of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsObjectCollectionRule.
        A string that describes the details of the rule. It does not have to be unique, and can be changed.
        Avoid entering confidential information.


        :param description: The description of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this LogAnalyticsObjectCollectionRule.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this LogAnalyticsObjectCollectionRule.
        The `OCID`__ of the compartment to which this rule belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def os_namespace(self):
        """
        **[Required]** Gets the os_namespace of this LogAnalyticsObjectCollectionRule.
        Object Storage namespace.


        :return: The os_namespace of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._os_namespace

    @os_namespace.setter
    def os_namespace(self, os_namespace):
        """
        Sets the os_namespace of this LogAnalyticsObjectCollectionRule.
        Object Storage namespace.


        :param os_namespace: The os_namespace of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._os_namespace = os_namespace

    @property
    def os_bucket_name(self):
        """
        **[Required]** Gets the os_bucket_name of this LogAnalyticsObjectCollectionRule.
        Name of the Object Storage bucket.


        :return: The os_bucket_name of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._os_bucket_name

    @os_bucket_name.setter
    def os_bucket_name(self, os_bucket_name):
        """
        Sets the os_bucket_name of this LogAnalyticsObjectCollectionRule.
        Name of the Object Storage bucket.


        :param os_bucket_name: The os_bucket_name of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._os_bucket_name = os_bucket_name

    @property
    def collection_type(self):
        """
        **[Required]** Gets the collection_type of this LogAnalyticsObjectCollectionRule.
        The type of collection.
        Accepted values are: LIVE.
        Collection type LIVE indicates to enable log collection from the time of this rule creation,
        and continue until the rule exists.

        Allowed values for this property are: "LIVE", "HISTORIC", "HISTORIC_LIVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The collection_type of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._collection_type

    @collection_type.setter
    def collection_type(self, collection_type):
        """
        Sets the collection_type of this LogAnalyticsObjectCollectionRule.
        The type of collection.
        Accepted values are: LIVE.
        Collection type LIVE indicates to enable log collection from the time of this rule creation,
        and continue until the rule exists.


        :param collection_type: The collection_type of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        allowed_values = ["LIVE", "HISTORIC", "HISTORIC_LIVE"]
        if not value_allowed_none_or_none_sentinel(collection_type, allowed_values):
            collection_type = 'UNKNOWN_ENUM_VALUE'
        self._collection_type = collection_type

    @property
    def poll_since(self):
        """
        **[Required]** Gets the poll_since of this LogAnalyticsObjectCollectionRule.
        The oldest time of the file in the bucket to consider for collection.
        Accepted values are: BEGINNING or CURRENT_TIME or RFC3339 formatted datetime string.
        When collectionType is LIVE, specifying pollSince value other than CURRENT_TIME will result in error.


        :return: The poll_since of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._poll_since

    @poll_since.setter
    def poll_since(self, poll_since):
        """
        Sets the poll_since of this LogAnalyticsObjectCollectionRule.
        The oldest time of the file in the bucket to consider for collection.
        Accepted values are: BEGINNING or CURRENT_TIME or RFC3339 formatted datetime string.
        When collectionType is LIVE, specifying pollSince value other than CURRENT_TIME will result in error.


        :param poll_since: The poll_since of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._poll_since = poll_since

    @property
    def poll_till(self):
        """
        Gets the poll_till of this LogAnalyticsObjectCollectionRule.
        The oldest time of the file in the bucket to consider for collection.
        Accepted values are: CURRENT_TIME or RFC3339 formatted datetime string.
        When collectionType is LIVE, specifying pollTill will result in error.


        :return: The poll_till of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._poll_till

    @poll_till.setter
    def poll_till(self, poll_till):
        """
        Sets the poll_till of this LogAnalyticsObjectCollectionRule.
        The oldest time of the file in the bucket to consider for collection.
        Accepted values are: CURRENT_TIME or RFC3339 formatted datetime string.
        When collectionType is LIVE, specifying pollTill will result in error.


        :param poll_till: The poll_till of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._poll_till = poll_till

    @property
    def log_group_id(self):
        """
        **[Required]** Gets the log_group_id of this LogAnalyticsObjectCollectionRule.
        Log Analytics Log group OCID to associate the processed logs with.


        :return: The log_group_id of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """
        Sets the log_group_id of this LogAnalyticsObjectCollectionRule.
        Log Analytics Log group OCID to associate the processed logs with.


        :param log_group_id: The log_group_id of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._log_group_id = log_group_id

    @property
    def log_source_name(self):
        """
        **[Required]** Gets the log_source_name of this LogAnalyticsObjectCollectionRule.
        Name of the Log Analytics Source to use for the processing.


        :return: The log_source_name of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._log_source_name

    @log_source_name.setter
    def log_source_name(self, log_source_name):
        """
        Sets the log_source_name of this LogAnalyticsObjectCollectionRule.
        Name of the Log Analytics Source to use for the processing.


        :param log_source_name: The log_source_name of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._log_source_name = log_source_name

    @property
    def entity_id(self):
        """
        Gets the entity_id of this LogAnalyticsObjectCollectionRule.
        Log Analytics entity OCID to associate the processed logs with.


        :return: The entity_id of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this LogAnalyticsObjectCollectionRule.
        Log Analytics entity OCID to associate the processed logs with.


        :param entity_id: The entity_id of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def char_encoding(self):
        """
        Gets the char_encoding of this LogAnalyticsObjectCollectionRule.
        An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing.
        It is recommended to set this value as ISO_8589_1 when configuring content of the objects having more numeric characters,
        and very few alphabets.
        For e.g. this applies when configuring VCN Flow Logs.


        :return: The char_encoding of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._char_encoding

    @char_encoding.setter
    def char_encoding(self, char_encoding):
        """
        Sets the char_encoding of this LogAnalyticsObjectCollectionRule.
        An optional character encoding to aid in detecting the character encoding of the contents of the objects while processing.
        It is recommended to set this value as ISO_8589_1 when configuring content of the objects having more numeric characters,
        and very few alphabets.
        For e.g. this applies when configuring VCN Flow Logs.


        :param char_encoding: The char_encoding of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._char_encoding = char_encoding

    @property
    def overrides(self):
        """
        Gets the overrides of this LogAnalyticsObjectCollectionRule.
        Use this to override some property values which are defined at bucket level to the scope of object.
        Supported propeties for override are, logSourceName, charEncoding.
        Supported matchType for override are \"contains\".


        :return: The overrides of this LogAnalyticsObjectCollectionRule.
        :rtype: dict(str, list[PropertyOverride])
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """
        Sets the overrides of this LogAnalyticsObjectCollectionRule.
        Use this to override some property values which are defined at bucket level to the scope of object.
        Supported propeties for override are, logSourceName, charEncoding.
        Supported matchType for override are \"contains\".


        :param overrides: The overrides of this LogAnalyticsObjectCollectionRule.
        :type: dict(str, list[PropertyOverride])
        """
        self._overrides = overrides

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this LogAnalyticsObjectCollectionRule.
        The current state of the rule.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this LogAnalyticsObjectCollectionRule.
        The current state of the rule.


        :param lifecycle_state: The lifecycle_state of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this LogAnalyticsObjectCollectionRule.
        A detailed status of the life cycle state.


        :return: The lifecycle_details of this LogAnalyticsObjectCollectionRule.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this LogAnalyticsObjectCollectionRule.
        A detailed status of the life cycle state.


        :param lifecycle_details: The lifecycle_details of this LogAnalyticsObjectCollectionRule.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this LogAnalyticsObjectCollectionRule.
        The time when this rule was created. An RFC3339 formatted datetime string.


        :return: The time_created of this LogAnalyticsObjectCollectionRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this LogAnalyticsObjectCollectionRule.
        The time when this rule was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this LogAnalyticsObjectCollectionRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this LogAnalyticsObjectCollectionRule.
        The time when this rule was last updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this LogAnalyticsObjectCollectionRule.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsObjectCollectionRule.
        The time when this rule was last updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this LogAnalyticsObjectCollectionRule.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this LogAnalyticsObjectCollectionRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this LogAnalyticsObjectCollectionRule.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this LogAnalyticsObjectCollectionRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this LogAnalyticsObjectCollectionRule.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this LogAnalyticsObjectCollectionRule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this LogAnalyticsObjectCollectionRule.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this LogAnalyticsObjectCollectionRule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this LogAnalyticsObjectCollectionRule.
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
