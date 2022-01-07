# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostInsightSummary(object):
    """
    Summary of a host insight resource.
    """

    #: A constant which can be used with the entity_source property of a HostInsightSummary.
    #: This constant has a value of "MACS_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_MACS_MANAGED_EXTERNAL_HOST = "MACS_MANAGED_EXTERNAL_HOST"

    #: A constant which can be used with the entity_source property of a HostInsightSummary.
    #: This constant has a value of "EM_MANAGED_EXTERNAL_HOST"
    ENTITY_SOURCE_EM_MANAGED_EXTERNAL_HOST = "EM_MANAGED_EXTERNAL_HOST"

    #: A constant which can be used with the status property of a HostInsightSummary.
    #: This constant has a value of "DISABLED"
    STATUS_DISABLED = "DISABLED"

    #: A constant which can be used with the status property of a HostInsightSummary.
    #: This constant has a value of "ENABLED"
    STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the status property of a HostInsightSummary.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a HostInsightSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a HostInsightSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a HostInsightSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a HostInsightSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a HostInsightSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a HostInsightSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a HostInsightSummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new HostInsightSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.MacsManagedExternalHostInsightSummary`
        * :class:`~oci.opsi.models.EmManagedExternalHostInsightSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this HostInsightSummary.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param id:
            The value to assign to the id property of this HostInsightSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this HostInsightSummary.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this HostInsightSummary.
        :type host_name: str

        :param host_display_name:
            The value to assign to the host_display_name property of this HostInsightSummary.
        :type host_display_name: str

        :param host_type:
            The value to assign to the host_type property of this HostInsightSummary.
        :type host_type: str

        :param processor_count:
            The value to assign to the processor_count property of this HostInsightSummary.
        :type processor_count: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this HostInsightSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this HostInsightSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this HostInsightSummary.
        :type system_tags: dict(str, dict(str, object))

        :param status:
            The value to assign to the status property of this HostInsightSummary.
            Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param time_created:
            The value to assign to the time_created property of this HostInsightSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this HostInsightSummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this HostInsightSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this HostInsightSummary.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'host_display_name': 'str',
            'host_type': 'str',
            'processor_count': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'status': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'host_display_name': 'hostDisplayName',
            'host_type': 'hostType',
            'processor_count': 'processorCount',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'status': 'status',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._entity_source = None
        self._id = None
        self._compartment_id = None
        self._host_name = None
        self._host_display_name = None
        self._host_type = None
        self._processor_count = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._status = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entitySource']

        if type == 'MACS_MANAGED_EXTERNAL_HOST':
            return 'MacsManagedExternalHostInsightSummary'

        if type == 'EM_MANAGED_EXTERNAL_HOST':
            return 'EmManagedExternalHostInsightSummary'
        else:
            return 'HostInsightSummary'

    @property
    def entity_source(self):
        """
        **[Required]** Gets the entity_source of this HostInsightSummary.
        Source of the host entity.

        Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_source of this HostInsightSummary.
        :rtype: str
        """
        return self._entity_source

    @entity_source.setter
    def entity_source(self, entity_source):
        """
        Sets the entity_source of this HostInsightSummary.
        Source of the host entity.


        :param entity_source: The entity_source of this HostInsightSummary.
        :type: str
        """
        allowed_values = ["MACS_MANAGED_EXTERNAL_HOST", "EM_MANAGED_EXTERNAL_HOST"]
        if not value_allowed_none_or_none_sentinel(entity_source, allowed_values):
            entity_source = 'UNKNOWN_ENUM_VALUE'
        self._entity_source = entity_source

    @property
    def id(self):
        """
        **[Required]** Gets the id of this HostInsightSummary.
        The `OCID`__ of the host insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this HostInsightSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HostInsightSummary.
        The `OCID`__ of the host insight resource.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this HostInsightSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this HostInsightSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this HostInsightSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HostInsightSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this HostInsightSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this HostInsightSummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :return: The host_name of this HostInsightSummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this HostInsightSummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :param host_name: The host_name of this HostInsightSummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def host_display_name(self):
        """
        Gets the host_display_name of this HostInsightSummary.
        The user-friendly name for the host. The name does not have to be unique.


        :return: The host_display_name of this HostInsightSummary.
        :rtype: str
        """
        return self._host_display_name

    @host_display_name.setter
    def host_display_name(self, host_display_name):
        """
        Sets the host_display_name of this HostInsightSummary.
        The user-friendly name for the host. The name does not have to be unique.


        :param host_display_name: The host_display_name of this HostInsightSummary.
        :type: str
        """
        self._host_display_name = host_display_name

    @property
    def host_type(self):
        """
        Gets the host_type of this HostInsightSummary.
        Operations Insights internal representation of the host type. Possible value is EXTERNAL-HOST.


        :return: The host_type of this HostInsightSummary.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """
        Sets the host_type of this HostInsightSummary.
        Operations Insights internal representation of the host type. Possible value is EXTERNAL-HOST.


        :param host_type: The host_type of this HostInsightSummary.
        :type: str
        """
        self._host_type = host_type

    @property
    def processor_count(self):
        """
        Gets the processor_count of this HostInsightSummary.
        Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.


        :return: The processor_count of this HostInsightSummary.
        :rtype: int
        """
        return self._processor_count

    @processor_count.setter
    def processor_count(self, processor_count):
        """
        Sets the processor_count of this HostInsightSummary.
        Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.


        :param processor_count: The processor_count of this HostInsightSummary.
        :type: int
        """
        self._processor_count = processor_count

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this HostInsightSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this HostInsightSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this HostInsightSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this HostInsightSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this HostInsightSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this HostInsightSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this HostInsightSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this HostInsightSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this HostInsightSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this HostInsightSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this HostInsightSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this HostInsightSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def status(self):
        """
        Gets the status of this HostInsightSummary.
        Indicates the status of a host insight in Operations Insights

        Allowed values for this property are: "DISABLED", "ENABLED", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this HostInsightSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this HostInsightSummary.
        Indicates the status of a host insight in Operations Insights


        :param status: The status of this HostInsightSummary.
        :type: str
        """
        allowed_values = ["DISABLED", "ENABLED", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def time_created(self):
        """
        Gets the time_created of this HostInsightSummary.
        The time the the host insight was first enabled. An RFC3339 formatted datetime string


        :return: The time_created of this HostInsightSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this HostInsightSummary.
        The time the the host insight was first enabled. An RFC3339 formatted datetime string


        :param time_created: The time_created of this HostInsightSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this HostInsightSummary.
        The time the host insight was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this HostInsightSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this HostInsightSummary.
        The time the host insight was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this HostInsightSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this HostInsightSummary.
        The current state of the host.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this HostInsightSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this HostInsightSummary.
        The current state of the host.


        :param lifecycle_state: The lifecycle_state of this HostInsightSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this HostInsightSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this HostInsightSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this HostInsightSummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this HostInsightSummary.
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
