# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrPlanGroupDetails(object):
    """
    The details for updating a DR Plan group.
    """

    #: A constant which can be used with the type property of a UpdateDrPlanGroupDetails.
    #: This constant has a value of "USER_DEFINED"
    TYPE_USER_DEFINED = "USER_DEFINED"

    #: A constant which can be used with the type property of a UpdateDrPlanGroupDetails.
    #: This constant has a value of "BUILT_IN"
    TYPE_BUILT_IN = "BUILT_IN"

    #: A constant which can be used with the type property of a UpdateDrPlanGroupDetails.
    #: This constant has a value of "BUILT_IN_PRECHECK"
    TYPE_BUILT_IN_PRECHECK = "BUILT_IN_PRECHECK"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrPlanGroupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this UpdateDrPlanGroupDetails.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this UpdateDrPlanGroupDetails.
        :type display_name: str

        :param type:
            The value to assign to the type property of this UpdateDrPlanGroupDetails.
            Allowed values for this property are: "USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK"
        :type type: str

        :param steps:
            The value to assign to the steps property of this UpdateDrPlanGroupDetails.
        :type steps: list[oci.disaster_recovery.models.UpdateDrPlanStepDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'type': 'str',
            'steps': 'list[UpdateDrPlanStepDetails]'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'type': 'type',
            'steps': 'steps'
        }

        self._id = None
        self._display_name = None
        self._type = None
        self._steps = None

    @property
    def id(self):
        """
        Gets the id of this UpdateDrPlanGroupDetails.
        The unique id of this group. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :return: The id of this UpdateDrPlanGroupDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateDrPlanGroupDetails.
        The unique id of this group. Must not be modified by user.

        Example: `sgid1.group..examplegroupsgid`


        :param id: The id of this UpdateDrPlanGroupDetails.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateDrPlanGroupDetails.
        The display name of this group.

        Example: `My_GROUP_3 - EBS Start`


        :return: The display_name of this UpdateDrPlanGroupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateDrPlanGroupDetails.
        The display name of this group.

        Example: `My_GROUP_3 - EBS Start`


        :param display_name: The display_name of this UpdateDrPlanGroupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        Gets the type of this UpdateDrPlanGroupDetails.
        The group type.

        Allowed values for this property are: "USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK"


        :return: The type of this UpdateDrPlanGroupDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateDrPlanGroupDetails.
        The group type.


        :param type: The type of this UpdateDrPlanGroupDetails.
        :type: str
        """
        allowed_values = ["USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                "Invalid value for `type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._type = type

    @property
    def steps(self):
        """
        Gets the steps of this UpdateDrPlanGroupDetails.
        The list of steps in this group.


        :return: The steps of this UpdateDrPlanGroupDetails.
        :rtype: list[oci.disaster_recovery.models.UpdateDrPlanStepDetails]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps of this UpdateDrPlanGroupDetails.
        The list of steps in this group.


        :param steps: The steps of this UpdateDrPlanGroupDetails.
        :type: list[oci.disaster_recovery.models.UpdateDrPlanStepDetails]
        """
        self._steps = steps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
