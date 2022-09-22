# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredResourceMemberSummary(object):
    """
    Monitored resource member
    """

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceMemberSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceMemberSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceMemberSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceMemberSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceMemberSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MonitoredResourceMemberSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredResourceMemberSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_id:
            The value to assign to the resource_id property of this MonitoredResourceMemberSummary.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this MonitoredResourceMemberSummary.
        :type resource_name: str

        :param resource_display_name:
            The value to assign to the resource_display_name property of this MonitoredResourceMemberSummary.
        :type resource_display_name: str

        :param resource_type:
            The value to assign to the resource_type property of this MonitoredResourceMemberSummary.
        :type resource_type: str

        :param host_name:
            The value to assign to the host_name property of this MonitoredResourceMemberSummary.
        :type host_name: str

        :param external_id:
            The value to assign to the external_id property of this MonitoredResourceMemberSummary.
        :type external_id: str

        :param parent_id:
            The value to assign to the parent_id property of this MonitoredResourceMemberSummary.
        :type parent_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoredResourceMemberSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MonitoredResourceMemberSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MonitoredResourceMemberSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MonitoredResourceMemberSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_display_name': 'str',
            'resource_type': 'str',
            'host_name': 'str',
            'external_id': 'str',
            'parent_id': 'str',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_display_name': 'resourceDisplayName',
            'resource_type': 'resourceType',
            'host_name': 'hostName',
            'external_id': 'externalId',
            'parent_id': 'parentId',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._resource_id = None
        self._resource_name = None
        self._resource_display_name = None
        self._resource_type = None
        self._host_name = None
        self._external_id = None
        self._parent_id = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def resource_id(self):
        """
        Gets the resource_id of this MonitoredResourceMemberSummary.
        Monitored resource identifier


        :return: The resource_id of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this MonitoredResourceMemberSummary.
        Monitored resource identifier


        :param resource_id: The resource_id of this MonitoredResourceMemberSummary.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        Gets the resource_name of this MonitoredResourceMemberSummary.
        Monitored resource name


        :return: The resource_name of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this MonitoredResourceMemberSummary.
        Monitored resource name


        :param resource_name: The resource_name of this MonitoredResourceMemberSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_display_name(self):
        """
        Gets the resource_display_name of this MonitoredResourceMemberSummary.
        Monitored resource display name.


        :return: The resource_display_name of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._resource_display_name

    @resource_display_name.setter
    def resource_display_name(self, resource_display_name):
        """
        Sets the resource_display_name of this MonitoredResourceMemberSummary.
        Monitored resource display name.


        :param resource_display_name: The resource_display_name of this MonitoredResourceMemberSummary.
        :type: str
        """
        self._resource_display_name = resource_display_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this MonitoredResourceMemberSummary.
        Monitored resource type


        :return: The resource_type of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this MonitoredResourceMemberSummary.
        Monitored resource type


        :param resource_type: The resource_type of this MonitoredResourceMemberSummary.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def host_name(self):
        """
        Gets the host_name of this MonitoredResourceMemberSummary.
        Monitored Resource Host


        :return: The host_name of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this MonitoredResourceMemberSummary.
        Monitored Resource Host


        :param host_name: The host_name of this MonitoredResourceMemberSummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def external_id(self):
        """
        Gets the external_id of this MonitoredResourceMemberSummary.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource type identifiers - externalcontainerdatabase,
        externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The external_id of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this MonitoredResourceMemberSummary.
        External resource is any OCI resource identifier `OCID`__
        which is not a Stack Monitoring service resource.
        Currently supports only following resource type identifiers - externalcontainerdatabase,
        externalnoncontainerdatabase, externalpluggabledatabase and OCI compute instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param external_id: The external_id of this MonitoredResourceMemberSummary.
        :type: str
        """
        self._external_id = external_id

    @property
    def parent_id(self):
        """
        Gets the parent_id of this MonitoredResourceMemberSummary.
        Parent monitored resource identifier


        :return: The parent_id of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this MonitoredResourceMemberSummary.
        Parent monitored resource identifier


        :param parent_id: The parent_id of this MonitoredResourceMemberSummary.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MonitoredResourceMemberSummary.
        The current state of the Resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MonitoredResourceMemberSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoredResourceMemberSummary.
        The current state of the Resource.


        :param lifecycle_state: The lifecycle_state of this MonitoredResourceMemberSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MonitoredResourceMemberSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MonitoredResourceMemberSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MonitoredResourceMemberSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MonitoredResourceMemberSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MonitoredResourceMemberSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MonitoredResourceMemberSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MonitoredResourceMemberSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MonitoredResourceMemberSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MonitoredResourceMemberSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MonitoredResourceMemberSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MonitoredResourceMemberSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MonitoredResourceMemberSummary.
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
