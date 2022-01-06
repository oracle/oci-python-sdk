# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnterpriseManagerBridge(object):
    """
    Enterprise Manager bridge resource.
    """

    #: A constant which can be used with the lifecycle_state property of a EnterpriseManagerBridge.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a EnterpriseManagerBridge.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a EnterpriseManagerBridge.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EnterpriseManagerBridge.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a EnterpriseManagerBridge.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a EnterpriseManagerBridge.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a EnterpriseManagerBridge.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new EnterpriseManagerBridge object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EnterpriseManagerBridge.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EnterpriseManagerBridge.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this EnterpriseManagerBridge.
        :type display_name: str

        :param description:
            The value to assign to the description property of this EnterpriseManagerBridge.
        :type description: str

        :param object_storage_namespace_name:
            The value to assign to the object_storage_namespace_name property of this EnterpriseManagerBridge.
        :type object_storage_namespace_name: str

        :param object_storage_bucket_name:
            The value to assign to the object_storage_bucket_name property of this EnterpriseManagerBridge.
        :type object_storage_bucket_name: str

        :param object_storage_bucket_status_details:
            The value to assign to the object_storage_bucket_status_details property of this EnterpriseManagerBridge.
        :type object_storage_bucket_status_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EnterpriseManagerBridge.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EnterpriseManagerBridge.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EnterpriseManagerBridge.
        :type system_tags: dict(str, dict(str, object))

        :param time_created:
            The value to assign to the time_created property of this EnterpriseManagerBridge.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EnterpriseManagerBridge.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EnterpriseManagerBridge.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EnterpriseManagerBridge.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'object_storage_namespace_name': 'str',
            'object_storage_bucket_name': 'str',
            'object_storage_bucket_status_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'object_storage_namespace_name': 'objectStorageNamespaceName',
            'object_storage_bucket_name': 'objectStorageBucketName',
            'object_storage_bucket_status_details': 'objectStorageBucketStatusDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._object_storage_namespace_name = None
        self._object_storage_bucket_name = None
        self._object_storage_bucket_status_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EnterpriseManagerBridge.
        Enterprise Manager bridge identifier


        :return: The id of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EnterpriseManagerBridge.
        Enterprise Manager bridge identifier


        :param id: The id of this EnterpriseManagerBridge.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EnterpriseManagerBridge.
        Compartment identifier of the Enterprise Manager bridge


        :return: The compartment_id of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EnterpriseManagerBridge.
        Compartment identifier of the Enterprise Manager bridge


        :param compartment_id: The compartment_id of this EnterpriseManagerBridge.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this EnterpriseManagerBridge.
        User-friedly name of Enterprise Manager Bridge that does not have to be unique.


        :return: The display_name of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EnterpriseManagerBridge.
        User-friedly name of Enterprise Manager Bridge that does not have to be unique.


        :param display_name: The display_name of this EnterpriseManagerBridge.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this EnterpriseManagerBridge.
        Description of Enterprise Manager Bridge


        :return: The description of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EnterpriseManagerBridge.
        Description of Enterprise Manager Bridge


        :param description: The description of this EnterpriseManagerBridge.
        :type: str
        """
        self._description = description

    @property
    def object_storage_namespace_name(self):
        """
        **[Required]** Gets the object_storage_namespace_name of this EnterpriseManagerBridge.
        Object Storage Namespace Name


        :return: The object_storage_namespace_name of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._object_storage_namespace_name

    @object_storage_namespace_name.setter
    def object_storage_namespace_name(self, object_storage_namespace_name):
        """
        Sets the object_storage_namespace_name of this EnterpriseManagerBridge.
        Object Storage Namespace Name


        :param object_storage_namespace_name: The object_storage_namespace_name of this EnterpriseManagerBridge.
        :type: str
        """
        self._object_storage_namespace_name = object_storage_namespace_name

    @property
    def object_storage_bucket_name(self):
        """
        **[Required]** Gets the object_storage_bucket_name of this EnterpriseManagerBridge.
        Object Storage Bucket Name


        :return: The object_storage_bucket_name of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._object_storage_bucket_name

    @object_storage_bucket_name.setter
    def object_storage_bucket_name(self, object_storage_bucket_name):
        """
        Sets the object_storage_bucket_name of this EnterpriseManagerBridge.
        Object Storage Bucket Name


        :param object_storage_bucket_name: The object_storage_bucket_name of this EnterpriseManagerBridge.
        :type: str
        """
        self._object_storage_bucket_name = object_storage_bucket_name

    @property
    def object_storage_bucket_status_details(self):
        """
        Gets the object_storage_bucket_status_details of this EnterpriseManagerBridge.
        A message describing status of the object storage bucket of this resource. For example, it can be used to provide actionable information about the permission and content validity of the bucket.


        :return: The object_storage_bucket_status_details of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._object_storage_bucket_status_details

    @object_storage_bucket_status_details.setter
    def object_storage_bucket_status_details(self, object_storage_bucket_status_details):
        """
        Sets the object_storage_bucket_status_details of this EnterpriseManagerBridge.
        A message describing status of the object storage bucket of this resource. For example, it can be used to provide actionable information about the permission and content validity of the bucket.


        :param object_storage_bucket_status_details: The object_storage_bucket_status_details of this EnterpriseManagerBridge.
        :type: str
        """
        self._object_storage_bucket_status_details = object_storage_bucket_status_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this EnterpriseManagerBridge.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EnterpriseManagerBridge.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EnterpriseManagerBridge.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EnterpriseManagerBridge.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this EnterpriseManagerBridge.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EnterpriseManagerBridge.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EnterpriseManagerBridge.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EnterpriseManagerBridge.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EnterpriseManagerBridge.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this EnterpriseManagerBridge.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EnterpriseManagerBridge.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this EnterpriseManagerBridge.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this EnterpriseManagerBridge.
        The time the the Enterprise Manager bridge was first created. An RFC3339 formatted datetime string


        :return: The time_created of this EnterpriseManagerBridge.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EnterpriseManagerBridge.
        The time the the Enterprise Manager bridge was first created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this EnterpriseManagerBridge.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EnterpriseManagerBridge.
        The time the Enterprise Manager bridge was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this EnterpriseManagerBridge.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EnterpriseManagerBridge.
        The time the Enterprise Manager bridge was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this EnterpriseManagerBridge.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this EnterpriseManagerBridge.
        The current state of the Enterprise Manager bridge.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EnterpriseManagerBridge.
        The current state of the Enterprise Manager bridge.


        :param lifecycle_state: The lifecycle_state of this EnterpriseManagerBridge.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this EnterpriseManagerBridge.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this EnterpriseManagerBridge.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this EnterpriseManagerBridge.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this EnterpriseManagerBridge.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
