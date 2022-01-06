# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkflowMonitor(object):
    """
    The workflow monitor for this work request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkflowMonitor object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param workflow_name:
            The value to assign to the workflow_name property of this WorkflowMonitor.
        :type workflow_name: str

        :param resource_name:
            The value to assign to the resource_name property of this WorkflowMonitor.
        :type resource_name: str

        :param workflow_steps:
            The value to assign to the workflow_steps property of this WorkflowMonitor.
        :type workflow_steps: list[oci.oce.models.WorkflowStep]

        """
        self.swagger_types = {
            'workflow_name': 'str',
            'resource_name': 'str',
            'workflow_steps': 'list[WorkflowStep]'
        }

        self.attribute_map = {
            'workflow_name': 'workflowName',
            'resource_name': 'resourceName',
            'workflow_steps': 'workflowSteps'
        }

        self._workflow_name = None
        self._resource_name = None
        self._workflow_steps = None

    @property
    def workflow_name(self):
        """
        Gets the workflow_name of this WorkflowMonitor.
        workflow name for this work request


        :return: The workflow_name of this WorkflowMonitor.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """
        Sets the workflow_name of this WorkflowMonitor.
        workflow name for this work request


        :param workflow_name: The workflow_name of this WorkflowMonitor.
        :type: str
        """
        self._workflow_name = workflow_name

    @property
    def resource_name(self):
        """
        Gets the resource_name of this WorkflowMonitor.
        resource name for this work request


        :return: The resource_name of this WorkflowMonitor.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this WorkflowMonitor.
        resource name for this work request


        :param resource_name: The resource_name of this WorkflowMonitor.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def workflow_steps(self):
        """
        Gets the workflow_steps of this WorkflowMonitor.
        Workflow step of workflow monitor.


        :return: The workflow_steps of this WorkflowMonitor.
        :rtype: list[oci.oce.models.WorkflowStep]
        """
        return self._workflow_steps

    @workflow_steps.setter
    def workflow_steps(self, workflow_steps):
        """
        Sets the workflow_steps of this WorkflowMonitor.
        Workflow step of workflow monitor.


        :param workflow_steps: The workflow_steps of this WorkflowMonitor.
        :type: list[oci.oce.models.WorkflowStep]
        """
        self._workflow_steps = workflow_steps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
