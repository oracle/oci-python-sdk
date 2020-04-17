# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_item_details import UpdateItemDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateActivityItemDetails(UpdateItemDetails):
    """
    Details of Activity Item
    """

    #: A constant which can be used with the activity_type property of a UpdateActivityItemDetails.
    #: This constant has a value of "NOTES"
    ACTIVITY_TYPE_NOTES = "NOTES"

    #: A constant which can be used with the activity_type property of a UpdateActivityItemDetails.
    #: This constant has a value of "PROBLEM_DESCRIPTION"
    ACTIVITY_TYPE_PROBLEM_DESCRIPTION = "PROBLEM_DESCRIPTION"

    #: A constant which can be used with the activity_type property of a UpdateActivityItemDetails.
    #: This constant has a value of "UPDATE"
    ACTIVITY_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the activity_type property of a UpdateActivityItemDetails.
    #: This constant has a value of "CLOSE"
    ACTIVITY_TYPE_CLOSE = "CLOSE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateActivityItemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cims.models.UpdateActivityItemDetails.type` attribute
        of this class is ``activity`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UpdateActivityItemDetails.
        :type type: str

        :param comments:
            The value to assign to the comments property of this UpdateActivityItemDetails.
        :type comments: str

        :param activity_type:
            The value to assign to the activity_type property of this UpdateActivityItemDetails.
            Allowed values for this property are: "NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE"
        :type activity_type: str

        """
        self.swagger_types = {
            'type': 'str',
            'comments': 'str',
            'activity_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'comments': 'comments',
            'activity_type': 'activityType'
        }

        self._type = None
        self._comments = None
        self._activity_type = None
        self._type = 'activity'

    @property
    def comments(self):
        """
        Gets the comments of this UpdateActivityItemDetails.
        Comments to update as part of Activity


        :return: The comments of this UpdateActivityItemDetails.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this UpdateActivityItemDetails.
        Comments to update as part of Activity


        :param comments: The comments of this UpdateActivityItemDetails.
        :type: str
        """
        self._comments = comments

    @property
    def activity_type(self):
        """
        Gets the activity_type of this UpdateActivityItemDetails.
        Type of activity. eg: NOTES, UPDATE

        Allowed values for this property are: "NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE"


        :return: The activity_type of this UpdateActivityItemDetails.
        :rtype: str
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """
        Sets the activity_type of this UpdateActivityItemDetails.
        Type of activity. eg: NOTES, UPDATE


        :param activity_type: The activity_type of this UpdateActivityItemDetails.
        :type: str
        """
        allowed_values = ["NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE"]
        if not value_allowed_none_or_none_sentinel(activity_type, allowed_values):
            raise ValueError(
                "Invalid value for `activity_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._activity_type = activity_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
