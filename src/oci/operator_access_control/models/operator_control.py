# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperatorControl(object):
    """
    Operator Access Control enables you to grant, audit, or revoke the access Oracle has to your Exadata Cloud@Customer infrastructure, and obtain audit reports of all actions taken by a human operator, in a near real-time manner.
    """

    #: A constant which can be used with the lifecycle_state property of a OperatorControl.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControl.
    #: This constant has a value of "ASSIGNED"
    LIFECYCLE_STATE_ASSIGNED = "ASSIGNED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControl.
    #: This constant has a value of "UNASSIGNED"
    LIFECYCLE_STATE_UNASSIGNED = "UNASSIGNED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControl.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new OperatorControl object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OperatorControl.
        :type id: str

        :param operator_control_name:
            The value to assign to the operator_control_name property of this OperatorControl.
        :type operator_control_name: str

        :param description:
            The value to assign to the description property of this OperatorControl.
        :type description: str

        :param approvers_list:
            The value to assign to the approvers_list property of this OperatorControl.
        :type approvers_list: list[str]

        :param approver_groups_list:
            The value to assign to the approver_groups_list property of this OperatorControl.
        :type approver_groups_list: list[str]

        :param pre_approved_op_action_list:
            The value to assign to the pre_approved_op_action_list property of this OperatorControl.
        :type pre_approved_op_action_list: list[str]

        :param approval_required_op_action_list:
            The value to assign to the approval_required_op_action_list property of this OperatorControl.
        :type approval_required_op_action_list: list[str]

        :param is_fully_pre_approved:
            The value to assign to the is_fully_pre_approved property of this OperatorControl.
        :type is_fully_pre_approved: bool

        :param system_message:
            The value to assign to the system_message property of this OperatorControl.
        :type system_message: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OperatorControl.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OperatorControl.
            Allowed values for this property are: "CREATED", "ASSIGNED", "UNASSIGNED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_of_creation:
            The value to assign to the time_of_creation property of this OperatorControl.
        :type time_of_creation: datetime

        :param time_of_modification:
            The value to assign to the time_of_modification property of this OperatorControl.
        :type time_of_modification: datetime

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this OperatorControl.
        :type time_of_deletion: datetime

        :param last_modified_info:
            The value to assign to the last_modified_info property of this OperatorControl.
        :type last_modified_info: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OperatorControl.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OperatorControl.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'operator_control_name': 'str',
            'description': 'str',
            'approvers_list': 'list[str]',
            'approver_groups_list': 'list[str]',
            'pre_approved_op_action_list': 'list[str]',
            'approval_required_op_action_list': 'list[str]',
            'is_fully_pre_approved': 'bool',
            'system_message': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'time_of_creation': 'datetime',
            'time_of_modification': 'datetime',
            'time_of_deletion': 'datetime',
            'last_modified_info': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'operator_control_name': 'operatorControlName',
            'description': 'description',
            'approvers_list': 'approversList',
            'approver_groups_list': 'approverGroupsList',
            'pre_approved_op_action_list': 'preApprovedOpActionList',
            'approval_required_op_action_list': 'approvalRequiredOpActionList',
            'is_fully_pre_approved': 'isFullyPreApproved',
            'system_message': 'systemMessage',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'time_of_creation': 'timeOfCreation',
            'time_of_modification': 'timeOfModification',
            'time_of_deletion': 'timeOfDeletion',
            'last_modified_info': 'lastModifiedInfo',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._operator_control_name = None
        self._description = None
        self._approvers_list = None
        self._approver_groups_list = None
        self._pre_approved_op_action_list = None
        self._approval_required_op_action_list = None
        self._is_fully_pre_approved = None
        self._system_message = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._time_of_creation = None
        self._time_of_modification = None
        self._time_of_deletion = None
        self._last_modified_info = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OperatorControl.
        The OCID of the operator control.


        :return: The id of this OperatorControl.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OperatorControl.
        The OCID of the operator control.


        :param id: The id of this OperatorControl.
        :type: str
        """
        self._id = id

    @property
    def operator_control_name(self):
        """
        **[Required]** Gets the operator_control_name of this OperatorControl.
        Name of the operator control. The name must be unique.


        :return: The operator_control_name of this OperatorControl.
        :rtype: str
        """
        return self._operator_control_name

    @operator_control_name.setter
    def operator_control_name(self, operator_control_name):
        """
        Sets the operator_control_name of this OperatorControl.
        Name of the operator control. The name must be unique.


        :param operator_control_name: The operator_control_name of this OperatorControl.
        :type: str
        """
        self._operator_control_name = operator_control_name

    @property
    def description(self):
        """
        Gets the description of this OperatorControl.
        Description of operator control.


        :return: The description of this OperatorControl.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this OperatorControl.
        Description of operator control.


        :param description: The description of this OperatorControl.
        :type: str
        """
        self._description = description

    @property
    def approvers_list(self):
        """
        Gets the approvers_list of this OperatorControl.
        List of users who can approve an access request associated with a target resource under the governance of this operator control.


        :return: The approvers_list of this OperatorControl.
        :rtype: list[str]
        """
        return self._approvers_list

    @approvers_list.setter
    def approvers_list(self, approvers_list):
        """
        Sets the approvers_list of this OperatorControl.
        List of users who can approve an access request associated with a target resource under the governance of this operator control.


        :param approvers_list: The approvers_list of this OperatorControl.
        :type: list[str]
        """
        self._approvers_list = approvers_list

    @property
    def approver_groups_list(self):
        """
        Gets the approver_groups_list of this OperatorControl.
        List of user groups who can approve an access request associated with a target resource under the governance of this operator control.


        :return: The approver_groups_list of this OperatorControl.
        :rtype: list[str]
        """
        return self._approver_groups_list

    @approver_groups_list.setter
    def approver_groups_list(self, approver_groups_list):
        """
        Sets the approver_groups_list of this OperatorControl.
        List of user groups who can approve an access request associated with a target resource under the governance of this operator control.


        :param approver_groups_list: The approver_groups_list of this OperatorControl.
        :type: list[str]
        """
        self._approver_groups_list = approver_groups_list

    @property
    def pre_approved_op_action_list(self):
        """
        Gets the pre_approved_op_action_list of this OperatorControl.
        List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be
        automatically approved if the access request only contain operator actions in the pre-approved list.


        :return: The pre_approved_op_action_list of this OperatorControl.
        :rtype: list[str]
        """
        return self._pre_approved_op_action_list

    @pre_approved_op_action_list.setter
    def pre_approved_op_action_list(self, pre_approved_op_action_list):
        """
        Sets the pre_approved_op_action_list of this OperatorControl.
        List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be
        automatically approved if the access request only contain operator actions in the pre-approved list.


        :param pre_approved_op_action_list: The pre_approved_op_action_list of this OperatorControl.
        :type: list[str]
        """
        self._pre_approved_op_action_list = pre_approved_op_action_list

    @property
    def approval_required_op_action_list(self):
        """
        Gets the approval_required_op_action_list of this OperatorControl.
        List of operator actions that need explicit approval. Any operator action not in the pre-approved list will require explicit
        approval. Access requests associated with a resource governed by this operator control will be
        require explicit approval if the access request contains any operator action in this list.


        :return: The approval_required_op_action_list of this OperatorControl.
        :rtype: list[str]
        """
        return self._approval_required_op_action_list

    @approval_required_op_action_list.setter
    def approval_required_op_action_list(self, approval_required_op_action_list):
        """
        Sets the approval_required_op_action_list of this OperatorControl.
        List of operator actions that need explicit approval. Any operator action not in the pre-approved list will require explicit
        approval. Access requests associated with a resource governed by this operator control will be
        require explicit approval if the access request contains any operator action in this list.


        :param approval_required_op_action_list: The approval_required_op_action_list of this OperatorControl.
        :type: list[str]
        """
        self._approval_required_op_action_list = approval_required_op_action_list

    @property
    def is_fully_pre_approved(self):
        """
        Gets the is_fully_pre_approved of this OperatorControl.
        Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator control
        will be auto-approved.


        :return: The is_fully_pre_approved of this OperatorControl.
        :rtype: bool
        """
        return self._is_fully_pre_approved

    @is_fully_pre_approved.setter
    def is_fully_pre_approved(self, is_fully_pre_approved):
        """
        Sets the is_fully_pre_approved of this OperatorControl.
        Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator control
        will be auto-approved.


        :param is_fully_pre_approved: The is_fully_pre_approved of this OperatorControl.
        :type: bool
        """
        self._is_fully_pre_approved = is_fully_pre_approved

    @property
    def system_message(self):
        """
        Gets the system_message of this OperatorControl.
        System message that would be displayed to the operator users on accessing the target resource under the governance of this operator control.


        :return: The system_message of this OperatorControl.
        :rtype: str
        """
        return self._system_message

    @system_message.setter
    def system_message(self, system_message):
        """
        Sets the system_message of this OperatorControl.
        System message that would be displayed to the operator users on accessing the target resource under the governance of this operator control.


        :param system_message: The system_message of this OperatorControl.
        :type: str
        """
        self._system_message = system_message

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OperatorControl.
        The OCID of the compartment that contains the operator control.


        :return: The compartment_id of this OperatorControl.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OperatorControl.
        The OCID of the compartment that contains the operator control.


        :param compartment_id: The compartment_id of this OperatorControl.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OperatorControl.
        The current lifecycle state of the operator control.

        Allowed values for this property are: "CREATED", "ASSIGNED", "UNASSIGNED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OperatorControl.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OperatorControl.
        The current lifecycle state of the operator control.


        :param lifecycle_state: The lifecycle_state of this OperatorControl.
        :type: str
        """
        allowed_values = ["CREATED", "ASSIGNED", "UNASSIGNED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_of_creation(self):
        """
        Gets the time_of_creation of this OperatorControl.
        Time when the operator control was created expressed in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_creation of this OperatorControl.
        :rtype: datetime
        """
        return self._time_of_creation

    @time_of_creation.setter
    def time_of_creation(self, time_of_creation):
        """
        Sets the time_of_creation of this OperatorControl.
        Time when the operator control was created expressed in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_creation: The time_of_creation of this OperatorControl.
        :type: datetime
        """
        self._time_of_creation = time_of_creation

    @property
    def time_of_modification(self):
        """
        Gets the time_of_modification of this OperatorControl.
        Time when the operator control was last modified expressed in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_modification of this OperatorControl.
        :rtype: datetime
        """
        return self._time_of_modification

    @time_of_modification.setter
    def time_of_modification(self, time_of_modification):
        """
        Sets the time_of_modification of this OperatorControl.
        Time when the operator control was last modified expressed in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_modification: The time_of_modification of this OperatorControl.
        :type: datetime
        """
        self._time_of_modification = time_of_modification

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this OperatorControl.
        Time when deleted expressed in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'.
        Note a deleted operator control still stays in the system, so that you can still audit operator actions associated with access requests
        raised on target resources governed by the deleted operator control.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this OperatorControl.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this OperatorControl.
        Time when deleted expressed in `RFC 3339`__timestamp format. Example: '2020-05-22T21:10:29.600Z'.
        Note a deleted operator control still stays in the system, so that you can still audit operator actions associated with access requests
        raised on target resources governed by the deleted operator control.

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this OperatorControl.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def last_modified_info(self):
        """
        Gets the last_modified_info of this OperatorControl.
        Description associated with the latest modification of the operator control.


        :return: The last_modified_info of this OperatorControl.
        :rtype: str
        """
        return self._last_modified_info

    @last_modified_info.setter
    def last_modified_info(self, last_modified_info):
        """
        Sets the last_modified_info of this OperatorControl.
        Description associated with the latest modification of the operator control.


        :param last_modified_info: The last_modified_info of this OperatorControl.
        :type: str
        """
        self._last_modified_info = last_modified_info

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OperatorControl.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :return: The freeform_tags of this OperatorControl.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OperatorControl.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :param freeform_tags: The freeform_tags of this OperatorControl.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OperatorControl.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :return: The defined_tags of this OperatorControl.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OperatorControl.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :param defined_tags: The defined_tags of this OperatorControl.
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
