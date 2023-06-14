# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverBundleStatusDetails(object):
    """
    Information required to retrieve rover bundle status of a copyObject operation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverBundleStatusDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param work_request_id:
            The value to assign to the work_request_id property of this RoverBundleStatusDetails.
        :type work_request_id: str

        """
        self.swagger_types = {
            'work_request_id': 'str'
        }

        self.attribute_map = {
            'work_request_id': 'workRequestId'
        }

        self._work_request_id = None

    @property
    def work_request_id(self):
        """
        **[Required]** Gets the work_request_id of this RoverBundleStatusDetails.
        The workRequestId for an async copyObject operation.


        :return: The work_request_id of this RoverBundleStatusDetails.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this RoverBundleStatusDetails.
        The workRequestId for an async copyObject operation.


        :param work_request_id: The work_request_id of this RoverBundleStatusDetails.
        :type: str
        """
        self._work_request_id = work_request_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
