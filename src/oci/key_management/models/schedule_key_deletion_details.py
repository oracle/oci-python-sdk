# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleKeyDeletionDetails(object):
    """
    Details for scheduling key deletion.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleKeyDeletionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this ScheduleKeyDeletionDetails.
        :type time_of_deletion: datetime

        """
        self.swagger_types = {
            'time_of_deletion': 'datetime'
        }

        self.attribute_map = {
            'time_of_deletion': 'timeOfDeletion'
        }

        self._time_of_deletion = None

    @property
    def time_of_deletion(self):
        """
        Gets the time_of_deletion of this ScheduleKeyDeletionDetails.
        An optional property to indicate when to delete the vault, expressed in
        `RFC 3339`__ timestamp format. The specified
        time must be between 7 and 30 days from when the request is received.
        If this property is missing, it will be set to 30 days from the time of the request
        by default.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this ScheduleKeyDeletionDetails.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this ScheduleKeyDeletionDetails.
        An optional property to indicate when to delete the vault, expressed in
        `RFC 3339`__ timestamp format. The specified
        time must be between 7 and 30 days from when the request is received.
        If this property is missing, it will be set to 30 days from the time of the request
        by default.

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this ScheduleKeyDeletionDetails.
        :type: datetime
        """
        self._time_of_deletion = time_of_deletion

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
