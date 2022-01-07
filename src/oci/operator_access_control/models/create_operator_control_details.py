# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOperatorControlDetails(object):
    """
    While creating the operator control, specify how operator actions are approved and the users who have the privilege of approving the operator actions associated with the Operator Control.

    You must specify which operator actions must be pre-approved. The rest of the operator actions associated with the Operator Control will require an explicit approval from the users selected either through the approver groups or individually.

    You must name your Operator Control appropriately so it reflects the resources that will be governed by the Operator Control. Neither the Operator Controls nor their assignments to resources are visible to the Oracle operators.
    """

    #: A constant which can be used with the resource_type property of a CreateOperatorControlDetails.
    #: This constant has a value of "EXACC"
    RESOURCE_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the resource_type property of a CreateOperatorControlDetails.
    #: This constant has a value of "EXADATAINFRASTRUCTURE"
    RESOURCE_TYPE_EXADATAINFRASTRUCTURE = "EXADATAINFRASTRUCTURE"

    #: A constant which can be used with the resource_type property of a CreateOperatorControlDetails.
    #: This constant has a value of "AUTONOMOUSVMCLUSTER"
    RESOURCE_TYPE_AUTONOMOUSVMCLUSTER = "AUTONOMOUSVMCLUSTER"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOperatorControlDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operator_control_name:
            The value to assign to the operator_control_name property of this CreateOperatorControlDetails.
        :type operator_control_name: str

        :param description:
            The value to assign to the description property of this CreateOperatorControlDetails.
        :type description: str

        :param approvers_list:
            The value to assign to the approvers_list property of this CreateOperatorControlDetails.
        :type approvers_list: list[str]

        :param approver_groups_list:
            The value to assign to the approver_groups_list property of this CreateOperatorControlDetails.
        :type approver_groups_list: list[str]

        :param pre_approved_op_action_list:
            The value to assign to the pre_approved_op_action_list property of this CreateOperatorControlDetails.
        :type pre_approved_op_action_list: list[str]

        :param is_fully_pre_approved:
            The value to assign to the is_fully_pre_approved property of this CreateOperatorControlDetails.
        :type is_fully_pre_approved: bool

        :param resource_type:
            The value to assign to the resource_type property of this CreateOperatorControlDetails.
            Allowed values for this property are: "EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER"
        :type resource_type: str

        :param email_id_list:
            The value to assign to the email_id_list property of this CreateOperatorControlDetails.
        :type email_id_list: list[str]

        :param system_message:
            The value to assign to the system_message property of this CreateOperatorControlDetails.
        :type system_message: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOperatorControlDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOperatorControlDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOperatorControlDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'operator_control_name': 'str',
            'description': 'str',
            'approvers_list': 'list[str]',
            'approver_groups_list': 'list[str]',
            'pre_approved_op_action_list': 'list[str]',
            'is_fully_pre_approved': 'bool',
            'resource_type': 'str',
            'email_id_list': 'list[str]',
            'system_message': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'operator_control_name': 'operatorControlName',
            'description': 'description',
            'approvers_list': 'approversList',
            'approver_groups_list': 'approverGroupsList',
            'pre_approved_op_action_list': 'preApprovedOpActionList',
            'is_fully_pre_approved': 'isFullyPreApproved',
            'resource_type': 'resourceType',
            'email_id_list': 'emailIdList',
            'system_message': 'systemMessage',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._operator_control_name = None
        self._description = None
        self._approvers_list = None
        self._approver_groups_list = None
        self._pre_approved_op_action_list = None
        self._is_fully_pre_approved = None
        self._resource_type = None
        self._email_id_list = None
        self._system_message = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def operator_control_name(self):
        """
        **[Required]** Gets the operator_control_name of this CreateOperatorControlDetails.
        Name of the operator control.


        :return: The operator_control_name of this CreateOperatorControlDetails.
        :rtype: str
        """
        return self._operator_control_name

    @operator_control_name.setter
    def operator_control_name(self, operator_control_name):
        """
        Sets the operator_control_name of this CreateOperatorControlDetails.
        Name of the operator control.


        :param operator_control_name: The operator_control_name of this CreateOperatorControlDetails.
        :type: str
        """
        self._operator_control_name = operator_control_name

    @property
    def description(self):
        """
        Gets the description of this CreateOperatorControlDetails.
        Description of the operator control.


        :return: The description of this CreateOperatorControlDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateOperatorControlDetails.
        Description of the operator control.


        :param description: The description of this CreateOperatorControlDetails.
        :type: str
        """
        self._description = description

    @property
    def approvers_list(self):
        """
        Gets the approvers_list of this CreateOperatorControlDetails.
        List of users who can approve an access request associated with a resource governed by this operator control.


        :return: The approvers_list of this CreateOperatorControlDetails.
        :rtype: list[str]
        """
        return self._approvers_list

    @approvers_list.setter
    def approvers_list(self, approvers_list):
        """
        Sets the approvers_list of this CreateOperatorControlDetails.
        List of users who can approve an access request associated with a resource governed by this operator control.


        :param approvers_list: The approvers_list of this CreateOperatorControlDetails.
        :type: list[str]
        """
        self._approvers_list = approvers_list

    @property
    def approver_groups_list(self):
        """
        **[Required]** Gets the approver_groups_list of this CreateOperatorControlDetails.
        List of user groups who can approve an access request associated with a resource governed by this operator control.


        :return: The approver_groups_list of this CreateOperatorControlDetails.
        :rtype: list[str]
        """
        return self._approver_groups_list

    @approver_groups_list.setter
    def approver_groups_list(self, approver_groups_list):
        """
        Sets the approver_groups_list of this CreateOperatorControlDetails.
        List of user groups who can approve an access request associated with a resource governed by this operator control.


        :param approver_groups_list: The approver_groups_list of this CreateOperatorControlDetails.
        :type: list[str]
        """
        self._approver_groups_list = approver_groups_list

    @property
    def pre_approved_op_action_list(self):
        """
        Gets the pre_approved_op_action_list of this CreateOperatorControlDetails.
        List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be
        auto-approved if the access request only contain operator actions in the pre-approved list.


        :return: The pre_approved_op_action_list of this CreateOperatorControlDetails.
        :rtype: list[str]
        """
        return self._pre_approved_op_action_list

    @pre_approved_op_action_list.setter
    def pre_approved_op_action_list(self, pre_approved_op_action_list):
        """
        Sets the pre_approved_op_action_list of this CreateOperatorControlDetails.
        List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be
        auto-approved if the access request only contain operator actions in the pre-approved list.


        :param pre_approved_op_action_list: The pre_approved_op_action_list of this CreateOperatorControlDetails.
        :type: list[str]
        """
        self._pre_approved_op_action_list = pre_approved_op_action_list

    @property
    def is_fully_pre_approved(self):
        """
        **[Required]** Gets the is_fully_pre_approved of this CreateOperatorControlDetails.
        Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator control
        will be auto-approved.


        :return: The is_fully_pre_approved of this CreateOperatorControlDetails.
        :rtype: bool
        """
        return self._is_fully_pre_approved

    @is_fully_pre_approved.setter
    def is_fully_pre_approved(self, is_fully_pre_approved):
        """
        Sets the is_fully_pre_approved of this CreateOperatorControlDetails.
        Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator control
        will be auto-approved.


        :param is_fully_pre_approved: The is_fully_pre_approved of this CreateOperatorControlDetails.
        :type: bool
        """
        self._is_fully_pre_approved = is_fully_pre_approved

    @property
    def resource_type(self):
        """
        **[Required]** Gets the resource_type of this CreateOperatorControlDetails.
        resourceType for which the OperatorControl is applicable

        Allowed values for this property are: "EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER"


        :return: The resource_type of this CreateOperatorControlDetails.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this CreateOperatorControlDetails.
        resourceType for which the OperatorControl is applicable


        :param resource_type: The resource_type of this CreateOperatorControlDetails.
        :type: str
        """
        allowed_values = ["EXACC", "EXADATAINFRASTRUCTURE", "AUTONOMOUSVMCLUSTER"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            raise ValueError(
                "Invalid value for `resource_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._resource_type = resource_type

    @property
    def email_id_list(self):
        """
        Gets the email_id_list of this CreateOperatorControlDetails.
        List of emailId.


        :return: The email_id_list of this CreateOperatorControlDetails.
        :rtype: list[str]
        """
        return self._email_id_list

    @email_id_list.setter
    def email_id_list(self, email_id_list):
        """
        Sets the email_id_list of this CreateOperatorControlDetails.
        List of emailId.


        :param email_id_list: The email_id_list of this CreateOperatorControlDetails.
        :type: list[str]
        """
        self._email_id_list = email_id_list

    @property
    def system_message(self):
        """
        Gets the system_message of this CreateOperatorControlDetails.
        This is the message that will be displayed to the operator users while accessing the system.


        :return: The system_message of this CreateOperatorControlDetails.
        :rtype: str
        """
        return self._system_message

    @system_message.setter
    def system_message(self, system_message):
        """
        Sets the system_message of this CreateOperatorControlDetails.
        This is the message that will be displayed to the operator users while accessing the system.


        :param system_message: The system_message of this CreateOperatorControlDetails.
        :type: str
        """
        self._system_message = system_message

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOperatorControlDetails.
        The OCID of the compartment that contains this operator control.


        :return: The compartment_id of this CreateOperatorControlDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOperatorControlDetails.
        The OCID of the compartment that contains this operator control.


        :param compartment_id: The compartment_id of this CreateOperatorControlDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOperatorControlDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :return: The freeform_tags of this CreateOperatorControlDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOperatorControlDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :param freeform_tags: The freeform_tags of this CreateOperatorControlDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOperatorControlDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :return: The defined_tags of this CreateOperatorControlDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOperatorControlDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :param defined_tags: The defined_tags of this CreateOperatorControlDetails.
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
