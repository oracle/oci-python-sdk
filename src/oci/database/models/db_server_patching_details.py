# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbServerPatchingDetails(object):
    """
    The scheduling details for the quarterly maintenance window. Patching and system updates take place during the maintenance window.
    """

    #: A constant which can be used with the patching_status property of a DbServerPatchingDetails.
    #: This constant has a value of "SCHEDULED"
    PATCHING_STATUS_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the patching_status property of a DbServerPatchingDetails.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    PATCHING_STATUS_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the patching_status property of a DbServerPatchingDetails.
    #: This constant has a value of "FAILED"
    PATCHING_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the patching_status property of a DbServerPatchingDetails.
    #: This constant has a value of "COMPLETE"
    PATCHING_STATUS_COMPLETE = "COMPLETE"

    def __init__(self, **kwargs):
        """
        Initializes a new DbServerPatchingDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param estimated_patch_duration:
            The value to assign to the estimated_patch_duration property of this DbServerPatchingDetails.
        :type estimated_patch_duration: int

        :param patching_status:
            The value to assign to the patching_status property of this DbServerPatchingDetails.
            Allowed values for this property are: "SCHEDULED", "MAINTENANCE_IN_PROGRESS", "FAILED", "COMPLETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type patching_status: str

        :param time_patching_started:
            The value to assign to the time_patching_started property of this DbServerPatchingDetails.
        :type time_patching_started: datetime

        :param time_patching_ended:
            The value to assign to the time_patching_ended property of this DbServerPatchingDetails.
        :type time_patching_ended: datetime

        """
        self.swagger_types = {
            'estimated_patch_duration': 'int',
            'patching_status': 'str',
            'time_patching_started': 'datetime',
            'time_patching_ended': 'datetime'
        }

        self.attribute_map = {
            'estimated_patch_duration': 'estimatedPatchDuration',
            'patching_status': 'patchingStatus',
            'time_patching_started': 'timePatchingStarted',
            'time_patching_ended': 'timePatchingEnded'
        }

        self._estimated_patch_duration = None
        self._patching_status = None
        self._time_patching_started = None
        self._time_patching_ended = None

    @property
    def estimated_patch_duration(self):
        """
        Gets the estimated_patch_duration of this DbServerPatchingDetails.
        Estimated time, in minutes, to patch one database server.


        :return: The estimated_patch_duration of this DbServerPatchingDetails.
        :rtype: int
        """
        return self._estimated_patch_duration

    @estimated_patch_duration.setter
    def estimated_patch_duration(self, estimated_patch_duration):
        """
        Sets the estimated_patch_duration of this DbServerPatchingDetails.
        Estimated time, in minutes, to patch one database server.


        :param estimated_patch_duration: The estimated_patch_duration of this DbServerPatchingDetails.
        :type: int
        """
        self._estimated_patch_duration = estimated_patch_duration

    @property
    def patching_status(self):
        """
        Gets the patching_status of this DbServerPatchingDetails.
        The status of the patching operation.

        Allowed values for this property are: "SCHEDULED", "MAINTENANCE_IN_PROGRESS", "FAILED", "COMPLETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The patching_status of this DbServerPatchingDetails.
        :rtype: str
        """
        return self._patching_status

    @patching_status.setter
    def patching_status(self, patching_status):
        """
        Sets the patching_status of this DbServerPatchingDetails.
        The status of the patching operation.


        :param patching_status: The patching_status of this DbServerPatchingDetails.
        :type: str
        """
        allowed_values = ["SCHEDULED", "MAINTENANCE_IN_PROGRESS", "FAILED", "COMPLETE"]
        if not value_allowed_none_or_none_sentinel(patching_status, allowed_values):
            patching_status = 'UNKNOWN_ENUM_VALUE'
        self._patching_status = patching_status

    @property
    def time_patching_started(self):
        """
        Gets the time_patching_started of this DbServerPatchingDetails.
        The time when the patching operation started.


        :return: The time_patching_started of this DbServerPatchingDetails.
        :rtype: datetime
        """
        return self._time_patching_started

    @time_patching_started.setter
    def time_patching_started(self, time_patching_started):
        """
        Sets the time_patching_started of this DbServerPatchingDetails.
        The time when the patching operation started.


        :param time_patching_started: The time_patching_started of this DbServerPatchingDetails.
        :type: datetime
        """
        self._time_patching_started = time_patching_started

    @property
    def time_patching_ended(self):
        """
        Gets the time_patching_ended of this DbServerPatchingDetails.
        The time when the patching operation ended.


        :return: The time_patching_ended of this DbServerPatchingDetails.
        :rtype: datetime
        """
        return self._time_patching_ended

    @time_patching_ended.setter
    def time_patching_ended(self, time_patching_ended):
        """
        Sets the time_patching_ended of this DbServerPatchingDetails.
        The time when the patching operation ended.


        :param time_patching_ended: The time_patching_ended of this DbServerPatchingDetails.
        :type: datetime
        """
        self._time_patching_ended = time_patching_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
