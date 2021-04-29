# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperatorControlAssignment(object):
    """
    An Operator Control Assignment identifies the target resource that is placed under the governance of an Operator Control. Creating an Operator Control Assignment Assignment with a time duration ensures that
    human accesses to the target resource will be governed by Operator Control for the duration specified.
    """

    #: A constant which can be used with the resource_type property of a OperatorControlAssignment.
    #: This constant has a value of "EXACC"
    RESOURCE_TYPE_EXACC = "EXACC"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlAssignment.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlAssignment.
    #: This constant has a value of "APPLIED"
    LIFECYCLE_STATE_APPLIED = "APPLIED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlAssignment.
    #: This constant has a value of "APPLYFAILED"
    LIFECYCLE_STATE_APPLYFAILED = "APPLYFAILED"

    #: A constant which can be used with the lifecycle_state property of a OperatorControlAssignment.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new OperatorControlAssignment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OperatorControlAssignment.
        :type id: str

        :param operator_control_id:
            The value to assign to the operator_control_id property of this OperatorControlAssignment.
        :type operator_control_id: str

        :param resource_id:
            The value to assign to the resource_id property of this OperatorControlAssignment.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this OperatorControlAssignment.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this OperatorControlAssignment.
            Allowed values for this property are: "EXACC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_type: str

        :param resource_compartment_id:
            The value to assign to the resource_compartment_id property of this OperatorControlAssignment.
        :type resource_compartment_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OperatorControlAssignment.
        :type compartment_id: str

        :param time_assignment_from:
            The value to assign to the time_assignment_from property of this OperatorControlAssignment.
        :type time_assignment_from: datetime

        :param time_assignment_to:
            The value to assign to the time_assignment_to property of this OperatorControlAssignment.
        :type time_assignment_to: datetime

        :param is_enforced_always:
            The value to assign to the is_enforced_always property of this OperatorControlAssignment.
        :type is_enforced_always: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OperatorControlAssignment.
            Allowed values for this property are: "CREATED", "APPLIED", "APPLYFAILED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param assigner_id:
            The value to assign to the assigner_id property of this OperatorControlAssignment.
        :type assigner_id: str

        :param time_of_assignment:
            The value to assign to the time_of_assignment property of this OperatorControlAssignment.
        :type time_of_assignment: datetime

        :param comment:
            The value to assign to the comment property of this OperatorControlAssignment.
        :type comment: str

        :param unassigner_id:
            The value to assign to the unassigner_id property of this OperatorControlAssignment.
        :type unassigner_id: str

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this OperatorControlAssignment.
        :type time_of_deletion: datetime

        :param detachment_description:
            The value to assign to the detachment_description property of this OperatorControlAssignment.
        :type detachment_description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OperatorControlAssignment.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OperatorControlAssignment.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'operator_control_id': 'str',
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'resource_compartment_id': 'str',
            'compartment_id': 'str',
            'time_assignment_from': 'datetime',
            'time_assignment_to': 'datetime',
            'is_enforced_always': 'bool',
            'lifecycle_state': 'str',
            'assigner_id': 'str',
            'time_of_assignment': 'datetime',
            'comment': 'str',
            'unassigner_id': 'str',
            'time_of_deletion': 'datetime',
            'detachment_description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'operator_control_id': 'operatorControlId',
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'resource_compartment_id': 'resourceCompartmentId',
            'compartment_id': 'compartmentId',
            'time_assignment_from': 'timeAssignmentFrom',
            'time_assignment_to': 'timeAssignmentTo',
            'is_enforced_always': 'isEnforcedAlways',
            'lifecycle_state': 'lifecycleState',
            'assigner_id': 'assignerId',
            'time_of_assignment': 'timeOfAssignment',
            'comment': 'comment',
            'unassigner_id': 'unassignerId',
            'time_of_deletion': 'timeOfDeletion',
            'detachment_description': 'detachmentDescription',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._operator_control_id = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._resource_compartment_id = None
        self._compartment_id = None
        self._time_assignment_from = None
        self._time_assignment_to = None
        self._is_enforced_always = None
        self._lifecycle_state = None
        self._assigner_id = None
        self._time_of_assignment = None
        self._comment = None
        self._unassigner_id = None
        self._time_of_deletion = None
        self._detachment_description = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OperatorControlAssignment.
        The OCID of the operator control assignment.


        :return: The id of this OperatorControlAssignment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OperatorControlAssignment.
        The OCID of the operator control assignment.


        :param id: The id of this OperatorControlAssignment.
        :type: str
        """
        self._id = id

    @property
    def operator_control_id(self):
        """
        **[Required]** Gets the operator_control_id of this OperatorControlAssignment.
        The OCID of the operator control.


        :return: The operator_control_id of this OperatorControlAssignment.
        :rtype: str
        """
        return self._operator_control_id

    @operator_control_id.setter
    def operator_control_id(self, operator_control_id):
        """
        Sets the operator_control_id of this OperatorControlAssignment.
        The OCID of the operator control.


        :param operator_control_id: The operator_control_id of this OperatorControlAssignment.
        :type: str
        """
        self._operator_control_id = operator_control_id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this OperatorControlAssignment.
        The OCID of the target resource.


        :return: The resource_id of this OperatorControlAssignment.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this OperatorControlAssignment.
        The OCID of the target resource.


        :param resource_id: The resource_id of this OperatorControlAssignment.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this OperatorControlAssignment.
        Name of the target resource.


        :return: The resource_name of this OperatorControlAssignment.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this OperatorControlAssignment.
        Name of the target resource.


        :param resource_name: The resource_name of this OperatorControlAssignment.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this OperatorControlAssignment.
        Type of the target resource.

        Allowed values for this property are: "EXACC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_type of this OperatorControlAssignment.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this OperatorControlAssignment.
        Type of the target resource.


        :param resource_type: The resource_type of this OperatorControlAssignment.
        :type: str
        """
        allowed_values = ["EXACC"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            resource_type = 'UNKNOWN_ENUM_VALUE'
        self._resource_type = resource_type

    @property
    def resource_compartment_id(self):
        """
        Gets the resource_compartment_id of this OperatorControlAssignment.
        The OCID of the compartment that contains the target resource.


        :return: The resource_compartment_id of this OperatorControlAssignment.
        :rtype: str
        """
        return self._resource_compartment_id

    @resource_compartment_id.setter
    def resource_compartment_id(self, resource_compartment_id):
        """
        Sets the resource_compartment_id of this OperatorControlAssignment.
        The OCID of the compartment that contains the target resource.


        :param resource_compartment_id: The resource_compartment_id of this OperatorControlAssignment.
        :type: str
        """
        self._resource_compartment_id = resource_compartment_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this OperatorControlAssignment.
        The OCID of the comparment that contains the operator control assignment.


        :return: The compartment_id of this OperatorControlAssignment.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OperatorControlAssignment.
        The OCID of the comparment that contains the operator control assignment.


        :param compartment_id: The compartment_id of this OperatorControlAssignment.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_assignment_from(self):
        """
        Gets the time_assignment_from of this OperatorControlAssignment.
        The time at which the target resource will be brought under the governance of the operator control expressed in `RFC 3339`__ timestamp format.
        Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_assignment_from of this OperatorControlAssignment.
        :rtype: datetime
        """
        return self._time_assignment_from

    @time_assignment_from.setter
    def time_assignment_from(self, time_assignment_from):
        """
        Sets the time_assignment_from of this OperatorControlAssignment.
        The time at which the target resource will be brought under the governance of the operator control expressed in `RFC 3339`__ timestamp format.
        Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_assignment_from: The time_assignment_from of this OperatorControlAssignment.
        :type: datetime
        """
        self._time_assignment_from = time_assignment_from

    @property
    def time_assignment_to(self):
        """
        Gets the time_assignment_to of this OperatorControlAssignment.
        The time at which the target resource will leave the governance of the operator control expressed in `RFC 3339`__ timestamp format.
        Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_assignment_to of this OperatorControlAssignment.
        :rtype: datetime
        """
        return self._time_assignment_to

    @time_assignment_to.setter
    def time_assignment_to(self, time_assignment_to):
        """
        Sets the time_assignment_to of this OperatorControlAssignment.
        The time at which the target resource will leave the governance of the operator control expressed in `RFC 3339`__ timestamp format.
        Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_assignment_to: The time_assignment_to of this OperatorControlAssignment.
        :type: datetime
        """
        self._time_assignment_to = time_assignment_to

    @property
    def is_enforced_always(self):
        """
        Gets the is_enforced_always of this OperatorControlAssignment.
        If set, then the target resource is always governed by the operator control.


        :return: The is_enforced_always of this OperatorControlAssignment.
        :rtype: bool
        """
        return self._is_enforced_always

    @is_enforced_always.setter
    def is_enforced_always(self, is_enforced_always):
        """
        Sets the is_enforced_always of this OperatorControlAssignment.
        If set, then the target resource is always governed by the operator control.


        :param is_enforced_always: The is_enforced_always of this OperatorControlAssignment.
        :type: bool
        """
        self._is_enforced_always = is_enforced_always

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this OperatorControlAssignment.
        The current lifcycle state of the OperatorControl.

        Allowed values for this property are: "CREATED", "APPLIED", "APPLYFAILED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OperatorControlAssignment.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OperatorControlAssignment.
        The current lifcycle state of the OperatorControl.


        :param lifecycle_state: The lifecycle_state of this OperatorControlAssignment.
        :type: str
        """
        allowed_values = ["CREATED", "APPLIED", "APPLYFAILED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def assigner_id(self):
        """
        Gets the assigner_id of this OperatorControlAssignment.
        The OCID of the user who created this operator control assignment.


        :return: The assigner_id of this OperatorControlAssignment.
        :rtype: str
        """
        return self._assigner_id

    @assigner_id.setter
    def assigner_id(self, assigner_id):
        """
        Sets the assigner_id of this OperatorControlAssignment.
        The OCID of the user who created this operator control assignment.


        :param assigner_id: The assigner_id of this OperatorControlAssignment.
        :type: str
        """
        self._assigner_id = assigner_id

    @property
    def time_of_assignment(self):
        """
        Gets the time_of_assignment of this OperatorControlAssignment.
        Time when the operator control assignment is created in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_assignment of this OperatorControlAssignment.
        :rtype: datetime
        """
        return self._time_of_assignment

    @time_of_assignment.setter
    def time_of_assignment(self, time_of_assignment):
        """
        Sets the time_of_assignment of this OperatorControlAssignment.
        Time when the operator control assignment is created in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_assignment: The time_of_assignment of this OperatorControlAssignment.
        :type: datetime
        """
        self._time_of_assignment = time_of_assignment

    @property
    def comment(self):
        """
        Gets the comment of this OperatorControlAssignment.
        Comment about the assignment of the operator control to this target resource.


        :return: The comment of this OperatorControlAssignment.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this OperatorControlAssignment.
        Comment about the assignment of the operator control to this target resource.


        :param comment: The comment of this OperatorControlAssignment.
        :type: str
        """
        self._comment = comment

    @property
    def unassigner_id(self):
        """
        Gets the unassigner_id of this OperatorControlAssignment.
        User id who released the operatorControl.


        :return: The unassigner_id of this OperatorControlAssignment.
        :rtype: str
        """
        return self._unassigner_id

    @unassigner_id.setter
    def unassigner_id(self, unassigner_id):
        """
        Sets the unassigner_id of this OperatorControlAssignment.
        User id who released the operatorControl.


        :param unassigner_id: The unassigner_id of this OperatorControlAssignment.
        :type: str
        """
        self._unassigner_id = unassigner_id

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this OperatorControlAssignment.
        Time on which the operator control assignment was deleted in `RFC 3339`__timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this OperatorControlAssignment.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this OperatorControlAssignment.
        Time on which the operator control assignment was deleted in `RFC 3339`__timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this OperatorControlAssignment.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    @property
    def detachment_description(self):
        """
        Gets the detachment_description of this OperatorControlAssignment.
        description containing reason for releasing of OperatorControl.


        :return: The detachment_description of this OperatorControlAssignment.
        :rtype: str
        """
        return self._detachment_description

    @detachment_description.setter
    def detachment_description(self, detachment_description):
        """
        Sets the detachment_description of this OperatorControlAssignment.
        description containing reason for releasing of OperatorControl.


        :param detachment_description: The detachment_description of this OperatorControlAssignment.
        :type: str
        """
        self._detachment_description = detachment_description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OperatorControlAssignment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :return: The freeform_tags of this OperatorControlAssignment.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OperatorControlAssignment.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :param freeform_tags: The freeform_tags of this OperatorControlAssignment.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OperatorControlAssignment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :return: The defined_tags of this OperatorControlAssignment.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OperatorControlAssignment.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :param defined_tags: The defined_tags of this OperatorControlAssignment.
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
