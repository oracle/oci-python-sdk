# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateOperatorControlAssignmentDetails(object):
    """
    Details of the Operator Control assignment. An Operator Control Assignment identifies the target resource that is placed under the governance of an Operator Control.
    Creating an Operator Control Assignment Assignment with a time duration ensures that human accesses to the target resource will be governed by Operator Control for the duration specified.
    """

    #: A constant which can be used with the resource_type property of a CreateOperatorControlAssignmentDetails.
    #: This constant has a value of "EXACC"
    RESOURCE_TYPE_EXACC = "EXACC"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateOperatorControlAssignmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operator_control_id:
            The value to assign to the operator_control_id property of this CreateOperatorControlAssignmentDetails.
        :type operator_control_id: str

        :param resource_id:
            The value to assign to the resource_id property of this CreateOperatorControlAssignmentDetails.
        :type resource_id: str

        :param resource_name:
            The value to assign to the resource_name property of this CreateOperatorControlAssignmentDetails.
        :type resource_name: str

        :param resource_type:
            The value to assign to the resource_type property of this CreateOperatorControlAssignmentDetails.
            Allowed values for this property are: "EXACC"
        :type resource_type: str

        :param resource_compartment_id:
            The value to assign to the resource_compartment_id property of this CreateOperatorControlAssignmentDetails.
        :type resource_compartment_id: str

        :param time_assignment_from:
            The value to assign to the time_assignment_from property of this CreateOperatorControlAssignmentDetails.
        :type time_assignment_from: datetime

        :param time_assignment_to:
            The value to assign to the time_assignment_to property of this CreateOperatorControlAssignmentDetails.
        :type time_assignment_to: datetime

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateOperatorControlAssignmentDetails.
        :type compartment_id: str

        :param is_enforced_always:
            The value to assign to the is_enforced_always property of this CreateOperatorControlAssignmentDetails.
        :type is_enforced_always: bool

        :param comment:
            The value to assign to the comment property of this CreateOperatorControlAssignmentDetails.
        :type comment: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateOperatorControlAssignmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateOperatorControlAssignmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'operator_control_id': 'str',
            'resource_id': 'str',
            'resource_name': 'str',
            'resource_type': 'str',
            'resource_compartment_id': 'str',
            'time_assignment_from': 'datetime',
            'time_assignment_to': 'datetime',
            'compartment_id': 'str',
            'is_enforced_always': 'bool',
            'comment': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'operator_control_id': 'operatorControlId',
            'resource_id': 'resourceId',
            'resource_name': 'resourceName',
            'resource_type': 'resourceType',
            'resource_compartment_id': 'resourceCompartmentId',
            'time_assignment_from': 'timeAssignmentFrom',
            'time_assignment_to': 'timeAssignmentTo',
            'compartment_id': 'compartmentId',
            'is_enforced_always': 'isEnforcedAlways',
            'comment': 'comment',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._operator_control_id = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._resource_compartment_id = None
        self._time_assignment_from = None
        self._time_assignment_to = None
        self._compartment_id = None
        self._is_enforced_always = None
        self._comment = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def operator_control_id(self):
        """
        **[Required]** Gets the operator_control_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the operator control that is being assigned to a target resource.


        :return: The operator_control_id of this CreateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._operator_control_id

    @operator_control_id.setter
    def operator_control_id(self, operator_control_id):
        """
        Sets the operator_control_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the operator control that is being assigned to a target resource.


        :param operator_control_id: The operator_control_id of this CreateOperatorControlAssignmentDetails.
        :type: str
        """
        self._operator_control_id = operator_control_id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the target resource being brought under the governance of the operator control.


        :return: The resource_id of this CreateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the target resource being brought under the governance of the operator control.


        :param resource_id: The resource_id of this CreateOperatorControlAssignmentDetails.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this CreateOperatorControlAssignmentDetails.
        Name of the target resource.


        :return: The resource_name of this CreateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this CreateOperatorControlAssignmentDetails.
        Name of the target resource.


        :param resource_name: The resource_name of this CreateOperatorControlAssignmentDetails.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """
        Gets the resource_type of this CreateOperatorControlAssignmentDetails.
        Type of the target resource.

        Allowed values for this property are: "EXACC"


        :return: The resource_type of this CreateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """
        Sets the resource_type of this CreateOperatorControlAssignmentDetails.
        Type of the target resource.


        :param resource_type: The resource_type of this CreateOperatorControlAssignmentDetails.
        :type: str
        """
        allowed_values = ["EXACC"]
        if not value_allowed_none_or_none_sentinel(resource_type, allowed_values):
            raise ValueError(
                "Invalid value for `resource_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._resource_type = resource_type

    @property
    def resource_compartment_id(self):
        """
        **[Required]** Gets the resource_compartment_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the compartment that contains the target resource.


        :return: The resource_compartment_id of this CreateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._resource_compartment_id

    @resource_compartment_id.setter
    def resource_compartment_id(self, resource_compartment_id):
        """
        Sets the resource_compartment_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the compartment that contains the target resource.


        :param resource_compartment_id: The resource_compartment_id of this CreateOperatorControlAssignmentDetails.
        :type: str
        """
        self._resource_compartment_id = resource_compartment_id

    @property
    def time_assignment_from(self):
        """
        Gets the time_assignment_from of this CreateOperatorControlAssignmentDetails.
        The time at which the target resource will be brought under the governance of the operator control in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_assignment_from of this CreateOperatorControlAssignmentDetails.
        :rtype: datetime
        """
        return self._time_assignment_from

    @time_assignment_from.setter
    def time_assignment_from(self, time_assignment_from):
        """
        Sets the time_assignment_from of this CreateOperatorControlAssignmentDetails.
        The time at which the target resource will be brought under the governance of the operator control in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_assignment_from: The time_assignment_from of this CreateOperatorControlAssignmentDetails.
        :type: datetime
        """
        self._time_assignment_from = time_assignment_from

    @property
    def time_assignment_to(self):
        """
        Gets the time_assignment_to of this CreateOperatorControlAssignmentDetails.
        The time at which the target resource will leave the governance of the operator control in `RFC 3339`__timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_assignment_to of this CreateOperatorControlAssignmentDetails.
        :rtype: datetime
        """
        return self._time_assignment_to

    @time_assignment_to.setter
    def time_assignment_to(self, time_assignment_to):
        """
        Sets the time_assignment_to of this CreateOperatorControlAssignmentDetails.
        The time at which the target resource will leave the governance of the operator control in `RFC 3339`__timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_assignment_to: The time_assignment_to of this CreateOperatorControlAssignmentDetails.
        :type: datetime
        """
        self._time_assignment_to = time_assignment_to

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the compartment that contains the operator control assignment.


        :return: The compartment_id of this CreateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateOperatorControlAssignmentDetails.
        The OCID of the compartment that contains the operator control assignment.


        :param compartment_id: The compartment_id of this CreateOperatorControlAssignmentDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_enforced_always(self):
        """
        Gets the is_enforced_always of this CreateOperatorControlAssignmentDetails.
        If set, then the target resource is always governed by the operator control.


        :return: The is_enforced_always of this CreateOperatorControlAssignmentDetails.
        :rtype: bool
        """
        return self._is_enforced_always

    @is_enforced_always.setter
    def is_enforced_always(self, is_enforced_always):
        """
        Sets the is_enforced_always of this CreateOperatorControlAssignmentDetails.
        If set, then the target resource is always governed by the operator control.


        :param is_enforced_always: The is_enforced_always of this CreateOperatorControlAssignmentDetails.
        :type: bool
        """
        self._is_enforced_always = is_enforced_always

    @property
    def comment(self):
        """
        Gets the comment of this CreateOperatorControlAssignmentDetails.
        Comment about the assignment of the operator control to this target resource.


        :return: The comment of this CreateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this CreateOperatorControlAssignmentDetails.
        Comment about the assignment of the operator control to this target resource.


        :param comment: The comment of this CreateOperatorControlAssignmentDetails.
        :type: str
        """
        self._comment = comment

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateOperatorControlAssignmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :return: The freeform_tags of this CreateOperatorControlAssignmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateOperatorControlAssignmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :param freeform_tags: The freeform_tags of this CreateOperatorControlAssignmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateOperatorControlAssignmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :return: The defined_tags of this CreateOperatorControlAssignmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateOperatorControlAssignmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :param defined_tags: The defined_tags of this CreateOperatorControlAssignmentDetails.
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
