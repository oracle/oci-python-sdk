# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .task_details import TaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogRuleTaskDetails(TaskDetails):
    """
    The log rule task.
    For configuration instructions, see
    `To create a service connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/service-connector-hub/managingconnectors.htm#create
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogRuleTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.LogRuleTaskDetails.kind` attribute
        of this class is ``logRule`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this LogRuleTaskDetails.
            Allowed values for this property are: "function", "logRule"
        :type kind: str

        :param condition:
            The value to assign to the condition property of this LogRuleTaskDetails.
        :type condition: str

        """
        self.swagger_types = {
            'kind': 'str',
            'condition': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'condition': 'condition'
        }

        self._kind = None
        self._condition = None
        self._kind = 'logRule'

    @property
    def condition(self):
        """
        **[Required]** Gets the condition of this LogRuleTaskDetails.
        A filter or mask to limit the source used in the flow defined by the service connector.


        :return: The condition of this LogRuleTaskDetails.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this LogRuleTaskDetails.
        A filter or mask to limit the source used in the flow defined by the service connector.


        :param condition: The condition of this LogRuleTaskDetails.
        :type: str
        """
        self._condition = condition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
