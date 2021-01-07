# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkflowStep(object):
    """
    Workflow step of workflow monitor.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkflowStep object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_name:
            The value to assign to the step_name property of this WorkflowStep.
        :type step_name: str

        :param status:
            The value to assign to the status property of this WorkflowStep.
        :type status: str

        """
        self.swagger_types = {
            'step_name': 'str',
            'status': 'str'
        }

        self.attribute_map = {
            'step_name': 'stepName',
            'status': 'status'
        }

        self._step_name = None
        self._status = None

    @property
    def step_name(self):
        """
        Gets the step_name of this WorkflowStep.
        workflow step name


        :return: The step_name of this WorkflowStep.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this WorkflowStep.
        workflow step name


        :param step_name: The step_name of this WorkflowStep.
        :type: str
        """
        self._step_name = step_name

    @property
    def status(self):
        """
        Gets the status of this WorkflowStep.
        workflow step status


        :return: The status of this WorkflowStep.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkflowStep.
        workflow step status


        :param status: The status of this WorkflowStep.
        :type: str
        """
        self._status = status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
