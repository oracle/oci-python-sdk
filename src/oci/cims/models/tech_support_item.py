# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .item import Item
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TechSupportItem(Item):
    """
    Details about the TechSupportItem object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TechSupportItem object with values from keyword arguments. The default value of the :py:attr:`~oci.cims.models.TechSupportItem.type` attribute
        of this class is ``tech`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param item_key:
            The value to assign to the item_key property of this TechSupportItem.
        :type item_key: str

        :param name:
            The value to assign to the name property of this TechSupportItem.
        :type name: str

        :param type:
            The value to assign to the type property of this TechSupportItem.
        :type type: str

        :param category:
            The value to assign to the category property of this TechSupportItem.
        :type category: oci.cims.models.Category

        :param sub_category:
            The value to assign to the sub_category property of this TechSupportItem.
        :type sub_category: oci.cims.models.SubCategory

        :param issue_type:
            The value to assign to the issue_type property of this TechSupportItem.
        :type issue_type: oci.cims.models.IssueType

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
        self._type = 'tech'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
