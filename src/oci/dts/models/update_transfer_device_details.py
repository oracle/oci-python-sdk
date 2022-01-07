# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTransferDeviceDetails(object):
    """
    UpdateTransferDeviceDetails model.
    """

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferDeviceDetails.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferDeviceDetails.
    #: This constant has a value of "READY"
    LIFECYCLE_STATE_READY = "READY"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferDeviceDetails.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTransferDeviceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UpdateTransferDeviceDetails.
            Allowed values for this property are: "PREPARING", "READY", "CANCELLED"
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState'
        }

        self._lifecycle_state = None

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UpdateTransferDeviceDetails.
        Allowed values for this property are: "PREPARING", "READY", "CANCELLED"


        :return: The lifecycle_state of this UpdateTransferDeviceDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UpdateTransferDeviceDetails.

        :param lifecycle_state: The lifecycle_state of this UpdateTransferDeviceDetails.
        :type: str
        """
        allowed_values = ["PREPARING", "READY", "CANCELLED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
