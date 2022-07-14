# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataMaskingActivity(object):
    """
    Details of data masking activity.
    """

    #: A constant which can be used with the lifecycle_state property of a DataMaskingActivity.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a DataMaskingActivity.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a DataMaskingActivity.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DataMaskingActivity.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a DataMaskingActivity.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new DataMaskingActivity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DataMaskingActivity.
        :type id: str

        :param fusion_environment_id:
            The value to assign to the fusion_environment_id property of this DataMaskingActivity.
        :type fusion_environment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataMaskingActivity.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_masking_start:
            The value to assign to the time_masking_start property of this DataMaskingActivity.
        :type time_masking_start: datetime

        :param time_masking_finish:
            The value to assign to the time_masking_finish property of this DataMaskingActivity.
        :type time_masking_finish: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'fusion_environment_id': 'str',
            'lifecycle_state': 'str',
            'time_masking_start': 'datetime',
            'time_masking_finish': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'fusion_environment_id': 'fusionEnvironmentId',
            'lifecycle_state': 'lifecycleState',
            'time_masking_start': 'timeMaskingStart',
            'time_masking_finish': 'timeMaskingFinish'
        }

        self._id = None
        self._fusion_environment_id = None
        self._lifecycle_state = None
        self._time_masking_start = None
        self._time_masking_finish = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataMaskingActivity.
        Unique identifier that is immutable on creation.


        :return: The id of this DataMaskingActivity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataMaskingActivity.
        Unique identifier that is immutable on creation.


        :param id: The id of this DataMaskingActivity.
        :type: str
        """
        self._id = id

    @property
    def fusion_environment_id(self):
        """
        **[Required]** Gets the fusion_environment_id of this DataMaskingActivity.
        Fusion Environment Identifier.


        :return: The fusion_environment_id of this DataMaskingActivity.
        :rtype: str
        """
        return self._fusion_environment_id

    @fusion_environment_id.setter
    def fusion_environment_id(self, fusion_environment_id):
        """
        Sets the fusion_environment_id of this DataMaskingActivity.
        Fusion Environment Identifier.


        :param fusion_environment_id: The fusion_environment_id of this DataMaskingActivity.
        :type: str
        """
        self._fusion_environment_id = fusion_environment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DataMaskingActivity.
        The current state of the DataMaskingActivity.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataMaskingActivity.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataMaskingActivity.
        The current state of the DataMaskingActivity.


        :param lifecycle_state: The lifecycle_state of this DataMaskingActivity.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_masking_start(self):
        """
        **[Required]** Gets the time_masking_start of this DataMaskingActivity.
        The time the data masking activity started. An RFC3339 formatted datetime string.


        :return: The time_masking_start of this DataMaskingActivity.
        :rtype: datetime
        """
        return self._time_masking_start

    @time_masking_start.setter
    def time_masking_start(self, time_masking_start):
        """
        Sets the time_masking_start of this DataMaskingActivity.
        The time the data masking activity started. An RFC3339 formatted datetime string.


        :param time_masking_start: The time_masking_start of this DataMaskingActivity.
        :type: datetime
        """
        self._time_masking_start = time_masking_start

    @property
    def time_masking_finish(self):
        """
        **[Required]** Gets the time_masking_finish of this DataMaskingActivity.
        The time the data masking activity ended. An RFC3339 formatted datetime string.


        :return: The time_masking_finish of this DataMaskingActivity.
        :rtype: datetime
        """
        return self._time_masking_finish

    @time_masking_finish.setter
    def time_masking_finish(self, time_masking_finish):
        """
        Sets the time_masking_finish of this DataMaskingActivity.
        The time the data masking activity ended. An RFC3339 formatted datetime string.


        :param time_masking_finish: The time_masking_finish of this DataMaskingActivity.
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
