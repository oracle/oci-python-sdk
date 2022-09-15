# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddAgentDependencyDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddAgentDependencyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param agent_dependency_id:
            The value to assign to the agent_dependency_id property of this AddAgentDependencyDetails.
        :type agent_dependency_id: str

        """
        self.swagger_types = {
            'agent_dependency_id': 'str'
        }

        self.attribute_map = {
            'agent_dependency_id': 'agentDependencyId'
        }

        self._agent_dependency_id = None

    @property
    def agent_dependency_id(self):
        """
        **[Required]** Gets the agent_dependency_id of this AddAgentDependencyDetails.
        The OCID of the agentDependency, which is added to the source environment.


        :return: The agent_dependency_id of this AddAgentDependencyDetails.
        :rtype: str
        """
        return self._agent_dependency_id

    @agent_dependency_id.setter
    def agent_dependency_id(self, agent_dependency_id):
        """
        Sets the agent_dependency_id of this AddAgentDependencyDetails.
        The OCID of the agentDependency, which is added to the source environment.


        :param agent_dependency_id: The agent_dependency_id of this AddAgentDependencyDetails.
        :type: str
        """
        self._agent_dependency_id = agent_dependency_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
