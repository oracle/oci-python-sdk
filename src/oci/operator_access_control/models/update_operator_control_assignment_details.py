# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOperatorControlAssignmentDetails(object):
    """
    Details for modifying the Operator Control assignment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOperatorControlAssignmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_assignment_from:
            The value to assign to the time_assignment_from property of this UpdateOperatorControlAssignmentDetails.
        :type time_assignment_from: datetime

        :param time_assignment_to:
            The value to assign to the time_assignment_to property of this UpdateOperatorControlAssignmentDetails.
        :type time_assignment_to: datetime

        :param is_enforced_always:
            The value to assign to the is_enforced_always property of this UpdateOperatorControlAssignmentDetails.
        :type is_enforced_always: bool

        :param comment:
            The value to assign to the comment property of this UpdateOperatorControlAssignmentDetails.
        :type comment: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOperatorControlAssignmentDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOperatorControlAssignmentDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'time_assignment_from': 'datetime',
            'time_assignment_to': 'datetime',
            'is_enforced_always': 'bool',
            'comment': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'time_assignment_from': 'timeAssignmentFrom',
            'time_assignment_to': 'timeAssignmentTo',
            'is_enforced_always': 'isEnforcedAlways',
            'comment': 'comment',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._time_assignment_from = None
        self._time_assignment_to = None
        self._is_enforced_always = None
        self._comment = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def time_assignment_from(self):
        """
        Gets the time_assignment_from of this UpdateOperatorControlAssignmentDetails.
        The time at which the target resource will be brought under the governance of the operator control in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_assignment_from of this UpdateOperatorControlAssignmentDetails.
        :rtype: datetime
        """
        return self._time_assignment_from

    @time_assignment_from.setter
    def time_assignment_from(self, time_assignment_from):
        """
        Sets the time_assignment_from of this UpdateOperatorControlAssignmentDetails.
        The time at which the target resource will be brought under the governance of the operator control in `RFC 3339`__ timestamp format. Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_assignment_from: The time_assignment_from of this UpdateOperatorControlAssignmentDetails.
        :type: datetime
        """
        self._time_assignment_from = time_assignment_from

    @property
    def time_assignment_to(self):
        """
        Gets the time_assignment_to of this UpdateOperatorControlAssignmentDetails.
        The time at which the target resource will leave the governance of the operator control in `RFC 3339`__timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_assignment_to of this UpdateOperatorControlAssignmentDetails.
        :rtype: datetime
        """
        return self._time_assignment_to

    @time_assignment_to.setter
    def time_assignment_to(self, time_assignment_to):
        """
        Sets the time_assignment_to of this UpdateOperatorControlAssignmentDetails.
        The time at which the target resource will leave the governance of the operator control in `RFC 3339`__timestamp format.Example: '2020-05-22T21:10:29.600Z'

        __ https://tools.ietf.org/html/rfc3339


        :param time_assignment_to: The time_assignment_to of this UpdateOperatorControlAssignmentDetails.
        :type: datetime
        """
        self._time_assignment_to = time_assignment_to

    @property
    def is_enforced_always(self):
        """
        Gets the is_enforced_always of this UpdateOperatorControlAssignmentDetails.
        If true, then the target resource is always governed by the operator control. Otherwise governance is time-based as specified by timeAssignmentTo and timeAssignmentFrom.


        :return: The is_enforced_always of this UpdateOperatorControlAssignmentDetails.
        :rtype: bool
        """
        return self._is_enforced_always

    @is_enforced_always.setter
    def is_enforced_always(self, is_enforced_always):
        """
        Sets the is_enforced_always of this UpdateOperatorControlAssignmentDetails.
        If true, then the target resource is always governed by the operator control. Otherwise governance is time-based as specified by timeAssignmentTo and timeAssignmentFrom.


        :param is_enforced_always: The is_enforced_always of this UpdateOperatorControlAssignmentDetails.
        :type: bool
        """
        self._is_enforced_always = is_enforced_always

    @property
    def comment(self):
        """
        Gets the comment of this UpdateOperatorControlAssignmentDetails.
        Comment about the modification of the operator control assignment.


        :return: The comment of this UpdateOperatorControlAssignmentDetails.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this UpdateOperatorControlAssignmentDetails.
        Comment about the modification of the operator control assignment.


        :param comment: The comment of this UpdateOperatorControlAssignmentDetails.
        :type: str
        """
        self._comment = comment

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOperatorControlAssignmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :return: The freeform_tags of this UpdateOperatorControlAssignmentDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOperatorControlAssignmentDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.


        :param freeform_tags: The freeform_tags of this UpdateOperatorControlAssignmentDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOperatorControlAssignmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :return: The defined_tags of this UpdateOperatorControlAssignmentDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOperatorControlAssignmentDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.


        :param defined_tags: The defined_tags of this UpdateOperatorControlAssignmentDetails.
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
