# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_item_details import CreateItemDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLimitItemDetails(CreateItemDetails):
    """
    Details of Limit Item
    """

    #: A constant which can be used with the limit_status property of a CreateLimitItemDetails.
    #: This constant has a value of "APPROVED"
    LIMIT_STATUS_APPROVED = "APPROVED"

    #: A constant which can be used with the limit_status property of a CreateLimitItemDetails.
    #: This constant has a value of "PARTIALLY_APPROVED"
    LIMIT_STATUS_PARTIALLY_APPROVED = "PARTIALLY_APPROVED"

    #: A constant which can be used with the limit_status property of a CreateLimitItemDetails.
    #: This constant has a value of "NOT_APPROVED"
    LIMIT_STATUS_NOT_APPROVED = "NOT_APPROVED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLimitItemDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.cims.models.CreateLimitItemDetails.type` attribute
        of this class is ``limit`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this CreateLimitItemDetails.
        :type type: str

        :param category:
            The value to assign to the category property of this CreateLimitItemDetails.
        :type category: CreateCategoryDetails

        :param sub_category:
            The value to assign to the sub_category property of this CreateLimitItemDetails.
        :type sub_category: CreateSubCategoryDetails

        :param issue_type:
            The value to assign to the issue_type property of this CreateLimitItemDetails.
        :type issue_type: CreateIssueTypeDetails

        :param name:
            The value to assign to the name property of this CreateLimitItemDetails.
        :type name: str

        :param current_limit:
            The value to assign to the current_limit property of this CreateLimitItemDetails.
        :type current_limit: int

        :param current_usage:
            The value to assign to the current_usage property of this CreateLimitItemDetails.
        :type current_usage: int

        :param requested_limit:
            The value to assign to the requested_limit property of this CreateLimitItemDetails.
        :type requested_limit: int

        :param limit_status:
            The value to assign to the limit_status property of this CreateLimitItemDetails.
            Allowed values for this property are: "APPROVED", "PARTIALLY_APPROVED", "NOT_APPROVED"
        :type limit_status: str

        """
        self.swagger_types = {
            'type': 'str',
            'category': 'CreateCategoryDetails',
            'sub_category': 'CreateSubCategoryDetails',
            'issue_type': 'CreateIssueTypeDetails',
            'name': 'str',
            'current_limit': 'int',
            'current_usage': 'int',
            'requested_limit': 'int',
            'limit_status': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'category': 'category',
            'sub_category': 'subCategory',
            'issue_type': 'issueType',
            'name': 'name',
            'current_limit': 'currentLimit',
            'current_usage': 'currentUsage',
            'requested_limit': 'requestedLimit',
            'limit_status': 'limitStatus'
        }

        self._type = None
        self._category = None
        self._sub_category = None
        self._issue_type = None
        self._name = None
        self._current_limit = None
        self._current_usage = None
        self._requested_limit = None
        self._limit_status = None
        self._type = 'limit'

    @property
    def current_limit(self):
        """
        Gets the current_limit of this CreateLimitItemDetails.
        Current available limit of the resource


        :return: The current_limit of this CreateLimitItemDetails.
        :rtype: int
        """
        return self._current_limit

    @current_limit.setter
    def current_limit(self, current_limit):
        """
        Sets the current_limit of this CreateLimitItemDetails.
        Current available limit of the resource


        :param current_limit: The current_limit of this CreateLimitItemDetails.
        :type: int
        """
        self._current_limit = current_limit

    @property
    def current_usage(self):
        """
        Gets the current_usage of this CreateLimitItemDetails.
        Current used limit of the resource


        :return: The current_usage of this CreateLimitItemDetails.
        :rtype: int
        """
        return self._current_usage

    @current_usage.setter
    def current_usage(self, current_usage):
        """
        Sets the current_usage of this CreateLimitItemDetails.
        Current used limit of the resource


        :param current_usage: The current_usage of this CreateLimitItemDetails.
        :type: int
        """
        self._current_usage = current_usage

    @property
    def requested_limit(self):
        """
        Gets the requested_limit of this CreateLimitItemDetails.
        Requested limit for the resource


        :return: The requested_limit of this CreateLimitItemDetails.
        :rtype: int
        """
        return self._requested_limit

    @requested_limit.setter
    def requested_limit(self, requested_limit):
        """
        Sets the requested_limit of this CreateLimitItemDetails.
        Requested limit for the resource


        :param requested_limit: The requested_limit of this CreateLimitItemDetails.
        :type: int
        """
        self._requested_limit = requested_limit

    @property
    def limit_status(self):
        """
        Gets the limit_status of this CreateLimitItemDetails.
        Status of the Limit

        Allowed values for this property are: "APPROVED", "PARTIALLY_APPROVED", "NOT_APPROVED"


        :return: The limit_status of this CreateLimitItemDetails.
        :rtype: str
        """
        return self._limit_status

    @limit_status.setter
    def limit_status(self, limit_status):
        """
        Sets the limit_status of this CreateLimitItemDetails.
        Status of the Limit


        :param limit_status: The limit_status of this CreateLimitItemDetails.
        :type: str
        """
        allowed_values = ["APPROVED", "PARTIALLY_APPROVED", "NOT_APPROVED"]
        if not value_allowed_none_or_none_sentinel(limit_status, allowed_values):
            raise ValueError(
                "Invalid value for `limit_status`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._limit_status = limit_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
