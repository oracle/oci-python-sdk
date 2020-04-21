# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Item(object):
    """
    Details of Item
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Item object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cims.models.LimitItem`
        * :class:`~oci.cims.models.TechSupportItem`
        * :class:`~oci.cims.models.ActivityItem`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param item_key:
            The value to assign to the item_key property of this Item.
        :type item_key: str

        :param name:
            The value to assign to the name property of this Item.
        :type name: str

        :param type:
            The value to assign to the type property of this Item.
        :type type: str

        :param category:
            The value to assign to the category property of this Item.
        :type category: Category

        :param sub_category:
            The value to assign to the sub_category property of this Item.
        :type sub_category: SubCategory

        :param issue_type:
            The value to assign to the issue_type property of this Item.
        :type issue_type: IssueType

        """
        self.swagger_types = {
            'item_key': 'str',
            'name': 'str',
            'type': 'str',
            'category': 'Category',
            'sub_category': 'SubCategory',
            'issue_type': 'IssueType'
        }

        self.attribute_map = {
            'item_key': 'itemKey',
            'name': 'name',
            'type': 'type',
            'category': 'category',
            'sub_category': 'subCategory',
            'issue_type': 'issueType'
        }

        self._item_key = None
        self._name = None
        self._type = None
        self._category = None
        self._sub_category = None
        self._issue_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'limit':
            return 'LimitItem'

        if type == 'tech':
            return 'TechSupportItem'

        if type == 'activity':
            return 'ActivityItem'
        else:
            return 'Item'

    @property
    def item_key(self):
        """
        **[Required]** Gets the item_key of this Item.
        Unique ID that identifies an Item


        :return: The item_key of this Item.
        :rtype: str
        """
        return self._item_key

    @item_key.setter
    def item_key(self, item_key):
        """
        Sets the item_key of this Item.
        Unique ID that identifies an Item


        :param item_key: The item_key of this Item.
        :type: str
        """
        self._item_key = item_key

    @property
    def name(self):
        """
        Gets the name of this Item.
        Name of item


        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Item.
        Name of item


        :param name: The name of this Item.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Item.
        Type of item. eg: ActivityItem, LimitItem


        :return: The type of this Item.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Item.
        Type of item. eg: ActivityItem, LimitItem


        :param type: The type of this Item.
        :type: str
        """
        self._type = type

    @property
    def category(self):
        """
        Gets the category of this Item.

        :return: The category of this Item.
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Item.

        :param category: The category of this Item.
        :type: Category
        """
        self._category = category

    @property
    def sub_category(self):
        """
        Gets the sub_category of this Item.

        :return: The sub_category of this Item.
        :rtype: SubCategory
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """
        Sets the sub_category of this Item.

        :param sub_category: The sub_category of this Item.
        :type: SubCategory
        """
        self._sub_category = sub_category

    @property
    def issue_type(self):
        """
        Gets the issue_type of this Item.

        :return: The issue_type of this Item.
        :rtype: IssueType
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        """
        Sets the issue_type of this Item.

        :param issue_type: The issue_type of this Item.
        :type: IssueType
        """
        self._issue_type = issue_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
