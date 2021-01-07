# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_item_details import CreateItemDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTechSupportItemDetails(CreateItemDetails):
    """
    Details about the issue that the technical support request relates to.

    **Caution:** Avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTechSupportItemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cims.models.CreateTechSupportItemDetails.type` attribute
        of this class is ``tech`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateTechSupportItemDetails.
        :type type: str

        :param category:
            The value to assign to the category property of this CreateTechSupportItemDetails.
        :type category: oci.cims.models.CreateCategoryDetails

        :param sub_category:
            The value to assign to the sub_category property of this CreateTechSupportItemDetails.
        :type sub_category: oci.cims.models.CreateSubCategoryDetails

        :param issue_type:
            The value to assign to the issue_type property of this CreateTechSupportItemDetails.
        :type issue_type: oci.cims.models.CreateIssueTypeDetails

        :param name:
            The value to assign to the name property of this CreateTechSupportItemDetails.
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
        self._type = 'tech'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
