# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .item import Item
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActivityItem(Item):
    """
    Details about the ActivityItem object.
    """

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "NOTES"
    ACTIVITY_TYPE_NOTES = "NOTES"

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "PROBLEM_DESCRIPTION"
    ACTIVITY_TYPE_PROBLEM_DESCRIPTION = "PROBLEM_DESCRIPTION"

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "UPDATE"
    ACTIVITY_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "CLOSE"
    ACTIVITY_TYPE_CLOSE = "CLOSE"

    #: A constant which can be used with the activity_author property of a ActivityItem.
    #: This constant has a value of "CUSTOMER"
    ACTIVITY_AUTHOR_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the activity_author property of a ActivityItem.
    #: This constant has a value of "ORACLE"
    ACTIVITY_AUTHOR_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new ActivityItem object with values from keyword arguments. The default value of the :py:attr:`~oci.cims.models.ActivityItem.type` attribute
        of this class is ``activity`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param item_key:
            The value to assign to the item_key property of this ActivityItem.
        :type item_key: str

        :param name:
            The value to assign to the name property of this ActivityItem.
        :type name: str

        :param type:
            The value to assign to the type property of this ActivityItem.
        :type type: str

        :param category:
            The value to assign to the category property of this ActivityItem.
        :type category: Category

        :param sub_category:
            The value to assign to the sub_category property of this ActivityItem.
        :type sub_category: SubCategory

        :param issue_type:
            The value to assign to the issue_type property of this ActivityItem.
        :type issue_type: IssueType

        :param comments:
            The value to assign to the comments property of this ActivityItem.
        :type comments: str

        :param time_created:
            The value to assign to the time_created property of this ActivityItem.
        :type time_created: int

        :param time_updated:
            The value to assign to the time_updated property of this ActivityItem.
        :type time_updated: int

        :param activity_type:
            The value to assign to the activity_type property of this ActivityItem.
            Allowed values for this property are: "NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type activity_type: str

        :param activity_author:
            The value to assign to the activity_author property of this ActivityItem.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type activity_author: str

        """
        self.swagger_types = {
            'item_key': 'str',
            'name': 'str',
            'type': 'str',
            'category': 'Category',
            'sub_category': 'SubCategory',
            'issue_type': 'IssueType',
            'comments': 'str',
            'time_created': 'int',
            'time_updated': 'int',
            'activity_type': 'str',
            'activity_author': 'str'
        }

        self.attribute_map = {
            'item_key': 'itemKey',
            'name': 'name',
            'type': 'type',
            'category': 'category',
            'sub_category': 'subCategory',
            'issue_type': 'issueType',
            'comments': 'comments',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'activity_type': 'activityType',
            'activity_author': 'activityAuthor'
        }

        self._item_key = None
        self._name = None
        self._type = None
        self._category = None
        self._sub_category = None
        self._issue_type = None
        self._comments = None
        self._time_created = None
        self._time_updated = None
        self._activity_type = None
        self._activity_author = None
        self._type = 'activity'

    @property
    def comments(self):
        """
        Gets the comments of this ActivityItem.
        Comments added with the activity on the support ticket.


        :return: The comments of this ActivityItem.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this ActivityItem.
        Comments added with the activity on the support ticket.


        :param comments: The comments of this ActivityItem.
        :type: str
        """
        self._comments = comments

    @property
    def time_created(self):
        """
        Gets the time_created of this ActivityItem.
        The time when the activity was created, in milliseconds since epoch time.


        :return: The time_created of this ActivityItem.
        :rtype: int
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ActivityItem.
        The time when the activity was created, in milliseconds since epoch time.


        :param time_created: The time_created of this ActivityItem.
        :type: int
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ActivityItem.
        The time when the activity was updated, in milliseconds since epoch time.


        :return: The time_updated of this ActivityItem.
        :rtype: int
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ActivityItem.
        The time when the activity was updated, in milliseconds since epoch time.


        :param time_updated: The time_updated of this ActivityItem.
        :type: int
        """
        self._time_updated = time_updated

    @property
    def activity_type(self):
        """
        Gets the activity_type of this ActivityItem.
        The type of activity occuring on the support ticket.

        Allowed values for this property are: "NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The activity_type of this ActivityItem.
        :rtype: str
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """
        Sets the activity_type of this ActivityItem.
        The type of activity occuring on the support ticket.


        :param activity_type: The activity_type of this ActivityItem.
        :type: str
        """
        allowed_values = ["NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE"]
        if not value_allowed_none_or_none_sentinel(activity_type, allowed_values):
            activity_type = 'UNKNOWN_ENUM_VALUE'
        self._activity_type = activity_type

    @property
    def activity_author(self):
        """
        Gets the activity_author of this ActivityItem.
        The person who updates the activity on the support ticket.

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The activity_author of this ActivityItem.
        :rtype: str
        """
        return self._activity_author

    @activity_author.setter
    def activity_author(self, activity_author):
        """
        Sets the activity_author of this ActivityItem.
        The person who updates the activity on the support ticket.


        :param activity_author: The activity_author of this ActivityItem.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(activity_author, allowed_values):
            activity_author = 'UNKNOWN_ENUM_VALUE'
        self._activity_author = activity_author

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
