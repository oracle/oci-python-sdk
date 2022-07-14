# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataMaskingActivitySummary(object):
    """
    Summary of the data masking activity.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataMaskingActivitySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DataMaskingActivitySummary.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataMaskingActivitySummary.
        :type lifecycle_state: str

        :param time_masking_start:
            The value to assign to the time_masking_start property of this DataMaskingActivitySummary.
        :type time_masking_start: datetime

        :param time_masking_finish:
            The value to assign to the time_masking_finish property of this DataMaskingActivitySummary.
        :type time_masking_finish: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'lifecycle_state': 'str',
            'time_masking_start': 'datetime',
            'time_masking_finish': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'time_masking_start': 'timeMaskingStart',
            'time_masking_finish': 'timeMaskingFinish'
        }

        self._id = None
        self._lifecycle_state = None
        self._time_masking_start = None
        self._time_masking_finish = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataMaskingActivitySummary.
        Unique identifier that is immutable on creation.


        :return: The id of this DataMaskingActivitySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataMaskingActivitySummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this DataMaskingActivitySummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DataMaskingActivitySummary.
        The current state of the data masking activity Scheduled, In progress , Failed, Completed


        :return: The lifecycle_state of this DataMaskingActivitySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataMaskingActivitySummary.
        The current state of the data masking activity Scheduled, In progress , Failed, Completed


        :param lifecycle_state: The lifecycle_state of this DataMaskingActivitySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_masking_start(self):
        """
        **[Required]** Gets the time_masking_start of this DataMaskingActivitySummary.
        The time the data masking activity started. An RFC3339 formatted datetime string.


        :return: The time_masking_start of this DataMaskingActivitySummary.
        :rtype: datetime
        """
        return self._time_masking_start

    @time_masking_start.setter
    def time_masking_start(self, time_masking_start):
        """
        Sets the time_masking_start of this DataMaskingActivitySummary.
        The time the data masking activity started. An RFC3339 formatted datetime string.


        :param time_masking_start: The time_masking_start of this DataMaskingActivitySummary.
        :type: datetime
        """
        self._time_masking_start = time_masking_start

    @property
    def time_masking_finish(self):
        """
        **[Required]** Gets the time_masking_finish of this DataMaskingActivitySummary.
        The time the data masking activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :return: The time_masking_finish of this DataMaskingActivitySummary.
        :rtype: datetime
        """
        return self._time_masking_finish

    @time_masking_finish.setter
    def time_masking_finish(self, time_masking_finish):
        """
        Sets the time_masking_finish of this DataMaskingActivitySummary.
        The time the data masking activity actually completed / cancelled / failed. An RFC3339 formatted datetime string.


        :param time_masking_finish: The time_masking_finish of this DataMaskingActivitySummary.
        :type: datetime
        """
        self._time_masking_finish = time_masking_finish

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
