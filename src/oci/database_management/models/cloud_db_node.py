# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloudDbNode(object):
    """
    The details of a cloud database node.
    """

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "NOT_CONNECTED"
    LIFECYCLE_STATE_NOT_CONNECTED = "NOT_CONNECTED"

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a CloudDbNode.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new CloudDbNode object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CloudDbNode.
        :type id: str

        :param dbaas_id:
            The value to assign to the dbaas_id property of this CloudDbNode.
        :type dbaas_id: str

        :param display_name:
            The value to assign to the display_name property of this CloudDbNode.
        :type display_name: str

        :param component_name:
            The value to assign to the component_name property of this CloudDbNode.
        :type component_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloudDbNode.
        :type compartment_id: str

        :param cloud_db_system_id:
            The value to assign to the cloud_db_system_id property of this CloudDbNode.
        :type cloud_db_system_id: str

        :param cloud_connector_id:
            The value to assign to the cloud_connector_id property of this CloudDbNode.
        :type cloud_connector_id: str

        :param host_name:
            The value to assign to the host_name property of this CloudDbNode.
        :type host_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CloudDbNode.
        :type cpu_core_count: float

        :param memory_size_in_gbs:
            The value to assign to the memory_size_in_gbs property of this CloudDbNode.
        :type memory_size_in_gbs: float

        :param additional_details:
            The value to assign to the additional_details property of this CloudDbNode.
        :type additional_details: dict(str, str)

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CloudDbNode.
            Allowed values for this property are: "CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this CloudDbNode.
        :type lifecycle_details: str

        :param domain_name:
            The value to assign to the domain_name property of this CloudDbNode.
        :type domain_name: str

        :param time_created:
            The value to assign to the time_created property of this CloudDbNode.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this CloudDbNode.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CloudDbNode.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CloudDbNode.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this CloudDbNode.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'dbaas_id': 'str',
            'display_name': 'str',
            'component_name': 'str',
            'compartment_id': 'str',
            'cloud_db_system_id': 'str',
            'cloud_connector_id': 'str',
            'host_name': 'str',
            'cpu_core_count': 'float',
            'memory_size_in_gbs': 'float',
            'additional_details': 'dict(str, str)',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'domain_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'id': 'id',
            'dbaas_id': 'dbaasId',
            'display_name': 'displayName',
            'component_name': 'componentName',
            'compartment_id': 'compartmentId',
            'cloud_db_system_id': 'cloudDbSystemId',
            'cloud_connector_id': 'cloudConnectorId',
            'host_name': 'hostName',
            'cpu_core_count': 'cpuCoreCount',
            'memory_size_in_gbs': 'memorySizeInGBs',
            'additional_details': 'additionalDetails',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'domain_name': 'domainName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }
        self._id = None
        self._dbaas_id = None
        self._display_name = None
        self._component_name = None
        self._compartment_id = None
        self._cloud_db_system_id = None
        self._cloud_connector_id = None
        self._host_name = None
        self._cpu_core_count = None
        self._memory_size_in_gbs = None
        self._additional_details = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._domain_name = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this CloudDbNode.
        The `OCID`__ of the cloud DB node.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this CloudDbNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudDbNode.
        The `OCID`__ of the cloud DB node.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this CloudDbNode.
        :type: str
        """
        self._id = id

    @property
    def dbaas_id(self):
        """
        Gets the dbaas_id of this CloudDbNode.
        The `OCID`__ of the cloud DB node in DBaas service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The dbaas_id of this CloudDbNode.
        :rtype: str
        """
        return self._dbaas_id

    @dbaas_id.setter
    def dbaas_id(self, dbaas_id):
        """
        Sets the dbaas_id of this CloudDbNode.
        The `OCID`__ of the cloud DB node in DBaas service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param dbaas_id: The dbaas_id of this CloudDbNode.
        :type: str
        """
        self._dbaas_id = dbaas_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CloudDbNode.
        The user-friendly name for the cloud DB node. The name does not have to be unique.


        :return: The display_name of this CloudDbNode.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CloudDbNode.
        The user-friendly name for the cloud DB node. The name does not have to be unique.


        :param display_name: The display_name of this CloudDbNode.
        :type: str
        """
        self._display_name = display_name

    @property
    def component_name(self):
        """
        **[Required]** Gets the component_name of this CloudDbNode.
        The name of the cloud DB node.


        :return: The component_name of this CloudDbNode.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this CloudDbNode.
        The name of the cloud DB node.


        :param component_name: The component_name of this CloudDbNode.
        :type: str
        """
        self._component_name = component_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CloudDbNode.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CloudDbNode.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CloudDbNode.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CloudDbNode.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cloud_db_system_id(self):
        """
        **[Required]** Gets the cloud_db_system_id of this CloudDbNode.
        The `OCID`__ of the cloud DB system that the DB node is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_db_system_id of this CloudDbNode.
        :rtype: str
        """
        return self._cloud_db_system_id

    @cloud_db_system_id.setter
    def cloud_db_system_id(self, cloud_db_system_id):
        """
        Sets the cloud_db_system_id of this CloudDbNode.
        The `OCID`__ of the cloud DB system that the DB node is a part of.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_db_system_id: The cloud_db_system_id of this CloudDbNode.
        :type: str
        """
        self._cloud_db_system_id = cloud_db_system_id

    @property
    def cloud_connector_id(self):
        """
        Gets the cloud_connector_id of this CloudDbNode.
        The `OCID`__ of the cloud connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The cloud_connector_id of this CloudDbNode.
        :rtype: str
        """
        return self._cloud_connector_id

    @cloud_connector_id.setter
    def cloud_connector_id(self, cloud_connector_id):
        """
        Sets the cloud_connector_id of this CloudDbNode.
        The `OCID`__ of the cloud connector.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param cloud_connector_id: The cloud_connector_id of this CloudDbNode.
        :type: str
        """
        self._cloud_connector_id = cloud_connector_id

    @property
    def host_name(self):
        """
        Gets the host_name of this CloudDbNode.
        The host name for the DB node.


        :return: The host_name of this CloudDbNode.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this CloudDbNode.
        The host name for the DB node.


        :param host_name: The host_name of this CloudDbNode.
        :type: str
        """
        self._host_name = host_name

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this CloudDbNode.
        The number of CPU cores available on the DB node.


        :return: The cpu_core_count of this CloudDbNode.
        :rtype: float
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CloudDbNode.
        The number of CPU cores available on the DB node.


        :param cpu_core_count: The cpu_core_count of this CloudDbNode.
        :type: float
        """
        self._cpu_core_count = cpu_core_count

    @property
    def memory_size_in_gbs(self):
        """
        Gets the memory_size_in_gbs of this CloudDbNode.
        The total memory in gigabytes (GB) on the DB node.


        :return: The memory_size_in_gbs of this CloudDbNode.
        :rtype: float
        """
        return self._memory_size_in_gbs

    @memory_size_in_gbs.setter
    def memory_size_in_gbs(self, memory_size_in_gbs):
        """
        Sets the memory_size_in_gbs of this CloudDbNode.
        The total memory in gigabytes (GB) on the DB node.


        :param memory_size_in_gbs: The memory_size_in_gbs of this CloudDbNode.
        :type: float
        """
        self._memory_size_in_gbs = memory_size_in_gbs

    @property
    def additional_details(self):
        """
        Gets the additional_details of this CloudDbNode.
        The additional details of the cloud DB node defined in `{\"key\": \"value\"}` format.
        Example: `{\"bar-key\": \"value\"}`


        :return: The additional_details of this CloudDbNode.
        :rtype: dict(str, str)
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this CloudDbNode.
        The additional details of the cloud DB node defined in `{\"key\": \"value\"}` format.
        Example: `{\"bar-key\": \"value\"}`


        :param additional_details: The additional_details of this CloudDbNode.
        :type: dict(str, str)
        """
        self._additional_details = additional_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this CloudDbNode.
        The current lifecycle state of the cloud DB node.

        Allowed values for this property are: "CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CloudDbNode.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CloudDbNode.
        The current lifecycle state of the cloud DB node.


        :param lifecycle_state: The lifecycle_state of this CloudDbNode.
        :type: str
        """
        allowed_values = ["CREATING", "NOT_CONNECTED", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this CloudDbNode.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this CloudDbNode.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this CloudDbNode.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this CloudDbNode.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def domain_name(self):
        """
        Gets the domain_name of this CloudDbNode.
        Name of the domain.


        :return: The domain_name of this CloudDbNode.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this CloudDbNode.
        Name of the domain.


        :param domain_name: The domain_name of this CloudDbNode.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this CloudDbNode.
        The date and time the cloud DB node was created.


        :return: The time_created of this CloudDbNode.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CloudDbNode.
        The date and time the cloud DB node was created.


        :param time_created: The time_created of this CloudDbNode.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this CloudDbNode.
        The date and time the cloud DB node was last updated.


        :return: The time_updated of this CloudDbNode.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this CloudDbNode.
        The date and time the cloud DB node was last updated.


        :param time_updated: The time_updated of this CloudDbNode.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CloudDbNode.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CloudDbNode.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CloudDbNode.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CloudDbNode.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CloudDbNode.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CloudDbNode.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CloudDbNode.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CloudDbNode.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this CloudDbNode.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this CloudDbNode.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this CloudDbNode.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        System tags can be viewed by users, but can only be created by the system.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this CloudDbNode.
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
