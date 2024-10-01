# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IntegrationInstance(object):
    """
    Description of Integration Instance.
    """

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstance.
    #: This constant has a value of "STANDARD"
    INTEGRATION_INSTANCE_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstance.
    #: This constant has a value of "ENTERPRISE"
    INTEGRATION_INSTANCE_TYPE_ENTERPRISE = "ENTERPRISE"

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstance.
    #: This constant has a value of "STANDARDX"
    INTEGRATION_INSTANCE_TYPE_STANDARDX = "STANDARDX"

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstance.
    #: This constant has a value of "ENTERPRISEX"
    INTEGRATION_INSTANCE_TYPE_ENTERPRISEX = "ENTERPRISEX"

    #: A constant which can be used with the integration_instance_type property of a IntegrationInstance.
    #: This constant has a value of "HEALTHCARE"
    INTEGRATION_INSTANCE_TYPE_HEALTHCARE = "HEALTHCARE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a IntegrationInstance.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the consumption_model property of a IntegrationInstance.
    #: This constant has a value of "UCM"
    CONSUMPTION_MODEL_UCM = "UCM"

    #: A constant which can be used with the consumption_model property of a IntegrationInstance.
    #: This constant has a value of "GOV"
    CONSUMPTION_MODEL_GOV = "GOV"

    #: A constant which can be used with the consumption_model property of a IntegrationInstance.
    #: This constant has a value of "OIC4SAAS"
    CONSUMPTION_MODEL_OIC4_SAAS = "OIC4SAAS"

    #: A constant which can be used with the shape property of a IntegrationInstance.
    #: This constant has a value of "DEVELOPMENT"
    SHAPE_DEVELOPMENT = "DEVELOPMENT"

    #: A constant which can be used with the shape property of a IntegrationInstance.
    #: This constant has a value of "PRODUCTION"
    SHAPE_PRODUCTION = "PRODUCTION"

    #: A constant which can be used with the data_retention_period property of a IntegrationInstance.
    #: This constant has a value of "MONTHS_1"
    DATA_RETENTION_PERIOD_MONTHS_1 = "MONTHS_1"

    #: A constant which can be used with the data_retention_period property of a IntegrationInstance.
    #: This constant has a value of "MONTHS_3"
    DATA_RETENTION_PERIOD_MONTHS_3 = "MONTHS_3"

    #: A constant which can be used with the data_retention_period property of a IntegrationInstance.
    #: This constant has a value of "MONTHS_6"
    DATA_RETENTION_PERIOD_MONTHS_6 = "MONTHS_6"

    def __init__(self, **kwargs):
        """
        Initializes a new IntegrationInstance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IntegrationInstance.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this IntegrationInstance.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IntegrationInstance.
        :type compartment_id: str

        :param integration_instance_type:
            The value to assign to the integration_instance_type property of this IntegrationInstance.
            Allowed values for this property are: "STANDARD", "ENTERPRISE", "STANDARDX", "ENTERPRISEX", "HEALTHCARE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type integration_instance_type: str

        :param time_created:
            The value to assign to the time_created property of this IntegrationInstance.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this IntegrationInstance.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IntegrationInstance.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this IntegrationInstance.
        :type lifecycle_details: str

        :param state_message:
            The value to assign to the state_message property of this IntegrationInstance.
        :type state_message: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this IntegrationInstance.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this IntegrationInstance.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this IntegrationInstance.
        :type system_tags: dict(str, dict(str, object))

        :param is_byol:
            The value to assign to the is_byol property of this IntegrationInstance.
        :type is_byol: bool

        :param instance_url:
            The value to assign to the instance_url property of this IntegrationInstance.
        :type instance_url: str

        :param instance_design_time_url:
            The value to assign to the instance_design_time_url property of this IntegrationInstance.
        :type instance_design_time_url: str

        :param message_packs:
            The value to assign to the message_packs property of this IntegrationInstance.
        :type message_packs: int

        :param is_file_server_enabled:
            The value to assign to the is_file_server_enabled property of this IntegrationInstance.
        :type is_file_server_enabled: bool

        :param is_visual_builder_enabled:
            The value to assign to the is_visual_builder_enabled property of this IntegrationInstance.
        :type is_visual_builder_enabled: bool

        :param custom_endpoint:
            The value to assign to the custom_endpoint property of this IntegrationInstance.
        :type custom_endpoint: oci.integration.models.CustomEndpointDetails

        :param alternate_custom_endpoints:
            The value to assign to the alternate_custom_endpoints property of this IntegrationInstance.
        :type alternate_custom_endpoints: list[oci.integration.models.CustomEndpointDetails]

        :param consumption_model:
            The value to assign to the consumption_model property of this IntegrationInstance.
            Allowed values for this property are: "UCM", "GOV", "OIC4SAAS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type consumption_model: str

        :param network_endpoint_details:
            The value to assign to the network_endpoint_details property of this IntegrationInstance.
        :type network_endpoint_details: oci.integration.models.NetworkEndpointDetails

        :param idcs_info:
            The value to assign to the idcs_info property of this IntegrationInstance.
        :type idcs_info: oci.integration.models.IdcsInfoDetails

        :param attachments:
            The value to assign to the attachments property of this IntegrationInstance.
        :type attachments: list[oci.integration.models.AttachmentDetails]

        :param shape:
            The value to assign to the shape property of this IntegrationInstance.
            Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type shape: str

        :param private_endpoint_outbound_connection:
            The value to assign to the private_endpoint_outbound_connection property of this IntegrationInstance.
        :type private_endpoint_outbound_connection: oci.integration.models.OutboundConnection

        :param is_disaster_recovery_enabled:
            The value to assign to the is_disaster_recovery_enabled property of this IntegrationInstance.
        :type is_disaster_recovery_enabled: bool

        :param disaster_recovery_details:
            The value to assign to the disaster_recovery_details property of this IntegrationInstance.
        :type disaster_recovery_details: oci.integration.models.DisasterRecoveryDetails

        :param data_retention_period:
            The value to assign to the data_retention_period property of this IntegrationInstance.
            Allowed values for this property are: "MONTHS_1", "MONTHS_3", "MONTHS_6", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_retention_period: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'integration_instance_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'state_message': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'is_byol': 'bool',
            'instance_url': 'str',
            'instance_design_time_url': 'str',
            'message_packs': 'int',
            'is_file_server_enabled': 'bool',
            'is_visual_builder_enabled': 'bool',
            'custom_endpoint': 'CustomEndpointDetails',
            'alternate_custom_endpoints': 'list[CustomEndpointDetails]',
            'consumption_model': 'str',
            'network_endpoint_details': 'NetworkEndpointDetails',
            'idcs_info': 'IdcsInfoDetails',
            'attachments': 'list[AttachmentDetails]',
            'shape': 'str',
            'private_endpoint_outbound_connection': 'OutboundConnection',
            'is_disaster_recovery_enabled': 'bool',
            'disaster_recovery_details': 'DisasterRecoveryDetails',
            'data_retention_period': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'integration_instance_type': 'integrationInstanceType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'state_message': 'stateMessage',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'is_byol': 'isByol',
            'instance_url': 'instanceUrl',
            'instance_design_time_url': 'instanceDesignTimeUrl',
            'message_packs': 'messagePacks',
            'is_file_server_enabled': 'isFileServerEnabled',
            'is_visual_builder_enabled': 'isVisualBuilderEnabled',
            'custom_endpoint': 'customEndpoint',
            'alternate_custom_endpoints': 'alternateCustomEndpoints',
            'consumption_model': 'consumptionModel',
            'network_endpoint_details': 'networkEndpointDetails',
            'idcs_info': 'idcsInfo',
            'attachments': 'attachments',
            'shape': 'shape',
            'private_endpoint_outbound_connection': 'privateEndpointOutboundConnection',
            'is_disaster_recovery_enabled': 'isDisasterRecoveryEnabled',
            'disaster_recovery_details': 'disasterRecoveryDetails',
            'data_retention_period': 'dataRetentionPeriod'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._integration_instance_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._state_message = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._is_byol = None
        self._instance_url = None
        self._instance_design_time_url = None
        self._message_packs = None
        self._is_file_server_enabled = None
        self._is_visual_builder_enabled = None
        self._custom_endpoint = None
        self._alternate_custom_endpoints = None
        self._consumption_model = None
        self._network_endpoint_details = None
        self._idcs_info = None
        self._attachments = None
        self._shape = None
        self._private_endpoint_outbound_connection = None
        self._is_disaster_recovery_enabled = None
        self._disaster_recovery_details = None
        self._data_retention_period = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IntegrationInstance.
        Unique identifier that is immutable on creation.


        :return: The id of this IntegrationInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IntegrationInstance.
        Unique identifier that is immutable on creation.


        :param id: The id of this IntegrationInstance.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this IntegrationInstance.
        Integration Instance Identifier, can be renamed.


        :return: The display_name of this IntegrationInstance.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IntegrationInstance.
        Integration Instance Identifier, can be renamed.


        :param display_name: The display_name of this IntegrationInstance.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IntegrationInstance.
        Compartment Identifier.


        :return: The compartment_id of this IntegrationInstance.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IntegrationInstance.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this IntegrationInstance.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def integration_instance_type(self):
        """
        **[Required]** Gets the integration_instance_type of this IntegrationInstance.
        Standard or Enterprise type,
        Oracle Integration Generation 2 uses ENTERPRISE and STANDARD,
        Oracle Integration 3 uses ENTERPRISEX and STANDARDX

        Allowed values for this property are: "STANDARD", "ENTERPRISE", "STANDARDX", "ENTERPRISEX", "HEALTHCARE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The integration_instance_type of this IntegrationInstance.
        :rtype: str
        """
        return self._integration_instance_type

    @integration_instance_type.setter
    def integration_instance_type(self, integration_instance_type):
        """
        Sets the integration_instance_type of this IntegrationInstance.
        Standard or Enterprise type,
        Oracle Integration Generation 2 uses ENTERPRISE and STANDARD,
        Oracle Integration 3 uses ENTERPRISEX and STANDARDX


        :param integration_instance_type: The integration_instance_type of this IntegrationInstance.
        :type: str
        """
        allowed_values = ["STANDARD", "ENTERPRISE", "STANDARDX", "ENTERPRISEX", "HEALTHCARE"]
        if not value_allowed_none_or_none_sentinel(integration_instance_type, allowed_values):
            integration_instance_type = 'UNKNOWN_ENUM_VALUE'
        self._integration_instance_type = integration_instance_type

    @property
    def time_created(self):
        """
        Gets the time_created of this IntegrationInstance.
        The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.


        :return: The time_created of this IntegrationInstance.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IntegrationInstance.
        The time the the IntegrationInstance was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this IntegrationInstance.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this IntegrationInstance.
        The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this IntegrationInstance.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this IntegrationInstance.
        The time the IntegrationInstance was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this IntegrationInstance.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this IntegrationInstance.
        The current state of the integration instance.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IntegrationInstance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IntegrationInstance.
        The current state of the integration instance.


        :param lifecycle_state: The lifecycle_state of this IntegrationInstance.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this IntegrationInstance.
        Additional details of lifecycleState or substates


        :return: The lifecycle_details of this IntegrationInstance.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this IntegrationInstance.
        Additional details of lifecycleState or substates


        :param lifecycle_details: The lifecycle_details of this IntegrationInstance.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def state_message(self):
        """
        Gets the state_message of this IntegrationInstance.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this IntegrationInstance.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this IntegrationInstance.
        An message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this IntegrationInstance.
        :type: str
        """
        self._state_message = state_message

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this IntegrationInstance.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this IntegrationInstance.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this IntegrationInstance.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this IntegrationInstance.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this IntegrationInstance.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this IntegrationInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this IntegrationInstance.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this IntegrationInstance.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this IntegrationInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this IntegrationInstance.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this IntegrationInstance.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this IntegrationInstance.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def is_byol(self):
        """
        **[Required]** Gets the is_byol of this IntegrationInstance.
        Bring your own license.


        :return: The is_byol of this IntegrationInstance.
        :rtype: bool
        """
        return self._is_byol

    @is_byol.setter
    def is_byol(self, is_byol):
        """
        Sets the is_byol of this IntegrationInstance.
        Bring your own license.


        :param is_byol: The is_byol of this IntegrationInstance.
        :type: bool
        """
        self._is_byol = is_byol

    @property
    def instance_url(self):
        """
        **[Required]** Gets the instance_url of this IntegrationInstance.
        The Integration Instance URL.


        :return: The instance_url of this IntegrationInstance.
        :rtype: str
        """
        return self._instance_url

    @instance_url.setter
    def instance_url(self, instance_url):
        """
        Sets the instance_url of this IntegrationInstance.
        The Integration Instance URL.


        :param instance_url: The instance_url of this IntegrationInstance.
        :type: str
        """
        self._instance_url = instance_url

    @property
    def instance_design_time_url(self):
        """
        Gets the instance_design_time_url of this IntegrationInstance.
        The Integration Instance Design Time URL


        :return: The instance_design_time_url of this IntegrationInstance.
        :rtype: str
        """
        return self._instance_design_time_url

    @instance_design_time_url.setter
    def instance_design_time_url(self, instance_design_time_url):
        """
        Sets the instance_design_time_url of this IntegrationInstance.
        The Integration Instance Design Time URL


        :param instance_design_time_url: The instance_design_time_url of this IntegrationInstance.
        :type: str
        """
        self._instance_design_time_url = instance_design_time_url

    @property
    def message_packs(self):
        """
        **[Required]** Gets the message_packs of this IntegrationInstance.
        The number of configured message packs (if any)


        :return: The message_packs of this IntegrationInstance.
        :rtype: int
        """
        return self._message_packs

    @message_packs.setter
    def message_packs(self, message_packs):
        """
        Sets the message_packs of this IntegrationInstance.
        The number of configured message packs (if any)


        :param message_packs: The message_packs of this IntegrationInstance.
        :type: int
        """
        self._message_packs = message_packs

    @property
    def is_file_server_enabled(self):
        """
        Gets the is_file_server_enabled of this IntegrationInstance.
        The file server is enabled or not.


        :return: The is_file_server_enabled of this IntegrationInstance.
        :rtype: bool
        """
        return self._is_file_server_enabled

    @is_file_server_enabled.setter
    def is_file_server_enabled(self, is_file_server_enabled):
        """
        Sets the is_file_server_enabled of this IntegrationInstance.
        The file server is enabled or not.


        :param is_file_server_enabled: The is_file_server_enabled of this IntegrationInstance.
        :type: bool
        """
        self._is_file_server_enabled = is_file_server_enabled

    @property
    def is_visual_builder_enabled(self):
        """
        Gets the is_visual_builder_enabled of this IntegrationInstance.
        VisualBuilder is enabled or not.


        :return: The is_visual_builder_enabled of this IntegrationInstance.
        :rtype: bool
        """
        return self._is_visual_builder_enabled

    @is_visual_builder_enabled.setter
    def is_visual_builder_enabled(self, is_visual_builder_enabled):
        """
        Sets the is_visual_builder_enabled of this IntegrationInstance.
        VisualBuilder is enabled or not.


        :param is_visual_builder_enabled: The is_visual_builder_enabled of this IntegrationInstance.
        :type: bool
        """
        self._is_visual_builder_enabled = is_visual_builder_enabled

    @property
    def custom_endpoint(self):
        """
        Gets the custom_endpoint of this IntegrationInstance.

        :return: The custom_endpoint of this IntegrationInstance.
        :rtype: oci.integration.models.CustomEndpointDetails
        """
        return self._custom_endpoint

    @custom_endpoint.setter
    def custom_endpoint(self, custom_endpoint):
        """
        Sets the custom_endpoint of this IntegrationInstance.

        :param custom_endpoint: The custom_endpoint of this IntegrationInstance.
        :type: oci.integration.models.CustomEndpointDetails
        """
        self._custom_endpoint = custom_endpoint

    @property
    def alternate_custom_endpoints(self):
        """
        Gets the alternate_custom_endpoints of this IntegrationInstance.
        A list of alternate custom endpoints used for the integration instance URL.


        :return: The alternate_custom_endpoints of this IntegrationInstance.
        :rtype: list[oci.integration.models.CustomEndpointDetails]
        """
        return self._alternate_custom_endpoints

    @alternate_custom_endpoints.setter
    def alternate_custom_endpoints(self, alternate_custom_endpoints):
        """
        Sets the alternate_custom_endpoints of this IntegrationInstance.
        A list of alternate custom endpoints used for the integration instance URL.


        :param alternate_custom_endpoints: The alternate_custom_endpoints of this IntegrationInstance.
        :type: list[oci.integration.models.CustomEndpointDetails]
        """
        self._alternate_custom_endpoints = alternate_custom_endpoints

    @property
    def consumption_model(self):
        """
        Gets the consumption_model of this IntegrationInstance.
        The entitlement used for billing purposes.

        Allowed values for this property are: "UCM", "GOV", "OIC4SAAS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The consumption_model of this IntegrationInstance.
        :rtype: str
        """
        return self._consumption_model

    @consumption_model.setter
    def consumption_model(self, consumption_model):
        """
        Sets the consumption_model of this IntegrationInstance.
        The entitlement used for billing purposes.


        :param consumption_model: The consumption_model of this IntegrationInstance.
        :type: str
        """
        allowed_values = ["UCM", "GOV", "OIC4SAAS"]
        if not value_allowed_none_or_none_sentinel(consumption_model, allowed_values):
            consumption_model = 'UNKNOWN_ENUM_VALUE'
        self._consumption_model = consumption_model

    @property
    def network_endpoint_details(self):
        """
        Gets the network_endpoint_details of this IntegrationInstance.

        :return: The network_endpoint_details of this IntegrationInstance.
        :rtype: oci.integration.models.NetworkEndpointDetails
        """
        return self._network_endpoint_details

    @network_endpoint_details.setter
    def network_endpoint_details(self, network_endpoint_details):
        """
        Sets the network_endpoint_details of this IntegrationInstance.

        :param network_endpoint_details: The network_endpoint_details of this IntegrationInstance.
        :type: oci.integration.models.NetworkEndpointDetails
        """
        self._network_endpoint_details = network_endpoint_details

    @property
    def idcs_info(self):
        """
        Gets the idcs_info of this IntegrationInstance.

        :return: The idcs_info of this IntegrationInstance.
        :rtype: oci.integration.models.IdcsInfoDetails
        """
        return self._idcs_info

    @idcs_info.setter
    def idcs_info(self, idcs_info):
        """
        Sets the idcs_info of this IntegrationInstance.

        :param idcs_info: The idcs_info of this IntegrationInstance.
        :type: oci.integration.models.IdcsInfoDetails
        """
        self._idcs_info = idcs_info

    @property
    def attachments(self):
        """
        Gets the attachments of this IntegrationInstance.
        A list of associated attachments to other services


        :return: The attachments of this IntegrationInstance.
        :rtype: list[oci.integration.models.AttachmentDetails]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this IntegrationInstance.
        A list of associated attachments to other services


        :param attachments: The attachments of this IntegrationInstance.
        :type: list[oci.integration.models.AttachmentDetails]
        """
        self._attachments = attachments

    @property
    def shape(self):
        """
        Gets the shape of this IntegrationInstance.
        Shape

        Allowed values for this property are: "DEVELOPMENT", "PRODUCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The shape of this IntegrationInstance.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this IntegrationInstance.
        Shape


        :param shape: The shape of this IntegrationInstance.
        :type: str
        """
        allowed_values = ["DEVELOPMENT", "PRODUCTION"]
        if not value_allowed_none_or_none_sentinel(shape, allowed_values):
            shape = 'UNKNOWN_ENUM_VALUE'
        self._shape = shape

    @property
    def private_endpoint_outbound_connection(self):
        """
        Gets the private_endpoint_outbound_connection of this IntegrationInstance.

        :return: The private_endpoint_outbound_connection of this IntegrationInstance.
        :rtype: oci.integration.models.OutboundConnection
        """
        return self._private_endpoint_outbound_connection

    @private_endpoint_outbound_connection.setter
    def private_endpoint_outbound_connection(self, private_endpoint_outbound_connection):
        """
        Sets the private_endpoint_outbound_connection of this IntegrationInstance.

        :param private_endpoint_outbound_connection: The private_endpoint_outbound_connection of this IntegrationInstance.
        :type: oci.integration.models.OutboundConnection
        """
        self._private_endpoint_outbound_connection = private_endpoint_outbound_connection

    @property
    def is_disaster_recovery_enabled(self):
        """
        Gets the is_disaster_recovery_enabled of this IntegrationInstance.
        Is Disaster Recovery enabled for the integrationInstance


        :return: The is_disaster_recovery_enabled of this IntegrationInstance.
        :rtype: bool
        """
        return self._is_disaster_recovery_enabled

    @is_disaster_recovery_enabled.setter
    def is_disaster_recovery_enabled(self, is_disaster_recovery_enabled):
        """
        Sets the is_disaster_recovery_enabled of this IntegrationInstance.
        Is Disaster Recovery enabled for the integrationInstance


        :param is_disaster_recovery_enabled: The is_disaster_recovery_enabled of this IntegrationInstance.
        :type: bool
        """
        self._is_disaster_recovery_enabled = is_disaster_recovery_enabled

    @property
    def disaster_recovery_details(self):
        """
        Gets the disaster_recovery_details of this IntegrationInstance.

        :return: The disaster_recovery_details of this IntegrationInstance.
        :rtype: oci.integration.models.DisasterRecoveryDetails
        """
        return self._disaster_recovery_details

    @disaster_recovery_details.setter
    def disaster_recovery_details(self, disaster_recovery_details):
        """
        Sets the disaster_recovery_details of this IntegrationInstance.

        :param disaster_recovery_details: The disaster_recovery_details of this IntegrationInstance.
        :type: oci.integration.models.DisasterRecoveryDetails
        """
        self._disaster_recovery_details = disaster_recovery_details

    @property
    def data_retention_period(self):
        """
        Gets the data_retention_period of this IntegrationInstance.
        Data retention period set for given integration instance

        Allowed values for this property are: "MONTHS_1", "MONTHS_3", "MONTHS_6", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_retention_period of this IntegrationInstance.
        :rtype: str
        """
        return self._data_retention_period

    @data_retention_period.setter
    def data_retention_period(self, data_retention_period):
        """
        Sets the data_retention_period of this IntegrationInstance.
        Data retention period set for given integration instance


        :param data_retention_period: The data_retention_period of this IntegrationInstance.
        :type: str
        """
        allowed_values = ["MONTHS_1", "MONTHS_3", "MONTHS_6"]
        if not value_allowed_none_or_none_sentinel(data_retention_period, allowed_values):
            data_retention_period = 'UNKNOWN_ENUM_VALUE'
        self._data_retention_period = data_retention_period

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
