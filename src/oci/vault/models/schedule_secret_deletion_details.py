# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleSecretDeletionDetails(object):
    """
    Details for scheduling the deletion of the specified secret.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleSecretDeletionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_of_deletion:
            The value to assign to the time_of_deletion property of this ScheduleSecretDeletionDetails.
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
        Gets the time_of_deletion of this ScheduleSecretDeletionDetails.
        An optional property indicating when to delete the secret version, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_deletion of this ScheduleSecretDeletionDetails.
        :rtype: datetime
        """
        return self._time_of_deletion

    @time_of_deletion.setter
    def time_of_deletion(self, time_of_deletion):
        """
        Sets the time_of_deletion of this ScheduleSecretDeletionDetails.
        An optional property indicating when to delete the secret version, expressed in `RFC 3339`__ timestamp format.

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_deletion: The time_of_deletion of this ScheduleSecretDeletionDetails.
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
