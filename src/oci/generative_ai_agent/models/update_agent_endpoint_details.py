# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20240531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAgentEndpointDetails(object):
    """
    The data to update an endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAgentEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAgentEndpointDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateAgentEndpointDetails.
        :type description: str

        :param content_moderation_config:
            The value to assign to the content_moderation_config property of this UpdateAgentEndpointDetails.
        :type content_moderation_config: oci.generative_ai_agent.models.ContentModerationConfig

        :param should_enable_trace:
            The value to assign to the should_enable_trace property of this UpdateAgentEndpointDetails.
        :type should_enable_trace: bool

        :param should_enable_citation:
            The value to assign to the should_enable_citation property of this UpdateAgentEndpointDetails.
        :type should_enable_citation: bool

        :param session_config:
            The value to assign to the session_config property of this UpdateAgentEndpointDetails.
        :type session_config: oci.generative_ai_agent.models.SessionConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAgentEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAgentEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'content_moderation_config': 'ContentModerationConfig',
            'should_enable_trace': 'bool',
            'should_enable_citation': 'bool',
            'session_config': 'SessionConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'content_moderation_config': 'contentModerationConfig',
            'should_enable_trace': 'shouldEnableTrace',
            'should_enable_citation': 'shouldEnableCitation',
            'session_config': 'sessionConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._description = None
        self._content_moderation_config = None
        self._should_enable_trace = None
        self._should_enable_citation = None
        self._session_config = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAgentEndpointDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateAgentEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAgentEndpointDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateAgentEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateAgentEndpointDetails.
        An optional description of the AgentEndpoint.


        :return: The description of this UpdateAgentEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateAgentEndpointDetails.
        An optional description of the AgentEndpoint.


        :param description: The description of this UpdateAgentEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def content_moderation_config(self):
        """
        Gets the content_moderation_config of this UpdateAgentEndpointDetails.

        :return: The content_moderation_config of this UpdateAgentEndpointDetails.
        :rtype: oci.generative_ai_agent.models.ContentModerationConfig
        """
        return self._content_moderation_config

    @content_moderation_config.setter
    def content_moderation_config(self, content_moderation_config):
        """
        Sets the content_moderation_config of this UpdateAgentEndpointDetails.

        :param content_moderation_config: The content_moderation_config of this UpdateAgentEndpointDetails.
        :type: oci.generative_ai_agent.models.ContentModerationConfig
        """
        self._content_moderation_config = content_moderation_config

    @property
    def should_enable_trace(self):
        """
        Gets the should_enable_trace of this UpdateAgentEndpointDetails.
        Whether to show traces in the chat result.


        :return: The should_enable_trace of this UpdateAgentEndpointDetails.
        :rtype: bool
        """
        return self._should_enable_trace

    @should_enable_trace.setter
    def should_enable_trace(self, should_enable_trace):
        """
        Sets the should_enable_trace of this UpdateAgentEndpointDetails.
        Whether to show traces in the chat result.


        :param should_enable_trace: The should_enable_trace of this UpdateAgentEndpointDetails.
        :type: bool
        """
        self._should_enable_trace = should_enable_trace

    @property
    def should_enable_citation(self):
        """
        Gets the should_enable_citation of this UpdateAgentEndpointDetails.
        Whether to show citations in the chat result.


        :return: The should_enable_citation of this UpdateAgentEndpointDetails.
        :rtype: bool
        """
        return self._should_enable_citation

    @should_enable_citation.setter
    def should_enable_citation(self, should_enable_citation):
        """
        Sets the should_enable_citation of this UpdateAgentEndpointDetails.
        Whether to show citations in the chat result.


        :param should_enable_citation: The should_enable_citation of this UpdateAgentEndpointDetails.
        :type: bool
        """
        self._should_enable_citation = should_enable_citation

    @property
    def session_config(self):
        """
        Gets the session_config of this UpdateAgentEndpointDetails.

        :return: The session_config of this UpdateAgentEndpointDetails.
        :rtype: oci.generative_ai_agent.models.SessionConfig
        """
        return self._session_config

    @session_config.setter
    def session_config(self, session_config):
        """
        Sets the session_config of this UpdateAgentEndpointDetails.

        :param session_config: The session_config of this UpdateAgentEndpointDetails.
        :type: oci.generative_ai_agent.models.SessionConfig
        """
        self._session_config = session_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAgentEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAgentEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAgentEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAgentEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAgentEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAgentEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAgentEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAgentEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
