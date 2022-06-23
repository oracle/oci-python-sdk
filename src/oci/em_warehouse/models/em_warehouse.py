# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EmWarehouse(object):
    """
    Description of EmWarehouse.
    """

    #: A constant which can be used with the lifecycle_state property of a EmWarehouse.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a EmWarehouse.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a EmWarehouse.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EmWarehouse.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a EmWarehouse.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a EmWarehouse.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new EmWarehouse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operations_insights_warehouse_id:
            The value to assign to the operations_insights_warehouse_id property of this EmWarehouse.
        :type operations_insights_warehouse_id: str

        :param latest_etl_run_status:
            The value to assign to the latest_etl_run_status property of this EmWarehouse.
        :type latest_etl_run_status: str

        :param latest_etl_run_message:
            The value to assign to the latest_etl_run_message property of this EmWarehouse.
        :type latest_etl_run_message: str

        :param latest_etl_run_time:
            The value to assign to the latest_etl_run_time property of this EmWarehouse.
        :type latest_etl_run_time: str

        :param id:
            The value to assign to the id property of this EmWarehouse.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this EmWarehouse.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EmWarehouse.
        :type compartment_id: str

        :param em_warehouse_type:
            The value to assign to the em_warehouse_type property of this EmWarehouse.
        :type em_warehouse_type: str

        :param em_bridge_id:
            The value to assign to the em_bridge_id property of this EmWarehouse.
        :type em_bridge_id: str

        :param time_created:
            The value to assign to the time_created property of this EmWarehouse.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EmWarehouse.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EmWarehouse.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this EmWarehouse.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this EmWarehouse.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this EmWarehouse.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this EmWarehouse.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'operations_insights_warehouse_id': 'str',
            'latest_etl_run_status': 'str',
            'latest_etl_run_message': 'str',
            'latest_etl_run_time': 'str',
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'em_warehouse_type': 'str',
            'em_bridge_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'operations_insights_warehouse_id': 'operationsInsightsWarehouseId',
            'latest_etl_run_status': 'latestEtlRunStatus',
            'latest_etl_run_message': 'latestEtlRunMessage',
            'latest_etl_run_time': 'latestEtlRunTime',
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'em_warehouse_type': 'emWarehouseType',
            'em_bridge_id': 'emBridgeId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._operations_insights_warehouse_id = None
        self._latest_etl_run_status = None
        self._latest_etl_run_message = None
        self._latest_etl_run_time = None
        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._em_warehouse_type = None
        self._em_bridge_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def operations_insights_warehouse_id(self):
        """
        **[Required]** Gets the operations_insights_warehouse_id of this EmWarehouse.
        operations Insights Warehouse Identifier


        :return: The operations_insights_warehouse_id of this EmWarehouse.
        :rtype: str
        """
        return self._operations_insights_warehouse_id

    @operations_insights_warehouse_id.setter
    def operations_insights_warehouse_id(self, operations_insights_warehouse_id):
        """
        Sets the operations_insights_warehouse_id of this EmWarehouse.
        operations Insights Warehouse Identifier


        :param operations_insights_warehouse_id: The operations_insights_warehouse_id of this EmWarehouse.
        :type: str
        """
        self._operations_insights_warehouse_id = operations_insights_warehouse_id

    @property
    def latest_etl_run_status(self):
        """
        Gets the latest_etl_run_status of this EmWarehouse.
        Data Flow Run Status


        :return: The latest_etl_run_status of this EmWarehouse.
        :rtype: str
        """
        return self._latest_etl_run_status

    @latest_etl_run_status.setter
    def latest_etl_run_status(self, latest_etl_run_status):
        """
        Sets the latest_etl_run_status of this EmWarehouse.
        Data Flow Run Status


        :param latest_etl_run_status: The latest_etl_run_status of this EmWarehouse.
        :type: str
        """
        self._latest_etl_run_status = latest_etl_run_status

    @property
    def latest_etl_run_message(self):
        """
        Gets the latest_etl_run_message of this EmWarehouse.
        Data Flow Run Status Message


        :return: The latest_etl_run_message of this EmWarehouse.
        :rtype: str
        """
        return self._latest_etl_run_message

    @latest_etl_run_message.setter
    def latest_etl_run_message(self, latest_etl_run_message):
        """
        Sets the latest_etl_run_message of this EmWarehouse.
        Data Flow Run Status Message


        :param latest_etl_run_message: The latest_etl_run_message of this EmWarehouse.
        :type: str
        """
        self._latest_etl_run_message = latest_etl_run_message

    @property
    def latest_etl_run_time(self):
        """
        Gets the latest_etl_run_time of this EmWarehouse.
        Data Flow Run Total Time


        :return: The latest_etl_run_time of this EmWarehouse.
        :rtype: str
        """
        return self._latest_etl_run_time

    @latest_etl_run_time.setter
    def latest_etl_run_time(self, latest_etl_run_time):
        """
        Sets the latest_etl_run_time of this EmWarehouse.
        Data Flow Run Total Time


        :param latest_etl_run_time: The latest_etl_run_time of this EmWarehouse.
        :type: str
        """
        self._latest_etl_run_time = latest_etl_run_time

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EmWarehouse.
        Unique identifier that is immutable on creation


        :return: The id of this EmWarehouse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EmWarehouse.
        Unique identifier that is immutable on creation


        :param id: The id of this EmWarehouse.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this EmWarehouse.
        EmWarehouse Identifier, can be renamed


        :return: The display_name of this EmWarehouse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this EmWarehouse.
        EmWarehouse Identifier, can be renamed


        :param display_name: The display_name of this EmWarehouse.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EmWarehouse.
        Compartment Identifier


        :return: The compartment_id of this EmWarehouse.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EmWarehouse.
        Compartment Identifier


        :param compartment_id: The compartment_id of this EmWarehouse.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def em_warehouse_type(self):
        """
        **[Required]** Gets the em_warehouse_type of this EmWarehouse.
        Type of the EmWarehouse.


        :return: The em_warehouse_type of this EmWarehouse.
        :rtype: str
        """
        return self._em_warehouse_type

    @em_warehouse_type.setter
    def em_warehouse_type(self, em_warehouse_type):
        """
        Sets the em_warehouse_type of this EmWarehouse.
        Type of the EmWarehouse.


        :param em_warehouse_type: The em_warehouse_type of this EmWarehouse.
        :type: str
        """
        self._em_warehouse_type = em_warehouse_type

    @property
    def em_bridge_id(self):
        """
        Gets the em_bridge_id of this EmWarehouse.
        EMBridge Identifier


        :return: The em_bridge_id of this EmWarehouse.
        :rtype: str
        """
        return self._em_bridge_id

    @em_bridge_id.setter
    def em_bridge_id(self, em_bridge_id):
        """
        Sets the em_bridge_id of this EmWarehouse.
        EMBridge Identifier


        :param em_bridge_id: The em_bridge_id of this EmWarehouse.
        :type: str
        """
        self._em_bridge_id = em_bridge_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this EmWarehouse.
        The time the the EmWarehouse was created. An RFC3339 formatted datetime string


        :return: The time_created of this EmWarehouse.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EmWarehouse.
        The time the the EmWarehouse was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this EmWarehouse.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this EmWarehouse.
        The time the EmWarehouse was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this EmWarehouse.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EmWarehouse.
        The time the EmWarehouse was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this EmWarehouse.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this EmWarehouse.
        The current state of the EmWarehouse.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EmWarehouse.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EmWarehouse.
        The current state of the EmWarehouse.


        :param lifecycle_state: The lifecycle_state of this EmWarehouse.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this EmWarehouse.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this EmWarehouse.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this EmWarehouse.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this EmWarehouse.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this EmWarehouse.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this EmWarehouse.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this EmWarehouse.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this EmWarehouse.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this EmWarehouse.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this EmWarehouse.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this EmWarehouse.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this EmWarehouse.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this EmWarehouse.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this EmWarehouse.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this EmWarehouse.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this EmWarehouse.
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
