# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestSummarizedApplicationsDetails(object):
    """
    The information to summarize the applications.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestSummarizedApplicationsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param idcs_open_id:
            The value to assign to the idcs_open_id property of this RequestSummarizedApplicationsDetails.
        :type idcs_open_id: str

        """
        self.swagger_types = {
            'idcs_open_id': 'str'
        }

        self.attribute_map = {
            'idcs_open_id': 'idcsOpenId'
        }

        self._idcs_open_id = None

    @property
    def idcs_open_id(self):
        """
        Gets the idcs_open_id of this RequestSummarizedApplicationsDetails.
        Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter


        :return: The idcs_open_id of this RequestSummarizedApplicationsDetails.
        :rtype: str
        """
        return self._idcs_open_id

    @idcs_open_id.setter
    def idcs_open_id(self, idcs_open_id):
        """
        Sets the idcs_open_id of this RequestSummarizedApplicationsDetails.
        Encrypted IDCS Open ID token. This is required for pre-UCPIS cloud accounts, but not UCPIS, hence not a required parameter


        :param idcs_open_id: The idcs_open_id of this RequestSummarizedApplicationsDetails.
        :type: str
        """
        self._idcs_open_id = idcs_open_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
