# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CancellationDetails(object):
    """
    Defines the cancellation details of the job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CancellationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_forced:
            The value to assign to the is_forced property of this CancellationDetails.
        :type is_forced: bool

        """
        self.swagger_types = {
            'is_forced': 'bool'
        }

        self.attribute_map = {
            'is_forced': 'isForced'
        }

        self._is_forced = None

    @property
    def is_forced(self):
        """
        Gets the is_forced of this CancellationDetails.
        Indicates whether a forced cancellation was requested for the job while it was running.
        A forced cancellation can result in an incorrect state file.
        For example, the state file might not reflect the exact state of the provisioned resources.


        :return: The is_forced of this CancellationDetails.
        :rtype: bool
        """
        return self._is_forced

    @is_forced.setter
    def is_forced(self, is_forced):
        """
        Sets the is_forced of this CancellationDetails.
        Indicates whether a forced cancellation was requested for the job while it was running.
        A forced cancellation can result in an incorrect state file.
        For example, the state file might not reflect the exact state of the provisioned resources.


        :param is_forced: The is_forced of this CancellationDetails.
        :type: bool
        """
        self._is_forced = is_forced

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
