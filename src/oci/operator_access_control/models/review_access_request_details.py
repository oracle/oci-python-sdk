# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReviewAccessRequestDetails(object):
    """
    Details to mark access request in review.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReviewAccessRequestDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param approver_comment:
            The value to assign to the approver_comment property of this ReviewAccessRequestDetails.
        :type approver_comment: str

        """
        self.swagger_types = {
            'approver_comment': 'str'
        }

        self.attribute_map = {
            'approver_comment': 'approverComment'
        }

        self._approver_comment = None

    @property
    def approver_comment(self):
        """
        Gets the approver_comment of this ReviewAccessRequestDetails.
        Comment by the approver explaining that the access request is in review.


        :return: The approver_comment of this ReviewAccessRequestDetails.
        :rtype: str
        """
        return self._approver_comment

    @approver_comment.setter
    def approver_comment(self, approver_comment):
        """
        Sets the approver_comment of this ReviewAccessRequestDetails.
        Comment by the approver explaining that the access request is in review.


        :param approver_comment: The approver_comment of this ReviewAccessRequestDetails.
        :type: str
        """
        self._approver_comment = approver_comment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
