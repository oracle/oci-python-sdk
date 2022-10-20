# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDrPlanExecutionDetails(object):
    """
    The details for creating a DR Plan Execution.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDrPlanExecutionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDrPlanExecutionDetails.
        :type display_name: str

        :param plan_id:
            The value to assign to the plan_id property of this CreateDrPlanExecutionDetails.
        :type plan_id: str

        :param execution_options:
            The value to assign to the execution_options property of this CreateDrPlanExecutionDetails.
        :type execution_options: oci.disaster_recovery.models.DrPlanExecutionOptionDetails

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDrPlanExecutionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDrPlanExecutionDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'plan_id': 'str',
            'execution_options': 'DrPlanExecutionOptionDetails',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'plan_id': 'planId',
            'execution_options': 'executionOptions',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._plan_id = None
        self._execution_options = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDrPlanExecutionDetails.
        The display name of the DR Plan Execution.

        Example: `Execution - EBS Switchover PHX to IAD`


        :return: The display_name of this CreateDrPlanExecutionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDrPlanExecutionDetails.
        The display name of the DR Plan Execution.

        Example: `Execution - EBS Switchover PHX to IAD`


        :param display_name: The display_name of this CreateDrPlanExecutionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def plan_id(self):
        """
        **[Required]** Gets the plan_id of this CreateDrPlanExecutionDetails.
        The OCID of the DR Plan.

        Example: `ocid1.drplan.oc1.iad.exampleocid2`


        :return: The plan_id of this CreateDrPlanExecutionDetails.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this CreateDrPlanExecutionDetails.
        The OCID of the DR Plan.

        Example: `ocid1.drplan.oc1.iad.exampleocid2`


        :param plan_id: The plan_id of this CreateDrPlanExecutionDetails.
        :type: str
        """
        self._plan_id = plan_id

    @property
    def execution_options(self):
        """
        **[Required]** Gets the execution_options of this CreateDrPlanExecutionDetails.

        :return: The execution_options of this CreateDrPlanExecutionDetails.
        :rtype: oci.disaster_recovery.models.DrPlanExecutionOptionDetails
        """
        return self._execution_options

    @execution_options.setter
    def execution_options(self, execution_options):
        """
        Sets the execution_options of this CreateDrPlanExecutionDetails.

        :param execution_options: The execution_options of this CreateDrPlanExecutionDetails.
        :type: oci.disaster_recovery.models.DrPlanExecutionOptionDetails
        """
        self._execution_options = execution_options

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDrPlanExecutionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :return: The freeform_tags of this CreateDrPlanExecutionDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDrPlanExecutionDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"Department\": \"Finance\"}`


        :param freeform_tags: The freeform_tags of this CreateDrPlanExecutionDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDrPlanExecutionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :return: The defined_tags of this CreateDrPlanExecutionDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDrPlanExecutionDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`


        :param defined_tags: The defined_tags of this CreateDrPlanExecutionDetails.
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
