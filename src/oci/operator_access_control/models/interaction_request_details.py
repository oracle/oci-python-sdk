# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InteractionRequestDetails(object):
    """
    Details for asking to provide more information to operators.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InteractionRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param more_info_details:
            The value to assign to the more_info_details property of this InteractionRequestDetails.
        :type more_info_details: str

        """
        self.swagger_types = {
            'more_info_details': 'str'
        }

        self.attribute_map = {
            'more_info_details': 'moreInfoDetails'
        }

        self._more_info_details = None

    @property
    def more_info_details(self):
        """
        Gets the more_info_details of this InteractionRequestDetails.
        questions for asking to provide more information to operators.


        :return: The more_info_details of this InteractionRequestDetails.
        :rtype: str
        """
        return self._more_info_details

    @more_info_details.setter
    def more_info_details(self, more_info_details):
        """
        Sets the more_info_details of this InteractionRequestDetails.
        questions for asking to provide more information to operators.


        :param more_info_details: The more_info_details of this InteractionRequestDetails.
        :type: str
        """
        self._more_info_details = more_info_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
