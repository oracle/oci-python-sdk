# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitoredInstanceSummary(object):
    """
    Summary of the monitored instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitoredInstanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_id:
            The value to assign to the instance_id property of this MonitoredInstanceSummary.
        :type instance_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MonitoredInstanceSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MonitoredInstanceSummary.
        :type display_name: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this MonitoredInstanceSummary.
        :type management_agent_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MonitoredInstanceSummary.
        :type lifecycle_state: str

        :param monitoring_state:
            The value to assign to the monitoring_state property of this MonitoredInstanceSummary.
        :type monitoring_state: str

        """
        self.swagger_types = {
            'instance_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'management_agent_id': 'str',
            'lifecycle_state': 'str',
            'monitoring_state': 'str'
        }

        self.attribute_map = {
            'instance_id': 'instanceId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'management_agent_id': 'managementAgentId',
            'lifecycle_state': 'lifecycleState',
            'monitoring_state': 'monitoringState'
        }

        self._instance_id = None
        self._compartment_id = None
        self._display_name = None
        self._management_agent_id = None
        self._lifecycle_state = None
        self._monitoring_state = None

    @property
    def instance_id(self):
        """
        **[Required]** Gets the instance_id of this MonitoredInstanceSummary.
        The `OCID`__ of monitored instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The instance_id of this MonitoredInstanceSummary.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this MonitoredInstanceSummary.
        The `OCID`__ of monitored instance.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param instance_id: The instance_id of this MonitoredInstanceSummary.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MonitoredInstanceSummary.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this MonitoredInstanceSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MonitoredInstanceSummary.
        Compartment Identifier `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this MonitoredInstanceSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this MonitoredInstanceSummary.
        A user-friendly name of the monitored instance. It is binded to `Compute Instance`__.
        DisplayName is fetched from `Core Service API`__.

        __ https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm
        __ https://docs.cloud.oracle.com/api/#/en/iaas/20160918/Instance/


        :return: The display_name of this MonitoredInstanceSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MonitoredInstanceSummary.
        A user-friendly name of the monitored instance. It is binded to `Compute Instance`__.
        DisplayName is fetched from `Core Service API`__.

        __ https://docs.cloud.oracle.com/Content/Compute/Concepts/computeoverview.htm
        __ https://docs.cloud.oracle.com/api/#/en/iaas/20160918/Instance/


        :param display_name: The display_name of this MonitoredInstanceSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def management_agent_id(self):
        """
        Gets the management_agent_id of this MonitoredInstanceSummary.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The management_agent_id of this MonitoredInstanceSummary.
        :rtype: str
        """
        return self._management_agent_id

    @management_agent_id.setter
    def management_agent_id(self, management_agent_id):
        """
        Sets the management_agent_id of this MonitoredInstanceSummary.
        Management Agent Identifier `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param management_agent_id: The management_agent_id of this MonitoredInstanceSummary.
        :type: str
        """
        self._management_agent_id = management_agent_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this MonitoredInstanceSummary.
        The current state of the monitored instance.


        :return: The lifecycle_state of this MonitoredInstanceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MonitoredInstanceSummary.
        The current state of the monitored instance.


        :param lifecycle_state: The lifecycle_state of this MonitoredInstanceSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def monitoring_state(self):
        """
        Gets the monitoring_state of this MonitoredInstanceSummary.
        Monitoring status. Can be either enabled or disabled.


        :return: The monitoring_state of this MonitoredInstanceSummary.
        :rtype: str
        """
        return self._monitoring_state

    @monitoring_state.setter
    def monitoring_state(self, monitoring_state):
        """
        Sets the monitoring_state of this MonitoredInstanceSummary.
        Monitoring status. Can be either enabled or disabled.


        :param monitoring_state: The monitoring_state of this MonitoredInstanceSummary.
        :type: str
        """
        self._monitoring_state = monitoring_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
