# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WorkRequests(object):
    """
    Logical grouping used for Operations Insights Work Request operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WorkRequests object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param work_requests:
            The value to assign to the work_requests property of this WorkRequests.
        :type work_requests: object

        """
        self.swagger_types = {
            'work_requests': 'object'
        }

        self.attribute_map = {
            'work_requests': 'workRequests'
        }

        self._work_requests = None

    @property
    def work_requests(self):
        """
        Gets the work_requests of this WorkRequests.
        OPSI Work Request Object.


        :return: The work_requests of this WorkRequests.
        :rtype: object
        """
        return self._work_requests

    @work_requests.setter
    def work_requests(self, work_requests):
        """
        Sets the work_requests of this WorkRequests.
        OPSI Work Request Object.


        :param work_requests: The work_requests of this WorkRequests.
        :type: object
        """
        self._work_requests = work_requests

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
