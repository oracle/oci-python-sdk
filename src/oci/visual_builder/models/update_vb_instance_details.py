# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateVbInstanceDetails(object):
    """
    Information about updating a VbInstance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateVbInstanceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateVbInstanceDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateVbInstanceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateVbInstanceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param idcs_open_id:
            The value to assign to the idcs_open_id property of this UpdateVbInstanceDetails.
        :type idcs_open_id: str

        :param node_count:
            The value to assign to the node_count property of this UpdateVbInstanceDetails.
        :type node_count: int

        :param is_visual_builder_enabled:
            The value to assign to the is_visual_builder_enabled property of this UpdateVbInstanceDetails.
        :type is_visual_builder_enabled: bool

        :param custom_endpoint:
            The value to assign to the custom_endpoint property of this UpdateVbInstanceDetails.
        :type custom_endpoint: oci.visual_builder.models.UpdateCustomEndpointDetails

        :param alternate_custom_endpoints:
            The value to assign to the alternate_custom_endpoints property of this UpdateVbInstanceDetails.
        :type alternate_custom_endpoints: list[oci.visual_builder.models.UpdateCustomEndpointDetails]

        """
        self.swagger_types = {
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'idcs_open_id': 'str',
            'node_count': 'int',
            'is_visual_builder_enabled': 'bool',
            'custom_endpoint': 'UpdateCustomEndpointDetails',
            'alternate_custom_endpoints': 'list[UpdateCustomEndpointDetails]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'idcs_open_id': 'idcsOpenId',
            'node_count': 'nodeCount',
            'is_visual_builder_enabled': 'isVisualBuilderEnabled',
            'custom_endpoint': 'customEndpoint',
            'alternate_custom_endpoints': 'alternateCustomEndpoints'
        }

        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._idcs_open_id = None
        self._node_count = None
        self._is_visual_builder_enabled = None
        self._custom_endpoint = None
        self._alternate_custom_endpoints = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateVbInstanceDetails.
        Vb Instance Identifier.


        :return: The display_name of this UpdateVbInstanceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateVbInstanceDetails.
        Vb Instance Identifier.


        :param display_name: The display_name of this UpdateVbInstanceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateVbInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateVbInstanceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateVbInstanceDetails.
        Simple key-value pair that is applied without any predefined name,
        type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateVbInstanceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateVbInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateVbInstanceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateVbInstanceDetails.
        Usage of predefined tag keys. These predefined keys are scoped to
        namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateVbInstanceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def idcs_open_id(self):
        """
        Gets the idcs_open_id of this UpdateVbInstanceDetails.
        Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter


        :return: The idcs_open_id of this UpdateVbInstanceDetails.
        :rtype: str
        """
        return self._idcs_open_id

    @idcs_open_id.setter
    def idcs_open_id(self, idcs_open_id):
        """
        Sets the idcs_open_id of this UpdateVbInstanceDetails.
        Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter


        :param idcs_open_id: The idcs_open_id of this UpdateVbInstanceDetails.
        :type: str
        """
        self._idcs_open_id = idcs_open_id

    @property
    def node_count(self):
        """
        Gets the node_count of this UpdateVbInstanceDetails.
        The number of Nodes


        :return: The node_count of this UpdateVbInstanceDetails.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """
        Sets the node_count of this UpdateVbInstanceDetails.
        The number of Nodes


        :param node_count: The node_count of this UpdateVbInstanceDetails.
        :type: int
        """
        self._node_count = node_count

    @property
    def is_visual_builder_enabled(self):
        """
        Gets the is_visual_builder_enabled of this UpdateVbInstanceDetails.
        Enable Visual Builder. If Visual Builder is enabled alredy, then it cannot be disabled.


        :return: The is_visual_builder_enabled of this UpdateVbInstanceDetails.
        :rtype: bool
        """
        return self._is_visual_builder_enabled

    @is_visual_builder_enabled.setter
    def is_visual_builder_enabled(self, is_visual_builder_enabled):
        """
        Sets the is_visual_builder_enabled of this UpdateVbInstanceDetails.
        Enable Visual Builder. If Visual Builder is enabled alredy, then it cannot be disabled.


        :param is_visual_builder_enabled: The is_visual_builder_enabled of this UpdateVbInstanceDetails.
        :type: bool
        """
        self._is_visual_builder_enabled = is_visual_builder_enabled

    @property
    def custom_endpoint(self):
        """
        Gets the custom_endpoint of this UpdateVbInstanceDetails.

        :return: The custom_endpoint of this UpdateVbInstanceDetails.
        :rtype: oci.visual_builder.models.UpdateCustomEndpointDetails
        """
        return self._custom_endpoint

    @custom_endpoint.setter
    def custom_endpoint(self, custom_endpoint):
        """
        Sets the custom_endpoint of this UpdateVbInstanceDetails.

        :param custom_endpoint: The custom_endpoint of this UpdateVbInstanceDetails.
        :type: oci.visual_builder.models.UpdateCustomEndpointDetails
        """
        self._custom_endpoint = custom_endpoint

    @property
    def alternate_custom_endpoints(self):
        """
        Gets the alternate_custom_endpoints of this UpdateVbInstanceDetails.
        A list of alternate custom endpoints to be used for the vb instance URL
        (contact Oracle for alternateCustomEndpoints availability for a specific instance).


        :return: The alternate_custom_endpoints of this UpdateVbInstanceDetails.
        :rtype: list[oci.visual_builder.models.UpdateCustomEndpointDetails]
        """
        return self._alternate_custom_endpoints

    @alternate_custom_endpoints.setter
    def alternate_custom_endpoints(self, alternate_custom_endpoints):
        """
        Sets the alternate_custom_endpoints of this UpdateVbInstanceDetails.
        A list of alternate custom endpoints to be used for the vb instance URL
        (contact Oracle for alternateCustomEndpoints availability for a specific instance).


        :param alternate_custom_endpoints: The alternate_custom_endpoints of this UpdateVbInstanceDetails.
        :type: list[oci.visual_builder.models.UpdateCustomEndpointDetails]
        """
        self._alternate_custom_endpoints = alternate_custom_endpoints

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
