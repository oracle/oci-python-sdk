# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIntegrationInstanceDetails(object):
    """
    The information about new IntegrationInstance.
    """

    #: A constant which can be used with the integration_instance_type property of a CreateIntegrationInstanceDetails.
    #: This constant has a value of "STANDARD"
    INTEGRATION_INSTANCE_TYPE_STANDARD = "STANDARD"

    #: A constant which can be used with the integration_instance_type property of a CreateIntegrationInstanceDetails.
    #: This constant has a value of "ENTERPRISE"
    INTEGRATION_INSTANCE_TYPE_ENTERPRISE = "ENTERPRISE"

    #: A constant which can be used with the consumption_model property of a CreateIntegrationInstanceDetails.
    #: This constant has a value of "UCM"
    CONSUMPTION_MODEL_UCM = "UCM"

    #: A constant which can be used with the consumption_model property of a CreateIntegrationInstanceDetails.
    #: This constant has a value of "GOV"
    CONSUMPTION_MODEL_GOV = "GOV"

    #: A constant which can be used with the consumption_model property of a CreateIntegrationInstanceDetails.
    #: This constant has a value of "OIC4SAAS"
    CONSUMPTION_MODEL_OIC4_SAAS = "OIC4SAAS"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIntegrationInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateIntegrationInstanceDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateIntegrationInstanceDetails.
        :type compartment_id: str

        :param integration_instance_type:
            The value to assign to the integration_instance_type property of this CreateIntegrationInstanceDetails.
            Allowed values for this property are: "STANDARD", "ENTERPRISE"
        :type integration_instance_type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateIntegrationInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateIntegrationInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param is_byol:
            The value to assign to the is_byol property of this CreateIntegrationInstanceDetails.
        :type is_byol: bool

        :param idcs_at:
            The value to assign to the idcs_at property of this CreateIntegrationInstanceDetails.
        :type idcs_at: str

        :param message_packs:
            The value to assign to the message_packs property of this CreateIntegrationInstanceDetails.
        :type message_packs: int

        :param is_visual_builder_enabled:
            The value to assign to the is_visual_builder_enabled property of this CreateIntegrationInstanceDetails.
        :type is_visual_builder_enabled: bool

        :param custom_endpoint:
            The value to assign to the custom_endpoint property of this CreateIntegrationInstanceDetails.
        :type custom_endpoint: oci.integration.models.CreateCustomEndpointDetails

        :param alternate_custom_endpoints:
            The value to assign to the alternate_custom_endpoints property of this CreateIntegrationInstanceDetails.
        :type alternate_custom_endpoints: list[oci.integration.models.CreateCustomEndpointDetails]

        :param consumption_model:
            The value to assign to the consumption_model property of this CreateIntegrationInstanceDetails.
            Allowed values for this property are: "UCM", "GOV", "OIC4SAAS"
        :type consumption_model: str

        :param is_file_server_enabled:
            The value to assign to the is_file_server_enabled property of this CreateIntegrationInstanceDetails.
        :type is_file_server_enabled: bool

        :param network_endpoint_details:
            The value to assign to the network_endpoint_details property of this CreateIntegrationInstanceDetails.
        :type network_endpoint_details: oci.integration.models.NetworkEndpointDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'integration_instance_type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'is_byol': 'bool',
            'idcs_at': 'str',
            'message_packs': 'int',
            'is_visual_builder_enabled': 'bool',
            'custom_endpoint': 'CreateCustomEndpointDetails',
            'alternate_custom_endpoints': 'list[CreateCustomEndpointDetails]',
            'consumption_model': 'str',
            'is_file_server_enabled': 'bool',
            'network_endpoint_details': 'NetworkEndpointDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'integration_instance_type': 'integrationInstanceType',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'is_byol': 'isByol',
            'idcs_at': 'idcsAt',
            'message_packs': 'messagePacks',
            'is_visual_builder_enabled': 'isVisualBuilderEnabled',
            'custom_endpoint': 'customEndpoint',
            'alternate_custom_endpoints': 'alternateCustomEndpoints',
            'consumption_model': 'consumptionModel',
            'is_file_server_enabled': 'isFileServerEnabled',
            'network_endpoint_details': 'networkEndpointDetails'
        }

        self._display_name = None
        self._compartment_id = None
        self._integration_instance_type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._is_byol = None
        self._idcs_at = None
        self._message_packs = None
        self._is_visual_builder_enabled = None
        self._custom_endpoint = None
        self._alternate_custom_endpoints = None
        self._consumption_model = None
        self._is_file_server_enabled = None
        self._network_endpoint_details = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateIntegrationInstanceDetails.
        Integration Instance Identifier.


        :return: The display_name of this CreateIntegrationInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateIntegrationInstanceDetails.
        Integration Instance Identifier.


        :param display_name: The display_name of this CreateIntegrationInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateIntegrationInstanceDetails.
        Compartment Identifier.


        :return: The compartment_id of this CreateIntegrationInstanceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIntegrationInstanceDetails.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this CreateIntegrationInstanceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def integration_instance_type(self):
        """
        **[Required]** Gets the integration_instance_type of this CreateIntegrationInstanceDetails.
        Standard or Enterprise type

        Allowed values for this property are: "STANDARD", "ENTERPRISE"


        :return: The integration_instance_type of this CreateIntegrationInstanceDetails.
        :rtype: str
        """
        return self._integration_instance_type

    @integration_instance_type.setter
    def integration_instance_type(self, integration_instance_type):
        """
        Sets the integration_instance_type of this CreateIntegrationInstanceDetails.
        Standard or Enterprise type


        :param integration_instance_type: The integration_instance_type of this CreateIntegrationInstanceDetails.
        :type: str
        """
        allowed_values = ["STANDARD", "ENTERPRISE"]
        if not value_allowed_none_or_none_sentinel(integration_instance_type, allowed_values):
            raise ValueError(
                "Invalid value for `integration_instance_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._integration_instance_type = integration_instance_type

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateIntegrationInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateIntegrationInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateIntegrationInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateIntegrationInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateIntegrationInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateIntegrationInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateIntegrationInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateIntegrationInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def is_byol(self):
        """
        **[Required]** Gets the is_byol of this CreateIntegrationInstanceDetails.
        Bring your own license.


        :return: The is_byol of this CreateIntegrationInstanceDetails.
        :rtype: bool
        """
        return self._is_byol

    @is_byol.setter
    def is_byol(self, is_byol):
        """
        Sets the is_byol of this CreateIntegrationInstanceDetails.
        Bring your own license.


        :param is_byol: The is_byol of this CreateIntegrationInstanceDetails.
        :type: bool
        """
        self._is_byol = is_byol

    @property
    def idcs_at(self):
        """
        Gets the idcs_at of this CreateIntegrationInstanceDetails.
        IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.


        :return: The idcs_at of this CreateIntegrationInstanceDetails.
        :rtype: str
        """
        return self._idcs_at

    @idcs_at.setter
    def idcs_at(self, idcs_at):
        """
        Sets the idcs_at of this CreateIntegrationInstanceDetails.
        IDCS Authentication token. This is required for all realms with IDCS. Its optional as its not required for non IDCS realms.


        :param idcs_at: The idcs_at of this CreateIntegrationInstanceDetails.
        :type: str
        """
        self._idcs_at = idcs_at

    @property
    def message_packs(self):
        """
        **[Required]** Gets the message_packs of this CreateIntegrationInstanceDetails.
        The number of configured message packs


        :return: The message_packs of this CreateIntegrationInstanceDetails.
        :rtype: int
        """
        return self._message_packs

    @message_packs.setter
    def message_packs(self, message_packs):
        """
        Sets the message_packs of this CreateIntegrationInstanceDetails.
        The number of configured message packs


        :param message_packs: The message_packs of this CreateIntegrationInstanceDetails.
        :type: int
        """
        self._message_packs = message_packs

    @property
    def is_visual_builder_enabled(self):
        """
        Gets the is_visual_builder_enabled of this CreateIntegrationInstanceDetails.
        Visual Builder is enabled or not.


        :return: The is_visual_builder_enabled of this CreateIntegrationInstanceDetails.
        :rtype: bool
        """
        return self._is_visual_builder_enabled

    @is_visual_builder_enabled.setter
    def is_visual_builder_enabled(self, is_visual_builder_enabled):
        """
        Sets the is_visual_builder_enabled of this CreateIntegrationInstanceDetails.
        Visual Builder is enabled or not.


        :param is_visual_builder_enabled: The is_visual_builder_enabled of this CreateIntegrationInstanceDetails.
        :type: bool
        """
        self._is_visual_builder_enabled = is_visual_builder_enabled

    @property
    def custom_endpoint(self):
        """
        Gets the custom_endpoint of this CreateIntegrationInstanceDetails.

        :return: The custom_endpoint of this CreateIntegrationInstanceDetails.
        :rtype: oci.integration.models.CreateCustomEndpointDetails
        """
        return self._custom_endpoint

    @custom_endpoint.setter
    def custom_endpoint(self, custom_endpoint):
        """
        Sets the custom_endpoint of this CreateIntegrationInstanceDetails.

        :param custom_endpoint: The custom_endpoint of this CreateIntegrationInstanceDetails.
        :type: oci.integration.models.CreateCustomEndpointDetails
        """
        self._custom_endpoint = custom_endpoint

    @property
    def alternate_custom_endpoints(self):
        """
        Gets the alternate_custom_endpoints of this CreateIntegrationInstanceDetails.
        A list of alternate custom endpoints to be used for the integration instance URL
        (contact Oracle for alternateCustomEndpoints availability for a specific instance).


        :return: The alternate_custom_endpoints of this CreateIntegrationInstanceDetails.
        :rtype: list[oci.integration.models.CreateCustomEndpointDetails]
        """
        return self._alternate_custom_endpoints

    @alternate_custom_endpoints.setter
    def alternate_custom_endpoints(self, alternate_custom_endpoints):
        """
        Sets the alternate_custom_endpoints of this CreateIntegrationInstanceDetails.
        A list of alternate custom endpoints to be used for the integration instance URL
        (contact Oracle for alternateCustomEndpoints availability for a specific instance).


        :param alternate_custom_endpoints: The alternate_custom_endpoints of this CreateIntegrationInstanceDetails.
        :type: list[oci.integration.models.CreateCustomEndpointDetails]
        """
        self._alternate_custom_endpoints = alternate_custom_endpoints

    @property
    def consumption_model(self):
        """
        Gets the consumption_model of this CreateIntegrationInstanceDetails.
        Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.

        Allowed values for this property are: "UCM", "GOV", "OIC4SAAS"


        :return: The consumption_model of this CreateIntegrationInstanceDetails.
        :rtype: str
        """
        return self._consumption_model

    @consumption_model.setter
    def consumption_model(self, consumption_model):
        """
        Sets the consumption_model of this CreateIntegrationInstanceDetails.
        Optional parameter specifying which entitlement to use for billing purposes. Only required if the account possesses more than one entitlement.


        :param consumption_model: The consumption_model of this CreateIntegrationInstanceDetails.
        :type: str
        """
        allowed_values = ["UCM", "GOV", "OIC4SAAS"]
        if not value_allowed_none_or_none_sentinel(consumption_model, allowed_values):
            raise ValueError(
                "Invalid value for `consumption_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._consumption_model = consumption_model

    @property
    def is_file_server_enabled(self):
        """
        Gets the is_file_server_enabled of this CreateIntegrationInstanceDetails.
        The file server is enabled or not.


        :return: The is_file_server_enabled of this CreateIntegrationInstanceDetails.
        :rtype: bool
        """
        return self._is_file_server_enabled

    @is_file_server_enabled.setter
    def is_file_server_enabled(self, is_file_server_enabled):
        """
        Sets the is_file_server_enabled of this CreateIntegrationInstanceDetails.
        The file server is enabled or not.


        :param is_file_server_enabled: The is_file_server_enabled of this CreateIntegrationInstanceDetails.
        :type: bool
        """
        self._is_file_server_enabled = is_file_server_enabled

    @property
    def network_endpoint_details(self):
        """
        Gets the network_endpoint_details of this CreateIntegrationInstanceDetails.

        :return: The network_endpoint_details of this CreateIntegrationInstanceDetails.
        :rtype: oci.integration.models.NetworkEndpointDetails
        """
        return self._network_endpoint_details

    @network_endpoint_details.setter
    def network_endpoint_details(self, network_endpoint_details):
        """
        Sets the network_endpoint_details of this CreateIntegrationInstanceDetails.

        :param network_endpoint_details: The network_endpoint_details of this CreateIntegrationInstanceDetails.
        :type: oci.integration.models.NetworkEndpointDetails
        """
        self._network_endpoint_details = network_endpoint_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
