# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAgentDetails(object):
    """
    Information about the new Agent.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAgentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateAgentDetails.
        :type display_name: str

        :param agent_type:
            The value to assign to the agent_type property of this CreateAgentDetails.
        :type agent_type: str

        :param agent_version:
            The value to assign to the agent_version property of this CreateAgentDetails.
        :type agent_version: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAgentDetails.
        :type compartment_id: str

        :param environment_id:
            The value to assign to the environment_id property of this CreateAgentDetails.
        :type environment_id: str

        :param os_version:
            The value to assign to the os_version property of this CreateAgentDetails.
        :type os_version: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAgentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAgentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'agent_type': 'str',
            'agent_version': 'str',
            'compartment_id': 'str',
            'environment_id': 'str',
            'os_version': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'agent_type': 'agentType',
            'agent_version': 'agentVersion',
            'compartment_id': 'compartmentId',
            'environment_id': 'environmentId',
            'os_version': 'osVersion',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._agent_type = None
        self._agent_version = None
        self._compartment_id = None
        self._environment_id = None
        self._os_version = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateAgentDetails.
        Agent identifier.


        :return: The display_name of this CreateAgentDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAgentDetails.
        Agent identifier.


        :param display_name: The display_name of this CreateAgentDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def agent_type(self):
        """
        **[Required]** Gets the agent_type of this CreateAgentDetails.
        Agent identifier.


        :return: The agent_type of this CreateAgentDetails.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        """
        Sets the agent_type of this CreateAgentDetails.
        Agent identifier.


        :param agent_type: The agent_type of this CreateAgentDetails.
        :type: str
        """
        self._agent_type = agent_type

    @property
    def agent_version(self):
        """
        **[Required]** Gets the agent_version of this CreateAgentDetails.
        Agent identifier.


        :return: The agent_version of this CreateAgentDetails.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """
        Sets the agent_version of this CreateAgentDetails.
        Agent identifier.


        :param agent_version: The agent_version of this CreateAgentDetails.
        :type: str
        """
        self._agent_version = agent_version

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAgentDetails.
        Compartment identifier.


        :return: The compartment_id of this CreateAgentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAgentDetails.
        Compartment identifier.


        :param compartment_id: The compartment_id of this CreateAgentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def environment_id(self):
        """
        **[Required]** Gets the environment_id of this CreateAgentDetails.
        Environment identifier.


        :return: The environment_id of this CreateAgentDetails.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """
        Sets the environment_id of this CreateAgentDetails.
        Environment identifier.


        :param environment_id: The environment_id of this CreateAgentDetails.
        :type: str
        """
        self._environment_id = environment_id

    @property
    def os_version(self):
        """
        **[Required]** Gets the os_version of this CreateAgentDetails.
        OS version.


        :return: The os_version of this CreateAgentDetails.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this CreateAgentDetails.
        OS version.


        :param os_version: The os_version of this CreateAgentDetails.
        :type: str
        """
        self._os_version = os_version

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAgentDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAgentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAgentDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace/scope. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAgentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAgentDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAgentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAgentDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAgentDetails.
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
