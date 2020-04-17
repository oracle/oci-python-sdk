# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateItemDetails(object):
    """
    Details of Item
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateItemDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.cims.models.CreateTechSupportItemDetails`
        * :class:`~oci.cims.models.CreateLimitItemDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateItemDetails.
        :type type: str

        :param category:
            The value to assign to the category property of this CreateItemDetails.
        :type category: CreateCategoryDetails

        :param sub_category:
            The value to assign to the sub_category property of this CreateItemDetails.
        :type sub_category: CreateSubCategoryDetails

        :param issue_type:
            The value to assign to the issue_type property of this CreateItemDetails.
        :type issue_type: CreateIssueTypeDetails

        :param name:
            The value to assign to the name property of this CreateItemDetails.
        :type name: str

        """
        self.swagger_types = {
            'type': 'str',
            'category': 'CreateCategoryDetails',
            'sub_category': 'CreateSubCategoryDetails',
            'issue_type': 'CreateIssueTypeDetails',
            'name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'category': 'category',
            'sub_category': 'subCategory',
            'issue_type': 'issueType',
            'name': 'name'
        }

        self._type = None
        self._category = None
        self._sub_category = None
        self._issue_type = None
        self._name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'tech':
            return 'CreateTechSupportItemDetails'

        if type == 'limit':
            return 'CreateLimitItemDetails'
        else:
            return 'CreateItemDetails'

    @property
    def type(self):
        """
        Gets the type of this CreateItemDetails.
        Type of item. eg: CreateTechSupportItemDetails, CreateLimitItemDetails


        :return: The type of this CreateItemDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateItemDetails.
        Type of item. eg: CreateTechSupportItemDetails, CreateLimitItemDetails


        :param type: The type of this CreateItemDetails.
        :type: str
        """
        self._type = type

    @property
    def category(self):
        """
        Gets the category of this CreateItemDetails.

        :return: The category of this CreateItemDetails.
        :rtype: CreateCategoryDetails
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this CreateItemDetails.

        :param category: The category of this CreateItemDetails.
        :type: CreateCategoryDetails
        """
        self._category = category

    @property
    def sub_category(self):
        """
        Gets the sub_category of this CreateItemDetails.

        :return: The sub_category of this CreateItemDetails.
        :rtype: CreateSubCategoryDetails
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        """
        Sets the sub_category of this CreateItemDetails.

        :param sub_category: The sub_category of this CreateItemDetails.
        :type: CreateSubCategoryDetails
        """
        self._sub_category = sub_category

    @property
    def issue_type(self):
        """
        Gets the issue_type of this CreateItemDetails.

        :return: The issue_type of this CreateItemDetails.
        :rtype: CreateIssueTypeDetails
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        """
        Sets the issue_type of this CreateItemDetails.

        :param issue_type: The issue_type of this CreateItemDetails.
        :type: CreateIssueTypeDetails
        """
        self._issue_type = issue_type

    @property
    def name(self):
        """
        Gets the name of this CreateItemDetails.
        Name of the item


        :return: The name of this CreateItemDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateItemDetails.
        Name of the item


        :param name: The name of this CreateItemDetails.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
