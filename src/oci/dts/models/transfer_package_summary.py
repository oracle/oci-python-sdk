# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferPackageSummary(object):
    """
    TransferPackageSummary model.
    """

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "SHIPPING"
    LIFECYCLE_STATE_SHIPPING = "SHIPPING"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "RECEIVED"
    LIFECYCLE_STATE_RECEIVED = "RECEIVED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "PROCESSING"
    LIFECYCLE_STATE_PROCESSING = "PROCESSING"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "PROCESSED"
    LIFECYCLE_STATE_PROCESSED = "PROCESSED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "RETURNED"
    LIFECYCLE_STATE_RETURNED = "RETURNED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackageSummary.
    #: This constant has a value of "CANCELLED_RETURNED"
    LIFECYCLE_STATE_CANCELLED_RETURNED = "CANCELLED_RETURNED"

    def __init__(self, **kwargs):
        """
        Initializes a new TransferPackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this TransferPackageSummary.
        :type label: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TransferPackageSummary.
            Allowed values for this property are: "PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param creation_time:
            The value to assign to the creation_time property of this TransferPackageSummary.
        :type creation_time: datetime

        """
        self.swagger_types = {
            'label': 'str',
            'lifecycle_state': 'str',
            'creation_time': 'datetime'
        }

        self.attribute_map = {
            'label': 'label',
            'lifecycle_state': 'lifecycleState',
            'creation_time': 'creationTime'
        }

        self._label = None
        self._lifecycle_state = None
        self._creation_time = None

    @property
    def label(self):
        """
        Gets the label of this TransferPackageSummary.

        :return: The label of this TransferPackageSummary.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this TransferPackageSummary.

        :param label: The label of this TransferPackageSummary.
        :type: str
        """
        self._label = label

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TransferPackageSummary.
        Allowed values for this property are: "PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TransferPackageSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TransferPackageSummary.

        :param lifecycle_state: The lifecycle_state of this TransferPackageSummary.
        :type: str
        """
        allowed_values = ["PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TransferPackageSummary.

        :return: The creation_time of this TransferPackageSummary.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TransferPackageSummary.

        :param creation_time: The creation_time of this TransferPackageSummary.
        :type: datetime
        """
        self._creation_time = creation_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
